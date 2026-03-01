# Using subscriptions for real-time data applications in AWS AppSync

###### Important

As of Mar 13, 2025, you can build a real-time PubSub API powered by WebSockets using
AWS AppSync Events. For more information, see [Publish events via WebSocket](../eventapi/publish-websocket.md "../eventapi/publish-websocket.md") in the _AWS AppSync Events
Developer Guide_.

AWS AppSync
allows you to utilize subscriptions to implement live application updates, push
notifications, etc. When clients invoke the GraphQL subscription operations, a secure
WebSocket connection is automatically established and maintained by AWS AppSync.
Applications can then distribute data in real-time from a data source to subscribers while
AWS AppSync continually manages the application's connection and scaling requirements. The
following sections will show you how subscriptions in AWS AppSync
work.

## GraphQL schema subscription directives

Subscriptions in AWS AppSync are invoked as a response to a mutation. This means
that you can make any data source in AWS AppSync real time by specifying a GraphQL schema
directive on a mutation.

The AWS Amplify client libraries automatically handle subscription connection
management. The libraries use pure WebSockets as the network protocol between the client
and service.

###### Note

To control authorization at connection time to a subscription, you can use
AWS Identity and Access Management (IAM), AWS Lambda, Amazon Cognito identity pools, or Amazon Cognito user pools for
field-level authorization. For fine-grained access controls on subscriptions, you
can attach resolvers to your subscription fields and perform logic using the
identity of the caller and AWS AppSync data sources. For more information, see
[Configuring authorization and authentication to secure your GraphQL APIs](security-authz.md "security-authz.md").

Subscriptions are triggered from mutations and the mutation selection set is sent to
subscribers.

The following example shows how to work with GraphQL subscriptions. It doesn't specify
a data source because the data source could be Lambda, Amazon DynamoDB, or Amazon OpenSearch Service.

To get started with subscriptions, you must add a subscription entry point to your
schema as follows:

```
schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
}
```

Suppose you have a blog post site, and you want to subscribe to new blogs and changes
to existing blogs. To do this, add the following `Subscription` definition to
your schema:

```
type Subscription {
    addedPost: Post
    updatedPost: Post
    deletedPost: Post
}
```

Suppose further that you have the following mutations:

```
type Mutation {
    addPost(id: ID! author: String! title: String content: String url: String): Post!
    updatePost(id: ID! author: String! title: String content: String url: String ups: Int! downs: Int! expectedVersion: Int!): Post!
    deletePost(id: ID!): Post!
}
```

You can make these fields real time by adding an `@aws_subscribe(mutations:
 ["mutation_field_1", "mutation_field_2"])` directive for each of the
subscriptions you want to receive notifications for, as follows:

```
type Subscription {
    addedPost: Post
    @aws_subscribe(mutations: ["addPost"])
    updatedPost: Post
    @aws_subscribe(mutations: ["updatePost"])
    deletedPost: Post
    @aws_subscribe(mutations: ["deletePost"])
}
```

Because the `@aws_subscribe(mutations: ["",..,""])` takes an array of
mutation inputs, you can specify multiple mutations, which initiate a subscription. If
you're subscribing from a client, your GraphQL query might look like the
following:

```
subscription NewPostSub {
    addedPost {
        __typename
        version
        title
        content
        author
        url
    }
}
```

This subscription query is needed for client connections and tooling.

With the pure WebSockets client, selection set filtering is done per client, as each
client can define its own selection set. In this case, the subscription selection set
must be a subset of the mutation selection set. For example, a subscription
`addedPost{author title}` linked to the mutation `addPost(...){id
 author title url version}` receives only the author and title of the post. It
does not receive the other fields. However, if the mutation lacked the author in its
selection set, the subscriber would get a `null` value for the author field
(or an error in case the author field is defined as required/not-null in the
schema).

The subscription selection set is essential when using pure WebSockets. If a field is
not explicitly defined in the subscription, then AWS AppSync doesn't return the field.

In the previous example, the subscriptions didn't have arguments. Suppose that your
schema looks like the following:

```
type Subscription {
    updatedPost(id:ID! author:String): Post
    @aws_subscribe(mutations: ["updatePost"])
}
```

In this case, your client defines a subscription as follows:

