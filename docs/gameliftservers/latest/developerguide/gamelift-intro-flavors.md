# Amazon GameLift Servers game hosting options

Amazon GameLift Servers offers a range of options for hosting game servers for session-based
multiplayer games. Whether you want to set up cloud-based hosting managed by Amazon GameLift Servers or
incorporate hosting resources that you already have, you can work with Amazon GameLift Servers to build the
hosting solution you need for your players. For more details about what a game hosting
solution looks like, see [How hosting with Amazon GameLift Servers works](gamelift-howitworks.md "gamelift-howitworks.md").

###### Topics

- [Managed EC2](#gamelift-intro-flavors-hosting-managed-ec2 "#gamelift-intro-flavors-hosting-managed-ec2")
- [Managed containers](#gamelift-intro-flavors-hosting-managed-containers "#gamelift-intro-flavors-hosting-managed-containers")
- [Anywhere
  hosting](#gamelift-intro-flavors-hosting-anywhere "#gamelift-intro-flavors-hosting-anywhere")
- [Hybrid hosting](#gamelift-intro-flavors-hosting-hybrid "#gamelift-intro-flavors-hosting-hybrid")

## Managed EC2

Offload the work of managing your production game servers onto Amazon GameLift Servers with
managed EC2 hosting. Take advantage of optimizations for multiplayer game servers while
still relying on the high performance and reliability of Amazon Elastic Compute Cloud (Amazon EC2) and AWS
global computing infrastructure.

[Start building an Amazon GameLift Servers managed EC2
hosting solution](gamelift-roadmap-managed.md "gamelift-roadmap-managed.md")

###### Characteristics

- Host multiplayer game servers that run on Amazon Linux or Windows Server operating
  systems.
- Use Amazon GameLift Servers to deploy and manage your custom game servers to hosting resources
  AWS Cloud. Choose the hardware type and where to deploy it, and configure
  additional details only where you need to.
- Configure the runtime process manager to automatically maintain game server
  processes as needed to host game sessions.
- Set up custom health tracking to help Amazon GameLift Servers detect and resolve poor-performing
  game servers.
- Take advantage of Amazon GameLift Servers performance monitoring. Track metrics such as
  hardware performance and server process life cycles. You can also download and
  store game session logs.
- Use Amazon GameLift Servers to manage access between game server processes and other AWS
  resources.
- For production hosting, automate game hosting deployments and
  management with AWS CloudFormation templates and the AWS Cloud Development Kit (AWS CDK). Take advantage of
  continuous integration and continuous delivery (CI/CD) tools and services such
  as AWS CodePipeline.

## Managed containers

Amazon GameLift Servers provides a complete cloud hosting solution for containerized
game servers, so you can take advantage of the core benefits of container usage, such as
portability, agility, and fault tolerance. As with managed EC2 hosting , managed
container hosting deploys and runs your containers on Amazon EC2 instances.

[Start developing an Amazon GameLift Servers managed
hosting solution for your containerized game server.](gamelift-roadmap-containers.md "gamelift-roadmap-containers.md")

###### Characteristics

- Develop a custom architecture with lightweight containers to run your game server build,
  dependencies and auxillary software.
- Use Docker tools to create a Linux-based container image. Store images in an Amazon Elastic Container Registry (Amazon ECR)
  repository for deployment.
- Use Amazon GameLift Servers to deploy and manage your custom game servers to hosting resources
  AWS Cloud. Choose the hardware type and where to deploy it, and configure
  additional details only where you need to.
- Manage hosting fleet life-cycle with tools to model game server versions.
  Deploy game server updates and other configuration changes as needed.
- Track game hosting performance with container-specific performance
  metrics. Monitor the health of your fleet resources using hardware
  metrics.
- Manage container fleet resources using AWS CloudFormation templates for Amazon GameLift Servers.

## Anywhere

hosting

With Anywhere hosting, you can take advantage of Amazon GameLift Servers game session management
features, including matchmaking and game session metrics, to host game servers wherever
you want to. Self-manage your game server deployments, game server health monitoring,
and capacity scaling.

###### Note

Anywhere fleets are particularly useful as test environments for
rapid, iterative game development. Set up an Anywhere fleet for your
own local workstation or a cloud-based hosting resource. For more information about
testing with Anywhere, see [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md").

[Start developing an Amazon GameLift Servers Anywhere hosting solution for your game.](gamelift-roadmap-anywhere.md "gamelift-roadmap-anywhere.md")

###### Characteristics

- Deploy game servers on your own hardware, on-premises infrastructure, or other
  cloud providers. Make use of available hardware close to your players,
  anywhere.
- Use Amazon GameLift Servers session management features to monitor game server availability,
  start new game sessions, and join players to game session slots.

## Hybrid hosting

For production hosting, you might choose a hybrid approach, with
Anywhere fleets for the hosting resources you supply and manage, and
Amazon GameLift Servers managed fleets filling in where needed. A hybrid solution uses the same processes
to start game sessions and connect players to deliver a seamless player experience. You
can monitor and collect usage metrics for all hosting, regardless of resource
type.

Common scenarios where a hybrid solution makes sense:

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
  hosting.** If you're considering or planning to migrate to the
  AWS Cloud, a hybrid hosting solution is a viable way for you to make the
  transition as gradually as you need to. It lets you build the solution you need
  right now while preparing for where you want to be in the future.
- **Lower latency for players in locations beyond
  those serviced by Amazon GameLift Servers.** If you're already using Amazon GameLift Servers managed
  hosting, you might need to support players in unusual situations. For example,
  you might want to better reach players in unusually remote locations or support
  players with special access needs. Add custom hosting locations and use Amazon GameLift Servers
  Anywhere to support those locations along with your managed hosting
  resources.
-

[Start developing an Amazon GameLift Servers hybrid hosting solution for your game.](gamelift-roadmap-hybrid.md "gamelift-roadmap-hybrid.md")
