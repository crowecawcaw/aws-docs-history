# Development roadmap for hybrid hosting

with Amazon GameLift Servers

This roadmap guides you through how to develop a hosting solution for your multiplayer
game. Amazon GameLift Servers offers several game hosting options; for more information on these
options, see [Amazon GameLift Servers game hosting options](gamelift-intro-flavors.md "gamelift-intro-flavors.md").

A hybrid solution uses a combination of hosting resources, including cloud-based
resources managed by Amazon GameLift Servers and your own self-managed hosting resources. For a more
detailed discussion of hybrid hosting, see this article: [Hybrid game server hosting with Amazon GameLift Servers Anywhere](https://aws.amazon.com/blogs/gametech/hybrid-game-server-hosting-with-amazon-gamelift-anywhere/ "https://aws.amazon.com/blogs/gametech/hybrid-game-server-hosting-with-amazon-gamelift-anywhere/"). With Amazon GameLift Servers, you
can set up a hybrid solution that uses common components and processes, so you can
centrally manage a global fleet and easily move loads between all types of
resources.

A hybrid architecture consists of the following components:

- A single game server build, integrated with the server SDK for Amazon GameLift Servers, to
  deploy across all fleets.
- A single game client and backend service, integrated with the AWS
  SDK, to interact with the Amazon GameLift Servers service and request game
  sessions.
- A shared Amazon GameLift Servers queue to place new game sessions with available game
  servers and balance load across all fleets.
- (Optional) A process manager agent, which is deployed with an Anywhere
  fleet, to simplify server process management tasks across computes
  in all fleets.
- (Optional) A FlexMatch matchmaker to create multi-player matches and set
  up game sessions for them.
- One or more Amazon GameLift Servers managed fleets, which use Amazon Elastic Compute Cloud (Amazon EC2)
  instances optimized for multiplayer game hosting.
- One or more Amazon GameLift Servers Anywhere fleets, which use your existing on-premises
  or other hosting resources, including your configuration management
  and deployment tooling. (You can optionally use the
  AWS Systems Manager.)
  This roadmap presents a streamlined path to getting your multiplayer game up and
  running successfully in a hybrid hosting solution with Amazon GameLift Servers. After you have the
  necessary components in place, you can continue to iterate on game development and
  customize your hosting solution. As you get closer to launch, see these [Prepare for launch with Amazon GameLift Servers hosting](gamelift_quickstart_customservers_checklist.md "gamelift_quickstart_customservers_checklist.md") for help with
  preparing your hosting solution for production-level usage.

###### Get a jump start with the Amazon GameLift Servers plugin

If you're developing projects with Unreal Engine or Unity, start setting up
your game for hosting with the Amazon GameLift Servers plugin. With the plugin, you can add
the Amazon GameLift Servers SDKs to your game project and use the guided workflows to build a
simple working version of a hybrid hosting solution with both an Anywhere
fleet and an Amazon GameLift Servers managed fleet. You can then use these fundamentals to
build on and customize as needed.

Add functionality to your game server so that it can communicate with
the Amazon GameLift Servers service when it's deployed for hosting. The same
functionality is required if the game server is running on an Amazon GameLift Servers
managed fleet or an Anywhere fleet.

- **Get the server SDK for Amazon GameLift Servers (version 5.x) for your
  game project.** The server SDK is
  available in C++, C#, and Go. [Download the
  server SDK for Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/getting-started-sdks/ "https://aws.amazon.com/gamelift/servers/getting-started-sdks/").
- **Modify your game server code to
  add server SDK functionality.** For
  guidance, see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md"). At a
  minimum, do the following:
  - Add code to initialize the Amazon GameLift Servers SDK and
    establish a WebSocket connection with the Amazon GameLift Servers
    service. Use the server SDK action
    `InitSdk()`. Include code to specify
    server parameters when running on an Anywhere
    fleet compute.
  - Add code to report to the Amazon GameLift Servers service when
    the server process is ready to host game sessions.
    Use the server SDK action
    `ProcessReady()`.
  - Implement the required callback functions
    `OnProcessTerminate()`, and
    `OnStartGameSession()`. With these
    functions, game server processes can maintain a
    connection with the Amazon GameLift Servers service, initiate a game
    session when prompted by Amazon GameLift Servers, and respond to a
    prompt to end the game server process.
  - Add code to report to the Amazon GameLift Servers service when
    the server process is ending a game session. Use
    the server SDK action
    `ProcessEnding()`.

