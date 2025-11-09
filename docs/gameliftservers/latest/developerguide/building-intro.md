# Building a game hosting solution with Amazon GameLift Servers

This section includes guidance on how to build all the components of an Amazon GameLift Servers
game hosting solution, including design best practices. Whether you're starting from scratch or
migrating an existing game, you'll find comprehensive information to help you architect, implement,
and optimize your game hosting infrastructure using Amazon GameLift Servers.

###### Hosting solution components

Your hosting solution must have some version of the following components. For more detail on these components
and how they work together, see [How hosting with Amazon GameLift Servers works](gamelift-howitworks.md "gamelift-howitworks.md").

- **Game client** runs on player devices.
- **Backend service** coordinates communication between game
  clients and Amazon GameLift Servers.
- **Game server** software manages multiplayer gameplay.
- **Placement system** matches players to game servers.
- **Game hosting fleets** provide computing resources in geographic
  locations.
- **Game hosting management system** monitors game hosting status
  and manages capacity.

###### Topics

- [Development roadmaps](roadmaps-intro.md "roadmaps-intro.md")
- [Prepare a game for hosting with Amazon GameLift Servers](integration-intro.md "integration-intro.md")
- [Build a backend service for Amazon GameLift Servers](gamelift_quickstart_customservers_designbackend.md "gamelift_quickstart_customservers_designbackend.md")
- [Deploy hosting fleets for Amazon GameLift Servers](fleets-intro.md "fleets-intro.md")
- [Configure game session placement](queues-intro.md "queues-intro.md")
- [Customize to your game hosting solution](customize-solution-intro.md "customize-solution-intro.md")
