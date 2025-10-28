# Server SDK 5.x for Amazon GameLift Servers

This section provides reference documentation for the server SDK 5.x for Amazon GameLift Servers. The server
SDK provides core functionality that your game server uses to interact with the Amazon GameLift Servers
service. For example, your game server receives prompts from the service to start and stop
game sessions and it provides regular game session status updates to the service. Integrate
your game servers with the server SDK before you deploy them for hosting.

Use this server SDK reference to integrate your custom multiplayer game servers
for hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").

The latest major version of the server SDK for Amazon GameLift Servers is 5.x. The following hosting features require
the use of version 5.x:

- Amazon GameLift Servers Anywhere
- Amazon GameLift Servers plugin for Unreal Engine and Unity

###### Note

If you need to use server SDK version 4.x or earlier, see [Server SDK for Amazon GameLift Servers version 4 and
earlier](reference-serversdk4.md "reference-serversdk4.md") for documentation and download information.

###### Topics

- [Updates in server SDK 5 for Amazon GameLift Servers](#reference-serversdk5-about "#reference-serversdk5-about")
- [Migrate to server SDK 5.x for
  Amazon GameLift Servers](reference-serversdk5-migration.md "reference-serversdk5-migration.md")
- [C++ server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-cpp-actions.md "integration-server-sdk5-cpp-actions.md")
- [C# server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")
- [Go server SDK for Amazon GameLift Servers --
  Actions](integration-server-sdk-go-actions.md "integration-server-sdk-go-actions.md")
- [C++ (Unreal) server SDK 5.x for
  Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")

## Updates in server SDK 5 for Amazon GameLift Servers

Your hosted game servers use the server SDK for Amazon GameLift Servers to communicate with the Amazon GameLift Servers
service to start and manage game sessions for players. The latest version, Amazon GameLift Servers server
SDK 5, offers a number of improvements and support for new Amazon GameLift Servers features. If your game
server build currently uses Amazon GameLift Servers server SDK 4 or earlier, follow the guidance in this
topic to update your games.

Amazon GameLift Servers server SDK version 5.0.0 and above includes these updates:

- Expanded languages – Libraries are available in the following
  languages: C++, C#, Go. You can build the C++ libraries for use with Unreal
  Engine.
- Game engine plugin support – The Amazon GameLift Servers standalone plugins for Unreal
  Engine and Unity require Amazon GameLift Servers server SDK 5 libraries. These plugins offer
  guided workflows for integrating, testing, and deploying your games to Amazon GameLift Servers
  for hosting. See [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md")
  and [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md")
  documentation.
- Amazon GameLift Servers Anywhere support – With Anywhere fleets you can set up your own
  hosting resources to use Amazon GameLift Servers features (including matchmaking). Add the
  Amazon GameLift Servers Agent to automate game session life cycle management. Use Anywhere
  fleets for production hosting with on- premises hardware, or set up test
  environments for fast iterative game development. See [Anywhere
  hosting](gamelift-intro-flavors.md#gamelift-intro-flavors-hosting-anywhere "gamelift-intro-flavors.md#gamelift-intro-flavors-hosting-anywhere") and the [Amazon GameLift Servers
  Agent](https://github.com/aws/amazon-gamelift-agent "https://github.com/aws/amazon-gamelift-agent").
- Updated testing tools – The Amazon GameLift Servers Anywhere feature lets you set up local or cloud-based
  test environments for your games. Set up testing with or without the Amazon GameLift Servers
  Agent. These tools replace Amazon GameLift Servers Local. See [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md").
- Consolidated .NET solution for C# – The C# server SDK 5.1+ supports .NET
  Framework 4.6.2 (upgraded from 4.6.1) and .NET 6.0 in a single solution. .NET
  Standard 2.1 is available with the Unity-built libraries.
- New `Compute` resource – This new resource combines
  different types of hosting resources. It includes cloud-based hosting resources
  (managed EC2 or container fleets) and customer-controlled hosting resources
  (Anywhere fleets). It includes the following updates:
  - New API calls for the `Compute` resource include: [ListCompute()](../apireference/API_ListCompute.md "../apireference/API_ListCompute.md"), [DescribeCompute()](../apireference/API_DescribeCompute.md "../apireference/API_DescribeCompute.md"), and [GetComputeAccess()](../apireference/API_GetComputeAccess.md "../apireference/API_GetComputeAccess.md"). These actions return hosting resource
    information for any type of Amazon GameLift Servers fleet. In general, for fleets with
    game servers that use server SDK 5.x, use the compute-specific actions
    to replace instance-specific actions. In addition, these actions are for
    use in Anywhere fleets without the Amazon GameLift Servers Agent: [RegisterCompute()](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md"), [DeregisterCompute()](../apireference/API_DeregisterCompute.md "../apireference/API_DeregisterCompute.md"), and [GetComputeAuthToken()](../apireference/API_GetComputeAuthToken.md "../apireference/API_GetComputeAuthToken.md").
  - New metric `ActiveCompute` with CloudWatch dimensions
    `FleetId`, `Location`, and
    `ComputeType`. This metric replaces the previous metric
    `ActiveInstances`.

- Amazon EC2 Systems Manager (SSM )for remote access – For added security, use SSM instead of SSH when
  connecting to instances in Amazon GameLift Servers managed fleets. See [Remotely connect to Amazon GameLift Servers fleet instances](fleets-remote-access.md "fleets-remote-access.md").
