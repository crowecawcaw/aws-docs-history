# Migrating from a CodeDeploy blue/green to an Amazon ECS rolling update service deployment

You can migrate your service deployments from an CodeDeploy blue/green deployment to an Amazon ECS rolling update deployment. This moves you away from CodeDeploy dependency to using an integrated deployment.

The Amazon ECS service scheduler replaces the currently running tasks with new tasks.
The number of tasks that Amazon ECS adds or removes from the service during a rolling update
is controlled by the service deployment configuration.

## Prerequisites

Perform the following operations before you start a blue/green deployment.

1. You no longer need the Amazon ECS CodeDeploy IAM role.
2. Turn off CodeDeploy automation. For more information, see [Working with
   deployment groups in CodeDeploy](../../../codedeploy/latest/userguide/deployment-groups.md "../../../codedeploy/latest/userguide/deployment-groups.md") in the _CodeDeploy User
   Guide_.
3. Verify that there are no ongoing service deployments for the service. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md "service-deployment.md").

For more information about updating a service's deployment controller, see [Update Amazon ECS service parameters](update-service-parameters.md "update-service-parameters.md").

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.

The cluster details page displays. 3. From the **Services** tab, choose the service.

The service details page displays. 4. In the banner, choose **Migrate**.

The **Update deployment configuration** page displays. 5. Expand **Deployment options**, and then specify the
following parameters.

    1. For **Deployment controller type**, choose
     **ECS**.
    2. For **Deployment strategy**, choose **Rolling
     update**.
    3. For **Min running tasks**,
     enter the lower limit on the number of tasks in
     the service that must remain in the
     `RUNNING` state during a deployment, as
     a percentage of the desired number of tasks
     (rounded up to the nearest integer). For more
     information, see [Deployment configuration](service_definition_parameters.md#sd-deploymentconfiguration "service_definition_parameters.md#sd-deploymentconfiguration").
    4. For **Max running tasks**,
     enter the upper limit on the number of tasks in
     the service that are allowed in the
     `RUNNING` or `PENDING` state
     during a deployment, as a percentage of the
     desired number of tasks (rounded down to the
     nearest integer).

6. Expand **Load Balancing**, and then configure the
   following:
   1. For **Role**, choose the role that you created in the
      prerequisites with the blue/green permissions.

   For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md "blue-green-permissions.md"). 2. For **Listener**, choose the production listener from
   your CodeDeploy blue/green deployment. 3. For **Target group**, choose the production target
   group from your CodeDeploy blue/green deployment.

7. Choose **Update**.

## Next steps

You must update the service for the change to take effect. For more information, see
[Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
