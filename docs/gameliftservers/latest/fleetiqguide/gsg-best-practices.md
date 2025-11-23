# Amazon GameLift Servers FleetIQ best practices

Amazon GameLift Servers FleetIQ is a low-level logic layer that helps you manage Amazon EC2 resources for game
hosting. In particular, Amazon GameLift Servers FleetIQ optimizes the use of Spot Instances that are viable for
game hosting by minimizing the chance that game sessions might be interrupted. It also
provides basic game hosting functionality to track available game servers and route gameplay
to low-cost, high-viability game servers.

Amazon GameLift Servers FleetIQ as a standalone feature does not provide advanced features that are offered with
the fullly managed Amazon GameLift Servers solution, which also uses FleetIQ to minimize hosting costs. If you
need features such as matchmaking, latency-based player routing, game session and player
session management, and versioning, take a look at the Amazon GameLift Servers solutions.

Here are some best practices that can help you get the most benefit from Amazon GameLift Servers FleetIQ.

- **Use Amazon GameLift Servers FleetIQ for session-based games.** Amazon GameLift Servers FleetIQ
  works best when it is constantly directing players onto instances that are least
  likely to have game session interruptions. Maintaining long-lived sessions
  interferes with the Amazon GameLift Servers FleetIQ balancing process, which increases the likelihood that
  games sessions might be interrupted. The ideal workflow is for players to go from
  matchmaking (or server selection) into gameplay. When the game ends, players go back
  to matchmaking and are routed to another game server on a new instance. We recommend
  using Amazon GameLift Servers FleetIQ for games with sessions under two hours.
- **Provide many instance types to choose from.** When
  you set up a game server group, you provide a list of instance types to be used. The
  more instance types that you include, the greater flexibility Amazon GameLift Servers FleetIQ has to use
  Spot Instances with high viability for game hosting. For example, you might list
  multiple sizes within the same instance family (c5.large, c5.xlarge, c5.2xlarge,
  c5.4xlarge). With larger instances, you can run more game servers on each instance,
  potentially lowering costs. With smaller instances, autoscaling can react faster to
  changes in player demand. Keep in mind that the list of desired instance types is
  not prioritized—an Amazon EC2 Auto Scaling group will use a balance of viable instance types to
  maintain the group's resiliency.
- **Test your game on all instance types.** Ensure that
  your game server runs properly on every instance type that you configure for your
  game server group.
- **Use instance capacity weighting.** If you configure
  your game server group to use a range of instance sizes (such as c5.2xlarge,
  c5.4xlarge, c5.12xlarge), include capacity weighting information for each instance
  type. For more information, see [Instance Weighting for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/asg-instance-weighting.md "../../../autoscaling/ec2/userguide/asg-instance-weighting.md") in the _Amazon EC2 Auto Scaling User Guide_.
- **Place your game sessions using Amazon GameLift Servers FleetIQ.** When
  placing groups of players with game servers, use the Amazon GameLift Servers API
  `ClaimGameServer()`. Amazon GameLift Servers FleetIQ avoids placing players on instances
  with a higher chance of game session interruptions.
- **Report game server status to Amazon GameLift Servers FleetIQ.**
  Periodically report server health and utilization status with the Amazon GameLift Servers API
  `UpdateGameServer()`. Maintaining accurate game server status helps
  Amazon GameLift Servers FleetIQ place gameplay more efficiently. It also helps avoid terminating instances
  with active gameplay during Spot balancing activity.
- **Set up an auto scaling policy.** You can create a
  target-tracking scaling policy that maintains your hosting capacity based on player
  utilization and anticipated demand. The Amazon GameLift Servers FleetIQ metric
  `PercentUtilizedGameServers` is a measure of how much of your hosting
  capacity is currently in use. Most games want to maintain a buffer of unused game
  servers so that new players can get into a game quickly. You can create a scaling
  policy that maintains a certain buffer size, adding or removing instances as player
  demand fluctuates. For more information, see [Target Tracking Scaling
  Policies](../../../autoscaling/ec2/userguide/as-scaling-target-tracking.md "../../../autoscaling/ec2/userguide/as-scaling-target-tracking.md") in the Amazon EC2 Auto Scaling User Guide.
- **Use different AWS accounts for development and production
  environments.** Separating your development and production
  configurations across accounts can reduce the risk of misconfiguration impacting
  live players.
- **Enable game session protection for game server groups in
  production.** To protect your players, turn on game session protection
  and prevent active game sessions from being terminated early due to scaling or
  balancing activity.
- **Test your game on EC2 before integrating it with
  Amazon GameLift Servers FleetIQ.** We recommend getting your game up and running on EC2 and
  fine-tune your configuration first. You can then create a game server group using
  the same launch template and AMI.

If you're using Kubernetes, we recommend first getting standard EC2 instances
added to your Kubernetes cluster, then create a game server group using the launch
template you create for worker nodes in your Kubernetes cluster. If you're using
EKS, create your EKS cluster and game server group separately. For the game server
group, use the EKS-optimized AMI with the appropriate user data and the launch
template configuration used for your EKS integration. See more details about EKS
worker nodes and the EKS optimized AMI in the [Amazon EKS-Optimized Linux
AMI](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md") guide.

- **Use the game server group balancing strategy
  `ON_DEMAND_ONLY` for reliable game server
  availability.** With this balancing strategy in force, no Spot
  Instances are used. This is a useful tool to ensure server availability when you
  need it most, such as during feature launches or other special events. You can
  swtich a game server group from a Spot to an On-Demand strategy as needed.
  Also review these AWS best practices:

- [Best Practices for
  Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-best-practices.md "../../../AWSEC2/latest/UserGuide/ec2-best-practices.md")
- [Best Practices for Amazon EC2
  Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/gs-best-practices.md "../../../autoscaling/ec2/userguide/gs-best-practices.md")
