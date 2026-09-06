

# Create an Amazon ECS blue/green deployment through CloudFormation
<a name="deployments-create-ecs-cfn"></a>

You can use AWS CloudFormation to manage Amazon ECS blue/green deployments through CodeDeploy. You generate your deployment by defining your green and blue resources and specifying the traffic routing and stabilization settings to use in CloudFormation. This topic covers the differences between Amazon ECS blue/green deployments that are managed by CodeDeploy and deployments that are managed by CloudFormation.

For step-by-step instructions on using CloudFormation to manage your Amazon ECS blue/green deployments, see [Automate ECS blue/green deployments through CodeDeploy using AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html) in the *AWS CloudFormation User Guide*.

**Note**  
Managing Amazon ECS blue/green deployments with CloudFormation is not available in the Asia Pacific (Osaka) Region.

## Differences between Amazon ECS blue/green deployments through CodeDeploy and CloudFormation
<a name="differences-ecs-bg-cfn"></a>

The CloudFormation stack template models Amazon ECS task-related resources and infrastructure, and also the configuration options for deployments. So there are differences between the standard Amazon ECS blue/green deployments and blue/green deployments that are created through CloudFormation.

Unlike standard Amazon ECS blue/green deployments, you don't model or manually create the following:
+ You don't create an AWS CodeDeploy application by specifying a name that uniquely represents what you want to deploy.
+ You don't create an AWS CodeDeploy deployment group.
+ You don't specify an *application specification file* (AppSpec file). The information normally managed with the AppSpec file, such as the weighted configuration options or lifecycle events, is managed by the `AWS::CodeDeploy::BlueGreen` hook.

 This table summarizes the differences in the high-level workflow between deployment types.



| Function | Standard blue/green deployments | Blue/green deployments through CloudFormation | 
| --- | --- | --- | 
| Specify the Amazon ECS cluster, Amazon ECS service, Application Load Balancer or Network Load Balancer, Production listener, test listener, and two target groups. | Create a CodeDeploy deployment group that specifies these resources. | Create a CloudFormation template to model these resources. | 
| Specify the change to be deployed. | Create a CodeDeploy application. | Create a CloudFormation template that specifies the container image. | 
| Specify the Amazon ECS task definition, container name, and container port. | Create an AppSpec file that specifies these resources. | Create a CloudFormation template to model these resources. | 
| Specify the deployment traffic shifting options and lifecycle event hooks. | Create an AppSpec file that specifies these options. | Create a CloudFormation template that uses the AWS::CodeDeploy::BlueGreen hook parameters to specify these options. | 
| CloudWatch alarms. | Create a CloudWatch alarm that triggers a rollback. | Configure a CloudWatch alarm at the CloudFormation stack level that triggers a rollback. | 
| Rollback/redeployment. | Specify rollback and redeployment options. | Cancel the stack update in CloudFormation. | 

## Monitoring Amazon ECS blue/green deployments through CloudFormation
<a name="monitoring-ecs-bg-cfn"></a>

You can monitor blue/green deployments through CloudFormation and CodeDeploy. For information about monitoring through CloudFormation, see [Monitoring blue/green events in CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html#blue-green-events) in the *AWS CloudFormation User Guide*.

**To view deployment status of blue/green deployments in CodeDeploy**

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy).
**Note**  
Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md).

1. In **Deployments**, the deployment that was triggered by the CloudFormation stack update appears. Choose the deployment to view the **Deployment history**.  
![Console screenshot showing the Deployments section and deployment history.](http://docs.aws.amazon.com/codedeploy/latest/userguide/images/cfn-cd-bg-deplhist.png)

1. Choose the deployment to view the traffic shifting status. Note that the application and deployment group are not created.  
![Console screenshot showing the deployment details with deployment status completed.](http://docs.aws.amazon.com/codedeploy/latest/userguide/images/cfn-cd-bg-deplstatus.png)

1. The following apply for rolling back or stopping the deployment:
   + The successful deployment appears in CodeDeploy and shows that the deployment was initiated by CloudFormation.
   + If you want to stop and roll back the deployment, you must cancel the stack update in CloudFormation.