## 3.1 Intro to Dapps
Applications that run on a distributed computing system are called *Dapps*, short for decentralized applications.

Let’s have a look at some attributes of Dapps.

**Decentralization**
Because they run on a distributed computing system, there is no single entity that can stop Dapps or delete their data. This is also called *censorship resistance*. 

**Transparency**
Since Dapps run on an open platform, everyone can read the source code of a Dapp and look into the transaction history. This enables trust because users can find out how an application will behave, and it fosters innovation because anybody can fork a Dapp and create their own version.

**Costliness**
Smart contract code has to be executed through transactions and is then synchronized on the whole network. Users have to pay for these transactions when they interact with a smart contract. This makes Dapps more expensive to use than regular apps and also slower.

When developing Dapps it is useful to think about these attributes and find application eras where decentralization and transparency are important and are worth higher costs.

Learn more about Dapps on [Open Tezos](https://opentezos.com/dapp).

In contrast to typical applications that run backend code on centralized servers, Dapps run their backend code on a decentralized peer-to-peer network, such as Tezos. As we learned before we call the backend code that runs on blockchain-based platforms smart contracts.

A Dapp does not only need backend code in the form of smart contracts but also frontend code to create user interfaces that can make calls to smart contracts. We will learn how to build the frontend for a Dapp in this chapter.


## 3.2 Initializing the Taquito Boilerplate Dapp
In this section of the chapter, we will show you how to get started with the Taquito Boilerplate in React and how to interact with a Tezos Dapp through your Temple wallet.

Before we get started let's learn a bit more about Taquito.
Taquito is a TypeScript library suite that will help you build web interfaces for your Dapp. We will use Taquito to connect our Dapp to the user’s wallet, to make transactions, and to interact with a contract. Taquito is your Dapp’s connection to the Tezos blockchain.

You can learn more about Taquito on the [Taquito website](https://tezostaquito.io/) or on [Open Tezos](https://opentezos.com/dapp/taquito).

In this chapter, we will go through the Taquito boilerplate and look into the most important functionality of Taquito. In this section, we will clone the boilerplate repository, install the dependencies, and start and test the functions of the Dapp.

1. Open your command-line interface.
2. Clone the boilerplate repository.
```
git clone https://github.com/ecadlabs/taquito-react-template.git
```

3. Navigate to the new repository.
```
cd taquito-react-template
```

4. Install all dependencies.
```
npm install
```

5. Start a local development server.
```
npm run start
```

Your project should be running at http://localhost:3000/.

Hint: If you have problems starting the Dapp, because of an HTTPS error. In the package.json under scripts, change line 25 from `"start": "HTTPS=true react-scripts start",` to `"start": "react-scripts start",`.

For this Dapp we will use the simple increment/decrement contract that you have seen before.

```
type storage = int
type parameter =
  Increment of int
| Decrement of int
 
type return = operation list * storage
 
let add (n, s : int * storage) : storage = n + s
let sub (n, s : int * storage) : storage = n - s
 
let main (p, s : parameter * storage) : return =
 ([] : operation list), 
 (match p with
   Increment n -> add (n, s)
 | Decrement n -> sub (n, s))
```

```python
# TODO: very and write proper test
import smartpy as sp

class Counter(sp.Contract):
    def __init__(self, value):
        self.init(counter = value)

    @sp.entry_point
    def increment(self, params):
        self.data.counter += params.value

    @sp.entry_point
    def decrement(self, params):
        self.data.counter -= params.value

    @sp.offchain_view(pure = True)
    def get_counter(self, req):
        sp.result(self.data.counter)

@sp.add_test(name = "Counter")
def test():
    c1 = Counter(0)
    scenario = sp.test_scenario()
    scenario += c1
    #c1.increment(1)
    #scenario.verify(c1.data.counter == 1)
```

You can test and if you want even deploy it in the [LIGOlang IDE](https://ide.ligolang.org/p/LhrUay2LusUXBiqiEhU4iA) or your CLI
> [name=gabriela]maybe a gif to visually explain how to deploy the contract? and maybe suggest a function name from which the contract should start and suggested initial storage

Before we look into how the frontend is built we will test the functionality of this Dapp. We will connect our wallet, make a transfer and interact with the contract.

**Connect wallet**
//GIF

**Make transfer**
//GIF

**Interact with contract**
//GIF

Now that you know what the Dapp can do, lets look into what is happening under the hood.

## 3.3 Connecting your Dapp to the blockchain
In this section, you will learn how to connect your Dapp to a wallet and how to read out the user’s address and tez balance.

Let’s open src/App.tsx and have a look at what we are importing.

```
import React, { useState } from "react";
import { TezosToolkit } from "@taquito/taquito";
import "./App.css";
import ConnectButton from "./components/ConnectWallet";
import DisconnectButton from "./components/DisconnectWallet";
import qrcode from "qrcode-generator";
import UpdateContract from "./components/UpdateContract";
import Transfers from "./components/Transfers";
```

Among other things, we are importing the `useState` hook from `React` to add state to our components, the *TezosToolkit* which contains the functionality of the Taquito library, and our components. In the `ConnectButton` component, we will handle our most important functionality, connecting to the user's wallet and reading out the state we need. `UpdateContract` will handle the user’s interactions with the contract and `Transfers`, the functionality of making a transaction.

```
const App = () => {
  const [Tezos, setTezos] = useState<TezosToolkit>(
    new TezosToolkit("https://api.tez.ie/rpc/florencenet")
  );
  const [contract, setContract] = useState<any>(undefined);
  const [publicToken, setPublicToken] = useState<string | null>("");
  const [wallet, setWallet] = useState<any>(null);
  const [userAddress, setUserAddress] = useState<string>("");
  const [userBalance, setUserBalance] = useState<number>(0);
  const [storage, setStorage] = useState<number>(0);
  const [copiedPublicToken, setCopiedPublicToken] = useState<boolean>(false);
  const [beaconConnection, setBeaconConnection] = useState<boolean>(false);
  const [activeTab, setActiveTab] = useState<string>("transfer");
```

Next, we are handling our state. First, we declare our state variable `Tezos` and the function `setTezos` that we use to update `Tezos`. We then use the `useState` hook to set the initial value of `Tezos`, we instantiate the `TezosToolkit` with an RPC URL. In our case, we will operate on the Florence testnet.

Our most important state variables: `contract`, `wallet`, `userAddress`, `userBalance` and `storage` will all be empty initially. Their purpose should be self-explanatory from their naming.

We create a constant `contractAddress` that contains the address of increment/decrement contract.

```
  // Florencenet Increment/Decrement contract
  const contractAddress: string = "KT1XCAdyQsHuNTkeLJes7R3krmGhtsmoBvNz";
```

Now we will go through the code by following the flow of the Dapp.
There are three different states for the div with the class main-box that we use to display content to the user.

In the first state the user loads our Dapp for the first time and won’t be connected to their wallet.
We have one state where the user clicked on the connect button but didn’t connect their wallet yet and a third state, where the user is connected.

Once the user pairs our Dapp with BeaconWallet we will get `publicToken` and when they connect to their wallet account we will get `userAddress` and `userBalance`.

Let's look at the disconnected state first, where we haven't set `publicToken`, `userAddress`, and `userBalance` yet (Line 170).

```
  } else if (!publicToken && !userAddress && !userBalance) {
```

For now, we have some greetings and explanatory text, but most importantly our `connectButton` component on line 202, where we pass the state and callback functions to update the state from inside our component.

```
          <ConnectButton
            Tezos={Tezos}
            setContract={setContract}
            setPublicToken={setPublicToken}
            setWallet={setWallet}
            setUserAddress={setUserAddress}
            setUserBalance={setUserBalance}
            setStorage={setStorage}
            contractAddress={contractAddress}
            setBeaconConnection={setBeaconConnection}
            wallet={wallet}
          />
```


Let's look into the component. Open src/components/connectWallet.tsx.

We start on line 85, when the user loads the Dapp an async function is executed that creates a wallet instance.

```
    (async () => {
      // creates a wallet instance
      const wallet = new BeaconWallet({
        name: "Taquito Boilerplate",
        preferredNetwork: NetworkType.EDONET,
        disableDefaultEvents: true, // Disable all events / UI. This also disables the pairing alert.
        eventHandlers: {
          // To keep the pairing alert, we have to add the following default event handlers back
          [BeaconEvent.PAIR_INIT]: {
            handler: defaultEventCallbacks.PAIR_INIT
          },
          [BeaconEvent.PAIR_SUCCESS]: {
            handler: data => setPublicToken(data.publicKey)
          }
        }
      });
```

The BeaconWallet package is the recommended way to connect your Dapp to a wallet. It implements the TZIP-10 standard that describes the communication between wallet and Dapp. It works with any wallet supporting TZIP-10, such as the Beacon extension, Temple, or Kukai.

The necessary bare minimum to instantiate the wallet is an object with a name property that contains the name of your Dapp. We also need to specify that we want to connect to the Florence testnet.

Next, we use event handlers, most important here for the event PAIR_sucess. When the user successfully pairs their wallet, we update the state variable `publicToken` through the callback function `setPublicToken` with `data.publicKey`.

```
      Tezos.setWalletProvider(wallet);
      setWallet(wallet);
      // checks if wallet was connected before
      const activeAccount = await wallet.client.getActiveAccount();
      if (activeAccount) {
        const userAddress = await wallet.getPKH();
        await setup(userAddress);
        setBeaconConnection(true);
```

Even if the user has not paired their wallet yet, we use our new wallet object to set it as a wallet provider for our `TezosToolkit` instance `Tezos`. We also set the wallet object for our `wallet` state variable with the `setWallet` callback function.

In the next lines, we check through the wallet method `getActiveAccount` if the user is already connected. The user might just have closed the Dapp but remained connected, then they will still have an active account. We can check this with the wallet `getActiveAccount` method.

If the user is connected we can get their address with the wallet method `getPKH`.
We use the address of the user as an argument for our setup function.

Let's look at the setup function at line 39.

```
  const setup = async (userAddress: string): Promise<void> => {
    setUserAddress(userAddress);
    // updates balance
    const balance = await Tezos.tz.getBalance(userAddress);
    setUserBalance(balance.toNumber());
    // creates contract instance
    const contract = await Tezos.wallet.at(contractAddress);
    const storage: any = await contract.storage();
    setContract(contract);
    setStorage(storage.toNumber());
  };
```

We update our state variable `userAddress` through the `setUserAddress` callback function and with the `userAddress` argument.

In the next line, we get the balance of the user through the `TezosToolkit` method `getBalance` and update our `userBalance` state variable.

Next, we create a contract instance of the increment/decrement contract. Then we use the contract `storage` method to get the storage of the contract. We update the `contract` state variable with the `setContract` callback function passing the contract instance, and update the `storage` state variable. Since in this contract the storage is just one integer we can simply use the JavaScript `toNumber()` method to display the current number that is stored to the user.

This was the most important function that updated a lot of our state variables.
But we not only call the setup when the user is already logged in, but also if the user clicks on the “Connect with wallet” button (line 116).

```
      <button className="button" onClick={connectWallet}>
        <span>
          <i className="fas fa-wallet"></i>&nbsp; Connect with wallet
        </span>
      </button>
```

If the user clicks on the “Connect with wallet” we call the `connectWallet` function (line 51)

```
  const connectWallet = async (): Promise<void> => {
    try {
      await wallet.requestPermissions({
        network: {
          type: NetworkType.FLORENCENET,
          rpcUrl: "https://api.tez.ie/rpc/florencenet"
        }
      });
      // gets user's address
      const userAddress = await wallet.getPKH();
      await setup(userAddress);
      setBeaconConnection(true);
    } catch (error) {
      console.log(error);
    }
  };
```

We already updated our `wallet` state variable with the wallet instance when the Dapp is loaded. Now we need to wait until the user has given permission to connect its wallet to the Florence testnet. If so, we get the user address as before and call our setup function again.

That’s it! Our user is connected and all state variables are set.

## 3.4 Create a tez transaction
In this section of the chapter, you will learn how to make a tez transaction with your Dapp.

Let's get back to our App.tsx.
If the user has connected to the Dapp with their wallet we will have the values of our state variables `userAddress` and the `userBalance`.

The user will then be able to view a different state of our Dapp, starting on line 92.

```
  } else if (userAddress && !isNaN(userBalance)) {
```

The content div with the class main-box will look different.
We have two tabs, one to make a transfer and one to interact with the contract. 
Let's look at how to make a transfer first, the tab with the id `transfers` (line 115).

```
              <div id="transfers">
                <h3 className="text-align-center">Make a transfer</h3>
                <Transfers
                  Tezos={Tezos}
                  setUserBalance={setUserBalance}
                  userAddress={userAddress}
                />
              </div>
```

We pass our `TezosToolkit` and the `userAddress` to the Transfers component and update the `userBalance` from within it after we make a transaction.

Let's look into the transfer component in src/components/Transfers.tsx.

On line 39, start the input fields.

```
      <input
        type="text"
        placeholder="Recipient"
        value={recipient}
        onChange={e => setRecipient(e.target.value)}
      />
      <input
        type="number"
        placeholder="Amount"
        value={amount}
        onChange={e => setAmount(e.target.value)}
      />
      <button
        className="button"
        disabled={!recipient && !amount}
        onClick={sendTransfer}
      >
```

The user needs to input the address of the recipient and the amount they want to transfer.
If the user clicks the button we execute the `sendTransfer` function.

Let's look at the `sendTransfer` function on line 17.

```
  const sendTransfer = async (): Promise<void> => {
    if (recipient && amount) {
      setLoading(true);
      try {
        const op = await Tezos.wallet
          .transfer({ to: recipient, amount: parseInt(amount) })
          .send();
        await op.confirmation();
        setRecipient("");
        setAmount("");
        const balance = await Tezos.tz.getBalance(userAddress);
        setUserBalance(balance.toNumber());
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    }
  };
```

If we have the address of the recipient and an amount to send, we can use the wallet transfer method to make the transaction. The transfer must then be sent using the send method, which returns a promise. We then call the confirmation method and pass the number of confirmation we want to wait. Let’s leave it at the default value: one. When the promise is resolved and we got a confirmation we empty our recipient and amount values and update the `userBalance` state variable as we have already done before.

Learn more about making transactions in the [Taquito documentation](https://tezostaquito.io/docs/wallet_API#making-transfers).

## 3.5 Contract interactions
In this section, we will show you how to interact with the increment/decrement contract through your Dapp.

Let's look into the second tab of our main content div in App.tsx. It has the id `increment-decrement` (line 124).

```
              <div id="increment-decrement">
                <h3 className="text-align-center">
                  Current counter: <span>{storage}</span>
                </h3>
                <UpdateContract
                  contract={contract}
                  setUserBalance={setUserBalance}
                  Tezos={Tezos}
                  userAddress={userAddress}
                  setStorage={setStorage}
                />
              </div>
```

First, we read out the state variable `storage`. As you remember we converted the storage of the contract to a number when we connected to our wallet. This storage just stores an int and is easy to display.

We pass our `TezosToolkit`, the `userAddress`, and the contract instance of our increment/decrement contract to the `UpdateContract` component. We update the `userBalance` and `storage` state variables from within the component because once the user will interact with the contract, its storage will change and the user will have to pay for that, so their balance will change too.

Let's look into the UpdateContract component in src/components/UpdateContract.tsx.

There are two buttons, `increment`, and `decrement`, starting on line 48. 

```
 <div className="buttons">
      <button className="button" disabled={loadingIncrement} onClick={increment}>
        {loadingIncrement ? (
          <span>
            <i className="fas fa-spinner fa-spin"></i>&nbsp; Please wait
          </span>
        ) : (
          <span>
            <i className="fas fa-plus"></i>&nbsp; Increment by 1
          </span>
        )}
      </button>
      <button className="button" onClick={decrement}>
        {loadingDecrement ? (
          <span>
            <i className="fas fa-spinner fa-spin"></i>&nbsp; Please wait
          </span>
        ) : (
          <span>
            <i className="fas fa-minus"></i>&nbsp; Decrement by 1
          </span>
        )}
      </button>
    </div>
```

They look pretty similar. Let's look at what happens when the user clicks on the increment button and we call the async `increment` function, which is defined on line 16.

```
  const increment = async (): Promise<void> => {
    setLoadingIncrement(true);
    try {
      const op = await contract.methods.increment(1).send();
      await op.confirmation();
      const newStorage: any = await contract.storage();
      if (newStorage) setStorage(newStorage.toNumber());
      setUserBalance(await Tezos.tz.getBalance(userAddress));
    } catch (error) {
      console.log(error);
    } finally {
      setLoadingIncrement(false);
    }
  };

```

We have the abstraction of our increment/decrement contract from our `contract` state variable and we can call its entrypoints as methods. In this case, we call the `increment` entrypoint and pass the argument 1, since we just want to increase the `storage` by 1. Then we call the `send` method and send the transaction. Once we get one confirmation we update the storage and the user balance.

Learn more about interactions with contract entrypoints in the [Taquito documentation](https://tezostaquito.io/docs/wallet_API#--contract-entrypoint-arguments).

There is one more component that we didn’t look into, the `DisconnectButton` component. If the user is connected and clicks on the “Disconnect wallet” button, we empty all state variables and create a new `TezosToolkit`.

And we are done. That was the most important functionality of the Taquito Boilerplate and should give you the tools to create your own Dapp.

In the next chapter, we will show a concrete example of how to tweak the boilerplate a little to adjust it to the needs of a custom contract.
