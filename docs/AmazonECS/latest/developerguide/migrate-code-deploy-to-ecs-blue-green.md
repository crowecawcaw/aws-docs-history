# Migrating from a CodeDeploy blue/green to

an Amazon ECS blue/green service deployment

By using Amazon ECS blue/green deployments, you can make and test service changes before
implementing them in a production environment.

You must create new lifecycle hooks for your Amazon ECS blue/green deployment.

## Prerequisites

Perform the following operations before you start a blue/green deployment.

1.  Replace the Amazon ECS CodeDeploy IAM role with the following permissions.
    - For information about ELB permissions, see [Amazon ECS infrastructure
      IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md "AmazonECSInfrastructureRolePolicyForLoadBalancers.md").
    - For information about Lambda permissions, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md "blue-green-permissions.md").

2.  Turn off CodeDeploy automation. For more information, see [Working with
    deployment groups in CodeDeploy](../../../codedeploy/latest/userguide/deployment-groups.md "../../../codedeploy/latest/userguide/deployment-groups.md") in the _CodeDeploy User
    Guide_.
3.  Make sure that you have the following information from your CodeDeploy blue/green
    deployment. You can reuse this information for the Amazon ECS blue/green deployment:
    - The production target group
    - The production listener
    - The production rule
    - The test target group

    This is the target group for the green service revision,

4.  Ensure that your Application Load Balancer target groups are properly associated with listener rules:

        * If you are not using test listeners, both target groups (production and test) must be associated with production listener rules.
        * If you are using test listeners, one target group must be linked to production listener rules and the other target group must be linked to test listener rules.

    If this requirement is not met, the service deployment will fail with the following error: `Service deployment rolled back because of invalid networking configuration. Both targetGroup and alternateTargetGroup must be associated with the productionListenerRule or testListenerRule.`

5.  Verify that there are no ongoing service deployments for the service. For more
    information, see [View service history using Amazon ECS service
    deployments](service-deployment.md "service-deployment.md").
6.  Amazon ECS blue/green deployments require your service to use one of the
    following features: Configure the appropriate resources.
    - Application Load Balancer - For more information, see [Application Load Balancer resources for blue/green, linear, and canary deployments](alb-resources-for-blue-green.md "alb-resources-for-blue-green.md").
    - Network Load Balancer - For more information, see [Network Load Balancer resources for Amazon ECS blue/green deployments](nlb-resources-for-blue-green.md "nlb-resources-for-blue-green.md").
    - Service Connect - For more information, see [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](service-connect-blue-green.md "service-connect-blue-green.md").

7.  Decide if you want to run Lambda functions for the lifecycle stages for the
    stages in the Amazon ECS blue/green deployment.

        * Pre scale up
        * After scale up
        * Test traffic shift
        * After test traffic shift
        * Production traffic shift
        * After production traffic shift

    Create Lambda functions for each lifecycle stage. For more information, see
    [Create a Lambda function with the console](../../../lambda/latest/dg/getting-started.md#getting-started-create-function "../../../lambda/latest/dg/getting-started.md#getting-started-create-function") in the _AWS Lambda Developer Guide_.

For more information about updating a service's deployment controller, see [Update Amazon ECS service parameters](update-service-parameters.md "update-service-parameters.md").

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.

The cluster details page displays. 3. From the **Services** tab, choose the service.

The service details page displays. 4. In the banner, choose **Update deployment controller
type**.

The **Migrate deployment controller type** page
displays. 5. Expand **New**, and then specify the following
parameters.

    1. For **Deployment controller type**, choose
     **ECS**.
    2. For **Deployment strategy**, choose
     **Blue/green**.
    3. For **Bake time**, enter the time that both the blue
     and green service revisions run.
    4. To run Lambda functions for a lifecycle stage, under
     **Deployment lifecyce hooks** do the following for
     each unique Lambda function:


    	1. Choose **Add**.


    	Repeat for every unique function you want to run.
    	2. For **Lambda function**, enter the function
    	 name.
    	3. For **Role**, choose the role that you
    	 created in the prerequisites with the blue/green
    	 permissions.


    	For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md "blue-green-permissions.md").
    	4. For **Lifecycle stages**, select the stages
    	 the Lambda function runs.
    	5. (Optional) For **Hook details**, enter a key-value pair that provides information about the hook.

6. Expand **Load Balancing**, and the configure the
   following:
   1. For **Role**, choose the role that you created in the
      prerequisites with the blue/green permissions.

   For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md "blue-green-permissions.md"). 2. For **Listener**, choose the production listener from
   your CodeDeploy blue/green deployment. 3. For **Production rule**, choose the production rule
   from your CodeDeploy blue/green deployment. 4. For **Test rule**, choose the test rule from your
   CodeDeploy blue/green deployment. 5. For **Target group**, choose the production target
   group from your CodeDeploy blue/green deployment. 6. For **Alternate target group**, choose the test
   target group from your CodeDeploy blue/green deployment.

7. Choose **Update**.

## Next steps

- Update the service to start the deployment. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
- Monitor the deployment process to ensure it follows the blue/green
  pattern:
  - The green service revision is created and scaled up
  - Test traffic is routed to the green revision (if configured)
  - Production traffic is shifted to the green revision
  - After the bake time, the blue revision is terminated
