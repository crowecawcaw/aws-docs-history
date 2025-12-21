# Working with deployment configurations in

CodeDeploy

A deployment configuration is a set of rules and success and failure conditions used by
CodeDeploy during a deployment. These rules and conditions are different, depending on whether you
deploy to an EC2/On-Premises compute platform, AWS Lambda compute platform, or
Amazon ECS compute platform.

## Deployment configurations on an

EC2/on-premises compute platform

When you deploy to an EC2/On-Premises compute platform, the deployment configuration
specifies, through the use of a 'minimum healthy hosts' value and an optional 'minimum healthy
hosts per zone' value, the number or percentage of instances that must remain available at any
time during a deployment.

You can use one of the three predefined deployment configurations provided by AWS or
create a custom deployment configuration. For more information about creating custom
deployment configurations, see [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md"). If you don't specify a deployment
configuration, CodeDeploy uses the CodeDeployDefault.OneAtATime deployment configuration.

For more information about how CodeDeploy monitors and evaluates instance health during a
deployment, see [Instance Health](instances-health.md "instances-health.md"). To view a
list of deployment configurations already registered to your AWS account, see [View Deployment Configuration Details](deployment-configurations-view-details.md "deployment-configurations-view-details.md").

### Predefined deployment configurations

for an EC2/on-premises compute platform

The following table lists the predefined deployment configurations.

###### Note

There are no predefined deployment configurations that support the [zonal configuration](deployment-configurations-create.md#zonal-config "deployment-configurations-create.md#zonal-config") feature (which is the feature that
lets you specify the number of healthy hosts per Availability Zone). If you want to use
this feature, you must [create your own
deployment configuration](deployment-configurations-create.md "deployment-configurations-create.md").

| Deployment configuration      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CodeDeployDefault.AllAtOnce   | **In-place deployments**:Attempts to<br>deploy an application revision to as many instances as possible at once. The status<br>of the overall deployment is displayed as **Succeeded**<br>if the application revision is deployed to one or more of the instances. The status<br>of the overall deployment is displayed as **Failed\*<br>• if<br>the application revision is not deployed to any of the instances. Using an example<br>of nine instances, CodeDeployDefault.AllAtOnce attempts to deploy to all nine<br>instances at once. The overall deployment succeeds if deployment to even a single<br>instance is successful. It fails only if deployments to all nine instances fail.<br>**Blue/green deployments\*\*:<br>• Deployment to replacement environment: Follows the same deployment rules<br>as CodeDeployDefault.AllAtOnce for in-place deployments.<br>• Traffic rerouting: Routes traffic to all instances in the replacement<br>environment at once. Succeeds if traffic is successfully rerouted to at least<br>one instance. Fails after rerouting to all instances fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CodeDeployDefault.HalfAtATime | **In-place deployments**:<br>Deploys to up to half of the instances at a time (with fractions rounded<br>down). The overall deployment succeeds if the application revision is deployed to<br>at least half of the instances (with fractions rounded up). Otherwise, the<br>deployment fails. In the example of nine instances, it deploys to up to four<br>instances at a time. The overall deployment succeeds if deployment to five or more<br>instances succeed. Otherwise, the deployment fails.<br>NoteIf you're deploying to instances in multiple Auto Scaling groups, CodeDeploy will deploy<br>to up to half of the instances at a time _regardless of the Auto Scaling group<br>they're in_. For example, let's assume you have two Auto Scaling groups,<br>`ASG1` and `ASG2`, each with 10 instances. In this<br>scenario, CodeDeploy might deploy to 10 instances in just `ASG1` and<br>consider this a success because it has deployed to at least half of the<br>instances.<br>**Blue/green deployments**:<br>• Deployment to replacement environment: Follows the same deployment rules<br>as CodeDeployDefault.HalfAtATime for in-place deployments.<br>• Traffic rerouting: Routes traffic to up to half the instances in the<br>replacement environment at a time. Succeeds if rerouting to at least half of<br>the instances succeeds. Otherwise, fails.                                                                                                                                                                                                                                                         |
| CodeDeployDefault.OneAtATime  | **In-place deployments**:<br>Deploys the application revision to only one instance at a time.<br>For deployment groups that contain more than one instance:<br>• The overall deployment succeeds if the application revision is deployed to<br>all of the instances. The exception to this rule is that if deployment to the<br>last instance fails, the overall deployment still succeeds. This is because<br>CodeDeploy allows only one instance at a time to be taken offline with the<br>CodeDeployDefault.OneAtATime configuration.<br>• The overall deployment fails as soon as the application revision fails to<br>be deployed to any but the last instance.<br>• In an example using nine instances, it deploys to one instance at a time.<br>The overall deployment succeeds if deployment to the first eight instances is<br>successful. The overall deployment fails if deployment to any of the first<br>eight instances fails.<br>For deployment groups that contain only one instance, the overall deployment<br>is successful only if deployment to the single instance is successful.<br>**Blue/green deployments**:<br>• Deployment to replacement environment: Follows same deployment rules as<br>CodeDeployDefault.OneAtATime for in-place deployments.<br>• Traffic rerouting: Routes traffic to one instance in the replacement<br>environment at a time. Succeeds if traffic is successfully rerouted to all<br>replacement instances. Fails after the very first rerouting failure. The<br>exception to this rule is that if the last instance fails to register, the<br>overall deployment still succeeds. |

## Deployment configurations on an Amazon ECS compute

platform

When you deploy to an Amazon ECS compute platform, the deployment configuration specifies
how traffic is shifted to the updated Amazon ECS task set. You can shift traffic using a **canary**, **linear**, or **all-at-once** deployment configuration. For more information, see [Deployment configuration](primary-components.md#primary-components-deployment-configuration "primary-components.md#primary-components-deployment-configuration").

You can also create your own custom canary or linear deployment configuration. For more
information, see [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md").

### Predefined deployment

configurations for an Amazon ECS compute platform

The following table lists the predefined configurations available for Amazon ECS
deployments.

###### Note

If you're using a Network Load Balancer, only the `CodeDeployDefault.ECSAllAtOnce` predefined
deployment configuration is supported.

| Deployment configuration                          | Description                                                                                                      |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| CodeDeployDefault.ECSLinear10PercentEvery1Minutes | Shifts 10 percent of traffic every minute until all traffic is shifted.                                          |
| CodeDeployDefault.ECSLinear10PercentEvery3Minutes | Shifts 10 percent of traffic every three minutes until all traffic is<br>shifted.                                |
| CodeDeployDefault.ECSCanary10Percent5Minutes      | Shifts 10 percent of traffic in the first increment. The remaining 90 percent<br>is deployed five minutes later. |
| CodeDeployDefault.ECSCanary10Percent15Minutes     | Shifts 10 percent of traffic in the first increment. The remaining 90 percent<br>is deployed 15 minutes later.   |
| CodeDeployDefault.ECSAllAtOnce                    | Shifts all traffic to the updated Amazon ECS container at once.                                                  |

## Deployment configurations for CloudFormation

blue/green deployments (Amazon ECS)

When you deploy to an Amazon ECS compute platform through CloudFormation blue/green deployments,
the deployment configuration specifies how traffic is shifted to the updated Amazon ECS container.
You can shift traffic using a **canary**, **linear**, or **all-at-once** deployment
configuration. For more information, see [Deployment configuration](primary-components.md#primary-components-deployment-configuration "primary-components.md#primary-components-deployment-configuration").

With CloudFormation blue/green deployments, you cannot create your own custom canary or linear
deployment configuration. For step-by-step instructions on using CloudFormation to manage your Amazon ECS
blue/green deployments, see [Automate ECS blue/green deployments
through CodeDeploy using CloudFormation](../../../AWSCloudFormation/latest/UserGuide/blue-green.md "../../../AWSCloudFormation/latest/UserGuide/blue-green.md") in the _CloudFormation User Guide_.

###### Note

Managing Amazon ECS blue/green deployments with CloudFormation is not
available in the Europe (Milan), Africa (Cape Town), and Asia Pacific (Osaka)
regions.

## Deployment configurations on an AWS Lambda

compute platform

When you deploy to an AWS Lambda compute platform, the deployment configuration
specifies the way traffic is shifted to the new Lambda function versions in your application.
You can shift traffic using a **canary**, **linear**, or **all-at-once** deployment
configuration. For more information, see [Deployment configuration](primary-components.md#primary-components-deployment-configuration "primary-components.md#primary-components-deployment-configuration").

You can also create your own custom canary or linear deployment configuration. For more
information, see [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md").

### Predefined deployment

configurations for an AWS Lambda compute platform

The following table lists the predefined configurations available for AWS Lambda
deployments.

| Deployment configuration                              | Description                                                                                                      |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| CodeDeployDefault.LambdaCanary10Percent5Minutes       | Shifts 10 percent of traffic in the first increment. The remaining 90 percent<br>is deployed five minutes later. |
| CodeDeployDefault.LambdaCanary10Percent10Minutes      | Shifts 10 percent of traffic in the first increment. The remaining 90 percent<br>is deployed 10 minutes later.   |
| CodeDeployDefault.LambdaCanary10Percent15Minutes      | Shifts 10 percent of traffic in the first increment. The remaining 90 percent<br>is deployed 15 minutes later.   |
| CodeDeployDefault.LambdaCanary10Percent30Minutes      | Shifts 10 percent of traffic in the first increment. The remaining 90 percent<br>is deployed 30 minutes later.   |
| CodeDeployDefault.LambdaLinear10PercentEvery1Minute   | Shifts 10 percent of traffic every minute until all traffic is shifted.                                          |
| CodeDeployDefault.LambdaLinear10PercentEvery2Minutes  | Shifts 10 percent of traffic every two minutes until all traffic is<br>shifted.                                  |
| CodeDeployDefault.LambdaLinear10PercentEvery3Minutes  | Shifts 10 percent of traffic every three minutes until all traffic is<br>shifted.                                |
| CodeDeployDefault.LambdaLinear10PercentEvery10Minutes | Shifts 10 percent of traffic every 10 minutes until all traffic is<br>shifted.                                   |
| CodeDeployDefault.LambdaAllAtOnce                     | Shifts all traffic to the updated Lambda functions at once.                                                      |

**Topics**

- [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md")
- [View Deployment Configuration Details](deployment-configurations-view-details.md "deployment-configurations-view-details.md")
- [Delete a Deployment Configuration](deployment-configurations-delete.md "deployment-configurations-delete.md")
