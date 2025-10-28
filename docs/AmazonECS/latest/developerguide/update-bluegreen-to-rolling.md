# Updating the deployment strategy from Amazon ECS blue/green to rolling update

You can migrate a blue/green deployment to a rolling update deployment.

Keep the following considerations in mind when migrating to rolling deployments:

- **Traffic handling**: With rolling deployments, new
  tasks start receiving traffic as soon as they pass health checks. There is no
  separate testing phase as with blue/green deployments.
- **Resource efficiency**: Rolling deployments
  typically use fewer resources than blue/green deployments because they replace tasks
  incrementally rather than creating a complete duplicate environment.
- **Rollback complexity**: Rolling deployments make
  rollbacks more complex compared to blue/green deployments. If you need to roll back,
  you must initiate a new deployment with the previous task definition.
- **Deployment speed**: Rolling deployments may take
  longer to complete than blue/green deployments, especially for services with many
  tasks.
- **Load balancer configuration**: Your existing load
  balancer configuration will continue to work with rolling deployments, but the
  traffic shifting behavior will be different.

## Prerequisites

Before migrating your service from blue/green to rolling deployments, ensure you have the following:

- An existing Amazon ECS service using the blue/green deployment strategy
- No ongoing deployments for the service (wait for any current deployments to complete)
- A clear understanding of how your service will behave with rolling deployments

###### Note

You cannot migrate a service to rolling deployment if it has an ongoing deployment. Wait for any current deployments to complete before proceeding.

## Migration procedure

Follow these steps to migrate your Amazon ECS service from blue/green to rolling deployments:

1. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the cluster that contains the service you want to migrate.
4. On the **Cluster details** page, choose the **Services** tab.
5. Select the service you want to migrate, and then choose **Update**.
6. On the **Update service** page, navigate to the **Deployment options** section and expand it if necessary.
7. For **Deployment strategy**, choose **Rolling update**.
8. Configure the rolling deployment settings:
   1. For **Minimum healthy percent**, enter the minimum percentage of tasks that must remain in the `RUNNING` state during a deployment. This value is specified as a percentage of the desired number of tasks for the service.
   2. For **Maximum percent**, enter the maximum percentage of tasks that are allowed in the `RUNNING` or `PENDING` state during a deployment. This value is specified as a percentage of the desired number of tasks for the service.

9. Optional: Under **Deployment failure detection**, configure how Amazon ECS detects and handles deployment failures:
   1. To enable the deployment circuit breaker, choose **Use the deployment circuit breaker**.
   2. To automatically roll back failed deployments, choose **Rollback on failure**.

10. Review your configuration changes, and then choose **Update** to save your changes and migrate the service to rolling deployment.

Amazon ECS will update your service configuration to use the rolling deployment strategy. The next time you update your service, it will use the rolling deployment process.

###### Note

When you migrate from blue/green to rolling deployment, Amazon ECS handles the transition by:

1. Identifying the current active service revision that is serving traffic.
2. Maintaining the existing load balancer configuration but changing how new deployments are handled.
3. Preparing the service for future rolling deployments.

## Next steps

- Update the service to start the deployment. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
