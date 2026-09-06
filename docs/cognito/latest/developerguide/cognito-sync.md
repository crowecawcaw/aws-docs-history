

# Amazon Cognito Sync
<a name="cognito-sync"></a>

**Note**  
Amazon Cognito Sync is no longer open to new customers. For alternatives to Amazon Cognito Sync, please explore [AWS AppSync](https://docs.aws.amazon.com/appsync/) and [DynamoDB](https://docs.aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

**Note**  
If you're new to Amazon Cognito Sync, use [AWS AppSync](https://aws.amazon.com/appsync/). Like Amazon Cognito Sync, AWS AppSync is a service for synchronizing application data across devices.  
It enables user data like app preferences or game state to be synchronized. It also extends these capabilities by allowing multiple users to synchronize and collaborate in real time on shared data.

 Amazon Cognito Sync is an AWS service and client library that makes it possible to sync application-related user data across devices. Amazon Cognito Sync can synchronize user profile data across mobile devices and the web without using your own backend. The client libraries cache data locally so that your app can read and write data regardless of device connectivity status. When the device is online, you can synchronize data. If you set up push sync, you can notify other devices immediately that an update is available. 

 For information about Amazon Cognito Identity region availability, see [AWS Service Region Availability](http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). 

To learn more about Amazon Cognito Sync, see the following topics.

**Topics**
+ [Amazon Cognito Sync availability change](cognito-sync-availability-change.md)
+ [Getting started with Amazon Cognito Sync](getting-started-with-cognito-sync.md)
+ [Synchronizing data across clients](synchronizing-data.md)
+ [Handling event callbacks](handling-callbacks.md)
+ [Implementing push synchronization](push-sync.md)
+ [Implementing Amazon Cognito Sync streams](cognito-streams.md)
+ [Customizing workflows with Amazon Cognito Events](cognito-events.md)