## 2.1 Intro to Tezos Smart contracts
In this brief intro, we will introduce you to Tezos smart contracts and give you a short overview of the different smart contract languages on Tezos.

**Smart contracts**
A *smart contract* is computer code that is stored and runs on a blockchain-based platform. Since data that is stored on blockchains is *immutable* (unchangeable) the code of smart contracts becomes immutable too once deployed to the network.

This enables smart contracts to execute agreements automatically based on predefined conditions with a dependable outcome, independent from any third party involvement. 

On Tezos, smart contracts are a type of *account* with an *address* that can store code, have a *balance*, and can send *transactions*. Users of smart contracts can interact with them by submitting transactions to the smart contract that execute functions as defined in the smart contract.

Learn more about smart contracts on [Open Tezos](https://ligolang.org/docs/language-basics/sets-lists-tuples#sets).

**Michelson**
In Tezos, the low-level, machine language that runs smart contracts on the Tezos network is called *Michelson*. The language is stack-based, with high-level data types and primitives, and strict static type checking.

Learn more about Michelson in the [Tezos Documentation](https://tezos.gitlab.io/active/michelson.html).

Since it’s hard to get started writing in a low-level language, there are different high-level languages in the Tezos ecosystem that compile to Michelson.

*LIGO* comes in four different syntaxes, *Camel*, *Pascal*, *Reason*, and *Javascript*. 
*SmartPy* is inspired by Python. 
*Morley* was the first high-level language developed for Tezos.

In this course, we will focus on LIGO and SmartPy.

**LIGO**
LIGO is great because it is statically-typed and *CameLIGO* and *ReasonLIGO* allow you to write in a functional style, which helps you to avoid mistakes and create more secure code which is crucial when writing smart contracts.
In this course, we will work with CameLIGO which is inspired by the popular functional language *OCaml*. Many contracts developed by the Tezos community are developed in OCaml and it is the language of choice for many professional developers.
popular
Learn more about LIGO in the [LIGO Documentation](https://ligolang.org/docs/intro/introduction).

**SmartPy** 
SmartPy is a great starting point if you are familiar with Python and want an easy entry.
SmartPy adds another abstraction layer, it compiles to SmartML which is written in OCaml, which is then compiled to Michelson.

Learn more about SmartPy in the [SmartPy Documentation](https://smartpy.io/reference.html).

For the following sections of this chapter, you will be able to choose if you want to learn how to write Tezos smart contracts in CameLIGO or SmartPy.

## 2.2 Introduction to CameLigo
In this section, we will give you a brief intro to LIGO, its different syntaxes, and Ocaml.

While it has great benefits to run immutable code on a decentralized network it also poses new challenges. 

Running smart contracts is much more expensive than running code on your local computer or using a traditional cloud computing provider. To execute a function and change the state of the contract you have to create a transaction that you have to pay for.

Because of their transparent, immutable nature, smart contracts are often used to communicate value, often in the form of monetary tokens and financial applications. This makes them prone to attacks and poses severe security risks.

Another issue is the immutability itself, once deployed you will be not able to change or update your code.

**LIGO**

To address these challenges LIGO was designed.
LIGO is a simple, *functional language* that allows you to write simple code that is easy to formally verify by the compiler. LIGO is strongly and *statically typed*. Statically typed languages are *type checking* (verifying and enforcing the constraints of types) at *compile time* as opposed to dynamically typed languages that do it at *runtime*. This enables you to write concise code that is easy to test and decreases security risks.

LIGO comes in the syntaxes CameLIGO, PascaLIGO, ReasonLIGO and JsLIGO.
CameLIGO is inspired by Ocaml and ReasonLIGO by ReasonML, they both allow writing in a functional style. ReasonLIGO builds upon Ocaml but offers some similarities with Javascript. PascaLIGO is inspired by Pascal and offers an imperative experience and JsLIGO is inspired by JavaScript.

For the following sections, we decided to use CameLIGO to offer a functional and more pure Ocaml approach.

**OCaml**

OCaml is a *general-purpose programming language* that focuses on safety. It offers an advanced type system that helps you to catch mistakes easily. This makes a great choice in environments, where even small mistakes can be very costly. 
OCaml is a functional programming language. It enables you to use functions as ordinary values, that can be passed as arguments or can be returned by a function.

Learn more about OCaml on the [OCaml Website](https://ocaml.org/learn/description.html).

To start writing contracts with CameLIGO it is very helpful to become familiar with the OCaml syntax. We recommend you to take the [Guided Tour by Real World OCaml](https://dev.realworldocaml.org/guided-tour.html).

In the next section, you will learn how to use the LIGOlang IDE to write CameLIGO contracts.

## 2.3 Introduction to the IDE
In this section, we will give you an introduction to the LIGO IDE.

To quickly test contracts and interact with the learned content, we will use an IDE (integrated development environment) in the first sections of this chapter.

**IDE Basics**
![](https://raw.githubusercontent.com/moritzfelipe/tezos-development-101/main/content/gifs/tezos_2_3_1_IDE.gif)

You can reach the LIGO IDE under [ide.ligolang.org](https://ide.ligolang.org/) (GIF 1.).

The LIGO IDE is part of the ligolang website. In the top navigation, you will find links that will lead you to various sections of the website.

On the left side next to the code editor, you can find code examples in different LIGO flavors. Let's choose “Increment (CameLIGO)” (GIF 2.).

The code editor has syntax highlighting for the different LIGO flavors. 
On the top right of the code editor, you can select the LIGO flavor that you want to code with (GIF 3.). Be sure to always select the right flavor, leaving the selection on the default is a common source for unexpected errors.

On the top left of the editor, you have the ability to create a link, with which you can share your code (GIF 4.). This is very practical to receive feedback from peers.
Under all contracts in this chapter, we will provide a link to the contract so you can quickly test and interact with it. The best way to learn is to interact with newly formed knowledge so we highly encourage you to do that.

**Compile Contract and Expression**
![](https://raw.githubusercontent.com/moritzfelipe/tezos-development-101/main/content/gifs/tezos_2_3_2_IDE.gif)

On the right side, in the configure section you can perform various actions on your contract code.

You can compile your contract (GIF 1.). 
Underneath your code editor will appear either a compilation error (GIF 1.1) or a compiled version of your contract in Michelson (GIF 2.1).

You can also compile a single expression (GIF 3.).

**Evaluate Function and Value**
![](https://raw.githubusercontent.com/moritzfelipe/tezos-development-101/main/content/gifs/tezos_2_3_3_IDE.gif)

With “Evaluate Function” you can evaluate a single function (GIF 1.) and with “Evaluate Value” a single value (GIF 2.).

**Dry Run and Generate Deploy Script**
![](https://raw.githubusercontent.com/moritzfelipe/tezos-development-101/main/content/gifs/tezos_2_3_4_IDE.gif)

The Dry Run functionality is also very important. You can use it to test how your contract will behave once deployed. In the first input field “Access function” you have to enter the name of your main function. Beneath the main function, you need to input the parameters of the function and under the parameters, you enter the storage (GIF 1.). Don’t worry if this is a bit cryptic at the moment we will explain these concepts in the next section.
After entering the inputs and pressing the “Run” button you either see compilation errors or the return value of your contract in Michelson (GIF 2.1).

You can also choose “Generate Deploy Script” which will compile your contract to Michelson and generate a script that you can deploy via the command line (GIF 3.).

In the next section, we will create our first contract and interact with it in the IDE.

## 2.4 "Hello, World!" contract

In this section, we will explain the basic building blocks of the most simple “Hello, World!” contract on Tezos.

**Main function**
A Tezos smart contract has one *main function*, that is the only way to interact with the smart contract and the data that it stores on-chain, *the storage*.

The main function receives one pair of parameters, the contract parameter and the on-chain storage as an input. It outputs a *pair* of an *operation list* and a new, modified storage. 

Let’s have a look at the most simple “Hello, World!” contract to understand the basic structure of a main function. This contract is simplified for illustration purposes and should never run in production.

```
let main (p, s : string * string) : operation list * string = 
(([] : operation list), s)
```
TODO:
- explain entry_point annotation

```
# this is a very useless example (just like the one in camligo) down below is a better hello world
import smartpy as sp
class MyContractExample(sp.Contract):
    pass

@sp.add_test(name = "MyContractExample")
def test():
    c1 = MyContractExample()
    scenario  = sp.test_scenario()
    scenario += c1
```

```
import smartpy as sp
class MyContractExample(sp.Contract):
    def __init__(self):
        self.init(
            greet="Hello World"
        )

    @sp.offchain_view(pure=True)
    def greet(self):
        sp.result(self.data.greet)


@sp.add_test(name = "MyContractExample")
def test():
    # define a contract
    c1 = MyContractExample()
    scenario  = sp.test_scenario()
    scenario += c1
    scenario.verify(c1.data.greet == "Hello World")
```


In CameLIGO you define functions with the *let* keyword and the function name, in this case, the main function.

Like in OCaml, CameLigo functions only take one parameter. If we want to create functions with more than one parameter, we use *tuples*. Because the tuple in this example only consists of two components it is also called a pair. Inside the tuple, we have the parameters that we arbitrarily called `p` and `s` for parameter and storage. They are followed by the value types for the parameters, in this example, both are a `string`. 

After the colon we define the return type of the main function, this is an operation list and the type of the storage, in this case, a `string`. While the type of the storage is up to you to decide, the operation list is not and always has to be returned in the main function.

In the next line, we return the `operation list`, which in this case is empty, and the storage, in this contract we just return the storage that we received as an input.

**Operation list**
In functional programming we write functions without *side effects*, meaning that functions don’t cause any *state change* of the application other than the return value. This makes it easier to maintain the code and avoid mistakes.

But our contract might need to interact with other contracts or addresses, to transfer tokens for example. Since we can’t interact from inside the contract, we specify a list of operations that our contract needs to execute and return them as an output once our main function is complete.

**Storage**
When the contract is *originated* (deployed), the initial value of the storage is provided. A main function contains parameter and storage. When the main function is called after the contract is originated only the parameter is provided, not the storage.

Let’s test this contract now, and since we originate it we need to provide parameter and storage.
In the case of this very simple contract, we just return the storage and do nothing with the parameter.

![](https://raw.githubusercontent.com/moritzfelipe/tezos-development-101/main/content/gifs/tezos_2_4_1_IDE.gif)

Test this contract yourself in the [LIGOlang IDE](https://ide.ligolang.org/p/E74sPdvyFgpGTV5qnOfCww).

As mentioned, this is a very simplified contract and doesn’t follow the conventions of a Tezos smart contract. In the next section, you will see how we use type aliasing to adapt it to a more conventional style.

## 2.5 Basic Types, Constants and Variables
In this section, we are going to look into the most important simple Tezos data types and their usage.

### Type aliasing
Type *aliases* create a new name for a type, to make your contracts more readable.

In the example below, we create aliases for our string types: `storage` and `parameter` to communicate the intent of the types of our [“Hello, World!” contract](#24-“Hello-World”-contract) more clearly.

```
type storage = string
type parameter = string
type return = operation list * storage
 
let main (p, s : parameter * storage) : return = 
(([] : operation list), s)
```
 
```
import smartpy as sp
class MyContractExample(sp.Contract):
    def __init__(self):
        self.init_type(
            sp.TRecord(
                my_field_one = sp.TString,
                my_field_two = sp.TNat
            )
        )
        self.init(
            sp.record(
                my_field_one = "Test",
                my_field_two = 1
            )
        )

@sp.add_test(name = "MyContractExample")
def test():
    # define a contract
    c1 = MyContractExample()
    scenario  = sp.test_scenario()
    scenario += c1
```
Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/9WMafeGvmLBkIYBzttu_tg).

Now the contract looks like a conventional Tezos contract, without much functionality though.
Before we can add more functionality you need to learn some basic Tezos types and in the next part how to name your values.

### Constants 
Values can only be assigned to a *constant* at their definition. Constants are *immutable* and can not be reassigned.

**Constant definition**
You define a constant with the `let` keyword a *name*, *type* and *value*.
`let my_name : string = "Alice"`

### Variables 
CameLIGO only features constant variables. Once they are declared, the value cannot be changed.

```
let add (a : int) (b : int) : int =
 let c : int = a + b in c
```

*Build-in types* are data types that are the basic building blocks of the LIGO language.

### String 
A string is a sequence of characters and is defined with the string keyword.
`let my_name : string = "alice"`
 
Strings can be *concatenated* (joined) using the ^ operator.
```
let name : string = "Alice"
let greeting : string = "Hello"
let full_greeting : string = greeting ^ " " ^ name  // "Hello Alice"
```

Evaluate this value in the [LIGOlang IDE](https://ide.ligolang.org/p/E74sPdvyFgpGTV5qnOfCww).
 
// GIF showing how to evaluate value.
 
*Substrings* can be extracted using the built-in function `String.sub`. The first character has the index 0.
```
let name  : string = "Alice"
let slice : string = String.sub 0n 3n name // "Ali"
```
 
The length of a string can be found using a built-in function `String.length`.
```
let name : string = "Alice"
let length : nat = String.length name  // length = 5
```
 

### Numerical Types
LIGO offers three built-in numerical types: *int*, *nat*, and *tez*.

**Int**
Values of type `int` are *integers*. They can be positive, negative, or zero.

```
let a: int = 42
let b: int = -3
let c: int = 0
```

**Nat**
Values of type `nat` are *natural integral numbers*. They can’t have a negative value. 
Natural numbers are written as digits followed by the *suffix* (group of letters added at the end of a word) `n`.

```
let a : nat = 7n
let b : nat = 0n
```

**Tez**
Tezos tokens can be written as digits followed by the suffix `tez` or `tz` for the unit `tez`.

```
let a : tez = 1tez
let b : tez = 3tz
 
let c : tez = 1.3tez
let d : tez = 3.3tz
```
 
Tezos tokens can be written as digits followed by the suffix `mutez` for the unit of millionth of tez. 
```
let e : tez = 1000000mutez
```
 
You can use underscores to improve readability when defining large numbers.
```
let f : tez = 1000_000mutez
```

You can *cast* (convert) an int to a nat and the other way around.
```
let a : int = int (1n)
let b : nat = abs (1)
```
 
You can check if a value is a nat with `Michelson.is_nat`. It accepts an int and returns an `optional nat`. If the input is not a nat it returns none.

```
let is_a_nat : nat option = Michelson.is_nat (3)
```

In the next section, you will learn how to do simple arithmetics with these numerical types.

### Boolean
A *boolean* has one of two possible values: `true` or `false`.

`let admin : bool = false`

### Address
*Addresses* consist of a string value and an `address` type.
 
```
let my_account : address =
 ("tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx" : address)
```

### Timestamp
You can obtain the starting time of the current block using the built-in function `Tezos.now`.

`let today : timestamp = Tezos.now`

Timestamps can do arithmetical operations with integers.
```
let some_date : timestamp = ("2009-01-03t00:00:00Z" : timestamp)
let one_day : int = 86_400
let one_day_later : timestamp = some_date + one_day
```

Please be aware that it is up to the *baker* (validator of a block) to set the current timestamp value.

### Unit
The `unit` type has only one value that carries no information, it is generally used as a placeholder.

`let n : unit = ()`

The unit type is also used as an argument in functions that don’t need an input value.
 
`let time_now() : timestamp = Tezos.now`

We have now looked into most of the important basic types. If you want to have a look at a full list of all available data types you can find them in this [LIGOlang GitLab repository](https://gitlab.com/ligolang/ligo/-/blob/dev/src/environment/environment.ml).

We will explore more complex data types in the following sections.

## 2.6 Math
In the previous section, you were introduced to the built-in numerical types: `int`, `nat`, and `tez`. In this section, we will look at how to do simple arithmetic operations with them and look into their compatibility.

### Addition
The addition of two numeric values of the same type results in the same type.
```
let a : int = 5 + 10
let b : nat = 5n + 10n
let c : tez = 5mutez + 0.000_010tez
```

The addition of a nat and an int results in an int.
`let b : int = 5n + 10`

### Subtraction
The subtraction of int and int results in an int.
`let a : int = 5 - 10`

The subtraction of a nat and a nat results in an int.
`let b : int = 5n - 2n`

The subtraction of a tez and a tez results in a tez.
`let d : tez = 5mutez - 1mutez`

### Multiplication
The multiplication of an int and int results in an int.
`let a : int = 5 * 5`

The multiplication of a nat and a nat results in an nat.
`let b : nat = 5n * 5n`

The multiplication of a tez and a nat results in a tez.
`let c : tez = 5n * 5mutez`

### Division
The division of an int and int results in an int.
`let a : int = 10 / 3`

The division of a nat and a nat results in an nat.
`let b : nat = 10n / 3n`

The division of a tez and a tez results in a nat.
`let c : nat = 10mutez / 3mutez`

You can learn how to compute the remainder of the Euclidean division and how to return the quotient and the remainder in the [LIGOlang documentation](https://ligolang.org/docs/language-basics/math-numbers-tez).

## 2.7 Functions

In this section, we will look into a very important building block of Tezos contracts, the function.

Functions are as the name suggests, important in functional programming languages. One thing to keep in mind is that functions can only change the state of your application through their return value; there are no side effects, as we have mentioned before. 

**Function Definition**
We use the `let` keyword to define functions. After the function *name*, you specify the *parameter*, consisting of a *name* and *type* for the *argument value*. After the parameter, you specify the *return type* and finally the *return value*.

```
let add (a, b : int * int) : int = a + b 
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/tPgv-MsjhEgdx0BnkcVMUw).
Function name: `add`
Example parameters: `5, 6`

In this case, our function is called `add`, our parameter consists of a *tuple* (to be more precise a pair) `a` and `b` both from the type `int`. The return type is also an `int` and the return value is the result of `a + b`.

//Gif of testing function as quick reminder how to test a function

As mentioned before, CameLIGO functions only take one parameter, but if we want to build a function with more than one parameter we can enter the arguments in a tuple and pass it as a single parameter.

We will look into tuples in more detail in the upcoming sections.

Now that we know the basics we can finally create a more interesting contract.

**Example Contract: Parameter + Storage** 
Let's create a simple example contract that takes the storage and adds the value of a parameter the user enters.

```
type storage = int
type parameter = int
type return = operation list * storage
 
let add (a, b : int * int) : int = a + b
 
let main (p, s : parameter * storage) : return = 
 (([] : operation list), add (p,s))
```

Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/Vd0E04dzttIvflhtw7nkbw).
Example parameters: `5`
Example storage: `3`

We are declaring the types: `storage`, `parameter`, and `return` as we did before.
In the next line, we define the `add` function as described.
 
Now our main function doesn’t simply return the storage as in our previous contract but returns the value of our `add` function. As arguments, we pass on parameter `p` and storage `s` from the main function.
 
This is how your contract should behave in the IDE:
// GIF of testing
 
**Example Contract: Parameter + Storage 2**
This contract is very similar to the last one but we use a constant and we introduce the new keyword `in`.

```
type storage = int
type parameter = int
type return = operation list * storage
 
let add (a, b : int * int) : int = a + b
 
let main (p, s : parameter * storage) : return = 
 let sn = add (p, s) in
 (([] : operation list), sn)
```
 
Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/6trff3Xx1IaH2k-lhGEGUA).

This contract is basically the same as the contract before, the difference is that we create a new constant inside the main function that has the value of `add`. Usually, every function has one expression but if you want to write more than one you need to add the keyword `in` after them.
In the next line, we return the constant `sn` instead of the function `add`.

As mentioned before, we can use functions like ordinary values, we can pass them as arguments or return them in a function.

### Lambdas (Anonymous functions)
An *anonymous function* can be defined without assigning them a name. It is the most basic style of a function.

Anonymous functions are being defined using the `fun` keyword.

```
let increment (b : int) : int = (fun (a : int) -> a + 1) b
let a : int = increment 1 // a = 2
```

Anonymous functions are often arguments or returned from other functions, making the latter *higher-order functions*.

```
type storage = int
type parameter = int
type return = operation list * storage
  
let main (p, s : parameter * storage) : return = 
 (([] : operation list), (fun (s : int) -> s + 1) p)
```

One of the most popular use cases for anonymous functions is to pass them to iteration functions like `List.map`. More on lists and iterations in another section.
 
```
let incr_map (l : int list) : int list =
  List.map (fun (i : int) -> i + 1) l
```

There are two other types of important functions that should be mentioned in this section.
*Nested functions* and *Recursive functions*. If you want to learn more about them have a look into the [LIGOlang Documentation](https://ligolang.org/docs/language-basics/functions#nested-functions-also-known-as-closures).

At the beginning of this chapter, we have already talked about *main functions*. Every contract has to have at least one main function. How this main function can dispatch the *control flow* to other functions called *entrypoints* will be a topic of the next section.

## 2.8 Control flow - Pattern matching, Conditionals and Iterations
In this section, you will learn how to make your contracts smart, by routing their control flow.

### Variant
A *variant* type can define a type depending on different cases.

**Definition**
```
type user = 
  General 
| Guest
 
let general : user = General
let guest : user = Guest
```

In this example, we define a variant, `user` that can either be a general user: `General`, or a guest user: `Guest`. The variants, in this case, `General` and `Guest` are also called *constructors*.

The constants `general` and `guest` are both of type `user`. The constant `general` gets assigned the constructor `General` and guest the constructor `Guest`. In this example, the variants carry no information besides the name.

Let's look at an example where the variants carry information.

```
type name = string
 
type user =
  Admin of name
| General of name
| Guest
 
let a : user = Admin "Alice"
let b : user = Guest
```

In this example, we add more information to the variant in the form of an argument of the type `name`, a `string` and add a third constructor, `Guest` with no information.

### Pattern matching
`Pattern matching` executes code based on different cases.
We can use the value of variants, records, tuples, or lists to perform these different actions.

**Match on variants**
Let's see how pattern matching works if we *match* on variants. We use the same variant as in the example before.

```
type user =
  Admin of name
| General of name
| Guest
 
let greet_user (u : user) : string =
 match u with
   Admin (n) -> "Hello, admin " ^ n
 | General (n) -> "Hello, user " ^ n
 | Guest -> "Hello"
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/SnCFAD33dHvevHsboOHP_g).
Function name: `greet_user`
Example parameter: `Admin("Alice")`


In this example, the function `greet_user` receives the variant `user` as an argument. With the keywords `match` and `with` we match the argument with the available options, in the case of `Admin` and `General`, pass the string and perform an action. In this case a greeting.


**Example Contract: Increment and Decrement**
```
type storage = int
type parameter =
  Increment of int
| Decrement of int
| Reset
type return = operation list * storage
 
let add (n, s : int * storage) : storage = n + s
let sub (n, s : int * storage) : storage = n - s
 
let main (p, s : parameter * storage) : return =
 ([] : operation list), 
 (match p with
   Increment n -> add (n, s)
 | Decrement n -> sub (n, s)
 | Reset         -> 0)
```

Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/Y1HWdMBds8SrAsAXSkuYTA).

This contract should look familiar. It is almost the same contract as you have seen in our IDE introduction section. It is part of the example contracts of the IDE. Let's look at it and learn about a new concept, *entrypoints*.

### Entrypoints 
As you already know, the main function dispatches the control flow according to its parameters; the functions that are called through these parameters are called *entrypoints*.

The increment function that we just built is a very conventional structure for a main function of a Tezos contract.

The parameter of the contract is a variant type and dependent on its constructors, in this case, `Increment`, `Decrement`, or `Reset` the entrypoints `add` or `sub` are called. If `Reset` is used we return `0`. 

Through pattern matching, you can control the flow of your contract by only accessing one function, the main function.

As mentioned before, you can also use tuples, records, and maps for pattern matching. Have a look at the [LIGO documentation](https://ligolang.org/docs/language-basics/unit-option-pattern-matching#match-on-records-or-tuples) to learn more about it.

### Booleans
A boolean has one of two possible values: `true` or `false`.

**Definition**
```
let admin : bool = false
let guest : bool = true
```

### Logical operators
Here is a list of logical operators that can help your contract make decisions.

**&& (Logical and)**
`let logical_and: bool = true && true`

**|| (Logical or)**
`let logical_or: bool = false || true`

**! (Logical not)**
`let logical_not: bool = not false`

**= (Equals)**
`let eq: bool = 2 = 3`

**<> (Not equals)**
`let not_eq: bool = 2 <> 3`

**> (Greater than)**
`let gt: bool = 4 > 3`

**< (Less than)**
`let lt: bool = 4 < 3`

**>= (Greater than or equal to)**
`let gte: bool = 4 >= 3`

**<= (Less than or equal to)**
`let lte: bool = 4 <= 3`

### Comparing Values
Only values of the same type can be compared, but not all types are comparable. Comparable types include `int`, `nat`, `string`, `tez`, `timestamp`, `address`.
Non-comparable types include `maps`, `sets`, or `lists`.

**Comparing strings**
```
let a : string = "Alice"
let b : string = "Alice"
let c : bool = (a = b) // true
```

**Comparing numbers**
```
let a : int  = 5
let b : int  = 4
let c : bool = (a = b)
let d : bool = (a > b)
let e : bool = (a <= b)
let f : bool = (a <> b)
```

**Comparing tez**
```
let a : tez  = 5mutez
let b : tez  = 10mutez
let c : bool = (a = b) // false
```

### Conditionals
Conditional logic enables forking the `control flow` depending on the state.

Let's use conditional logic to decide if a user is either a minor or an adult.

```
type user_majority = 
  Minor
| Adult

let check_majority (a : nat) : daytime =
  if a < 18n then Minor else Adult
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/6IemBM-M4xWnAkGT6Hxi9w).

We use the conditional construct, if-then-else to return either our constructor `Minor` or `Adult`. If a boolean condition is true, in this case, `if` the nat `a` is smaller than `18n` then follows a *consequent*, in this case, the constructor `Minor`, `else` follows an alternative, in this case, the *constructor* `Adult`.

Let's have a look at a special case of a variant type, an *optional value*.

### Options
The *option* type is a predefined variant type that is used to express whether there is a value of some type or none. 

Let's look at an example where this might make sense, a function that performs a division between two numbers. As you know in ordinary arithmetic the division by zero is undefined. Our contract would fail if we would perform such an operation. This is a great use case to use `option`.

```
let div (a, b : nat * nat) : nat option =
  if b = 0n then (None : nat option) else Some (a/b)
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/rks7H4MldgARld46kzmq1Q).

We define for our function `div` with `nat option` a return type where the value is optional, we might receive a `nat` or we might receive no value. If `b` is `0` then we return no value else we return `a` divided through `b`. 
If there is the possibility that you could return nothing you need to specify the type of the value as option.

### Iterations
Since CameLIGO is a functional language we can use *recursive functions* instead of loops to iterate over values. LIGO functions are not recursive by default, you need to indicate them with the `rec` keyword.

```
let rec iter (x,y : nat * nat) : nat =
  if y = 0n then x else iter (y, x mod y)
 
let gcd (x, y : nat * nat) : nat =
  let (x, y) = if x < y then y,x else x,y in
  iter (x, y)
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/w3tBKN6FJ9RGtCCsfqzjwg).

This example function computes the greatest common divisor of two natural numbers.
The main logic is in the `iter` function. If `y` is `0n` we don’t need to continue and return it. Otherwise, the function calls itself, with the value of `y` as the argument for the parameter `x`. For the parameter `y`, we pass with the modulo operation the remainder of the division of `x` through `y`. 
Iter calls itself until `x` is 0.

With the function `gcd`, we just check if `x` is bigger than `y` and if that is not the case we switch the arguments `x` and `y` before entering them into our `iter` function. We do this to make sure that `x` is bigger than `y` and `y` and the greatest common denominator can be computed by `iter`.

One of the most common use cases for interactions are iterations over a collection of values, we will see in the next section how we can iterate over lists and maps.

## 2.9 Data Structures Tuple, List, Record, Map
In this section we will look into data structures and use the types *Tuple*, *List*, *Record* and *Map* to store multiple values. You will learn to create more complex contracts and apply what you learned in the sections before.

### Tuples
Let's first look at *tuples*, a simple data structure. 

* Tuples can store values of different types.
* Tuples have a fixed length, meaning that you can not add or delete values.
* Tuples only store values.

Tuples also have a specific order and the values that they store are called components.

**Declaration**
```
type name = (string * string)
```
**Definition**
```
let user = ("Alice", "Doe" : string * string)
```
**Access** 
You can access each component by their index.

```
let firstName: string = user.0
let lastName: string = user.1
```
 
**Example Contract: Full Name**
A simple contract that concatenated two strings.

```
type storage = string
type parameter = (string * string)
type return = operation list * storage
 
let main (p, s : parameter * storage) : return = 
 (([] : operation list), p.0 ^ " " ^ p.1)
```

Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/fMmRoHkAHZtJUw7ZtgKq4Q).
Example parameters: `"Jane", "Doe"`
Example storage: `"Bob Green"`

This is a very simple contract that gets a tuple of two strings and a storage string as arguments, and returns the storage in the form of a concatenated string from the parameter tuples.

Learn more about tuples in the [LIGOlang documentation](https://ligolang.org/docs/language-basics/sets-lists-tuples#tuples).

### Lists
Now we are going to look into *Lists*, you know them from the list of operations that we return in our main functions.

* Lists store values of the same type.
* Lists have a variable length.
* Lists only store values.

The special thing about Lists is that you can not access elements directly, only either the first item or the rest. But there are various ways to iterate over Lists, we will look into them soon. Lists are also ordered and elements in them can be repeated.

**Declaration**
`type my_list = int list`

**Definition**
```
let empty_list : int list = []
let my_list : int list = [1; 2; 2]
```

**Access**
The first element in a List is called the head, and the elements after it the tail. You can access them with the functions `List.head_opt` and `List.tail_opt`.
```
let head : int option = List.head_opt my_list // 1
let tail : int list option = List.tail_opt my_list // [2;2]
```

**Add**
You can add a new element before the head of the List with the cons operator `::`.
```
let larger_list : int list = 5 :: my_list
```

Now we learn how to iterate over data structures.

**Functional Iterators**
As you know we don’t use loops in cameLIGO but we can use functional iterators. A functional iterator is a function that calls a given function over every element of a data structure.

**Iterated Operation**
The first kind of functional iterator we are going to look at is called an *iterated operation*. The iterated operation doesn’t return any value, just a unit.

You can use it to check for values inside a list and if one value doesn’t meet the requirements fail with an error.

Use `List.iter` to to implement an iterated operation.

```
let majority_check (l, i : int list * int) : unit =
  let predicate = fun (j : int) -> assert (j > i)
  in List.iter predicate l
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/lcwKqBO6g1kbY0sr3iGgrw).
Example parameters: `[23;25;26],18`

With `majority_check`, the user can input a list and a value; `predicate` contains an anonymous function that checks if the passed integer value is bigger than the second parameter that is provided by the user. Finally with `List.iter` we execute `predicate` for every element of our list `l`.

**Mapped Operation**
With the functional operator *map operation* we can apply a function to every element inside a list and change its value. 

Use `List.map` to implement a mapped operation.

```
let list_increment (l : int list) : int list =
  let increment (i : int) : int = i + 1
  in List.map increment l
```
 
Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/cCvAnTWzCu0m5lj_XDL7Yg).
Example parameters: `[2;3;4]`
 
The function list_increment, the user can input a list and increase the value of all elements by `1`. With increment we increase each integer value by `1`.
We use the List.map to apply increment to each element of our list `l`.

The function `list_increment`, the user can input a list and increase the value of all elements by `1`. With increment we increase each integer value by `1`.
We use the `List.map` to apply increment to each element of our list `l`.

**Folded Operation**
The third and last kind of functional operator is called a *folded operation*. You can learn more about folded operations in the [LIGO documentation](https://ligolang.org/docs/language-basics/sets-lists-tuples#folded-operation-over-lists).

**Example contract: User Credit List**
In this contract we are storing a list of user names and their credits and are performing some of the operations on it that we just learned.

```
type name = string
type credits = int
type user = name * credits
type storage = user list
type parameter =
  Extend of user
| Increment
| Tail
type return = operation list * storage
 
let extend_list (u, s : user * storage) : storage = u :: s
 
let increment (u : user) : user = (u.0, u.1 + 1)
let increment_list (s : user list) : user list = List.map increment s
 
let get_tail (s : storage) : storage = 
 match List.tail_opt s with 
   Some(x) -> x
 | None -> []
 
let main (p, s : parameter * storage) : return =
 ([] : operation list), 
 (match p with
   Extend (u) -> extend_list (u, s)
 | Increment -> increment_list (s)
 | Tail -> get_tail (s))
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/5kMQFtdk-9MDme7HUvm4bw).
Example parameters: `Increment`
Example storage: `[("Alice",12);("Bob",3);("Celine",7)]`

Our storage is from the type `user list` which consist of a tuple of `name` and `credit` which are a `string` and an `int`.
Our contract has three different entrypoints. With `exend_list` we can add a new element at the top of our list with `increment_list` we can increment the credits of our users by one, and with `get_tail` we return all elements of the list but the first. 

### Sets
We won’t go into too many details of sets, but here is a brief overview.

* Sets only store values of the same type.
* Sets have a variable length.
* Sets only store values.

Sets are unique, meaning that values can not be repeated in a set and sets have no specific order which distinguishes them from lists.

We will not go into more detail explaining sets here, but you can learn more about them in the [LIGO documentation](https://ligolang.org/docs/language-basics/sets-lists-tuples#sets).

Until now we have looked at pretty basic data structures that could only store values. In the next part we will look into the more complex constructs, records and maps.

### Record
A record is a very heavily used data structure and you will encounter them everywhere.

* Records can store values of different types.
* Records have a fixed length.
* Records store fields.

A record is made of a set of fields, which consist of a field name and a field type.

**Declaration**
```
type user = {
  age: nat;
  username: string;
}
```
 
In this example the record user has two fields. The field name `age`, the corresponding field type is `nat`, as well as`username`, which is a `string`.

**Definition**
```
let alice : user = {
  age = 18n;
  username= "Alice";
}
```
 
**Access**
You can access the value of a given field by specifying the name of the record followed by a dot (period) and the field name.
```
let name: string = alice.username
```

**Functional Update**
LIGO offers a way to only update the fields that are modified, instead of having to replace the entire record.

```
type user = {
  age: nat;
  username: string;
}

let user_nineteen (p : user) : user =
  {p with age = 19n}
```

Test this function in the [LIGOlang IDE](https://ide.ligolang.org/p/53ZFpy_gmiDrX2wOHHK-qw).
Example parameters: `{ age = 21n; username = "Alice" }`

You can use the `with` keyword and the field name to update only the value instead of the whole record.

**Example contract: User Management Record**
In this contract we are storing a simple user record where we can update name and admin status.

```
type user = {
 id       : nat;
 is_admin : bool;
 name     : string
}
type storage = user
type parameter =
  Name of string
| Admin of bool
type return = operation list * storage
 
let update_name (n, s : string * storage) : storage =
 {s with name = n}
 
let update_admin (n, s : bool * storage) : storage =
 {s with is_admin = n}
 
let main (p, s : parameter * storage) : return =
 ([] : operation list), 
 (match p with
   Name (n)  -> update_name (n, s)
 | Admin (n) -> update_admin (n, s))
```

Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/dx2wF9i5LdjvBlGwZsf1gg).
Example parameters: `Name ("Alice the great")`
Example storage: `{ id = 50n ; is_admin = false ; name = "Alice" }`
 
In this contract we have a user record that stores the id, the admin status and the name of the user. We have the entrypoints `update_name` and `update_admin` that we can use to update the fields. At the moment we just have one user, let's change that. In the next part we are creating a map of records where we can store various users.

### Map
If you want to create more complex data structures you need to use `maps`. 

* Maps can store up to two different types.
* Maps have a variable length.
* Maps store key-value pairs.

A map stores bindings of keys and values. All keys must be of the same type and all values must be of the same type. Maps are often used in combination with other data structures like records.

**Declaration**
```
type usernames = (int, string) map
```

**Definition**
```
let my_usernames : usernames =
  Map.literal [
    (0, "Alice");
    (1, "Bob");
    (2, "Celia")
  ]
```

Here is how you can create an empty map.
`let empty : my_usernames = Map.empty`

**Access**
Access a value in a map with the function `Map.find_opt` and a key.
```
  let my_username : string option =
   Map.find_opt 1 my_usernames
```

**Update**
To update a map you need a value and the function Map.update.
```
  let update (u : usernames) : usernames =
   Map.update (2) (Some("Cillian")) u
```

In this case we are updating our value “Celia” with a new name “Cillian” we are using an optional value indicated by the keyword `Some` here to account for the possibility that we could have an empty value.
 
**Add**
To add a new element to a map we can use the function `Map.add` and provide a key and a value. 
```
  let add (u : usernames) : usernames =
   Map.add (3) ("Dan") u
```

**Remove**
To remove an element from a map we use the keyword `Map.remove` and need the key of the element.
```
  let remove (u : usernames) : usernames =
   Map.remove (2) u
```

**Iterated Operation**
Similar to the iterated operation for lists we can use an iterated operation for maps with the function `Map.iter`.
```
  let iter_op (u : usernames) : unit =
   let predicate = fun (i,j : int * string) -> assert (j <> "Bob")
   in Map.iter predicate u
```
 
In this example we test a map for the occurrence of the name `"Bob"` in the values.
 
**Map Operation**
Similar to the map operation for lists we can use a map operation for maps with the function `Map.map`.
```
  let map_op (u : usernames) : usernames =
   let add_user = fun (i,j : int * string) -> "user_" ^ j 
   in Map.map add_user u
```

In this example we add the string "user_" to every username.

Test these functions in the [LIGOlang IDE](https://ide.ligolang.org/p/MxmLkjboRs4te4KtBVv9gg).
Example parameters: `map_op`
Example storage: `Map.literal [(0, "Alice"); (1, "Bob"); (2, "Celia")]`

**Example contract: User Management Map**
In this contract we are building another system to manage our users, but this time we are able to handle multiple users and can add, update and remove them.

```
type user = { name : string ; is_admin : bool }
type id = nat
type user_storage = (id, user) map
type parameter =
  Add of id * user
| Update of id * user
| Remove of id
type return = operation list * user_storage
 
let add_entry (i, u, s : id * user * user_storage) : user_storage =
  Map.add i u s
 
let update_entry (i, u, s : id * user * user_storage) : user_storage =
  Map.update i (Some (u)) s
 
let remove_entry (i, s : id * user_storage) : user_storage =
  Map.remove i s
 
let main (p, s : parameter * user_storage) : return =
 ([] : operation list),
 (match p with
   Add (i, u)  -> add_entry (i, u, s)
 | Update (i, u) -> update_entry (i, u, s)
 | Remove (i) -> remove_entry (i, s))
```
 
In this contract we create a record called `user` with a field for the `name`, which is a `string` and a field for the admin status, which is a boolean.
We create a type `id` which is a `nat` and map it to our user record.

We create the entrypoints to add a new entry, to update an entry and to remove an entry. In the case of `add_entry` and `update_entry` we have a tuple with three components as parameter, so we can pass the key, the new record and the storage.

Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/jwCaEr58GCxuLcrDkkqHlw).
Example parameters: `Add(3n,{ name="Dan"; is_admin=true})`
Example storage: 
```
Map.literal [ 
 0n, { name="Alice"; is_admin=false }; 
 1n, { name="Bob"; is_admin=false }; 
 2n, { name="Celia"; is_admin=false };
]
```
 
**Big Maps**
There is one special type of map, called a *big map*. You should use big maps if you intend to create a data structure that potentially needs to be able to handle a very large amount of elements.

Learn more about big maps in the [LIGO documentation](https://ligolang.org/docs/language-basics/maps-records#big-maps).

## 2.10 CLI
In this section, you will learn how to use the command line interface (CLI) to test, compile and deploy your contracts.

We will use a Docker container to run the LIGOlang CLI. Make sure that you have Docker installed. You can download Docker on the [Docker homepage](https://docs.docker.com/get-docker/).

Hint: If you are having problems installing Docker on windows, try to download the [Linux update package](https://docs.microsoft.com/en-gb/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package).

After you have successfully installed Docker you can run LIGO in your terminal.

**On Linux or OSX**
```
docker run --rm -v "$PWD":"$PWD" -w "$PWD" ligolang/ligo:0.19.0
```

**On Windows**
```
docker run --rm -v "%CD%":/cd -w /cd ligolang/ligo:0.19.0
```

Hint: If you have trouble running LIGO through this command on windows try:
```
docker run --rm -v ${pwd}:/cd -w /cd ligolang/ligo:0.19.0
```

Now you should see various commands that should look familiar from the functionality of the IDE.

`compile-contract`

`compile-expression`

`dry-run`

`evaluate-call`

`evaluate-value`

You can compile your contract and an expression, dry run your contract and evaluate a function and value.

// Add Tezos Client interactions, still having problems to find the easiest way to get the client running on windows.

## 2.11 Transactions
In this section, we will learn how to make a Tezos transaction through a smart contract.

To transfer tez to an account or a smart contract you can use the built-in function `Tezos.transaction`.

A transaction operation to a wallet looks like this:

```
let payoutOperation : operation = 
Tezos.transaction unit amount receiver_contract
```

The first parameter is either the entrypoint to another contract or if we transfer tez to another wallet its `unit`, like in this example.

The second parameter is the amount that we want to transfer in mutez.

The third parameter is a contract interface of the recipient, that you can retrieve from the address of a wallet or another contract.

Let’s look at a contract example to make this clearer.

**Example contact: Simple Transaction**
```
let ownerAddress : address =
  ("tz1VburAsF7JxEyJE7K8ZSodVsrSXa57vPw2" : address)
 
let main (p, s: unit * unit) : operation list * unit =
 
  let receiver : unit contract =
    match (Tezos.get_contract_opt ownerAddress : unit contract option) with
    | Some (contract) -> contract
    | None -> (failwith ("Not a contract") : (unit contract))
  in
 
  let payoutOperation : operation = 
    Tezos.transaction unit amount receiver 
  in
  let operations : operation list = 
    [payoutOperation] 
  in
  ((operations: operation list), s)
```
Test this contract in the [LIGOlang IDE](https://ide.ligolang.org/p/RNeHMuOL7Nsk4iGBqsbKAA).
Storage: `unit`

We first created an `ownerAddress` with the address of the beneficiary of the transaction.
Then a very simple main function that does practically nothing.

To create the receiver, we wrap the address as a unit contract that represents an account. But before we do that we need to check if the account exists. If it doesn’t we fail the transaction with an error message.

In the last step, we will create a transaction to an account and not a contract, so we will use `unit` as the first parameter and then pass the `amount` and the `receiver` contract interface.
We need to create a list of operations that we will return at the end of the contract, which in this case will be just one, and then return the list at the end of the contract as well as our updated `s` storage.

That’s it! You can deploy your contract now.
//GIF showing how to deploy the contract

After the deployment, you can use [better-call-dev](https://better-call.dev/) to test your contract and make a transaction.
//GIF showing how to make a transaction from one account to another.

## 2.12 The FA2 Token Standard (WIP)

In this section, we will get an introduction to the *FA2* token standard.

A crypto token or simply token is a digital asset whose ownership is stored on a blockchain. 

A token can be *fungible* which means that all tokens of this type are the same and they are interchangeable. This is the case for cryptocurrencies like tez or btc for example.

A token can also be *non-fungible*, which means that all tokens are different. Such a token is called non-fungible token (*NFT*) and it can represent ownership of unique assets like digital art, music or in-game items.

FA2 is a token standard on Tezos similar to the ERC-20 token standard on Ethereum. A token standard helps to standardize important features of tokens like functionality and permissions. This allows us to create common interface standards so that developers can build applications that interact with tokens like wallets, exchanges, or games.

An FA2 compliant token must follow a list of rules. It must have the following entrypoints:

```
type fa2_entry_points =
 
| Transfer of transfer list
| Balance_of of balance_of_param
| Total_supply of total_supply_param
| Token_metadata of token_metadata_param
| Permissions_descriptor of permissions_descriptor contract
| Update_operators of update_operator list
| Is_operator of is_operator_param
```

**Transfer**
The `Transfer` entrypoint transfers tokens between owners.

**Balance of**
The `Balance_of` entrypoint gets the balance of multiple account/token pairs.

**Metadata**
The `token_metadata` entrypoint gets the metadata for multiple token types.

**Total supply**
The `Total_supply` entrypoint gets the total supply of tokens for multiple token types.

You can learn more about the FA2 token standard on GitLab [LIGO/Michelson implementation](https://gitlab.com/tezos/tzip/-/blob/master/proposals/tzip-12/implementing-fa2.md).
