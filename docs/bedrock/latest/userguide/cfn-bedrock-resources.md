# `AWS::Bedrock` resources

The `AWS::Bedrock` namespace contains the Amazon Bedrock control-plane resources that
you create through `bedrock` and : agents, knowledge bases, flows, guardrails,
and prompts.

## Amazon Bedrock and CloudFormation templates

To provision and configure resources for Amazon Bedrock and related services, you must
understand [CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation
Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation
Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

Amazon Bedrock supports creating the following resources

in CloudFormation.

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
