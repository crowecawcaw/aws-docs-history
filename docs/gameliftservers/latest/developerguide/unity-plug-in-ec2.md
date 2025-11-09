# Plugin for Unity: Deploy your game to a managed EC2

fleet

In this workflow, you use the plugin to prepare your game for hosting on cloud-based
compute resources that are managed by Amazon GameLift Servers. You add client and server game code for
Amazon GameLift Servers functionality, then upload your server build to the Amazon GameLift Servers service for hosting.
When this workflow is complete, you’ll have game servers running in the cloud and a
working game client that can connect to them.

###### To start the Amazon GameLift Servers managed Amazon EC2 workflow:

- In the Unity editor main menu, choose **Amazon GameLift Servers** and select **Host
  with Managed EC2**. This workflow presents a six-step process to
  integrate, build, deploy, and launch your game components.

## Set your profile

Choose the profile you want to use when following this workflow. The profile you
select impacts all steps in the workflow. All resources you create are associated
with the profile’s AWS account and are placed in the profile’s default AWS
Region. The profile user’s permissions determine your access to AWS resources and
actions.

1. Select a profile from the dropdown list of available profiles. If you
   don’t have a profile yet or want to create a new one, go to the Amazon GameLift Servers menu and choose **Set AWS Account
   Profiles**.
2. If bootstrap status is not “Active“, choose **Bootstrap
   profile** and wait for the status to change to “Active“.

## Integrate your game with Amazon GameLift Servers

For this task, you make updates to the client and server code in
your game project.

- Game servers must be able to communicate with the Amazon GameLift Servers
  service to receive prompts to start a game session, provide game session
  connection information, and report status.
- Game clients must be able to get information about game sessions, join or
  start game sessions, and get connection information to join a game.

###### Note

If you imported the sample game, you can skip this step. The sample game
assets already have the necessary server and client code in place.

### Integrate your server code

When using your own game project with custom scenes, use the provided sample
code to add required server code to your game project. If you integrated your
game project for testing with an Anywhere fleet, you’ve already completed the
instructions in this step.

1. In your game project files, open the
   `Assets/Scripts/Server` folder. If it doesn’t
   exist, create it.
