# Set up local testing with Amazon GameLift Servers Anywhere

###### Note

This topic covers local testing for games that are integrated with the server SDK for Amazon GameLift Servers
version 5.x. If your game uses server SDK version 4.x or earlier, see [Test your integration using Amazon GameLift Servers Local](integration-testing-local.md "integration-testing-local.md").

Use an Amazon GameLift Servers Anywhere fleet and your own hardware to iteratively build and test your game
components in a simulated hosted environment. Set up an Anywhere fleet and register a
local device to establish a connection to the Amazon GameLift Servers service. Install your game server
build onto the device, start a game server process, and test game functionality as needed.
You can update your game server build as often as needed to test each new build
iteration.

With an Anywhere fleet, you can test using the AWS CLI or with test scripts. If you've
integrated a game client with Amazon GameLift Servers, you can run the client on the same local device or on a
different device.

Testing locally with an Anywhere fleet is particularly useful for testing your game
server integration with Amazon GameLift Servers. You have full visibility into all hosting activity on the
local machine, as well as events and logging data.

###### Note

Are you using the Amazon GameLift Servers plugin for Unreal Engine or Unity? These tools include guided
workflows for setting up local testing with an Anywhere fleet. Follow the
documentation for [Plugin for Unity: Set up local testing with
Amazon GameLift Servers Anywhere](unity-plug-in-anywhere.md "unity-plug-in-anywhere.md") or [Plugin for Unreal: Host your game locally with
Amazon GameLift Servers Anywhere](unreal-plugin-anywhere.md "unreal-plugin-anywhere.md").

###### Topics

