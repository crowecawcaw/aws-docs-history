# Creating Amazon Verified Permissions resources with

AWS CloudFormation

Amazon Verified Permissions is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want
(such as policy stores), and AWS CloudFormation provisions and configures those resources for you.

When you use AWS CloudFormation, you can reuse your template to set up your Verified Permissions resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

###### Important

Amazon Cognito Identity is not available in all of the same AWS Regions as Amazon Verified Permissions. If you receive
an error from AWS CloudFormation regarding Amazon Cognito Identity, such as `Unrecognized resource types:
 AWS::Cognito::UserPool, AWS::Cognito::UserPoolClient`, we recommend that you
create the Amazon Cognito user pool and client in the geographically closest AWS Region where
Amazon Cognito Identity is available. Use this newly created user pool when creating the Verified Permissions identity
source.

## Verified Permissions and AWS CloudFormation templates

To provision and configure resources for Verified Permissions and related services, you must
understand [AWS CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These templates
describe the resources that you want to provision in your AWS CloudFormation stacks. If you're
unfamiliar with JSON or YAML, you can use AWS CloudFormation Designer to help you get started with
AWS CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the
_AWS CloudFormation User Guide_.

Verified Permissions supports creating identity sources, policies, policy stores, and policy templates in AWS CloudFormation. For
more information, including examples of JSON and YAML templates for Verified Permissions resources, see
the [Amazon Verified Permissions
resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_VerifiedPermissions.md "../../../AWSCloudFormation/latest/UserGuide/AWS_VerifiedPermissions.md") in the _AWS CloudFormation User Guide_.

## AWS CDK constructs

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework for defining cloud
infrastructure in code and provisioning it through AWS CloudFormation. Constructs, or reusable
cloud components, can be used to create AWS CloudFormation templates. These templates can then be used
to deploy your cloud infrastructure.

To learn more and download AWS CDK, see [AWS Cloud Development Kit](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/").

The following are links to documentation for Verified Permissions AWS CDK resources, such as constructs.

- [Amazon Verified Permissions L2 CDK Construct](https://github.com/cdklabs/cdk-verified-permissions "https://github.com/cdklabs/cdk-verified-permissions")

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API
  Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
