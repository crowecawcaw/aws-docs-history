# How Amazon GameLift Servers works

This topic describes how Amazon GameLift Servers manages dedicated hosting for your multiplayer game servers
and makes them available to players. It outlines how core features work.

## Hosting game servers

With Amazon GameLift Servers, you can host your game servers in several different ways: Managed Amazon GameLift Servers,
Amazon GameLift Servers FleetIQ, and Amazon GameLift Servers Anywhere. For more information about Amazon GameLift Servers FleetIQ, see [What is
Amazon GameLift Servers FleetIQ?](../fleetiqguide/gsg-intro.md "../fleetiqguide/gsg-intro.md")

You can design a fleet to fit your game's needs. For more information about designing
a fleet, see [Customize your Amazon GameLift Servers EC2 managed fleets](fleets-design.md "fleets-design.md").

###### Managed Amazon GameLift Servers

With managed Amazon GameLift Servers, you can host your game servers on Amazon GameLift Servers virtual computing
resources, called **instances**. Set up your hosting
resources by creating a **fleet** of instances and
deploying them to run your game servers.

###### Amazon GameLift Servers Anywhere

With Amazon GameLift Servers Anywhere, you can host your game servers on compute that you manage.
Set up your hosting resources by creating an Anywhere fleet that references your
compute.

###### Fleet aliases

An **alias** is a designation that you can transfer
between fleets, making it a convenient way to have a generic fleet location. You can
use an alias to switch game clients from using one fleet to another without changing
your game client. You can also create a terminal alias that you point to
content.

## Running game sessions

After you deploy your game server build to a fleet and Amazon GameLift Servers launches game server
processes on each instance, the fleet can host game sessions. Amazon GameLift Servers starts new game
sessions when your game client service sends a placement request to the backend service
or to Amazon GameLift Servers.

###### Game session placement and the FleetIQ algorithm

Queues use the FleetIQ algorithm to select an available game server to
host a new game session. The key component for game session placement is the Amazon GameLift Servers
game session **queue**. You assign a game session queue
a list of fleets, which determines where the queue can place game sessions. For more
information about game session queues and how to design them for your game, see
[Customize a game session queue](queues-design.md "queues-design.md").

###### Optimizing game session placement with UDP ping beacons

Using Amazon GameLift Servers UDP ping beacons, you can calculate roundtrip latency for UDP packets between
players and game servers in different locations to help pick the optimal location
for a game session. For more information about UDP ping beacons and how you can use them to
measure latency, see [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md").

- For games that use game session queues for placement, the placement request
  can include latency data, which the queue automatically uses to prioritize
  placement locations. You can further customize prioritization and can set up
  policies including latency value caps. See [Prioritize game session placement](queues-design-priority.md "queues-design-priority.md").
- For games that don’t use game session queues but have fleets with multiple
  locations, you can evaluate latency data and choose the best available location
  before making a game session request to Amazon GameLift Servers. See the Get and Create game
  sessions sections in [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").
- If you're using FlexMatch for matchmaking, you can set match rules to use latency
  data. See [Request
  matchmaking for players](../flexmatchguide/match-client-start.md "../flexmatchguide/match-client-start.md") and the [Latency rule](../flexmatchguide/match-rules-reference-ruletype.md#match-rules-reference-ruletype-latency "../flexmatchguide/match-rules-reference-ruletype.md#match-rules-reference-ruletype-latency") section of FlexMatch rule types in the
  Amazon GameLift Servers FlexMatch Developer Guide.

###### Player connections to games

As part of the game session placement process, the queue or game session prompts
the selected game server to start a new game session. The game server responds to
the prompt and reports back to Amazon GameLift Servers when it's ready to accept player connections.
Amazon GameLift Servers then delivers connection information to the backend service or game client
service. Your game clients use this information to connect directly to the game
session and begin gameplay.

## Scaling fleet capacity

When a fleet is active and ready to host game sessions, you can adjust your fleet
capacity to meet player demand. We recommend that you find a balance between all
incoming players finding a game quickly and overspending on resources that sit
idle.

Amazon GameLift Servers provides a highly effective auto scaling tool, or you can manually set fleet
capacity. For more information, see [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md").

###### Auto scaling

Amazon GameLift Servers provides two methods of auto scaling:

- [Target-based auto scaling](fleets-autoscaling-target.md "fleets-autoscaling-target.md")
- [Auto scale with rule-based policies](fleets-autoscaling-rule.md "fleets-autoscaling-rule.md")

###### Additional scaling features

- **Game session protection** – Prevent
  Amazon GameLift Servers from ending game sessions that are hosting active players during a
  scale-down event.
- **Scaling limits** – Control overall
  instance usage by setting minimum and maximum limits on the number of instances
  in a fleet.
- **Suspending auto scaling** – Suspend auto
  scaling at the fleet location level without changing or deleting your auto
  scaling policies.
- **Scaling metrics** – Track a fleet's
  history of capacity and scaling events.

## Monitoring Amazon GameLift Servers

When you have fleets up and running, Amazon GameLift Servers collects a variety of information to help
you monitor the performance of your deployed game servers. You can use this information
to optimize your use of resources, troubleshoot issues, and gain insight into how
players are active in your games. Amazon GameLift Servers collects the following:

- Fleet, location, game session, and player session details
- Usage metrics
- Server process health
- Game session logs

For more information about monitoring in Amazon GameLift Servers, see [Monitoring Amazon GameLift Servers](monitoring-overview.md "monitoring-overview.md").

## Using other AWS resources

Your game servers and applications can communicate with other AWS resources. For
example, you might use a set of web services for player authentication or social
networking. For your game servers to access AWS resources that your AWS account
manages, explicitly allow Amazon GameLift Servers to access your AWS resources.

Amazon GameLift Servers provides a couple of options for managing this type of access. For more
information, see [Communicate with other AWS resources from
your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").
