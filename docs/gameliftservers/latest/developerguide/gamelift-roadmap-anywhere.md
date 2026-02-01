# Development roadmap for hosting with Amazon GameLift Servers Anywhere

This roadmap guides you through how to develop a hosting solution for your
multiplayer game to use with your own
resources (on-premises hardware or virtual machines). Amazon GameLift Servers offers several game hosting options;
for more information on these
options, see [Amazon GameLift Servers game hosting options](gamelift-intro-flavors.md "gamelift-intro-flavors.md").

With Amazon GameLift Servers Anywhere hosting, your game server is hosted on computing resources that you
supply and manage. You can create an Anywhere fleet with the configurations that you need
and geographically located wherever your players are. Amazon GameLift Servers delivers the following features
for an Anywhere fleet:

- Handles the game session placement process for you based on your configuration,
  including:
  - Tracking game server availability across your Anywhere fleets.
  - Processing game requests from your game client service and matching game
    requests with available servers.
  - Prompting game servers on Anywhere fleets to start game sessions.
  - Communicating connection details back to game clients.

- Collects performance metrics for the session placement process and usage metrics
  for game sessions and players.
- Supports the full FlexMatch matchmaking feature set, so that you can build a
  matchmaker and integrate it with the game session placement system.
- Offers the Amazon GameLift Servers Agent to handle key host management tasks on an Anywhere
  fleet.
- Supports combining with Amazon GameLift Servers managed fleets for a flexible hybrid
  solution.
  An Amazon GameLift Servers Anywhere solution is composed of the following components:

- A game server build, integrated with the server SDK for Amazon GameLift Servers, to deploy across all
  fleets.
- A game client and backend service, integrated with the AWS SDK, to interact with
  the Amazon GameLift Servers service and request game sessions.
- An Amazon GameLift Servers queue or other placement mechanism to place new game sessions with
  available game servers across all fleets.
- (Optional) A FlexMatch matchmaker to create multi-player matches and set up game
  sessions for them.
- One or more Amazon GameLift Servers Anywhere fleets with your on-premises or other hosting
  resources, managed with your existing configuration management and deployment
  tooling. (You can optionally use the AWS Systems Manager.)
  This roadmap presents a streamlined path to getting your multiplayer game up and running
  successfully with Amazon GameLift Servers Anywhere hosting. After you have the necessary components in place,
  you can continue to iterate on game development and customize your hosting solution. As you
  get closer to launch, see these [Prepare for launch with Amazon GameLift Servers hosting](gamelift_quickstart_customservers_checklist.md "gamelift_quickstart_customservers_checklist.md") for help with preparing
  your hosting solution for production-level usage.

###### Get a jump start with the Amazon GameLift Servers plugin for Unreal Engine and Unity

