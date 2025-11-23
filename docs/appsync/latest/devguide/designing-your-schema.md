# Designing your GraphQL schema

The GraphQL schema is the foundation of any GraphQL server implementation. Each GraphQL API is defined by a
**single** schema that contains types and fields describing how the data from
requests will be populated. The data flowing through your API and the operations performed must be validated
against the schema.

In general, the [GraphQL type system](https://graphql.org/learn/schema/#type-system "https://graphql.org/learn/schema/#type-system")
describes the capabilities of a GraphQL server and is used to determine if a query is valid. A server’s type
system is often referred to as that server’s schema and can consist of different object types, scalar types,
input types, and more. GraphQL is both declarative and strongly typed, meaning the types will be well-defined at
runtime and will only return what was specified.

AWS AppSync allows you to define and configure GraphQL schemas. The following section describes how to create
GraphQL schemas from scratch using AWS AppSync's services.

## Structuring a GraphQL Schema

###### Tip

We recommend reviewing the [Schemas](schema-components.md "schema-components.md") section before
continuing.

GraphQL is a powerful tool for implementing API services. According to [GraphQL's website](https://graphql.org/ "https://graphql.org/"), GraphQL is the following:

"_GraphQL is a query language for APIs and a runtime for fulfilling those
queries with your existing data. GraphQL provides a complete and understandable description of the
data in your API, gives clients the power to ask for exactly what they need and nothing more, makes
it easier to evolve APIs over time, and enables powerful developer tools._"

This section covers the very first part of your GraphQL implementation, the schema. Using the quote above,
a schema plays the role of "providing a complete and understandable description of the data in your API". In
other words, a GraphQL schema is a textual representation of your service's data, operations, and the
relations between them. The schema is considered the main entry point for your GraphQL service
implementation. Unsurprisingly, it's often one of the first things you make in your project. We recommend
reviewing the [Schemas](schema-components.md "schema-components.md") section before continuing.

To quote the [Schemas](schema-components.md "schema-components.md") section, GraphQL schemas are written in the _Schema Definition
Language_ (SDL). SDL is composed of types and fields with an established structure:

- **Types**: Types are how GraphQL defines the shape and behavior of
  the data. GraphQL supports a multitude of types that will be explained later in this section. Each
  type that's defined in your schema will contain its own scope. Inside the scope will be one or more
  fields that can contain a value or logic that will be used in your GraphQL service. Types fill many
  different roles, the most common being objects or scalars (primitive value types).
- **Fields**: Fields exist within the scope of a type and hold the
  value that's requested from the GraphQL service. These are very similar to variables in other
  programming languages. The shape of the data you define in your fields will determine how the data
  is structured in a request/response operation. This allows developers to predict what will be
  returned without knowing how the backend of the service is implemented.

The simplest schemas will contain three different data categories:

1. **Schema roots**: Roots define the entry points of your schema. It
   points to the fields that will be performing some operation on the data like adding, deleting, or
   modifying something.
2. **Types**: These are base types that are used to represent the shape
   of the data. You can almost think of these as objects or abstract representations of something with
   defined characteristics. For example, you could make a `Person` object that represents a
   person in a database. Each person's characteristics will be defined inside the `Person`
   as fields. They can be anything like the person's name, age, job, address, etc.
3. **Special object types**: These are the types that define the
   behavior of the operations in your schema. Each special object type is defined once per schema. They
   are first placed in the schema root, then defined in the schema body. Each field in a special object
   type defines a single operation to be implemented by your resolver.

To put this into perspective, imagine you're creating a service that stores authors and the books they've
written. Each author has a name and an array of books they've authored. Each book has a name and a list of
associated authors. We also want the ability to add or retrieve books and authors. A simple UML
representation of this relationship may look like this:

![UML diagram showing Author and Book classes with attributes and methods, linked by association.](images/GraphQL-UML-1.png)

In GraphQL, the entities `Author` and `Book` represent two different object types in
your schema:

```
type **Author** {
}

type **Book** {
}
```

`Author` contains `authorName` and `Books`, while `Book`
contains `bookName` and `Authors`. These can be represented as the fields within the
scope of your types:

```
type Author {
 **authorName: String
 Books: [Book]**
}

type Book {**bookName: String
 Authors: [Author]**
}
```

As you can see, the type representations are very close to the diagram. However, the methods are where it
gets a bit trickier. These will be placed in one of a few special object types as a field. Their special
object categorization depends on their behavior. GraphQL contains three fundamental special object types:
queries, mutations, and subscriptions. For more information, see [Special
objects](graphql-types.md#special-object-components "graphql-types.md#special-object-components").

Because `getAuthor` and `getBook` are both requesting data, they will be placed in a
`Query` special object type:

```
type Author {
  authorName: String
  Books: [Book]
}

type Book {
  bookName: String
  Authors: [Author]
}

**type Query {
 getAuthor(authorName: String): Author
 getBook(bookName: String): Book
}**
```

The operations are linked to the query, which itself is linked to the schema. Adding a schema root will
define the special object type (`Query` in this case) as one of your entry points. This can be
done using the `schema` keyword:

```
**schema {
 query: Query
}**

type Author {
  authorName: String
  Books: [Book]
}

type Book {
  bookName: String
  Authors: [Author]
}

type Query {
  getAuthor(authorName: String): Author
  getBook(bookName: String): Book
}
```

Looking at the final two methods, `addAuthor` and `addBook` are adding data to your
database, so they will be defined in a `Mutation` special object type. However, from the [Types](graphql-types.md#input-components "graphql-types.md#input-components")
page, we also know that inputs directly referencing Objects aren't allowed because they're strictly output
types. In this case, we can't use `Author` or `Book`, so we need to make an input type
with the same fields. In this example, we added `AuthorInput` and `BookInput`, both of
which accept the same fields of their respective types. Then, we create our mutation using the inputs as our
parameters:

```
schema {
  query: Query
  **mutation: Mutation**
}

type Author {
  authorName: String
  Books: [Book]
}

**input AuthorInput {
 authorName: String
 Books: [BookInput]
}**

type Book {
  bookName: String
  Authors: [Author]
}

**input BookInput {
 bookName: String
 Authors: [AuthorInput]
}**

type Query {
  getAuthor(authorName: String): Author
  getBook(bookName: String): Book
}

**type Mutation {
 addAuthor(input: [BookInput]): Author
 addBook(input: [AuthorInput]): Book
}**
```

Let's review what we just did:

1. We created a schema with the `Book` and `Author` types to represent our
   entities.
2. We added the fields containing the characteristics of our entities.
3. We added a query to retrieve this information from the database.
4. We added a mutation to manipulate data in the database.
5. We added input types to replace our object parameters in the mutation to comply with GraphQL's
   rules.
6. We added the query and mutation to our root schema so that the GraphQL implementation understands
   the root type location.

As you can see, the process of creating a schema takes a lot of concepts from data modeling (especially
database modeling) in general. You can think of the schema as fitting the shape of the data from the source.
It also serves as the model that the resolver will implement. In the following, sections, you'll learn how
to make a schema using various AWS-backed tools and services.

###### Note

The examples in the following sections are not meant to run in a real application. They are only there
to showcase the commands so you can build your own applications.

## Creating schemas

Your schema will be in a file called `schema.graphql`. AWS AppSync allows users to create new
schemas for their GraphQL APIs using various methods. In this example, we'll be creating a blank API along
with a blank schema.

Console

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **Dashboard**, choose **Create API**.
   2. Under **API options**, choose **GraphQL APIs**, **Design from
      scratch**, then **Next**.
      1. For **API name**, change the prepopulated name to
         what your application needs.
      2. For **contact details**, you can enter a
         point of contact to identify a manager for the API. This is an optional
         field.
      3. Under **Private API configuration**, you
         can enable private API features. A private API can only be accessed from
         a configured VPC endpoint (VPCE). For more information, see [Private
         APIs](using-private-apis.md "using-private-apis.md").

      We don't recommend enabling this feature for this example. Choose
      **Next** after reviewing your
      inputs.

   3. Under **Create a GraphQL type**, you can choose
      to create a DynamoDB table to use as a data source or skip this and do it
      later.

   For this example, choose **Create GraphQL resources
   later**. We will be creating a resource in a separate
   section. 4. Review your inputs, then choose **Create
   API**.

2. You will be in the dashboard of your specific API. You can tell because the API's name
   will be at the top of the dashboard. If this isn't the case, you can select **APIs** in the **Sidebar**, then
   choose your API in the **APIs dashboard**.
   1. In the **Sidebar** underneath your API's name,
      choose **Schema**.

3. In the **Schema editor**, you can configure your
   `schema.graphql` file. It may be empty or filled with types generated
   from a model. On the right, you have the **Resolvers**
   section for attaching resolvers to your schema fields. We won't be looking at resolvers
   in this section.

CLI

###### Note

When using the CLI, make sure you have the correct permissions to access and create
resources in the service. You may want to set [least-privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") policies for non-admin users who need to access the service.
For more information about AWS AppSync policies, see [Identity and access management for
AWS AppSync](security-iam.md "security-iam.md").

Additionally, we recommend reading the console version first if you haven't done so
already.

1. If you haven't already done so, [install](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") the AWS
   CLI, then add your [configuration](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md").
2. Create a GraphQL API object by running the [`create-graphql-api`](../../../cli/latest/reference/appsync/create-graphql-api.md "../../../cli/latest/reference/appsync/create-graphql-api.md") command.

You'll need to type in two parameters for this particular command:

    1. The `name` of your API.
    2. The `authentication-type`, or the type of credentials used to
     access the API (IAM, OIDC, etc.).

###### Note

Other parameters such as `Region` must be configured but will usually
default to your CLI configuration values.

An example command may look like this:

```
aws appsync create-graphql-api --name testAPI123 --authentication-type API_KEY
```

An output will be returned in the CLI. Here's an example:

```
{
    "graphqlApi": {
        "xrayEnabled": false,
        "name": "testAPI123",
        "authenticationType": "API_KEY",
        "tags": {},
        "apiId": "abcdefghijklmnopqrstuvwxyz",
        "uris": {
            "GRAPHQL": "https://zyxwvutsrqponmlkjihgfedcba.appsync-api.us-west-2.amazonaws.com/graphql",
            "REALTIME": "wss://zyxwvutsrqponmlkjihgfedcba.appsync-realtime-api.us-west-2.amazonaws.com/graphql"
        },
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz"
    }
}
```

3. ###### Note

This is an optional command that takes an existing schema and uploads it to the
AWS AppSync service using a base-64 blob. We will not be using this command for the sake
of this example.

Run the [`start-schema-creation`](../../../cli/latest/reference/appsync/start-schema-creation.md "../../../cli/latest/reference/appsync/start-schema-creation.md") command.

You'll need to type in two parameters for this particular command:

    1. Your `api-id` from the previous step.
    2. The schema `definition` is a base-64 encoded binary blob.

An example command may look like this:

```
 aws appsync start-schema-creation --api-id abcdefghijklmnopqrstuvwxyz --definition "aa1111aa-123b-2bb2-c321-12hgg76cc33v"
```

An output will be returned:

```
{
    "status": "PROCESSING"
}
```

This command will not return the final output after processing. You must use a
separate command, [`get-schema-creation-status`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-schema-creation-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-schema-creation-status.html"), to see the result. Note that
these two commands are asynchronous, so you can check the output status even while the
schema is still being created.

CDK

###### Tip

Before you use the CDK, we recommend reviewing the CDK's [official documentation](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
along with AWS AppSync's [CDK reference](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md").

The steps listed below will only show a general example of the snippet used to add a
particular resource. This is **not** meant to be a working
solution in your production code. We also assume you already have a working app.

1. The starting point for the CDK is a bit different. Ideally, your
   `schema.graphql` file should already be created. You just need to create
   a new file with the `.graphql` file extension. This can be an empty
   file.
2. In general, you may have to add the import directive to the service you're using. For
   example, it may follow the forms:

```
import * as `x` from '`x`'; # import wildcard as the 'x' keyword from 'x-service'
import {`a`, `b`, ...} from '`c`'; # import {specific constructs} from 'c-service'
```

To add a GraphQL API, your stack file needs to import the AWS AppSync service:

```
import * as appsync from 'aws-cdk-lib/aws-appsync';
```

###### Note

This means we're importing the entire service under the `appsync`
keyword. To use this in your app, your AWS AppSync constructs will use the format
`appsync.construct_name`. For instance, if we wanted to make a
GraphQL API, we would say `new appsync.GraphqlApi(args_go_here)`. The
following step depicts this. 3. The most basic GraphQL API will include a `name` for the API and the
`schema` path.

```
const `add_api` = new appsync.GraphqlApi(this, '`API_ID`', {
  name: '`name_of_API_in_console`',
  schema: appsync.SchemaFile.fromAsset(path.join(__dirname, '`schema_name.graphql`')),
});
```

###### Note

Let's review what this snippet does. Inside the scope of `api`, we're
creating a new GraphQL API by calling `appsync.GraphqlApi(scope: Construct, id:
 string, props: GraphqlApiProps)`. The scope is `this`, which
refers to the current object. The id is `API_ID`, which
will be your GraphQL API's resource name in CloudFormation when it's created. The
`GraphqlApiProps` contains the `name` of your GraphQL API
and the `schema`. The `schema` will generate a schema
(`SchemaFile.fromAsset`) by searching the absolute path
(`__dirname`) for the `.graphql` file
(`schema_name.graphql`). In a real scenario, your
schema file will probably be inside the CDK app.

To use changes made to your GraphQL API, you'll have to redeploy the app.

## Adding types to schemas

Now that you've added your schema, you can start adding both your input and output types. Note that the
types here shouldn't be used in real code; they're just examples to help you understand the process.

First, we'll create an object type. In real code, you don't have to start with these types. You can make
any type you want at any time so long as you follow GraphQL's rules and syntax.

###### Note

These next few sections will be using the **schema editor**, so keep this
open.

Console

- You can create an object type using the `type` keyword along with the
  type's name:

```
type `Type_Name_Goes_Here` {}
```

Inside the type's scope, you can add fields that represent the object's
characteristics:

```
type `Type_Name_Goes_Here` {
  # Add fields here
}
```

Here's an example:

```
type `Obj_Type_1` {
 `id: ID!
 title: String
 date: AWSDateTime`
}
```

###### Note

In this step, we added a generic object type with a required `id` field
stored as `ID`, a `title` field stored as a
`String`, and a `date` field stored as an
`AWSDateTime`. To see a list of types and fields and what they do,
see [Schemas](schema-components.md "schema-components.md"). To see a
list of scalars and what they do, see the [Type reference](type-reference.md "type-reference.md").

CLI

###### Note

We recommend reading the console version first if you haven't done so already.

- You can create an object type by running the [`create-type`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html") command.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `definition`, or the content of your type. In the console
     example, this was:



    ```
    type `Obj_Type_1` {
     `id: ID!
     title: String
     date: AWSDateTime`
    }
    ```
    3. The `format` of your input. In this example, we're using
     `SDL`.

An example command may look like this:

```
aws appsync create-type --api-id abcdefghijklmnopqrstuvwxyz --definition "type Obj_Type_1{id: ID! title: String date: AWSDateTime}" --format SDL
```

An output will be returned in the CLI. Here's an example:

```
{
    "type": {
        "definition": "type Obj_Type_1{id: ID! title: String date: AWSDateTime}",
        "name": "Obj_Type_1",
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/Obj_Type_1",
        "format": "SDL"
    }
}
```

###### Note

In this step, we added a generic object type with a required `id` field
stored as `ID`, a `title` field stored as a
`String`, and a `date` field stored as an
`AWSDateTime`. To see a list of types and fields and what they do,
see [Schemas](schema-components.md "schema-components.md"). To see a
list of scalars and what they do, see [Type reference](type-reference.md "type-reference.md").

On a further note, you may have realized that entering the definition directly
works for smaller types but is infeasible for adding larger or multiple types. You
can opt to add everything in a `.graphql` file and then [pass it as the input](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md").

CDK

###### Tip

Before you use the CDK, we recommend reviewing the CDK's [official documentation](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
along with AWS AppSync's [CDK reference](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md").

The steps listed below will only show a general example of the snippet used to add a
particular resource. This is **not** meant to be a working
solution in your production code. We also assume you already have a working app.

To add a type, you need to add it to your `.graphql` file. For instance, the
console example was:

```
type `Obj_Type_1` {
 `id: ID!
 title: String
 date: AWSDateTime`
}
```

You can add your types directly to the schema like any other file.

###### Note

To use changes made to your GraphQL API, you'll have to redeploy the app.

The [object type](https://graphql.org/learn/schema/#object-types-and-fields "https://graphql.org/learn/schema/#object-types-and-fields") has fields
that are [scalar types](https://graphql.org/learn/schema/#scalar-types "https://graphql.org/learn/schema/#scalar-types") such as strings
and integers. AWS AppSync also allows you to use enhanced scalar types like `AWSDateTime` in
addition to the base GraphQL scalars. Also, any field that ends in an exclamation point is required.

The `ID` scalar type in particular is a unique identifier that can be either
`String` or `Int`. You can control these in your resolver code for automatic
assignment.

There are similarities between special object types like `Query` and "regular" object types
like the example above in that they both use the `type` keyword and are considered objects.
However, for the special object types (`Query`, `Mutation`, and
`Subscription`), their behavior is vastly different because they are exposed as the entry
points for your API. They're also more about shaping operations rather than data. For more information, see
[The query and mutation
types](https://graphql.org/learn/schema/#the-query-and-mutation-types "https://graphql.org/learn/schema/#the-query-and-mutation-types").

On the topic of special object types, the next step could be to add one or more of them to perform
operations on the shaped data. In a real scenario, every GraphQL schema must at least have a root query type
for requesting data. You can think of the query as one of the entry points (or endpoints) for your GraphQL
server. Let's add a query as an example.

Console

- To create a query, you can simply add it to the schema file like any other type. A
  query would require a `Query` type and an entry in the root like this:

```
schema {
  query: `Name_of_Query`
}

type `Name_of_Query` {
  # Add field operation here
}
```

Note that `Name_of_Query` in a production environment will
simply be called `Query` in most cases. We recommend keeping it at this
value. Inside the query type, you can add fields. Each field will perform an operation
in the request. As a result, most, if not all, of these fields will be attached to a
resolver. However, we're not concerned with that in this section. Regarding the format
of the field operation, it might look like this:

```
`Name_of_Query(params): Return_Type` # version with params
`Name_of_Query: Return_Type` # version without params
```

Here's an example:

```
schema {
  query: Query
}

type Query {
  `getObj: [Obj_Type_1]`
}

type Obj_Type_1 {
  id: ID!
  title: String
  date: AWSDateTime
}
```

###### Note

In this step, we added a `Query` type and defined it in our
`schema` root. Our `Query` type defined a
`getObj` field that returns a list of `Obj_Type_1`
objects. Note that `Obj_Type_1` is the object of the previous step. In
production code, your field operations will normally be working with data shaped by
objects like `Obj_Type_1`. In addition, fields like `getObj`
will normally have a resolver to perform the business logic. That will be covered in
a different section.

As an additional note, AWS AppSync automatically adds a schema root during
exports, so technically you don't have to add it directly to the schema. Our service
will automatically process duplicate schemas. We're adding it here as a best
practice.

CLI

###### Note

We recommend reading the console version first if you haven't done so already.

1. Create a `schema` root with a `query` definition by running the
   [`create-type`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html") command.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `definition`, or the content of your type. In the console
     example, this was:



    ```
    schema {
      query: Query
    }
    ```
    3. The `format` of your input. In this example, we're using
     `SDL`.

An example command may look like this:

```
aws appsync create-type --api-id abcdefghijklmnopqrstuvwxyz --definition "schema {query: Query}" --format SDL
```

An output will be returned in the CLI. Here's an example:

```
{
    "type": {
        "definition": "schema {query: Query}",
        "name": "schema",
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/schema",
        "format": "SDL"
    }
}
```

###### Note

Note that if you didn't input something correctly in the `create-type`
command, you can update your schema root (or any type in the schema) by running the
[`update-type`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-type.html") command. In this example, we'll be
temporarily changing the schema root to contain a `subscription`
definition.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `type-name` of your type. In the console example, this was
     `schema`.
    3. The `definition`, or the content of your type. In the console
     example, this was:



    ```
    schema {
      query: Query
    }
    ```

    The schema after adding a `subscription` will look like
     this:



    ```
    schema {
      query: Query
      **subscription: Subscription**
    }
    ```
    4. The `format` of your input. In this example, we're using
     `SDL`.An example command may look like this:

```
aws appsync update-type --api-id abcdefghijklmnopqrstuvwxyz --type-name schema --definition "schema {query: Query subscription: Subscription}" --format SDL
```

An output will be returned in the CLI. Here's an example:

```
{
    "type": {
        "definition": "schema {query: Query subscription: Subscription}",
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/schema",
        "format": "SDL"
    }
}
```

Adding preformatted files will still work in this example. 2. Create a `Query` type by running the [`create-type`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html") command.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `definition`, or the content of your type. In the console
     example, this was:



    ```
    type Query {
      getObj: [Obj_Type_1]
    }
    ```
    3. The `format` of your input. In this example, we're using
     `SDL`.

An example command may look like this:

```
aws appsync create-type --api-id abcdefghijklmnopqrstuvwxyz --definition "type Query {getObj: [Obj_Type_1]}" --format SDL
```

An output will be returned in the CLI. Here's an example:

```
{
    "type": {
        "definition": "Query {getObj: [Obj_Type_1]}",
        "name": "Query",
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/Query",
        "format": "SDL"
    }
}
```

###### Note

In this step, we added a `Query` type and defined it in your
`schema` root. Our `Query` type defined a
`getObj` field that returned a list of `Obj_Type_1`
objects.

In the `schema` root code `query: Query`, the
`query:` part indicates that a query was defined in your schema,
while the `Query` part indicates the actual special object name.

CDK

###### Tip

Before you use the CDK, we recommend reviewing the CDK's [official documentation](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
along with AWS AppSync's [CDK reference](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md").

The steps listed below will only show a general example of the snippet used to add a
particular resource. This is **not** meant to be a working
solution in your production code. We also assume you already have a working app.

You'll need to add your query and the schema root to the `.graphql` file. Our
example looked like the example below, but you'll want to replace it with your actual schema
code:

```
schema {
  query: Query
}

type Query {
  getObj: [Obj_Type_1]
}

type Obj_Type_1 {
  id: ID!
  title: String
  date: AWSDateTime
}
```

You can add your types directly to the schema like any other file.

###### Note

Updating the schema root is optional. We added it to this example as a best
practice.

To use changes made to your GraphQL API, you'll have to redeploy the app.

You've now seen an example of creating both objects and special objects (queries). You've also seen how
these can be interconnected to describe data and operations. You can have schemas with only the data
description and one or more queries. However, we'd like to add another operation to add data to the data
source. We'll add another special object type called `Mutation` that modifies data.

Console

- A mutation will be called `Mutation`. Like `Query`, the field
  operations inside `Mutation` will describe an operation and will be attached
  to a resolver. Also, note that we need to define it in the `schema` root
  because it's a special object type. Here's an example of a mutation:

```
schema {
  `mutation: Name_of_Mutation`
}

type `Name_of_Mutation` {
  # Add field operation here
}
```

A typical mutation will be listed in the root like a query. The mutation is defined
using the `type` keyword along with the name.
`Name_of_Mutation` will usually be called
`Mutation`, so we recommend keeping it that way. Each field will also
perform an operation. Regarding the format of the field operation, it might look like
this:

```
Name_of_Mutation(params): Return_Type # version with params
Name_of_Mutation: Return_Type # version without params
```

Here's an example:

```
schema {
  query: Query
  `mutation: Mutation`
}

type Obj_Type_1 {
  id: ID!
  title: String
  date: AWSDateTime
}

type Query {
  getObj: [Obj_Type_1]
}

type Mutation {
  `addObj(id: ID!, title: String, date: AWSDateTime): Obj_Type_1`
}
```

###### Note

In this step, we added a `Mutation` type with an `addObj`
field. Let's summarize what this field does:

```
addObj(id: ID!, title: String, date: AWSDateTime): Obj_Type_1
```

`addObj` is using the `Obj_Type_1` object to perform an
operation. This is apparent due to the fields, but the syntax proves this in the
`: Obj_Type_1` return type. Inside `addObj`, it's
accepting the `id`, `title`, and `date` fields from
the `Obj_Type_1` object as parameters. As you may see, it looks a lot
like a method declaration. However, we haven't described the behavior of our method
yet. As stated earlier, the schema is only there to define what the data and
operations will be and not how they operate. Implementing the actual business logic
will come later when we create our first resolvers.

Once you're done with your schema, there's an option to export it as a
`schema.graphql` file. In the **Schema
editor**, you can choose **Export schema**
to download the file in a supported format.

As an additional note, AWS AppSync automatically adds a schema root during
exports, so technically you don't have to add it directly to the schema. Our service
will automatically process duplicate schemas. We're adding it here as a best
practice.

CLI

###### Note

We recommend reading the console version first if you haven't done so already.

1. Update your root schema by running the [`update-type`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-type.html") command.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `type-name` of your type. In the console example, this was
     `schema`.
    3. The `definition`, or the content of your type. In the console
     example, this was:



    ```
    schema {
      query: Query
      mutation: Mutation
    }
    ```
    4. The `format` of your input. In this example, we're using
     `SDL`.

An example command may look like this:

```
aws appsync update-type --api-id abcdefghijklmnopqrstuvwxyz --type-name schema --definition "schema {query: Query mutation: Mutation}" --format SDL
```

An output will be returned in the CLI. Here's an example:

```
{
    "type": {
        "definition": "schema {query: Query mutation: Mutation}",
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/schema",
        "format": "SDL"
    }
}
```

2. Create a `Mutation` type by running the [`create-type`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html") command.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `definition`, or the content of your type. In the console
     example, this was



    ```
    type Mutation {
      addObj(id: ID!, title: String, date: AWSDateTime): Obj_Type_1
    }
    ```
    3. The `format` of your input. In this example, we're using
     `SDL`.

An example command may look like this:

```
aws appsync create-type --api-id abcdefghijklmnopqrstuvwxyz --definition "type Mutation {addObj(id: ID! title: String date: AWSDateTime): Obj_Type_1}" --format SDL
```

An output will be returned in the CLI. Here's an example:

```
{
    "type": {
        "definition": "type Mutation {addObj(id: ID! title: String date: AWSDateTime): Obj_Type_1}",
        "name": "Mutation",
        "arn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/Mutation",
        "format": "SDL"
    }
}
```

CDK

###### Tip

Before you use the CDK, we recommend reviewing the CDK's [official documentation](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
along with AWS AppSync's [CDK reference](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md").

The steps listed below will only show a general example of the snippet used to add a
particular resource. This is **not** meant to be a working
solution in your production code. We also assume you already have a working app.

You'll need to add your query and the schema root to the `.graphql` file. Our
example looked like the example below, but you'll want to replace it with your actual schema
code:

```
schema {
  query: Query
  mutation: Mutation
}

type Obj_Type_1 {
  id: ID!
  title: String
  date: AWSDateTime
}

type Query {
  getObj: [Obj_Type_1]
}

type Mutation {
  addObj(id: ID!, title: String, date: AWSDateTime): Obj_Type_1
}
```

###### Note

Updating the schema root is optional. We added it to this example as a best
practice.

To use changes made to your GraphQL API, you'll have to redeploy the app.

## Optional considerations - Using enums as statuses

At this point, you know how to make a basic schema. However, there are many things you could add to
increase the schema's functionality. One common thing found in applications is the use of enums as statuses.
You can use an enum to force a specific value from a set of values to be chosen when called. This is good
for things that you know will not change drastically over long periods of time. Hypothetically speaking, we
could add an enum that returns the status code or String in the response.

As an example, let's assume we're making a social media app that's storing a user's post data in the
backend. Our schema contains a `Post` type that represents an individual post's data:

```
type Post {
  id: ID!
  title: String
  date: AWSDateTime
  poststatus: PostStatus
}
```

Our `Post` will contain a unique `id`, post `title`, `date` of
posting, and an enum called `PostStatus` that represents the post's state as it's processed by
the app. For our operations, we'll have a query that returns all post data:

```
type Query {
  getPosts: [Post]
}
```

We'll also have a mutation that adds posts to the data source:

```
type Mutation {
  addPost(id: ID!, title: String, date: AWSDateTime, poststatus: PostStatus): Post
}
```

Looking at our schema, the `PostStatus` enum could have several statuses. We might want the
three basic states called `success` (post successfully processed), `pending` (post
being processed), and `error` (post unable to be processed). To add the enum, we could do
this:

```
enum PostStatus {
  success
  pending
  error
}
```

The full schema might look like this:

```
schema {
  query: Query
  mutation: Mutation
}

type Post {
  id: ID!
  title: String
  date: AWSDateTime
  poststatus: PostStatus
}

type Mutation {
  addPost(id: ID!, title: String, date: AWSDateTime, poststatus: PostStatus): Post
}

type Query {
  getPosts: [Post]
}

enum PostStatus {
  success
  pending
  error
}
```

If a user adds a `Post` in the application, the `addPost` operation will be called
to process that data. As the resolver attached to `addPost` processes the data, it will
continually update the `poststatus` with the status of the operation. When queried, the
`Post` will contain the final status of the data. Keep in mind, we're only describing how we
want the data to work in the schema. We're assuming a lot about the implementation of our resolver(s), which
will implement the actual business logic for handling the data to fulfill the request.

## Optional considerations - Subscriptions

Subscriptions in AWS AppSync are invoked as a response to a mutation. You configure this with a
`Subscription` type and `@aws_subscribe()` directive in the schema to denote which
mutations invoke one or more subscriptions. For more information about configuring subscriptions, see [Real-time
data](aws-appsync-real-time-data.md "aws-appsync-real-time-data.md").

## Optional considerations - Relations and

pagination

Suppose you had a million `Posts` stored in a DynamoDB table, and you wanted to return some of
that data. However, the example query given above only returns all posts. You wouldn’t want to fetch all of
these every time you made a request. Instead, you would want to [paginate](https://graphql.org/learn/pagination/ "https://graphql.org/learn/pagination/") through them. Make the following changes to
your schema:

- In the `getPosts` field, add two input arguments: `nextToken` (iterator) and
  `limit` (iteration limit).
- Add a new `PostIterator` type containing `Posts` (retrieves the list of
  `Post` objects) and `nextToken` (iterator) fields.
- Change `getPosts` so that it returns `PostIterator` and not a list of
  `Post` objects.

```
schema {
  query: Query
  mutation: Mutation
}

type Post {
  id: ID!
  title: String
  date: AWSDateTime
  poststatus: PostStatus
}

type Mutation {
  addPost(id: ID!, title: String, date: AWSDateTime, poststatus: PostStatus): Post
}

type Query {
  getPosts(limit: Int, nextToken: String): PostIterator
}

enum PostStatus {
  success
  pending
  error
}

type PostIterator {
  posts: [Post]
  nextToken: String
}
```

The `PostIterator` type allows you to return a portion of the list of `Post` objects
and a `nextToken` for getting the next portion. Inside `PostIterator`, there is a list
of `Post` items (`[Post]`) that is returned with a pagination token
(`nextToken`). In AWS AppSync, this would be connected to Amazon DynamoDB through a resolver and
automatically generated as an encrypted token. This converts the value of the `limit` argument to
the `maxResults` parameter and the `nextToken` argument to the
`exclusiveStartKey` parameter. For examples and the built-in template samples in the
AWS AppSync console, see [Resolver reference
(JavaScript)](resolver-reference-js-version.md "resolver-reference-js-version.md").
