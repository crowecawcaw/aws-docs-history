# Test your integration using Amazon GameLift Servers Local

###### Note

This topic covers testing for games that are integrated with
the server SDK for Amazon GameLift Servers version 3.x and 4.x only.
Your server SDK package includes a compatible version of Amazon GameLift Servers Local.
If you're using server SDK version 5.x, see [Local testing with GameLift Server SDK 5.x](integration-testing-local.md "integration-testing-local.md") for local
testing with an Amazon GameLift Servers Anywhere fleet.
For guidance on migrating from SDK 4.x to 5.x, see [Migrate to GameLift Server SDK 5.x](../../../gamelift/latest/developerguide/reference-serversdk5-migration.md "../../../gamelift/latest/developerguide/reference-serversdk5-migration.md").

Use Amazon GameLift Servers Local to run a limited version of the managed Amazon GameLift Servers service on a local device
and test your game integration against it. This tool is useful when doing iterative
development on your game integration. The alternative—uploading each new build to
Amazon GameLift Servers and configuring a fleet to host your game—can take several or more each
time.

With Amazon GameLift Servers Local, you can verify the following:

- Your game server is correctly integrated with the Server SDK and is properly
  communicating with the Amazon GameLift Servers service to start new game sessions, accept new players,
  and report health and status.
- Your game client is correctly integrated with the AWS SDK for Amazon GameLift Servers and is able
  to retrieve information on existing game sessions, start new game sessions, join
  players to games and connect to the game session.
  Amazon GameLift Servers Local is a command-line tool that starts a self-contained version of the managed
  Amazon GameLift Servers service. Amazon GameLift Servers Local also provides a running event log of server process
  initialization, health checks, and API calls and responses. Amazon GameLift Servers Local recognizes a subset
  of the AWS SDK actions for Amazon GameLift Servers. You can make calls from the AWS CLI or from your game
  client. All API actions perform locally just as they do in the Amazon GameLift Servers web service.

Each server process should only host a single game session. The game session is the
executable you use to connect to Amazon GameLift Servers Local. When the game session is completed, you should
call `GameLiftServerSDK::ProcessEnding` and then exit the process. When testing
locally with Amazon GameLift Servers Local, you can start multiple server processes. Each process will connect
to Amazon GameLift Servers Local. You can then create one game session for each server process. When your game
session ends, your game server process should exit. You must then manually start another
server process.

Amazon GameLift Servers local supports the following APIs:

- CreateGameSession
- CreatePlayerSession
- CreatePlayerSessions
- DescribeGameSessions
- DescribePlayerSessions

## Set up Amazon GameLift Servers local