2. Go to the GitHub repo [aws/amazon-gamelift-plugin-unity](https://github.com/aws/amazon-gamelift-plugin-unity "https://github.com/aws/amazon-gamelift-plugin-unity") and open the path
   `Samples~/SampleGame/Assets/Scripts/Server`.
3. Locate the file `GameLiftServer.cs` and copy it
   into your game project’s `Server` folder. When you
   build a server executable, use this file as the build target.

The sample code includes these minimum required elements, which use Amazon GameLift Servers C# server SDK (version 5):

- Initializes an Amazon GameLift Servers API client. The InitSDK() call with
  server parameters is required for an Amazon GameLift Servers Anywhere fleet.
  These settings are automatically set for use in the plugin.
- Implements required callback functions to respond to requests from the
  Amazon GameLift Servers service, including `OnStartGameSession`,
  `OnProcessTerminate`, and
  `onHealthCheck`.
- Calls `ProcessReady()` with a designated port to notify the
  Amazon GameLift Servers service when the server process is ready to host game
  sessions.

If you want to customize the sample server code, see these resources:

- [Add Amazon GameLift Servers to your game server with the server
  SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
- [C# server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")

### Integrate your client code

For game clients that connect to cloud-based game servers, it’s a best
practice to use a client-side backend service to make calls to the Amazon GameLift Servers service, instead of making the calls directly from the game client.

In the plugin workflow for hosting on a managed EC2 fleet, each deployment
scenario includes a pre-built backend service that includes the following
components:

- A set of Lambda functions and DynamoDB tables that are used to
  request game sessions and retrieve game session information. These
  components use an API gateway as the proxy.
- An Amazon Cognito user pool that generates unique player IDs and
  authenticates player connections.

To use these components, your game client needs functionality to send requests
to the backend service to do the following:

- Create a player user in the AWS Cognito user pool and
  authenticate.
- Join a game session and receive connection information.
- Join a game using matchmaking.

Use the following resources as a guide.

- Integrate the client with the [GameLiftCoreApi](https://github.com/aws/amazon-gamelift-plugin-unity/blob/main/Runtime/GameLiftCoreApi.cs "https://github.com/aws/amazon-gamelift-plugin-unity/blob/main/Runtime/GameLiftCoreApi.cs") class in the GitHub repo
  [aws/amazon-gamelift-plugin-unity](https://github.com/aws/amazon-gamelift-plugin-unity "https://github.com/aws/amazon-gamelift-plugin-unity"). This class provides controls for player authentication and for
  retrieving game session information.
- To view the sample game integrations go to the GitHub repo
  [aws/amazon-gamelift-plugin-unity](https://github.com/aws/amazon-gamelift-plugin-unity "https://github.com/aws/amazon-gamelift-plugin-unity") , `Samples~/SampleGame/Assets/Scripts/Client/GameLiftClient.cs`.
- [Integrate Amazon GameLift Servers game client functionality](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").

## Select deployment scenario

In this step, you choose the game hosting solution that you want to deploy at this time. You can have multiple deployments of your game, using any of the scenarios.

- **Single-region fleet:** Deploys your game server to a single
  fleet of hosting resources in the active profile’s default AWS region.
  This scenario is a good starting point for testing your server integration
  with AWS and server build configuration. It deploys the following
  resources:
  - AWS fleet (On-Demand) with your game server build installed and running.
  - Amazon Cognito user pool and client to enable players to authenticate and start a game.
  - API gateway authorizer that links user pool with APIs.
  - WebACl for throttling excessive player calls to API gateway.
  - API gateway + Lambda function for players to request a game slot. This function calls
    `CreateGameSession()` if none are available.
  - API gateway + Lambda function for players to get connection info for their game request.

- **FlexMatch fleet:** Deploys your game server to a set of fleets
  and sets up a FlexMatch matchmaker with rules to create player matches. This scenario uses low-cost Spot hosting with a multi-fleet, multi-location structure for durable availability. This
  approach is useful when you're ready to start designing a matchmaker
  component for your hosting solution. In this scenario, you'll create the
  basic resources for this solution, which you can customize later as needed.
  It deploys the following resources:
  - FlexMatch matchmaking configuration and matchmaking rule set to accept player requests and
    form matches.
  - Three AWS fleets with your game server build installed and
    running in multiple locations. Includes two Spot fleets and one
    On-Demand fleet as a backup.
  - AWS game session placement queue that fulfills requests
    for proposed matches by finding the best possible hosting resource
    (based on viability, cost, player latency, etc.) and starting a game
    session.
  - Amazon Cognito user pool and client to enable players to authenticate
    and start a game.
  - API gateway authorizer that links user pool with APIs.
  - WebACl for throttling excessive player calls to API gateway.
  - API gateway + Lambda function for players to request a game slot. This
    function calls `StartMatchmaking()`.
  - API gateway + Lambda function for players to get connection info for
    their game request.
  - Amazon DynamoDB tables to store matchmaking tickets for players and game
    session information.
  - SNS topic + Lambda function to handle GameSessionQueue events.

## Set game parameters

In this step, you describe your game for uploading to AWS.

- **Game name:** Provide a meaningful
  name for your game project. This name is used within the
  plugin.
- **Fleet name:** Provide a meaningful
  name for your managed EC2 fleet. Amazon GameLift Servers uses this name
  (along with the fleet ID) when listing resources in the AWS
  console.
- **Build name:** Provide a meaningful
  name for your server build. AWS uses this name to refer to the copy
  of your server build that’s uploaded to Amazon GameLift Servers and used for
  deployments.
- **Launch parameters:** Enter
  optional instructions to run when launching the server executable on
  a managed EC2 fleet instance. Maximum length is 1024
  characters.
- **Game server folder:** Provide the
  path to a local folder containing your server build.
- **Game server file:** Specify the
  server executable file name.

## Deploy scenario

In this step, you deploy your game to a cloud hosting solution based on the deployment
scenario you chose. This process can take several minutes while AWS
validates your server build, provisions hosting resources, installs your game server,
launches server processes, and gets them ready to host game sessions.

To start deployment, choose **Deploy CloudFormation**.
You can track the status of your game hosting here. For more detailed information, you
can sign in to the AWS Management console for AWS and view event
notifications. Be sure to sign in using the same account, user, and AWS Region as the
active user profile in the plugin.

When deployment is complete, you have your game server installed on an AWS
EC2 instance. At least one server process is running and ready to start a game session.

## Launch game client

When your fleet is successfully deployed, you now have game servers running and
available to host game sessions. You can now build your client, launch it, connect
to join the game session.

1. Configure your game client. In this step, you prompt the plugin to update
   a `GameLiftClientSettings` asset for your game project.
   The plugin uses this asset to store certain information that your game
   client needs to connect to the Amazon GameLift Servers service.
   1. If you didn’t import and initialize the sample game, create a new
      `GameLiftClientSettings` asset. In the Unity
      editor main menu, choose **Assets, Create,
      Amazon GameLift, Client Settings**. If you create
      multiple copies of `GameLiftClientSettings` in
      your project, the plugin automatically detects this and notifies you
      which asset the plugin will update.
   2. In **Launch Game**, choose **Configure Client: Apply Managed EC2
      Settings**. This action updates your game client
      settings to use the managed EC2 fleet that you just
      deployed.

2. Build your game client. Build a client executable using the standard Unity
   build process. In File, Build Settings, switch the platform to Windows, Mac,
   Linux. If you imported the sample game and initialized the settings, the
   build list and build target are automatically updated.
3. Launch the newly build game client executable. To start playing the game,
   start two to four client instances and use the UI in each to join a game
   session.

If you're using the sample game client, it has the following
characteristics:

- A player login component. When connecting to a game server on an Anywhere
  fleet, there is no player validation. You can enter any values to join the
  game session.
- A simple join game UI. When a client attempts to join a game, the client
  automatically looks for an active game session with an available player
  slot. If no game session is available, the client requests a new game
  session. If a game session is available, the client requests to join the
  available game session. When testing your game with multiple concurrent
  clients, the first client starts the game session, and the remaining clients
  automatically join the existing game session.
- Game sessions with four player slots. You can launch up to four game
  client instances concurrently and they will join the same game session.
