# GAMESUS02-BP01 Select managed services for appropriate compute

workloads

Architect your game backend services to use managed services for
event driven or highly variable traffic workloads. Managed services
shift the management of infrastructure to AWS and distributes the
environmental impact across multiple users because of the
multi-tenanted control planes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS services like AWS Lambda, AWS Fargate (Containers), and Amazon
Gamelift (Game server orchestration) can run code, containers, or
orchestrate your game servers without having to manage the
underlying infrastructure. These services automatically scale
based on player demand and you're only charged for the resources
you consume. Because the underlying infrastructure is managed on
your behalf, you are able to focus solely on your games and
backend services' requirements.

You can use [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") to run code without provisioning or managing
servers. Lambda runs your code on a high-availability compute
infrastructure and performs the administration of the compute
resources, including server and operating system maintenance,
capacity provisioning and automatic scaling, and logging. With
Lambda, you need to supply your code in one of the language
runtimes that Lambda supports. Lambda is useful for processing
game events, player authentication, in-game purchase processing,
and matchmaking requests. Lambda automatically scales based on the
number of events and can handle unexpected spikes in traffic.

[AWS Fargate](https://aws.amazon.com/fargate/?nc=sn&loc=0 "https://aws.amazon.com/fargate/?nc=sn&loc=0") is a serverless compute engine for containers that
works with both
[Amazon Elastic Container Service](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") (ECS) and
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/") (EKS). AWS Fargate makes it
straightforward to focus on building your applications by
alleviating the need to provision and manage servers, lets you
specify and pay for resources per application, and improves
security through application isolation by design. Fargate is ideal
for backend services that handle player profiles, state management
and matchmaking.

[Amazon
GameLift](https://aws.amazon.com/gamelift/ "https://aws.amazon.com/gamelift/") is a managed service for deploying, operating, and
scaling dedicated game servers for session-based multiplayer
games. You can deploy your first game server in the cloud in just
minutes, saving up to thousands of engineering hours in upfront
software development and lowering the technical risks that often
cause developers to cut multiplayer features from their designs.

### Implementation steps

- Use AWS Lambda for event-driven workloads like processing
  game events, player authentication, in-game purchases, and
  matchmaking requests, leveraging its automatic scaling and
  serverless management.
- Deploy AWS Fargate with ECS or EKS for backend services such
  as player profiles, state management, and matchmaking,
  removing server management and improving application
  isolation.
- Use Amazon GameLift to deploy and scale dedicated game
  servers for session-based multiplayer games, reducing
  development time and operational complexity.
