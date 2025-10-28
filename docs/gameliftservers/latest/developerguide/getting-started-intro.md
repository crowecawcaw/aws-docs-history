# Getting started with Amazon GameLift Servers

Take advantage of these getting started resources to learn more about the Amazon GameLift Servers
service and how you can start developing a custom hosting solution for your session-based
multiplayer games.

## Before you start

- Create an AWS account (or designate an existing one) to use with Amazon GameLift Servers.
- Set up users with permissions for Amazon GameLift Servers and related AWS services.
- Select an AWS Region to work in. For development, choose a Region that's close to your
  location. You can change Regions at any time.

[Set up an AWS account](setting-up-aws-login.md "setting-up-aws-login.md")

## Quick onboarding options

Try out these quick start tools to get a basic hosting solution up and running fast with
streamlined development. These tools are ideal for proof of concept and prototyping, or
use them to build test environments for rapid iterative game development. After using
these tools to deploy a game server for hosting, you can use the Amazon GameLift Servers console and API
tools to monitor fleet performance, manage game sessions, and analyze metrics.

- [Game server
  wrapper for Amazon GameLift Servers](https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper/ "https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper/") – This tool is the quickest and easiest way
  to get your game server hosted and running game sessions with Amazon GameLift Servers, with no
  changes to game code required. The game server wrapper offers basic game session
  management functionality and streamlined game server deployment. It's ideal for
  doing a hands-on evaluation of Amazon GameLift Servers using your own game project or a sample
  project. When you're ready to build a custom game hosting solution, switch to
  one of the custom development options with full integration with the server SDK
  for Amazon GameLift Servers. If your game doesn't need a custom hosting solution, you can continue
  to use the game server wrapper to deploy and host your game servers in production.
- [Amazon GameLift Servers plugin for Unreal Engine or Unity](getting-started-plugin.md "getting-started-plugin.md")
  – The
  plugins give you GUI workflows and sample assets to guide you through the
  initial steps and deploy your game server with a basic hosting solution. Use the
  plugin to set up hosting with self-managed Anywhere fleets, or deploy
  cloud-based, managed EC2 fleets or container fleets. When you're ready to
  develop a custom hosting solution, you can build on your plugin-built
  solutions.
- [Starter kit for Amazon GameLift Servers managed containers](https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit "https://github.com/aws/amazon-gamelift-toolkit/tree/main/containers-starter-kit") – This kit
  streamlines tasks to integrate a game server, prepare a game server container
  image, and deploy a container fleet for hosting. For integration, the kit adds
  essential game session management features to your game server. The kit uses
  pre-configured templates to build a container fleet and an automated deployment
  pipeline for the game server. When you're ready to add full game session
  management features, follow one of the custom development roadmaps to integrate
  the server SDK for Amazon GameLift Servers.

## Custom development options

Follow one of these development roadmaps to get started building a full-featured
custom hosting solution for your game. The roadmaps provide detailed guidance on how to
create, test, and customize each component in your hosting solution.

- [Development roadmap for hosting with Amazon GameLift Servers
  managed EC2](gamelift-roadmap-managed.md "gamelift-roadmap-managed.md")
- [Development roadmap for hosting with Amazon GameLift Servers managed
  containers](gamelift-roadmap-containers.md "gamelift-roadmap-containers.md")
- [Development roadmap for hosting with Amazon GameLift Servers Anywhere](gamelift-roadmap-anywhere.md "gamelift-roadmap-anywhere.md")
- [Development roadmap for hybrid hosting
  with Amazon GameLift Servers](gamelift-roadmap-hybrid.md "gamelift-roadmap-hybrid.md")

## Amazon GameLift Servers examples

If you're considering using Amazon GameLift Servers to manage your custom game server, or you're interested
in taking advantage of Amazon GameLift Servers Realtime, we recommend that you try the following examples before you
use the service for your own game. The custom game server example gives you experience with
game hosting in the Amazon GameLift Servers console. The Amazon GameLift Servers Realtime example shows you how to prepare a game for
hosting using Realtime servers.

### Custom game server example

This example demonstrates the process of deploying a sample game server to Amazon GameLift Servers
managed EC2 fleet for hosting. Use the sample game client to connect to a live game
session. You can experience how to use Amazon GameLift Servers .tools, including the console and the AWS
CLI, to monitor the fleet's hosting performance and usage.

The example walks you through the following steps:

- Upload the sample game server build.
- Create a fleet to run the game server build.
- Get the sample game client and use it to connect to a game server and join a
  game session.
- Review fleet and game session metrics.

Start up multiple game clients and play the game to generate hosting data. Use the
Amazon GameLift Servers console to view hosting resources, track metrics, and explore options for scaling
the fleet's hosting capacity.

To get started, sign in to the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/sample-game "https://console.aws.amazon.com/gamelift/sample-game"). In the left-side navigation, go to
**Resources**, **Try a sample game**.

### Amazon GameLift Servers Realtime example

This example is a complete tutorial that walks you through how to deploy a sample
multiplayer game, Mega Frog Race, with Amazon GameLift Servers Realtime. The tutorial covers how to integrate
your game client with the Realtime SDK and deploy a complete hosting solution with Realtime servers on
managed EC2 fleets.

For a hands-on tutorial, see [Creating Servers for Multiplayer Mobile Games with Just a Few Lines of
JavaScript](https://aws.amazon.com/blogs/gametech/creating-servers-for-multiplayer-mobile-games-with-amazon-gamelift/ "https://aws.amazon.com/blogs/gametech/creating-servers-for-multiplayer-mobile-games-with-amazon-gamelift/") on the AWS for Games blog. For the source code of Mega Frog
Race, see the [GitHub repository](https://github.com/aws-samples/megafrograce-gamelift-realtime-servers-sample "https://github.com/aws-samples/megafrograce-gamelift-realtime-servers-sample").

The source code includes the following parts:

- Game client – Source code for the C++ game client, created in Unity.
  The game client gets game session connection information, connects to the
  server, and exchanges updates with other players.
- Backend service – Source code for an AWS Lambda function that manages
  direct calls to the service API for Amazon GameLift Servers.
- Realtime script – A source script file that configures a fleet of
  Realtime servers for the game. This script includes the minimum configuration required for
  each Realtime server to communicate with Amazon GameLift Servers and host game sessions.

After you set up the sample game for hosting, use it as a starting point to experiment
with other Amazon GameLift Servers features such as FlexMatch.
