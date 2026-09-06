

# Start stream sessions with Amazon GameLift Streams
<a name="stream-sessions"></a>

This section covers stream sessions, the actual instance of a stream where an end user or player can interact with your application or play your game. You'll learn about how to test your own stream session and understand the stream session lifecycle.

 To launch stream sessions to end users, you can integrate Amazon GameLift Streams into your own service and client application; for more information, see [Amazon GameLift Streams backend service and web client](sdk.md). You can also create a stream URL, which starts a stream session in a supported web browser without requiring the end user to have AWS credentials or a client integration; for more information, see [Share stream sessions with stream URLs](stream-urls.md). 

## About stream sessions
<a name="stream-sessions-about"></a>

 The prerequisites to start a stream session are an application in **Ready** status, a stream group that has available capacity in the location where you want to stream, and the application replicated to the location where you want to stream. A stream session runs on one of the compute resources that a stream group has allocated. When you start a stream, you must specify a stream group and an application to stream using their ARN or ID values. 

 When you successfully start a stream session, you receive a unique identifier for that stream session. Then, you use that ID to connect the stream session to an end user. For more information, see [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html) in the *Amazon GameLift Streams API Reference*. 

 Optionally, you can provide an IAM role ARN when starting a stream session. If provided, Amazon GameLift Streams assumes the role and your application automatically receives AWS credentials. You do not need to change your application code. For more information, see [Provide AWS credentials to your streaming application](session-credentials.md). 

## Testing a stream in the console
<a name="stream-sessions-testing"></a>

 The most direct way for you to test how your application streams is through the Amazon GameLift Streams console. When you start a stream, Amazon GameLift Streams uses one of the compute resources that your stream group allocates. So, you must have available capacity in your stream group. 

**To test your stream in the Amazon GameLift Streams console**

1.  Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/).

1. You can test a stream in several ways. Start from the **Stream groups** page or **Test stream** page and follow these steps:

   1. Select a stream group that you want to use to stream.

   1. If you're starting from the **Stream groups** page, choose **Test stream**. If you're starting from the **Test stream** page, select **Choose**. This opens the **Test stream** configuration page for the selected stream group.

   1. In **Linked applications**, select an application.

   1. In **Location**, choose a location with available capacity.

   1. (Optional) In **Program configurations**, enter command-line arguments or environment variables to pass to the application as it launches.

   1. Confirm your selection, and choose **Test stream**.

1. After your stream loads, you can do the following actions in your stream:

   1. To connect input, such as your mouse, keyboard, and gamepad (except microphones, which are not supported in **Test stream**), choose **Attach input**. You automatically attach your mouse when you move the cursor into the stream window.

   1. To have files that were created during the streaming session exported to an Amazon S3 bucket at the end of the session, choose **Export files** and specify the bucket details. Exported files can be found on the **Sessions** page.

   1. To view the stream in fullscreen, choose **Fullscreen**. Press **Escape** to reverse this action.

1. To end the stream, choose **Terminate session**. When the stream disconnects, the stream capacity becomes available to start another stream.

**Note**  
The **Test stream** feature in the Amazon GameLift Streams console does not support microphones.

## Stream session lifecycle
<a name="stream-sessions-lifecycle"></a>

When working with stream sessions in Amazon GameLift Streams, this diagram can help you understand the different states that a stream session transitions to throughout its lifecycle. 
+ [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html) creates a new stream session, which begins in `ACTIVATING` state. When Amazon GameLift Streams finds available resources to host the stream, the stream session transitions to `ACTIVE`. When a client connects to the active stream, the stream session transitions to `CONNECTED`.
+ When a client disconnects from a stream, the stream session transitions to `PENDING_CLIENT_RECONNECTION` state. [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html) transitions the stream session to `RECONNECTING`, and will either initiate the client to reconnect to the stream or create a new stream session. When a stream session is ready for the client to reconnect, it transitions to `ACTIVE`. When the client reconnects, it transitions back to `CONNECTED`. If a client is disconnected for longer than `ConnectionTimeoutSeconds`, the stream session ends.
+ When a client doesn't connect to a stream session in `ACTIVE` or `PENDING_CLIENT_RECONNECTION` state within the period of time specified by `ConnectionTimeoutSeconds`, then it transitions to `TERMINATED`.
+ [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html) initiates termination of the stream, and the stream session transitions to `TERMINATING` state. When the stream session terminates successfully, it transitions to `TERMINATED`.
+ A stream session in any state, except `TERMINATED`, can transition to `ERROR`. When an API call returns `ERROR` as a Status value, check the value of StatusReason for a short description of the cause of the error. You can also call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) to check these values. 

