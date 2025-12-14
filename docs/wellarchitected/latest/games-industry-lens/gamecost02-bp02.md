# GAMECOST02-BP02 Optimize the number of game sessions hosted on

each game server instance to optimize costs

Optimize the number of game sessions hosted per server instance to
achieve better compute utilization and reduce compute infrastructure
costs. 

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To optimize costs, game developers should maximize the number of
game sessions hosted on the same physical or virtual server, also
known as the packing density of their game servers. This is
achieved by increasing the number of game server processes that
can be simultaneously hosted on an instance.

A single game server process should not usually require the use of
the entire resources available on the EC2 instance. This is one of
the most important ways to reduce compute costs for a game and
requires the use of software that can spawn and manage multiple
server processes on the EC2 Instance on separate ports.

For example, Amazon GameLift has a quota on the maximum number of
game server processes per instance, which you should strive to
utilize so that you can reduce hosting costs. For more
information, see
[Amazon
GameLift Servers endpoints and quotas](../../../general/latest/gr/gamelift.md "../../../general/latest/gr/gamelift.md") for details on the
current quota for maximum game server processes per instance.

As an alternative to deploying game server processes on virtual
machines such as EC2 instances, it is becoming popular for game
developers to run their game servers as container-based
applications using container orchestration solutions. Game
developers can use
[Amazon Elastic Container Service](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") (Amazon ECS) or
[Guidance
for Game Server Hosting Using Agones and Open Match on Amazon EKS](https://aws.amazon.com/solutions/guidance/game-server-hosting-using-agones-and-open-match-on-amazon-eks/ "https://aws.amazon.com/solutions/guidance/game-server-hosting-using-agones-and-open-match-on-amazon-eks/"). Another option is
[Game
Server Hosting on AWS Fargate](https://aws.amazon.com/blogs/gametech/game-server-hosting-on-aws-fargate/ "https://aws.amazon.com/blogs/gametech/game-server-hosting-on-aws-fargate/"), a serverless compute engine
that works with both ECS and EKS, enabling you to focus on your
game without having to manage the underlying infrastructure.

Container solutions provide job scheduling functionality that can
automatically find an available container instance in the cluster
to host your game server container based on resource requirements
and other placement logic that you specify. However, it is
important to consider how you will manage the scaling and player
placement behavior in a way that doesn't disrupt active player
sessions.

### Implementation steps

- Increase packing density by running multiple game server
  processes per EC2 instance using separate ports and process
  management software.
- Use Amazon GameLift or container solutions like ECS, EKS, or
  AWS Fargate to manage game server processes efficiently and
  reduce infrastructure costs.
- Continuously monitor resource utilization to refine packing
  density and maintain cost-efficiency without compromising
  player experience.
