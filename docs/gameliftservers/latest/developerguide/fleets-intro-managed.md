# Amazon GameLift Servers managed EC2 fleets

Amazon GameLift Servers managed EC2 fleets provide cloud-based resources for production hosting. With a
managed fleet, you get the flexibility, security, and reliability of AWS Cloud resources
optimized for multiplayer game hosting. Amazon GameLift Servers provides robust host management tools.

A managed EC2 fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances that Amazon GameLift Servers owns and operates
based on your configuration. These instances are physically located in supported
AWS Regions or Local Zones. When you create a fleet, you choose an EC2 instance type that
meets your game server's requirements for computing power, memory, storage, networking
capabilities.

When starting each instance in the fleet, Amazon GameLift Servers deploys your game server build with the
required runtime environment. The runtime environment uses the latest Amazon Machine Image
(AMI) version available when the fleet is created. All instances in the fleet use the same
AMI version.

###### Note

As a best practice, we recommend replacing your fleets every 30 days to
maintain a secure and up-to-date runtime environment for your hosted game servers. This
requires creating a new fleet and migrating player traffic to it. For more guidance, see
[Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

After installing the runtime environment and your game server build on an instance, Amazon GameLift Servers
starts launching game server processes. Each game server process establishes a connection to
the Amazon GameLift Servers service, reports readiness to host a game session, and begins communicating health
status. Amazon GameLift Servers can then prompt the server process to start a game session.

In addition to fleet deployment, Amazon GameLift Servers handles the following host management tasks so you
don't have to:

- Tracks the status of all computes in the fleet and replaces stale or unhealthy
  computes.
- Handles authentication for communication between server processes and the Amazon GameLift Servers
  service.
- Automatically starts and stops game server processes on each compute, based on
  your runtime configuration.
- Offers auto scaling tools to adjust fleet capacity dynamically to meet player
  demand.
- Reports performance metrics for the fleet's EC2 instances.
  See these topics about how to set up and maintain managed EC2 fleets:

- [Development roadmap for hosting with Amazon GameLift Servers
  managed EC2](gamelift-roadmap-managed.md "gamelift-roadmap-managed.md")
- [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md")
- [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md")
- [Hosting resource customizations](fleets-design.md "fleets-design.md")
- [Update an Amazon GameLift Servers fleet configuration](fleets-editing.md "fleets-editing.md")

## Managed EC2 fleet creation workflow

For managed fleets, Amazon GameLift Servers sets up the fleet resource and also deploys a set of compute
resources with your game server software installed and running. When the creation
workflow is complete and successful, the fleet has one active EC2 instance in the fleet
home Region and one each in the fleet's remote locations. All instances have game are
ready to host game sessions.

1. Amazon GameLift Servers creates the fleet resource in the fleet's home Region and sets desired
   capacity in each location to one (1) instance. Fleet and location status is set to
   **New**.
2. Amazon GameLift Servers begins writing events to the fleet event log.
3. Amazon GameLift Servers sets fleet status to **Downloading** and begins
   preparing the game server software for deployment.
   1. Gets the uploaded game server build and extracts the compressed
      files.
   2. Runs install scripts, if provided.
   3. Sets fleet status to **Validating** and
      begins verifying that no errors occurred when downloading and installing the
      build files.

4. Amazon GameLift Servers sets the fleet status to **Building**,
   configures fleet hardware, and allocates one EC2 instance for each fleet instance.
5. Amazon GameLift Servers sets the fleet status to **Activating**.
   Launches a game server process on each instance (based on the fleet's runtime
   instructions) and tests connectivity between the build and the Amazon GameLift Servers service.
6. When game server processes on each instance establish a connection and report
   readiness to host game sessions, Amazon GameLift Servers sets fleet and location statuses to **Active**. At this point, the fleet is considered ready to
   host game sessions.
