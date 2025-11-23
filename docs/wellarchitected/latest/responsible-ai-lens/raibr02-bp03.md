# RAIBR02-BP03 Identify potential harmful events impacting

robustness

Mishandling foreseeable variations in inputs can create harmful
events. Input variations come in two kinds. Intrinsic variations
are differences in input data to which an AI system must attend to
succeed. Confounding variations are differences in input data that
an AI system must ignore to succeed. You should also consider
whether slight changes in input data can produce dramatically
different outputs and how input instabilities can cascade across
system components.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Map input variation scenarios and their potential harmful
   impacts. Consider medical imaging AI, where varying equipment
   calibrations and scan qualities influence diagnostic accuracy.
   Document how differences in data format, quality, and
   characteristics affect reliability.
2. Analyze how input patterns shift over time to identify
   distribution harms. For example, recommendation systems should
   adapt to evolving user preferences and emerging content
   categories. Seasonal trends and special events often introduce
   unexpected usage patterns.
3. Consider cascading effects in multi-step workflows. In a
   multi-step AI workflow where one model's output feeds into
   another, assess how initial inaccuracies could amplify through
   the chain. For example, in a document processing system,
   errors in text extraction might affect subsequent
   classification or summarization steps.

## Resources

**Related documents:**

- [Improve
  LLM application robustness with Amazon Bedrock Guardrails and
  Amazon Bedrock Agents](https://aws.amazon.com/blogs/machine-learning/improve-llm-application-robustness-with-amazon-bedrock-guardrails-and-amazon-bedrock-agents/ "https://aws.amazon.com/blogs/machine-learning/improve-llm-application-robustness-with-amazon-bedrock-guardrails-and-amazon-bedrock-agents/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.5.4 Assessing AI system impact on
  individuals or groups of individuals
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems

**Related tools:**

## Evaluate the performance of Amazon Bedrock Resources

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
