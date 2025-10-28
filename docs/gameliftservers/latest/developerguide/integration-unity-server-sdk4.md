# Integrate Amazon GameLift Servers with a Unity game server

project

###### Note

This topic provides information for an earlier version of the Amazon GameLift Servers plugin for Unity. Version 1.0.0
(released in 2021) uses the server SDK for Amazon GameLift Servers 4.x or earlier. For documentation on the
latest version of the plugin, which uses server SDK 5.x and supports Amazon GameLift Servers Anywhere, see
[Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md").

This topic helps you prepare your custom game server for hosting on Amazon GameLift Servers. The game server
must be able to notify Amazon GameLift Servers about its status, to start and stop game sessions when
prompted, and to perform other tasks. For more information, see  [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").

## Prerequisites

Before integrating your game server, complete the following tasks:

- [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md")
- [Install and set up the plugin](unity-plug-in-sdk4.md#unity-plug-in-sdk4-install "unity-plug-in-sdk4.md#unity-plug-in-sdk4-install")

## Set up a new server process

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

Set up communication with Amazon GameLift Servers and report that the server process is ready to host a
game session.

1. Initialize the server SDK by calling `InitSDK()`.
2. To prepare the server to accept a game session, call
   `ProcessReady()` with the connection port and game session
   location details. Include the names of callback functions that Amazon GameLift Servers service
   invokes, such as `OnGameSession()`,
   `OnGameSessionUpdate()`, `OnProcessTerminate()`,
   `OnHealthCheck()`. Amazon GameLift Servers might take a few minutes to provide a
   callback.
3. Amazon GameLift Servers updates the status of the server process to `ACTIVE`.
4. Amazon GameLift Servers calls `onHealthCheck` periodically.

The following code example shows how to set up a simple server process with Amazon GameLift Servers.

```
//initSDK
var initSDKOutcome = GameLiftServerAPI.InitSDK();

//processReady
// Set parameters and call ProcessReady
var processParams = new ProcessParameters(
    this.OnGameSession,
    this.OnProcessTerminate,
    this.OnHealthCheck,
    this.OnGameSessionUpdate,
    port,
    // Examples of log and error files written by the game server
    new LogParameters(new List<string>()
        {
            "C:\\game\\logs",
            "C:\\game\\error"
        })
);

var processReadyOutcome = GameLiftServerAPI.ProcessReady(processParams);

// Implement callback functions
void OnGameSession(GameSession gameSession)
{
    // game-specific tasks when starting a new game session, such as loading map
    // When ready to receive players
    var activateGameSessionOutcome = GameLiftServerAPI.ActivateGameSession();
}

void OnProcessTerminate()
{
    // game-specific tasks required to gracefully shut down a game session,
    // such as notifying players, preserving game state data, and other cleanup
    var ProcessEndingOutcome = GameLiftServerAPI.ProcessEnding();
}

bool OnHealthCheck()
{
    bool isHealthy;
    // complete health evaluation within 60 seconds and set health
    return isHealthy;
}
```

## Start a game session

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

After game initialization is complete, you can start a game session.

1. Implement the callback function `onStartGameSession`. Amazon GameLift Servers invokes
   this method to start a new game session on the server process and receive player
   connections.
2. To activate a game session, call `ActivateGameSession()`. For more
   information about the SDK, see [C# server SDK for Amazon GameLift Servers 4.x --
   Actions](integration-server-sdk-csharp-ref-actions.md "integration-server-sdk-csharp-ref-actions.md").

The following code example illustrates how to start a game session with Amazon GameLift Servers.

```
void OnStartGameSession(GameSession gameSession)
{
    // game-specific tasks when starting a new game session, such as loading map
    ...
    // When ready to receive players
    var activateGameSessionOutcome = GameLiftServerAPI.ActivateGameSession();
}
```

## End a game session

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

Notify Amazon GameLift Servers when a game session is ending. As a best practice, shut down server
processes after game sessions complete to recycle and refresh hosting resources.

1. Set up a function named `onProcessTerminate` to receive requests
   from Amazon GameLift Servers and call `ProcessEnding()`.
2. The process status changes to `TERMINATED`.

The following example describes how to end a process for a game session.

```
var processEndingOutcome = GameLiftServerAPI.ProcessEnding();

if (processReadyOutcome.Success)
   Environment.Exit(0);

// otherwise, exit with error code
Environment.Exit(errorCode);

```

## Create server build and upload to Amazon GameLift Servers

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

After you integrate your game server with Amazon GameLift Servers, upload the build files to a fleet so
that Amazon GameLift Servers can deploy it for game hosting. For more information on how to upload your
server to Amazon GameLift Servers, see [Deploy a custom server build for Amazon GameLift Servers
hosting](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md").
