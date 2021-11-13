import smartpy as sp
FA2imp = sp.io.import_template("FA2.py")

class FA2(FA2imp.FA2):
    pass

class TokenShop_config:
    def __init__(self, ownerAddress):
        self.ownerAddress = ownerAddress

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
                    current_stock = sp.nat(100),
                    token_address = token.address,
                    price = sp.tez(1)
                )
            })
        )
        scenario += shop

        tokenMeta = FA2.make_metadata(
            name = "FreshTacoToken",
            decimals = 0,
            symbol= "FTT0"
        )

        token.mint(
            address = shop.address,
            amount = 1,
            metadata = tokenMeta,
            token_id = 0
        ).run(
            sender = admin
        )

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


    # Adjust the compilation target accoring to your contract and admin address
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
