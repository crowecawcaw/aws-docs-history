# Creating automation rules with CloudFormation

AWS Compute Optimizer integrates with AWS CloudFormation, enabling you to define and deploy automation rules
with infrastructure-as-code. You can create a template that describes the automation rules
you want, and CloudFormation provisions and configures those rules for you. When you use CloudFormation, you
can reuse your template to set up your automation rules consistently and repeatedly across
multiple AWS accounts.

## Compute Optimizer and CloudFormation templates

To provision and configure automation rules, you must understand how [CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") work. Templates are text files in JSON or YAML format. These templates
describe the resources that you want to provision in your CloudFormation stacks.

If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get
started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User
Guide_.

You can create CloudFormation templates for the following types of automation rules:

- Account rules that apply recommended actions only to your account
- Organization rules that centrally apply recommended actions across member
  accounts

For more information, including examples of JSON and YAML templates for automation
rules, see [AWS::ComputeOptimizer::AutomationRule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.md") in the _AWS CloudFormation User
Guide_.

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API
  Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
