

# Updating the deployment strategy from rolling update to Amazon ECS blue/green
<a name="update-rolling-to-bluegreen"></a>

You can migrate from a rolling update deployment to an Amazon ECS blue/green deployment when you want to make and test service changes before implementing them in a production environment. 

## Prerequisites
<a name="update-rolling-to-bluegreen-prerequisites"></a>

Before migrating your service from rolling to blue/green deployments, ensure you have the following:
+  Wait for any current deployments to complete. 
+ An existing Amazon ECS service using the rolling deployment strategy.
+ If you have multiple service revisions serving traffic, Amazon ECS attempts to consolidate traffic to a single revision during migration. If this fails, you might need to manually update your service to use a single revision before migrating.
+ Configure the appropriate permissions.
  + For information about Elastic Load Balancing permissions, see [Amazon ECS infrastructure IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md).
  + For information about Lambda permissions, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md).
+ Depending on configuration, you need to perform one of the following:
  + If your service uses Elastic Load Balancing, update your service with the new `advancedConfiguration` and start a rolling deployment. 
  + If your service uses Service Connect, update your service and start a rolling deployment. 
  + If your service uses both Elastic Load Balancing and Service Connect, perform both preceding steps (you can use a single UpdateService request). 
  + If your service uses none of these, then no additional operation is needed.
+ Amazon ECS blue/green deployments require that your service uses one of the following features. Configure the appropriate resources.
  + Application Load Balancer - For more information, see [Application Load Balancer resources for blue/green, linear, and canary deployments](alb-resources-for-blue-green.md).
  + Network Load Balancer - For more information, see [Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments](nlb-resources-for-blue-green.md).
  + Service Connect - For more information, see [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](service-connect-blue-green.md).

## Procedure
<a name="update-rolling-to-bluegreen-procedure"></a>

1. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose the cluster that contains the service you want to migrate.

   The Cluster details page is displayed.

1. On the **Cluster details** page, choose the **Services** tab.

1. Choose the service, and then choose **Update**.

   The Update service page is displayed

1. Expand **Deployment options**, and then do the following:

1. For **Deployment strategy**, choose **Blue/green**.

1. Configure the blue/green deployment settings:

   1. For **Bake time**, enter the number of minutes that both the blue and green service revisions will run simultaneously before the blue revision is terminated. 

      This allows time for verification and testing.

   1. (Optional) Configure Lambda functions to run at specific stages of the deployment. Under **Deployment lifecycle hooks**, configure Lambda functions for the following stages:
      + **Pre scale up**: Runs before scaling up the green service revision
      + **Post scale up**: Runs after scaling up the green service revision
      + **Test traffic shift**: Runs during test traffic routing to the green service revision
      + **Post test traffic shift**: Runs after test traffic is routed to the green service revision
      + **Production traffic shift**: Runs during production traffic routing to the green service revision
      + **Post production traffic shift**: Runs after production traffic is routed to the green service revision

      To add a lifecycle hook:

      1. Choose **Add**.

      1. For **Lambda function**, enter the function name or ARN.

      1. For **Role**, choose the IAM role that has permission to invoke the Lambda function.

      1. For **Lifecycle stages**, select the stages when the Lambda function should run.

      1. Optional: For **Hook details**, enter key-value pairs to provide additional information to the hook.

1. Configure the load balancer settings:

   1. Under **Load balancing**, verify that your service is configured to use a load balancer.

   1. For **Target group**, choose the primary target group for your production (blue) environment.

   1. For **Alternate target group**, choose the target group for your test (green) environment.

   1. For **Production listener rule**, choose the listener rule for routing production traffic.

   1. Optional: For **Test listener rule**, choose a listener rule for routing test traffic to your green environment.

   1. For **Role**, choose the IAM role that allows Amazon ECS to manage your load balancer.

1. Review your configuration changes, and then choose **Update**.

## Next steps
<a name="update-rolling-to-bluegreen-next-steps"></a>
+ Update the service to start the deployment. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md).
+ Monitor the deployment process to ensure it follows the blue/green pattern:
  + The green service revision is created and scaled up
  + Test traffic is routed to the green revision (if configured)
  + Production traffic is shifted to the green revision
  + After the bake time, the blue revision is terminated