- **Package your game server
  build.** Create an install script with
  your build files, dependencies and supporting
  software. See [Package your game build files](gamelift-build-packaging.md "gamelift-build-packaging.md"). We
  recommend using an Amazon Simple Storage Service (Amazon S3) bucket to store
  versions of your game build.
- **Test your game server
  integration.** For this task, we
  recommend setting up an Amazon GameLift Servers Anywhere fleet with a
  local workstation, as described in [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md"). For this
  step, manually install your game server build onto
  the test device and start a server process. Use the
  AWS CLI to request a new game session, and verify
  that the Amazon GameLift Servers service successfully prompts your
  server process to start a game session.
  Create a way for your game client to request to join a game session,
  get connection info, and then connect directly to a hosted game
  session. The most common approach is to set up backend service
  functionality that serves as a middleman between your game client
  and the Amazon GameLift Servers service. This approach protects your hosting resources
  and gives you greater control over how players are placed into game
  sessions.

- **Build backend service
  functionality for hosting.** The backend
  service communicates with the Amazon GameLift Servers service and
  delivers connection information to a game client.
  This functionality includes starting game sessions,
  placing players into games, and retrieving game
  session information. For guidance, see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md"). At a
  minimum, do the following:
  - Get the AWS SDK for Amazon GameLift Servers and add it
    to your backend service project. See [Amazon GameLift Servers SDK
    resources for client services](gamelift-supported.md#gamelift-supported-clients "gamelift-supported.md#gamelift-supported-clients").
  - Add code to initialize an Amazon GameLift Servers
    client and store key settings. See [Set up the Amazon GameLift Servers API](gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize "gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize").
  - Add functionality to call the AWS SDK
    action `CreateGameSession()` and
    provide game session connection information to a
    game client. See [Create a
    game session on a specific fleet](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").

  Calling `CreateGameSession()` is
  a convenient starting point for requesting new
  game sessions, After you have a game session
  placement system in place (see Step 3), you'll
  replace this code with a call to
  `StartGameSessionPlacement()` (or
  `StartMatchmaking()` if you're using
  FlexMatch).

  For guidance on designing your backend
  service, see [Build a backend service for Amazon GameLift Servers](gamelift_quickstart_customservers_designbackend.md "gamelift_quickstart_customservers_designbackend.md").

- **Add functionality to your game
  client that lets players join a hosted game
  session.** The game client makes requests
  to your backend service, not directly to Amazon GameLift Servers.
  After the backend service provides game session
  connection information, the game client connects
  directly with the game session to play the game.
- **Test your game client
  integration.** You can use the same
  Amazon GameLift Servers Anywhere fleet with a local workstation for
  testing.

During the development phase, if you want to test how
your game build behaves in an Amazon GameLift Servers managed fleet,
we recommend that you also set up a [cloud-based test environment](integration-dev-iteration-cloud.md "integration-dev-iteration-cloud.md"). This Amazon GameLift Servers
Toolkit solution mimics the behavior of a managed
fleet but lets you update game server builds with
minimal turnaround time.
Customize how you want Amazon GameLift Servers to process requests for new game session
and locate available game servers to host them. Amazon GameLift Servers automatically
tracks the availability of all game servers on all fleets. When a
game client sends a request to join a game session, Amazon GameLift Servers looks for
the "best possible" placement based on a set of defined priorities
such as minimum latency, cost, and availability.

- **Create a game session queue for
  placing new game session with available game
  servers.** Queues are the primary
  mechanism for game session placement. For guidance,
  see [Create a game session queue](queues-creating.md "queues-creating.md").
  - At minimum, add your Anywhere fleets as
    destinations in your queue. All other settings are
    optional customizations.

- **In your backend service code,
  convert the `CreateGameSession()` call
  to
  `StartGameSessionPlacement()`.**
  See [Create a game session in a multi-location
  queue](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").
- **Create a mechanism to notify a
  game client when a game session is ready to
  join.** While in development, you can
  poll for game session status using a call to
  DescribeGameSessionPlacement. Before using a queue
  to process high volumes, however, you'll need to
  enable event notifications. See [Set up event notification for game session
  placement](queue-notification.md "queue-notification.md").
- (Optional) **Add FlexMatch
  matchmaking components.** For guidance,
  see the [Amazon GameLift Servers FlexMatch developer guide](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md").
  Up to this point you've been working with local devices (registered as
  Anywhere fleet computes) to test and iterate on your game
  components. The next step is to set up the type of fleets you'll
  need for a production system. Start with an Anywhere fleet, and add
  the Amazon GameLift Servers Agent to manage some key on-compute host management tasks.
  For more details, see [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md "integration-dev-iteration-agent.md").

- **Get the Amazon GameLift Servers Agent and add it
  to your game server install package.**
  Get and build the Agent source code, available in
  the [Amazon GameLift Servers Agent Github repository](https://github.com/aws/amazon-gamelift-agent "https://github.com/aws/amazon-gamelift-agent"). Place the
  resulting JAR file executable into the same
  directory as your game build executable.
- **Modify your startup script for
  the Agent as needed.** Ensure that Agent
  executable launches as soon as a compute starts
  running. See the readme file in the Agent repo for
  help with installing and running the Agent on your
  hosting computes. Your launch command should include
  options to specify, at minimum, the Anywhere fleet
  ID and AWS Region, a custom location, and a
  compute name.

The Agent automatically handles the following tasks
for you, so if you've been handling these tasks with
scripts, you can remove them:

    + Calls `RegisterCompute()` to add
     the compute to an Anywhere fleet.
    + Calls `GetComputeAuthToken()` to
     authenticate game servers when they connect to the
     Amazon GameLift Servers service. The Agent manages getting and
     refreshing the auth token, which can be used by
     all game server processes that are running on the
     compute.
    + Starts new server processes on the compute
     based on a set of runtime instructions.

- **Create a runtime configuration
  for computes in your Anywhere fleet.**
  At minimum, specify the launch path for your game
  server executable. You can use the Amazon GameLift Servers console or
  the AWS CLI to create or modify runtime
  instructions for the fleet. The Agent carries out
  these instructions and periodically requests updates
  from the Amazon GameLift Servers service.
- **Set up or modify your game
  session queue as needed.** Create a new
  queue (or update an existing one) and designate a
  destination for the Anywhere fleet deployed with the
  Amazon GameLift Servers Agent.
- **Test the Agent integration with
  your Anywhere fleets.** Check that the
  Agent is properly starting server processes based on
  the runtime configuration.
  Create an Amazon GameLift Servers managed EC2 fleet to supplement your Anywhere fleet.
  If you set up a cloud-based test environment in Step 2 to speed up
  development, plan to create a managed fleet after you've completed
  most of your game development and testing. You need a fully managed
  fleet to configure and test additional settings such as automatic
  capacity scaling.

- **Package your game server build
  and upload to Amazon GameLift Servers.** Create an install
  script with your build files, dependencies and
  supporting software. You can use the same build
  software with both your Anywhere and managed fleets.
  See [Create a game server build for Amazon GameLift Servers](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md").
  You can upload your build to Amazon GameLift Servers using either the
  console or the AWS CLI.

Before uploading your build, decide in what
AWS Region you want to create the managed fleet.
You must upload the build to the same Region. For
more on choosing a fleet location, see [Geographic locations](gamelift-compute.md#gamelift-compute-location "gamelift-compute.md#gamelift-compute-location").

- **Create a managed EC2
  fleet.** You can use the Amazon GameLift Servers console or
  the AWS CLI to create a managed fleet. When you
  create a fleet, Amazon GameLift Servers immediately begins deploying
  your game server build for hosting. You can
  configure many aspects of a managed fleet. For
  guidance, see [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md"). At minimum, do
  the following:
  - Give the fleet a name and specify which
    uploaded game build to deploy.
  - Choose On-Demand Instances for your fleet
    and select an instance type that's available in
    your fleet location. Spot fleets are a valuable
    option but require additional design and
    configuration.
  - Create a runtime configuration with similar
    settings as you used with the Anywhere fleet. At
    minimum, specify the launch path for your game
    server executable.
  - Specify port settings to allow inbound
    traffic to access your game servers.

- **Add the managed fleet to your
  shared game session queue.** Update the
  queue from Step 4 so that it includes destinations
  for both the managed fleet and the Anywhere fleet
  deployed with the Amazon GameLift Servers Agent.
- **Test game hosting with your
  managed fleets.** At this point you
  should be able to test the entire hosting cycle,
  with a game client requesting a game session,
  getting connection info, and successfully connecting
  to a game session.
  As you prepare for game launch, you'll need to fine-tune your hosting
  solutions. Some of the decisions to consider include:

- For Anywhere fleets, automate the process of starting
  and shutting down computes as needed, including
  installing and running game server software.
  Recycling computes is useful to ensure that they are
  updated regularly, and shutting down computes can
  save costs when they're not needed.
- If your game server needs to communicate other AWS
  resources, set up IAM roles to manage access. See
  [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").
- Determine where geographically you want to position
  game servers. Add remote locations to your managed
  fleets. See [Hosting resource customizations](fleets-design.md "fleets-design.md").
- For managed fleets, consider using Spot fleets for
  cost savings. See [Reduce game hosting costs with Spot fleets](fleets-spot.md "fleets-spot.md") .
- Optimize fleet performance by selecting compute
  resource configurations, then configure your the
  runtime instructions to run the optimal number of
  server processes per compute. Do this for both
  Anywhere fleets and managed fleets. See [Optimize game server runtime configuration on managed Amazon GameLift Servers](fleets-multiprocess.md "fleets-multiprocess.md").
- Experiment with game session placement options for
  managed fleets, including customizing prioritization
  settings. See [Customize a game session queue](queues-design.md "queues-design.md").
- For managed fleets, set up automatic capacity scaling
  to meet expected player demand. See [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md").
- For Anywhere fleets, create mechanisms to handle
  manual or automated capacity scaling to meet
  expected player demand.
- Design and implement failover to other resources if
  needed. Set up standby fleets in other AWS Regions
  and modify queues and auto scaling to handle
  failovers if needed.
- Set up hosting observability tools, including
  analytics and logging. See [Monitoring Amazon GameLift Servers](monitoring-overview.md "monitoring-overview.md"). Create
  metric groups to aggregate analytics for all your
  hosting resources.
- Automate your deployment using [infrastructure as code (IaC)](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md"). See [Manage Amazon GameLift Servers hosting resources using AWS CloudFormation](resources-cloudformation.md "resources-cloudformation.md").

Amazon GameLift Servers supports the use of AWS CloudFormation templates for any
deployment-specific configurations. You can also use
the AWS Cloud Development Kit (AWS CDK) to define your Amazon GameLift Servers resources. For
more information about the AWS CDK, see the [AWS Cloud Development Kit (AWS CDK) Developer Guide](../../../cdk/v2/guide.md "../../../cdk/v2/guide.md").

To manage the deployment of your AWS CloudFormation stacks, we
recommend using continuous integration and
continuous delivery (CI/CD) tools and services such
as AWS CodePipeline. These tools help you deploy
automatically or with approval whenever you build
game server binary. With a CI/CD tool or service,
resources deployment for a new game server version
can look like this:

    + Build and test your game server
     binary.
    + Upload the binary to Amazon GameLift Servers.
    + Deploy new fleets with the new build.
    + Add the new fleets to your game session
     queue and remove the fleets with the previous
     build version.
    + When the fleets with the previous build are
     no longer hosting active game sessions, delete the
     AWS CloudFormation stacks of those fleets.
