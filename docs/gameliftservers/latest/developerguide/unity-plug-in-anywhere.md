# Plugin for Unity: Set up local testing with

Amazon GameLift Servers Anywhere

In this workflow, you add client and server game code for Amazon GameLift Servers
functionality and use the plugin to designate your local workstation as a test game
server host. When you've completed integration tasks, use the plugin to build your game
client and server components.

###### To start the Amazon GameLift Servers Anywhere workflow:

- In the Unity editor main menu, choose **Amazon GameLift Servers** and select **Host
  with Anywhere**. This action opens the plugin page for setting up
  your game with an @Anywhere fleet. The page presents a five-step process to
  integrate, build, and launch your game components.

## Set your profile

Choose the profile you want to use when following this workflow. The profile you
select impacts all steps in the workflow. All resources you create are associated
with the profile’s AWS account and are placed in the profile’s default AWS Region.
The profile user’s permissions determine your access to AWS resources and
actions.

1. Select a profile from the dropdown list of available profiles. If you
   don’t have a profile yet or want to create a new one, go to the **Amazon GameLift Servers**
   menu and choose **Set AWS Account Profiles**.
2. If bootstrap status is not “Active“, choose **Bootstrap
   profile** and wait for the status to change to “Active“.

## Integrate your game code with the C# server

SDK

###### Note

If you imported the sample game, you can skip this step. The sample game assets already
have the necessary server and client code in place.

For this step in the workflow, you make updates to the client and server code in your game project.

- \* Game servers must be able to communicate with the Amazon GameLift Servers service to receive
  prompts to start a game session, provide game session connection information, and report status.
- Game clients must be able to get information about game sessions, join or start game
  sessions, and get connection information to join a game.

### Integrate your server code

If you’re using your own game project with custom scenes, use provided sample code to add required
server code to your game project:

1. In your game project files, open the
   `Assets/Scripts/Server` folder. If it doesn’t
   exist, create it.
