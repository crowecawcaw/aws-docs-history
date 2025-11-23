# Create Amazon Keyspaces resources with AWS CloudFormation

Amazon Keyspaces is integrated with AWS CloudFormation, a service that helps you model and set up your
AWS keyspaces and tables so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes the keyspaces and tables that you want,
and CloudFormation takes care of provisioning and configuring those resources for
you.

When you use CloudFormation, you can reuse your template to set up your Amazon Keyspaces resources
consistently and repeatedly. Just describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## Amazon Keyspaces and CloudFormation templates

To provision and configure resources for Amazon Keyspaces, you must understand [CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These templates describe
the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or
YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more
information, see [What is CloudFormation
designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

Amazon Keyspaces supports creating keyspaces and tables in CloudFormation. For the tables you create using CloudFormation templates, you can specify the
schema, read/write mode, provisioned throughput settings, and other supported features.
For more information, including examples of JSON and YAML templates for
keyspaces and tables, see [Amazon Keyspaces (for Apache Cassandra) resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Cassandra.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Cassandra.md") in the
_AWS CloudFormation Template Reference_.

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation command
  line interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
