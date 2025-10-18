# About blue/green deployments

This topic provides an overview of how performing blue/green deployments with CloudFormation
 works. It also explains how to prepare your CloudFormation template for blue/green
 deployments.

###### Topics

* [How it works](#blue-green-how-it-works "#blue-green-how-it-works")
* [Resource updates that initiate green deployments](#blue-green-resources "#blue-green-resources")
* [Preparing your template](#blue-green-setup "#blue-green-setup")
* [Modeling your blue/green deployment](#blue-green-required "#blue-green-required")
* [Change sets](#blue-green-changesets "#blue-green-changesets")
* [Monitoring stack events](#blue-green-events "#blue-green-events")
* [IAM permissions](#blue-green-iam "#blue-green-iam")

## How it works


When using CloudFormation to perform ECS blue/green deployments through CodeDeploy, you start by
 creating a stack template that defines the resources for both your blue and green
 application environments, including specifying the traffic routing and stabilization
 settings to use. Next, you create a stack from that template. This generates your blue
 (current) application. CloudFormation only creates the blue resources during stack creation.
 Resources for a green deployment aren't created until they're required.


Then, if in a future stack update you update the task definition or task set resources
 in your blue application, CloudFormation does the following:



* Generates all the necessary green application environment resources
* Shifts the traffic based on the specified traffic routing parameters
* Deletes the blue resources

If an error occurs at any point before the green deployment is successful and finalized,
 CloudFormation rolls the stack back to its state before the entire green deployment was
 initiated.


## Resource updates that initiate green
 deployments


When you perform a stack update that updates certain properties of specific ECS
 resources, CloudFormation initiates a green deployment process. The resources that initiate this
 process are:



* [AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")
* [AWS::ECS::TaskSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskset.html")

However, if the updates to these resources don't involve property changes that require
 replacement, a green deployment won't be initiated. For more information, see [Understand update behaviors of stack
 resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md").


It's important to note that you can't combine updates to the above resources with
 updates to other resources in the same stack update operation. If you need to update both
 the listed resources and other resources within the same stack, you have two options:



* Perform two separate stack update operations: one that includes only the updates to
 the above resources, and a separate stack update that includes changes to any other
 resources.
* Remove the `Transform` and `Hooks` sections from your template
 and then perform the stack update. In this case, CloudFormation won't perform a green
 deployment.

## Preparing your template to perform ECS blue/green
 deployments


To enable blue/green deployments on your stack, include the following sections in your
 stack template before performing a stack update.



* Add a reference to the `AWS::CodeDeployBlueGreen` transform to your
 template:



```
"Transform": [
  "AWS::CodeDeployBlueGreen"
],
```
* Add a `Hooks` section that invokes the
 `AWS::CodeDeploy::BlueGreen` hook and specifies the properties for your
 deployment. For more information, see [AWS::CodeDeploy::BlueGreen hook
 syntax](blue-green-hook-syntax.md "blue-green-hook-syntax.md").
* In the `Resources` section, define the blue and green resources for your
 deployment.

You can add these sections when you first create the template (that's, before creating
 the stack itself), or you can add them to an existing template before performing a stack
 update. If you specify the blue/green deployment for a new stack, CloudFormation only creates
 the blue resources during stack creation — resources for the green deployment aren't
 created until they're required during a stack update.


## Modeling your blue/green deployment using CloudFormation
 resources


To perform CodeDeploy blue/green deployment on ECS, your CloudFormation template needs to include
 the resources that model your deployment, such as an Amazon ECS service and load balancer. For
 more details on what these resources represent, see [Before you begin an Amazon ECS deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-ecs.html#deployment-steps-prerequisites-ecs "https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-ecs.html#deployment-steps-prerequisites-ecs") in the *AWS CodeDeploy User
 Guide*.




| Requirement | Resource | Required/Optional | Initiates blue/green deployment if replaced? |
| --- | --- | --- | --- |
| Amazon ECS cluster | [AWS::ECS::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html") | Optional. The default cluster can be used. | No |
| Amazon ECS service | [AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html") | Required. | No |
| Application or Network Load Balancer | [AWS::ECS::Service LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-loadbalancer.html") | Required. | No |
| Production listener | [AWS::ElasticLoadBalancingV2::Listener](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html") | Required. | No |
| Test listener  | [AWS::ElasticLoadBalancingV2::Listener](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html") | Optional. | No |
| Two target groups | [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html") | Required. | No |
| Amazon ECS task definition  | [AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html") | Required. | Yes |
| Container for your Amazon ECS application | [AWS::ECS::TaskDefinition ContainerDefinition Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-name "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-name") | Required. | No |
| Port for your replacement task set | [AWS::ECS::TaskDefinition PortMapping ContainerPort](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-containerport "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-containerport") | Required. | No | ## Change sets We strongly recommend that you create a change set before performing a stack update that will initiate a green deployment. This allows you to see the actual changes that will be made to your stack before performing stack update. Be aware that resource changes may not be listed in the order in which they will be performed during the stack update. For more information, see [Update CloudFormation stacks using change sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md"). ## Monitoring stack events You can view the stack events generated at each step of the ECS deployment on the **Events** tab of the **Stack** page, and using the AWS CLI. For more information, see [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md"). ## IAM permissions for blue/green deployments In order for CloudFormation to successfully perform the blue-green deployments, you must have the following CodeDeploy permissions: <br>• `codedeploy:Get*` <br>• `codedeploy:CreateCloudFormationDeployment` For more information, see [Actions, resources, and condition keys for CodeDeploy](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodedeploy.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodedeploy.html") in the *Service Authorization Reference*.
