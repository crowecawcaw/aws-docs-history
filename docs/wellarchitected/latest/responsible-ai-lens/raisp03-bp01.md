# RAISP03-BP01 Add privacy-preserving filters

Implement filtering mechanisms that automatically detect and remove
unwanted confidential and personal data from both inputs and
outputs. Design input sanitization processes that cleanse user
queries and system data of unwanted information before processing,
using both rule-based and machine learning approaches to identify
personal data. Implement output filtering that blocks the generation
or disclosure of confidential or personal information, including
techniques like anonymization that replace identifying details with
generic placeholders or synthetic alternatives.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Create a strategy for Identifying unwanted data including
   personal information and domain-specific information that
   should not be included in inputs or outputs, then implement
   appropriate detection methods using tools like Amazon Bedrock
   Guardrails for filtering inputs and outputs.
2. Design and implement privacy filters for both inputs and
   outputs, using meaningful placeholders for redacted
   information and verifying proper encryption for data storage
   and transmission.
3. Design for unwanted data redaction across data touchpoints
   including logs and evaluation reports, not just primary inputs
   and outputs.

## Resources

**Related video:**

- [Amazon
  Bedrock Guardrails: Implementing Custom Safeguards for
  Responsible AI Applications](https://aws.amazon.com/awstv/watch/02103dd95d3/ "https://aws.amazon.com/awstv/watch/02103dd95d3/")
- [AWS re:Inforce 2025 - Privacy-first generative AI: Establishing
  guardrails for compliance (COM224)](https://www.youtube.com/watch?v=GAjWNoxgkYY "https://www.youtube.com/watch?v=GAjWNoxgkYY")

**Related tools:**

- [Remove
  PII from conversations by using sensitive information
  filters](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md")

**Related documents:**

- [Differentially
  Private Fair Learning](https://arxiv.org/abs/1812.02696 "https://arxiv.org/abs/1812.02696")
- [Remove
  PII from conversations by using sensitive information
  filters](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md")
- [Towards
  Efficient Privacy-Preserving Machine Learning: A Systematic
  Review from Protocol, Model, and System Perspectives](https://arxiv.org/pdf/2507.14519 "https://arxiv.org/pdf/2507.14519")
- [Training
  curriculum on AI and data protection Fundamentals of Secure AI
  Systems with Personal Data](https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf "https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf")
- [AI
  Privacy Risks & Mitigations - Large Language Models
  (LLMs)](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf "https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf")
- [An
  overview of implementing security and privacy in federated
  learning](https://link.springer.com/article/10.1007/s10462-024-10846-8 "https://link.springer.com/article/10.1007/s10462-024-10846-8")
- [Understanding
  Users' Security and Privacy Concerns and Attitudes Towards
  Conversational AI Platforms](https://arxiv.org/html/2504.06552v1 "https://arxiv.org/html/2504.06552v1")
- [Clio:
  Privacy-Preserving Insights into Real-World AI Use](https://arxiv.org/pdf/2506.07555 "https://arxiv.org/pdf/2506.07555")
- [Privacy
  Preserving Machine Learning Model Personalization through
  Federated Personalized Learning](https://arxiv.org/pdf/2505.01788 "https://arxiv.org/pdf/2505.01788")
- [Privacy-Preserving
  AI: Techniques & Frameworks](https://dialzara.com/blog/privacy-preserving-ai-techniques-and-frameworks "https://dialzara.com/blog/privacy-preserving-ai-techniques-and-frameworks")
- [Data
  Anonymisation Made Simple - 7 Methods & Best
  Practices](https://spotintelligence.com/2025/03/06/data-anonymisation/ "https://spotintelligence.com/2025/03/06/data-anonymisation/")
- [A
  Comprehensive Guide to Differential Privacy: From Theory to
  User Expectations](https://arxiv.org/html/2509.03294v1 "https://arxiv.org/html/2509.03294v1")
- [ISO/IEC
  42001:2023 A.6.1.2 Objectives for responsible development of
  AI system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
