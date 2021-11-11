    sp.add_compilation_target("FA2_comp", FA2(config = FA2_config(non_fungible = True),
                              metadata = sp.utils.metadata_of_url("https://example.com"),
                              admin = sp.address("tz1Te9TEmMpqQxe13cvsT2ipfLGHm9uhCadM")))
