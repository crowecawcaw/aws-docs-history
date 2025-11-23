# Required resources for Amazon ECS canary deployments

To use a canary deployment with managed traffic shifting, your service must use one of the
following features:

- ELB
- Service Connect

###### Note

Canary deployments do not support Network Load Balancers. For Network Load Balancer configurations, use blue/green deployments instead.

The following list provides a high-level overview of what you need to configure for Amazon ECS
canary deployments:

- Your service uses an Application Load Balancer, or Service Connect. Configure the appropriate
  resources.
  - Application Load Balancer - For more information, see [Application Load Balancer resources for blue/green, linear, and canary deployments](alb-resources-for-blue-green.md "alb-resources-for-blue-green.md").
  - Service Connect - For more information, see [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](service-connect-blue-green.md "service-connect-blue-green.md").

- Set the service deployment controller to `ECS`.
- Configure the deployment strategy as `canary` in your service
  definition.
- Optionally, configure additional parameters such as:
  - Bake time for the new deployment
  - The percentage of traffic to route to the new service revision during the
    canary phase.
  - The duration to wait during the canary phase before shifting the remaining
    traffic to the new service revision.
  - CloudWatch alarms for automatic rollback
  - Deployment lifecycle hooks (these are Lambda functions that run at
    specified deployment stages)

## Best practices

Follow these best practices for successful Amazon ECS lcanary deployments:

- **Ensure your application can handle both service
  revisions running simultaneously.**
- **Plan for sufficient cluster capacity to handle both
  service revisions during deployment.**
- **Test your rollback procedures before implementing them
  in production.**
- Configure appropriate health checks that accurately reflect your application's health.
- Set a bake time that allows sufficient testing of the green deployment.
- Implement CloudWatch alarms to automatically detect issues and trigger rollbacks.
- Use lifecycle hooks to perform automated testing at each deployment stage.
- Start with small canary percentages (5-10%) to minimize impact if issues
  occur.
- Set appropriate evaluation periods that allow sufficient time for meaningful
  performance data collection.
- Implement comprehensive monitoring with CloudWatch alarms for automated rollback
  triggers.
- Configure health checks that accurately reflect your application's readiness
  and functionality.
- Monitor both technical metrics (response time, error rate) and business
  metrics during evaluation.
- Ensure your application can handle traffic splitting without session or state
  issues.
- Plan rollback procedures and test them regularly to ensure they work when
  needed.
- Schedule canary deployments during business hours when teams can monitor and
  respond.
- Validate changes thoroughly in staging environments before canary
  deployment.
- Document clear procedures for manual intervention and rollback
  decisions.
