# Creating Security Hub CSPM resources with

CloudFormation

AWS Security Hub CSPM integrates with AWS CloudFormation, which is a service that helps you model and set up
your AWS resources so that you can spend less time creating and managing your resources
and infrastructure. You create a template that describes all the AWS resources that you
want (such as automation rules), and AWS CloudFormation provisions and configures those resources for
you.

When you use AWS CloudFormation, you can reuse your template to set up your Security Hub CSPM resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## Security Hub CSPM and AWS CloudFormation templates

To provision and configure resources for Security Hub CSPM and related services, you must
understand how [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md")
work. Templates are text files in JSON or YAML format. These templates describe the
resources that you want to provision in your AWS CloudFormation stacks.

If you're unfamiliar with JSON or YAML, you can use AWS CloudFormation Designer to help you get
started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the
_AWS CloudFormation User Guide_.

You can create AWS CloudFormation templates for the following types of Security Hub CSPM resources:

- Enabling Security Hub CSPM
- Designating the delegated Security Hub CSPM administrator for an organization
- Specify the way your organization is configured in Security Hub CSPM
- Enabling a security standard
- Enabling cross-Region aggregation
- Creating a central configuration policy and associating it with accounts, organizational unit (OUs), or the root
- Creating a custom insight
- Creating an automation rule
- Customizing control parameters
- Subscribing to a third-party product integration

For more information, including examples of JSON and YAML templates for resources, see
the [AWS Security Hub CSPM resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.md") in the _AWS CloudFormation User Guide_.

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API
  Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
