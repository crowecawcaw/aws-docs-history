# Package a game server build for deployment

Get your game server software ready for deployment on your hosting resources. Once deployed, the
software is installed on each hosting resource, and then one or more game server process is launched
and readied to host game sessions for players.

Getting a game server build ready varies depending on the type of Amazon GameLift Servers
hosting options you're using. All game server builds must be integrated with the server SDK for Amazon GameLift Servers,
as described in
[Integrate a game server with Amazon GameLift Servers](gamelift-sdk-server.md "gamelift-sdk-server.md").

The topics in this section provide guidance on how to get your software ready for
deployment to the following scenarios.

- For managed EC2 hosting, package your server software and upload
  it to Amazon GameLift Servers for deployment.
- For managed containers hosting, build a container image with your
  server software and store it in Amazon Elastic Container Registry for deployment.
- For hosting with Amazon GameLift Servers Anywhere, package your server software as needed
  for installation on your own hosting resources.

###### Note

If you're deploying an Amazon GameLift Servers Realtime configured script, see
[Upload a script for Amazon GameLift Servers Realtime](../realtimeguide/realtime-script-uploading.md "../realtimeguide/realtime-script-uploading.md").

###### Topics

- [Create a game server build for Amazon GameLift Servers](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md")
- [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md")
