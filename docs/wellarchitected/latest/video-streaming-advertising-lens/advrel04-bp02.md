# ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful

Implement gradual, phased deployments to minimize risks and
service impacts when updating systems.

## Implementation guidance

When deploying new code or resources, it is possible for
unintended results to occur. Various deployment strategies can
be used to reduce frequency and service impact.

By making changes through a blue/green deployment methodology,
you can significantly reduce the impact of any potential issues
and avoid downtime.

When a blue/green deployment isn't possible, a rolling
deployment methodology should be used to reduce the number of
resources being modified simultaneously. With a rolling
deployment, changes are made in small batches, with a
pre-determined amount of buffer time between batches. If an
issue occurs with the deployment, the unchanged resources can
continue handling traffic, avoiding downtime.

## Key AWS services

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/")

## Resources

- [Blue/Green
  Deployments on AWS](../../../whitepapers/latest/blue-green-deployments/welcome.md "../../../whitepapers/latest/blue-green-deployments/welcome.md")
- [Rolling
  deployments](../../../whitepapers/latest/overview-deployment-options/rolling-deployments.md "../../../whitepapers/latest/overview-deployment-options/rolling-deployments.md")
- [Deployment
  methods](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.md "Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.md")
