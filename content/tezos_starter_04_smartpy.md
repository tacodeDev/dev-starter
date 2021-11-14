## 4.1 Shop Contract

In this section, we will build a very simple shop where users can buy various tokens. We will store the number of tokens we have in stock as well as each token’s price. In this section, we won’t transfer real tokens, only handle the shop mechanism.

Let’s get started.

```
import smartpy as sp
 
class TokenShop_config:
    def __init__(self, ownerAddress):
        self.ownerAddress = ownerAddress
```

First, we create a configuration class, because we want to enable the user to enter an address that receives the tez that are earned.

We initiate `ownerAddress` and assign it the value of our parameter `ownerAddress`.

Now let's build our contract.

```
class TokenShop(sp.Contract):
    def __init__(self, config):
        self.init_type(
            sp.TMap(
                sp.TNat,
                sp.TRecord(
                    current_stock = sp.TNat,
                    price = sp.TMutez
                )
            )
        )
        self.init(
            sp.map({
                sp.nat(0) :
                sp.record(
                    current_stock = sp.nat(2),
                    price = sp.tez(2)
                )
            })
        )
        self.config = config
```

We call our contract `TokenShop`, add a config parameter and then create a type constraint. 
The shop is going to sell multiple tokens and we want to know the price and stock of each token. In order to store this information, we are going to use a map. 

Inside our map we have the key, the index of the token, this will be a positive number so we use the natural number type, the value of the map will be of the type record.
The record consists of two fields: `current_stock`, a natural number that stores how many tokens of this type are left in the store, and `price` which stores the price of the token in tez.

We initiated our map with the index 0 and a record with a stock of two tokens for the price of two tez.

Finally, we assign `self.config` the value of our config parameter. Here we are going to save the address of the owner.

Ok, that’s it for the first part now, let's create our entry point.

```
@sp.entry_point()
def buy_token(self, token_kind_index):
    sp.set_type(token_kind_index, sp.TNat)
    sp.verify(
        self.data.contains(token_kind_index),
        message = "Unknown kind of token"
    )
    token_kind = self.data.get(token_kind_index)
    sp.verify(
        sp.amount >= token_kind.price,
        message = "Sorry, the token you are trying to purchase has a different price"
    )
    sp.verify(
        token_kind.current_stock > sp.nat(0),
        message = "Sorry, the token you are trying to purchase is out of stock"
    )

```

We name the entry point `buy_token` and need one parameter, the index of the token the user wants to buy. This parameter will be a natural number.

In the next lines, we create some conditions to check and raise errors if they are not met. 

First, we check if the token index exists with the built-in method `data.contains`, if it does we create a new variable, `token_kind`, and assign it the value of `toke_kind_index` with the method `self.data.get`.

Next, we check if the amount the user sends is higher or has the same value as the `token_kind.price`.

In our last check, we are testing if the token is in stock.

After all, checks are successfully passed, we decrease the stock and send the owner the tez as payment.

```
    self.data[token_kind_index].current_stock = abs(token_kind.current_stock - sp.nat(1))
    # send the owner of the TokenShop all the tez that the caller sent
    sp.send(self.config.ownerAddress, sp.amount, message = "Not an account")
```

First, we update the record field for the stock of the token that is purchased. We assign it a new value which is the old stock reduced by one since in this simple contract we only allow to buy one token per purchase. We use `abs` to ensure that it is a `nat` that we are assigning.

Finally, we use `sp.send` to send the owner of the token shop the amount of tez that the user paid to buy the token. We need as parameters the destination address in our case `ownerAddress` that we created in our config, the amount that will be transferred to the owner, and an error message if the contract is not an account.

In the last step, we create the tests for our contract.

```
@sp.add_test(name = "TokenShop")
def test():
    alice = sp.test_account("Alice")
    bob = sp.test_account("Bob")
 
    scenario  = sp.test_scenario()
 
    shop = TokenShop(
        config = TokenShop_config(
            ownerAddress = bob.address
        )
    )
    scenario += shop
```

