# Preparing your games for hosting with Amazon GameLift Servers Realtime

Get your multiplayer games ready for hosting with Amazon GameLift Servers Realtime. This section guides you through the steps required to
create a hosting solution for your game using Realtime servers and Amazon GameLift Servers managed EC2 hosting in the cloud.

Your solution will have the following components:

- A Realtime server that you customize to work with your game. This component is in the form
  of a script containing JavaScript code that provides your custom configuration and optional extensions. This
  script tells Amazon GameLift Servers how to set up and run Realtime servers for you. To use this script, you upload it to the Amazon GameLift Servers
  service.
- A version of your game client that's been integrated with the AWS SDK and the Amazon GameLift Servers Realtime client SDK. Use these
  tools to add the necessary functionality to communicate with the Amazon GameLift Servers service to start or join game sessions,
  as well as connect to and interact with Realtime servers to play the game.

###### Topics

- [Customize an Amazon GameLift Servers Realtime script](realtime-script.md "realtime-script.md")
- [Integrate a game client for Amazon GameLift Servers Realtime](realtime-client.md "realtime-client.md")
- [Upload a script for Amazon GameLift Servers Realtime servers](realtime-script-uploading.md "realtime-script-uploading.md")
- [Update an Amazon GameLift Servers Realtime script](realtime-script-uploading-update.md "realtime-script-uploading-update.md")
