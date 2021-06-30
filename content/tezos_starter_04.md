## 4.1 The smart contract of the Token Shop
In this section, we will build a very simple shop where users can buy various tokens. We will store the amount of tokens we have in stock as well as their price.

Let's start with defining some types. 

```
type token_supply = { current_stock : nat ; token_price : tez }
type token_shop_storage = (nat, token_supply) map
type return = operation list * token_shop_storage
```
First, we define the type `token_supply` which is a record with two fields `current_stock` which is a nat, since our stock can’t get negative, and `token_price` which is a tez.

We then create a type `token_shop_storage` which maps an index, a nat, to our token_supply record. Like this, we can keep track of the supply of the various tokens in stock.

The last type we are going to define is a return type for our main function which consists of a tuple of operation list and the storage. This should look familiar by now.

```
let ownerAddress : address =
  ("tz1TGu6TN5GSez2ndXXeDX6LgUDvLzPLqgYV" : address)
```
We are also storing an address to which we will pay out the earnings of the token sales.

```
let main (token_kind_index, token_shop_storage : nat * token_shop_storage) : return =
```
In the main function, we have as a parameter a tuple of the token index and the storage.

```
  let token_kind : token_supply =
    match Map.find_opt (token_kind_index) token_shop_storage with
    | Some k -> k
    | None -> (failwith "Unknown kind of token" : token_supply)
  in
```
Now we want to retrieve the record of the token index that was passed in the main function, we do this with the `map.find_opt`. We use pattern matching to account for the case that there is no record with this index stored in our map.

```
  let () = if Tezos.amount <> token_kind.token_price then
    failwith "Sorry, the token you are trying to purchase has a different price"
  in
```
We need to check if the amount the user sends with their transaction is equal to the price of the token, if not the transaction fails with an error message.

```
 let () = if token_kind.current_stock = 0n then
    failwith "Sorry, the token you are trying to purchase is out of stock"
  in
```
We need to check if the amount the user sends with their transaction is equal to the price of the token, if not the transaction fails with an error message.

```
  let () = if token_kind.current_stock = 0n then
    failwith "Sorry, the token you are trying to purchase is out of stock"
  in
```
We also need to check if there are still tokens left, if not then we also fail the transaction with an error message.

```
  let token_shop_storage = Map.update
    token_kind_index
    (Some { token_kind with current_stock = abs (token_kind.current_stock - 1n) })
    token_shop_storage
  in
```
Now we want to decrease the `current_stock` field in the record of the token the user wants to purchase. We use `Map.update` and specify the index of the token and pass the new `current_stock` value, decreasing it by one. We use `abs` to get a nat from our subtraction. And we need to specify the map we want to update, our `token_shop_storage` of course.

For the last part of our contract, we are going to send the tokens from the purchase to the owner address that we specified at the beginning of the contract.

```
  let receiver : unit contract =
    match (Tezos.get_contract_opt ownerAddress : unit contract option) with
    | Some (contract) -> contract
    | None -> (failwith ("Not a contract") : (unit contract))
  in
```

We need to create the receiver address and wrap it as a contract unit that represents an account so that we can send it the tokens. But first, we need to check if the account exists. If it doesn’t we fail the transaction with an error message.

```
  let payoutOperation : operation = 
    Tezos.transaction unit amount receiver 
  in
  let operations : operation list = 
    [payoutOperation] 
  in
  ((operations: operation list), token_shop_storage)
```
We will create a transaction to an account and not a contract so we will use unit as the first parameter and then pass the amount and the receiver address.
We need to create a list of operations that we will return at the end of the contract, which in this case will be just one, and then return the list at the end of the contract as well as our updated `token_shop_storage` storage.