We define two test accounts, `alice` and `bob` and create our shop contract making bob the owner of the shop. Now let's start the testing.


```
# buy token
shop.buy_token(0).run(
    sender = alice,
    amount = sp.tez(2),
)
# buy token with wrong id
shop.buy_token(1).run(
    sender = alice,
    amount = sp.tez(2),
    valid = False
)
# buy token with wrong price
shop.buy_token(0).run(
    sender = alice,
    amount = sp.tez(1),
    valid = False
)
# buy to a higher price than specified
shop.buy_token(0).run(
    sender = alice,
    amount = sp.tez(3),
)
# token is out of stock
shop.buy_token(0).run(
    sender = alice,
    amount = sp.tez(2),
    valid = False
)

```

We try to buy the token, which should not raise any errors. Then we try to buy the token with an ID that doesn't exist, for a lower price, for a higher price and for a token that is already out of stock. 

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJy1VU1v2zAMvftXCNnFxjKj3W4FUqwbsFt7WLvTMBiKTCdCHMmQ5HbusP8@UnYc@SMIunU6JLb4TD5Sj5TcV9o4ZvfcuKph3DJbRZEoubXsQe9A3W91lQmtCrm5ihiuHAqWZVJJl2WxhbJYMv2kwNzkuQFrkxZFi4xpaGOrAXQSJ7ZV@lkrZ7hwycloLZlxHA9xTQVxv@9tVfpwy6vh5sFwx91y1vAVhDb59CNaojYGlMus02KHGZ10RKsyUkAHuq0dPE9QSTT_lkzTm2S2x8R@zSWguIsvEnY1ZzMvy41cvU_OZoepIexMdr9PpteeKbpqHyJv_Yh@kY1pskpL5eKkV8S6bjJHqukk4Z@znVQ5SiWHn6E4qtRCp4wxbHk4vCSEP4KRRTMqNpHMuePE1HGp7MTZqEZ7FDjfUHUW39ROoe4ZYZkuWraLmVIcXVJR@5AbcNNoZxlXKd_rWjl2vQocp_7MTlK918Y0WM8ttN@wRteMG3wzjVQb3GRVbcSWW2D4wzjLZVEAiaZVw1xaJxgGpIa6uz5K@FWISst07ajy3v8cxTcoK2GAo5zJpccNFUon8X18Cj_SccfwdaiMkfndIbHLJAxtAQ@cwvrh6BWCL_1UZLws20ThGf@58y8CdxGM37qh1lUeBy01mL_LoyqWYTHvtMOTFN3kXSRRFFHv8TzPHFgXK773uJ4SQqgNvbHrNapgIRUEjvw@L4MZYV3GhaD48eKGDIu2Dmu9noN80msi41MToLiRmgW4w158wFCxVsF10hemHy_jK22oyNFdhayoBv6qGkomGXJ6u_Kxo64QOJ1aUfas0uPAukhSU6s4EBcKyZByykFjds0bDNdlEDoIwp6k27Ino1H1Mp8LefmPIWk9Ipam0hdeWjhPxM@C10z_8gVcUIJbudmi2_aCwp5R6AeELCTMVuhvWX0YHUpbh9G8@R8qOFGGP5f7w8c-).

## 4.2 NFT Transfer Contract
In this section we will create a very simple contract that can transfer an FA2 token, to be specific an NFT.

