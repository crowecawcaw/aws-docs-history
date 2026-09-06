

# Using local resolvers in AWS AppSync
<a name="tutorial-local-resolvers"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials-js.html).

AWS AppSync allows you to use supported data sources (AWS Lambda, Amazon DynamoDB, or Amazon OpenSearch Service) to perform various operations. However, in certain scenarios, a call to a supported data source might not be necessary.

This is where the local resolver comes in handy. Instead of calling a remote data source, the local resolver will just **forward** the result of the request mapping template to the response mapping template. The field resolution will not leave AWS AppSync.

Local resolvers are useful for several use cases. The most popular use case is to publish notifications without triggering a data source call. To demonstrate this use case, let’s build a paging application; where users can page each other. This example leverages *Subscriptions*, so if you aren’t familiar with *Subscriptions*, you can follow the [Real-Time Data](aws-appsync-real-time-data.md) tutorial.

## Create the Paging Application
<a name="create-the-paging-application"></a>

In our paging application, clients can subscribe to an inbox, and send pages to other clients. Each page includes a message. Here is the schema:

```
schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
}

type Subscription {
    inbox(to: String!): Page
    @aws_subscribe(mutations: ["page"])
}

type Mutation {
    page(body: String!, to: String!): Page!
}

type Page {
    from: String
    to: String!
    body: String!
    sentAt: String!
}

type Query {
    me: String
}
```

Let’s attach a resolver on the `Mutation.page` field. In the **Schema** pane, click on *Attach Resolver* next to the field definition on the right panel. Create a new data source of type *None* and name it *PageDataSource*.

For the request mapping template, enter:

```
{
  "version": "2017-02-28",
  "payload": {
    "body": $util.toJson($context.arguments.body),
    "from": $util.toJson($context.identity.username),
    "to":  $util.toJson($context.arguments.to),
    "sentAt": "$util.time.nowISO8601()"
  }
}
```

And for the response mapping template, select the default *Forward the result*. Save your resolver. You application is now ready, let’s page\!

## Send and subscribe to pages
<a name="send-and-subscribe-to-pages"></a>

For clients to receive pages, they must first be subscribed to an inbox.

In the **Queries** pane let’s execute the `inbox` subscription:

```
subscription Inbox {
    inbox(to: "Nadia") {
        body
        to
        from
        sentAt
    }
}
```

 *Nadia* will receive pages whenever the `Mutation.page` mutation is invoked. Let’s invoke the mutation by executing the mutation:

```
mutation Page {
    page(to: "Nadia", body: "Hello, World!") {
        body
        to
        from
        sentAt
    }
}
```

We just demonstrated the use of local resolvers, by sending a Page and receiving it without leaving AWS AppSync.