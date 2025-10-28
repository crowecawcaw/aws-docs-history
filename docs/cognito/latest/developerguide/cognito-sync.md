# Amazon Cognito Sync

If you're new to Amazon Cognito Sync, use [AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/"). Like Amazon Cognito Sync, AWS AppSync is
a service for synchronizing application data across devices.

It enables user data like app preferences or game state to be synchronized.
It also extends these capabilities by allowing multiple users to
synchronize and collaborate in real time on shared data.

Amazon Cognito Sync is an AWS service and client library that makes it possible to sync
application-related user data across devices. Amazon Cognito Sync can synchronize user profile data across
mobile devices and the web without using your own backend. The client libraries cache data
locally so that your app can read and write data regardless of device connectivity status. When
the device is online, you can synchronize data. If you set up push sync, you can notify other
devices immediately that an update is available.

For information about Amazon Cognito Identity region availability, see [AWS
Service Region Availability](http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

To learn more about Amazon Cognito Sync, see the following topics.

###### Topics

- [Getting started with Amazon Cognito Sync](getting-started-with-cognito-sync.md "getting-started-with-cognito-sync.md")
- [Synchronizing data across clients](synchronizing-data.md "synchronizing-data.md")
- [Handling event callbacks](handling-callbacks.md "handling-callbacks.md")
- [Implementing push synchronization](push-sync.md "push-sync.md")
- [Implementing Amazon Cognito Sync streams](cognito-streams.md "cognito-streams.md")
- [Customizing workflows with Amazon Cognito Events](cognito-events.md "cognito-events.md")
