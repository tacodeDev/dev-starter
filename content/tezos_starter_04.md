## 4.1 Shop Contract
In this section, we will build a very simple shop where users can buy various tokens. We will store the amount of tokens we have in stock as well as each token’s price.

Let's start with defining some types. 

```
type token_supply = { current_stock : nat ; token_price : tez }
type token_shop_storage = (nat, token_supply) map
type return = operation list * token_shop_storage
```
First, we define the type `token_supply`, which is a record with two fields: `current_stock` which is a nat since our stock can’t become negative, and `token_price` which is a tez.

We then create a type `token_shop_storage`, which maps an index, a nat, to our token_supply record. Like this, we can keep track of the supply of the various tokens in stock.

The last type we will define is a return type for our main function, which consists of a tuple of operation list and the storage. This should look familiar by now.

```
let owner_address : address =
  ("tz1TGu6TN5GSez2ndXXeDX6LgUDvLzPLqgYV" : address)
```
We are also storing an address to which we will pay out the earnings of the token sales.

```
let main (token_kind_index, token_shop_storage : nat * token_shop_storage) : return =
```
In the main function, we have a tuple of the token index and the storage as parameters.

```
  let token_kind : token_supply =
    match Map.find_opt (token_kind_index) token_shop_storage with
    | Some k -> k
    | None -> (failwith "Unknown kind of token" : token_supply)
  in
```
Now, we want to retrieve the record of the token index that was passed in the main function; we do this with the `map.find_opt`. We use pattern matching to account for the case that there is no record with this index stored in our map.

```
  let () = if Tezos.amount <> token_kind.token_price then
    failwith "Sorry, the token you are trying to purchase has a different price"
  in
```
We need to check if the amount the user sends with their transaction is equal to the token price. If not, the transaction fails with an error message.

```
 let () = if token_kind.current_stock = 0n then
    failwith "Sorry, the token you are trying to purchase is out of stock"
  in
```
We also need to check if there are still tokens left. If not, then we also fail the transaction with an error message.

```
  let token_shop_storage = Map.update
    token_kind_index
    (Some { token_kind with current_stock = abs (token_kind.current_stock - 1n) })
    token_shop_storage
  in
```
Now, we want to decrease the `current_stock` field in the record of the token the user wants to purchase. We use `Map.update` and specify the index of the token and pass the new `current_stock` value, decreasing it by one. We use `abs` to get a nat from our subtraction. And we need to specify the map we want to update, our `token_shop_storage` of course.

For the last part of our contract, we will send the tokens from the purchase to the owner’s address that we specified at the beginning of the contract.

```
  let receiver : unit contract =
    match (Tezos.get_contract_opt owner_address : unit contract option) with
    | Some (contract) -> contract
    | None -> (failwith ("Not a contract") : (unit contract))
  in
```

We need to create the receiver address and wrap it as a contract unit that represents an account. This will allow us to send the address the tokens. But first, we need to check if the account exists. If it doesn’t, we fail the transaction with an error message.

```
  let payout_operation : operation = 
    Tezos.transaction unit amount receiver 
  in
  let operations : operation list = 
    [payout_operation] 
  in
  ((operations: operation list), token_shop_storage)
```

We will create a transaction to an account and not a contract, so we will use unit as the first parameter and then pass the amount and the receiver address.
We need to create a list of operations that we will return at the end of the contract, which, in this case, will be just one, and then return the list as well as our updated `token_shop_storage` storage at the end of the contract.

You can now deploy this contract via the CLI or in the LIGOlang IDE.

