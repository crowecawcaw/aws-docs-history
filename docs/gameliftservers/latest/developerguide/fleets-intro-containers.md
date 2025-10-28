# Amazon GameLift Servers managed container fleets

Amazon GameLift Servers managed container fleets provide cloud-based resources for hosting your
containerized game server software. With a managed container fleet, you get the flexibility,
security, and reliability of AWS Cloud resources, optimized for multiplayer game hosting.
Amazon GameLift Servers provides robust host management tools.

###### Speed up onboarding with these tools for managed containers:

- The [containers starter kit](https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit "https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit") streamlines integration and fleet setup. It
  adds essential game session management features to your game server, and uses
  pre-configured templates to build a container fleet and an automated deployment
  pipeline for your game server. After deployment, use the Amazon GameLift Servers console and API
  tools to monitor fleet performance, manage game sessions, and analyze metrics.
- For Unreal Engine or Unity developers, use the game engine [Amazon GameLift Servers plugins and server SDKs](https://github.com/amazon-gamelift/ "https://github.com/amazon-gamelift/") to integrate your game
  server and build a container fleet from inside your game engine's development
  environment. The plugin's guided workflows help you create a fast, simple
  solution with cloud-based hosting using managed containers. You can build on
  this foundation to create a custom hosting solution for your game.
  A managed container fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances running Linux, which
  Amazon GameLift Servers owns and operates based on your configuration. These instances are physically located
  in supported AWS Regions or Local Zones. When you create a container fleet, you choose an
  EC2 instance type that meets your game server's requirements for computing power, memory,
  storage, networking capabilities.

For a managed container fleet, you store Linux-based container images in an Amazon Elastic Container Registry
(Amazon ECR) repository and create a container group definition to describe your container
architecture. When you create a fleet, Amazon GameLift Servers provisions a fleet instance with the latest
version of the Linux Amazon Machine Image (AMI) and uses the container group definition to
deploy your container images. All instances in a container fleet will use the same AMI
version, even if you update a container group definition or change a container image.

###### Note

As a best practice, we recommend replacing your fleets every 30 days to
maintain a secure and up-to-date runtime environment for your hosted game servers. This
requires creating a new fleet and migrating player traffic to it. For more guidance, see
[Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

After deploying the containerized instance, containers start launching game server
processes. Each game server process establishes a connection to the Amazon GameLift Servers service, reports
readiness to host a game session, and begins communicating health status. Amazon GameLift Servers can then
prompt the server process to start a game session.

In addition to fleet deployment, Amazon GameLift Servers handles the following host management tasks so you
don't have to:

- Tracks the status of all containers in the fleet and replaces stale or unhealthy
  ones.
- Handles authentication for communication between server processes and the Amazon GameLift Servers
  service.
- Offers auto-scaling tools that adjust fleet capacity dynamically to meet player
  demand.
- Reports performance metrics for the fleet's EC2 instances, containers, and server
  processes.
  See these topics about how to set up and maintain managed container fleets:

- [Development roadmap for hosting with Amazon GameLift Servers managed
  containers](gamelift-roadmap-containers.md "gamelift-roadmap-containers.md")
- [Create an Amazon GameLift Servers managed container fleet](containers-build-fleet.md "containers-build-fleet.md")
- [Customize an Amazon GameLift Servers container fleet](containers-design-fleet.md "containers-design-fleet.md")
- [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md")
- [Update an Amazon GameLift Servers managed container fleet](containers-update-fleet.md "containers-update-fleet.md")
