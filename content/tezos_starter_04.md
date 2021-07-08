## 4.1 The smart contract of the Token Shop
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
let ownerAddress : address =
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
    match (Tezos.get_contract_opt ownerAddress : unit contract option) with
    | Some (contract) -> contract
    | None -> (failwith ("Not a contract") : (unit contract))
  in
```

We need to create the receiver address and wrap it as a contract unit that represents an account. This will allow us to send the address the tokens. But first, we need to check if the account exists. If it doesn’t, we fail the transaction with an error message.

```
  let payoutOperation : operation = 
    Tezos.transaction unit amount receiver 
  in
  let operations : operation list = 
    [payoutOperation] 
  in
  ((operations: operation list), token_shop_storage)
```
We will create a transaction to an account and not a contract, so we will use unit as the first parameter and then pass the amount and the receiver address.
We need to create a list of operations that we will return at the end of the contract, which, in this case, will be just one, and then return the list as well as our updated `token_shop_storage` storage at the end of the contract.

You can now deploy this contract via the CLI or in the [LIGOlang IDE](https://ide.ligolang.org/p/N3D8IeExpI9AeQel39bkuw).
Storage example: `Map.literal [
 (1n, { current_stock = 20n ; token_price = 2tez }) ;
 (2n, { current_stock = 4n ; token_price = 3tez }) ;
]`

## 4.2 Adding the FA2 functionality to the Token Shop
Coming soon.

## 4.3 Debugging our contract
Coming soon.

## 4.4 The front end for the Token Shop 
Coming soon.