2. Go to the GitHub repo [aws/amazon-gamelift-plugin-unity](https://github.com/aws/amazon-gamelift-plugin-unity "https://github.com/aws/amazon-gamelift-plugin-unity") and open the path
   `Samples~/SampleGame/Assets/Scripts/Server`.
3. Locate the file `GameLiftServer.cs` and copy it into your game project’s
   `Server` folder. When you build a server
   executable, use this file as the build target.

The sample code includes these minimum required elements, which use Amazon GameLift Servers C# server SDK (version 5):

- Initializes an Amazon GameLift Servers API client. The `InitSDK()` call with server parameters is
  required for an Amazon GameLift Servers Anywhere fleet. These settings are automatically
  set for use in the plugin.
- Implements required callback functions to respond to requests from the Amazon GameLift Servers service,
  including `OnStartGameSession`,
  `OnProcessTerminate`, and
  `onHealthCheck`.
- Calls `ProcessReady()` with a designated port to notify the Amazon GameLift Servers service when the
  server process is ready to host game sessions.

If you want to customize the sample server code, see these resources:

- [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
- [C# server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")

### Integrate your client code

If you’re using your own game project with custom scenes, then you need to
integrate basic functionality into your game client. You also need to add UI
elements so that players can sign in and join a game session. Use the service API for Amazon GameLift Servers (in the AWS SDK) to get game session information, create
new game sessions, or join existing game sessions,

When building a client for local testing with an Anywhere fleet, you can add
direct calls to the Amazon GameLift Servers service. When you develop your game for
cloud hosting—or if you plan to use Anywhere fleets for production
hosting—you’ll need to create a client-side backend service to handle all
communication between game clients and the Amazon GameLift Servers service.

To integrate Amazon GameLift Servers into your client code, use the following
resources as a guide.

- Integrate the client with the GameLiftCoreApi class in the GitHub
  repo aws/amazon-gamelift-plugin-unity. This class provides controls
  for player authentication and for retrieving game session
  information.
- View sample game integrations, available in the GitHub repo
  aws/amazon-gamelift-plugin-unity,
  `Samples~/SampleGame/Assets/Scripts/Client/GameLiftClient.cs`.
- Follow instructions in Add Amazon GameLift Servers to your Unity game
  client.

For game clients connecting to an Anywhere fleet, your game client
needs the following information. The plugin automatically updates your game
project to use the resources that your create in the plugin.

- FleetId - The unique identifier for your Anywhere fleet.
- FleetLocation - The custom location of your Anywhere
  fleet.
- AwsRegion - The AWS region where your Anywhere fleet is hosted.
  This is the region you set in your user profile.
- ProfileName - An AWS credentials profile on your local machine that allows access to the
  AWS SDK for Amazon GameLift Servers . The game client uses these credentials to
  authenticate requests to the Amazon GameLift Servers service.

###### Note

The credentials profile is generated by the plugin and stored on the local
machine. As a result, you must run the client on the local machine (or on a
machine with the same profile).

## Connect to an Anywhere fleet

In this step, you designate an Anywhere fleet to use. An Anywhere fleet defines a collection of compute resources,
which can be located anywhere, for game server hosting.

- If the AWS account you’re currently using has existing Anywhere fleets, open the
  **Fleet name** dropdown field and choose a fleet. This
  dropdown only shows the Anywhere fleets in the AWS Region for the
  currently active user profile.
- If there are no existing fleets—or you want to create a new one, choose **Create new
  Anywhere fleet** and provide a fleet name.

After you’ve chosen an Anywhere fleet for your project, Amazon GameLift Servers verifies that fleet
status is active and displays the fleet ID. You can track progress of this request in
the Unity editor’s output log.

## Register a compute

In this step, you register your local workstation as a compute resource in the new Anywhere fleet.

1. Enter a compute name for your local machine. If you add more than one compute in the fleet, the names must
   be unique.
2. Choose **Register compute**. You can track progress of this request in the
   Unity editor’s output log.

The plugin registers your local workstation with the IP address set to localhost (127.0.0.1). This setting assumes that you’ll
run your game client and server on the same machine.

In response to this action, Amazon GameLift Servers verifies that it can connect to the compute and returns information about the
newly registered compute.

## Launch game

In this step you build your game components and launch them to play the game. Complete the following tasks:

1. Configure your game client. In this step, you prompt the plugin to
   update a `GameLiftClientSettings` asset for your game
   project. The plugin uses this asset to store certain information that your
   game client needs to connect to the Amazon GameLift Servers service.
   1. If you didn’t import and initialize the sample game, create a new
      `GameLiftClientSettings` asset. In the Unity
      editor main menu, choose **Assets, Create,
      Amazon GameLift, Client Settings**. If you create
      multiple copies of `GameLiftClientSettings` in
      your project, the plugin automatically detects this and notifies you
      which asset the plugin will update.
   2. In **Launch Game**, choose **Configure Client: Apply Anywhere Settings**.
      This action updates your game client settings to use the Anywhere fleet
      that you just set up.

2. Build and run your game client.
   1. Build a client executable using the standard Unity build process. In **File, Build
      Settings**, switch the platform to **Windows,
      Mac, Linux**. If you imported the sample game and
      initialized the settings, the build list and build target are
      automatically updated.
   2. Launch one or more instances of the newly built game client executable.

3. Launch a game server in your Anywhere fleet. Choose **Server: Launch Server**
   in Editor. This task starts a live server that your client can connect to as
   long as the Unity editor remains open.
4. Start or join a game session. In your game client instances, use the UI to join each client to a game session. How you do this depends on how you added functionality to the client.

If you're using the sample game client, it has the following characteristics:

- A player login component. When connecting to a game server on an Anywhere fleet,
  there is no player validation. You can enter any values to join the game
  session.
- A simple join game UI. When a client attempts to join a game, the client
  automatically looks for an active game session with an available player slot. If no
  game session is available, the client requests a new game session. If a game session
  is available, the client requests to join the available game session. When testing
  your game with multiple concurrent clients, the first client starts the game
  session, and the remaining clients automatically join the existing game
  session.
- Game sessions with four player slots. You can launch up to four game client instances
  concurrently and they will join the same game session.

###### Launch from a server executable (optional)

You can build and launch your game server executable for testing on an Anywhere fleet.

1. Build a server executable using the standard Unity build process. In **File, Build
   Settings**, switch the platform to **Dedicated
   Server** and build.
2. Get a short-term authentication token by calling the AWS CLI command
   [get-compute-auth-token](../../../cli/latest/reference/gamelift/get-compute-auth-token.md "../../../cli/latest/reference/gamelift/get-compute-auth-token.md") with your Anywhere fleet ID and AWS
   Region. The fleet ID is displayed in **Connect to an
   Anywhere Fleet** when you create the fleet. The AWS Region is
   displayed in **Set Your Profile** when you
   select your active profile.

```
aws gamelift get-compute-auth-token --fleet-id [your anywhere fleet ID] --region [your AWS region]
```

3. Launch the newly built game server executable from a command line and pass
   in a valid auth token.

```
my_project.exe --authToken [token]
```
