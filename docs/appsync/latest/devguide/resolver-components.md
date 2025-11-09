# Resolvers

From the previous sections, you learned about the components of the schema and data source. Now, we need
to address how the schema and data sources interact. It all begins with the resolver.

A resolver is a unit of code that handles how that field's data will be resolved when a request is made
to the service. Resolvers are attached to specific fields within your types in your schema. They are most
commonly used to implement the state-changing operations for your query, mutation, and subscription field
operations. The resolver will process a client's request, then return the result, which can be a group of
output types like objects or scalars:

![GraphQL schema with resolvers connecting to various AWS data sources for a single endpoint.](images/aws-flow-infographic.png)

## Resolver runtime

In AWS AppSync, you must first specify a runtime for your resolver. A resolver runtime indicates the
environment in which a resolver is executed. It also dictates the language your resolvers will be written
in. AWS AppSync currently supports APPSYNC_JS for JavaScript and Velocity Template Language (VTL). See [JavaScript runtime
features for resolvers and functions](resolver-util-reference-js.md "resolver-util-reference-js.md") for JavaScript or [Resolver mapping template utility
reference](resolver-util-reference.md "resolver-util-reference.md") for VTL.

## Resolver structure

Code-wise, resolvers can be structured in a couple of ways. There are **unit** and **pipeline** resolvers.

### Unit resolvers

A unit resolver is composed of code that defines a single request and response handler that are
executed against a data source. The request handler takes a context object as an argument and returns
the request payload used to call your data source. The response handler receives a payload back from
the data source with the result of the executed request. The response handler transforms the payload
into a GraphQL response to resolve the GraphQL field.

![GraphQL request flow showing request and response handlers interacting with a data source.](images/unit-resolver-js.png)

### Pipeline resolvers

When implementing pipeline resolvers, there is a general structure they follow:

- **Before step**: When a request is made by the client, the
  resolvers for the schema fields being used (typically your queries, mutations, subscriptions)
  are passed the request data. The resolver will begin processing the request data with a before
  step handler, which allows some preprocessing operations to be performed before the data moves
  through the resolver.
- **Function(s)**: After the before step runs, the request is
  passed to the functions list. The first function in the list will execute against the data
  source. A function is a subset of your resolver's code containing its own request and response
  handler. A request hander will take the request data and perform operations against the data
  source. The response handler will process the data source's response before passing it back to
  the list. If there is more than one function, the request data will be sent to the next function
  in the list to be executed. Functions in the list will be executed serially in the order defined
  by the developer. Once all functions have been executed, the final result is passed to the after
  step.
- **After step**: The after step is a handler function that allows
  you to perform some final operations on the final function's response before passing it to the
  GraphQL response.

![GraphQL request flow diagram showing interactions between request, data sources, and response components.](/images/appsync/latest/devguide/images/appsync-js-resolver-logic.png)

## Resolver handler structure

Handlers are typically functions called `Request` and `Response`:

```
export function request(ctx) {
    // Code goes here
}

export function response(ctx) {
    // Code goes here
}
```

In a unit resolver, there will only be one set of these functions. In a pipeline resolver, there will
be a set of these for the before and after step and an additional set per function. To visualize how this
could look, let's review a simple `Query` type:

```
type Query {
	helloWorld: String!
}
```

This is a simple query with one field called `helloWorld` of type `String`.
Let's assume we always want this field to return the string "Hello World". To implement this behavior, we
need to add the resolver to this field. In a unit resolver, we could add something like this:

```
export function request(ctx) {
    return {}
}

export function response(ctx) {
    return "Hello World"
}
```

The `request` can just be left blank because we're not requesting or processing data. We
can also assume our data source is `None`, indicating this code doesn't need to perform any
invocations. The response simply returns "Hello World". To test this resolver, we need to make a request
using the query type:

```
query helloWorldTest {
  helloWorld
}
```

This is a query called `helloWorldTest` that returns the `helloWorld` field.
When executed, the `helloWorld` field resolver also executes and returns the response:

```
{
  "data": {
    "helloWorld": "Hello World"
  }
}
```

Returning constants like this is the simplest thing you could do. In reality, you'll be returning
inputs, lists, and more. Here's a more complicated example:

```
type Book {
  id: ID!
  title: String
}

type Query {
  getBooks: [Book]
}
```

Here we're returning a list of `Books`. Let's assume we're using a DynamoDB table to store
book data. Our handlers may look like this:

```
/**
 * Performs a scan on the dynamodb data source
 */
export function request(ctx) {
  return { operation: 'Scan' };
}

/**
 * return a list of scanned post items
 */
export function response(ctx) {
  return ctx.result.items;
}
```

Our request used a built-in scan operation to search for all entries in the table, stored the findings
in the context, then passed it to the response. The response took the result items and returned them in
the response:

```
{
  "data": {
    "getBooks": {
      "items": [
        {
          "id": "abcdefgh-1234-1234-1234-abcdefghijkl",
          "title": "book1"
        },
        {
          "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
          "title": "book2"
        },

        ...

      ]
    }
  }
}
```

## Resolver context

In a resolver, each step in the chain of handlers must be aware of the state of the data from the
previous steps. The result from one handler can be stored and passed to another as an argument. GraphQL
defines four basic resolver arguments:

| Resolver base arguments       | Description                                                                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `obj`, `root`, `parent`, etc. | The result of the parent.                                                                                                                             |
| `args`                        | The arguments provided to the field in the GraphQL query.                                                                                             |
| `context`                     | A value which is provided to every resolver and holds important contextual information<br>like the currently logged in user, or access to a database. |
| `info`                        | A value which holds field-specific information relevant to the current query as well as<br>the schema details.                                        |

In AWS AppSync, the `context` (ctx)
argument can hold all of the data mentioned above. It's an object that's created per request and contains
data like authorization credentials, result data, errors, request metadata, etc. The context is an easy
way for programmers to manipulate data coming from other parts of the request. Take this snippet
again:

```
/**
 * Performs a scan on the dynamodb data source
 */
export function request(ctx) {
  return { operation: 'Scan' };
}

/**
 * return a list of scanned post items
 */
export function response(ctx) {
  return ctx.result.items;
}
```

The request is given the context (ctx) as the argument; this is the state of the request. It performs
a scan for all items in a table, then stores the result back in the context in `result`. The
context is then passed to the response argument, which accesses the `result` and returns its
contents.

## Requests and Parsing

When you make a query to your GraphQL service, it must run through a parsing and validation process
before being executed. Your request will be parsed and translated into an abstract syntax tree. The
content of the tree is validated by running through several validation algorithms against your schema.
After the validation step, the nodes of the tree are traversed and processed. Resolvers are invoked, the
results are stored in the context, and the response is returned. For example, take this query:

```
query {
  Person {  //object type
    name  //scalar
    age   //scalar
  }
}
```

We're returning `Person` with a `name` and `age` fields. When running
this query, the tree will look something like this:

![Hierarchical diagram showing query, Person, name, and age nodes connected by arrows.](images/ast-1.png)

From the tree, it appears that this request will search the root for the `Query` in the
schema. Inside of the query, the `Person` field will be resolved. From previous examples, we
know that this could be an input from the user, a list of values, etc. `Person` is most likely
tied to an object type holding the fields we need (`name` and `age`). Once these
two child fields are found, they are resolved in the order given (`name` followed by
`age`). Once the tree is completely resolved, the request is completed and will be sent
back to the client.
