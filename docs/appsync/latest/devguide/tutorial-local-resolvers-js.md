# Using local resolvers in AWS AppSync

AWS AppSync allows you to use supported data sources (AWS Lambda, Amazon DynamoDB, or Amazon OpenSearch Service)
to perform various operations. However, in certain scenarios, a call to a supported data
source might not be necessary.

This is where the local resolver comes in handy. Instead of calling a remote data source, the local resolver
will just **forward** the result of the request handler to the response handler.
The field resolution will not leave AWS AppSync.

Local resolvers are useful in a plethora of situations. The most popular use case is to publish notifications
without triggering a data source call. To demonstrate this use case, let’s build a pub/sub application in which
users can publish and subscribe to messages. This example leverages _Subscriptions_, so if you aren’t familiar with _Subscriptions_, you can follow the [Real-Time
Data](aws-appsync-real-time-data.md "aws-appsync-real-time-data.md") tutorial.

## Creating the pub/sub app

First, create a blank GraphQL API by choosing the **Design from scratch**
option and configuring the optional details when creating your GraphQL API.

In our pub/sub application, clients can subscribe to and publish messages. Each published message includes
a name and data. Add this to the schema:

```
type Channel {
	name: String!
	data: AWSJSON!
}

type Mutation {
	publish(name: String!, data: AWSJSON!): Channel
}

type Query {
	getChannel: Channel
}

type Subscription {
	subscribe(name: String!): Channel
		@aws_subscribe(mutations: ["publish"])
}
```

Next, let’s attach a resolver to the `Mutation.publish` field. In the **Resolvers** pane next to the **Schema** pane, find the
`Mutation` type, then the `publish(...): Channel` field, then click on **Attach**.

Create a _None_ data source and name it _PageDataSource_. Attach it
to your resolver.

Add your resolver implementation using the following snippet:

```
export function request(ctx) {
  return { payload: ctx.args };
}

export function response(ctx) {
  return ctx.result;
}
```

Make sure you create the resolver and save the changes you made.

## Send and subscribe to messages

For clients to receive messages, they must first be subscribed to an inbox.

In the **Queries** pane, execute the `SubscribeToData`
subscription:

```
subscription SubscribeToData {
    subscribe(name:"channel") {
        name
        data
    }
}
```

The subscriber will receive messages whenever the `publish` mutation is invoked but only when
the message is sent to the `channel` subscription. Let’s try this in the **Queries** pane. While your subscription is still running in the console, open up another
console and run the following request in the **Queries** pane:

###### Note

We're using valid JSON strings in this example.

```
mutation PublishData {
    publish(data: "{\"msg\": \"hello world!\"}", name: "channel") {
        data
        name
    }
}
```

The result will look like this:

```
{
  "data": {
    "publish": {
      "data": "{\"msg\":\"hello world!\"}",
      "name": "channel"
    }
  }
}
```

We just demonstrated the use of local resolvers, by publishing a message and receiving it without leaving
the AWS AppSync service.
