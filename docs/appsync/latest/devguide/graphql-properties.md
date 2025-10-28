# Additional properties of GraphQL

GraphQL consists of several design principles to maintain simplicity and robustness at scale.

## Declarative

GraphQL is declarative, which means the user will describe (shape) the data by only declaring the fields
they want to query. The response will only return the data for these properties. For example, here's an
operation that retrieves a `Book` object in a DynamoDB table with the ISBN 13 `id` value
of `9780199536061`:

```
{
  getBook(id: "`9780199536061`") {
    name
    year
    author
  }
}
```

The response will return the fields in the payload (`name`, `year`, and
`author`) and nothing else:

```
{
  "data": {
    "getBook": {
      "name": "Anna Karenina",
      "year": "1878",
      "author": "Leo Tolstoy",
    }
  }
}
```

Because of this design principle, GraphQL eliminates the perennial issues of over- and under-fetching
that REST APIs deal with in complex systems. This results in more efficient data gathering and improved
network performance.

## Hierarchical

GraphQL is flexible in that the data requested can be shaped by the user to fit the needs of the
application. Requested data always follows the types and syntax of the properties defined in your GraphQL
API. For instance, the following snippet shows the `getBook` operation with a new field scope
called `quotes` that returns all stored quote strings and pages linked to the `Book`
`9780199536061`:

```
{
  getBook(id: "`9780199536061`") {
    name
    year
    author
    quotes {
      description
      page
    }
  }
}
```

Running this query returns the following result:

```
{
  "data": {
    "getBook": {
      "name": "Anna Karenina",
      "year": "1878",
      "author": "Leo Tolstoy",
      "quotes": [
         {
            "description": "The highest Petersburg society is essentially one: in it everyone knows everyone else, everyone even visits everyone else.",
            "page": 135
         },
         {
            "description": "Happy families are all alike; every unhappy family is unhappy in its own way.",
            "page": 1
         },
         {
            "description": "To Konstantin, the peasant was simply the chief partner in their common labor.",
            "page": 251
         }
      ]
    }
  }
}
```

As you can see, the `quotes` fields linked to the requested book was returned as an array in
the same format that was described by our query. Although it wasn't shown here, GraphQL has the added
advantage of not being particular about the location of the data it's retrieving. `Books` and
`quotes` could be stored separately, but GraphQL will still retrieve the information so long
as the association exists. This means your query can retrieve multitudes of standalone data in a single
request.

## Introspective

GraphQL is self-documenting, or introspective. It supports several built-in operations that allow users
to view the underlying types and fields within the schema. For example, here's a `Foo` type with
a `date` and `description` field:

```
type Foo {
	date: String
	description: String
}
```

We could use the `_type` operation to find the typing metadata underneath the schema:

```
{
  __type(name: "Foo") {
    name                   # returns the name of the type
    fields {               # returns all fields in the type
      name                 # returns the name of each field
      type {               # returns all types for each field
        name               # returns the scalar type
      }
    }
  }
}
```

This will return a response:

```
{
  "__type": {
    "name": "Foo",                     # The type name
    "fields": [
      {
        "name": "date",                # The date field
        "type": { "name": "String" }   # The date's type
      },
      {
        "name": "description",         # The description field
        "type": { "name": "String" }   # The description's type
      },
    ]
  }
}
```

This feature can be used to find out what types and fields a particular GraphQL schema supports. GraphQL
supports a wide variety of these introspective operations. For more information, see [Introspection](https://graphql.org/learn/introspection/ "https://graphql.org/learn/introspection/").

## Strong typing

GraphQL supports strong typing through its types and fields system. When you define something in your
schema, it must have a type that can be validated before runtime. It must also follow GraphQL's syntax
specification. This concept is no different from programming in other languages. For example, here's the
`Foo` type from earlier:

```
type Foo {
	date: String
	description: String
}
```

We can see that `Foo` is the object that will be created. Inside an instance of
`Foo`, there will be a `date` and `description` field, both of the
`String` primitive type (scalar). Syntactically, we see that `Foo` was declared,
and its fields exist inside its scope. This combination of type checking and logical syntax ensures that
your GraphQL API is concise and self-evident. GraphQL's typing and syntax specification can be found [here](https://spec.graphql.org/ "https://spec.graphql.org/").
