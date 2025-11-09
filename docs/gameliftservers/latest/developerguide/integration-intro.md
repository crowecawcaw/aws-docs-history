# Prepare a game for hosting with Amazon GameLift Servers

Before you can deploy your game for hosting on Amazon GameLift Servers, you need to prepare both your game server and game client components. This involves integrating your game server with the Amazon GameLift Servers Server SDK and building a backend service that handles player authentication and game session management.

The Server SDK integration enables your game server to communicate with the Amazon GameLift Servers service, report its health status, and manage game sessions. The backend service acts as an intermediary between your game clients and the Amazon GameLift Servers service, handling player requests and coordinating game session placement.

###### Topics

- [Prepare your Unreal or Unity game with the Amazon GameLift Servers plugin](getting-started-plugin.md "getting-started-plugin.md")
- [Integrate a game server with Amazon GameLift Servers](gamelift-sdk-server.md "gamelift-sdk-server.md")
- [Package a game server build for deployment](gamelift-build-intro.md "gamelift-build-intro.md")
- [Game client/server interactions with
  Amazon GameLift Servers](gamelift-sdk-interactions.md "gamelift-sdk-interactions.md")
