# GraphQL fields

Fields exist within the scope of a type and hold the value that's requested from the GraphQL service.
These are very similar to variables in other programming languages. For example, here's a
`Person` object type:

```
type Person {
   **name: String
 age: Int**
}
```

The fields in this case are `name` and `age` and hold a `String` and
`Int` value, respectively. Object fields like the ones shown above can be used as the
inputs in the fields (operations) of your queries and mutations. For example, see the `Query`
below:

```
type Query {
  **people: [Person]**
}
```

The `people` field is requesting all instances of `Person` from the data source.
When you add or retrieve a `Person` in your GraphQL server, you can expect the data to follow
the format of your types and fields, that is, the structure of your data in the schema determines how
it'll be structured in your response:

```
}
  "data": {
    "people": [
      {
        "name": "John Smith",
        "age": "50"
      },
      {
        "name": "Andrew Miller",
        "age": "60"
      },
      .
      .
      .
    ]
  }
}
```

Fields play an important role in structuring data. There are a couple of additional properties
explained below that can be applied to fields for more customization.

## Lists

Lists return all items of a specified type. A list can be added to a field's type using brackets
`[]`:

```
type Person {
  name: String
  age: Int
}
type Query {
  people: **[Person]**
}
```

In `Query`, the brackets surrounding `Person` indicate that you want to
return all instances of `Person` from the data source as an array. In the response, the
`name` and `age` values of each `Person` will be returned as a
single, delimited list:

```
}
  "data": {
    "people": [
      {
        "name": "John Smith",         # Data of Person 1
        "age": "50"
      },
      {
        "name": "Andrew Miller",      # Data of Person 2
        "age": "60"
      },
      .                               # Data of Person N
      .
      .
    ]
  }
}
```

You aren't limited to special object types. You can also use lists in the fields of regular object
types.

## Non-nulls

Non-nulls indicate a field that cannot be null in the response. You can set a field to non-null by
using the `!` symbol:

```
type Person {
  name: **String!**
  age: Int
}
type Query {
  people: [Person]
}
```

The `name` field cannot be explicitly null. If you were to query the data source and
provided a null input for this field, an error would be thrown.

You can combine lists and non-nulls. Compare these queries:

```
type Query {
  people: **[Person!]**      # Use case 1
}

.
.
.

type Query {
  people: **[Person]!**      # Use case 2
}

.
.
.

type Query {
  people: **[Person!]!**     # Use case 3
}
```

In use case 1, the list cannot contain null items. In use case 2, the list itself cannot be set to
null. In use case 3, the list and its items cannot be null. However, in any case, you can still return
empty lists.
