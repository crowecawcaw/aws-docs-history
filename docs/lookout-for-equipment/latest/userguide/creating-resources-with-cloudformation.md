On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Creating Amazon Lookout for Equipment resources with

AWS CloudFormation

Amazon Lookout for Equipment is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your Lookout for Equipment resources and
infrastructure. You create a template that describes all the AWS resources that you want (such as
Amazon S3 buckets), and CloudFormation provisions and configures those resources for
you.

When you use CloudFormation, you can reuse your template to set up your Lookout for Equipment resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## Lookout for Equipment and CloudFormation templates

To provision and configure resources for Lookout for Equipment and related services, you must
understand [CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation
Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation
Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

Lookout for Equipment supports creating Amazon S3 buckets

in CloudFormation. For more information, including examples of JSON and YAML templates for
Amazon S3 buckets, see the [Lookout For Equipment resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_LookoutEquipment.md "../../../AWSCloudFormation/latest/UserGuide/AWS_LookoutEquipment.md") in the
_AWS CloudFormation User Guide_.

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
