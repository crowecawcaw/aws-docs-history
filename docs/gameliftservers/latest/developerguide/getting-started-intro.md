# Getting started with Amazon GameLift Servers

Take advantage of these getting started resources to learn more about the Amazon GameLift Servers
service and how you can start developing a custom hosting solution for your session-based
multiplayer games.

## Before you start

- Create an AWS account (or designate an existing one) to use with Amazon GameLift Servers.
- Set up users with permissions for Amazon GameLift Servers and related AWS services.
- Select an AWS Region to work in. For development, choose a Region that's close to your
  location. You can change Regions at any time.

[Set up an AWS user account](setting-up-aws-login.md "setting-up-aws-login.md")

## Choose your path

### I want to explore Amazon GameLift Servers quickly

Best for: learning, creating a proof of concept, rapid prototyping

Quick qtart options:

- [Game server
  wrapper for Amazon GameLift Servers](https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper/ "https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper/") – See [Tutorial: Quick onboarding with the Amazon GameLift Servers wrapper](gamelift-wrapper-tutorial.md "gamelift-wrapper-tutorial.md").
  This tool is the quickest and easiest way
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

### I want to build a custom hosting solution

Best for: creating a production-level solution for a custom game server

Review the page [Amazon GameLift Servers game hosting options](gamelift-intro-flavors.md "gamelift-intro-flavors.md") and choose one of the options for your solution.
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

## Recommended learning path

1. Start small. Try the game server wrapper or the plugin for Unreal.
2. Understand the concepts. Review the page [How hosting with Amazon GameLift Servers works](gamelift-howitworks.md "gamelift-howitworks.md").
3. Choose architecture. Select your hosting model based on your game's requirements.
4. Build and test. Follow the appropriate development roadmap. Build a basic version of each component and then iterate and customize.
5. Scale and optimize. Optimize your solution for production-level usage. Add advanced features such as matchmaking.
