import smartpy as sp

FA2imp = sp.io.import_template("FA2.py")
class FA2(FA2imp.FA2):
    pass

class TacoShop_config:
    def __init__(self, ownerAddress, tokenAddress):
        self.ownerAddress = ownerAddress
        self.tokenAddress = tokenAddress

class TacoShop(sp.Contract):
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
                    current_stock = sp.nat(10),
                    price = sp.tez(1)
                )
            })
        )
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
        # decreace the stock
        self.data[token_kind_index].current_stock = abs(token_kind.current_stock - sp.nat(1))
        # send the owner of the TacoShop all the tez that the caller sent
        sp.send(self.config.ownerAddress, sp.amount, message = "Not a contract")

        # FA2 token transfer,
        # send 1000000 of token_id 0 from this contract
        # to the sender of the tx
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

        # sp.transfer(arg, 0, self.config.tokenAddress)
        contract = sp.contract(
            txArgsType,
            self.config.tokenAddress,
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


@sp.add_test(name = "TacoShop")
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

    shop = TacoShop(
        config = TacoShop_config(
            ownerAddress = bob.address,
            tokenAddress = token.address
        )
    )
    scenario += shop

    tokenMeta = FA2.make_metadata(
        name = "FreshTacoToken",
        decimals = 0,
        symbol= "FTT0"
    )
    token.mint(
        address = shop.address,
        amount = 100,
        metadata = tokenMeta,
        token_id = 0
    ).run(
        sender = admin
    )

    shop.buy_token(0).run(
        sender=alice,
        amount=sp.tez(1),
    )
    shop.buy_token(1).run(
        sender=alice,
        amount=sp.tez(1),
        valid=False
    )
