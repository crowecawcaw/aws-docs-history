# Deploying game server software for Amazon GameLift Servers hosting

Deploy your multiplayer game server software by installing it on your hosting resources,
launching game server processes, and getting them ready to host games for players. The steps for
getting the game server software ready for deployment depends on the type of Amazon GameLift Servers
solution you're using. In all scenarios, the deployed game server software interacts with
the Amazon GameLift Servers service to handle game session placement and communicate connection details for a game client.

Your game server software must first be integrated with Amazon GameLift Servers, as described in
[Preparing games for Amazon GameLift Servers](integration-intro.md "integration-intro.md").

The topics in this section provide guidance on how to get your software ready for
deployment to the following scenarios.

- Custom game server software
  - For Amazon GameLift Servers managed EC2 hosting
  - For Amazon GameLift Servers managed containers hosting
  - For Amazon GameLift Servers Anywhere hosting

- Amazon GameLift Servers Realtime customized script for Amazon GameLift Servers managed EC2 hosting

###### Topics

- [Deploy a custom server build for Amazon GameLift Servers
  hosting](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md")
- [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md")
- [Deploy a script for Amazon GameLift Servers Realtime](realtime-script-uploading.md "realtime-script-uploading.md")
