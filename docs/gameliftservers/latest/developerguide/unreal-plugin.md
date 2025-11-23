# Amazon GameLift Servers plugin for Unreal Engine

This plugin adds the Amazon GameLift Servers C++ server SDK and tools to the UE editor. Use the
guided UI workflows to integrate server SDK functionality into your game project and deploy
an Amazon GameLift Servers hosting solution for your game server.

With the plugin, you can build a basic working hosting solution and then optimize and
customize as needed. Set up an Amazon GameLift Servers Anywhere fleet with your local workstation as a
host. For cloud hosting with managed EC2 or managed container fleets, deploy your game
server with a complete solution to manage game session requests and client
connections.

###### Topics

- [Install the plugin for your Unreal game project](#unreal-plugin-install "#unreal-plugin-install")
- [Next steps: Customize your game hosting solution](#unreal-plugin-next-steps "#unreal-plugin-next-steps")
- [Plugin for Unreal: Set up an AWS user
  profile](unreal-plugin-profiles.md "unreal-plugin-profiles.md")
- [Plugin for Unreal: Integrate your game code](unreal-plugin-integrate.md "unreal-plugin-integrate.md")
- [Plugin for Unreal: Host your game locally with
  Amazon GameLift Servers Anywhere](unreal-plugin-anywhere.md "unreal-plugin-anywhere.md")
- [Plugin for Unreal: Deploy your game to a managed EC2
  fleet](unreal-plugin-ec2.md "unreal-plugin-ec2.md")
- [Plugin for Unreal: Deploy your game to a
  managed container fleet](unreal-plugin-container.md "unreal-plugin-container.md")

##

Install the plugin for your Unreal game project

**[Get the Amazon GameLift Servers plugin for Unreal Engine from GitHub](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal")**

See the GitHub repository readme for information about how to install the plugin in your Unreal
Editor for a game project.

The plugin includes these components:

- Plugin modules for the UE editor. When the plugin is installed, a new main
  menu button gives you access to Amazon GameLift Servers functionality.
- C++ libraries for the Amazon GameLift Servers service API. Use API functionality in a
  client-side backend service to help game clients request game sessions and
  send/retrieve game session information.
- Unreal libraries for the Amazon GameLift Servers server SDK (version 5). Use the server
  SDK in your game server code to manage communication between hosted game server
  processes and the Amazon GameLift Servers service.
- Content for testing, including a startup game map and two testing maps
  with basic blueprints and UI elements for use with testing a server
  integration.
- Editable configurations, in the form of CloudFormation templates, that the plugin
  uses when deploying your game server for hosting.

This plugin uses AWS CloudFormation
templates to deploy hosting solutions for common gaming scenarios. Use these solutions
as provided or customize them as needed for your games.

## Next steps: Customize your game hosting solution

Using the plugin's guided workflows is a good way to get up and running fast with an
Amazon GameLift Servers hosting solution. With the plugin, you can set up basic versions of each of your
solution's components.

When you're ready, you can build on this basic solution by customizing each component,
and fine-tuning your solution as you prepare for game launch. Consider these options:

- Modify your fleets and fleet configurations. See [Hosting resource customizations](fleets-design.md "fleets-design.md").
- Customize your game session queue configuration. See [Customize a game session queue](queues-design.md "queues-design.md"):
- Add functionality to your game server and game client.
  See [Integrate a game server with Amazon GameLift Servers](gamelift-sdk-server.md "gamelift-sdk-server.md") and
  [Integrate Amazon GameLift Servers game client functionality](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").
- Customize your backend service.
  See [Build a backend service for Amazon GameLift Servers](gamelift_quickstart_customservers_designbackend.md "gamelift_quickstart_customservers_designbackend.md").
- Set up automatic capacity scaling to meet expected player demand. See [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md").
- Set up hosting observability tools, including analytics and logging. See [Monitoring Amazon GameLift Servers](monitoring-overview.md "monitoring-overview.md").
- Automate your deployment using [infrastructure as code (IaC)](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md"). The plugin's guided workflows for managed solutions use AWS CloudFormation
  templates. You can customize these as needed. See [Manage Amazon GameLift Servers hosting resources using CloudFormation](resources-cloudformation.md "resources-cloudformation.md").

###### Topics

- [Plugin for Unreal: Set up an AWS user
  profile](unreal-plugin-profiles.md "unreal-plugin-profiles.md")
- [Plugin for Unreal: Integrate your game code](unreal-plugin-integrate.md "unreal-plugin-integrate.md")
- [Plugin for Unreal: Host your game locally with
  Amazon GameLift Servers Anywhere](unreal-plugin-anywhere.md "unreal-plugin-anywhere.md")
- [Plugin for Unreal: Deploy your game to a managed EC2
  fleet](unreal-plugin-ec2.md "unreal-plugin-ec2.md")
- [Plugin for Unreal: Deploy your game to a
  managed container fleet](unreal-plugin-container.md "unreal-plugin-container.md")
