# AWS CloudFormation templates for CodeDeploy

reference

This section introduces the AWS CloudFormation resources, transform, and hook designed to work with
CodeDeploy deployments. For a walkthrough of creating a stack update managed by the AWS CloudFormation hook
for CodeDeploy, see [Create an Amazon ECS blue/green deployment
through AWS CloudFormation](deployments-create-ecs-cfn.md "deployments-create-ecs-cfn.md")

###### Note

AWS CloudFormation hooks are part of the AWS CloudFormation components for AWS and are different from CodeDeploy
lifecycle event hooks.

In addition to the other methods available to you in CodeDeploy, you can use AWS CloudFormation templates to
perform the following tasks:

- Create applications.
- Create deployment groups and specify a target revision.
- Create deployment configurations.
- Create Amazon EC2 instances.
  AWS CloudFormation is a service that helps you model and set up your AWS resources using templates.
  An AWS CloudFormation template is a text file whose format complies with the JSON standard. You create a
  template that describes all of the AWS resources you want, and AWS CloudFormation takes care of
  provisioning and configuring those resources for you.

For more information, see [What is
AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") and [Working with
AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") in _AWS CloudFormation User Guide_.

If you plan to use AWS CloudFormation templates that are compatible with CodeDeploy in your organization, as
an administrator, you must grant access to AWS CloudFormation and to the AWS services and actions on
which AWS CloudFormation depends. To grant permissions to create applications, deployment groups, and
deployment configurations, add the following policy to the permission set of the users who
will work with AWS CloudFormation:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about policies, see the following topics:

- To view the policy that must be added to the permission set of users who will
  create Amazon EC2 instances, see [Create an Amazon EC2 instance for
  CodeDeploy (AWS CloudFormation template)](instances-ec2-create-cloudformation-template.md "instances-ec2-create-cloudformation-template.md").
- For information about adding policies to permission sets, see [Create a
  permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _IAM User Guide_.
- To learn how to restrict users to a limited set of CodeDeploy actions and resources,
  see [AWS managed (predefined) policies for
  CodeDeploy](managed-policies.md "managed-policies.md").
  The following table shows the actions an AWS CloudFormation template can perform on your behalf and
  includes links to more information about the AWS resource types and their property types
  you can add to an AWS CloudFormation template.

| Action                                                                                                                                                                                                     | AWS CloudFormation reference                                                                                                                                                                                                                 | Reference type                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Create a CodeDeploy application.                                                                                                                                                                           | [AWS::CodeDeploy::application](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.md")                                      | AWS CloudFormation resource                                                      |
| Create and specify the details for a deployment group to be used to deploy your application revisions. ¹                                                                                                   | [AWS::CodeDeploy::DeploymentGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.md")                          | AWS CloudFormation resource                                                      |
| Create a set of deployment rules, deployment success conditions, and deployment failure conditions that CodeDeploy will use during a deployment.                                                           | [AWS::CodeDeploy::DeploymentConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.md")                       | AWS CloudFormation resource                                                      |
| Create an Amazon EC2 instance. ²                                                                                                                                                                           | [AWS::EC2::instance](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.md")                                                                | AWS CloudFormation resource                                                      |
| Use the AWS CloudFormation `AWS::CodeDeployBlueGreen` transform and `AWS::CodeDeploy::BlueGreen` hook to manage stack updates, create resources, and shift traffic for CodeDeploy blue/green deployments.3 | [AWS::CodeDeployBlueGreen](../../../AWSCloudFormation/latest/UserGuide/blue-green.md "../../../AWSCloudFormation/latest/UserGuide/blue-green.md")                                                                                            | The `AWS::CodeDeployBlueGreen` transform is a macro hosted by AWS CloudFormation |
| [AWS::CodeDeploy::BlueGreen](../../../AWSCloudFormation/latest/UserGuide/blue-green.md "../../../AWSCloudFormation/latest/UserGuide/blue-green.md")                                                        | The `AWS::CodeDeploy::BlueGreen` hook is structured as a `Hook` resource in AWS CloudFormation. The hook includes parameters that take the place of your CodeDeploy AppSpec file by pointing to designated CodeDeploy lifecycle event hooks. |                                                                                  | ¹ If you specify the version of the application revision that you want to be deployed as part of the deployment group, your target revision will be deployed as soon as the provisioning process is complete. For more information about template configuration, see [CodeDeploy DeploymentGroup deployment revision S3Location](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.md") and [CodeDeploy DeploymentGroup deployment revision GitHubLocation](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.md") in the _AWS CloudFormation User Guide_. ² We provide templates you can use to create Amazon EC2 instances in the regions in which CodeDeploy is supported. For more information about using these templates, see [Create an Amazon EC2 instance for CodeDeploy (AWS CloudFormation template)](instances-ec2-create-cloudformation-template.md "instances-ec2-create-cloudformation-template.md"). 3Only Amazon ECS blue/green deployments are supported by this deployment configuration. For more information about deployment configurations for Amazon ECS blue/green deployments through AWS CloudFormation, see [Deployment configurations for AWS CloudFormation blue/green deployments (Amazon ECS)](deployment-configurations.md#deployment-configuration-cfn-bg "deployment-configurations.md#deployment-configuration-cfn-bg"). For more information about Amazon ECS blue/green deployments through AWS CloudFormation and how to view your deployment in CodeDeploy, see [Create an Amazon ECS blue/green deployment through AWS CloudFormation](deployments-create-ecs-cfn.md "deployments-create-ecs-cfn.md"). |     |
