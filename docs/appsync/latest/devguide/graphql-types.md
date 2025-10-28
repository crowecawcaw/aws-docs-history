# GraphQL types

GraphQL supports many different types. As you saw in the previous section, types define the shape or
behavior of your data. They are the fundamental building blocks of a GraphQL schema.

Types can be categorized into inputs and outputs. Inputs are types that are allowed to be passed in as
the argument for the special object types (`Query`, `Mutation`, etc.), whereas
output types are strictly used to store and return data. A list of types and their categorizations are
listed below:

- **Objects**: An object contains fields describing an entity. For
  instance, an object could be something like a `book` with fields describing its
  characteristics like `authorName`, `publishingYear`, etc. They are strictly
  output types.
- **Scalars**: These are primitive types like int, string, etc. They
  are typically assigned to fields. Using the `authorName` field as an example, it could
  be assigned the `String` scalar to store a name like "John Smith". Scalars can be both
  input and output types.
- **Inputs**: Inputs allow you to pass a group of fields as an
  argument. They are structured very similarly to objects, but they can be passed in as arguments to
  special objects. Inputs allow you to define scalars, enums, and other inputs in its scope. Inputs
  can only be input types.
- **Special objects**: Special objects perform state-changing
  operations and do the bulk of the heavy lifting of the service. There are three special object
  types: query, mutation, and subscription. Queries typically fetch data; mutations manipulate data;
  subscriptions open and maintain a two-way connection between clients and servers for constant
  communication. Special objects are neither input nor output given their functionality.
- **Enums**: Enums are predefined lists of legal values. If you call
  an enum, its values can only be what's defined in its scope. For example, if you had an enum called
  `trafficLights` depicting a list of traffic signals, it could have values like
  `redLight` and `greenLight` but not `purpleLight`. A real
  traffic light will only have so many signals, so you could use the enum to define them and force
  them to be the only legal values when referencing `trafficLight`. Enums can be both
  input and output types.
- **Unions/interfaces**: Unions allow you to return one or more
  things in a request depending on the data that was requested by the client. For example, if you had
  a `Book` type with a `title` field and an `Author` type with a
  `name` field, you could create a union between both types. If your client wanted to
  query a database for the phrase "Julius Caesar", the union could return _Julius Caesar_ (the play by William Shakespeare) from the `Book`
  `title` and _Julius Caesar_ (the author of _Commentarii de Bello Gallico_) from the `Author`
  `name`. Unions can only be output types.

Interfaces are sets of fields that objects must implement. This is a bit
similar to interfaces in programming languages like Java where you must
implement the fields defined in the interface. For example, let's say you made
an interface called `Book` that contained a `title`
field. Let's say you later created a type called `Novel` that
implemented `Book`. Your `Novel` would have to include a
`title` field. However, your `Novel` could also
include other fields not in the interface like `pageCount` or
`ISBN`. Interfaces can only be output types.
The following sections will explain how each type works in GraphQL.

## Objects

GraphQL objects are the main type you will see in production code. In GraphQL, you can think of an
object as a grouping of different fields (similar to variables in other languages), with each field
being defined by a type (typically a scalar or another object) that can hold a value. Objects
represent a unit of data that can be retrieved/manipulated from your service implementation.

Object types are declared using the `Type` keyword. Let's modify our schema example
slightly:

```
type Person {
  id: ID!
  name: String
  age: Int
  occupation: **Occupation**
}

type **Occupation** {
  title: String
}
```

The object types here are `Person` and `Occupation`. Each object has its own
fields with its own types. One feature of GraphQL is the ability to set fields to other types. You can
see the `occupation` field in `Person` contains an `Occupation`
object type. We can make this association because GraphQL is only describing the data and not the
implementation of the service.

## Scalars

Scalars are essentially primitive types that hold values. In AWS AppSync, there are two types of
scalars: the default GraphQL scalars and AWS AppSync scalars. Scalars are typically used to store field
values within object types. Default GraphQL types include `Int`, `Float`,
`String`, `Boolean`, and `ID`. Let's use the previous example
again:

