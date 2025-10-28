# Creating Macie resources with

AWS CloudFormation

Amazon Macie integrates with [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md"), which is a service that helps you model and set up your AWS resources so
that you can spend less time creating and managing your resources and infrastructure. You create a
template that describes all the AWS resources that you want (such as custom data identifiers), and AWS CloudFormation
provisions and configures those resources for you.

When you use AWS CloudFormation, you can reuse your template to set up your Macie resources consistently
and repeatedly. Describe your resources once, and then provision the same resources over and over
in multiple AWS accounts and AWS Regions.

## Macie and AWS CloudFormation templates

To provision and configure resources for Amazon Macie and related services, you must understand
AWS CloudFormation templates. The templates describe the resources that you want to provision in your AWS CloudFormation
stacks. They are text files in JSON or YAML format. If you're unfamiliar with JSON or YAML,
AWS Infrastructure Composer or AWS CloudFormation Designer can help you get started. For more information, see [Working with
CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") in the _AWS CloudFormation User
Guide_.

You can create AWS CloudFormation templates for the following types of Macie resources:

- Allow lists
- Custom data identifiers
- Filter rules and suppression rules for findings, also referred to as _findings filters_

For more information, including examples of JSON and YAML templates for these types of
resources, see the [Amazon Macie resource type reference](../../../AWSCloudFormation/latest/TemplateReference/AWS_Macie.md "../../../AWSCloudFormation/latest/TemplateReference/AWS_Macie.md") in the
_AWS CloudFormation User Guide_.

## Additional learning resources for AWS CloudFormation

To learn more about AWS CloudFormation, refer to the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
