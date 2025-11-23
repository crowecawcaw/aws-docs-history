# RAISP03-BP03 Implement output filtering to catch unsafe content

before it reaches users

Build screening mechanisms that automatically review and filter your
system's outputs to catch potentially harmful content before users
see it, acting as a final safety check regardless of what your
system generates. This means implementing safety classifiers that
can identify toxic, harmful, or inappropriate content in real-time,
content filtering systems that block or modify unsafe outputs based
on your safety definitions, and automated screening processes that
evaluate each response against your safety criteria before delivery.

For example, if your release criteria include safety standards for
blocking harmful outputs, you might implement toxicity detection
models that score each response, build content filters that
automatically block responses containing harmful information, or
create screening systems that flag suspicious outputs for human
review before they reach users.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Based upon release criteria, identify types of potentially
   harmful content, including adversarial inputs and categories
   outside of your system's use case
2. Map the types of potentially harmful content to available
   content filters, such as those already built-in to safeguard
   services. Additional safety concerns may require custom
   safeguards, either through system prompting, fine tuning,
   exact match word configuration, or non-AI solutions that
   control critical access and permissions to resources.
3. Configure or customize safety filters that can identify and
   block potentially harmful content across multiple categories
   such as violence, self-harm, illegal activities, and other
   context-specific safety concerns.

## Resources

**Related documents:**

- [Amazon
  Bedrock Guardrails enhances generative AI application safety
  with new capabilities](https://aws.amazon.com/blogs/aws/amazon-bedrock-guardrails-enhances-generative-ai-application-safety-with-new-capabilities/ "https://aws.amazon.com/blogs/aws/amazon-bedrock-guardrails-enhances-generative-ai-application-safety-with-new-capabilities/")
- [Measuring
  and Mitigating Toxicity in LLMs](https://github.com/aws-samples/measuring-and-mitigating-toxicity-in-llms?tab=readme-ov-file#measuring-and-mitigating-toxicity-in-llms "https://github.com/aws-samples/measuring-and-mitigating-toxicity-in-llms?tab=readme-ov-file#measuring-and-mitigating-toxicity-in-llms")
- [Flag
  harmful content using Amazon Comprehend toxicity
  detection](https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/ "https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/")
- [Thorn
  and All Tech Is Human Forge Generative AI Principles with AI
  Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/ "https://www.thorn.org/blog/generative-ai-principles/")
- [ISO/IEC
  42001:2023 A.6.1.2 Objectives for responsible development of
  AI system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related video:**

- [AWS re:Invent 2024 - Responsible AI: From theory to practice with
  AWS (AIM210)](https://www.youtube.com/watch?v=SCXw2xuoF6o "https://www.youtube.com/watch?v=SCXw2xuoF6o")
- [AWS re:Invent 2024 - Build an AI gateway for Amazon Bedrock with
  AWS AppSync (FWM310)](https://www.youtube.com/watch?v=iW7OWwct-Ww "https://www.youtube.com/watch?v=iW7OWwct-Ww")

**Related tools:**

- [Amazon
  Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/ "https://aws.amazon.com/bedrock/guardrails/")
