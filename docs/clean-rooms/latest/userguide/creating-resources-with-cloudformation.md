# Creating AWS Clean Rooms resources with

AWS CloudFormation

AWS Clean Rooms is integrated with AWS CloudFormation, a service that helps you to model and set up
your AWS resources. As a result of this integration, you can spend less time creating and
managing your resources and infrastructure. You create a template that describes all the AWS
resources that you want, and AWS CloudFormation provisions and configures those resources for you. Examples
of resources include collaborations, configured tables, configured table associations, and memberships.

When you use AWS CloudFormation, you can reuse your template to set up your AWS Clean Rooms resources
consistently and repeatedly. Describe your resources once, and then provision the same resources
over and over in multiple AWS accounts and AWS Regions.

## AWS Clean Rooms and AWS CloudFormation templates

To provision and configure resources for AWS Clean Rooms and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md").
Templates are formatted text files in JSON or YAML. These templates describe the resources
that you want to provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you
can use AWS CloudFormation Designer to help you get started with AWS CloudFormation templates. For more information, see
[What is
AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

AWS Clean Rooms supports creating collaborations, configured tables, configured table associations, and memberships in AWS CloudFormation. For more information, including examples
of JSON and YAML templates for collaborations, configured tables, configured table associations, and memberships, see the [AWS Clean Rooms](../../../AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.md") and
[AWS Clean Rooms ML](../../../AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.md") resource type references in the
_AWS CloudFormation User Guide_.

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation
  Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
