# Amazon GameLift Servers plugin for Unity (server SDK 5.x)

This plugin adds the Amazon GameLift Servers C# server SDK and tools to the Unity editor. Use the
guided UI workflows to integrate server SDK functionality into your game project and deploy
an Amazon GameLift Servers hosting solution for your game server.

With the plugin, you can build a basic working hosting solution and then optimize and
customize as needed. Set up an Amazon GameLift Servers Anywhere fleet with your local workstation as a
host. For cloud hosting with managed EC2 or managed container fleets, deploy your game
server with a complete solution to manage game session requests and client
connections.

###### Topics

- [Install the plugin for your Unity game project](#unity-plugin-install "#unity-plugin-install")
- [Plugin for Unity: Set up an AWS user
  profile](unity-plug-in-profiles.md "unity-plug-in-profiles.md")
- [Plugin for Unity: Set up local testing with
  Amazon GameLift Servers Anywhere](unity-plug-in-anywhere.md "unity-plug-in-anywhere.md")
- [Plugin for Unity: Deploy your game to a managed EC2
  fleet](unity-plug-in-ec2.md "unity-plug-in-ec2.md")
- [Plugin for Unity: Deploy your game to a
  managed container fleet](unity-plug-in-container.md "unity-plug-in-container.md")

##

Install the plugin for your Unity game project

**[Get the Amazon GameLift Servers plugin for Unity from GitHub](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity")**

See the GitHub repository readme for information about how to install the plugin for a game project.

The plugin includes these components:

- Plugin modules for the Unity editor. When the plugin is installed, a new
  main menu item gives you access to Amazon GameLift Servers functionality.
- C# libraries for the Amazon GameLift Servers service API with client-side functionality.
- C# libraries for the Amazon GameLift Servers server SDK (version 5.x).
- Sample game content, including assets and scenes, so you can try out
  Amazon GameLift Servers even if you don't have a build-ready multiplayer game.
- Solution configurations, provided as CloudFormation templates, that the plugin uses
  when deploying your game server to the cloud for hosting.

This plugin uses AWS CloudFormation
templates to deploy hosting solutions for common gaming scenarios. Use these solutions
as provided or customize them as needed for your games.
