# Migrate to server SDK 5.x for

Amazon GameLift Servers

To update a game project to use server SDK version 5.x, make the following changes:

###### Note

If you need to continue using server SDK version 4.x or earlier, see [Server SDK for Amazon GameLift Servers version 4 and
earlier](reference-serversdk4.md "reference-serversdk4.md") for documentation and download information.
For SDK version 4.0.2 specifically, you can download it from the [official GitHub releases](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/releases "https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/releases").

1. Get the latest server SDK for Amazon GameLift Servers package for your development environment
   **[[Download site](https://aws.amazon.com/gamelift/servers/getting-started-sdks/ "https://aws.amazon.com/gamelift/servers/getting-started-sdks/")]**.
   Follow the install instructions in the `Readme` file for your
   downloaded package and version. See these instructions for using the server SDKs
   with your game project.
   - [For development environments using C++, C#, or
     Go](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
   - [For Unreal Engine projects (C++ server SDK
     for Unreal libraries only)](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md")
   - [For Unity projects (C# server SDK for Unity
     libraries only)](integration-engines-unity-using.md "integration-engines-unity-using.md")
   - [For use with the Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md")
   - [For use with the Amazon GameLift Servers plugin for Unity](unity-plug-in.md "unity-plug-in.md")

2. Update your server code as follows:
   - Change the server code callback function `onCreateGameSession()` to
     `onStartGameSession()`.
   - Update the `InitSDK()` inputs as appropriate:
     - If you plan to deploy the game server build to either an Amazon GameLift Servers managed
       EC2 fleet or an Anywhere fleet with the Amazon GameLift Servers Agent:

     Call `InitSDK()` with no parameters ([C++](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk"))
     ([C#](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk")) ([Unreal](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk")). This call sets up the compute environment
     and a WebSocket connection to the Amazon GameLift Servers service.
     - If you plan to deploy the game server build to an Anywhere
       fleet without the Amazon GameLift Servers Agent:

     Call `InitSDK()` with server parameters ([C++](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk-anywhere "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk-anywhere")) ([C#](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk-anywhere "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk-anywhere")) ([Unreal](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk-anywhere "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk-anywhere")). A game server process uses these parameters
     to establish a connection with the Amazon GameLift Servers service.

3. If your game server build or other hosted applications communicate with other
   AWS resources while running, you'll need to change how the application gets
   access to those resources. Replace the use of `AssumeRoleCredentials`
   with the new server SDK action `GetFleetRoleCredentials()` (for
   game servers) or use shared credentials (for other applications). For more on
   how to implement this change, see [Communicate with other AWS resources from
   your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").
4. If your project called the server SDK action
   `GetInstanceCertificate()` to retrieve a TLS certificate, modify
   your code to use the new `GetComputeCertificate()` ([C++](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-getcomputecertificate "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-getcomputecertificate"))
   ([C#](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-getcomputecertificate "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-getcomputecertificate")) ([Unreal](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-getcomputecertificate "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-getcomputecertificate")) instead.
5. When uploading your game build to Amazon GameLift Servers (such as with [upload-build](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html") or [CreateBuild()](../apireference/API_CreateBuild.md "../apireference/API_CreateBuild.md")), set the `ServerSdkVersion` parameter to
   the 5.x version you're using (this parameter currently defaults to 4.0.2). This
   parameter must match the actual server SDK libraries in the game server build.
   If you specify the wrong version for an uploaded game server build, any fleets
   you create with that build will fail. See [Deploy a custom server build for Amazon GameLift Servers
   hosting](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md").

The following example illustrates how to specify the server SDK version:

```
aws gamelift upload-build \
    --operating-system AMAZON_LINUX_2023 \
    --server-sdk-version "5.0.0" \
    --build-root "~/mygame" \
    --name "My Game Nightly Build" \
    --build-version "build 255" \
    --region us-west-2
```

6. If you use scripts to remotely connect to managed fleets, update the scripts
   to use the new process, as described in [Remotely connect to Amazon GameLift Servers fleet instances](fleets-remote-access.md "fleets-remote-access.md").