Amazon GameLift Servers Local is provided as an executable `.jar` file bundled with
the [Server SDK](https://aws.amazon.com/gamelift/servers/getting-started/ "https://aws.amazon.com/gamelift/servers/getting-started/"). It can be
run on Windows or Linux and used with any Amazon GameLift Servers-supported language. For SDK version 4.0.2,
you can download it from the [official GitHub releases](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/releases "https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/releases").
The GameLiftLocal.jar file is included in the GameLift-CSharp-ServerSDK-4.0.2.zip artifact.

Before running Local, you must also have the following installed.

- A build of the server SDK for Amazon GameLift Servers version 3.1.5 to 4.x.
- Java 8

## Test a game server

If you want to test your game server only, you can use the AWS CLI to simulate game
client calls to the Amazon GameLift Servers Local service. This verifies that your game server is
performing as expected with the following:

- The game server launches properly and initializes the server SDK for Amazon GameLift Servers.
- As part of the launch process, the game server notifies Amazon GameLift Servers that the server
  is ready to host game sessions.
- The game server sends health status to Amazon GameLift Servers every minute while
  running.
- The game server responds to requests to start a new game session.

1. **Start Amazon GameLift Servers Local.**

Open a command prompt window, navigate to the directory containing the file
`GameLiftLocal.jar` and
run it. By default, Local listens for requests from game clients on port 8080.
To specify a different port number, use the `-p` parameter, as shown
in the following example:

```
java -jar GameLiftLocal.jar -p 9080
```

Once Local starts, you see logs indicating that two local servers were
started, one listening for your game server and one listening for your game
client or the AWS CLI. Logs continue to report activity on the two local servers,
including communication to and from your game components. 2. **Start your game server.**

Start your Amazon GameLift Servers-integrated game server locally. You don't need to change the
endpoint for the game server.

In the Local command prompt window, log messages indicate that your game
server has connected to the Amazon GameLift Servers Local service. This means that your game
server successfully initialized the server SDK for Amazon GameLift Servers (with
`InitSDK()`). It has called `ProcessReady()` with the
log paths shown and, if successful, is ready to host a game session. While the
game server is running, Amazon GameLift Servers logs each health status report from the game
server. The following log messaging example shows a successfully integrated game
server:

```
16:50:53,217  INFO || - [SDKListenerImpl] nioEventLoopGroup-3-1 - SDK connected: /127.0.0.1:64247
16:50:53,217  INFO || - [SDKListenerImpl] nioEventLoopGroup-3-1 - SDK pid is 17040, sdkVersion is 3.1.5 and sdkLanguage is CSharp
16:50:53,217  INFO || - [SDKListenerImpl] nioEventLoopGroup-3-1 - NOTE: Only SDK versions 3.1.5 and above are supported in GameLiftLocal!
16:50:53,451  INFO || - [SDKListenerImpl] nioEventLoopGroup-3-1 - onProcessReady received from: /127.0.0.1:64247 and ackRequest requested? true
16:50:53,543  INFO || - [SDKListenerImpl] nioEventLoopGroup-3-1 - onProcessReady data: logPathsToUpload: "C:\\game\\logs"
logPathsToUpload: "C:\\game\\error"
port: 1935

16:50:53,544  INFO || - [HostProcessManager] nioEventLoopGroup-3-1 - Registered new process true, true,
16:50:53,558  INFO || - [SDKListenerImpl] nioEventLoopGroup-3-1 - onReportHealth received from /127.0.0.1:64247 with health status: healthy
```

Potential error and warning messages include the following:

    * Error: "ProcessReady did not find a process with pID:
     `<process ID>`! Was InitSDK()
     invoked?"
    * Warning: "Process state already exists for process with pID:
     `<process ID>`! Is ProcessReady(...)
     invoked more than once?"

3. **Start the AWS CLI.**

Once your game server successfully calls `ProcessReady()`, you can
start making client calls. Open another command prompt window and start the
AWS CLI tool. The AWS CLI by default uses the Amazon GameLift Servers web service endpoint. You must
override this with the Local endpoint in every request using the
`--endpoint-url` parameter, as shown in the following example
request.

```
AWS gamelift describe-game-sessions --endpoint-url http://localhost:9080  --fleet-id fleet-123
```

In the AWS CLI command prompt window, `AWS gamelift` commands
result in responses as documented in the [AWS CLI Command Reference](../../../cli/latest/reference/gamelift.md "../../../cli/latest/reference/gamelift.md"). 4. **Create a game session.**

With the AWS CLI, submit a [CreateGameSession()](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md") request. The request should follow the expected
syntax. For Local, the `FleetId` parameter can be set to any valid
string (`^fleet-\S+`).

```
AWS gamelift create-game-session --endpoint-url http://localhost:9080 --maximum-player-session-count 2 --fleet-id
    fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
```

In the Local command prompt window, log messages indicate that Amazon GameLift Servers Local has
sent your game server an `onStartGameSession` callback. If a game
session is successfully created, your game server responds by invoking
`ActivateGameSession`.

```
13:57:36,129  INFO || - [SDKInvokerImpl]
        Thread-2 - Finished sending event to game server to start a game session:
        arn:aws:gamelift:local::gamesession/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d/gsess-ab423a4b-b827-4765-aea2-54b3fa0818b6.
        Waiting for ack response.13:57:36,143  INFO || - [SDKInvokerImpl]
        Thread-2 - Received ack response: true13:57:36,144  INFO || -
        [CreateGameSessionDispatcher] Thread-2 - GameSession with id:
        arn:aws:gamelift:local::gamesession/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d/gsess-ab423a4b-b827-4765-aea2-54b3fa0818b6
        created13:57:36,227  INFO || - [SDKListenerImpl]
        nioEventLoopGroup-3-1 - onGameSessionActivate received from: /127.0.0.1:60020 and ackRequest
        requested? true13:57:36,230  INFO || - [SDKListenerImpl]
        nioEventLoopGroup-3-1 - onGameSessionActivate data: gameSessionId:
        "arn:aws:gamelift:local::gamesession/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d/gsess-abcdef12-3456-7890-abcd-ef1234567890"
```

In the AWS CLI window, Amazon GameLift Servers responds with a game session object including a
game session ID. Notice that the new game session's status is Activating. The
status changes to Active once your game server invokes ActivateGameSession. If
you want to see the changed status , use the AWS CLI to call
`DescribeGameSessions()`.

```
{
    "GameSession": {
      "Status": "ACTIVATING",
      "MaximumPlayerSessionCount": 2,
      "FleetId": "fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
      "GameSessionId": "arn:aws:gamelift:local::gamesession/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d/gsess-abcdef12-3456-7890-abcd-ef1234567890",
      "IpAddress": "127.0.0.1",
      "Port": 1935
    }
}
```

## Test a game server and client

To check your full game integration, including connecting players to games, you can
run both your game server and client locally. This allows you to test programmatic calls
from your game client to the Amazon GameLift Servers Local. You can verify the following actions:

- The game client is successfully making AWS SDK requests to the Amazon GameLift Servers Local
  service, including to create game sessions, retrieve information on existing
  game sessions, and create player sessions.
- The game server is correctly validating players when they try to join a game
  session. For validated players, the game server may retrieve player data (if
  implemented).
- The game server reports a dropped connection when a player leaves the
  game.
- The game server reports ending a game session.

1. **Start Amazon GameLift Servers Local.**

Open a command prompt window, navigate to the directory containing the file
`GameLiftLocal.jar` and
run it. By default, Local listens for requests from game clients on port 8080.
To specify a different port number, use the `-p` parameter, as shown
in the following example.

```
./gamelift-local -p 9080
```

Once Local starts, you see logs showing that two local servers were started,
one listening for your game server and one listening for your game client or the
AWS CLI. 2. **Start your game server.**

Start your Amazon GameLift Servers-integrated game server locally. See [Test a game server](#integration-testing-local-server "#integration-testing-local-server") for more detail on
message logs. 3. **Configure your game client for Local and start
it.**

To use your game client with the Amazon GameLift Servers Local service, you must make the
following changes to your game client's setup, as described in [Set up the Amazon GameLift Servers API](gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize "gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize"):

    * Change the `ClientConfiguration` object to point to your
     Local endpoint, such as `http://localhost:9080`.
    * Set a target fleet ID value. For Local, you do not need a real fleet
     ID; set the target fleet to any valid string (`^fleet-\S+`),
     such as `fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d`.
    * Set AWS credentials. For Local, you do not need real AWS
     credentials; you can set the access key and secret key to any string.

In the Local command prompt window, once you start the game client, log
messages should indicate that it has initialized the `GameLiftClient`
and is successfully communicated with the Amazon GameLift Servers service. 4. **Test game client calls to the Amazon GameLift Servers
service.**

Verify that your game client is successfully making any or all of the
following API calls:

    * [CreateGameSession()](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md")
    * [DescribeGameSessions()](../../../gamelift/latest/apireference/API_DescribeGameSessions.md "../../../gamelift/latest/apireference/API_DescribeGameSessions.md")
    * [CreatePlayerSession()](../../../gamelift/latest/apireference/API_CreatePlayerSession.md "../../../gamelift/latest/apireference/API_CreatePlayerSession.md")
    * [CreatePlayerSessions()](../../../gamelift/latest/apireference/API_CreatePlayerSessions.md "../../../gamelift/latest/apireference/API_CreatePlayerSessions.md")
    * [DescribePlayerSessions()](../../../gamelift/latest/apireference/API_DescribePlayerSessions.md "../../../gamelift/latest/apireference/API_DescribePlayerSessions.md")

In the Local command prompt window, only calls to
`CreateGameSession()` result in log messages. Log messages show
when Amazon GameLift Servers Local prompts your game server to start a game session
(`onStartGameSession` callback) and gets a successful
`ActivateGameSession` when your game server invokes it. In the
AWS CLI window, all API calls result in responses or error messages as documented. 5. **Verify that your game server is validating new player
connections.**

After creating a game session and a player session, establish a direct
connection to the game session.

In the Local command prompt window, log messages should show that the game
server has sent an `AcceptPlayerSession()` request to validate the
new player connection. If you use the AWS CLI to call
`DescribePlayerSessions()`, the player session status should
change from Reserved to Active. 6. **Verify that your game server is reporting game and
player status to the Amazon GameLift Servers service.**

For Amazon GameLift Servers to manage player demand and correctly report metrics, your game
server must report various statuses back to Amazon GameLift Servers. Verify that Local is logging
events related to following actions. You may also want to use the AWS CLI to track
status changes.

    * **Player disconnects from a game
     session** – Amazon GameLift Servers Local log messages should show
     that your game server calls `RemovePlayerSession()`. An AWS CLI
     call to `DescribePlayerSessions()` should reflect a status
     change from `Active` to `Completed`. You might
     also call `DescribeGameSessions()` to check that the game
     session's current player count decreases by one.
    * **Game session ends** – Amazon GameLift Servers
     Local log messages should show that your game server calls
     `TerminateGameSession()`.


    ###### Note

    Previous guidance was to call `TerminateGameSession()`
     when ending a game session. This method is deprecated with Amazon GameLift Servers
     Server SDK v4.0.1. See [End a game session](gamelift-sdk-server-api.md#gamelift-sdk-server-shutdownsession "gamelift-sdk-server-api.md#gamelift-sdk-server-shutdownsession").
    * **Server process is terminated** –
     Amazon GameLift Servers Local log messages should show that your game server calls
     `ProcessEnding()`. An AWS CLI call to
     `DescribeGameSessions()` should reflect a status change
     from `Active` to `Terminated` (or
     `Terminating`).

## Variations with local

When using Amazon GameLift Servers Local, keep in mind the following:

- Unlike the Amazon GameLift Servers web service, Local does not track a server's health status
  and initiate the `onProcessTerminate` callback. Local simply stops
  logging health reports for the game server.
- For calls to the AWS SDK, fleet IDs are not validated, and can be any string
  value that meets the parameter requirements (`^fleet-\S+`).
- Game session IDs created with Local have a different structure. They include
  the string `local`, as shown here:

```
arn:aws:gamelift:local::gamesession/fleet-123/gsess-56961f8e-db9c-4173-97e7-270b82f0daa6
```
