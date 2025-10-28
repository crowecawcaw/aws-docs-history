# Tutorial: Deploy an Amazon ECS service with a

validation test

In this tutorial, you learn how to use a Lambda function to validate part of the deployment
of an updated Amazon ECS application. This tutorial uses the CodeDeploy application, CodeDeploy deployment
group, and the Amazon ECS application you used in [Tutorial: Deploy an application into Amazon ECS](tutorial-ecs-deployment.md "tutorial-ecs-deployment.md"). Complete that tutorial before starting this
one.

To add validation test, you first implement the test in a Lambda function. Next, in your
deployment AppSpec file, you specify the Lambda function for the lifecycle hook you want to
test. If a validation test fails, the deployment stops, is rolled back, and marked failed. If
the test succeeds, the deployment continues to the next deployment lifecycle event or hook.

During an Amazon ECS deployment with validation tests, CodeDeploy uses a load balancer that is
configured with two target groups: one production traffic listener and one test traffic
listener. The following diagram shows how the load balancer, production and test listeners,
target groups, and your Amazon ECS application are related before the deployment starts. This
tutorial uses an Application Load Balancer. You can also use a Network Load Balancer.

![The connections between the Application Load Balancer or Network Load Balancer, listeners, target groups, task set, and Amazon ECS service.](images/codedeploy-ecs-deployment-step-1.png)
During an Amazon ECS deployment, there are five lifecycle hooks for testing. This tutorial
implements one test during the third lifecycle deployment hook,
`AfterAllowTestTraffic`. For more information, see [List of lifecycle
event hooks for an Amazon ECS deployment](reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-list-ecs "reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-list-ecs"). After a successful
deployment, the production traffic listener serves traffic to your new replacment task set and
the original task set is terminated. The following diagram shows how your resources are related
after a successful deployment. For more information, see [What happens during an Amazon ECS
deployment](deployment-steps-ecs.md#deployment-steps-what-happens "deployment-steps-ecs.md#deployment-steps-what-happens").

![The connections between the Application Load Balancer or Network Load Balancer, listeners, target groups, and replacement task set after a deployment.](images/codedeploy-ecs-deployment-step-6.png)

###### Note

Completing this tutorial might result in charges to your AWS account. These include
possible charges for CodeDeploy, AWS Lambda, and CloudWatch. For more information, see [AWS CodeDeploy pricing](https://aws.amazon.com/codedeploy/pricing/ "https://aws.amazon.com/codedeploy/pricing/"), [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/"), and [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Prerequisites](tutorial-ecs-with-hooks-prereqs.md "tutorial-ecs-with-hooks-prereqs.md")
- [Step 1: Create a test
  listener](tutorial-ecs-with-hooks-create-second-listener.md "tutorial-ecs-with-hooks-create-second-listener.md")
- [Step 2: Update your
  Amazon ECS application](tutorial-ecs-with-hooks-update-the-ecs-application.md "tutorial-ecs-with-hooks-update-the-ecs-application.md")
- [Step 3: Create a lifecycle hook Lambda
  function](tutorial-ecs-with-hooks-create-hooks.md "tutorial-ecs-with-hooks-create-hooks.md")
- [Step 4: Update your AppSpec
  file](tutorial-ecs-with-hooks-create-appspec-file.md "tutorial-ecs-with-hooks-create-appspec-file.md")
- [Step 5: Use the CodeDeploy console to deploy
  your Amazon ECS service](tutorial-ecs-with-hooks-deployment.md "tutorial-ecs-with-hooks-deployment.md")
- [Step 6: View your Lambda hook function
  output in CloudWatch Logs](tutorial-ecs-with-hooks-view-cw-logs.md "tutorial-ecs-with-hooks-view-cw-logs.md")
- [Step 7: Clean up](tutoria-ecs-with-hooks-clean-up.md "tutoria-ecs-with-hooks-clean-up.md")