### FA2 Token Standard
You might have heard of the ERC-20 token standard on Ethereum. FA2 is a token standard on Tezos. A token standard helps to standardize the important features of tokens, like functionality and permissions. This allows us to create common interface standards so that developers can easily build applications that interact with tokens like wallets, exchanges, or games. Have a look a the [TZIP-12](https://gitlab.com/tezos/tzip/-/blob/master/proposals/tzip-12/tzip-12.md) which is a template for the FA2-standard. 

### FA2 entry points 
An FA2 compliant token must have the following Michelson entry points: transfer, balance_of, update_operators.

**Transfer** 
The Transfer entrypoint transfers tokens between owners.

**Balance of**
The Balance_of entrypoint gets the balance of multiple account/token pairs.

**Update_operators**
Update_operators adds or removes token operators for the specified token owners and token IDs. An operator is a Tezos address that originates token transfer operation on behalf of the owner, while the owner is a Tezos address that can hold tokens.

### FA2 NFT Transfer Contract
Now that you know what the FA2 token standard is, we can create a contract that can transfer FA2 tokens.

Our contract needs to transfer the NFT. The NFT we create works with the FA2 token standard. This means that we can transfer our NFT with the transfer entrypoint.

You can find a SmartPy FA2 implementation [here](https://smartpy.io/ide?cid=QmWxgJJaWedeZHLG5dTqauAM8wcCs4yqQGkBMLvQ6Qmcuy&k=5229ded0aaece06197d9). This is what we are going to use.

```
import smartpy as sp
 
FA2imp = sp.io.import_template("FA2.py")
class FA2(FA2imp.FA2):
    pass
```

We import the SmartPy FA2 implementation because we want to use their transfer entry point to transfer our token.

```
class TokenTransfer(sp.Contract):
    def __init__(self, tokenAddress):
        self.init_type(sp.TUnit)
        self.init()
        self.tokenAddress = tokenAddress
```

Next, we create our `TokenTransfer` contract class. We initiate the contract with an empty storage but store `tokenAddress` from a parameter, this will be the address of the FA2 token we want to transfer.

Now we will create the `transfer_token` entry point.

```
@sp.entry_point()
def transfer_token(self):
    sp.transfer(
      txArgs,
      sp.mutez(0),
      contract
    )
```

We will write this entry point from the bottom to the top to make it easier to understand.

We want to transfer a token, so we can use `sp.transfer`. You use it like this: `sp.transfer(arg, amount, destination)`. The destination is a contract, in our case the FA2 contract and it’s `transfer` entry point. You can specify an amount in tez that you want to send with the transfer and arguments that you call the contract with, `arg`.

We will create those arguments next, for now, we use `txArgs` as a variable. There is no need for an amount to send with at the moment so this stays `0` and our `contract` is also a variable that we will define later. Remember we are writing this contract in reverse, from the end to the beginning.

Let's create the arguments for our transfer function.

```
txArgs = sp.list([sp.record(
    from_ = sp.self_address,
    txs = sp.list([
        sp.record(
            to_ = sp.sender,
            token_id = 0,
            amount = sp.nat(1)
        )
    ])
)])

```

The arguments are a list of records to addresses with a list of transaction records. In the transaction records for a token transfer we need to define the sender address, the `token_id` of the token we want to send, and with the `amount`, how many tokens need to be sent.

Next, we create an instance of the token FA2 contract of the NFT with the transfer entry point that we want to call.

```
contract = sp.contract(
    txArgsType,
    self.tokenAddress,
    "transfer"
).open_some("INTERFACE ERROR")

```

We use the function `sp.contract`. Which is called like this: `sp.contract(t, address, entry_point = '<entry_point_name>')`. 
We first need to add the argument's type, this will be the type for the arguments the txArgs that we just created, we call it `txArgsType` and will define them next.
We need to provide the address of our token contract, this will be `self.tokenAddress` that is created when the contract is initiated.

The last argument is the entry point we want to call, in our case we want to call the transfer entry point of our FA2 compliant NFT token.
Finally, if the entry point does not exist we will return an error message.

Now to the last part of our contract, the argument type of the transactions.

```
txArgsType = sp.TList(
    sp.TRecord(
        from_ = sp.TAddress,
        txs = sp.TList(
            sp.TRecord(
                to_ = sp.TAddress,
                token_id = sp.TNat,
                amount = sp.TNat
            ).layout(("to_", ("token_id", "amount")))
        )
    ).layout(("from_", "txs"))
)

```

The arguments are a list of transaction records consisting of addresses with a list of transaction records. In the transaction records we have an address for the recipient, the `token_id` of the token we want to send, and with the `amount` we specify how many tokens will be sent, which is a nat.

That't it for this contract, here in its entirety:
```
import smartpy as sp
 
FA2imp = sp.io.import_template("FA2.py")
class FA2(FA2imp.FA2):
    pass
 
class TokenTransfer(sp.Contract):
    def __init__(self, tokenAddress):
        self.init_type(sp.TUnit)
        self.init()
        self.tokenAddress = tokenAddress
 
    @sp.entry_point()
    def transfer_token(self):
        txArgsType = sp.TList(
            sp.TRecord(
                from_ = sp.TAddress,
                txs = sp.TList(
                    sp.TRecord(
                        to_ = sp.TAddress,
                        token_id = sp.TNat,
                        amount = sp.TNat
                    ).layout(("to_", ("token_id", "amount")))
                )
            ).layout(("from_", "txs"))
        )
 
        contract = sp.contract(
            txArgsType,
            self.tokenAddress,
            "transfer"
        ).open_some("INTERFACE ERROR")
 
        txArgs = sp.list([sp.record(
            from_ = sp.self_address,
            txs = sp.list([
                sp.record(
                    to_ = sp.sender,
                    token_id = 0,
                    amount = sp.nat(1)
                )
            ])
        )])
        
        sp.transfer(
          txArgs,
          sp.mutez(0),
          contract
        )
```

Now let's add the tests.

```
@sp.add_test(name = "TokenTransfer")
def test():
    alice = sp.test_account("Alice")
    bob = sp.test_account("Bob")
    admin = sp.test_account("Administrator")
```

We create three test accounts. Two of them will be test users that will transfer tokens and we need one admin that needs to create the NFT token in our test scenario.

```
    scenario  = sp.test_scenario()

    token = FA2(
        FA2imp.FA2_config(debug_mode = True),
        metadata = sp.utils.metadata_of_url("https://example.com"),
        admin = admin.address
    )
    scenario += token
```

We create a token contract from our FA2 implementation, as arguments we enable debug mode, add an example URL for the meta data and add the admin address that we just created as the admin. We then add the token contract to our testing scenario.

```
    shop = TokenTransfer(tokenAddress = token.address)
    scenario += shop
```

Next, we also add our TokenTransfer contract. For the tokenAddress parameter in our contract, we add the address of the token that we just created.
 
Now we want to mint (create) the token in our test scenario.
 
```
    tokenMeta = FA2.make_metadata(
        name = "GreenSquare",
        decimals = 0,
        symbol = "GSP"
    )

    token.mint(
        address = shop.address,
        amount = 1,
        metadata = tokenMeta,
        token_id = 0
    ).run(
        sender = admin
    )
```

 
We will need some metadata for our token. This is data that can be used by programs like wallets or explorers to display and interact with your token correctly. We choose an arbitrary name, zero decimals, and a symbol.
 
To create our token we will use the mint method of the token that we just created. The recipient of the tokens will be the address of our token shop, we will create 1 token, add the metadata we just created and give the token the id 0. The admin will execute this function.
 
```
    shop.transfer_token().run(
        sender = alice
    )

    shop.transfer_token().run(
        sender = bob
    )
```
 
Finally, we test our token transfer entry point with our two user accounts. In the output panel, you should now see that 98 tokens are owned by the contract and one each by Alice and Bob.

Here is the complete contract with tests:
```
import smartpy as sp
 
FA2imp = sp.io.import_template("FA2.py")
class FA2(FA2imp.FA2):
    pass
 
class TokenTransfer(sp.Contract):
    def __init__(self, tokenAddress):
        self.init_type(sp.TUnit)
        self.init()
        self.tokenAddress = tokenAddress
 
    @sp.entry_point()
    def transfer_token(self):
        txArgsType = sp.TList(
            sp.TRecord(
                from_ = sp.TAddress,
                txs = sp.TList(
                    sp.TRecord(
                        to_ = sp.TAddress,
                        token_id = sp.TNat,
                        amount = sp.TNat
                    ).layout(("to_", ("token_id", "amount")))
                )
            ).layout(("from_", "txs"))
        )
 
        contract = sp.contract(
            txArgsType,
            self.tokenAddress,
            "transfer"
        ).open_some("INTERFACE ERROR")
 
        txArgs = sp.list([sp.record(
            from_ = sp.self_address,
            txs = sp.list([
                sp.record(
                    to_ = sp.sender,
                    token_id = 0,
                    amount = sp.nat(1)
                )
            ])
        )])
        
        sp.transfer(
          txArgs,
          sp.mutez(0),
          contract
        )
 
 
@sp.add_test(name = "TokenTransfer")
def test():
    # define a contract
    alice = sp.test_account("Alice")
    bob = sp.test_account("Bob")
    admin = sp.test_account("Administrator")
 
    scenario  = sp.test_scenario()
 
    token = FA2(
        FA2imp.FA2_config(debug_mode = True),
        metadata = sp.utils.metadata_of_url("https://example.com"),
        admin = admin.address
    )
    scenario += token
 
    shop = TokenTransfer(tokenAddress = token.address)
    scenario += shop
 
 
    tokenMeta = FA2.make_metadata(
        name = "GreenSquare",
        decimals = 0,
        symbol = "GSP"
    )
 
    token.mint(
        address = shop.address,
        amount = 100,
        metadata = tokenMeta,
        token_id = 0
    ).run(
        sender = admin
    )
 
    shop.transfer_token().run(
        sender = alice
    )
 
    shop.transfer_token().run(
        sender = bob
    )
```

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJydVV1v2yAUfc@vsNgL1iI33WOlScuqdpq0dVOaPU0TIjZpUQ14gKVmv373GmPj2lGn@SUBzj333C@QqjHWZ05x65tTxl3mmlW2ut2@k6rJ3sOqkKaQHYp5oZqae0EJnBfNieSrsubOZbCkwaSAn_xqlcHXwMmqB@zNk9B7y7U7CkuB9Npob3npe2wljhljUkvPGHWiPq4zjybbqrLCuR6FHx4WHdCfGoFU@x@wyucA@mIvJYTI0iVEjLAPwCZA14k1RupIgNp8L511Vp3CRJN_3toHtwc9IWP7L9J5Ohx3CmB3J0pjq@k@fkdrFOste0HrGcg_u7Pk_@Jk4DGvuhqhECuTVY@_4_48livTaj8iF4F5UfOTaT2lBGSQdYa_wQcsSOAgeZ7PrKc7CU@XOzSG_JDEMO9Lil_Z91pQF1fTFI0lnMY465zpMYmNQUbPhWkgJGcUzMnnu_3N7nZ7fZPd7HbfdiSVFVwGUTXW9Cf8sQvlS_oD5TC@pGToj0A1y@AZ7sHcDB50JexyoZOG2Cwj0jbQ3NPL10r5KylZ8n@c3KaIKU6Fh9ylGgCoWi_@0E2ebsdqTxtjhZMOaYQbDZKlucLBJZNLCkrVDT4C@lF_g1eB1CLjU1pey7KffIQzXpaYBUq2eEBCVAdzWIJ8NIcewCsl9SILHkBRLffGDh3kSqG5lSZLTOIejaCuYADA@3nIwHhRMwjjKB9oJQ7tA1Omwij2thVJCpXwvOKeBzetl7Ur4h4zR9bampJH7xt3dXEhnjm8EAJmTJGEI4bW_RY83rlDMwyxvO2v5Rjjo8E3aPp4LF3jkXNOhxTANmbjq@hiwQdM8SfBYixjfmI7fLJC6PvfLbeCjLFUopSK1246A@6kDqburO6_kz600Wmh8DlJ8hHVo7xiNs_DFF1uNouVGCIZT9PZDP4L2@rRZ5jrWIRUYafhxQN31hg7@n@NYQSC6V_dqT5p).

### 4.3 NFT Shop Contract
In this section of the chapter, we will combine our shop contract with our NFT transfer functionality.

The idea is to build a shop that can sell NFTs of artworks.


```
import smartpy as sp
 
FA2imp = sp.io.import_template("FA2.py")
class FA2(FA2imp.FA2):
    pass

We import the FA2 implementation as we have done in the token transfer contract.

class TokenShop_config:
    def __init__(self, ownerAddress):
        self.ownerAddress = ownerAddress
```

We add a token configuration class as we have done in our TokenShop contract before, but we add the token address of our FA2 token in here too.

```
class TokenShop(sp.Contract):
    def __init__(self, config, init_data):
        self.init_type(
            sp.TMap(
                sp.TNat,
                sp.TRecord(
                    current_stock = sp.TNat,
                    token_address = sp.TAddress,
                    price = sp.TMutez
                )
            )
        )
        self.init(init_data);
        self.config = config
```

We initialise our contract as we did in our TokenShop contract and set the stock of the token to 100.

```
    @sp.entry_point()
    def buy_token(self, token_kind_index):
        sp.set_type(token_kind_index, sp.TNat)
        sp.verify(
            self.data.contains(token_kind_index),
            message = "Unknown kind of token"
        )
        token_kind = self.data.get(token_kind_index)
        sp.verify(
            sp.amount >= token_kind.price,
            message = "Sorry, the token you are trying to purchase has a different price"
        )
        sp.verify(
            token_kind.current_stock > sp.nat(0),
            message = "Sorry, the token you are trying to purchase is out of stock"
        )
        self.data[token_kind_index].current_stock = abs(token_kind.current_stock - sp.nat(1))
        sp.send(self.config.ownerAddress, sp.amount, message = "Not a contract")
```


We take the start of our `buy_token` entry point from our TokenShop contract, we don’t change anything here.

 ```
        xArgsType = sp.TList(
            sp.TRecord(
                from_ = sp.TAddress,
                txs = sp.TList(
                    sp.TRecord(
                        to_ = sp.TAddress,
                        token_id = sp.TNat,
                        amount = sp.TNat
                    ).layout(("to_", ("token_id", "amount")))
                )
            ).layout(("from_", "txs"))
        )

        contract = sp.contract(
            txArgsType,
            token_kind.token_address,
            "transfer"
        ).open_some("INTERFACE ERROR")

        txArgs = sp.list([sp.record(
            from_ = sp.self_address,
            txs = sp.list([
                sp.record(
                    to_ = sp.sender,
                    token_id = 0,
                    amount = sp.nat(1)
                )
            ])
        )])
        sp.transfer(
          txArgs,
          sp.mutez(0),
          contract
        )
```
 
The bottom part of our `buy_token` entry point stays the same as in our TokenTransfer contract, the only thing that we change is how we get the `tokenAddress`. In this contract, it is provided by the config class, instead of coming from the parameter.

```
if "templates" not in __name__:
    @sp.add_test(name = "TokenShop")
    def test():
        alice = sp.test_account("Alice")
        bob = sp.test_account("Bob")
        admin = sp.test_account("Administrator")

        scenario  = sp.test_scenario()

        token = FA2(
            FA2imp.FA2_config(
                debug_mode = True,
                non_fungible = True
            ),
            metadata = sp.utils.metadata_of_url("https://example.com"),
            admin = admin.address
        )
        scenario += token

        shop = TokenShop(
            config = TokenShop_config(
                ownerAddress = bob.address
            ),
            init_data = sp.map({
                sp.nat(0) :
                sp.record(
                    current_stock = sp.nat(1),
                    token_address = token.address,
                    price = sp.tez(1)
                )
            })
        )
        scenario += shop

        tokenMeta = FA2.make_metadata(
            name = "Artwork01",
            decimals = 0,
            symbol= "ART1"
        )

        token.mint(
            address = shop.address,
            amount = 1,
            metadata = tokenMeta,
            token_id = 0
        ).run(
            sender = admin
        )

```

We begin the test in the same way as in our TokenTransfer contract. We create three test accounts and create a token contract from our FA2 implementation. We will need some metadata for our token. To create our token we will use the mint method of the token that we just created.

```
        # buy token with wrong id
        shop.buy_token(1).run(
            sender = alice,
            amount = sp.tez(1),
            valid = False
        )
        # buy token with wrong price
        shop.buy_token(0).run(
            sender = alice,
            amount = sp.tez(0),
            valid = False
        )
        # buy token
        shop.buy_token(0).run(
            sender = alice,
            amount = sp.tez(1),
        )
        # buy token again
        shop.buy_token(0).run(
            sender = alice,
            amount = sp.tez(1),
            valid = False
        )
```


Finally, we test the buy_token entry point in a similar way as we did in our TokenShop contract.
We try to buy the token, which should not raise any errors. Then we try to buy the token with an ID that doesn't exist, for a lower price and for a higher price.

```
    # after the tests we need to add a compilation target for the deplpyment to test or mainnet
    sp.add_compilation_target("taco_shop", TokenShop(
        config = TokenShop_config(
            ownerAddress = sp.address("tz1Te9TEmMpqQxe13cvsT2ipfLGHm9uhCadM")
        ),
        init_data = sp.map({
            sp.nat(0) :
            sp.record(
                current_stock = sp.nat(1),
                token_address = sp.address("KT1Sh2okif2FBZiTAAmhgpWvzDBvqRwvQiGo"),
                price = sp.tez(1)
            )
        })
    ))
```

Inside the compilation target we can add values for the initial storage and the config value.
In our case, we want to add the address of the owner of the shop in the config. In our initial storage,
we need to specify the available stock, the address of the token that we want to sell, and the price of the token.

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJy9WFtv2zYUfvevINQXCfPUOHtqgBRzsqQb1qSo42LAikCgJcrmLJEqSTlxhv33Hoq6UBLtJBg2PcSmzuHh4Xdun0PzgguFZI6FKvYISySLyfX8lOYFOofvIeUhrXQiRfIiw4r4HsjDYu8Fk0mcYSkRrH2zJ4SP4GyC4ClA0igs@Zawuw0vopizlK6NRkJSFEWUURVFviRZOkX8gRExTxJBpKzt6EcLQ1sGvtnL0Tk@eH7JmRI4VsHB04wzU1S9TLDCwyMrgdoXxG_fV7IiXN7gov@yEdxiNXUKFiTmIhlv0k9cCkGYiqTi8dYA7zakH6VvGeEWCa1cA@HeUAgak1rxplTkaaQVTNyrYIyH36HVFxo04RjzZVJJf4Yz4WJiHxWcMuUHbSxW5T6qblIHw9xqS1kCQUrIox2LIpSkDsRQbdpgFdjqOyJouh9ETTup_daeKkyZHBkL@vjlgChea@S8L2zLIOOQ1kU8Nd56Dpw6kxrw9sg1UePTnvW4CHHOS6bQ@3PLcFjF86Crd1yIPeC5IWYP2vMSYQErsadsDS9RUYp4gyVB8AdhlNA0JTr_TKa4rnXAQ8upfgq_1zsYVv7JYUxf4yiViJdKI1_Zd7rYgP11CPR9OKwvvLKDPxD_2Pg@C4J@DrLEt1K915GmXbSm9iVvuQKE47oX6Z7ZYvc4F2u5hKSuS_MjlaoH75GukQqeR8_UvnqUhyy_4IQuxM@d008GmjzXv@Cp07pVdOkFYYYhI5Tve@CDN0X605wAC8@Y8IIgGG7uvbCsVJjprQCMF9hNrv3axMl41qx62HRh693OyqZef@4peWCOSag1K39DXoC25DkM1t9ul1eL6_nlFbpaLD4txtli_Mp0OL_CFzEOnZUYOlWdbrSJYQwN8XMb7i7amofaEs4QW5lw4lSw428q7WgQ761g3fdqsgF00JYqsPong3KuZ9@oIzVRtvKBphCqmu5IDzGoYcqAPTCckyg6aycbgAu0CDDUAl3tLQHxukFXKVjTDGftNNaiCMexBsP35lrgdddb8ZVL7YKvLCWc5OCay5oWQHwFVlzYmSRjwrCgHFm7mne@nXFVTz6v2F0PsI7q1XRunCcJWZXrKOeJvuhSlGScBYyzKC3Zmq6yRqlPQoZzQ2Hd3I3TpaKZDJt3EU@jUmS@t1GqkGdv35JHDMEjUMC5N7DT4FV9hnV1uKZJg9IP9ei1AIT4ao9bsjlMJ0ODhqR3jNKA0UK8Rw45kGj5l4EiByL6t4twmumLzlyyI_Xt4qKmRF_GRqt16Go77WPxUV2Q4@If8NF_nITUCpCOyCBxb0gFkP6pkuMtiZpc6d@5qdu5UA9cbE9mXt_jhMQ0x5kcNzK5z1c8M1thm2uYGCRyTXsHKdgyd_DbDVXbIGcHy6C9Zl_D7r3WlBElG9Jh3b6bSnD5_0Zz9LoNPFC1QQ@CAy2jSa8Swo7Iz44ek41Iqz0FTCL05TvYo@9xDREgjhQ44GCVXod8PPmXPg6nxyt8_K9csmFzg4PXmP4vxx9DxCTWGzRP_iqlqmg_9OeCwpClnCGFBfxIQnp@iZr9A28THSXD8JPKdG@7SdZT2LIUGUsNW9S3BdLn6NYv7NSDLi3bioUTnmZL8m55ld8U3z4_ktlP8U4uT2mRfvzwa_6u3Fzi5Maa1RZQzzbxQw38SPN@ReN2_AuhvdTvy9nd5pRvaXp6ffEnXc7n@WZd_LF7@uVi923xsPtMP_DhVNXP8a7erepuDgT8OwCt300-).

