# Amazon GameLift Servers Anywhere fleets

Use Anywhere fleets when you want to take advantage of Amazon GameLift Servers features with
your own hosting resources. Anywhere fleets are commonly used as test environments for
iterative development or alongside managed fleets in a hybrid hosting solution.

An Anywhere fleet consists of a set of compute resources (virtual or physical) that you
supply and manage. Computes can reside in any geographic location with connectivity, from a
local laptop to remote outposts. When setting up an Anywhere fleet, you add computes to the
fleet by registering them through Amazon GameLift Servers. Each compute is registered with its IP address (or
DNS name) so that Amazon GameLift Servers can establish a connection with it.

You deploy game server software to an Anywhere fleet by installing it on each compute and
launching game server processes. Each launched game server process establishes a connection
to the Amazon GameLift Servers service and reports readiness to host a game session. You can use your existing
configuration management and deployment tooling to handle initial deployment and host
management tasks. There are a few additional tasks required for use with Amazon GameLift Servers, including:

- Register and deregister computes to add or remove them from the fleet.
- Maintain up-to-date authentication tokens on all computes. Server processes on the
  compute use them when connecting to the Amazon GameLift Servers service.

###### Note

Optionally deploy your Anywhere fleet with the Amazon GameLift Servers Agent to automate these key
management tasks. See [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md "integration-dev-iteration-agent.md").

See these topics about how to set up and maintain Anywhere fleets:

- [Development roadmap for hosting with Amazon GameLift Servers Anywhere](gamelift-roadmap-anywhere.md "gamelift-roadmap-anywhere.md")
- [Development roadmap for hybrid hosting
  with Amazon GameLift Servers](gamelift-roadmap-hybrid.md "gamelift-roadmap-hybrid.md")
- [Set up for iterative development with Amazon GameLift Servers Anywhere](integration-dev-iteration.md "integration-dev-iteration.md")
- [Create an Amazon GameLift Servers Anywhere fleet](fleets-creating-anywhere.md "fleets-creating-anywhere.md")
- [How Amazon GameLift Servers fleet creation works](fleets-intro.md#fleets-creation-workflow "fleets-intro.md#fleets-creation-workflow")
- [Update an Amazon GameLift Servers fleet configuration](fleets-editing.md "fleets-editing.md")

## Anywhere fleet creation workflow

For Anywhere fleets, Amazon GameLift Servers sets up the fleet resource only. You set up and register
computes with the fleet, and you install game server software and start game server
processes to host game sessions.

1. Amazon GameLift Servers creates the fleet resource in the fleet's home Region. Fleet status and
   custom location status are set to **New**.
2. Amazon GameLift Servers begins writing events to the fleet event log.
3. After the fleet resource is created. Amazon GameLift Servers sets the fleet status to **Active**. At this point, you can register new computes with
   the fleet.
