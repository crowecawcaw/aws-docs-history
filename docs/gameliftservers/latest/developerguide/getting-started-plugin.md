# Prepare your Unreal or Unity game with the Amazon GameLift Servers plugin

The Amazon GameLift Servers plugin is a full-featured add-on to your Unreal or Unity game engine. It guides
you through the basic steps to deploy your game for hosting with Amazon GameLift Servers. With the plugin's
tool set and workflows, you can work in your game engine development environment to prepare
your game server for hosting, set up hosting on a local machine for testing, create a simple
backend service, and deploy your game server to managed cloud-based hosting.

Use the plugin to experience working with Amazon GameLift Servers and get a game hosting solution up and
running fast. You can work with sample game assets or your own game project. The plugin
automates a number of steps so that you can quickly build a simple working solution. When
you complete the plugin's guided workflows, you'll be able to connect a game client to live
hosted game sessions through Amazon GameLift Servers. After using the plugin to create a simple hosting
solution, you can customize your solution to meet the needs of your game.

The plugin is available for the following game engines:

- Unreal Engine
- Unity
  The plugin includes these components for each game engine:

- Plugin modules for the game engine editor. When the plugin is installed, a new
  main menu button gives you access to Amazon GameLift Servers functionality.
- Libraries for the Amazon GameLift Servers service API with client-side functionality.
- Libraries for the Amazon GameLift Servers server SDK (version 5).
- Sample assets for use with testing a server integration.
- Editable configurations, in the form of CloudFormation templates, that define your game
  server solution.

###### Topics

- [Plugin workflow](#getting-started-plugin-workflow "#getting-started-plugin-workflow")
- [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md")
- [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md")
- [Amazon GameLift Servers plugin for Unity for server SDK 4](unity-plug-in-sdk4.md "unity-plug-in-sdk4.md")

## Plugin workflow

The following steps describe a typical path to preparing and deploying your game
project on Amazon GameLift Servers. You complete these steps by working in the game engine editor and
your game code.

1. Create a user profile that links to your AWS account user and provides
   access credentials with permissions to use Amazon GameLift Servers.
2. Set up related AWS resources that the plugin uses in the hosting solution
   (referred to as "bootstrapping").
3. Add server code to your project to establish communication between a running
   game server and the Amazon GameLift Servers service.
4. Add client code to your project that lets game clients send requests to
   Amazon GameLift Servers to start new game sessions and then connect to them.
5. Use the Anywhere workflow to set up your local workstation as an Anywhere
   compute and host your game server. Launch your game server and client locally
   through the plugin, connect to a game session, and test the integration.
6. Use the Managed EC2 workflow to upload your game server to Amazon GameLift Servers and
   deploy a simple but complete cloud hosting solution. Launch your game client
   locally through the plugin, request a game session and connect to it, and play
   your game.

When working in the plugin, you'll create and use AWS resources, These actions might
incur charges to the AWS account in use. If you're new to AWS, these actions might
be covered under the [AWS Free
Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").
