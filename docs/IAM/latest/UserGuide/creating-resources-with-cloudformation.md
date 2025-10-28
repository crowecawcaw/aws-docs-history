# Create IAM resources with

AWS CloudFormation

AWS Identity and Access Management is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want (such as
access keys, groups, group policies, instance profiles, managed policies, OIDC providers, inline policies, roles, role policies, SAML providers, server certificates, service-linked roles, users (and adding users to groups), user policies, and virtual MFA devices), and AWS CloudFormation provisions and configures those resources for
you.

When you use AWS CloudFormation, you can reuse your template to set up your IAM resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## IAM and AWS CloudFormation templates

To provision and configure resources for IAM and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use AWS CloudFormation
Designer to help you get started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation
Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

IAM supports creating access keys, groups, group policies, instance profiles, managed policies, OIDC providers, inline policies, roles, role policies, SAML providers, server certificates, service-linked roles, users (and adding users to groups), user policies, and virtual MFA devices
in AWS CloudFormation. For more information, including examples of JSON and YAML templates for
IAM resources, see the [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_.

You can also create templates that
create related resources, such as roles and managed policies.

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
