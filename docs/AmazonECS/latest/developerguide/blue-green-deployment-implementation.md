# Required resources for Amazon ECS blue/green deployments

To use a blue/green deployment with managed traffic shifting, your service must use
one of the following features:

- ELB
- Service Connect
  Services that don't use Service Discovery, Service Connect, VPC Lattice or ELB can also
  use blue/green deployments, but don't get any of the managed traffic shifting
  benefits.

The following list provides a high-level overview of what you need to configure for
Amazon ECS blue/green deployments:

- Your service uses an Application Load Balancer, Network Load Balancer, or Service Connect. Configure the appropriate
  resources.
  - Application Load Balancer - For more information, see [Application Load Balancer resources for blue/green, linear, and canary deployments](alb-resources-for-blue-green.md "alb-resources-for-blue-green.md").
  - Network Load Balancer - For more information, see [Network Load Balancer resources for Amazon ECS blue/green deployments](nlb-resources-for-blue-green.md "nlb-resources-for-blue-green.md").
  - Service Connect - For more information, see [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](service-connect-blue-green.md "service-connect-blue-green.md").

- Set the service deployment controller to `ECS`.
- Configure the deployment strategy as `blue/green` in your service definition.
- Optionally, configure additional parameters such as:
  - Bake time for the new deployment
  - CloudWatch alarms for automatic rollback
  - Deployment lifecycle hooks for testing (these are Lambda functions that run at specified deployment stages)

## Best practices

Follow these best practices for successful Amazon ECS blue/green deployments:

- Configure appropriate health checks that accurately reflect your application's health.
- Set a bake time that allows sufficient testing of the green deployment.
- Implement CloudWatch alarms to automatically detect issues and trigger rollbacks.
- Use lifecycle hooks to perform automated testing at each deployment stage.
- Ensure your application can handle both blue and green service revisions
  running simultaneously.
- Plan for sufficient cluster capacity to handle both service revisions during
  deployment.
- Test your rollback procedures before implementing them in production.
