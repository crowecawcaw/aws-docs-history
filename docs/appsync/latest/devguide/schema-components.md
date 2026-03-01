# GraphQL schemas

The GraphQL schema is the foundation of a GraphQL API. It serves as the blueprint that defines the shape
of your data. It's also a contract between your client and server that defines how your data will be
retrieved and/or modified.

GraphQL schemas are written in the _Schema Definition Language_ (SDL).
SDL is composed of types and fields with an established structure:

- **Types**: Types are how GraphQL defines the shape and behavior of the
  data. GraphQL supports a multitude of types that will be explained later in this section. Each type
  that's defined in your schema will contain its own scope. Inside the scope will be one or more fields
  that can contain a value or logic that will be used in your GraphQL service. Types fill many different
  roles, the most common being objects or scalars (primitive value types).
- **Fields**: Fields exist within the scope of a type and hold the value
  that's requested from the GraphQL service. These are very similar to variables in other programming
  languages. The shape of the data you define in your fields will determine how the data is structured
  in a request/response operation. This allows developers to predict what will be returned without
  knowing how the backend of the service is implemented.
  To visualize what a schema would look like, let's review the contents of a simple GraphQL schema. In
  production code, your schema will typically be in a file called `schema.graphql` or
  `schema.json`. Let's assume that we're peering into a project that implements a GraphQL
  service. This project is storing company personnel data, and the `schema.graphql` file is being
  used to retrieve personnel data and add new personnel to a database. The code may look like this:

schema.graphql

```
type Person {
   id: ID!
   name: String
   age: Int
}
type Query {
  people: [Person]
}
type Mutation {
  addPerson(id: ID!, name: String, age: Int): Person
}
```

We can see that there are three types defined in the schema: `Person`, `Query`, and
`Mutation`. Looking at `Person`, we can guess that this is the blueprint for an
instance of a company employee, which would make this type an object. Inside its scope, we see
`id`, `name`, and `age`. These are the fields that define the properties
of a `Person`. This means our data source stores each `Person`'s `name` as
a `String` scalar (primitive) type and `age` as an `Int` scalar (primitive)
type. The `id` acts as a special, unique identifier for each `Person`. It's also a
required value as denoted by the `!` symbol.

The next two object types behave differently. GraphQL reserves a few keywords for special object types
that define how the data will be populated in the schema. A `Query` type will retrieve data from
the source. In our example, our query might retrieve `Person` objects from a database. This may
remind you of `GET` operations in RESTful terminology. A `Mutation` will modify data.
In our example, our mutation may add more `Person` objects to the database. This may remind you
of state-changing operations like `PUT` or `POST`. The behaviors of all special object
types will be explained later in this section.

Let's assume the `Query` in our example will retrieve something from the database. If we look
at the fields of `Query`, we see one field called `people`. Its field value is
`[Person]`. This means we want to retrieve some instance of `Person` in the
database. However, the addition of brackets means that we want to return a list of all `Person`
instances and not just a specific one.

The `Mutation` type is responsible for performing state-changing operations like data
modification. A mutation is responsible for performing some state-changing operation on the data source. In
our example, our mutation contains an operation called `addPerson` that adds a new
`Person` object to the database. The mutation uses a `Person` and expects an input
for the `id`, `name`, and `age` fields.

At this point, you may be wondering how operations like `addPerson` work without a code
implementation given that it supposedly performs some behavior and looks a lot like a function with a
function name and parameters. Currently, it won't work because a schema only serves as the declaration. To
implement the behavior of `addPerson`, we would have to add a resolver to it. A resolver is a
unit of code that is executed whenever its associated field (in this case, the `addPerson`
operation) is called. If you want to use an operation, you'll have to add the resolver implementation at
some point. In a way, you can think of the schema operation as the function declaration and the resolver as
the definition. Resolvers will be explained in a different section.

This example shows only the simplest ways a schema can manipulate data. You build complex, robust, and
scalable applications by leveraging the features of GraphQL and AWS AppSync. In the next section, we'll define
all of the different types and field behaviors you can utilize in your schema.

As you can see, there are many moving components in GraphQL. In this section, we showed the structure of
a simple schema and the different types and fields a schema supports. In the following section, you will
discover the other components of a GraphQL API and how they work with the schema.