```
type Person {
  id: ID!
  **name**: String
  age: Int
  occupation: Occupation
}

type Occupation {
  **title**: String
}
```

Singling out the `name` and `title` fields, both hold a `String`
scalar. `Name` could return a string value like "`John Smith`" and the title
could return something like "`firefighter`". Some GraphQL implementations also support
custom scalars using the `Scalar` keyword and implementing the type's behavior. However,
AWS AppSync currently **doesn't support** custom scalars. For a list of
scalars, see [Scalar types in
AWS AppSync](scalars.md "scalars.md").

## Inputs

Due to the concept of input and output types, there are certain restrictions in place when passing
in arguments. Types that commonly need to be passed in, especially objects, are restricted. You can
use the input type to bypass this rule. Inputs are types that contain scalars, enums, and other input
types.

Inputs are defined using the `input` keyword:

```
type Person {
  id: ID!
  name: String
  age: Int
  occupation: Occupation
}

type Occupation {
  title: String
}

**input personInput {
 id: ID!
 name: String
 age: Int
 occupation: occupationInput
}

input occupationInput {
 title: String
}**
```

As you can see, we can have separate inputs that mimic the original type. These inputs will often
be used in your field operations like this:

```
type Person {
  id: ID!
  name: String
  age: Int
  occupation: Occupation
}

type Occupation {
  title: String
}

input **occupationInput** {
  title: String
}

type Mutation {
  addPerson(id: ID!, name: String, age: Int, occupation: **occupationInput**): Person
}
```

Note how we're still passing `occupationInput` in place of `Occupation` to
create a `Person`.

This is but one scenario for inputs. They don't necessarily need to copy objects 1:1, and in
production code, you most likely won't be using it like this. It's good practice to take advantage of
GraphQL schemas by defining only what you need to input as arguments.

Also, the same inputs can be used in multiple operations, but we don't recommend doing this. Each
operation should ideally contain its own unique copy of the inputs in case the schema's requirements
change.

## Special objects

GraphQL reserves a few keywords for special objects that define some of the business logic for how
your schema will retrieve/manipulate data. At most, there can be one of each of these keywords in a
schema. They act as entry points for all requested data that your clients run against your GraphQL
service.

Special objects are also defined using the `type` keyword. Though they're used
differently from regular object types, their implementation is very similar.

Queries
Queries are very similar to `GET` operations in that they perform a read-only
fetch to get data from your source. In GraphQL, the `Query` defines all of the
entry points for clients making requests against your server. There will always be a
`Query` in your GraphQL implementation.

Here are the `Query` and modified object types we used in our previous schema
example:

```
type Person {
  id: ID!
  name: String
  age: Int
  occupation: Occupation
}
type Occupation {
  title: String
}
type Query {
  people: [Person]
}
```

Our `Query` contains a field called `people` that returns a list of
`Person` instances from the data source. Let's say we need to change the
behavior of our application, and now we need to return a list of only the
`Occupation` instances for some separate purpose. We could simply add it to the
query:

```
type Query {
  people: [Person]
  occupations: [Occupation]
}
```

In GraphQL, we can treat our query as the single source of requests. As you can see, this
is potentially much simpler than RESTful implementations that might use different endpoints
to achieve the same thing (`.../api/1/people` and
`.../api/1/occupations`).

Assuming we have a resolver implementation for this
query, we can now perform an actual query.
While the `Query` type exists, we have to explicitly call it for it to run in the
application's code. This can be done using the `query` keyword:

```
query getItems {
   people {
      name
   }
   occupations {
      title
   }
}
```

As you can see, this query is called `getItems` and returns `people`
(a list of `Person` objects) and `occupations` (a list of
`Occupation` objects). In `people`, we're returning only the
`name` field of each `Person`, while we're returning the
`title` field of each `Occupation`. The response may look like
this:

