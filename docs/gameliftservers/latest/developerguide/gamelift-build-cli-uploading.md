

# Create a game server build for Amazon GameLift Servers
<a name="gamelift-build-cli-uploading"></a>

After you integrate your game server with Amazon GameLift Servers (see [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md)), install the game server software onto your compute resources for hosting. This process varies depending on the type of Amazon GameLift Servers hosting you're using.

## Deploy for managed hosting
<a name="gamelift-build-custom-upload"></a>

If you're using Amazon GameLift Servers managed EC2 hosting, you must package your game server software and upload it to Amazon GameLift Servers. When you create a managed fleet, Amazon GameLift Servers automatically deploys it to each fleet instance. 

The topics in this section describe how to package your build files for uploading, create an optional build install script, and then upload the files using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/) or AWS SDK.

## Deploy for Anywhere hosting
<a name="gamelift-build-custom-anywhere"></a>

If you're using Amazon GameLift Servers Anywhere fleets for self-managed hosting, it's your responsibility to install the game server software onto each compute in a fleet and keep it updated.

When an integrated game server process starts running, it automatically initializes and establishes communication with the Amazon GameLift Servers service. The server process starts game sessions from prompts by Amazon GameLift Servers and reports activity back to the service.

**Topics**
+ [Deploy for managed hosting](#gamelift-build-custom-upload)
+ [Deploy for Anywhere hosting](#gamelift-build-custom-anywhere)
+ [Package your game build files](gamelift-build-packaging.md)
+ [Add a build install script](gamelift-build-cli-uploading-install.md)
+ [Create an Amazon GameLift Servers build resource for managed hosting](gamelift-build-cli-uploading-builds.md)