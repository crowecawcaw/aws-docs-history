# Create Amazon Bedrock resources with

AWS CloudFormation

Amazon Bedrock is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want (such as
[Amazon Bedrock agents](agents.md "agents.md") or [Amazon Bedrock knowledge bases](knowledge-base.md "knowledge-base.md")), and AWS CloudFormation provisions and configures those resources for
you.

When you use AWS CloudFormation, you can reuse your template to set up your Amazon Bedrock resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## Amazon Bedrock and AWS CloudFormation templates

To provision and configure resources for Amazon Bedrock and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use AWS CloudFormation
Designer to help you get started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation
Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

Amazon Bedrock supports creating the following resources

in AWS CloudFormation.

- [AWS::Bedrock::Agent](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.md")
- [AWS::Bedrock::AgentAlias](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agentalias.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agentalias.md")
- [AWS::Bedrock::ApplicationInferenceProfile](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-applicationinferenceprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-applicationinferenceprofile.md")
- [AWS::Bedrock::AutomatedReasoningPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-automatedreasoningpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-automatedreasoningpolicy.md")
- [AWS::Bedrock::AutomatedReasoningPolicyVersion](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-automatedreasoningpolicyversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-automatedreasoningpolicyversion.md")
- [AWS::Bedrock::DataSource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-datasource.md")
- [AWS::Bedrock::Flow](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flow.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flow.md")
- [AWS::Bedrock::FlowVersion](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flowversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flowversion.md")
- [AWS::Bedrock::FlowAlias](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flowalias.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flowalias.md")
- [AWS::Bedrock::Guardrail](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-guardrail.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-guardrail.md")
- [AWS::Bedrock::GuardrailVersion](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-guardrailversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-guardrailversion.md")
- [AWS::Bedrock::KnowledgeBase](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-knowledgebase.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-knowledgebase.md")
- [AWS::Bedrock::Prompt](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-prompt.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-prompt.md")
- [AWS::Bedrock::PromptVersion](../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-promptversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-promptversion.md")

For more information, including examples of JSON and YAML templates for
[Amazon Bedrock agents](agents.md "agents.md") or [Amazon Bedrock knowledge bases](knowledge-base.md "knowledge-base.md"), see the [Amazon Bedrock resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Bedrock.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Bedrock.md") in the
_AWS CloudFormation User Guide_.

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
