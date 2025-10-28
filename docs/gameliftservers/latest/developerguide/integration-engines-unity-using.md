# Integrate Amazon GameLift Servers into a Unity

project

Learn how to integrate the Amazon GameLift Servers SDK for Unity into your game projects to access the full
server SDK feature set.

###### Tip

For faster deployment, try the Amazon GameLift Servers standalone plugin for Unity. It provides
guided UI workflows to quickly deploy your game server with minimal setup, so you can
try out your game components in action. See [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md").

Additional resources:

- [C# server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")
- [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md")

## Install the server SDK for

Unity

Get the open-source Amazon GameLift Servers for Unity from [GitHub](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity").
The repository's readme files contain prerequisites and installation
instructions.

## Set up an Amazon GameLift Servers Anywhere fleet for testing

You can set up your development workstation as an Amazon GameLift Servers Anywhere hosting fleet to iteratively test your Amazon GameLift Servers integration.
With this setup, you can start game server processes on your workstation, send player join or matchmaking requests to Amazon GameLift Servers
to start game sessions, and connect clients to the new game sessions. With your own workstation set up as a hosting server,
you can monitor all aspects of your game integration with Amazon GameLift Servers.

For instructions on setting up your workstation, see [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md")
to complete the following steps:

1. Create a custom location for your workstation.
2. Create an Amazon GameLift Servers Anywhere fleet with your new custom location. If successful, this request returns a fleet ID.
   Make a note of this value, as you'll need it later.
3. Register your workstation as a compute in the new Anywhere fleet. Provide a unique compute name and specify the
   IP address for your workstation. If successful, this request returns a service SDK endpoint, in the form of a WebSocket URL. Make
   a note of this value, as you'll need it later.
4. Generate an authentication token for your workstation compute. This short-lived authentication
   includes the token and an expiration date. Your game server uses it to
   authenticate communication with the Amazon GameLift Servers service. Store the authentication on
   your workstation compute so that your running game server processes can access
   it.

## Add Amazon GameLift Servers server code to your Unity

project

Your game server communicates with the Amazon GameLift Servers service to receive instructions and
report ongoing status. To accomplish this, you add game server code that uses the Amazon GameLift Servers
server SDK.

The provided code example illustrates the basic required integration elements. It uses
a `MonoBehavior` to illustrate a simple game server initialization with
Amazon GameLift Servers. The example assumes that the game server runs on an Amazon GameLift Servers Anywhere fleet for
testing. It includes code to:

- Initialize an Amazon GameLift Servers API client. The sample uses the version of
  `InitSDK()` with server parameters for your Anywhere fleet and
  compute. Use the WebSocket URL, fleet ID, compute name (host ID), and
  authentication token, as defined in the previous topic [Set up an Amazon GameLift Servers Anywhere fleet for testing](#integration-engines-unity-fleet "#integration-engines-unity-fleet").
- Implement callback functions to respond to requests from the Amazon GameLift Servers service,
  including `OnStartGameSession`, `OnProcessTerminate`, and
  `onHealthCheck`.
- Call ProcessReady() with a designated port to notify the Amazon GameLift Servers service when
  the process is ready to host game sessions.

The sample code provided establishes communication with the Amazon GameLift Servers service.
It also implements a set of callback functions that respond to requests from the Amazon GameLift Servers service. For
more information on each function and what the code does, see [Initialize the server process](gamelift-sdk-server-api.md#gamelift-sdk-server-initialize "gamelift-sdk-server-api.md#gamelift-sdk-server-initialize"). For more information on the SDK actions and
data types used in this code, read [C# server SDK 5.x for Amazon GameLift Servers --
Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md").

The sample code shows how to add the required functionality, as described in [Add Amazon GameLift Servers to your
game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md"). For more information on server SDK actions, see the [C# server SDK 5.x for Amazon GameLift Servers --
Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md").

```
using System.Collections.Generic;
using Aws.GameLift.Server;
using UnityEngine;

public class ServerSDKManualTest : MonoBehaviour
{
    //This example is a simple integration that initializes a game server process
    //that is running on an Amazon GameLift Servers Anywhere fleet.
    void Start()
    {
        //Identify port number (hard coded here for simplicity) the game server is listening on for player connections
        var listeningPort = 7777;

        //WebSocketUrl from RegisterHost call
        var webSocketUrl = "wss://us-west-2.api.amazongamelift.com";

        //Unique identifier for this process
        var processId = "myProcess";

        //Unique identifier for your host that this process belongs to
        var hostId = "myHost";

        //Unique identifier for your fleet that this host belongs to
        var fleetId = "myFleet";

        //Authorization token for this host process
        var authToken = "myAuthToken";

        //Server parameters are required for an Amazon GameLift Servers Anywhere fleet.
        //They are not required for an Amazon GameLift Servers managed EC2 fleet.
        ServerParameters serverParameters = new ServerParameters(
            webSocketUrl,
            processId,
            hostId,
            fleetId,
            authToken);

        //InitSDK establishes a local connection with an Amazon GameLift Servers agent
        //to enable further communication.
        var initSDKOutcome = GameLiftServerAPI.InitSDK(serverParameters);
        if (initSDKOutcome.Success)
        {
            //Implement callback functions
            ProcessParameters processParameters = new ProcessParameters(
            //Implement OnStartGameSession callback
                (gameSession) => {
                    //Amazon GameLift Servers sends a game session activation request to the game server
                    //with game session object containing game properties and other settings.
                    //Here is where a game server takes action based on the game session object.
                    //When the game server is ready to receive incoming player connections,
                    //it invokes the server SDK call ActivateGameSession().
                    GameLiftServerAPI.ActivateGameSession();
                },
                (updateGameSession) => {
                    //Amazon GameLift Servers sends a request when a game session is updated (such as for
                    //FlexMatch backfill) with an updated game session object.
                    //The game server can examine matchmakerData and handle new incoming players.
                    //updateReason explains the purpose of the update.
                },
                () => {
                    //Implement callback function OnProcessTerminate
                    //Amazon GameLift Servers invokes this callback before shutting down the instance hosting this game server.
                    //It gives the game server a chance to save its state, communicate with services, etc.,
                    //and initiate shut down. When the game server is ready to shut down, it invokes the
                    //server SDK call ProcessEnding() to tell Amazon GameLift Servers it is shutting down.
                    GameLiftServerAPI.ProcessEnding();
                },
                () => {
                    //Implement callback function OnHealthCheck
                    //Amazon GameLift Servers invokes this callback approximately every 60 seconds.
                    //A game server might want to check the health of dependencies, etc.
                    //Then it returns health status true if healthy, false otherwise.
                    //The game server must respond within 60 seconds, or Amazon GameLift Servers records 'false'.
                    //In this example, the game server always reports healthy.
                    return true;
                },
                //The game server gets ready to report that it is ready to host game sessions
                //and that it will listen on port 7777 for incoming player connections.
                listeningPort,
                new LogParameters(new List<string>()
                {
                    //Here, the game server tells Amazon GameLift Servers where to find game session log files.
                    //At the end of a game session, Amazon GameLift Servers uploads everything in the specified
                    //location and stores it in the cloud for access later.
                    "/local/game/logs/myserver.log"
                }));

            //The game server calls ProcessReady() to tell Amazon GameLift Servers it's ready to host game sessions.
            var processReadyOutcome = GameLiftServerAPI.ProcessReady(processParameters);
            if (processReadyOutcome.Success)
            {
                print("ProcessReady success.");
            }
            else
            {
                print("ProcessReady failure : " + processReadyOutcome.Error.ToString());
            }
        }
        else
        {
            print("InitSDK failure : " + initSDKOutcome.Error.ToString());
        }
    }

    void OnApplicationQuit()
    {
        //Make sure to call GameLiftServerAPI.ProcessEnding() and GameLiftServerAPI.Destroy() before terminating the server process.
        //These actions notify Amazon GameLift Servers that the process is terminating and frees the API client from memory.
        GenericOutcome processEndingOutcome = GameLiftServerAPI.ProcessEnding();
        GameLiftServerAPI.Destroy();
        if (processEndingOutcome.Success)
        {
            Environment.Exit(0);
        }
        else
        {
            Console.WriteLine("ProcessEnding() failed. Error: " + processEndingOutcome.Error.ToString());
            Environment.Exit(-1);
        }
    }
}
```

## Next steps

Now that you've prepared a game server build with the minimum required functionality
for hosting with Amazon GameLift Servers, consider these potential next steps:

- Deploy your integrated game server for and testing and development. With an
  Anywhere fleet, you can set up your local machine as a hosting resource and use
  it to test your game server and game client connections. For cloud-based
  hosting, deploy your game server to a managed EC2 or managed container fleet.
  See these topics for guidance:
  - [Set up for iterative development with Amazon GameLift Servers Anywhere](integration-dev-iteration.md "integration-dev-iteration.md")
  - [Amazon GameLift Servers Anywhere fleets](fleets-intro-anywhere.md "fleets-intro-anywhere.md")
  - [Amazon GameLift Servers managed EC2 fleets](fleets-intro-managed.md "fleets-intro-managed.md")
  - [Amazon GameLift Servers managed container fleets](fleets-intro-containers.md "fleets-intro-containers.md")

- Customize your game server integration by adding optional features. For
  example, you might want to add player sessions with unique player IDs, set up
  matchmaking backfill, or manage game server access to your other AWS resources
  (such as a database or content storage service). See these topics for guidance:
  - [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
  - [C++ (Unreal) server SDK 5.x for
    Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")

- Customize your game client component to request game sessions, receive
  connection information, and connect directly to a game server to play a game.
  See these topics for guidance:
  - [Integrate your game client
    withAmazon GameLift Servers](gamelift-sdk-client.md "gamelift-sdk-client.md")
