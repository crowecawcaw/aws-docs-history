# Amazon GameLift Servers examples

If you're considering using Amazon GameLift Servers to manage your custom game server, or you're interested
in taking advantage of Amazon GameLift Servers Realtime, we recommend that you try the following examples before you
use the service for your own game. The custom game server example gives you experience with
game hosting in the Amazon GameLift Servers console. The Amazon GameLift Servers Realtime example shows you how to prepare a game for
hosting using Realtime servers.

## Custom game server example

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