```
{
  "data": {
    "people": [
      {
        "name": "John Smith"
      },
      {
        "name": "Andrew Miller"
      },
      .
      .
      .
    ],
    "occupations": [
      {
        "title": "Firefighter"
      },
      {
        "title": "Bookkeeper"
      },
      .
      .
      .
    ]
  }
}
```

The example response shows how the data follows the shape of the query. Each entry
retrieved is listed within the scope of the field. `people` and
`occupations` are returning things as separate lists. Though useful, it might
be more convenient to modify the query to return a list of people's names and
occupations:

```
query getItems {
   people {
      name
      occupation {
        title
      }
}
```

This is a legal modification because our `Person` type contains an
`occupation` field of type `Occupation`. When listed within the
scope of `people`, we're returning each `Person`'s `name`
along with their associated `Occupation` by `title`. The response may
look like this:

```
}
  "data": {
    "people": [
      {
        "name": "John Smith",
        "occupation": {
          "title": "Firefighter"
        }
      },
      {
        "name": "Andrew Miller",
        "occupation": {
          "title": "Bookkeeper"
        }
      },
      .
      .
      .
    ]
  }
}
```

Mutations
Mutations are similar to state-changing operations like `PUT` or
`POST`. They perform a write operation to modify data in the source, then fetch
the response. They define your entry points for data modification requests. Unlike queries, a
mutation may or may not be included in the schema depending on the project's needs. Here's
the mutation from the schema example:

```
type Mutation {
  addPerson(id: ID!, name: String, age: Int): Person
}
```

The `addPerson` field represents one entry point that adds a
`Person` to the data source. `addPerson` is the field name;
`id`, `name`, and `age` are the parameters; and
`Person` is the return type. Looking back at the `Person`
type:

```
type Person {
  id: ID!
  name: String
  age: Int
  occupation: Occupation
}
```

We added the `occupation` field. However, we cannot set this field to
`Occupation` directly because objects cannot be passed in as arguments; they
are strictly output types. We should instead pass an input with the same fields as an
argument:

```
input occupationInput {
  title: String
}
```

We can also easily update our `addPerson` to include this as a parameter when
making new `Person` instances:

```
type Mutation {
  addPerson(id: ID!, name: String, age: Int, **occupation: occupationInput**): Person
}
```

Here's the updated schema:

```
type Person {
  id: ID!
  name: String
  age: Int
  occupation: Occupation
}

type Occupation {
  title: String
}

input occupationInput {
  title: String
}

type Mutation {
  addPerson(id: ID!, name: String, age: Int, occupation: occupationInput): Person
}
```

Note that `occupation` will pass in the `title` field from
`occupationInput` to complete the creation of the `Person` instead
of the original `Occupation` object. Assuming we have a resolver implementation
for `addPerson`, we can now perform an actual mutation. While the
`Mutation` type exists, we have to explicitly call it for it to run in the
application's code. This can be done using the `mutation` keyword:

```
mutation createPerson {
  addPerson(id: ID!, name: String, age: Int, occupation: occupationInput) {
    name
    age
    occupation {
      title
    }
  }
}
```

This mutation is called `createPerson`, and `addPerson` is the
operation. To create a new `Person`, we can enter the arguments for
`id`, `name`, `age`, and `occupation`. In the
scope of `addPerson`, we can also see other fields like `name`,
`age`, etc. This is your response; these are the fields that will be returned
after the `addPerson` operation is complete. Here's the final part of the
example:

```
mutation createPerson {
  addPerson(id: "**1**", name: "**Steve Powers**", age: "**50**", occupation: "**Miner**") {
    id
    name
    age
    occupation {
      title
    }
  }
}
```

Using this mutation, a result might look like this:

```
{
  "data": {
    "addPerson": {
      "id": "**1**",
      "name": "**Steve Powers**",
      "age": "**50**",
      "occupation": {
        "title": "**Miner**"
      }
    }
  }
}
```

As you can see, the response returned the values we requested in the same format that was
defined in our mutation. It's good practice to return all values that were modified to reduce
confusion and the need for more queries in the future. Mutations allow you to include
multiple operations within its scope. They will be run sequentially in the order listed in
the mutation. For example, if we create another operation called `addOccupation`
that adds job titles to the data source, we can call this in the mutation after
`addPerson`. `addPerson` will be handled first followed by
`addOccupation`.

