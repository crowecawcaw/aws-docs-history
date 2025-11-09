# Development roadmap for hosting with Amazon GameLift Servers managed

containers

This roadmap guides you through how to develop an Amazon GameLift Servers managed hosting solution for your
containerized game servers. Managed containers is just one hosting solution that is offered
by Amazon GameLift Servers. For more information on hosting options, see [Amazon GameLift Servers game hosting options](gamelift-intro-flavors.md "gamelift-intro-flavors.md").

A managed container solution with Amazon GameLift Servers has the following components:

- A container image with your game server build, uploaded to Amazon Elastic Container Registry (Amazon ECR) private
  repository. The game server build is integrated with the server SDK for Amazon GameLift Servers and built to run
  on Linux.
- A backend service that interacts with the Amazon GameLift Servers service on behalf of your game clients.
  The backend service uses functionality in the service API for Amazon GameLift Servers, which is part of the AWS
  SDK.
- An Amazon GameLift Servers game session queue or other placement mechanism that processes requests for new
  game sessions, searches for available game servers across all fleets, and prompts a
  game server to start a game session.
- (Optional) A FlexMatch matchmaker to create multi-player matches and set up game sessions
  for them.
- One or more container fleets, which use Amazon Elastic Compute Cloud (Amazon EC2) instances and are
  optimized for multiplayer game hosting.
  This roadmap presents a streamlined path to getting your containerized game servers up and
  running successfully with Amazon GameLift Servers managed containers. After you have the necessary components in
  place, you can continue to iterate on game development and customize your hosting solution. As
  you get closer to launch, see these [Prepare for launch with Amazon GameLift Servers hosting](gamelift_quickstart_customservers_checklist.md "gamelift_quickstart_customservers_checklist.md") for help with preparing your
  hosting solution for production-level usage.

###### Speed up onboarding with these tools for managed containers:

- The [containers starter kit](https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit "https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit") streamlines integration and fleet setup. It
  adds essential game session management features to your game server, and uses
  pre-configured templates to build a container fleet and an automated deployment
  pipeline for your game server. After deployment, use the Amazon GameLift Servers console and API
  tools to monitor fleet performance, manage game sessions, and analyze metrics.