You can now deploy this contract via the CLI or in the [LIGOlang IDE](https://ide.ligolang.org/p/N3D8IeExpI9AeQel39bkuw).
Storage example: `Map.literal [
 (1n, { current_stock = 20n ; token_price = 2tez }) ;
 (2n, { current_stock = 4n ; token_price = 3tez }) ;
]`

## 4.2 Adding the FA2 functionality to the Token Shop (WIP)

### FA2 Implementation (WIP)

// Currently we are using this working FA2 implementation by Philipp and John but not sure if this implementation is complient. We need feedback if we can use this and or help to creat a complient version for an fungible as well as non-fungible token.

```
type token_id = nat

type transfer_destination =
[@layout:comb]
{
  to_      : address;
  token_id : token_id;
  amount   : nat;
}

type transfer =
[@layout:comb]
{
  from_ : address;
  txs   : transfer_destination list;
 }

type balance_of_request =
[@layout:comb]
{
  owner    : address;
  token_id : token_id;
}

type balance_of_response =
[@layout:comb]
{
  request : balance_of_request;
  balance : nat;
}

type balance_of_param =
[@layout:comb]
{
  requests : balance_of_request list;
  callback : balance_of_response list contract;
}

type operator_param =
[@layout:comb]
{
  owner : address;
  operator : address;
  token_id : token_id;
}

type update_operator =
[@layout:comb]
| Add_operator     of operator_param
| Remove_operator  of operator_param

type entrypoint =
[@layout:comb]
| Transfer                of transfer list
| Balance_of              of balance_of_param
| Update_operators        of update_operator list

// (owner * (operator * token_id))
type operator_storage = ((address * (address * token_id)), unit) big_map

type token_metadata = (nat, (nat * (string,bytes) map )) big_map

type storage =
[@layout:comb]
{
  ledger         : ((address * token_id), nat) big_map;
  operators      : operator_storage;
  token_metadata : token_metadata;
}

let not_operator: string         = "FA2_NOT_OPERATOR"
let not_owner: string            = "FA2_NOT_OWNER"
let insufficient_balance: string = "FA2_INSUFFICIENT_BALANCE"
let token_undefined: string      = "FA2_TOKEN_UNDEFINED"

// Check if the operator exists in storage.operator
let default_operator_validator (owner, operator, token_id, operator_storage :
                                address * address * token_id * operator_storage) : unit =
    if owner <> operator then
      match (Big_map.find_opt (owner, (operator, token_id)) operator_storage) with
        | Some(_nothing) -> unit
        | None           -> ( failwith not_operator )


// perform a single transfer for a give from_ address and transfer_destination
let transfer_tx (from_, transfer_destination, storage:
                address * transfer_destination * storage) : storage =
   // check that the operator has permission to transfer the owner's tokens
   let _ = default_operator_validator (from_, sender, transfer_destination.token_id, storage.operators) in

   if transfer_destination.token_id <> 0n then
     ( failwith token_undefined : storage )
   else
     match (Big_map.find_opt (from_, transfer_destination.token_id) storage.ledger) with
       | None -> ( failwith insufficient_balance : storage)
       | Some(from_balance) ->
           if from_balance < transfer_destination.amount then
             (failwith insufficient_balance : storage)
           else
             // subtract transferred amount from the from_ address balance
             let new_ledger =
               Big_map.update (from_, transfer_destination.token_id) (Some (abs (from_balance - transfer_destination.amount))) storage.ledger
             in
             // get the to_ address balance
             let to_balance: nat =
             match (Big_map.find_opt (transfer_destination.to_, transfer_destination.token_id) storage.ledger) with
               | Some(to_balance_) -> to_balance_
               | None   -> 0n
             in
             // add transferred amount to the to_ address balance
             let new_ledger =
               Big_map.update (transfer_destination.to_, transfer_destination.token_id) ( Some (to_balance + transfer_destination.amount) ) new_ledger
             in
             { storage with ledger = new_ledger }


// validate the operator than execute the transactions
let transfer_txs (transfer, storage : transfer * storage) : storage =
  let exec (storage, transfer_destination : storage * transfer_destination) : storage =
    transfer_tx (transfer.from_, transfer_destination, storage)
  in
  List.fold exec transfer.txs storage




// Transfer entrypoint function
let transfer (transfers, storage : transfer list * storage ) : storage =
   let exec (storage, transfer: storage * transfer) : storage = 
    transfer_txs (transfer, storage)
   in
   List.fold exec transfers storage

// Balance_of entrypoint function
let balance_of (balance_of_param, storage : balance_of_param * storage) : (operation list * storage) =
   // convert each balance_of
   let to_balance(balance_of_request : balance_of_request) : balance_of_response =
       if (balance_of_request.token_id <> 0n) then
        ( failwith token_undefined : balance_of_response)
       else
         let owner_balance = match Big_map.find_opt (balance_of_request.owner, balance_of_request.token_id) storage.ledger with
           | Some(owner_balance_) -> owner_balance_
           | None                 -> 0n
         in
         { request = balance_of_request; balance = owner_balance }
   in
   let balances = List.map to_balance balance_of_param.requests in
   let operations = [Tezos.transaction balances Tezos.amount balance_of_param.callback] in
   (operations, storage)

// Update_operators entrypoint function

let update_operators (update_operators, storage : update_operator list * storage) : storage =
  let update_operator (storage, update_operator : storage * update_operator) : storage =
      let new_operators = match update_operator with
        | Add_operator(operator_param) ->
            if sender <> operator_param.owner then
              ( failwith not_owner :  operator_storage )
            else
              Big_map.update (operator_param.owner, (operator_param.operator, operator_param.token_id)) (Some unit) storage.operators
        | Remove_operator(operator_param) ->
            if sender <> operator_param.owner then
              ( failwith not_owner : operator_storage)
            else
              Big_map.remove (operator_param.owner, (operator_param.operator, operator_param.token_id)) storage.operators
      in
      { storage with operators = new_operators }
  in
  List.fold update_operator update_operators storage

let main (entrypoint, storage : entrypoint * storage) : (operation list * storage) =
  match entrypoint with
  | Transfer(transfers)          -> (([] : operation list), transfer (transfers, storage))
  | Balance_of(balance_of_param) -> balance_of (balance_of_param, storage)
  | Update_operators(xs)         -> (([] : operation list), update_operators (xs, storage))

```


### Token Shop with FA2 (WIP)
// Here we need feedback if we are on the right way and we need to adapt it to sell multiple fungible tokens and  NFTs. Would be great to get help with that to make sure we are building it the right way.

```
type token_supply = {
  current_stock : nat;
  price : tez
}

type token_shop_storage = (
  nat,
  token_supply
) map

type return = operation list * token_shop_storage

let err_INVALID_TOKEN_CONTRACT = "Invalid external token contract"

type token_id = nat

type transfer_details =
[@layout:comb]
{
  [@annot:to_] dst : address;
  token_id : token_id;
  amount : nat;
}

type fa2_batch_transfer =
[@layout:comb]
{
  [@annot:from_] src : address;
  txs : transfer_details list;
}

let get_fa2_transfer_entrypoint ( token_address : address ) : fa2_batch_transfer list contract =
  match ( Tezos.get_entrypoint_opt "%transfer" token_address : fa2_batch_transfer list contract option ) with
  | None -> ( failwith err_INVALID_TOKEN_CONTRACT : fa2_batch_transfer list contract )
  | Some e -> e

type fa2_token_identifier =
[@layout:comb]
{
  token_address : address;
  token_id : token_id;
}

type transfer_addresses =
[@layout:comb]
{
  src : address;
  dst : address;
}

let ownerAddress : address =
  ("tz1RknyQQoKrHcpEG8QtSU1VP1KZu6tx42P2" : address)

let tokenaddress : address =
  ("KT19v4on9GyE1ymuwSUt8CT63CJXF7oUxq2E" : address)

let get_fa2_transfer_op ( transfer_addresses, fa2_token_identifier, token_amount : transfer_addresses * fa2_token_identifier * nat ) : operation =
  let args : fa2_batch_transfer = {
    src = transfer_addresses.src;
    txs = [ {
      dst = transfer_addresses.dst;
      token_id = fa2_token_identifier.token_id;
      amount = token_amount;
    } ];
  } in
  let entrypoint = get_fa2_transfer_entrypoint fa2_token_identifier.token_address in
  Tezos.transaction [args] 0mutez entrypoint

let buy_token (token_kind_index, token_shop_storage : nat * token_shop_storage) : return =
  let token_kind : token_supply =
    match Map.find_opt (token_kind_index) token_shop_storage with
    | Some k -> k
    | None -> (failwith "Unknown kind of token" : token_supply)
  in

  let _ = if Tezos.amount < token_kind.price then
    failwith "Sorry, the token you are trying to purchase has a different price"
  in

  let token_shop_storage = Map.update
    token_kind_index
    (Some { token_kind with current_stock = abs (token_kind.current_stock - 1n) })
    token_shop_storage
  in

  let receiver : unit contract =
    match (Tezos.get_contract_opt ownerAddress : unit contract option) with
    | Some (contract) -> contract
    | None -> (failwith ("Not a contract") : (unit contract))
  in

  let payoutOperation : operation =
    Tezos.transaction unit Tezos.amount receiver
  in
  let op = get_fa2_transfer_op (
    {
      src = Tezos.self_address;
      dst = Tezos.sender
    },
    {
      token_address = tokenaddress;
      token_id = 0n;
    },
    1000000n
  ) in

  let operations : operation list =
    [payoutOperation; op]
  in

  ((operations : operation list), token_shop_storage)
```


## 4.3 Debugging our contract (WIP)

// We will show how to test this contract in better-call.dev. This will be easy to do. We will include GIFs.


## 4.4 The front end for the Token Shop (WIP)

// We already created a test front end that is working for the current work in progress version but would adapt it to a new version. There will be just very minimal changes made to the Boilerplate to just add basic functionality and strip it from unneeded functionality.

```
 const buy_token = async (): Promise<void> => {
    setLoading(true);
    try {
      const op = await contract.methods.default(1).send({ amount: 2 });
      await op.confirmation();
      const newStorage: any = await contract.storage();
      if (newStorage) setStorage(newStorage);
      setUserBalance(await Tezos.tz.getBalance(userAddress));
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  if (!contract && !userAddress) return <div>&nbsp;</div>;
  return (
    <div className="buttons">
      <button className="button" disabled={loading} onClick={buy_token}>
        {loading ? (
          <span>
            <i className="fas fa-spinner fa-spin"></i>&nbsp; Please wait
          </span>
        ) : (
          <span>
            <i className="fas fa-plus"></i>&nbsp; Buy Taco
          </span>
        )}
      </button>
    </div>
  );
};
```
