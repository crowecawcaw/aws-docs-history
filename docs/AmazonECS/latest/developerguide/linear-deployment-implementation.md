# Required resources for Amazon ECS linear deployments

To use a linear deployment with managed traffic shifting, your service must use
one of the following features:

- Application Load Balancer
- Service Connect

###### Note

Linear deployments do not support Network Load Balancer. For Network Load Balancer support, use blue/green deployments instead.

Linear deployments do not support Network Load Balancers. For Network Load Balancer configurations, use blue/green deployments instead.

The following list provides a high-level overview of what you need to configure for
Amazon ECS linear deployments:

- Your service uses an Application Load Balancer or Service Connect. Configure the appropriate
  resources.
  - Application Load Balancer - For more information, see .
  - Service Connect - For more information, see .

- Set the service deployment controller to `ECS`.
- Configure the deployment strategy as `linear` in your service
  definition.
- Optionally, configure additional parameters such as:
  - Bake time for the new deployment
  - The percentage of traffic to shift in each increment.
  - The duration in minutes to wait between each traffic shift increment.
  - CloudWatch alarms for automatic rollback
  - Deployment lifecycle hooks (these are Lambda functions that run at
    specified deployment stages such as BEFORE_INSTALL, PRODUCTION_TRAFFIC_SHIFT, or POST_PRODUCTION_TRAFFIC_SHIFT)

## Best practices

Follow these best practices for successful Amazon ECS linear deployments:

- **Ensure your application can handle both service
  revisions running simultaneously.**
- **Plan for sufficient cluster capacity to handle both
  service revisions during deployment.**
- **Test your rollback procedures before implementing them
  in production.**
- Configure appropriate health checks that accurately reflect your application's health.
- Set a bake time that allows sufficient testing of the new service
  revision.
- Implement CloudWatch alarms to automatically detect issues and trigger rollbacks.
- Choose step percentages and bake times that balance deployment speed with
  validation needs.
- Use smaller step percentages (5-10%) for critical applications to minimize
  risk exposure.
- Set longer step bake times for applications that need time to warm up or
  stabilize.
- Implement CloudWatch alarms to automatically detect issues and trigger rollbacks at
  any traffic increment.
- Monitor application metrics closely during each traffic shift to detect
  performance degradation early.
- Ensure your application can handle both service revisions running
  simultaneously.
- Test your rollback procedures at different traffic percentages before
  implementing them in production.