- For Unreal Engine and Unity developers, use the [Amazon GameLift Servers plugins](https://github.com/amazon-gamelift/ "https://github.com/amazon-gamelift/") to integrate your game
  server and build a container fleet from inside your game engine's development
  environment. The plugin's guided workflows help you create a fast, simple
  solution with cloud-based hosting using managed containers. You can build on
  this foundation to create a custom hosting solution for your game.
  Add functionality to your game server so that it can communicate with the Amazon GameLift Servers
  service when it's deployed for hosting.

- **Get the server SDK for Amazon GameLift Servers (version 5.2 or greater) for
  your game project.** The server SDK is available in C++, C#,
  and Go. [Download the server SDK for Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/getting-started-sdks/ "https://aws.amazon.com/gamelift/servers/getting-started-sdks/"). The server SDK is available in
  C++, C#, and Go.
- **Modify your game server code to add server SDK
  functionality.** For guidance, see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md"). At a minimum, do the following:
  - Add code to initialize the Amazon GameLift Servers SDK and establish a WebSocket
    connection with the Amazon GameLift Servers service. Use the server SDK action
    `InitSdk()`.
  - Add code to report to the Amazon GameLift Servers service when the server process is
    ready to host game sessions. Use the server SDK action
    `ProcessReady()`.
  - Implement the required callback functions
    `OnStartGameSession()`, and `OnProcessTerminate()`. With these functions, game server processes
    can maintain a connection with the Amazon GameLift Servers service, initiate a game session when
    prompted by Amazon GameLift Servers, and respond to a request to end the game server process.
  - Add code to report to the Amazon GameLift Servers service when the server process is
    ending a game session. Use the server SDK action
    `ProcessEnding()`.

- **Package your game server build.** Build your
  game server to run on Linux. Prepare the build and other files that are
  needed to run the game server. If you’re developing on Windows, this step
  might involve setting up a separate Linux workspace or using a tool such as
  Windows subsystem for Linux (WSL). You'll need a Linux environment to test
  your game server build, and also to build and test your container
  images.
- **Test your game server integration.** Verify
  that your integrated game server can connect to the Amazon GameLift Servers service and
  respond to prompts. We recommend setting up a simple Amazon GameLift Servers Anywhere fleet
  with a local workstation as a test host, as described in [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md").
  Install your game server build onto the test host and start a server
  process. Use the AWS CLI to request a new game session, and verify that
  the Amazon GameLift Servers service successfully prompts your server process to start a game
  session.
  After you've successfully integrated your game server, create a container image
  with your game server executable. Store it in an Amazon Elastic Container Registry (Amazon ECR) repository for
  use with Amazon GameLift Servers. For detailed instructions, see [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md").

- **Get the Dockerfile template for a game server
  container (provided by Amazon GameLift Servers).** Modify the file for your game
  server build files.
- **Build a game server container image.**
  Working in a Linux environment, use the Docker tool to create your
  image.
- **Push your container image to Amazon ECR.**
  Create a public or private repository in Amazon ECR, using the same AWS account
  and AWS Region where you plan to deploy your container fleet. Push your
  container image to it.
- **Test your container images using your Anywhere
  fleet (optional).** You might want to test your container
  images locally before deploying them to a cloud-hosted container fleet. You
  can use your existing Amazon GameLift Servers Anywhere fleet with a local workstation for
  testing. Install and run the game server container and verify that: (1) the
  Amazon GameLift Servers service successfully prompts your server process to start a game
  session, and (2) a game client can connect to the game session.
  Up to this point you've worked with a self-managed Anywhere fleet to test and
  iterate on your game components. When you have a working game server build that's integrated
  for Amazon GameLift Servers, you can start setting up the
  cloud-based Amazon GameLift Servers managed
  container fleet hosting resources that you'll need for a production environment.

- **Create container group definitions.** Container
  group definitions describe the container architecture for a fleet. and
  identify which container images to deploy. See [Create a container group definition for an Amazon GameLift Servers
  container fleet](containers-create-groups.md "containers-create-groups.md"). Create your container group
  definition in the same AWS Region where the container images are stored.
  For more on choosing a fleet location, see [Geographic locations](gamelift-compute.md#gamelift-compute-location "gamelift-compute.md#gamelift-compute-location"). At a minimum, do the
  following:
  - Create a game server container group definition.
  - Add a container definition with a container image with your game
    server build.
  - Configure a port range for the container's game server
    processes.

- **Create a managed container fleet.** When you
  create a fleet, Amazon GameLift Servers immediately begins deploying your game server build
  for hosting. You can configure many aspects of a managed fleet. For
  guidance, see [Create an Amazon GameLift Servers managed container fleet](containers-build-fleet.md "containers-build-fleet.md"). At minimum, do the following:
  - Set up an AWS Identity and Access Management (IAM) service role for the container fleet. See
    [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md").
  - Specify the game server container group definition to deploy to fleet
    instances.
  - Use default values where available for all other parameters. Amazon GameLift Servers
    calculates some parameters for optimal configuration.

- **Add the container fleets to your queue.** In
  your game session queue, replace the Anywhere test fleet with your managed
  container fleet.
- **Test game hosting with your container fleets.**
  At this point you should be able to test the entire solution. Start a game
  client and request a game session through the backend service. Get
  connection info and connect to a game session on the container fleet.
- **Iterate on your fleet deployments.** You
  can update container group definitions and fleet configurations, and then
  deploy updates to existing fleets.
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
- **Test your game client integration.** You can use your
  existing Amazon GameLift Servers Anywhere fleet with a local workstation for testing. Use the
  new backend service to request a new game session, and verify that: (1) the
  Amazon GameLift Servers service successfully prompts your server process to start a game
  session, and (2) a game client can connect to the game session.
  Customize how you want Amazon GameLift Servers to process requests for new game session and locate available
  game servers to host them. Amazon GameLift Servers automatically tracks the availability of all game
  servers on all fleets. When a game client sends a request to join a game session, Amazon GameLift Servers
  looks for the "best possible" placement based on a set of defined priorities such as
  minimum latency, cost, and availability.

- **Create a game session queue for placing new game session with
  available game servers.** Queues are the primary mechanism for game
  session placement. For guidance, see [Create a game session queue](queues-creating.md "queues-creating.md").
  - At minimum, add your Anywhere fleets as destinations in your queue.
    All other settings are optional customizations.

- **In your backend service code, convert the
  `CreateGameSession()` call to
  `StartGameSessionPlacement()`.** See [Create a game session in a
  multi-location queue](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").
- **Create a mechanism to notify a game client when a game
  session is ready to join.** While in development, you can poll
  for game session status using a call to
  `DescribeGameSessionPlacement`. Before using a queue to
  process high volumes, however, you'll need to enable event notifications.
  See [Set up event notification for game session
  placement](queue-notification.md "queue-notification.md").
- **Add FlexMatch matchmaking (optional).** Build a
  matchmaking rule set and create a matchmaking configuration to work with
  your game session queue. For guidance on setting up a matchmaking system,
  see the [Amazon GameLift Servers FlexMatch
  developer guide](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md").
- **Test the placement system.** You can use
  your existing Amazon GameLift Servers Anywhere fleet with a local workstation for testing. Use
  the backend service to request a new game session, and verify that the Amazon GameLift Servers
  service successfully prompts your server process to start a game
  session.
  As you prepare for game launch, you'll need to fine-tune your managed hosting
  resources. Some of the decisions to consider include:

- Optimize your container fleet configuration.
  See [Customize an Amazon GameLift Servers container fleet](containers-design-fleet.md "containers-design-fleet.md").
- Consider adding Spot fleets for cost savings. See [Reduce game hosting costs with Spot fleets](fleets-spot.md "fleets-spot.md") .
- If your game server needs to communicate other AWS resources, set up
  IAM roles to manage access. See [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").
- Determine where geographically you want to position game servers. Add remote locations to your
  managed fleets. See [Hosting resource customizations](fleets-design.md "fleets-design.md").
- Experiment with game session placement options for managed fleets, including customizing
  prioritization settings. See [Customize a game session queue](queues-design.md "queues-design.md").
- Set up automatic capacity scaling to meet expected player demand. See
  [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md").
- Create fleets in other AWS Regions and modify queues and auto scaling to
  handle failovers as needed.
- Set up hosting observability tools, including analytics and logging. See [Monitoring Amazon GameLift Servers](monitoring-overview.md "monitoring-overview.md").
- Automate your fleet deployments using [infrastructure as code (IaC)](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md"). See [Manage Amazon GameLift Servers hosting resources using AWS CloudFormation](resources-cloudformation.md "resources-cloudformation.md").

Amazon GameLift Servers supports the use of AWS CloudFormation templates for any deployment-specific
configurations. You can also use the AWS Cloud Development Kit (AWS CDK) to define your Amazon GameLift Servers
resources. For more information about the AWS CDK, see the [AWS Cloud Development Kit (AWS CDK) Developer Guide](../../../cdk/v2/guide.md "../../../cdk/v2/guide.md").

To manage the deployment of your AWS CloudFormation stacks, we recommend using
continuous integration and continuous delivery (CI/CD) tools and services
such as AWS CodePipeline. These tools help you deploy automatically or with
approval whenever you build game server binary. With a CI/CD tool or
service, resources deployment for a new game server version can look like
this:

    + Build and test your game server binary.
    + Upload the binary to Amazon GameLift Servers.
    + Deploy new fleets with the new build.
    + Add the new fleets to your game session queue and remove the fleets with
     the previous build version.
    + When the fleets with the previous build are no longer hosting active game
     sessions, delete the AWS CloudFormation stacks of those fleets.
