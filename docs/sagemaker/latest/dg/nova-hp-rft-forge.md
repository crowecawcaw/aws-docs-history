# Reinforcement Learning

###### Note

Detailed documentation is provided once subscribed

Nova Forge provides advanced reinforcement learning capabilities with the option to use remote reward functions in your own environment. Customers can choose to integrate their own endpoint to execute validation for immediate real-world feedback, or even use their own orchestrator to coordinate agentic multi-turn evaluations in your environment.

## Bring your own orchestrator for agentic multi-turn evaluations

For Forge users requiring multi-turn conversations or reward functions exceeding
15-minute timeouts, Nova Forge provides Bring Your Own Orchestration (BYOO)
capabilities. This allows you to coordinate agentic multi-turn evaluations in your environment (e.g., using chemistry tools to score molecular designs, or robotics simulations that reward efficient task completion and penalize collisions).

###### Topics

- [Architecture overview](#nova-hp-rft-forge-architecture "#nova-hp-rft-forge-architecture")
- [Setup and execution](#nova-hp-rft-forge-setup "#nova-hp-rft-forge-setup")

### Architecture overview

The BYOO architecture provides full control over the rollout and generation
process through customer-managed infrastructure.

**Training VPC:**

- **Rollout**: Coordinates training by
  delegating rollout generation to customer infrastructure
- **Trainer**: Performs model weight
  updates based on received rollouts

**Customer VPC (such as ECS on EC2):**

- **Proxy Lambda**: Receives rollout
  requests and coordinates with customer infrastructure
- **Rollout Response SQS**: Queue for
  returning completed rollouts to training infrastructure
- **Generate Request SQS**: Queue for model
  generation requests
- **Generate Response SQS**: Queue for
  model generation responses
- **Customer Container**: Implements custom
  orchestration logic (can use provided starter kit)
- **DynamoDB**: Stores and retrieves state
  across the orchestration process

**Workflow:**

1. Rollout delegates rollout generation to Proxy Lambda
2. Proxy Lambda pushes rollout API request to Generate Request SQS
3. Customer container processes requests, manages multi-turn
   interactions, and calls reward functions
4. Container stores and retrieves state from DynamoDB as needed
5. Container pushes rollout responses to Rollout Response SQS
6. Rollout sends completed rollouts to Trainer for weight updates

### Setup and execution

For detailed setup instructions, recipe configurations, request and response formats, and environment examples, refer to the confidential documentation provided to Nova Forge subscribers. To get the Nova Forge documents follow the below steps:

```
aws s3 cp s3://nova-forge-c7363-206080352451-us-east-1/v1/ ./ --recursive
```

Once the assets are downloaded, you can find all the documentation under the `docs` folder.
