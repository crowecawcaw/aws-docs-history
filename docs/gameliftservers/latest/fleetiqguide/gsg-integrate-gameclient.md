# Integrate Amazon GameLift Servers FleetIQ into a game client

This topic describes the tasks required to prepare your game client or matchmaking service
to communicate with Amazon GameLift Servers FleetIQ in order to acquire a game server to host a game
session.

Create a method that allows your game client or matchmaker to request a game server
resource for players. You have a couple of options for how to do this:

- Have Amazon GameLift Servers FleetIQ choose an available game server. This option takes advantage of
  Amazon GameLift Servers FleetIQ optimizations to use low-cost Spot Instances and for automatic
  scaling.
- Request all available game servers and select one to use (often referred to as
  "list and pick").

###### Topics

- [Let Amazon GameLift Servers FleetIQ choose a game
  server](gsg-integrate-gameclient-automatic.md "gsg-integrate-gameclient-automatic.md")
- [Choose your own game server](gsg-integrate-gameclient-optimized.md "gsg-integrate-gameclient-optimized.md")
