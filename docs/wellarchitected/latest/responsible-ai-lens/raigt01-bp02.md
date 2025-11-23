# RAIGT01-BP02 Create a system card that communicates intended

usage and limitations

AI system cards are a form of responsible AI documentation that
provide stakeholders with a single place to find information on the
intended use cases and limitations, responsible AI design choices,
and deployment and performance optimization best practices. System
cards do not provide guidance on expected performance of the AI
system on the specific inputs the deployer may provide; that testing
is the responsibility of the deployer.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Identify intended use case(s) to illustrate how users should
   plan to interact with your system. The use case section gives
   the reader a tangible example, describing the steps and
   workflow required end-to-end while calling out limitations in
   the technology.
2. Plan a specific set of evaluations for the AI service card. As
   appropriate, disclose the datasets chosen for the evaluations
   and how they meet the criteria to support the testing of each
   Responsible AI dimension. For example, datasets should have
   appropriate demographic labels for fairness testing, a
   representative sample of examples from known safety
   categories, and common as well as uncommon variations in the
   input examples for robustness testing.
3. Include performance metrics and success criteria for each use
   case, with real-world examples demonstrating proper
   implementation.
4. Detail system limitations and constraints. Consider financial
   risk assessment AI where specific market conditions or
   transaction types might fall outside system capabilities.
   Document scenarios where system performance may degrade or
   become unreliable, including environmental factors affecting
   behavior.
5. Outline potential failure modes and implementation strategies
   when appropriate. As an example, describe how a recommendation
   system might fail during high-traffic periods or with novel
   user patterns, and provide recommended responses. Include
   warning signs and blocking strategies for each failure mode.

## Resources

**Related documents:**

- [Introducing
  AWS AI Service Cards: A new resource to enhance transparency
  and advance responsible AI](https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai/ "https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai/")
- [Resources
  that promote AI transparency](https://aws.amazon.com/ai/responsible-ai/resources/ "https://aws.amazon.com/ai/responsible-ai/resources/")
- [Amazon SageMaker AI model cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md")
- [Model
  cards for model reporting](https://arxiv.org/abs/1810.03993 "https://arxiv.org/abs/1810.03993")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Transform
  responsible AI from theory into practice](https://aws.amazon.com/ai/responsible-ai/ "https://aws.amazon.com/ai/responsible-ai/")
- [Securing
  generative AI: data, compliance, and privacy
  considerations](https://aws.amazon.com/blogs/security/securing-generative-ai-data-compliance-and-privacy-considerations/ "https://aws.amazon.com/blogs/security/securing-generative-ai-data-compliance-and-privacy-considerations/")
- [Thorn
  and All Tech Is Human Forge Generative AI Principles with AI
  Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/ "https://www.thorn.org/blog/generative-ai-principles/")
- [ISO/IEC
  42001:2023 A.8.2 System documentation and information for
  users](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
- [ISO/IEC
  42001:2023 A.8.3 External Reporting](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
- [ISO/IEC
  42001:2023 A.8.5 Information for interested parties](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md")
- [Amazon SageMaker AI AI](../../../sagemaker/latest/dg/model-cards-create.md "../../../sagemaker/latest/dg/model-cards-create.md")
