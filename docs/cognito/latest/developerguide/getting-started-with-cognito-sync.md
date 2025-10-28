# Getting started with Amazon Cognito Sync

If you're new to Amazon Cognito Sync, use [AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/"). Like Amazon Cognito Sync, AWS AppSync is
a service for synchronizing application data across devices.

It enables user data like app preferences or game state to be synchronized.
It also extends these capabilities by allowing multiple users to
synchronize and collaborate in real time on shared data.

Amazon Cognito Sync is an AWS service and client library that enable cross-device syncing of
application-related user data. You can use it to synchronize user profile data across
mobile devices and web applications. The client libraries cache data locally so your app
can read and write data regardless of device connectivity status. When the device is
online, you can synchronize data, and if you set up push sync, notify other devices
immediately that an update is available.

## Set up an identity pool in Amazon Cognito

Amazon Cognito Sync requires an Amazon Cognito identity pool to provide user identities. Before you use
Amazon Cognito Sync you must first set up an identity pool. To create an identity pool and install the
SDK, see [Getting started with Amazon Cognito identity
pools](getting-started-with-identity-pools.md "getting-started-with-identity-pools.md").

## Store and sync data

After you have set up your identity pool and installed the SDK, you can start storing
and syncing data between devices. For more information, see [Synchronizing data across clients](synchronizing-data.md "synchronizing-data.md").