Subscriptions
Subscriptions use [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications "https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications") to open a lasting, two-way connection between the server and its
clients. Typically, a client will subscribe, or listen, to the server. Whenever the server
makes a server-side change or performs an event, the subscribed client will receive the
updates. This type of protocol is useful when multiple clients are subscribed and need to be
notified about changes happening in the server or other clients. For instance, subscriptions
can be used to update social media feeds. There could be two users, User A and User B, who
are both subscribed to automatic notification updates whenever they receive direct messages.
User A on Client A could send a direct message to User B on Client B. User A's client would
send the direct message, which would be processed by the server. The server would then send
the direct message to User B's account while sending an automatic notification to Client
B.

Here's an example of a `Subscription` that we could add to the schema
example:

```
type Subscription {
  personAdded: Person
}
```

The `personAdded` field will send a message to subscribed clients whenever a
new `Person` is added to the data source. Assuming we have a resolver
implementation for `personAdded`, we can now use the subscription. While the
`Subscription` type exists, we have to explicitly call it for it to run in the
application's code. This can be done using the `subscription` keyword:

```
subscription personAddedOperation {
  personAdded {
    id
    name
  }
}
```

The subscription is called `personAddedOperation`, and the operation is
`personAdded`. `personAdded` will return the `id` and
`name` fields of new `Person` instances. Looking at the mutation
example, we added a `Person` using this operation:

```
addPerson(id: "**1**", name: "**Steve Powers**", age: "**50**", occupation: "**Miner**")
```

If our clients were subscribed to updates to the newly added `Person`, they
might see this after `addPerson` runs:

```
{
  "data": {
    "personAdded": {
      "id": "**1**",
      "name": "**Steve Powers**"
    }
  }
}
```

Below is a summary of what subscriptions offer:

Subscriptions are two-way channels that allow the client and server to receive quick, but
steady, updates. They typically use the WebSocket protocol, which creates standardized and
secure connections.

Subscriptions are nimble in that they reduce connection setup overhead. Once subscribed, a
client can just keep running on that subscription for long periods of time. They generally
use computing resources efficiently by allowing developers to tailor the lifetime of the
subscription and to configure what information will be requested.

In general, subscriptions allow the client to make multiple subscriptions at once. As it
pertains to AWS AppSync, subscriptions are only used for receiving real-time updates from the
AWS AppSync service. They cannot be used to perform queries or mutations.

The main alternative to subscriptions is polling, which sends queries at set intervals to
request data. This process is typically less efficient than subscriptions and puts a lot of
strain on both the client and the backend.

One thing that wasn't mentioned in our schema example was the fact that your special object types
must also be defined in a `schema` root. So when you export a schema in AWS AppSync, it might
look like this:

schema.graphql

```
schema {
  query: Query
  mutation: Mutation
  subscription: Subscription
}

.
.
.

type Query {
  # code goes here
}
type Mutation {
  # code goes here
}
type Subscription {
  # code goes here
}
```

## Enumerations

Enumerations, or enums, are special scalars that limit the legal arguments a type or field may
have. This means that whenever an enum is defined in the schema, its associated type or field will be
limited to the values in the enum. Enums are serialized as string scalars. Note that different
programming languages may handle GraphQL enums differently. For example, JavaScript has no native enum
support, so the enum values may be mapped to int values instead.

Enums are defined using the `enum` keyword. Here's an example:

```
enum trafficSignals {
  solidRed
  solidYellow
  solidGreen
  greenArrowLeft
  ...
}
```

When calling the `trafficLights` enum, the argument(s) can only be
`solidRed`, `solidYellow`, `solidGreen`, etc. It's common to use
enums to depict things that have a distinct but limited number of choices.

## Unions/Interfaces

See [Interfaces
and unions](interfaces-and-unions.md "interfaces-and-unions.md") in GraphQL.