- [Set up a local Anywhere fleet](#integration-testing-anywhere-fleet "#integration-testing-anywhere-fleet")
- [Update and install your game server](#integration-testing-dev "#integration-testing-dev")
- [Test game session activity](#integration-testing-test "#integration-testing-test")
- [Iterate on your game server](#fleet-anywhere-iteration "#fleet-anywhere-iteration")
- [Transition your game to Amazon GameLift Servers managed fleets](#fleet-anywhere-transition "#fleet-anywhere-transition")

## Set up a local Anywhere fleet

Follow these steps to create an Anywhere fleet for your local workstation. For
detailed instructions using either the AWS CLI or the AWS Management Console for Amazon GameLift Servers, see [Create an Amazon GameLift Servers Anywhere fleet](fleets-creating-anywhere.md "fleets-creating-anywhere.md").

###### To create the Anywhere fleet

1. **Create a custom location for your local workstation. (AWS CLI or
   console).** A custom location is simply a label for the compute
   resource you plan to include in your Anywhere fleet. Custom location names
   must start with `custom-`. For example:
   `custom-my_laptop`. See [Create a custom location](fleets-creating-anywhere.md#fleet-anywhere-location "fleets-creating-anywhere.md#fleet-anywhere-location").
2. **Create an Anywhere fleet (AWS CLI or console).** In this
   step, create the fleet resource with the custom location for your local
   workstation. See [Create an Anywhere fleet](fleets-creating-anywhere.md#fleet-anywhere-create "fleets-creating-anywhere.md#fleet-anywhere-create").

Make a note of the new fleet's ID or ARN value. You'll need this value for the
next step. 3. **Register your local workstation as a fleet compute (AWS CLI
only).** An Anywhere fleet must have at least one compute
resource to host your game servers. See
[Add a compute to the fleet](fleets-creating-anywhere.md#fleet-anywhere-compute "fleets-creating-anywhere.md#fleet-anywhere-compute").
To add a compute to the fleet, you need the following information:

    * A compute name. Each compute in a fleet must have a unique
     name.
    * The Anywhere fleet identifier. You can use either the
     `FleetID` or `FleetArn`.
    * The compute's connection info. Specify either an
     `IpAddress` or `DnsName`. This is how
     Amazon GameLift Servers and game clients will connect to game servers.
    * A custom location in the Anywhere fleet.

Make a note of the `GameLiftServiceSdkEndpoint` return value. You'll
need this value when you update your game server to run on an Anywhere
fleet.

## Update and install your game server

This task assumes that you've already integrated a game server build with Amazon GameLift Servers server
SDK 5.x. The integration process involves adding code to your game server so that it can
interact with the Amazon GameLift Servers service to start and manage game sessions.

For an Anywhere fleet, you need to manually configure certain game server settings.
On an Amazon GameLift Servers managed fleet, these settings are configured automatically.

###### To prepare your game server for an Anywhere fleet

1. **Get an authentication token.** Your game server must include an
   authentication token with every communication with the Amazon GameLift Servers service. Amazon GameLift Servers auth
   tokens are short-lived and must be regularly refreshed.

As a best practice, create a script to complete the following tasks:

    * Call the AWS CLI action `get-compute-auth-token`.
    * Store the returned token value where game server processes can retrieve it, such as in an
     environment variable on the local compute.

Install the script with your game server on the compute. Set the script to run
before starting the first game server process. While game server processes are
active, run the script regularly to maintain a valid auth token. All game server
processes on the compute can use the same auth token. 2. **Update your Amazon GameLift Servers game server code.** When you integrated your
game server code with the server SDK for Amazon GameLift Servers, you added a call to the action
`InitSdk()`. When the game server runs on an Anywhere fleet,
this call requires additional server parameters. For more information, see [Initialize the server process](gamelift-sdk-server-api.md#gamelift-sdk-server-initialize "gamelift-sdk-server-api.md#gamelift-sdk-server-initialize") and the [Server SDK 5.x for Amazon GameLift Servers](reference-serversdk.md "reference-serversdk.md") for your
development language. The server parameters are:

    * `webSocketUrl` – Set this parameter to the
     `GameLiftServiceSdkEndpoint` value that is returned when
     you register a compute with the fleet.
    * `hostId` – Set this parameter to the compute name
     that you specifiy when you register a compute with the Anywhere
     fleet.
    * `fleetId` – Set this parameter to the ID of the
     Anywhere fleet.
    * `authToken` – Set this parameter to the token that
     is returned in response to a request to retrieve an authenticaiton token
     for a compute.
    * `processId` – Set this parameter to identify a game
     server process that's running on the local compute. Each concurrent game
     server process must have a unique process ID.

The server parameter values that each game server process uses needs to be
specific to the Anywhere fleet compute where the process is running. For details
on how to get the appropriate values for a compute, see [Add a compute to the fleet](fleets-creating-anywhere.md#fleet-anywhere-compute "fleets-creating-anywhere.md#fleet-anywhere-compute").
As a best practice, set `webSocketUrl`, `hostId`,
`fleetId`, and `authToken` as environment variables on
the local compute. All server processes that run on the compute will use these
values. 3. Install the game server build on the local compute. Include all dependencies needed to run the
game server. 4. Start one or more game server processes running on the local compute. When the game server
process calls the server SDK action `ProcessReady()`, the process is
ready to host a game session.

## Test game session activity

Test your game server integration by working with game sessions. If you don't
have a game client integrated with Amazon GameLift Servers functionality, you can use the AWS
CLI to start game sessions. Try the following scenarios:

- **Create a game session.** Call [create-game-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session.html") command (or the [CreateGameSession](../apireference/API_CreateGameSession.md "../apireference/API_CreateGameSession.md") API operation). Specify your Anywhere fleet's
  ID and custom location. This call returns a unique identifier for the new game
  session.
- **Check game session status.** Call [describe-game-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-sessions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-sessions.html") command (or the [DescribeGameSessions](../apireference/API_DescribeGameSessions.md "../apireference/API_DescribeGameSessions.md") API action). Specify the game session ID. This
  call returns detailed game session information, including the game session
  status. Game sessions in Active status are ready for players to connect. To get
  a list of all game sessions for the fleet, call [list-game-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-sessions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-sessions.html") command (or the [ListGameSessions](../apireference/API_ListGameSessions.md "../apireference/API_ListGameSessions.md") API action).
- **Connect to the game session.** If your game
  client has the ability to join a game session, use the connection information
  included in the game session information.

## Iterate on your game server

You can use the same Anywhere fleet and compute to test other versions
of your game server build.

1. **Clean up your existing
   `GameSession`.** If the game server process crashes or
   won't call `ProcessEnding()`, Amazon GameLift Servers cleans up the
   `GameSession` after the game server stops sending health
   checks.
2. **Generate a new game server build.** Make
   changes to your game server and package an revised build.
3. **Update the game server build on your local
   compute.** Your previous Anywhere fleet is still active and your
   laptop is still registered as a compute resource in the fleet.
4. **Get an updated authorization token.** Call the
   [get-compute-auth-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-compute-auth-token.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-compute-auth-token.html") CLI command and store the token on the local
   compute.
5. **Start one or more game server processes running on the
   local compute.** When the game server process calls
   `ProcessReady()`, it's ready to be used for testing.

## Transition your game to Amazon GameLift Servers managed fleets

After you've completed development testing and you're ready to prepare for launch,
this is a good time to switch over to Amazon GameLift Servers managed fleets. Use managed fleets to
fine-tune and test your game hosting resources. Implement your game session placement
solution (queues and matchmakers), select optimum hosting hardware (including Spot
fleets) and locations, and choose a strategy for scaling capacity. You might also want
to start using AWS CloudFormation to more efficiently manage the life cycles of all your game
hosting resources, including fleets, queues, and matchmakers.

You need to make a few minor modifications to transition from a local Anywhere test
fleet to an Amazon GameLift Servers managed fleet. You can reuse the same queues and matchmakers. Do the
following tasks:

- **Change the game server code call to
  `InitSdk()`.** Remove the server parameters. For a
  managed fleet, Amazon GameLift Servers automatically tracks this information.
- **Create an Amazon GameLift Servers build resource.** With an
  Anywhere test fleet, you have to manually deploy your game server build and
  dependencies to each fleet compute. With a managed fleet, you create and upload
  your game build package to Amazon GameLift Servers, which automatically deploys it to all fleet
  computes. See [Create a game server build for Amazon GameLift Servers](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md") for details on packaging your
  game build files and creating a build resource with files in an Amazon S3 bucket.
  Don't include scripts that register a compute and get an authentication token,
  as Amazon GameLift Servers automatically handles these tasks with managed fleets.
- **Create a managed fleet.** Create a fleet using
  the console or AWS CLI, specifying an EC2 managed fleet. This type of fleet
  requires additional configuration settings, including specifying the build
  resource and instance types. You alls need to set up a runtime configuration to
  manage game server life cycle on each fleet compute. See [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md") for details on
  creating a managed fleet.
- **Redirect fleet aliases (optional).** If you set
  up aliases to use with your Anywhere fleets, you can reuse the same aliases
  for your managed fleets. See [Create an Amazon GameLift Servers alias](aliases-creating.md "aliases-creating.md") for details on creating or updating an
  alias.
