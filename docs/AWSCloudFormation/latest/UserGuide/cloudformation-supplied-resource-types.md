# Extend your template's capabilities
 with CloudFormation-supplied resource types

CloudFormation offers several resource types that you can use in your stack template to extend
 its capabilities beyond those of a simple stack template.

These resource types include:



| Resource type | Description | Documentation |
| --- | --- | --- |
| Custom resources | The `AWS::CloudFormation::CustomResource` resource type allows you to create custom resources that can perform specific provisioning tasks or include resources that aren't available as CloudFormation resource types. | [Custom resources](template-custom-resources.md "template-custom-resources.md") |
| Macros | The `AWS::CloudFormation::Macro` resource type defines a reusable piece of code that can perform custom processing on CloudFormation templates. Macros can modify your templates, generate additional resources, or perform other custom operations during stack creation or updates. | [Template macros](template-macros.md "template-macros.md") |
| Nested stacks | The `AWS::CloudFormation::Stack` resource type allows you to create nested stacks within your CloudFormation templates for a more modular and reusable stack architectures. | [Nested stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md") |
| StackSet | The `AWS::CloudFormation::StackSet` resource type creates or updates a CloudFormation StackSet, which is a container for stacks that can be deployed across multiple AWS accounts and Regions. | [Managing stacks with StackSets](what-is-cfnstacksets.md "what-is-cfnstacksets.md") |
| Wait condition | The `AWS::CloudFormation::WaitCondition` resource type pauses stack creation or update until a specific condition is met, such as the successful completion of a long-running process or the availability of external resources.  | [Wait conditions](using-cfn-waitcondition.md "using-cfn-waitcondition.md") |
| Wait condition handle | The `AWS::CloudFormation::WaitConditionHandle` resource type works together with the `AWS::CloudFormation::WaitCondition` resource type. It provides a presigned URL that's used to send signals indicating that a specific condition has been met. These signals allow the stack creation or update process to proceed. | [Wait conditions](using-cfn-waitcondition.md "using-cfn-waitcondition.md") |