For faster deployment, try the [Amazon GameLift Servers plugin](https://github.com/amazon-gamelift/ "https://github.com/amazon-gamelift/") for Unreal Engine and Unity. It provides
guided UI workflows to quickly deploy your game server with minimal setup, so you can
try out your game components in action.
Then you can build on
this foundation to create a custom hosting solution for your game. For more details, see [Prepare your Unreal or Unity game with the Amazon GameLift Servers plugin](getting-started-plugin.md "getting-started-plugin.md").

Add functionality to your game server so that it can communicate with the Amazon GameLift Servers
service when it's deployed for hosting.

- **Get the server SDK for Amazon GameLift Servers (version
  5.x) for your game project.** The server SDK is
  available in C++, C#, and Go. [Download an Amazon GameLift Servers server
  SDK](https://aws.amazon.com/gamelift/servers/getting-started-sdks/ "https://aws.amazon.com/gamelift/servers/getting-started-sdks/").
- **Modify your game server code to add server SDK
  functionality.** For guidance, see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md"). At a minimum, do the following:
  - Add code to initialize the Amazon GameLift Servers SDK and establish a WebSocket
    connection with the Amazon GameLift Servers service. Use the server SDK action
    `InitSdk()` and include server parameters, which are
    required for an Anywhere fleet.
  - Add code to report to the Amazon GameLift Servers service when the server process is
    ready to host game sessions. Use the server SDK action
    `ProcessReady()`.
  - Implement the required callback functions
    `OnProcessTerminate()`, and
    `OnStartGameSession()`. With these functions, game server
    processes can maintain a connection with the Amazon GameLift Servers service, initiate a
    game session when prompted by Amazon GameLift Servers, and respond to a prompt to end the
    game server process.
  - Add code to report to the Amazon GameLift Servers service when the server process is
    ending a game session. Use the server SDK action
    `ProcessEnding()`.

- **Package your game server build.** Create an
  install script with your build files, dependencies and supporting software. See
  [Package your game build files](gamelift-build-packaging.md "gamelift-build-packaging.md"). We recommend using an Amazon Simple Storage Service
  (Amazon S3) bucket to store versions of your game build.
- **Test your game server integration.** For this
  task, we recommend setting up an Amazon GameLift Servers Anywhere fleet for a local workstation,
  as described in [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md"). For this step, manually install your
  game server build onto the test device and start a server process. Use the AWS
  CLI to request a new game session, and verify that the Amazon GameLift Servers service
  successfully prompts your server process to start a game session.
  Create a way for your game client to request to join a game session, get
  connection info, and then connect directly to a hosted game session. The most common approach
  is to set up backend service functionality that serves as a middleman between your game client and the
  Amazon GameLift Servers service. This approach protects your hosting resources and gives you greater control over how players
  are placed into game sessions.

- **Build backend service functionality for
  hosting.** The backend service communicates with the Amazon GameLift Servers service
  and delivers connection information to a game client. This functionality
  includes starting game sessions, placing players into games, and retrieving game
  session information. For guidance, see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md"). At a minimum, do the
  following:
  - Get the AWS SDK for Amazon GameLift Servers and add it to your backend service
    project. See [Amazon GameLift Servers SDK
    resources for client services](gamelift-supported.md#gamelift-supported-clients "gamelift-supported.md#gamelift-supported-clients").
  - Add code to initialize an Amazon GameLift Servers client and store key
    settings. See [Set up the Amazon GameLift Servers API](gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize "gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize").
  - Add functionality to call the AWS SDK action
    `CreateGameSession()` and provide game session connection
    information to a game client. See [Create a game session on a
    specific fleet](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").

  Calling `CreateGameSession()` is a convenient starting
  point for requesting new game sessions, After you have a game session
  placement system in place (see Step 3), you'll replace this code with a
  call to `StartGameSessionPlacement()` (or
  `StartMatchmaking()` if you're using FlexMatch).

  For guidance on designing your backend service, see
  [Build a backend service for Amazon GameLift Servers](gamelift_quickstart_customservers_designbackend.md "gamelift_quickstart_customservers_designbackend.md").

- **Add functionality to your game client that lets players
  join a hosted game session.** The game client makes requests to
  your backend service, not directly to Amazon GameLift Servers. After the backend service provides
  game session connection information, the game client connects directly with the
  game session to play the game.
- **Test your game client integration.** You can
  use the same Amazon GameLift Servers Anywhere fleet with local workstations for testing.
  Customize how you want Amazon GameLift Servers to process requests for new game session and locate available
  game servers to host them. Amazon GameLift Servers automatically tracks the availability of all game
  servers on all fleets. When a game client sends a request to join a game session, Amazon GameLift Servers
  looks for the "best possible" placement based on a set of defined priorities such as
  minimum latency, cost, and availability.

- **Create a game session queue for placing new game session with
  available game servers.** Queues are the primary mechanism for game
  session placement. For guidance, see [Create a game session queue](queues-creating.md "queues-creating.md").
  - At minimum, add your Anywhere fleets as destinations in your queue.
    All other settings are optional.

- **In your backend service code, convert the
  `CreateGameSession()` call to
  `StartGameSessionPlacement()`.** See [Create a game session in a
  multi-location queue](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").
- **Create a mechanism to notify a game client when a game
  session is ready to join.** While in development, you can poll for
  game session status using a call to DescribeGameSessionPlacement. Before using a
  queue to process high volumes, however, you'll need to enable event
  notifications. See [Set up event notification for game session
  placement](queue-notification.md "queue-notification.md").
- (Optional) **Add FlexMatch matchmaking components.**
  For guidance, see the [Amazon GameLift Servers FlexMatch
  developer guide](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md").
  Up to this point you've been working with local devices (registered as Anywhere
  fleet computes) to test and iterate on your game components. The next step is to set
  up the type of fleet you'll need for a production system. For these resources, use
  the Amazon GameLift Servers Agent to manage some key on-compute host management tasks. For more
  details, see [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md "integration-dev-iteration-agent.md").

- **Get the Amazon GameLift Servers Agent and add it to your game server
  install package.** Get and build the Agent source code, available
  in the [Amazon GameLift Servers Agent
  Github repository](https://github.com/aws/amazon-gamelift-agent "https://github.com/aws/amazon-gamelift-agent"). Place the resulting JAR file executable into the
  same directory as your game build executable.
- **Modify your startup script for the Agent as
  needed.** Ensure that Agent executable launches as soon as a
  compute starts running. See the readme file in the Agent repo for help with
  installing and running the Agent on your hosting computes. Your launch command
  should include options to specify, at minimum, the Anywhere fleet ID and
  AWS Region, a custom location, and a compute name.

The Agent automatically handles the following tasks for you, so if you've been
handling these tasks with scripts, you can remove them:

    + Calls `RegisterCompute()` to add the compute to an Anywhere
     fleet.
    + Calls `GetComputeAuthToken()` to authenticate game servers
     when they connect to the Amazon GameLift Servers service. The Agent manages getting and
     refreshing the auth token, which can be used by all game server
     processes that are running on the compute.
    + Starts new server processes on the compute based on a set of runtime
     instructions.

- **Create a runtime configuration for computes in your
  Anywhere fleet.** You can use the Amazon GameLift Servers console or the AWS CLI
  to create or modify runtime instructions for the fleet. The Agent carries out
  these instructions and periodically requests updates from the Amazon GameLift Servers service.
- **Set up or modify your game session queue as
  needed.** Create a new queue (or update an existing one) to use the
  Anywhere fleets that are deployed with the Amazon GameLift Servers Agent.
- **Test the Agent integration with your Anywhere fleets.** Check that the Agent is properly starting server processes based on
  the runtime configuration.
  As you prepare for game launch, you'll need to fine-tune your managed hosting
  resources. Some of the decisions to consider include:

- Automate the process of starting and shutting down computes as needed,
  including installing and running game server software. Recycling computes is
  useful to ensure that they are updated regularly, and shutting down computes
  can save costs when they're not needed.
- If your game server needs to communicate other AWS resources, set up IAM
  roles to manage access. See [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").
- Determine where geographically you want to position game servers. Add
  remote locations to your managed fleets. See [Hosting resource customizations](fleets-design.md "fleets-design.md").
- Optimize fleet performance by selecting compute resource configurations,
  then configure the runtime instructions to run an optimal number of server
  processes per compute.
- Experiment with game session placement options for managed fleets,
  including customizing prioritization settings. See [Customize a game session queue](queues-design.md "queues-design.md").
- Create mechanisms to handle manual or automated capacity scaling to meet
  expected player demand. Consider what factors should prompt the system to
  increase or decrease the number of computes that are available to host game
  sessions.
- Design and implement failover to other resources if needed.
- Set up hosting observability tools, including analytics and logging. See
  [Monitoring Amazon GameLift Servers](monitoring-overview.md "monitoring-overview.md").
