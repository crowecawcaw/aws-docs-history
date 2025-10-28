# Amazon GameLift Servers solutions

Amazon GameLift Servers offers a range of solutions for developers who are building session-based multiplayer games.

###### Solutions for game developers

- [Amazon GameLift Servers hosting options](#gamelift-intro-flavors-hosting "#gamelift-intro-flavors-hosting")
- [Amazon GameLift Servers FlexMatch for
  matchmaking](#gamelift-intro-flavors-flexmatch "#gamelift-intro-flavors-flexmatch")
- [Amazon GameLift Servers FleetIQ for self-managed Amazon EC2
  hosting](#gamelift-intro-flavors-fleetiq "#gamelift-intro-flavors-fleetiq")
- [Amazon GameLift Servers Realtime with customizable
  server logic](#gamelift-intro-flavors-realtime "#gamelift-intro-flavors-realtime")

## Amazon GameLift Servers hosting options

When working with Amazon GameLift Servers to operate your game servers, you have several options for
where and how your game servers are hosted. Whether you want to use hosting resources
you already have or want to set up cloud-based hosting managed by Amazon GameLift Servers, you can build a
seamless hosting experience for your players.

[Managed EC2](#gamelift-intro-flavors-hosting-managed-ec2 "#gamelift-intro-flavors-hosting-managed-ec2")

[Managed containers](#gamelift-intro-flavors-hosting-managed-containers "#gamelift-intro-flavors-hosting-managed-containers")

[Hybrid hosting](#gamelift-intro-flavors-hosting-hybrid "#gamelift-intro-flavors-hosting-hybrid")

[Anywhere
hosting](#gamelift-intro-flavors-hosting-anywhere "#gamelift-intro-flavors-hosting-anywhere")

### Managed EC2

With Amazon GameLift Servers managed EC2 hosting, you can offload most of the work of
managing your game servers. Choose compute resources from a wide selection of Amazon EC2
instance types. Integrate your game projects and let Amazon GameLift Servers handle the details. For
more about managed hosting, see [How Amazon GameLift Servers works](gamelift-howitworks.md "gamelift-howitworks.md").

[Start developing an Amazon GameLift Servers managed hosting solution for your game.](gamelift-roadmap-managed.md "gamelift-roadmap-managed.md")

###### Key features

- Host multiplayer games that run on Amazon Linux or Windows Server operating
  systems.
- Provide low-latency gameplay experiences to your players, wherever
  they are. Deploy game servers globally across any of the AWS Regions
  and Local Zones that Amazon GameLift Servers supports. For a complete list, see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md").
- Use Amazon GameLift Servers intelligent game session placement so that players always
  get the best possible hosted player experience. You can rely on Amazon GameLift Servers
  decision-making, or you can customize around placement criteria such as
  cost, player latency, and geographic locations.
- Choose how to scale your hosting resources to meet player demand.
  Manage capacity manually or set up automatic scaling. With target-based
  auto scaling, you can maintain a dynamically sized buffer of idle
  capacity, which helps you control costs while ensuring that new players
  can get into games with minimal waiting.
- Let Amazon GameLift Servers deploy and manage your cloud-based game servers. Amazon GameLift Servers
  creates resources as you need them, installs your game server software,
  and automatically starts processes to host game sessions for players.
  Set up custom health tracking and let Amazon GameLift Servers detect and resolve
  poor-performing resources.
- Take advantage of Amazon GameLift Servers monitoring capabilities to assess performance
  and usage. You can track metrics on factors such as hardware
  performance, game session placement efficiency, and server process life
  cycles. You can track active game sessions and player sessions to
  observe usage over time. You can also download and store game session
  logs.
- For production hosting, automate your game hosting resource management
  and deployments using AWS CloudFormation templates for Amazon GameLift Servers and the AWS Cloud Development Kit (AWS CDK).
  Take advantage of continuous integration and continuous delivery (CI/CD)
  tools and services such as AWS CodePipeline.

### Managed containers

Amazon GameLift Servers provides a complete cloud hosting solution for containerized
game servers. With Amazon GameLift Servers managed containers, you can take advantage of the core
benefits of container usage, such as portability, agility, and fault tolerance. The
following features are available with managed container fleets.

[Start developing an Amazon GameLift Servers managed
hosting solution for your containerized game server.](gamelift-roadmap-containers.md "gamelift-roadmap-containers.md")

###### Key features

- Develop a custom architecture with lightweight containers to run your game server software on
  Amazon GameLift Servers Linux-based hosting resources.
- Use Docker tools to create a Linux-based container image. Store images for deployment in an
  Amazon Elastic Container Registry (Amazon ECR) repository.
- Deliver low-latency player experiences by deploying container
  fleet resources to any AWS Region or Local Zone that Amazon GameLift Servers supports.
  See [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md").
- Manage fleet life-cycle with tools to model game server versions and
  deploy fleet updates.
- Use Amazon GameLift Servers game session placement features, including queues and FlexMatch
  matchmaking, to find the best possible game session matches for your
  players.
- Test your game server and container architecture with the Amazon GameLift Servers service using an Anywhere
  fleet. Test your game locally or on a cloud-based test environment.
- Track game hosting performance with container-specific performance
  metrics. Monitor the health of your fleet resources using hardware
  metrics.
- Manage container fleet resources using AWS CloudFormation templates for Amazon GameLift Servers.

### Hybrid hosting

Use the Amazon GameLift Servers service with a combination of Amazon GameLift Servers managed hosting and
Anywhere self-managed hosting. A hybrid approach lets you build the solution
you need right now while also preparing for where you need to be in the future.
Common scenarios where a hybrid solution makes sense include:

- **Expand your hosting solution to the
  AWS Cloud.** Supplement the capabilities of your existing
  hosting solution (on-premises hardware or other cloud-based hosting) by
  adding Amazon GameLift Servers managed hosting. With managed hosting, you can increase
  your hosting capacity or add "burst" capacity to rapidly scale up and
  pay only for resources when you need them. You can also take advantage
  of the Amazon GameLift Servers service's global footprint to reach more players around the
  world and provide the low-latency multiplayer experience they
  expect.
- **Prepare for migration to cloud-based
  hosting.** If you're considering or planning to migrate to
  the AWS Cloud (instead of upgrading your own hardware), a hybrid
  hosting solution is a viable way for you to make the transition as
  gradually as you need to.
- **Boost latency for players in locations beyond
  those serviced by Amazon GameLift Servers.** If you're already using Amazon GameLift Servers
  managed hosting, you might need to support players in certain
  situations. For example, you might want to reach players in unusually
  remote locations or significantly reduce latency to those areas. Add
  custom hosting locations and use Amazon GameLift Servers Anywhere to manage those
  locations along with your managed hosting resources.

[Start developing an Amazon GameLift Servers hybrid hosting solution for your game.](gamelift-roadmap-hybrid.md "gamelift-roadmap-hybrid.md")

Key features

- Use the same game client and server components with both managed and
  self-managed hosting resources. Provide a unified player experience
  across all hosting resources.
- Use the same FlexMatch matchmakers to place matches across all hosting
  resources.
- Centrally manage your hybrid hosting resources together while you
  deploy them across the globe.
- As player demand fluctuates, manage game session loads seamlessly
  across managed and self-managed resources.
- With the Amazon GameLift Servers Agent, you can use the same tooling to manage game
  server life cycles on all types of hosting resources.
- Gather game and player metrics and logs across all hosting resources.
  Take advantage of Amazon GameLift Servers features and other AWS services to combine
  data and develop cohesive observability solutions.

### Anywhere

hosting

Use Amazon GameLift Servers Anywhere fleets with Amazon GameLift Servers game session management, including
matchmaking, to host your custom game servers wherever you want to.
Anywhere fleets are particularly useful as test environments
for rapid, iterative game development. Set up an Anywhere fleet
for your own local workstation or a set of cloud-based hosting resources. For
production hosting, you might use a hybrid approach with Anywhere
fleets for your on-premises hardware supplemented by Amazon GameLift Servers managed
fleets.

For more information about testing with Anywhere, see [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md"). For more
information about setting up an Anywhere fleet, see [Setting up a hosting fleet with Amazon GameLift Servers](fleets-intro.md "fleets-intro.md").

[Start developing an Amazon GameLift Servers Anywhere hosting solution for your game.](gamelift-roadmap-anywhere.md "gamelift-roadmap-anywhere.md")

###### Key features

- Perform fast, iterative testing as you develop your multiplayer
  games.
- Use Amazon GameLift Servers tools to manage game servers that are hosted on your own
  hardware.
- Take advantage of available hardware that is closest to your players,
  anywhere.

## Amazon GameLift Servers FlexMatch for

matchmaking

Use FlexMatch to build custom rule sets to define multiplayer matches for your
game. FlexMatch uses rule sets to compare compatible players for each match and provide
players with the ideal multiplayer experience.

For more information about FlexMatch, see [What is Amazon GameLift Servers FlexMatch?](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md")

###### Key features

- Balance match creation speed and match quality.
- Match players or teams based on defined characteristics.
- Define rules to place players into matches based on latency.

## Amazon GameLift Servers FleetIQ for self-managed Amazon EC2

hosting

Use FleetIQ game server groups to work directly with your hosting resources in Amazon EC2 and Amazon EC2 Auto Scaling.
This provides the benefit of Amazon GameLift Servers optimizations for inexpensive, resilient game
hosting. This solution is for game developers who need more flexibility than what
fully managed Amazon GameLift Servers solutions provide.

For information about how FleetIQ works with Amazon EC2 and EC2 Auto Scaling for game hosting,
see the [Amazon GameLift ServersFleetIQ Developer Guide](../fleetiqguide/gsg-intro.md "../fleetiqguide/gsg-intro.md").

###### Key features

- Get optimized Spot Instance balancing using the FleetIQ algorithm.
- Use player routing features to manage your game server resources
  efficiently, and provide a better player experience for joining
  games.
- Automatically scale hosting capacity based on player usage.
- Directly manage Amazon EC2 instances in your own AWS account.
- Use any of the supported game server executable formats, including
  Windows, Linux, containers, and Kubernetes.

## Amazon GameLift Servers Realtime with customizable

server logic

Use Realtime servers to host games that don't need a custom-built game server. This
lightweight server solution provides game servers that you can configure to fit your
game. You can host Realtime servers using an Amazon GameLift Servers managed hosting solution.

For more information about hosting with Amazon GameLift Servers Realtime, see [Integrating games with Amazon GameLift Servers Realtime](realtime-intro.md "realtime-intro.md").

###### Key features

- Use Amazon GameLift Servers management features, including auto scaling, multi-location
  queues, and game session placement.
- Use Amazon GameLift Servers hosting resources and choose the type of AWS computing
  hardware for your fleets.
- Take advantage of a full network stack for game client and server
  interaction.
- Get core game server functionality with customizable server logic.
- Make live updates to Realtime configurations and server logic.