![This diagram shows the different states that a stream session transitions to throughout its lifecycle.](http://docs.aws.amazon.com/gameliftstreams/latest/developerguide/images/stream_session_lifecycle.png)


## Timeout values affecting stream sessions
<a name="stream-sessions-lifecycle-timeouts"></a>

Stream sessions are governed by several timeout values that control different aspects of the session lifecycle. In roughly chronological order of when you might typically encounter them during the stream session lifecycle, they include the following:

**Placement timeout**  
Time limit for Amazon GameLift Streams to find compute resources to host a stream session using available capacity. Placement timeout varies based on the capacity type used to fulfill your stream request:  
+ Always-on capacity: 75 seconds
+ On-demand capacity:
  + Linux/Proton runtimes: 90 seconds
  + Windows runtime: 10 minutes
+ Behavior: If Amazon GameLift Streams cannot identify available resources within this time, the stream session `Status` changes to `ERROR` with a `StatusReason` of `placementTimeout`.

**Connection timeout**  
Length of time Amazon GameLift Streams waits for a client to connect or reconnect to a stream session.  
+ Parameter: `ConnectionTimeoutSeconds` in [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html)
+ Range: 1 - 3600 seconds (1 hour)
+ Default: 120 seconds (2 minutes)
+ Behavior: Timer starts when the stream session reaches `ACTIVE` or `PENDING_CLIENT_RECONNECTION` status. If no client connects before the timeout, the session `Status` transitions to `TERMINATED`.

**Session length timeout**  
Maximum duration Amazon GameLift Streams keeps a stream session open.  
+ Parameter: `SessionLengthSeconds` in [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html)
+ Range: 1 - 86400 seconds (24 hours)
+ Default: 43200 seconds (12 hours)
+ Behavior: Terminates the stream session regardless of any existing client connection when the time limit is reached.

## Terminating a stream session
<a name="stream-sessions-terminate"></a>

If you need to force a stream session to terminate, you have the following options:
+ **Use the TerminateStreamSession API:** To use [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html), you will need the stream group ID and the stream session ID. You can use [ListStreamSessions](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html) or [ListStreamSessionsByAccount](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessionsByAccount.html) with the `--status CONNECTED` parameter to get a list of stream sessions that have a client connected.
+ **Remove the session's location from its stream group:** Removing the location from the stream group where the session is streaming will terminate all active stream sessions in that location. You can remove a location in a stream group from the console or by using the [RemoveStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RemoveStreamGroupLocations.html) API.
+ **Delete the session's stream group:** Deleting a stream group will terminate all active stream sessions in all locations of the stream group. You can delete a stream group from the console or by using the [DeleteStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html) API. Use with caution since you will be abruptly ending client connections.

## Reconnecting to a stream session
<a name="stream-sessions-reconnection"></a>

If a client gets disconnected from a stream session without ending the session, it can reconnect to the session within the time specified by `ConnectionTimeoutSeconds` when the stream session was started. To reconnect to a session, you need the stream session's ID. For details, see [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html) in the *Amazon GameLift Streams API Reference*. You can see an example of reconnecting to a stream session in the [React Starter Sample](https://github.com/aws-samples/sample-amazon-gamelift-streams-react-app).

Reconnection is not available for stream sessions that are started by activating a stream URL. Because there is no reconnection, opening the stream URL again starts a completely new session and consumes another use from its `UsageLimit`. For more information, see [Share stream sessions with stream URLs](stream-urls.md).