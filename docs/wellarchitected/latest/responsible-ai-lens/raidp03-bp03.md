# RAIDP03-BP03 Protect the privacy of individuals represented in

your datasets

Translate the guidance of your legal counsel on what constitutes
personal information into technical definitions appropriate to your
use case. Implement processes to identify and limit personal
information in training, evaluation, and auxiliary datasets, using
both automated filtering, data obfuscation, and manual review
approaches. Validate the effectiveness of your privacy protection
mechanisms against your taxonomy of personal information types.
Maintain detailed documentation of privacy protection measures and
regularly audit datasets so that personal information removal
doesn't compromise your ability to measure important system
behaviors.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Translate the guidance of your legal counsel into a taxonomy
   of personal data types. For example, define the string
   patterns for direct identifiers (like names and addresses),
   quasi-identifiers (like age and zip code), and other
   attributes (like health conditions and financial status)
   relevant to your domain.
2. Implement multi-layered privacy filtering processes combining
   automated detection, data obfuscation, and manual review. For
   instance, use regex patterns and named entity recognition to
   flag potential personal information, and then apply techniques
   like tokenization, masking, or synthetic data replacement.
3. Create test datasets with deliberately inserted personal
   information to evaluate privacy criteria while preserving data
   utility.
4. Balance privacy protection with system and evaluation needs by
   verifying that your privacy measures don't compromise your
   system's ability to address your use case or your ability to
   test release criteria. For instance, verify that anonymization
   techniques maintain demographic diversity needed for fairness
   assessments.
5. Document privacy protection decisions and create audit trails
   of what information gets filtered, obfuscated, or retained.

## Resources

**Related documents:**

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
- [Data
  protection in AWS Glue DataBrew](../../../databrew/latest/dg/data-protection.md "../../../databrew/latest/dg/data-protection.md")
- [Identifying
  and handling personally identifiable information (PII)](../../../databrew/latest/dg/personal-information-protection.md "../../../databrew/latest/dg/personal-information-protection.md")
- [Introducing
  PII data identification and handling using AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/ "https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/")
- [Machine
  learning with decentralized training data using federated
  learning on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/machine-learning-with-decentralized-training-data-using-federated-learning-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/machine-learning-with-decentralized-training-data-using-federated-learning-on-amazon-sagemaker/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.2 Data for development and enhancement
  of AI system
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems
