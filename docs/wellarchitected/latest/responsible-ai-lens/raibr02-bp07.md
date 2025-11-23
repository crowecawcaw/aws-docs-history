# RAIBR02-BP07 Identify potential harmful events impacting

explainability

Users may want or need to understand why their input produced the
system output that it did. Consider, for example, what harm might
result from rejecting a loan application if an explanation would
have assisted the user to fix an incorrect input. A lack of
understanding of system outputs can compound AI harmful events and
errors, making troubleshooting difficult.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Consider scenarios where your users might be confused or
   frustrated by your AI system's outputs, especially when those
   outputs could lead to significant decisions. For example, if
   your system recommends against a loan application or insurance
   coverage or flags content for removal, consider the
   information that users would want to contest or improve the
   result.
2. Identify situations where users could take corrective action
   if they understood your system's reasoning but might give up
   or make things worse without that understanding. This includes
   cases where users provided incorrect information, missed
   required fields, or could improve their outcomes by adjusting
   their inputs or approach.
3. Consider whether your organization has requirements around AI
   system outputs, and whether AI system outputs could fail to
   meet those requirements.
4. Consider how a lack of explanation might amplify other
   problems with your system by making it harder for users to
   provide feedback, for operators to troubleshoot issues, or for
   your team to identify when the system is making systematic
   errors.
5. Look for situations where misunderstanding your system's
   outputs could lead users to make harmful decisions themselves,
   such as ignoring important warnings, over-relying on uncertain
   recommendations, or losing trust in legitimate system outputs.
   Think about both immediate harms to individual users and
   broader impacts if many people misunderstand how your system
   works.

## Resources

**Related documents:**

- [Advanced tracing and evaluation of generative AI agents using LangChain and Amazon SageMaker AI MLFlow](https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/ "https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/")
- [Build
  verifiable explainability into financial services workflows with Automated reasoning checks using Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/build-verifiable-explainability-into-financial-services-workflows-with-automated-reasoning-checks-for-amazon-bedrock-guardrails/ "https://aws.amazon.com/blogs/machine-learning/build-verifiable-explainability-into-financial-services-workflows-with-automated-reasoning-checks-for-amazon-bedrock-guardrails/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.5.4 Assessing AI system impact on individuals or groups of individuals
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.8.2 System documentation and information for users

**Related videos:**

- [Amazon
  Bedrock AgentCore - Observability | Amazon Web Services](https://www.youtube.com/watch?v=i2Pxnck_3tY "https://www.youtube.com/watch?v=i2Pxnck_3tY")
- [AWS re:Invent 2024 - Building explainable AI models with Amazon SageMaker AI (DEV219)](https://www.youtube.com/watch?v=UbeyQmY1qCw "https://www.youtube.com/watch?v=UbeyQmY1qCw")

**Related tools:**

- [Amazon
  Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/ "https://aws.amazon.com/bedrock/guardrails/")
