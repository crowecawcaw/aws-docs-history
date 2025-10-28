# Update the Amazon ECS deployment strategy

Amazon ECS supports multiple deployment strategies for updating your services. You can migrate between these strategies based on your application requirements. This topic explains how to migrate between rolling deployments and blue/green deployments.

## Understanding Amazon ECS deployment strategies

Before migrating between deployment strategies, it's important to understand how each strategy works and their key differences:

**Rolling deployments**

In a rolling deployment, Amazon ECS replaces the current running version of your application with a new version. The service scheduler uses the minimum and maximum healthy percentage parameters to determine the deployment strategy.

Rolling deployments are simpler to set up but provide less control over the deployment process and traffic routing.

**Blue/green deployments**

In a blue/green deployment, Amazon ECS creates a new version of your service (green) alongside the existing version (blue). This allows you to verify the new version before routing production traffic to it.

Blue/green deployments provide more control over the deployment process, including traffic shifting, testing, and rollback capabilities.

## Best practices

Follow these best practices when migrating between deployment strategies:

- **Test in a non-production environment**: Always
  test the update in a non-production environment before applying changes to
  production services.
- **Plan for rollback**: Have a rollback plan in
  case the update doesn't work as expected.
- **Monitor during transition**: Closely monitor your service during and after the migration to ensure it continues to operate correctly.
- **Update documentation**: Update your deployment documentation to reflect the new deployment strategy.
- **Consider traffic impact**: Understand how the
  update might impact traffic to your service and plan accordingly.
