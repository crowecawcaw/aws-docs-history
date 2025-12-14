# GAMECOST01-BP01 Implement attribution of cost per player, game

feature, and environment

Cost attribution for game servers is usually simpler to perform than
game backend services because a game server is usually optimized to
be able to host a specific number of concurrent players per instance
which can be amortized across the cost of running the instance. 

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For game backend services, it is recommended to de-couple the
components of your game into distinct features that can be managed
as separate logical or physical resources to make it
straightforward to analyze costs.

For example, although it may seem straightforward to implement a
single monolithic application to host game backend services, this
pattern makes it hard to derive the total cost per player and game
feature over time as you add more features because the compute,
networking, and storage costs of resources are shared across the
features. Consider adopting a serverless architecture for your
game backend services with services such as
[Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") and AWS Lambda or AWS Fargate for compute,
[Amazon SQS](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/")
and [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") for messaging, Amazon S3 for object storage, and Amazon DynamoDB for database storage. These services are just a few
examples of products that offer pricing that is usage-based and
primarily driven by request volume so that costs can be visualized
with granularity. Individual resources such as Lambda functions,
Fargate services, DynamoDB tables, and S3 buckets can be
associated with cost allocation tags so that you can attribute the
costs of these services with game feature names that make it
straightforward for you to understand the costs for each of your
services.

It is also recommended to separately manage each of your game
development environments so that you can attribute costs for the
different environments. Typically, game developers will manage
separate environments for development, test, staging and
production environments, as described in the operations pillar of
this games industry lens. Each environment usually has different
scalability, performance, and usage requirements and may be
managed by separate teams. To control costs, organize these
environments so that you can properly monitor and attribute the
costs of each environment.

For more information, refer to the following documentation:

- [Building
  a serverless multi-player game that scales](https://aws.amazon.com/blogs/compute/building-a-serverless-multiplayer-game-that-scales/ "https://aws.amazon.com/blogs/compute/building-a-serverless-multiplayer-game-that-scales/")
- [Standalone
  game session servers with a WebSockets-based backend](../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_websockets.md "../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_websockets.md")
- [Standalone
  game session servers with a serverless backend](../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_serverless.md "../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_serverless.md")

### Implementation steps

- De-couple game backend services into distinct features using
  serverless or containerized architectures like AWS Lambda,
  Amazon API Gateway, and AWS Fargate to enable granular cost
  attribution per feature.
- Apply cost allocation tags to individual resources (for
  example, Lambda functions, DynamoDB tables, and S3 buckets)
  to associate costs with specific game features for better
  cost analysis.
- Manage separate environments for development, testing,
  staging, and production, organizing and monitoring their
  costs independently to align with scalability and usage
  requirements.
