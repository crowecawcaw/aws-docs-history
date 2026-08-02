# Amazon Cognito Sync availability change

Amazon Cognito Sync is no longer open to new customers. For alternatives to
Amazon Cognito Sync, please explore [AWS AppSync](../../../appsync.md "../../../appsync.md") and [DynamoDB](../../../dynamodb.md "../../../dynamodb.md").

This page provides information about Amazon Cognito Sync changes and includes alternatives
for Amazon Cognito Sync customers.

[AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/") is a serverless service that
lets developers create and manage GraphQL APIs. [DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") is a key-value store for per-user
data such as profiles, preferences, and application settings. Migration from Amazon Cognito Sync
requires data transfer and updates to your applications to the different APIs and query
patterns by the new service.

If you have additional questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

## Frequently asked questions

What does this mean for the service?

Amazon Cognito Sync will no longer be accepting new customers. The service
will continue to operate for existing customers but there will be no new
feature development.

How will existing customers be impacted?

Existing customers will not experience any disruption to their
workloads. You can continue using Amazon Cognito Sync as normal.

What are the recommended alternatives to Amazon Cognito Sync?

- [AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/") –
  For real-time data synchronization across devices with GraphQL
  APIs.
- [DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") –
  For simple key-value user data storage (profiles, preferences,
  settings).

How do I migrate my data?

Migration requires updating your data schema, migrating data from the
Amazon Cognito Sync store to your chosen alternative, and updating client
applications to use the new services.

How can I get help if I have issues?

If you have questions about this, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").