```
subscription UpdatedPostSub {
    updatedPost(id:"XYZ", author:"ABC") {
        title
        content
    }
}
```

The return type of a `subscription` field in your schema must match the
return type of the corresponding mutation field. In the previous example, this was shown
as both `addPost` and `addedPost` returned as a type of
`Post`.

To set up subscriptions on the client, see [Building a client application using Amplify client](building-a-client-app.md "building-a-client-app.md").

## Using subscription arguments

An important part of using GraphQL subscriptions is understanding when and how to use
arguments. You can make subtle changes to modify how and when to notify clients about
mutations that have occurred. To do this, see the sample schema from the quickstart
chapter, which creates "Todos". For this sample schema, the following
mutations are
defined:

```
type Mutation {
    createTodo(input: CreateTodoInput!): Todo
    updateTodo(input: UpdateTodoInput!): Todo
    deleteTodo(input: DeleteTodoInput!): Todo
}
```

In the default sample, clients can subscribe to updates to any `Todo` by
using the `onUpdateTodo`
`subscription` with no arguments:

```
subscription OnUpdateTodo {
  onUpdateTodo {
    description
    id
    name
    when
  }
}
```

You can filter your `subscription` by using its arguments. For example, to
only trigger a `subscription` when a `todo` with a specific
`ID` is updated, specify the `ID` value:

```
subscription OnUpdateTodo {
  onUpdateTodo(id: "`a-todo-id`") {
    description
    id
    name
    when
  }
}
```

You can also pass multiple arguments. For example, the following
`subscription` demonstrates how to get notified of any `Todo`
updates at a specific place and time:

```
subscription todosAtHome {
  onUpdateTodo(when: "tomorrow", where: "at home") {
    description
    id
    name
    when
    where
  }
}
```

Note that all of the arguments are optional. If you don't specify any arguments in
your `subscription`, you will be subscribed to all `Todo` updates
that occur in your application. However, you could update your
`subscription`'s field definition to require the `ID` argument.
This would force the response of a specific `todo` instead of all
`todo`s:

```
onUpdateTodo(
  id: ID!,
  name: String,
  when: String,
  where: String,
  description: String
): Todo
```

### Argument null value has meaning

When making a subscription query in AWS AppSync, a `null` argument
value will filter the results differently than omitting the argument
entirely.

Let's go back to the todos API sample where we could create todos. See the sample
schema from the quickstart chapter.

Let's modify our schema to include a new `owner` field, on the
`Todo` type, that describes who the owner is. The `owner`
field is not required and can only be set on `UpdateTodoInput`. See the
following simplified version of the schema:

```
type Todo {
  id: ID!
  name: String!
  when: String!
  where: String!
  description: String!
  owner: String
}

input CreateTodoInput {
  name: String!
  when: String!
  where: String!
  description: String!
}

input UpdateTodoInput {
  id: ID!
  name: String
  when: String
  where: String
  description: String
  owner: String
}

type Subscription {
    onUpdateTodo(
        id: ID,
        name: String,
        when: String,
        where: String,
        description: String
    ): Todo @aws_subscribe(mutations: ["updateTodo"])
}
```

The following subscription returns all `Todo`updates:

```
subscription MySubscription {
  onUpdateTodo {
    description
    id
    name
    when
    where
  }
}
```

If you modify the preceding subscription to add the field argument `owner:
 null`, you are now asking a different question. This subscription now
registers the client to get notified of all the `Todo` updates that have
not provided an owner.

```
subscription MySubscription {
  onUpdateTodo(owner: null) {
    description
    id
    name
    when
    where
  }
}
```

###### Note

**As of January 1, 2022, MQTT over WebSockets is no longer
available as a protocol for GraphQL subscriptions in AWS AppSync APIs. Pure
WebSockets is the only protocol supported in AWS AppSync.**

Clients based on the AWS AppSync SDK or the Amplify libraries, released after
November 2019, automatically use pure WebSockets by default. Upgrading the clients
to the latest version allows them to use AWS AppSync's pure WebSockets engine.

Pure WebSockets come with a larger payload size (240 KB), a wider variety of
client options, and improved CloudWatch metrics. For more information on using pure
WebSocket clients, see [Building a real-time WebSocket client in AWS AppSync](real-time-websocket-client.md "real-time-websocket-client.md").
