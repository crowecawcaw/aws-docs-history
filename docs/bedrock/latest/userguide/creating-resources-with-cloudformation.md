# Create Amazon Bedrock resources with AWS CloudFormation

Amazon Bedrock is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want (such as
[Amazon Bedrock agents](agents.md "agents.md") or [Amazon Bedrock knowledge bases](knowledge-base.md "knowledge-base.md")), and CloudFormation provisions and configures those resources for
you.

When you use CloudFormation, you can reuse your template to set up your Amazon Bedrock resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

Amazon Bedrock provides resources in two CloudFormation namespaces: `AWS::Bedrock`, for
control-plane resources such as agents, knowledge bases, flows, guardrails, and prompts; and
`AWS::BedrockMantle`, for projects on the `bedrock-mantle` endpoint. The
following topics describe each namespace.

###### Topics

- [AWS::Bedrock resources](cfn-bedrock-resources.md "cfn-bedrock-resources.md")
- [AWS::BedrockMantle resources](cfn-mantle-resources.md "cfn-mantle-resources.md")
- [Learn more about CloudFormation](#learn-more-cloudformation "#learn-more-cloudformation")

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
