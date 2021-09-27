## 2.1 Intro to Tezos Smart contracts
In this brief intro, we will introduce you to Tezos smart contracts and give you a short overview of the different smart contract languages on Tezos.

**Smart contracts**
A *smart contract* is computer code that is stored and runs on a blockchain-based platform. Since data stored on blockchains is *immutable* (unchangeable), the code of smart contracts becomes immutable too once deployed to the network.

This enables smart contracts to execute agreements automatically based on predefined conditions with a dependable outcome independent of third-party involvement. 

On Tezos, smart contracts are a type of *account* with an *address* that can store code, have a *balance*, and send *transactions*. Users of smart contracts can interact with them by submitting transactions to the smart contract that execute functions as defined in the smart contract.

Learn more about smart contracts on [Open Tezos](https://ligolang.org/docs/language-basics/sets-lists-tuples#sets).

**Michelson**
In Tezos, the low-level machine language that runs smart contracts on the Tezos network is called *Michelson*. The language is stack-based, with high-level data types and primitives, and strict static type checking.

Learn more about Michelson in the [Tezos Documentation](https://tezos.gitlab.io/active/michelson.html).

Since it’s hard to get started writing in a low-level language, there are different high-level languages in the Tezos ecosystem that compile to Michelson.

*LIGO* comes in four different syntaxes, *Camel*, *Pascal*, *Reason*, and *Javascript*. 
*SmartPy* is inspired by Python. 
*Morley* was the first high-level language developed for Tezos.

In this course, we will focus on LIGO and SmartPy.

**LIGO**
LIGO is great because it is statically-typed and *CameLIGO* and *ReasonLIGO* allow you to write in a functional style, which helps you avoid mistakes and create more secure code which is crucial when writing smart contracts.
In this course, we will work with CameLIGO, which is inspired by the functional language *OCaml*. Many contracts developed by the Tezos community are developed in OCaml which is the language of choice for many professional developers.

Learn more about LIGO in the [LIGO Documentation](https://ligolang.org/docs/intro/introduction).

**SmartPy** 
SmartPy is a great starting point if you are familiar with Python and want an easy entry.
SmartPy adds another abstraction layer; it compiles to SmartML, which is written in OCaml, which is then compiled to Michelson.

Learn more about SmartPy in the [SmartPy Documentation](https://smartpy.io/reference.html).

For the following sections of this chapter, you will how to write Tezos smart contracts in SmartPy. This chapter is also available for cameLIGO.

## 2.2 Introduction to SmartPy
*SmartPy* is a high-level Python smart contract library. SmartPy allows us to use Python to write programs that can construct smart contracts (*Meta-programming*).

Python is one of the most popular programming languages in the world. As of August 2021, it is ranked as the second most popular programming language on the TIOBE Programming Community Index; just behind C.

Using such a popular language helps developers who have no experience with smart contract development to get started easily. They don’t have to learn a completely new language, which is the case for most other smart contract languages.

SmartPy also offers a set of tools that enhance the smart contract development experience; especially for beginners.

**Compiler**
Once built, SmartPy contracts become SmartML contracts, written in OCaml that can be compiled into Michelson (Learn more about SmartML on [OpenTezos](https://opentezos.com/smartpy)). The Michelson contract can then be deployed on a Tezos network. 

**Analytics**
Executing functions on a smart contracts is much more expensive than running code on your local computer or using traditional cloud computing providers. To execute a function and change the state of the contract you have to create a transaction that you have to pay for.

Because of their transparent, immutable nature, smart contracts are often used to communicate value, e.g. in the form of monetary tokens and financial applications. This makes them prone to attacks and poses severe security risks.

Another issue is the immutability itself, once deployed you will be not able to change or update your code.

The SmartPy analytics tools allow simulation, debugging and testing of smart contracts to improve the experience for developers to create secure contracts.

**SmartPy.io**
SmartPy features an online editor with an integrated development environment (IDE) that can be reached under smartpy.io. The compiler and analytics can be accessed and used on [smartpy.io](https://smartpy.io/ide). In the following section, we will give you a quick introduction to this IDE.

**SmartPy CLI**
SmartPy also features a command-line interface that is called smartpy-cli that can be used to execute SmartPy Scripts and its tests as well as to compile and deploy smart contracts.

## 2.3 Introduction to the IDE
In this section, we will give you an introduction to the SmartPy IDE.

You can reach the SmartPy IDE under https://smartpy.io/ide.

Let's have a quick tour of the IDE. We start with the top middle bar next to the SmartPy logo.

**Top middle bar**
![](https://i.imgur.com/sNCrPLv.gif)

With the first icon that looks like a sun, you can toggle between a light and dark theme. Next to it, you can find the logos of Python, TypeScript, and Michelson, each one allowing you to switch between the different languages to use in the IDE. Please be aware that the TypeScript version is currently still in Beta mode.

**Top right bar**
![](https://i.imgur.com/EBo9PlL.gif)

On the top right bar, you can switch between the "EDITOR", the "EXPLORER", the "WALLET", and a "HELP" section. 
We will spend most of our time in the editor view where you can create and edit your contract. 
The explorer allows you to load contracts on the network and interact with them.

In the wallet view, you can set up a wallet that will allow you to interact with contracts and deploy your contracts. It is very easy to create your account and get free tokens for the testnet through the faucet importer.

When you click on the last button in this bar you will be directed to a help section where you get links to the documentation, to a telegram group of Tezos developers, and the Tezos StackExchange among other things.


**The editor**
![](https://i.imgur.com/A8f1gPS.gif)

You encounter four buttons on the top right of the editor: "TEMPLATES", "TOOLS", "SHARE", and "SETTINGS".

When clicking on the "TEMPLATES" button you open a modal that allows you to select between multiple helpful templates. As a beginner, it's helpful to click on the "REGULAR TEMPLATES" tab and then select "Simple Examples". You can click on the "Store Value contract" for example and then import the contract to your editor.
The templates are a great way to explore SmartPy code.

The "TOOLS" button allows you to download the contract and the content of the output panel as well as loading contracts from your disk.

With the "SHARE" button, you can share your code with other people, this is helpful to get quick feedback on your code.

With the "SETTINGS" button, you can change the UI and toggle the newcomer mode.

Now we are coming to the most important part of the editor, where you will spend the most time.

![](https://i.imgur.com/ERtezqb.gif)

At the top of the editor, you will find the RUN button. With the "RUN" button, you can build and compile the contract and run tests. If you have done so you will be able to select with the "TESTS" button on the right, between Compilations and Tests. With the trash icon right to it you delete the content displayed in the output panel.

If you have a contract in your code editor and then click on the "RUN" button, you will see content displayed in the output panel to the right of your code editor.

In the automatically selected "SmartPy" tab, you will see the balance, storage, and code of your contract. If you scroll further down you will see the output of your tests.

By clicking on the "Types" tab next to the SmartPy tab you will be able to see the types used in the contract. Since SmartPy uses type inference this can be helpful. 

The last tab at the top of the output panel, "Deploy Michelson Contract", allows you to see the compiled Michelson code of your contract and to deploy it to a main or test net by clicking on the "Deploy Michelson Contract" button.


## 2.4 "Hello, World!"
Before we get started with our contract, we are going to create a simple test so that you can get used to the IDE. We will use tests throughout this chapter to make sure that our smart contracts are working as intended. Test scenarios can describe a sequence of actions, e.g. originating contracts, computing expressions, or calling entry points.

Let's create our first test, for now without a contract.

**Tests**

```
import smartpy as sp
 
@sp.add_test(name = "myTest")
def test():
    scenario = sp.test_scenario()
    scenario.p("Hello World!")
```
Test this in the [SmartPy IDE](https://smartpy.io/ide?code=eJzLzC3ILypRKM5NLCopqFRILFYoLuBS4HIoLtBLTEmJL0ktLtHIS8xNVbBVUMqtDAFylTS5UlLTFMAymlZcCkBQnJyal1iUmQ9UBNQHkomHCWlooqjQK9BQ8kjNyclXCM8vyklRVNIEAOffKes-).

In the first line, we import our SmartPy library.

Now we use the `sp.add_test` to create a new test, we call it `myTest`.
We need to define our test and use the `sp.test_scenario()` function from the library to define a new scenario that we call `scenario`.

In the next line, we create the content of our test, since we dont have a contract at the moment we need some other information that we can display.

We add document information, in this case, the HTML `p` element, to display the string `"Hello World!"`.

If you click on "RUN" button, the scenario is computed and then displayed as an HTML document on the output panel on the right side next to the editor. You should now see the output "Hello World".

Learn more about tests in the [SmartPy documentation](https://smartpy.io/docs/scenarios/framework).

**Contracts**
A Tezos smart contract usually consists of a state that is stored on the blockchain and entry points; methods that can be called from outside the contract to interact with the contract.

In our first step we will just create a contract with a state but no entry point.

```
import smartpy as sp
 
class myContract(sp.Contract):
    def __init__(self, params):
        self.init(storage = params)
```

We import SmartPy and in the next line create our contract. It is a class definition that inherits from the contract class of the SmartPy library, we call it `myContract`.

A Python class is like a template for creating a new object and when we create a new class that inherits from that object it also provides us with the same methods and properties of the class, in this case of `sp.Contract`.

Now we need to create the storage of our contract. We create a constructor `__init__` with the parameter, `params` that calls `self.init` to initialize the contract storage. In this case, consisting of `storage` that gets assigned the value of the constructor parameter.

Let’s add a test to our contract.

```
import smartpy as sp

class myContract(sp.Contract):
    def __init__(self, params):
        self.init(storage = params)

@sp.add_test(name = "MyContract")
def test():
    scenario = sp.test_scenario()
    contract = myContract("Hello World!")
    scenario += contract
    contract
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJxVjr0KwzAMhHc_herJoSUPUAgUunTp3NEI2ykG_2FpydvXDkloNAndd3fyseTKQBErlwWQgIoQJiARxOWZE1c0rKiM@z7cBbSxbgatffKstSIX5hsUrBhp0_v089gRRZwrfh1MOyTEo2WitZodsUoYuyjfR6UcRK9Y1S2SjEtYfW5g83ZF7yc1rITZzI34e16@XAgZPrkGe5HDOes6Ha5TxA8YzVtV).

We create the test as we did in the example before, we initiate a new testing scenario and then our contract with the string `"Hello World"` as the initial value of the state.

In the next line we add this contract to the scenario and then execute the contract.
Now when we test this contract we can see the value of the storage, which should be "Hello World!".

Learn more about contracts in the [SmartPy documentation](https://smartpy.io/docs/introduction/contracts).

Let's add an entry point to this contract.

**Entry Points**
As we mentioned before, entry points are methods of a contract that can be called from outside the contract. They are usually used to interact with the contract and change its state.

We will add an entry point to our contract that can change the value of the storage.

```
import smartpy as sp
 
class MyContract(sp.Contract):
  def __init__(self, params):
      self.init(storage = params)
 
  @sp.entry_point
  def greet(self, params):
    self.data.storage = params
 
@sp.add_test(name = "MyContract")
def test():
  scenario = sp.test_scenario()
  contract = MyContract("Hello")
  scenario += contract
  contract.greet("Hello World!")
```

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJxtkL0KwyAQx_c8xdXJ0JIHKAQKXbp07ihHvAbBqHi35O2rSdOGUif5f_zu1E0pZgGeMEuaARk4NdAMHpnhPl9jkIyDaE7ddm_PDYClJxjjghNjNJN_niBhxokXt54qdjWgWWLGkaDfImUAwKUgqRBnk6IL8maOmUj@ARecRcHuF1dolYXWGiEWHXCqpvpur9qmshd3wfFAAbOLJVaaVTebpMt2MLyLxd_9gbqR91G1e8Cx_4R3vW59xlqAR8zeHlT7AgVId_g-).

Most of the code stays the same, but we add an entry point, marked with the `@sp.entry_point` decorator. We create an entry point called `greet` that saves the input from our parameters to the storage.

In the test, we initiate our contract just with the string `"Hello"` and then call our entry point, greet with the argument "Hello World!" and change the value of the storage.

If you test the contract your output should look like this:
![](https://i.imgur.com/dpMKyG0.png)


And that’s it for your first contract. In the next section we will look into different data types.

## 2.5 Data Types
In this section, we are going to look into the most important simple Tezos data types and their usage.

**Type Inference**
In SmartPy as in Python you don’t need to specify the types of objects. However the contracts that you write in SmartPy will be compiled to Michelson and Michelson requires types. Therefore SmartPy automatically detects the types of expressions (Type Inference).

Let's see this in action.

```
import smartpy as sp
 
class MyContract(sp.Contract):
  def __init__(self):
      self.init(storage = "Test")
 
  @sp.entry_point
  def greet(self, params):
    self.data.storage = params
 
@sp.add_test(name = "MyContract")
def test():
  scenario = sp.test_scenario()
  contract = MyContract()
  scenario += contract
  contract.greet("Hello Alice!")
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJxNj7EOwjAMRPd@hemUCtQPQEICsbCwsUdWalCkNIliL_17nFCgmZLz3fPFzzkVAZ6xSF4AGTh30LmAzHBfrilKQSeG8_i9D8cOYKInWOujF2sNU3g2tZ76GOvAsKSCL4IT9A9i6QcFA5wVRUpabE4@ysp6FSJpoANkLDjzCmy4CQXHP@5jUFpl4TRZUbyJOLdd_9a6sbLbtOHYUcTik9o0WXX7lYy2A7cGdb75@7BN7k8_1yYwfvr3NwohwSV4R7t@eANM2nIm).

In this simple contract, as in the "Hello World!" example contract, we don’t define the type of storage when we assign it a value. In this case the value `"Test"`. SmartPy automatically detects a string and declares `storage` as such. 

In our test, we assign storage a new value and since this value is also a string our test doesn't raise any errors.
If you replace `contract.greet("Hello Alice!")` with `contract.greet(4)` you will get an error that the parameter is of the wrong type.

**Type constraint**
We can constrain the storage type with the method `self.init_type(t)`. This will make the storage type explicit, it also allows you to define storage-less contracts.

Constraining the storage type will help you to write cleaner contracts and is appreciated by many developers, especially when dealing with larger contracts.

```
import smartpy as sp

class MyContract(sp.Contract):
    def __init__(self):
        self.init_type(sp.TRecord(storage = sp.TString))
        self.init(sp.record(storage = "Hello World!"))
 
    @sp.entry_point
    def greet(self, params):
        self.data.storage = params
 
@sp.add_test(name = "MyContract")
def test():
  scenario = sp.test_scenario()
  contract = MyContract()
  scenario += contract
  contract.greet("Hello Alice!")
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJxlkLFuxCAMhvc8Bc0EapUHqHRSqy5dbmkrdUQW@CIkAsj2krcvkNxddGWC3_5@_DssJZMoXoCkrApYcRkGF4FZndePnITAieYyXe_mdVD1eLwoa0MKYq1mjJddb6c9p16StWCDf77QZfKaJRPMqE6qid9CIc3G_AcbQ4_I@IkxZvWbKfqnsWEdfKu9WGdbbckhyW26mRClj_aiChAs_DiiB4Hp7r81VdfmCN5bQRadYOmf37cxmqH592q3ZIcJKOQtVtPtVdItnNvBWj_s1BzJ59Ot6wBMW4Y9@HsMDmvwPyqIjG8-).

With `init_type` we can set the storage type and in the next line initiate the storage with the `init` method.

Ok now let's have a look at some basic types.

**String**
A string is a sequence of characters.
Strings in SmartPy can be defined via quotation marks `"..."` or `'...'`, or by using `sp.string(s)`.

```
 my_name = "alice"
 my_name = 'alice'
 my_name = sp.string("alice")
```

Strings can be *concatenated* (joined) using the `+` operator.

```
name = sp.string("Alice")
greeting = sp.string("Hello")
full_greeting = sp.string(greeting + name) # "Hello Alice"
```

Substrings can be extracted using the built-in function `sp.slice`, this is also called *slicing*. The first character has the index 0. Keep in mind that it returns an option and needs to be converted back to string or fail with `open_some`.

```
sp.slice("Hello World", 0, 5) # sp.some("Hello")
```

Let's create a contract so you can test and play around with `sp.slice`.

```
import smartpy as sp
 
class MyContract(sp.Contract):
    def __init__(self):
        self.init(
            storage = "Hello World!"
        )
    @sp.entry_point()
    def slice_storage(self,params):
        s = self.data.storage
        n_s = sp.slice(s, params.a, params.b).open_some("Slicing failed.")
        self.data.storage = n_s
 
@sp.add_test(name = "MyContract")
def test():
    contract = MyContract()
    scenario  = sp.test_scenario()
    scenario += contract
    scenario += contract.slice_storage(a = 0, b = 5)
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJx1ULFuxCAM3e8r3EygRqhLl0onVepyS6cOHZEvkBMSAYRZ8vc1JEdzleoF4_f8nm23pJgL0IK5pBWQgNIJTpNHIvhcP2IoGaciKKl7Lt9OwGHsDFq74IrWgqyf93qN@lUVEr3UyiVmvFk4w3Cx3kf4jtmbp6GTZMve2cyy16pTdKEI2f3Iu8nqXaaZjgkzLnT0Zvnmb7Cg2rkdDbrhSTUpQSNsAgp7dpUqJsvEuFgxfDHPhRvM6Lw1apCPSx5NWJi7@Hp1ATRGF0tFBFzaxr_HZI26TEP3wacdYuLh6JsXTTZgdhG2wWubvtf@Up7PXepfQD1eEVn2ZYQrP6_yBwBHoWU-)

The length of a string can be found using the built-in function `sp.len`.

```
name = sp.string("Alice")
length = sp.len(name) # length = 5
```

**Numerical Types**
SmartPy offers three built-in numerical types: `int`, `nat`, and `tez`.

Int Values of type `int` are *integers* also called *signed integers*. They can be positive, negative, or zero.
```
a = sp.int(42)
b = sp.int(-3)
c = sp.int(0)
```

Nat Values of type `nat` are *natural integral numbers*; they are also called `unsigned integers`. They can’t have a negative value. 
```
a = sp.nat(7)
b = sp.nat(0)
```

Tezos tokens can be described like this.
```
a = sp.tez(1)
b = sp.tez(3)
```

```
c = sp.tez(1.3)
d = sp.tez(3.3)
```

Mutez are the unit of millionth of tez. In SmartPy `sp.TMutez` is the type of amounts.
```
e = sp.mutez(1000000)
```

You can use underscores to improve readability when defining large numbers.
```
f = sp.mutez(1000_000)
```

You can cast (convert) an `int` to a `nat` and the other way around.
```
a = int(1)
b = abs(1)
```

You can check if a value is a `nat` with `sp.is_nat`. It accepts an int and returns an optional nat. If the input is not a nat it returns none.
```
is_a_nat = sp.is_nat(3).open_some("Is not a nat")
```

In the next section, you will learn how to do simple arithmetics with these numerical types.

**Boolean**
A boolean has one of two possible values: True or False.
```
user = sp.bool(True)
admin = sp.bool(False)
```

**Address**
The address type describes an address of a contract or implicit account.
```
my_account = sp.address("tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx")
```

**Timestamp**
A timestamp can be defined via the method `sp.timestamp(i)`.
```
date = sp.timestamp(0) # Thu, 01 Jan 1970 00:00:00 GMT
```

You can obtain the starting time of the current block using the built-in function `sp.now`.

```
block_time = sp.now
```

Let's implement it into a contract, to see it in action.

```
import smartpy as sp

class MyContract(sp.Contract):
    def __init__(self):
        self.init_type(
            t = sp.TRecord(storage = sp.TOption(sp.TTimestamp))
        )
        self.init(
            storage = sp.none
        )
 
    @sp.entry_point()
    def add(self):
        self.data.storage = sp.some(sp.now)
 
@sp.add_test(name = "MyContract")
def test():
    # define a contract
    contract = MyContract()
    scenario  = sp.test_scenario()
    scenario += contract
    scenario += contract.add().run(now = sp.timestamp(1571761674))
```

We need to initiate the contract with a timestamp that we dont have at the time of initiation, we use the option type and then initiate it with the value none.

Seconds, minutes, hours and days can be added via built-in functions.

```
some_date = sp.timestamp_from_utc(2009,1,3,0,0,0)
one_day = sp.int(86_400)
one_day_later = some_date.add_seconds(one_day)
```

Timestamps can also be subtracted.
```
new_date = sp.timestamp(1571761674) - sp.timestamp(1571751421)
```

Please be aware that it is up to the baker (validator of a block) to set the current timestamp value.

**Unit**
The unit type has only one value that carries no information, it is generally used as a placeholder.
You use the unit type also for entry points with empty parameters and get it returned as the return type of commands.

```
u = sp.unit
```

## 2.6 Math
In the previous section, you were introduced to the built-in numerical types: `int`, `nat`, and `tez`. In this section, we will look at how to do simple arithmetic operations with them and look into their compatibility.

### Addition
The addition of two numeric values of the same type results in the same type.
```
a = sp.int(5) + sp.int(10)
b = sp.nat(5) + sp.nat(10)
c = sp.tez(5) + sp.mutez(1)
```

### Subtraction
The subtraction of int and int results in an int.
`a = sp.int(5) - sp.int(10)`

The subtraction of a nat and a nat results in an int.
`a = sp.nat(5) - sp.nat(2)`

The subtraction of a mutez and a tez results in a mutez.
`d = sp.mutez(5) - sp.tez(1)`

### Multiplication
The multiplication of an int and int results in an int.
`a = sp.int(5) * sp.int(5)`

The multiplication of a nat and a nat results in an nat.
`b = sp.nat(5) * sp.nat(5)`

The multiplication of a tez and a nat results in a tez.
`c = sp.mul(5, sp.mutez(5))`

### Division
The division of a nat and a nat results in an nat.
`b = sp.nat(10) / sp.nat(3)`

The division of a tez and a tez results in a tez.
`c = sp.mutez(10 // 3)`

## 2.7 Functions
We already saw the entry points methods that we can call from outside our contract, in this section we want to look into lambdas.

First, let's have a look at the global lambda.

**Global Lambda**
You define a global lambda with the `@sp.global_lambda` decorator.
Global lambdas are created for functions that are used more than once and that don’t change the state of the contract or create operations.

```
@sp.global_lambda
def add(params):
  sp.result(params.a + params.b)

Let’s test a global lambda in a contract.

import smartpy as sp
 
class MyContract(sp.Contract):
    def __init__(self):
        self.init_type(sp.TRecord(storage = sp.TInt))
        self.init(storage = 1)
 
    @sp.global_lambda
    def calc(params):
        sp.result(params.a + params.b)
 
    @sp.entry_point()
    def add(self, params):
        self.data.storage = self.calc(sp.record(a = params.a, b = params.b))
 
@sp.add_test(name = "MyContract")
def test():
    scenario  = sp.test_scenario()
    contract = MyContract()
    scenario += contract
    scenario += contract.add(a = 3,b = 2)
    scenario.verify(contract.data.storage == 5)
```

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJx1UcFqxCAQvecrhj0puwTa0kshUOiph15K7zJRswRMFJ0W8vd1rMkmLPWk8968eW8cp@AjQZowUlgAE6TQQKMdpgQfy5ufKaImkUK73uVLA_kYO4BS4zySUiJZN9Q6H362BaIlWG7@@rTaRyMS@YhXCx1w8X0mKe@7dqyHDBfCa@Zfne_RKYdTb3AzodFpETDilPYWQhtt@nZUoRbhDPXa70VtTrWo4MeZhNxE0ZgS6gL3ymzTIGG7C8O1YqTMLVEx19fZF@hvr54zNzw7T1FkE4kZJ5Y53TZ@kg37KGgdnrSdMY4e_rbHkFpr1bqu3Zmx@zx5bD93G@9fgK2VBE8Xdv54lGh_bByHRWzs4zo6eJa_h5a7Ww--)

We create a global lambda calc that calculates the sum of two parameters and returns the value via `sp.result`.
In our entry point `add`, we call `calc` with its parameters and save the result in the storage.

**Lambda**

To use a regular lambda function you use `sp.build_lambda(l)`. There are not many use cases for regular lambdas in SmartPy, but this is how you could use them in a contract.


```
import smartpy as sp
 
class MyContract(sp.Contract):
    def __init__(self):
        self.init_type(sp.TRecord(storage = sp.TInt))
        self.init(storage = 1)
   
    @sp.entry_point()
    def add(self, params):
        increment = sp.build_lambda(lambda b: b + 3)
        self.data.storage = increment(params)
 
@sp.add_test(name = "MyContract")
def test():
    scenario  = sp.test_scenario()
    contract = MyContract()
    scenario += contract
    scenario += contract.add(2)
    scenario.verify(contract.data.storage == 5)
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJx1kE9LxDAQxe_9FMOeElYKKl4WCoInD17Ee5gmqQSaP2RGod_epO12W8Vcksx7L_PLOJ9iZiCPmdMESECpgUaPSARv00sMnFGzoNRez_LSQFnGDqCUC46VEmTHYa3XVa_tLPGUbA1_vFsdsxHEMeOnhQ5q8TWwlH9TO9f9LM@W55KwBWFSKbrAQm4YaMxMcAcJM3rakbigs_UltnTsv9xo1Ii@NyiWDfoL9HCGx18gBhnbG8j2kFh7lClVotJbsSUWAX31nW5DO8mm0s3qikTaBswuwoJTJXWtrR_Sa7o4dvOXx_i523z_ChVNPByD7bfNbpjE5jn@soMn@QNOBqa5)

## 2.8 Control flow
In this section, you will learn how to make your contracts smart, by routing their control flow.

### Booleans
As we already said, a boolean has one of two possible values: `True` or `False`.

```
user = sp.bool(True)
admin = sp.bool(False)
```

### Logical operators
Here is a list of logical operators that can help your contract make decisions.

**&& (Logical and)**
`logical_and = True & True`

**|| (Logical or)**
`logical_or = False | True`

**! (Logical not)**
`logical_not = ~ False`

**= (Equals)**
`eq = sp.verify(2 == 2)`

**<> (Not equals)**
`not_eq = sp.verify(2 != 3)`

**> (Greater than)**
`gt = sp.verify(4 > 3)`

**< (Less than)**
`lt = sp.verify(2 < 3)`

**>= (Greater than or equal to)**
`gte = sp.verify(4 >= 3)`

**<= (Less than or equal to)**
`lte = sp.verify(3 <= 3)`

### Comparing Values
Now that we know how to use logical operators, we need the values to use them on. So let's have a look at how to compare different kinds of values.

**Comparing strings**
```
a = sp.string ("Alice")
b = sp.string ("Alice")
c = sp.verify(a == b) # true
```

**Comparing numbers**
```
a = sp.int(5)
b = sp.int(4)
c = sp.verify(a == b)
d = sp.verify(a > b)
e = sp.verify(a <= b)
f = sp.verify(a != b)
```

**Comparing tez**
```
a = sp.mutez(5)
b = sp.mutez(10)
c = sp.verify(a == b)
```

### Conditionals
Conditional logic enables forking the `control flow` depending on the state.

**If statement**
Let's use conditional logic and the commands `sp.if` and `sp.else` to decide if a user is either a minor or an adult.

```
@sp.entry_point()
def check_majority (self, params):
    sp.if params < 18:
        self.data.result = True
    sp.else:
        self.data.reslut = False
```

**Error conditions**
We can use *error conditions* to check if a boolean expression evaluates to true, if it doesn't we can raise an error.

```
sp.verify(params > 18 , message = "Sorry, you are a minor.")
```

We can also check equality between values with `sp.verify_equal`.


### Loops
We will use loops mostly to iterate over data strucutres, more on that in a later section, for now we will look into a loop with a very simple example. 

**For statement**
The most used loop is the for loop, in this example we use `sp.for` to calculate the sum of a range of numbers.

```
import smartpy as sp

class myContract(sp.Contract):
    def __init__(self):
        self.init_type(sp.TRecord(storage = sp.TInt))
        self.init(storage = 0)

    @sp.entry_point
    def sum(self, params):
        sp.for i in sp.range(1, params + 1):
            self.data.storage += i

@sp.add_test(name = "myContract")
def test():
    scenario = sp.test_scenario()
    contract = myContract()
    scenario += contract
    scenario += contract.sum(4)
    scenario.verify(contract.data.storage == 10)
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJx1UMtqxDAMvPsrxJ5stpgN9FQIFHrqtezdiNhZDOsHllrI32@cjdOEUp1kzYxnJB9yKgwUsHCeAAkoCzHckQjC9JEiFxxYUtatV28C5rJuBGN89GyMJHcf13mt@tQLxFN2VXz9ckMqVhKngjcHPdThZ2Sl_qp2rIsSC_4@093sP5mcfOQtAX2HxfwFMhYMtA@R9ZgKePCx9gXjzcmuEeEM3Y68@Vtk1M3_3IMXonqjtYYdsYwYaq7T721OStQkC7r@SIOLWHx6rlkR00byue@wimfG7srqqJ7tG@9fQNcLvB6F@scVP05y4xyW6nvoLuoBbH6dlA--).

**While statement**
You can also create while loops using `sp.while`.

```
sp.while 1 < y.value:
    self.data.value += 1
    y.value //= 2
```

## 2.9 Data Structures Pair, List, Record, Map
In this section, we will look into data structures and use the types Pair, List, Record, and Map to store multiple values. You will learn to create more complex contracts and apply what you learned in the sections before.

### Pairs
Let's first look at pairs, a simple data structure.

* Pairs can store values of different types.
* Pairs have a fixed length, meaning that you can not add or delete values.
* Pairs only store values, no keys.

**Definition**
```
user  = ("Alice", "Doe")
user2  = sp.pair("Alice", "Doe")
```

**Access**
You can access the elements of the pairs with `sp.fst(..)` and `sp.snd(..)`.

```
firstName = sp.fst(user) # "Alice"
lastName = sp.snd(user)  # "Doe"
```

**Example Contract**
We are creating a contract that has an entry point that takes a pair of strings as parameters, concatenates the strings and stores the result in the storage.

```
import smartpy as sp
 
class myContract(sp.Contract):
    def __init__(self):
        self.init_type(
          sp.TString
        )
        self.init("")
 
    @sp.entry_point()
    def main(self, params):
        sp.set_type(params, sp.TPair(sp.TString, sp.TString))
        self.data = sp.fst(params) + " " + sp.snd(params)
 
@sp.add_test(name = "myContract")
def test():
    scenario = sp.test_scenario()
    contract = myContract()
    scenario += contract
    contract.main(sp.pair("Alice", "Doe")).run()
```
Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJxlUcFqxSAQvOcrFk9Kgh9QeNDSfkDh9S5LYooQzeLaQ_6@akxeXqsXndlxZlfnaY0J2GNMtAEyMHXQjQsyg9_e15Aijkky6eOsXjrIa7IzGOOCS8ZItsvc8LLKVVcqbWTliWeG9Nc9RRe@T1D9l0khMlrx16yw2XgztLqQpDrNPbpQjQcgjOj5GoA02@a@k0O1_kQX5SPDcMmj_uSYMCHcSsHMqT2ioAeRd18NwnTAOWvJidNkks3VAb3NWvEYYO6nZK5sy8mjDRjdupsUxhxQ63Js4lxx@Qr1rO5vZ92TSO_zIU2lZ_G2uNGKAcTHaoVSOv4EqX4BHfCazg--).

We initiate our contract with an empty string. 
 
In the entry point `main`, we add a parameter and set its type, a pair of two strings. We access the first element of our `params` pair and concatenate it with the second element of our pair, our storage gets assigned the result of the operation.
 
In our test, we run the `main` entry point with the pair, `("Alice", "Doe")`, as arguments. If you run the test you can see in the output panel the joined strings as the new storage.

Learn more about pairs in the [SmartPy documentation](https://smartpy.io/docs/types/pairs).

### Lists
The special thing about lists is that you can not access elements directly, only either the first item or the rest of the elements. Lists are also ordered, and elements in them can be repeated.

* Lists store values of the same type.
* Lists have a variable length.
* Lists only store values, no keys.

**Declaration**
```
my_list_type = sp.TList(sp.TInt)
```

**Definition**
```
empty_list = sp.list([], t = sp.TNat)
my_list = sp.list([1,2,3], t = sp.TNat)
```

**Access**
The first element in a list is called the *head*, and the elements after the head are called the *tail*. 
You can match a list and access its head and tail as shown in the following example.

```
with sp.match_cons(my_list) as x1:
    self.data.head = x1.head
    self.data.tail = x1.tail
sp.else:
    self.data.head = "abc"
```

**Add** 
With `<list>.push(<element>)` you can add new elements on top of your list.

```
self.data.my_list = [1, 2, 3]  # [1, 2, 3]
self.data.my_list.push(4)     # [1, 2, 3, 4]
```

**Iterate**
With `sp.for x in <list>:` you can iterate over lists.

```
@sp.entry_point
def sum(self, params):
    self.data.result = 0
    sp.for x in params:
        self.data.result += x
```

**Example Contract**
In this contract, we are creating a list of guests, but only a selector will be able to add new guests to the list.

```
import smartpy as sp
 
class Guestlist(sp.Contract):
    def __init__(self, selector):
        self.init(guests = sp.list(t = sp.TString), selector = selector.address)
 
    @sp.entry_point
    def add_guest(self, params):
        sp.set_type(params, sp.TString)
        sp.verify(sp.sender == self.data.selector)
        self.data.guests.push(params)
 
@sp.add_test(name = "Guestlist")
def test():  
    selector = sp.test_account("selector")
    guest = sp.test_account("guest")
  
    contract = Guestlist(selector = selector)
    scenario = sp.test_scenario()
    scenario += contract
    
    scenario += contract.add_guest("Alice").run(sender = selector)
    scenario += contract.add_guest("Bob").run(sender = selector)
    scenario += contract.add_guest("Celia").run(sender = guest, valid = False)
```

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJylUctqwzAQvPsrhE8yDfqAQKAPaD@gvYutvEkFsiy064D_vno4jps2p@pgZM3s7MyuHcIYWdAAkcMsgASFRjTGAZF4m5DYWWJJQb2MniMY7vaNSKfHo9DaestaS0J33In0RcNjXBj5ZEBlkjxlLRKHpK@KJNf7xztH60_dtTy_L1cFfR@RqEuWstxjKsBkY9ZhtJ5XI4mmS4PFSYAIA219BEXImueAsoK7bfMt74zRHmdZKnyPyc6hxuiBQa0Zf0YsWI2owkRfS5PsO3vO_jjb8zBgyteuk227JgcoYLcXNeZ2EkFlTIMx4@RZthesrQ5Kz794BSikwjPL9hJ1s9XfE6@qZNBDtONG@PIkbxgPh1W7AHdRdV1S@@SswbZTcfLyMuV7Fu5IPI@f_xN4QWfhVqJgO3EGZ_v0@wqOsPsG@sQFvA--).

We initiate our contract with a parameter, the `selector`. We are going to store the address of the selector in the storage so we can make sure that only they are allowed to add new users. 
We are also storing a list of strings, the guests in the storage.

We create an entry point `add_guest`, it takes one parameter a string, which will be the name of the guest. To be able to add new guests to the list, we first verify if the entity executing the contract `sp.sender` has the same address as the address of the selector stored in the storage. If it does, we push the new name on top of the guestlist.

In the test, we first create two new test accounts: the `selector` and a `guest`. We then execute the entry point `add_guest` with two names from the selector account and one name as the guest, which we expect to fail, hence `valid = False`. If you test this contact you should see a list of guests with Alice and Bob in it and an address of the selector.

Learn more about lists in the [SmartPy documentation](https://smartpy.io/docs/types/lists).

### Records
A *record* is a very heavily used data structure and you will encounter them everywhere.

* Records can store values of different types.
* Records have a fixed length.
* Records store corresponding fields.

A record is made of a set of fields, which consist of a *field name* and a *field type*.

**Declaration**
```
user_type = sp.TRecord(
  age = sp.TNat,
  username = sp.TString
)
```

In this example, the record user has two fields. The field name `age`, the corresponding field type is `nat`, as well as `username`, which is a `string`.

**Definition**
```
sp.record(
    age = sp.nat(48),
    username = sp.string("bob")
)
```
 
**Access**
You can access the field's value by writing `<record>.<field>`

```
value  = record.username # "bob"
```


**Example Contract
**In this example, we are creating a very simple user management contract. For now, it will only be able to store one user record. An admin will be able to update the username and admin status.

```
import smartpy as sp
 
user_type = sp.TRecord(
    age = sp.TNat,
    username = sp.TString,
    admin = sp.TBool
)
 
class myContract(sp.Contract):
    def __init__(self):
        self.init_type(sp.TRecord(user = user_type))
        alice = sp.set_type_expr(
            sp.record(
                age = sp.nat(18),
                username = sp.string("Alice"),
                admin = False
            ),
            user_type
        )
        self.init(user = alice)
 
    @sp.entry_point()
    def update_name(self, param):
        sp.set_type(param, sp.TString)
        self.data.user.username = param
 
    @sp.entry_point()
    def update_admin(self, param):
        sp.set_type(param, sp.TBool)
        self.data.user.admin = param
 
@sp.add_test(name = "myContract")
def test():
    scenario = sp.test_scenario()
    contract = myContract()
    scenario += contract
 
    contract.update_name("Bob").run()
    contract.update_name("Celia").run()
    contract.update_admin(True).run()
```

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJyVkkFrxCAQhe_5FZKT0iD0VgoL7S702EO7d5km7iIkKmqg@fdVo67ZbUvrKXnzRr95KiatjEN2AuP0gsAiqxvUzJYb5hbN0c4L9PjGe2UG3CC_4JzVV3BdlIJdwpT1d2eEPK8lGCYhk75XamyI374fwVo0LQclnYHeYV_N3@Qx9g38hBgTUjjGsOXjKelhhV8aSwERV4ABxB9W8AkpTTCKPgFavnYy_qkNLo64taammrVeZW4JDt8_kO7GsY3BxhRw@xwObr@x52heYLR8U70yl3GKSm6zyLPHOUPIKHqePAn3yS5MKyEdJiXdWQ_gOAvAMeAOaTAw1TlfosKx1lXXe4Xg9wIaEGiVQmz6K0iM438k4UH9yJHjzRABAIaBOW4dToDt5Q22pAkwsZpOtj2XYIRa7zNUWJYSfp@avaN6zWTbfbcrvk0TrW@g3auPllAzy6utt64DHwX86ltjPJqZJ9cXsRcm5Q--).

In order to tidy our code a little bit, we specify `user_type` before we create a contract. We want to store a record that consists of three fields, the `age`, the `username`, and the `admin` status, which are a `nat`, a `string`, and a `bool`.

In our contract, we then initiate the type for the user record as `user_type`, that we just created.

We proceed to create the content for your record type in the form of alice, we use `set_type_expr` to ensure that it has the right type and then add some initial values for the records to be stored in the storage.

We create two entry points `update_name` and `update_admin` which have a parameter that can update the username or admin field of the user record.

In the test, we run our `update_name` entry point and our `update_admin` entry point with different values.

Learn more about records in the [SmartPy documentation](https://smartpy.io/docs/types/records).

### Maps
If you want to create more complex data structures you need to use *maps*.

* Maps can store up to two different types.
* Maps have a variable length.
* Maps store key-value pairs.

**Definition**
```
my_usernames = {
    0: "Alice",
    1: "Bob",
    2: "Celia",
}
my_usernames2 = sp.map(
  {
      0: "Alice",
      1: "Bob",
      2: "Celia",
  }
)
```

Here is how you can create an empty map.

```
empty = {}
empty2 = sp.map()
```

**Access** 
You can access an entry in a map via `<my_map>[key]`.

```
my_usernames[0]
```

You can also specify a default value or error message if the there is no entry for the key via `<my_map>.get(key, default_value = None, message = None)`.

```
my_usernames.get(1, message="No value for this key")
```

**Update**
You can update an element in a map using `<my_map>[key] = <new_value>`.
```
my_usernames[0] = "Cillian"
```

You can also use `sp.update_map(map, key, value)` to return a new copy of a map where the key has an optional value.

```
my_usernames = sp.update_map(my_usernames, 0, sp.some("Cillian"))
```

In this case, we are updating our value “Celia” with a new name “Cillian” we are using an optional value indicated by the keyword Some here to account for the possibility that we could have an empty value.

**Remove**
We can use `del my_map[key]` to delete an element from a map
```
del my_usernames[0]
```

We can also use `sp.update_map(my_map, key, sp.none)`.

```
my_usernames = sp.update_map(my_usernames, 0, sp.none)
```

We return a new copy of map my_map where `sp.none` is used to remove the entry.

**Example Contract**
In this example, we are going to build a more complex user management contract than in our record example. Now you will be able to save multiple user records and not just one. We will also add the functionality to add and delete user records.

```
import smartpy as sp
 
user_type = sp.TRecord( name = sp.TString, is_admin = sp.TBool )
id_type  = sp.TNat
user_storage_type = sp.TMap(id_type, user_type)
 
class UserManagement(sp.Contract):
    def __init__(self):
        self.init_type(user_storage_type)
        self.init({})
 
    @sp.entry_point()
    def add_user(self, params):
        sp.set_type(params, sp.TPair(id_type, user_type))
        id = sp.fst(params)
        user = sp.snd(params)
        self.data = sp.update_map(self.data, id, sp.some(user))
 
    @sp.entry_point()
    def remove(self, id):
        sp.set_type(id, id_type)
        del self.data[id]
```
As in the last contract we create a `user_type`, a record consisting of a `name` field which is a `string`, and an `admin` field which is a `boolean`. Next, we have an `id_type` which is a `nat`, we will use this as our index. Finally, we create `user_storage_type` which is a map that maps the `id_type`, our index, to the `user_type`, our user record. 

We initiate the contract by specifying the `init_type` and initiating it with an empty map.

In our first entry point `add_user`, we create the update functionality. The parameter will be a pair with the index, the `id_type`, and the content, our `user_type` record. This is what the user needs to provide to enter a new entry to the mapping. We take the two parameters and update our map with it.

The second entry point, `remove`, is pretty simple: we just need the `id_type` for the parameters and delete the corresponding entry in our mapping.

```
@sp.add_test(name = "UserManagement")
def test():
    scenario = sp.test_scenario()
    contract = UserManagement()
    scenario += contract
    contract.add_user(
        sp.pair(
            0,
            sp.record(
                name = "Alice",
                is_admin = True
            )
        )
    ).run()
    contract.add_user(
        sp.pair(
            1,
            sp.record(
                name = "Bob",
                is_admin = False
            )
        )
    ).run()
    contract.add_user(
        sp.pair(
            0,
            sp.record(
                name = "Alicia",
                is_admin = False
            )
        )
    ).run()
    contract.remove(1).run()
```

The testing here is also pretty straightforward, we test the `add_user` entry point three times providing the pair of index and user record content. First, we add the user Alice, then Bob, we replace Alice with Alicia, and finally, remove Bob via the `remove` entry point.

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJy1U8tqwzAQvPsrRE4WNaa5FgJtCr2llDY9lSK2lhIE1gOtUgil_17JUuw46Ruikzyz2plZyVJZ4zxBBc7bLQEkaAtSbFA45rdWkFkA6uW9aIzjJdGgdtCDd1KvKyKRAVdSZ3huTEtoIXk6ntFb8KkneuNgLfZ7L8CWubwivTANLpoWEMljgBagwykltC_DkWujvYPG04uChMXFijAmtfSMlSjaVcbjip91R8Wm5ZEHelxZvr1H8YhdBrGg6bbMGhm0aa8HnLPYrNOriAUHCvd1bY0iiyay6sLegXSfpR18SJ7mskKfTw5crE8san7Edgk4eEglGxv2gqkw3p4J18U7I2hUmgb9OasTyryKnFTyL1LGxjnYYImLdrD1JPlzEItCcXxehIT5QU3GlzyhRRTuKrIcNkKDkyZliwzbQdlqk19FqDh4MnTc4WzW144O1v2l7ge08cZ6IK7zavQZalz6PUZwXLt0V61sxKQ64vf@naXbiBE_DDHtaO02@iDqbx1P_@x4bl6@93sDLZ7O8P9GLOEknvP7n2byAxDkbxQ-).

Learn more about maps in the [SmartPy documentation](https://smartpy.io/docs/types/maps).

Ok, that’s it for the data structures, in the next section you will learn how to make tez transactions.

## 2.10 Transactions
In this section, we will learn how to make a Tezos transaction through a smart contract.
To transfer tez to an account you can use the built-in function `sp.send`.

A transaction operation to an account looks like this:

```
sp.send(
  sp.address("tz...."),
  sp.tez(5), # or sp.mutez(5000000), both yield to sp.TMutez
  message = "Error message" #error message if send fails
)
```

The first parameter is the *destination*, the account that is the recipient of the transaction.
The second parameter is the *amount* that you want to transfer in the transaction.
The third parameter is an *error message* that is issued should the address not resolve to an active account.

Let’s look at a contract example to see this in action. The contract will be very simple and just transfer some of its funds to an address.

```
import smartpy as sp
 
class myTransaction(sp.Contract):
    def __init__(self, ownerAddress):
        self.ownerAddress = ownerAddress
        self.init()
 
    @sp.entry_point()
    def main(self):
      sp.send(
        self.ownerAddress,
        sp.tez(5), # or sp.mutez(5000000), both yield to sp.TMutez
        message = "Error" #error message if send fails
      )
 
@sp.add_test(name = "myTransaction")
def test():
    scenario = sp.test_scenario()
    owner = sp.test_account("Owner")
    contract = myTransaction(owner.address)
    contract.set_initial_balance(sp.tez(10))
    scenario += contract
    scenario.verify(contract.balance == sp.tez(10))
    contract.main().run()
    scenario.verify(contract.balance == sp.tez(5))
```

Test this contract in the [SmartPy IDE](https://smartpy.io/ide?code=eJyVUbFOBCEQ7fcrJnsNxMvmLK4x2URjLI3N9WQOWCVZYMNwmvXrBcKtYmIhDWHe4715M8YuPkQgiyEuKyABLR10ckYisOspoCOU0XjHaBkevYshPfldB@koPYEQxpkoBCM9T3vwH06HB6WCJqqsfDI4_MRgbKgtMSsyntrIlfvkq5PtKhZvXKlXa4vGFdvNKFFJO8X@9t1_Q8sQ9Sc78j3swIf8tpdSOZST6mcf32A1elYQfSacnjNjk7BJEF91ytI_heBDDzud7w0wE@R@YEIzXzPmXDkTKiWipsgc2iLRTLvnXY5YCDVeiZGIpXGKAqX0lzSQ_iUD6UNhkdQOg_E_iNdSHZ2sS0yMdsHFIPdVltdw01hjWbTBWZxxRic1qxO8PXDeWt@M28cCNOjwroOZVrZJVzkYR_ituHHKqvkQLo7x_6odOf8CB_bpZQ--).

We create a contract with the parameter `ownerAddress` that will be the recipient of the transaction.

In the entry point main we implement the `sp.send` method as described above. The recipient is the address with which initiated the contract, we will transfer 5 tez and we display a generic error message.

In our test, we create a test account that we use to initiate the contract. We then set an initial balance of the contract, so we have something that we can transact, and finally, we run our main function to transfer the assets. We verify the balance before and after the transaction.

Congratulations you finished our short introduction to SmartPy, in the next chapter we will show you how to create a frontend that can interact with a Tezos contract



