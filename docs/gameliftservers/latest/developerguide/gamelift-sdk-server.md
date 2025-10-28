# Integrate your game server with Amazon GameLift Servers

After your custom game server is deployed and running on Amazon GameLift Servers instances, it must be
able to interact with Amazon GameLift Servers (and potentially other resources). This section describes how to
integrate your game server software with Amazon GameLift Servers.

###### Note

These instructions assume that you've created an AWS account and that you have an
existing game server project.

The topics in this section describe how to handle the following integration tasks:

- Establish communication between Amazon GameLift Servers and your game servers.
- Generate and use a TLS certificate to establish a secure connection between game
  client and game server.
- Provide permissions for your game server software to interact with other AWS
  resources.
- Allow game server processes to get information about the fleet that they're
  running on.

###### Topics

- [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
- [Communicate with other AWS resources from
  your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md")
