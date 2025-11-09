# Deployment approaches

A best practice for deployments in a microservice architecture is
to ensure that a change does not break the service contract of the
consumer. If the API owner makes a change that breaks the service
contract and the consumer is not prepared for it, failures can
occur.

Being aware of which consumers are using your APIs is the first
step to ensure that deployments are safe. Collecting metadata on
consumers and their usage allows you to make data driven decisions
about the impact of changes. API Keys are an effective way to
capture metadata about the API consumer/clients and often used as
a form of contact if a breaking change is made to an API.

Some customers who want to take a risk-averse approach to breaking changes may choose to
clone the API and route customers to a different subdomain (for example, v2.my-service.com) to
ensure that existing consumers aren’t impacted. While this approach enables new deployments
with a new service contract, the tradeoff is that the overhead of maintaining dual APIs (and
subsequent backend infrastructure) requires additional overhead.

The table shows the different approaches to deployment:

| Deployment                                                         | Consumer Impact                                                          | Rollback                                    | Event Model Factors                                                    | Deployment Speed                                                |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| [All-at-once](#all-at-once-deployments "#all-at-once-deployments") | All at once                                                              | Redeploy older version                      | Any event model at low concurrency rate                                | Immediate                                                       |
| [Blue/Green](#bluegreen-deployments "#bluegreen-deployments")      | All at once with some level of production environment testing beforehand | Revert traﬃc to previous environment        | Better for async and sync event models at medium concurrency workloads | Minutes to hours of validation, and then immediate to customers |
| [Canary](#canary-deployments "#canary-deployments") (or Linear)    | 1–10% typical initial traﬃc shift, then phased increases, or all at once | Revert 100% of traﬃc to previous deployment | Better for high concurrency workloads                                  | Minutes to hours                                                |

## All-at-once deployments

All-at-once deployments involve making
changes on top of the existing configuration. An advantage to this style of deployment is
that backend changes to data stores, such as a relational database, require a much smaller
level of effort to reconcile transactions during the change cycle. While this type of
deployment style is low-effort and can be made with little impact in low-concurrency models,
it adds risk when it comes to rollback and usually causes downtime. Use this deployment
model for non-critical environments, such as development, where impact to customers is not a
risk.

## Blue/green deployments

Another traffic shifting pattern is enabling blue/green
deployments. This near zero-downtime release enables traffic to
shift to the new live environment (green) while still keeping
the old production environment (blue) warm in case a rollback is
necessary. Since [API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") allows you to define what
percentage of traffic is shifted to a particular environment;
this style of deployment can be an effective technique. Since
blue/green deployments are designed to reduce downtime, many
customers adopt this pattern for production changes.

Serverless architectures that follow the best practice of
statelessness and idempotency are amenable to this deployment
style because there is no affinity to the underlying
infrastructure. You should bias these deployments toward smaller
incremental changes so that you can easily roll back to a
working environment if necessary.

You need the right indicators in place to know if a rollback is
required. As a best practice, we recommend customers using
[CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") high-resolution metrics, which can monitor in
1-second intervals, and quickly capture downward trends. Used
with [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") alarms, you can enable an expedited rollback to
occur. [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") metrics can be captured on [API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/"), [Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/"), [Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") (including custom metrics), and [DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/").

## Canary deployments

Canary deployments are a way for you to gradually
release new software in a coordinated and safe way that enable rapid deployment cycles.
Canary deployments involve deploying a
percentage of requests to new code, and monitoring for errors, degradations, or regressions.

You can use [Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") function aliases with
[AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/") to support various canary deployment strategies. [AWS SAM](https://aws.amazon.com/serverless/sam/ "https://aws.amazon.com/serverless/sam/") comes with built-in
support for [CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/"), which makes Canary
deployments even simpler. Operators can further control gradual deployments by leveraging
pre-traffic and post-traffic deployment hooks and [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") alarms to trigger automated rollback.
