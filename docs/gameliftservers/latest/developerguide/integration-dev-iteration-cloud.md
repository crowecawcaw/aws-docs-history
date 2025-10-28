# Build a cloud-based test

environment

###### Note

This topic covers iterative testing for games that are integrated with the server SDK for Amazon GameLift Servers
version 5.x. If your game uses server SDK version 4.x or earlier, see [Test your integration using Amazon GameLift Servers Local](integration-testing-local.md "integration-testing-local.md").

Use an Amazon GameLift Servers Anywhere fleet to iteratively build and test your game components in a
cloud-based hosted environment. Create an Anywhere fleet with hosting resources and a
connection to the Amazon GameLift Servers service, run your game servers on them, and test game
functionality as needed.

###### Deploy an Anywhere fleet with the Amazon GameLift Servers Agent

If your game server build is integrated with Amazon GameLift Servers SDK 5.x or later, you can deploy it
to a cloud-based Anywhere fleet with the Amazon GameLift Servers Agent. The Agent is a background
process that manages game server life cycles and other tasks on each compute in a fleet.
These tasks include registering the compute with an Anywhere fleet, acquiring an
authentication token, and starting/stopping game server processes based on a set of
instructions. The Agent is controlled by a fleet's runtime configuration, which you can
update at any time during the life of the fleet. (The Agent is automatically deployed to
managed EC2 fleets.) For more information and to download the Agent, see the [Amazon GameLift Servers GitHub
repository](https://github.com/aws/amazon-gamelift-agent "https://github.com/aws/amazon-gamelift-agent").

## Set up iterative testing with Amazon EC2

Use the guided workflow in this [Amazon GameLift Servers toolkit solution](https://github.com/aws/amazon-gamelift-toolkit/tree/main/development-instance-with-amazon-gamelift-anywhere-and-gamelift-agent " https://github.com/aws/amazon-gamelift-toolkit/tree/main/development-instance-with-amazon-gamelift-anywhere-and-gamelift-agent") to set up a cloud-based hosting environment that
mirrors the managed hosting experience with Amazon GameLift Servers.

The GitHub repository provides a set of scripts that automate most of the processes
for setting up a test environment with Amazon GameLift Servers Anywhere and the Amazon GameLift Servers Agent. It also
provides guidance for updating the environment whenever you have a new game server build
to test. You can run a single script that deploys a test environment with a sample game
server build, or you can walk through each step to set it up with your own game server
build.

In this workflow, you'll work entirely in the AWS Management Console, using
AWS CloudShell to run scripts and complete command-line tasks.

###### Note

For the tasks in this tutorial, you need an AWS account user with permissions
for the following services: Amazon GameLift Servers, AWS CloudShell, Amazon S3, AWS Systems Manager, Amazon EC2, and AWS Identity and Access Management.
Users with admin-level access to the AWS account already have the required
permissions.

The workflow covers the following tasks:

- **Package a game server build for Amazon GameLift Servers.** The
  workflow provides a script to build a sample C++ game server, which has already
  been integrated with the server SDK for Amazon GameLift Servers version 5.x and is ready for hosting.
  Alternatively, you can work with your own game project if you've completed
  integration.
- **Set up an Amazon Simple Storage Service bucket to store game server builds
  and dependencies.** As you produce new versions of your game
  builds, you can store them in S3 and use the scripts to update the Anywhere
  fleet for game testing.
- **Get and build the Amazon GameLift Servers Agent.** The Agent manages game server
  processes on a hosting resource based on your configuration. It uses the same
  logic and behaves identically to Amazon GameLift Servers managed EC2 hosting.
- **Set up an Anywhere fleet for your hosting resources.**
  With an Anywhere fleet you can use the Amazon GameLift Servers service for hosting resources
  that aren't managed by Amazon GameLift Servers. In this step, you'll also configure the runtime
  configuration, which instructs Amazon GameLift Servers Agent when and how to start game server
  processes.
- **Set up an Amazon EC2 instance.** This is your test environment for
  iterative testing. It is much faster to use a standard EC2 instance instead of a
  fully managed Amazon GameLift Servers instance (which is optimized for production-level usage).
  With a standard EC2 instance, you can quickly and continually update the game
  server as needed.
- **Deploy your game server build and Amazon GameLift Servers Agent to the
  Amazon EC2 instance.** The workflow provides a script that gets the
  latest version of your game build and all dependencies and installs it on your
  EC2 instance. In this workflow, dependencies include the Amazon GameLift Servers Agent and the
  CloudWatch Agent.
- **Start the Amazon GameLift Servers Agent.** Once installed, the
  Agent automatically starts and begins executing instructions. These include:
  - Register the EC2 instance as a compute in the Amazon GameLift Servers Anywhere fleet.
  - Establish a WebSocket connection with the Amazon GameLift Servers service and get the
    latest runtime configuration.
  - Start up game server processes based on the instructions in the
    runtime configuration. In this workflow, the Agent is instructed to
    start a single process of the game server executable.

- **Test your game scenarios.** With the test
  environment set up and your latest game server build installed, you can commence
  testing. The workflow walks through several steps for testing including starting
  a game session. Access CloudWatch game server logs to track progress as the game
  session starts up and prepares to accept players.

As you develop your game components, including a game client and client-side
backend service, you can include these in your test scenarios. Use a game client
to request a game session, retrieve connection info from the Amazon GameLift Servers service, and
then connect directly to the game session.

- **Deploy a new game server build and repeat tests.** As you
  develop your game, you can generate new game server builds, then quickly deploy
  them to the EC2 test environment for testing. Upload them to the Amazon S3 bucket
  and then use the workflow scripts to update the test environment.

## Transition your game to Amazon GameLift Servers managed

fleets

After you've completed development testing and you're ready to prepare for launch,
this is a good time to switch over to Amazon GameLift Servers managed fleets. Use managed fleets to
fine-tune and test your game hosting resources. Implement your game session placement
solution (queues and matchmakers), select optimum hosting hardware (including Spot
fleets) and locations, and choose a strategy for scaling capacity. You might also want
to start using AWS CloudFormation to more efficiently manage the life cycles of all your game
hosting resources, including fleets, queues, and matchmakers.

It requires minimal effort to transition from a cloud-based Anywhere test fleet to
an Amazon GameLift Servers managed fleet. You don't need to change any game code, and you can reuse the
same queues and matchmakers. Do the following tasks:

- **Create an Amazon GameLift Servers build resource.** With an
  Anywhere test fleet, you have to manually deploy your game server build and
  dependencies to each fleet compute. With a managed fleet, upload your game build
  package to Amazon GameLift Servers, which automatically deploys it to all fleet computes. See
  [Deploy a custom server build for Amazon GameLift Servers
  hosting](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md") for details on packaging your
  game build files and creating a build resource with files in an Amazon S3
  bucket.
- **Create a managed fleet.** Create a fleet using the console or
  AWS CLI, specifying an EC2 managed fleet. This type of fleet requires
  additional configuration settings, including specifying the build resource and
  instance types. You can use the same runtime configuration to manage game server
  life cycle on each fleet compute. See [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md") for details on creating a managed
  fleet.
- **Redirect fleet aliases (optional).** If you set up aliases to
  use with your Anywhere fleets, you can reuse the same aliases for your managed
  fleets. See [Create an Amazon GameLift Servers alias](aliases-creating.md "aliases-creating.md")
  for details on creating or updating an alias.
