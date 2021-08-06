## 1.1 What is Tezos?
In this section, you will revisit blockchain basics and learn about the most important Tezos concepts.

### Bitcoin and Ethereum
At the end of 2008, a *whitepaper* called “Bitcoin: A Peer-to-Peer Electronic Cash System” was released under the pseudonym of *Satoshi Nakamoto*. The whitepaper laid out a vision of a digital currency that could function without dependency on any centralized entity.

At the beginning of 2009, the Bitcoin software went live. All transactions of the Bitcoin currency are stored on a digital ledger that is distributed between the participants of the Bitcoin network. This ledger is called a *Blockchain*. 
Bitcoin's transactions are programmable, but its underlying scripting language is very limited.

In the summer of 2015, *Ethereum* was launched. The Ethereum blockchain offers a *Turing Complete* runtime environment called the Ethereum Virtual Machine (*EVM*). 
Programs that are written and deployed to the Ethereum blockchain are called *smart contracts*. Smart contracts on Ethereum are written in the high-level programming language *Solidity* and then compiled to EVM bytecode.

Ethereum made it easy for developers to not only store data of monetary transactions on a blockchain but to write and execute complete programs. Applications created in this decentralized manner are called decentralized applications (*Dapps*).

Learn more blockchain basics on [Open Tezos](https://opentezos.com/blockchain-basics).

Ethereum is struggling with a few challenges: Ethereum transactions are slow, expensive, and cost a lot of energy. Additionally, it is difficult to write secure smart contracts in Solidity and challenges with the protocol’s governance continue to cause a lot of friction in the community.

### Tezos
The first Tezos whitepaper was published in 2014. In 2017, the Tezos foundation raised funds to develop the Tezos blockchain protocol, and in 2018 the Tezos *mainnet* went live.

The Tezos protocol aims to address the challenges that Ethereum is facing.

To make transactions faster, cheaper, and more energy-efficient, Tezos relies on a different model than Ethereum 1.0 and Bitcoin for adding new transactions to its blockchain. The Tezos network adds new blocks of transactions and achieves consensus using a *Liquid Proof-of-Stake* (LPoS) instead of a *Proof-of-Work* (Pow) model.

Learn more about [LPoS](https://opentezos.com/tezos-basics/liquid-proof-of-stake) and [PoW](https://opentezos.com/blockchain-basics/proof-of-work) on Open Tezos.

Tezos features a governance model that is part of the protocol itself and allows the protocol to be upgraded when a proposal is approved through community voting. This self-amending *on-chain governance* helps prevent the protocol and the community from being split through hard-forks — which is what created Bitcoin and Bitcoin Cash or Ethereum and Ethereum Classic.

To make the development of secure smart contracts easier, Tezos smart contracts are written in a programming language that allows for formal verification, making contracts easier to test and to spot mistakes.

Learn more Tezos basics on [Open Tezos](https://opentezos.com/tezos-basics).

## 1.2 What is a Tezos wallet?

A cryptocurrency *wallet* is a software or hardware device that stores *private keys* — the passwords that give you access to your cryptocurrencies.

Most crypto wallets not only store your private keys but also enable you to send transactions and execute smart contracts.

The native cryptocurrency for the Tezos blockchain is called tez. To store and send tez tokens, you need to own a Tezos compatible crypto wallet.

You can find a list of audited Tezos wallets on [tezos.com](https://tezos.com/learn/store-and-use/).

To make the development and testing more straightforward for this course, we will use the [Temple](https://templewallet.com/) web wallet which you can install as a web extension for your browser.

In the next section, we are going to set up a Tezos wallet with Temple.

## 1.3 Create a Tezos wallet

In this section, we are going to walk you through the creation of a Tezos Temple wallet.

### Install Temple wallet
Before creating a Tezos wallet with Temple, we need to add the Temple extension to our browser. In this example, we will use the popular Chrome browser.

![](https://raw.githubusercontent.com/moritzfelipe/tezos-development-101/main/content/gifs/tezos_1_3_1_install_temple.gif)

1. Go to [templewallet.com](https://templewallet.com/).
2. Click on the “Install Now” button in the right corner of the page.
3. Select the browser that you are using, in this example, Chrome.
4. Click “Install” to open the browser extension in the Chrome Web Store and then click on the “Add to Chrome” button. 

### Create a new Tezos wallet
Once you have successfully installed the Temple wallet, you can proceed to create a Tezos wallet.

![](https://raw.githubusercontent.com/tacodeDev/dev-starter/main/content/gifs/tezos_1_3_2_create_wallet.gif)

1. Select the "Create a new Wallet" card in your browser extension.
2. Enter and repeat a password.
3. Next, accept the terms of usage. Of course, you should read them first.
4. In the next step, confirm that you have backed up your seed phrase. 

A *seed phrase* is a group of words used to encrypt your private key, making it more readable. You should store your seed phrase somewhere safe because it's the only way to recover your funds.

“Not your keys, not your coins” is a well-known saying suggesting that you don’t really own your digital assets unless you are in possession of the private keys/seed phrase for your wallet. Often a third party, like exchanges or payment providers, hold your private keys.

## 1.4 Use a Tezos wallet
In this section, we will show you how you can get tokens for the Tezos testnet, Florence, and how you can make a transaction with them.

### Get Tezos testnet tokens
![](https://raw.githubusercontent.com/tacodeDev/dev-starter/main/content/gifs/tezos_1_4_1_get_tokens.gif)

1. Open the telegram faucet bot [https://t.me/tezos_faucet_bot](https://t.me/tezos_faucet_bot).
2. Click on the “Get coins” button in the chat interface.
3. Copy the Tezos address of your account in the Temple wallet.
4. Send your Tezos address to the Telegram bot.
5. Change the network from the mainnet to the Florence Testnet.
6. Now, you should see 100 Testnet tokens in your wallet.

A testnet like Florence is Tezos test network. The mainnet is the main Tezos network. In contrast to the mainnet, transactions on the testnet don’t cost you anything, and Tezos tokens (tez) don’t have any real value. The testnet is a great place to test your contracts before deploying them to the mainnet.

There are different entities that can send you testnet tokens (*faucets*). You can find a list of them in the Tools section on the [Tezos homepage](https://tezos.com/developer-portal).

### Send Tezos testnet tokens
Now that you have received testnet tokens, you can make your first transaction.

![](https://raw.githubusercontent.com/tacodeDev/dev-starter/main/content/gifs/tezos_1_4_2_send_tokens.gif)

1. To test sending tokens, you need to create a second account.
2. Copy the address of your second account.
3. In the Temple wallet, switch back to your first account.
4. Click on the send transaction icon in the Temple wallet.
5. Paste the address of your second account in the address field, enter an amount and send the transaction.
6. You can then check out your transaction in the blockchain explorer.
7. After a couple of seconds, you should see the new balances in both of your accounts.

A *blockchain explorer* is an application that allows you to search data within a blockchain network. For example, you can search for any transaction that happened on the network. Learn more about blockchain explorers on [Open Tezos](https://opentezos.com/explorer).

Now that you have a brief understanding of Tezos, have created a crypto wallet, and have made your first transaction, you can continue to the next chapter, where you will write your first smart contract.
