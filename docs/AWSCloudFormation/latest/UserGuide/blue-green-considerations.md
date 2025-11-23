# Considerations when managing ECS blue/green

deployments using CloudFormation

The process of using CloudFormation to perform your ECS blue/green deployments through CodeDeploy
is different from a standard ECS deployment using just CodeDeploy. For a detailed understanding of
these differences, see [Differences between Amazon ECS blue/green deployments through CodeDeploy and CloudFormation](../../../codedeploy/latest/userguide/deployments-create-ecs-cfn.md#differences-ecs-bg-cfn "../../../codedeploy/latest/userguide/deployments-create-ecs-cfn.md#differences-ecs-bg-cfn") in the
_AWS CodeDeploy User Guide_.

When managing your blue/green deployment using CloudFormation, there are certain limitations
and considerations to keep in mind:

- Only updates to certain resources will initiate a green deployment. For more
  information, see [Resource updates that initiate green
  deployments](about-blue-green-deployments.md#blue-green-resources "about-blue-green-deployments.md#blue-green-resources").
- You can't include updates to resources that initiate green deployments and updates to
  other resources in the same stack update. For more information, see [Resource updates that initiate green
  deployments](about-blue-green-deployments.md#blue-green-resources "about-blue-green-deployments.md#blue-green-resources").
- You can only specify a single ECS service as the deployment target.
- Parameters whose values are obfuscated by CloudFormation can't be updated by CodeDeploy during
  a green deployment, and will lead to an error and stack update failure. These
  include:
  - Parameters defined with the `NoEcho` attribute.
  - Parameters that use dynamic references to retrieve their values from external
    services. For more information about dynamic references, see [Get values stored in other services using dynamic
    references](dynamic-references.md "dynamic-references.md").

- To cancel a green deployment that's still in progress, cancel the stack update in
  CloudFormation, not CodeDeploy or ECS. For more information, see [Cancel a stack update](using-cfn-stack-update-cancel.md "using-cfn-stack-update-cancel.md").
  After an update has finished, you can't cancel it. However, you can update a stack again
  with any previous settings.
- The following CloudFormation features are not currently supported for templates that
  define ECS blue/green deployments:
  - Declaring [outputs](outputs-section-structure.md "outputs-section-structure.md") or using [Fn::ImportValue](../TemplateReference/intrinsic-function-reference-importvalue.md "../TemplateReference/intrinsic-function-reference-importvalue.md") to import values from other stacks.
  - Importing resources. For more information about importing resources, see [Import AWS resources into a CloudFormation stack](import-resources.md "import-resources.md").
  - Using the `AWS::CodeDeploy::BlueGreen` hook in a template that includes
    nested stack resources. For more information about nested stacks, see [Split a template into reusable pieces using nested
    stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md").
  - Using the `AWS::CodeDeploy::BlueGreen` hook in a nested stack.
