# Get Amazon GameLift Servers development tools

Amazon GameLift Servers provides a set of SDKs and other tools to help you build game hosting solutions for
your games. The SDKs add functionality to game servers, game clients, and backend services
that enables them to interact with the Amazon GameLift Servers service. For the latest information about Amazon GameLift Servers
SDK versions and compatibility, see [Amazon GameLift Servers release notes](release-notes.md "release-notes.md").

## For game servers

Integrate and build your 64-bit game servers with the server SDK for Amazon GameLift Servers. The game
server uses the server SDK to communicate with the Amazon GameLift Servers service for game session
management, including starting, updating, and stopping game sessions. For help with
integrating the server SDK into your game projects, see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md").

### Development support

- **Development OS**
  - Windows
  - Linux

- **Programming languages**

**[Get the Amazon GameLift Servers SDK](https://github.com/amazon-gamelift "https://github.com/amazon-gamelift").** For version-specific information
and install instructions, see the included readme files in each package.

    + [C++ server SDK](https://github.com/amazon-gamelift/amazon-gamelift-servers-cpp-server-sdk "https://github.com/amazon-gamelift/amazon-gamelift-servers-cpp-server-sdk")




    	- [Server SDK reference](integration-server-sdk5-cpp-actions.md "integration-server-sdk5-cpp-actions.md")
    	- [How to integrate](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
    + [C# server SDK](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk "https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk") (Support for .NET 4, .NET 6, .NET 8 varies by version, see [SDK versions](release-notes.md#release-notes-history "release-notes.md#release-notes-history"))




    	- [Server SDK reference](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")
    	- [How to integrate](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
    + [Go server SDK](https://github.com/amazon-gamelift/amazon-gamelift-servers-go-server-sdk "https://github.com/amazon-gamelift/amazon-gamelift-servers-go-server-sdk")




    	- [Server SDK reference](integration-server-sdk-go-actions.md "integration-server-sdk-go-actions.md")
    	- [How to integrate](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")

- **Game engine support**

The full-featured plugin for Amazon GameLift Servers includes UI workflows and sample assets, as
well as built-in versions of the AWS SDK and server SDK. The workflows
guide you through how to configure and deploy your game server for hosting
with managed EC2 fleets, managed container fleets, or self-managed Anywhere
fleets. If you don't need the guided workflows, you can get just the server
SDK for your game engine from the same GitHub repositories.

If you're using another game
engine or development environment that the plugin doesn't support, get the server SDK
for your programming language and add it to your game project.

For version-specific information and install instructions, see
the included readme files in each package.

    + [Plugin for Unreal Engine](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal") – Built for use with
     Unreal Engine versions 5.0, 5.1, 5.2, 5.3,
     5.4, 5.5, and 5.6. Check version-specific readme files
     for Unreal support.




    	- [Plugin guide for Unreal Engine](unreal-plugin.md "unreal-plugin.md")
    	- [C++ (Unreal) server SDK 5.x for
    	 Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")
    + [Plugin for Unity](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity") – Built for use with LTS
     versions of Unity Editor 6.0, 2022.3, or
     2021.3. It supports Unity's .NET Framework and .NET
     Standard profiles, with .NET Standard 2.1 and .NET 4.x. Check
     version-specific readmes for Unity support.




    	- [Plugin guide for Unity](unity-plug-in.md "unity-plug-in.md")
    	- [C# server SDK 5.x for Amazon GameLift Servers --
    	 Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")C# server SDK
    	 reference
    + [Server SDK for Unreal](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal")




    	- [Server SDK reference](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")
    	- [Integrate Amazon GameLift Serversinto an Unreal Engine project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md")
    + [Server SDK for Unity](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity")




    	- [Server SDK reference](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")
    	- [Integrate Amazon GameLift Servers into a Unity project](integration-engines-unity-using.md "integration-engines-unity-using.md")

### Runtime support

For a managed hosting solution, build your game server to run on one of the
following Amazon machine images (AMIs). See [Amazon GameLift Servers AMI versions](reference-ec2-ami-version-history.md "reference-ec2-ami-version-history.md") for Amazon GameLift Servers for more
details.

- [Windows Server
  2016](https://aws.amazon.com/windows/products/ec2/windows-server-2016/ "https://aws.amazon.com/windows/products/ec2/windows-server-2016/")
- [Amazon Linux
  2023](https://aws.amazon.com/linux/amazon-linux-2023/ "https://aws.amazon.com/linux/amazon-linux-2023/")
- [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/")

###### Note

Amazon Linux 2 (AL2) will reach end of support on June 30, 2025. See more details
in the [Amazon Linux 2
FAQs](https://aws.amazon.com/amazon-linux-2/faqs/ "https://aws.amazon.com/amazon-linux-2/faqs/"). For game servers that are hosted on AL2 and use Amazon GameLift Servers server
SDK 4.x, first update the game server build to server SDK 5.x, and then deploy
to AL2023 instances. See [Migrate to server SDK 5.x for
Amazon GameLift Servers](reference-serversdk5-migration.md "reference-serversdk5-migration.md").

### Additional tools

###### [Game server wrapper for Amazon GameLift Servers](https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper/ "https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper/")

This tool helps you deploy a game server for hosting with a set of basic game
session management functionality. With this tool, you don't need to make changes
to your game code or integrate the server SDK for Amazon GameLift Servers. Use the game server
wrapper to package your game server and deploy it for game hosting using any of
the three Amazon GameLift Servers hosting solutions (Anywhere, managed EC2, or managed
containers). This tool is best suited for early evaluation or prototyping with
your own game or a sample game, as this tool doesn't support game server
customization. If your game doesn't need custom features, you can deploy your
game server with the game server wrapper for production hosting.

###### [Amazon GameLift Servers Toolkit](https://github.com/aws/amazon-gamelift-toolkit "https://github.com/aws/amazon-gamelift-toolkit")

The Amazon GameLift Servers Toolkit is a collection of scripts and other tools that we've
developed to help developers with common scenarios and issues. Toolkit materials include
scripts, sample code, and readmes.

- [Containers starter kit](https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit "https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit") – Use this tool to streamline the
  tasks of setting up game server builds for hosting with Amazon GameLift Servers managed
  containers. The kit integrates essential game session management features into a
  game server, and uses pre-configured templates to create a container fleet and
  set up an automated deployment pipeline for your game server build. After
  deployment, you can monitor fleet performance, manage game sessions, and analyze
  metrics using the Amazon GameLift Servers console and API tools. The kit integrates with AWS CodeBuild
  for build automation, Amazon Simple Storage Service for storage, and AWS CloudFormation for infrastructure
  deployment.
- [Fast build update tool](https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool "https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool") – Use this tool to modify a game
  server build that's already deployed to a managed EC2 fleet. The tool is built
  to help you quickly swap out game build files without having to configure and
  create new EC2 fleets with every change. You can update individual instances or
  all instances in the fleet. Options let you replace specific build files or an
  entire build, and let you manage how to restart game servers after the updates.

## For game client services

Create a 64-bit backend service for your game and integrate it with functionality from
the AWS SDK, which includes the service API for Amazon GameLift Servers. Use the backend service
to handle client-side interactions with the Amazon GameLift Servers service, including starting or finding
game sessions and joining players to games.

[Get the
AWS SDK](https://aws.amazon.com/developer/tools/#SDKs "https://aws.amazon.com/developer/tools/#SDKs")

For more information about using the AWS SDK with Amazon GameLift Servers, see the following
resources:

- [Amazon GameLift Servers API Reference](../apireference/Welcome.md "../apireference/Welcome.md")
- Integrate game client functionality
  - [Client-side service integration for games with custom game server builds](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md")
  - [Client-side service integration for games with Realtime
    servers](../realtimeguide/realtime-client.md "../realtimeguide/realtime-client.md")

- [Design a client backend service](gamelift_quickstart_customservers_designbackend.md "gamelift_quickstart_customservers_designbackend.md")

## For Amazon GameLift Servers resource management

Use the following tools to create, update, and monitor your Amazon GameLift Servers managed hosting resources.

- AWS Management Console – The AWS Console is a web-based application
  that provides centralized access to all individual AWS service consoles,
  including Amazon GameLift Servers. Use the Console to create or sign into an AWS account and
  open the Amazon GameLift Servers console to work with your game hosting resources. You can
  configure and deploy hosting fleets and other resources, view usage and
  performance metrics, track resources in the dashboard, and many other tasks.
  [Go to the Amazon GameLift Servers console.](https://console.aws.amazon.com/gamelift "https://console.aws.amazon.com/gamelift")
- [Service API for
  Amazon GameLift Servers](../apireference/Welcome.md "../apireference/Welcome.md") – This API gives you programmatic access to all of
  your Amazon GameLift Servers resources. It is part of the AWS SDK, which you can download for
  use with most popular programming languages. [Get the AWS SDK.](https://aws.amazon.com/developer "https://aws.amazon.com/developer")
- [AWS command line interface (CLI)](../../../cli.md "../../../cli.md") – The
  AWS CLI lets you interact with AWS services using a command-line shell. The
  tools provides direct access to the public APIs for AWS services as well as
  customized commands that are available for a service. [Get the AWS CLI.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") for
  Amazon GameLift Servers – The AWS CloudFormation service helps you model and set up AWS resources to
  streamline infrastructure deployment and management. Create an AWS CloudFormation template to
  describe the Amazon GameLift Servers resources for your hosting solution, and then use the
  template to build additional resources or update configurations. View the [Amazon GameLift Servers resource
  type reference.](../../../AWSCloudFormation/latest/UserGuide/AWS_GameLift.md "../../../AWSCloudFormation/latest/UserGuide/AWS_GameLift.md")

## For Amazon GameLift Servers Realtime

Configure and deploy Realtime servers to host your multiplayer games. To allow your
game clients to connect to Realtime servers, use the Amazon GameLift Servers Realtime client SDK.
To get started, [download the Realtime client SDK](https://aws.amazon.com/gamelift/servers/getting-started/ "https://aws.amazon.com/gamelift/servers/getting-started/").
For configuration information, see
[Integrating a game client for Amazon GameLift Servers Realtime](../realtimeguide/realtime-client.md "../realtimeguide/realtime-client.md").

**SDK support**

The Realtime Client SDK contains source for the following languages:

- C# (.NET)

**Development environments**

Build the SDK from source as needed for the following supported development operating
systems and game engines:

- **Operating systems** – Windows, Linux,
  Android, iOS
- **Game engines** – Unity, engines that
  support C# libraries

**Game server operating systems**

You can deploy Realtime servers onto hosting resources that run on the following
platforms:

- [Amazon Linux](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/")
- [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/")

###### Note

AL2 is nearing end of support. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/ "https://aws.amazon.com/amazon-linux-2/faqs/").