#### Deploy and test your contract 
Before you can deploy your contract, you need to know the address of the token you want to sell.

**Create an NFT to test**
To create a simple NFT on the granda testnet we will just fork a token contract.
1. Open this contract (https://better-call.dev/granadanet/KT1DRbT9JvFurMwx8dsMbEWattuWGDZxaA9y/fork) in "better-call.dev".
2. Click on Fork.
3. Add your address as the administrator.
4. Select "GRANADANET" as the network.
5. Click execute at the bottom and confirm the transaction with your temple wallet.
6. After your contract is deployed, save the address of the contract.

**Deploy your token shop contract**
You can use the smartpy IDE to deploy your contract.
1. Open the smartpy IDE.
2. In the compilation target, enter your address as the owner address and the address of the contract you just created as the token address.
3. Click on "run" to compile your contract.
4. Select token_shop from the dropdown under compilations.
5. Click on "Deploy Michelson Contract" in the right window and then own the "Deploy Michelson Contract" button.
6. Select the Granada network from the "Node and Network" dropdown.
7. Click on Temple wallet and confirm the connection.
8. Click on "ESTIMATE COST FROM RPC" button.
9. Click on "DEPLOY CONTRACT" button, accept the information and confirm the transaction.
10. After the contract is deployed, save the address of the contract.

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