Test this contract in the [Ligolang IDE](https://ide.ligolang.org/p/TBv_7CpnJRpSaBxTjoqoCg).

Storage example: `Map.literal [
 (0n, { current_stock = 20n ; token_price = 2mutez }) ;
 (1n, { current_stock = 4n ; token_price = 3mutez }) ;
]`

## 4.2 NFT Transfer Contract
In this section, we will create a very simple contract that can transfer an FA2 token, to be specific an NFT.

### FA2 Token Standard
You might have heard of the ERC-20 token standard on Ethereum. FA2 is a token standard on Tezos. A token standard helps to standardize the important features of tokens, like functionality and permissions. This allows us to create common interface standards so that developers can easily build applications that interact with tokens like wallets, exchanges, or games. Have a look a the [TZIP-12](https://gitlab.com/tezos/tzip/-/blob/master/proposals/tzip-12/tzip-12.md) which is a template for the FA2-standard.

### FA2 entrypoints
An FA2 compliant token must have the following Michelson entrypoints: transfer, balance_of, update_operators.

**Transfer**
The Transfer entrypoint transfers tokens between owners.

**Balance of**
The Balance_of entrypoint gets the balance of multiple account/token pairs.

**Update_operators**
Adds or removes token operators for the specified token owners and token IDs. An operator is a Tezos address that originates token transfer operation on behalf of the owner, while the owner is a Tezos address which can hold tokens.

### FA2 NFT Transfer Contract
Now that you know what the FA2 token standard is, we can create a contract that can transfer FA2 tokens.

**FA2 transfer entrypoint**
Our contract needs to transfer the NFT. The NFT we create works with the FA2 token standard. This means that we can transfer our NFT with the transfer entrypoint. 

You can find a description for the LIGO FA2 implementation of the transfer entrypoint on [Tezos’ GitLab](https://gitlab.com/tezos/tzip/-/blob/master/proposals/tzip-12/implementing-fa2.md). This is what we are going to use here.

```
type token_id = nat
 
type transfer_destination =
[@layout:comb]
{
  to_ : address;
  token_id : token_id;
  amount : nat;
}
 
type transfer =
[@layout:comb]
{
  from_ : address;
  txs : transfer_destination list;
}
```

The first type that is declared is the token_id a natural number, we have seen the token id earlier when we looked at the NFT in our wallet.

Next, we have the type transfer_destination, which is a record. When we want to transfer FA2 tokens we need to know, to which address, what token id, and how many of these tokens.

The type transfer is also a record that consists of the address from which the FA2 token transaction is executed and a list of transactions of the type transfer_destination that we just declared. 

Now that we have everything that we need for the FA2 transfer entrypoint let's write the rest of our contract.

```
type storage = unit
 
let main (token_address, storage : address * storage) : (operation list * storage) =
  let tr : transfer = {
    from_ = Tezos.self_address;
    txs = [ {
      to_ = Tezos.sender;
      token_id = 0n;
      amount = 1n;
    } ];
  } 
  in
```

We create a type of storage, as usual, here it will be of the type unit, because our simple contract won’t store anything, just transfer an FA2 token.

The only thing that we need as a parameter for our main function for this contract is the token address. 

Next, we are going to create a new transfer record that we declared in the beginning. We need the sender of the token, this will be of course the contract itself, so we can use the function Tezos.self_address. 

Now we need to create a list of token transactions, but in our case, we just send one. We need the recipient of the token, which will be the address that executes the contract, we can get this address with Tezos.sender.

Next, we need the token id, let’s hard code this, for now, to make it simpler, and use the first one, 0. We always want to send one token since it’s an NFT so the amount will be one.

```
  let entrypoint : transfer list contract = 
    match ( Tezos.get_entrypoint_opt "%transfer" token_address : transfer list contract option ) with
    | None -> ( failwith "Invalid external token contract" : transfer list contract )
    | Some e -> e
  in
  
  let fa2_operation : operation =
    Tezos.transaction [tr] 0mutez entrypoint in
  ([fa2_operation], storage)
```

As you might remember from the transfer section in chapter 2, we need a contract interface to make transactions. In our case, the FA2 entrypoint is from the type transfer list and an entrypoint.

With the built-in Tezos function get_entrypoint_opt we can get a contract from an address and entrypoint. The entrypoint that we need is called transfer and entrypoints are written in the form of "%entrypoint". 

We also need the address of the FA2 token contract, which is a parameter of our main function. The return type is transfer list contract but it is an option because there is the possibility that the token contract doesn’t exist, that is why we use pattern matching and fail with an error message if it doesn’t.

Now we can build our operation, which is a transaction. We have the list of our transactions of the type transfer that we defined earlier. We don’t want to transfer any tez tokens and we will use entrypoint, that we just created.

We need to return the operation we just created as a list, and the storage, and we are done.

Test this contract in the [Ligolang IDE](https://ide.ligolang.org/p/-mTUH135iSJ7VH5TwXHRCw).

## 4.3 NFT Shop Contract
In this section of the chapter, we will combine our shop contract with our NFT transfer functionality.

The idea is to build a shop that can sell artworks in limited editions.

```
Let's start with some types.
type token_supply = { current_stock : nat ; token_address : address ; token_price : tez }
type token_shop_storage = (nat, token_supply) map
type return = operation list * token_shop_storage
```

We can use the same types as in our token shop contract, the only difference is that we extend our record by one field, token_address which will be an address. We want to store in the storage how many tokens of an artwork we have, what the address of the token is, and how much it costs.

```
type token_id = nat
 
type transfer_destination =
[@layout:comb]
{
  to_ : address;
  token_id : token_id;
  amount : nat;
}
 
type transfer =
[@layout:comb]
{
  from_ : address;
  txs : transfer_destination list;
}
```

Let's also add the types that we need for our token transfer function. We won’t change anything here.

```
let owner_address : address =
  ("tz1VburAsF7JxEyJE7K8ZSodVsrSXa57vPw2" : address)
```

Next, we create an address that will receive the profit from the token sale, add your address there.

```
let main (token_kind_index, token_shop_storage : nat * token_shop_storage) : return =
  let token_kind : token_supply =
    match Map.find_opt (token_kind_index) token_shop_storage with
    | Some k -> k
    | None -> (failwith "Unknown kind of token" : token_supply)
  in
 
  let () = if Tezos.amount <> token_kind.token_price then
    failwith "Sorry, the token you are trying to purchase has a different price"
  in
 
  let () = if token_kind.current_stock = 0n then
    failwith "Sorry, the token you are trying to purchase is out of stock"
  in
 
  let token_shop_storage = Map.update
    token_kind_index
    (Some { token_kind with current_stock = abs (token_kind.current_stock - 1n) })
    token_shop_storage
  in
```

In the next part, we are using a large part of the shop contract to create the main function, get the kind of token from the index through the parameter and check if the token exists, the right price was paid, and if it's still in stock. We also update the storage and reduce the stock by one, if the contract execution goes through.

```
  let tr : transfer = {
    from_ = Tezos.self_address;
    txs = [ {
      to_ = Tezos.sender;
      token_id = abs (token_kind.current_stock - 1n);
      amount = 1n;
    } ];
  } 
  in
```
The only change from our transfer list is that we are reading the token_id type dynamically. The idea of this shop is that the owner creates the contract, specifies how many tokens of this can will be sold, and sends the token to the contract. Every time a token is sold we reduce the token id by one. It is important that the range for tokens with ids from 0 to the maximum amount to sell are sent without any id missing.

```
  let entrypoint : transfer list contract = 
    match ( Tezos.get_entrypoint_opt "%transfer" token_kind.token_address : transfer list contract option ) with
    | None -> ( failwith "Invalid external token contract" : transfer list contract )
    | Some e -> e
  in
 
  let fa2_operation : operation =
    Tezos.transaction [tr] 0mutez entrypoint
  in
```
We are creating the transaction operation for our FA2 transfer, the only change here is that we now get our token address from the token the user specified in the parameters with token_kind.token_address.

```
  let receiver : unit contract =
    match (Tezos.get_contract_opt owner_address : unit contract option) with
    | Some (contract) -> contract
    | None -> (failwith ("Not a contract") : (unit contract))
  in
 
  let payout_operation : operation = 
    Tezos.transaction unit amount receiver 
  in
 
```

The payout functionality remains the same as in the shop contract.

```
  ([fa2_operation ; payout_operation], token_shop_storage)
```

Finally, we return a list of operations consisting of the fa2_operation and the payout_operation. We also return the new storage, where we reduced the stock of the token.

Test this contract in the [Ligolang IDE](https://ide.ligolang.org/p/plMFVM9LSN5nddC0sRrPrQ).

#### Deploy and test your contract 
Before you can deploy your contract, you need to know the address of the token you want to sell.

**Create an NFT to test**
To create a simple NFT on the hangzhounet testnet we will just fork a token contract.
1. Open this contract (https://better-call.dev/hangzhou2net/KT1SZhncyQ4F7AGchwM8e4N1JsijkqZdYJ5o/fork) in "better-call.dev".
2. Click on Fork.
3. Add your address as the administrator.
4. Select "HANGZHOUNET" as the network.
5. Click execute at the bottom and confirm the transaction with your temple wallet.
6. After your contract is deployed, save the address of the contract.

**Deploy your contract**
Create the storage for your contract, which could look like this:

```
Map.literal [ 
  (0n, { 
    current_stock = 1n ; 
    token_address = ("KT1SZhncyQ4F7AGchwM8e4N1JsijkqZdYJ5o" : address); 
    token_price = 1mutez
  });
]
```

Use the addresses of the NFTs that you just created, add the initial stock and the price per asset in mutez.

Now you can deploy the contract. Either via the Tezos client or the IDE.
After you deployed your contract, copy the address of your contract.

**Mint a token and send it to the contract**
1. Open your NFT contract in "better-call.dev".
2. Click on "mint" in the right window.
3. Enter the address of your token shop contract as the owner address.
4. Enter the amount you want to mint (1).
5. Click on the "EXECUTE" button and confirm the transaction.

**Buy the token**
1. Open your token shop contract in "better-call.dev".
2. Click on the "TRANSFERS" tab and you should see the token you just minted.
3. Click on the "INTERACT" tab and enter ounder amount 1000000 mutez which is one tez.
4. Click on the "EXECUTE" button and confirm the transaction.
5. In your wallet you can click on "Manage", "Add Asset", and enter the address of your NFT token to see it in your wallet.  

That's it! Great job. You can now try to build your own contract and participate in our challenge to receive feedback on your project and maybe earn some tez for it!
