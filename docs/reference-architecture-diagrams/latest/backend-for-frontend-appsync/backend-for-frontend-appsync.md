# Backend for Frontend Using AppSync

Publication date: **May 6, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture shows how frontend client applications apply the Backend for Frontend (BFF) pattern to load UI-ready data projections and refresh the UI with event-driven notifications. You use [Amazon AppSync](../../../appsync/latest/devguide/what-is-appsync.md "../../../appsync/latest/devguide/what-is-appsync.md") GraphQL subscriptions over WebSockets to push real-time updates when microservices raise events about mutations in domain aggregates.

## Backend for Frontend Using AppSync

![Architecture diagram showing a Backend for Frontend pattern using Amazon AppSync, AWS Lambda, Amazon DynamoDB, and Amazon Cognito for real-time UI updates.](images/backend-for-frontend-appsync.png)

The following steps describe the architecture:

1. Purpose-built BFF event consumers catch events from your application and keep a denormalized view of data in [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") for frontend consumption.
2. On UI load, frontend clients authenticate with [Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md"), then query data with GraphQL by invoking the BFF API built with Amazon AppSync. The API fetches data from DynamoDB directly or through a BFF query handler built with [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md").
3. Frontend clients subscribe for subsequent data changes using Amazon AppSync subscriptions over WebSockets.
4. BFF event consumers continue to process all relevant events from your application and update the denormalized frontend data view in real time.
5. Amazon DynamoDB Streams captures all events from data changes in the BFF database. A Lambda trigger asynchronously invokes a BFF stream-handler function when it detects new stream records.
6. The BFF stream handler invokes an empty mutation on the Amazon AppSync GraphQL schema to force the subscription to trigger and send a notification to connected clients.
7. Frontend clients receive the change notification from Amazon AppSync and refresh the UI content.

## Further reading

For additional information, refer to the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date        |
| ------------------- | ----------------------------------------------- | ----------- |
| Initial publication | Reference architecture diagram first published. | May 6, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
