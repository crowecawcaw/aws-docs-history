# RAIGT01-BP04 Guide users on how to understand system

outputs

Provide accessible guidance on how a user should interpret system
outputs. Provide guidance on features the user can use to better
understand why a particular input might have produced a specific
output. This includes features such as confidence scores, feature
importance indicators, decision paths, or chains of thought. Tailor
the complexity and format of the guidance to match user expertise
levels, providing both high-level summaries and detailed technical
information as appropriate. Assist users to identify when to trust
system outputs, when to seek additional verification, and when to
override or ignore system recommendations based on their domain
knowledge.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

1. Provide guidance on assisting users to understand how the
   decisions were made for predicting certain outcome. This
   includes showing which factors were most influential (feature
   importance) and how certain the system is about its decision
   (confidence scores). For traditional ML models, Amazon SageMaker AI Canvas provides visual explanations showing these
   key factors and confidence levels. For example, a loan
   approval system would display the main factors affecting the
   decision with their relative importance, how confident the
   system is in its prediction (expressed as a percentage),
   historical patterns that influenced the decision and data
   quality indicators supporting the prediction.
2. For generative AI systems and agents, consider looking at
   chain of thought techniques that provide the step-by-step
   thinking process, use observability features like from Amazon
   Bedrock Cloud Watch integrations to understand traces
   collected from agents execution that provides visibility to
   how tools for the agent was selected to be invoked that
   allowed agents to act. Amazon Bedrock Agents and AgentCore
   provide detailed traces showing how the system reached its
   conclusion. For example, a customer service agent would show
   the sequence of steps taken to resolve a query, which
   knowledge sources or tools were consulted, why specific
   approaches were chosen and what alternative options that were
   considered
3. When possible, provide ways to the users of AI system to
   understand when to rely on system outputs and when to seek
   additional verification. Implement monitoring, for example,
   use AWS AgentCore observability features to trace reliability.
   For instance, an AI-powered diagnostic system would set clear
   thresholds for automatic approval versus human review based
   upon tool invoked and other criteria's, show confidence levels
   with simple-to-understand indicators, provide specific
   criteria for when to seek expert verification

## Resources

**Related documents:**

- [ISO/IEC
  42001:2023 A.8.2 System documentation and information for
  users](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [AWS EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Amazon Simple Notification Service](https://aws.amazon.com/pm/sns/ "https://aws.amazon.com/pm/sns/")
- [Observe
  your agent applications on Amazon Bedrock AgentCore
  Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
