# Creating Multi-party approval resources with

AWS CloudFormation

Multi-party approval is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want (such as
`AWS::MPA::ApprovalTeam` and `AWS::MPA::IdentitySource`), and AWS CloudFormation provisions and configures those resources for
you.

When you use AWS CloudFormation, you can reuse your template to set up your Multi-party approval resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

**Team activation requirements for AWS CloudFormation deployments**

If you create an approval team using AWS CloudFormation, the team will initially be created
in a _pending activation_ state. For more information see, [Team health](team-health.md "team-health.md"). To activate the team, every invited approver must accept the team invitation within 24 hours.

If at least one approver declines the team invitation or the 24-hour time window to respond expires, the team activation fails. This failure triggers a rollback of the AWS CloudFormation template, which deletes the team.

## Multi-party approval and AWS CloudFormation templates

To provision and configure resources for Multi-party approval and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use AWS CloudFormation
Designer to help you get started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation
Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

Multi-party approval supports creating `AWS::MPA::ApprovalTeam` and `AWS::MPA::IdentitySource`

in AWS CloudFormation. For more information, including examples of JSON and YAML templates for
`AWS::MPA::ApprovalTeam` and `AWS::MPA::IdentitySource`, see the [MPA](../../../AWSCloudFormation/latest/UserGuide/AWS_MPA.md "../../../AWSCloudFormation/latest/UserGuide/AWS_MPA.md") in the
_AWS CloudFormation User Guide_.

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
