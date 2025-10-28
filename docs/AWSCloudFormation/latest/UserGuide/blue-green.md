# Perform ECS blue/green deployments through CodeDeploy using

CloudFormation

To update an application running on Amazon Elastic Container Service (Amazon ECS), you can use a CodeDeploy blue/green
deployment strategy. This strategy helps minimize interruptions caused by changing application
versions.

In a blue/green deployment, you create a new application environment (referred to as
_green_) alongside your current, live environment (referred to as
_blue_). This allows you to monitor and test the green environment before
routing live traffic from the blue environment to the green environment. After the green
environment is serving live traffic, you can safely terminate the blue environment.

To perform CodeDeploy blue/green deployments on ECS using CloudFormation, you include the following
information in your stack template:

- A `Hooks` section that describes a `AWS::CodeDeploy::BlueGreen`
  hook.
- A `Transform` section that specifies the
  `AWS::CodeDeployBlueGreen` transform.
  The following topics guide you through setting up a CloudFormation template for a blue/green
  deployment on ECS.

###### Topics

- [About blue/green deployments](about-blue-green-deployments.md "about-blue-green-deployments.md")
- [Considerations when managing ECS blue/green
  deployments using CloudFormation](blue-green-considerations.md "blue-green-considerations.md")
- [AWS::CodeDeploy::BlueGreen hook
  syntax](blue-green-hook-syntax.md "blue-green-hook-syntax.md")
- [Blue/green deployment template example](blue-green-template-example.md "blue-green-template-example.md")
