# Game engines and Amazon GameLift Servers

You can use the managed Amazon GameLift Servers service with most major game engines that support C++ or C#
libraries, including O3DE, Unreal Engine, and Unity. Build the version you need for your
game; see the README files with each version for build instructions and minimum
requirements. For more information on available Amazon GameLift Servers SDKs, supported development platforms
and operating systems, see [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md") for game servers.

In addition to the engine-specific information provided in this topic, find additional
help with integrating Amazon GameLift Servers into your game servers, clients and services in the following
topics:

- [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
  – Detailed instructions on integrating Amazon GameLift Servers into a game server.
- [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md")
  – Detailed instructions on integrating into a game client or service,
  including creating game sessions and joining players to games.

## O3DE

###### Game servers

Prepare your game servers for hosting on Amazon GameLift Servers using the [server SDK for Amazon GameLift Servers for C++](integration-server-sdk5-cpp-actions.md "integration-server-sdk5-cpp-actions.md"). See
[Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md") to get help with integrating the required functionality into your game
server.

###### Game clients and services

Enable your game clients and/or game services to interact with Amazon GameLift Servers service, such
as to find available game sessions or create new ones, and add players to games.
Core client functionality is provided in the [AWS SDK for C++](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html "https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html"). To
integrate Amazon GameLift Servers into your O3DE game project, see [Add Amazon GameLift Servers to an O3DE game client and server](game-client-intro.md "game-client-intro.md") and [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").

## Unreal Engine

###### Game servers

Prepare your game servers for hosting on Amazon GameLift Servers by adding the [server SDK for Amazon GameLift Servers for Unreal
Engine](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md") to your project and implementing the required server
functionality. For help setting up the Unreal Engine plugin and adding Amazon GameLift Servers code,
see [Integrate Amazon GameLift Servers into an Unreal Engine
project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md").

###### Game clients and services

Enable your game clients and/or game services to interact with Amazon GameLift Servers service, such
as to find available game sessions or create new ones, and add players to games.
Core client functionality is provided in the [AWS SDK for C++](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html "https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html"). To
integrate Amazon GameLift Servers into your Unreal Engine game project, see [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").

## Unity

###### Game servers

Prepare your game servers for hosting on Amazon GameLift Servers by adding the [server SDK for Amazon GameLift Servers for C#](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md") to
your project and implementing the required server functionality. For help setting up
with Unity and adding Amazon GameLift Servers code, see [Integrate Amazon GameLift Servers into a Unity
project](integration-engines-unity-using.md "integration-engines-unity-using.md").

###### Game clients and services

Enable your game clients and/or game services to interact with Amazon GameLift Servers service, such
as to find available game sessions or create new ones, and add players to games.
Core client functionality is provided in the [AWS SDK for .NET](../../../sdkfornet/v3/apidocs.md "../../../sdkfornet/v3/apidocs.md"). To integrate Amazon GameLift Servers into your Unity game project, see [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").

## Other engines

For a full list of the Amazon GameLift Servers SDKs available for game servers and clients, see [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md").
