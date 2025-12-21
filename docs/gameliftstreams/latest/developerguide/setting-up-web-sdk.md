# Setting up a web server and client with Amazon GameLift Streams

In this tutorial, you will set up a web client application that integrates Amazon GameLift Streams' streaming service. Then, you will use the Amazon GameLift Streams
Web SDK, a JavaScript library, and sample code that you can start with. The sample code includes a simple Amazon GameLift Streams backend web server and a
simple web client. By the end of this tutorial, you can start a stream by using the sample code.

If it's your first time using Amazon GameLift Streams, we highly recommend starting with the [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md") tutorial, which walks you through uploading a game to Amazon S3 and testing streaming it from within
the Amazon GameLift Streams console in your browser.

## Prerequisites

- An AWS account with proper credentials for programmatic access. For more information, see [Setting up Amazon GameLift Streams as a developer](setting-up.md "setting-up.md").
- The AWS SDK.
- An Amazon GameLift Streams-supported web browser — see [Supported browsers and input](sdk-browsers-input.md "sdk-browsers-input.md").
- Node.js — see [Node.js downloads](https://nodejs.org/en/download "https://nodejs.org/en/download") page.

## Download the Web SDK

For this tutorial, you will need to download the following materials from the Resources section of the
[Getting Started product page](https://aws.amazon.com/gamelift/streams/getting-started/ "https://aws.amazon.com/gamelift/streams/getting-started/"):

- **Amazon GameLift Streams Web SDK bundle**: This includes sample code for a simple backend service and web
  client.
- **Amazon GameLift Streams Web SDK API Reference**: This API reference documents Amazon GameLift Streams API wrappers for
  JavaScript.

## Set up your streaming resources

You must have stream resources—an application and a stream group—to start a stream. Specifically, you must
have:

- An application in **Ready** status.
- A stream group in **Active** status with available stream capacity.
- For streaming in locations other than the primary location, the application must have finished replicating to that location.

To set up an application and a stream group using either the Amazon GameLift Streams console or Amazon GameLift Streams CLI, refer to [Prepare an application in Amazon GameLift Streams](applications.md "applications.md") and [Manage streaming with an Amazon GameLift Streams stream group](stream-groups.md "stream-groups.md"), respectively. Alternatively, for
an end-to-end walkthrough in the Amazon GameLift Streams console, refer to [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md").

## Set up a backend server

The backend server is responsible for handling tasks such as authenticating users, configuring stream parameters, and performing
Amazon GameLift Streams service API calls on behalf of end-users. Review the sample code and the Amazon GameLift Streams Web SDK API Reference to learn more about setting this
up. Specifically, see the server.js file in the Amazon GameLift Streams Web SDK package.

###### Important

This code is example code for testing and evaluation purposes only and should not be used in a production capacity.

###### To run the sample backend service

1. Open a terminal or command prompt and navigate to the folder
   `AmazonGameLiftStreamsWebSDK\GameLiftStreamsSampleGamePublisherService\`.
2. Run the following commands:

```

npm install
node server.js

```

With the sample backend service running, end-users can connect to a stream through the web client. Test the web client in the next
step.

## Launch a web client

The web client application is responsible for receiving and decoding Amazon GameLift Streams streams, streaming to end-users, and providing the web
browser UI for end-users to engage with the application. Review the sample code and the Amazon GameLift Streams Web SDK API Reference to learn more about how to
integrate the JavaScript Amazon GameLift Streams Web SDK into your own web client application. Specifically, see `public/index.html` in the
Amazon GameLift Streams Web SDK package. You can also look at the web page source when you launch a web client in your browser.

###### Note

The Windows runtime in Amazon GameLift Streams supports stream sessions over IPv4 or IPv6. However, Linux and Proton runtime environments only support
streaming over IPv4.

###### To launch a web client application

1. Open a web browser and navigate to `http://localhost:`port`/`. The port number is set
   by the backend server; by default, this is HTTP port 8000.
2. Play the game or use the software.
   1. To attach input, such as your mouse, choose **Attach input**.
   2. To exit the game, choose the **Esc** key.
   3. To stop the server process, choose **Ctrl+C** key.

## Clean up streaming resources

###### Warning

A stream group incurs costs when it has allocated streaming capacity, even if that capacity is unused. To avoid unnecessary
costs, scale your stream groups to your required size. We suggest during development that you scale always-on capacity and
target-idle capacity in your stream groups to zero when not in use. For more information, refer to [Scale stream groups to zero capacity](pricing.md#pricing-pause-stream-groups "pricing.md#pricing-pause-stream-groups").

After you complete the tutorial and no longer need to stream your application, follow these steps to clean up your Amazon GameLift Streams
resources.

**Deleting a stream group**

When you delete a stream group, Amazon GameLift Streams works to release all stream capacity.

###### To delete a stream group using the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. To view a list of your existing stream groups, in the navigation pane, choose **Stream groups**.
3. Choose the name of the stream group that you want to delete.
4. On the stream group detail page, choose **Delete**.
5. In the **Delete** dialog box, confirm the delete action.

Amazon GameLift Streams begins releasing compute resources and deleting the stream group. During this time, the stream group is in
**Deleting** status. After Amazon GameLift Streams deletes the stream group, you can no longer retrieve it.

**Deleting an application**

You can only delete an application that meets the following conditions:

- The application is in the **Ready** or **Error** state.
- An application is not streaming in any ongoing stream session. You must wait until the client ends the stream session or call
  [TerminateStreamSession](../apireference/API_TerminateStreamSession.md "../apireference/API_TerminateStreamSession.md") in the Amazon GameLift Streams API to end the stream.

If the application is linked to any stream groups, you must unlink it from all associated stream groups before you can delete it. In the console, a dialog box will walk you through this process.

###### To delete an application using the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. In the navigation bar, choose **Applications** to view a list
   of your existing applications. Choose the application you want to delete.
3. In the application detail page, choose **Delete**.
4. In the **Delete** dialog box, confirm the delete action.

Amazon GameLift Streams begins deleting the application. During this time, the application is in `Deleting` status. After Amazon GameLift Streams
deletes the application, you can no longer retrieve it.
