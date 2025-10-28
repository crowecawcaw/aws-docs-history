# Game server

Game servers represent one of the most important aspects of the compute infrastructure
for your game. _Game servers_, sometimes referred to as dedicated game
servers, are used when developing a multiplayer game or when server authoritative processing
of gameplay events is required. The game server is at the center of the game architecture,
serving as the location where the core logic executes, which includes managing player and
game state as well as managing the interactions between the connected game clients and the
game server. The game server is usually one of the most performance-sensitive aspects of a
game architecture because it is responsible for processing the inputs from a player’s game
client and properly distributing it to any other connected players in real-time. A badly
performing game server can impact the overall performance of the game experience. Therefore,
it is important to ensure that the game server performance is optimized and has sufficient
capacity, especially when the game is launched and during peak gameplay periods.

For the purposes of this document, a game server (or game server instance) refers to the
compute resources, such as a virtual machine (VM), that hosts one more game server
processes. A game server process represents a single instance of your game server build
hosting a game session, which is an instance of your running game that players can connect
to via a player session. For this reason, we refer to _game server
process_ and _game session_ interchangeably in this document,
due to the implied one-to-one relationship between a game session and the game server
process that is hosting it. In AWS, there are multiple options for compute resources to
host game servers, all of which provide access to scalable cloud-based capacity through
elastic provisioning of resources.

[Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") provides cloud-based virtual servers,
known as instances, with support for multiple versions of Linux and Windows. You can create
instances and manage them directly like any other server or virtual machine (VM). Typically,
multiple game server processes are deployed to an instance in order to improve efficiency
and reduce costs. Amazon EC2 is a good choice for game servers if you want the most control over
the compute infrastructure.

[Amazon Amazon GameLift Servers](https://aws.amazon.com/gamelift/ "https://aws.amazon.com/gamelift/") provides a fully-managed solution for dedicated game server hosting in the
cloud as well as additional features such as matchmaking with Amazon GameLift Servers FlexMatch. Amazon GameLift Servers
provides a layer of abstraction on top of Amazon EC2 to make game server management easier and is
available in most AWS Regions so that you can host game servers close to players to reduce
latency, achieve high availability, and significantly reduce costs by using Spot Instances.
While Amazon GameLift Servers can be integrated into existing game backends, it is especially useful for game
developers who do not want to develop their own game server management and matchmaking
solutions and want a solution that is managed by AWS and can scale as their game
grows.

[Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") is a fully managed
container orchestration service that enables you to run Docker-based containers, and [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/") enables you to run Docker-based
containers that are built using Kubernetes. Using container technologies such as those
provided by Amazon ECS and Amazon EKS can help you to improve the utilization of your compute
infrastructure by allowing you to efficiently pack many game server processes or other game
application instances into an EC2 instance. The use of containers can also improve developer
productivity by enabling applications to be hosted using the same Docker image operating
runtime that is used by developers on their local machines during development. You can
further reduce operational overhead by using [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/"),
which is a serverless compute
platform for running containers and is compatible with both Amazon EKS and Amazon ECS. Fargate is
best suited for use cases where you want to run game servers in containers without
responsibility for operating the underlying instances that the containers run on.

[AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/") allows you to run AWS services in any data center or on-premises
facility, which can enable games to run in on-premises environments and AWS using the same services
to support a hybrid cloud adoption strategy.
[AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/") serve
as extensions of AWS Regions to allow
you to run your game servers and other latency-sensitive workloads closer to your players or development teams.
Additionally, to reduce global network latency for your game servers,
[AWS Global Accelerator](https://aws.amazon.com/global-accelerator/ "https://aws.amazon.com/global-accelerator/") can be used to
improve performance for player traffic to your game servers.

[AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") is a serverless compute service that allows you to run code without
provisioning or managing servers and is useful for asynchronous game server use cases, such
as turn-based games. Lambda is also well suited for games with lightweight compute requirements, a small codebase, and
where gameplay functionality can be designed using a stateless microservices architecture.
Lambda functions run on an event-driven per-request
basis, rather than running as part of a long-running game server process. Lambda provides the most
runtime abstraction of the options described in this paper because the underlying application is
provided out-of-the-box for developers to choose from to host their code.

When selecting your approach for game server hosting, you need to consider various
requirements including operational overhead, legacy codebases, performance requirements, and
scale. Amazon EC2 instances and containers are good options for legacy codebases, as they require
the smallest amount of change to move to the cloud. EC2 instances also allow you to dedicate all the
resources of a compute instance, while containers can make management and high utilization
easier to achieve. Serverless functions offer the highest level of abstraction and allow you
to define code that only runs in response to events, which can reduce costs.
