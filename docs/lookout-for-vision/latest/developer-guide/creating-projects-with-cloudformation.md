End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating Amazon Lookout for Vision resources with

AWS CloudFormation

Amazon Lookout for Vision is integrated with AWS CloudFormation, a service that helps you model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want,
and AWS CloudFormation takes care of provisioning and configuring those resources for
you.

You can use AWS CloudFormation to provision and configure Amazon Lookout for Vision projects.

When you use AWS CloudFormation, you can reuse your template to set up your Lookout for Vision projects
consistently and repeatedly. Just describe your projects once, and then provision the same
projects over and over in multiple AWS accounts and Regions.

## Lookout for Vision and AWS CloudFormation templates

To provision and configure projects for Lookout for Vision and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use AWS CloudFormation
Designer to help you get started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation
Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

For reference information about Lookout for Vision projects, including examples of JSON and YAML templates,
see [LookoutVision resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_LookoutVision.md "../../../AWSCloudFormation/latest/UserGuide/AWS_LookoutVision.md").

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
