# RAISP02-BP02 Privacy: Build privacy-preserving mechanisms into

the core AI system

Design your system from the start to protect confidential and
personal data. This may include incorporating techniques like data
encryption, access controls, data minimization, data obfuscation,
and privacy-preserving training methods directly into how your
system works, based on your release criteria.

For example, if your release criteria include keeping certain types
of user information confidential, you might build in automatic data
masking, use techniques that scramble sensitive information while
keeping it useful for training, or set up your system to process
information without storing sensitive details. The specific privacy
mechanisms you choose should align with your release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Implement data protection measures: Establish security
   protections around sensitive information. First, identify
   essential data requirements through data minimization
   analysis. Create a mapping of sensitive fields and implement
   anonymization. For example, in a healthcare system, converting
   'John Doe, diabetic, 123 Main Street' to 'Patient_2384,
   condition_type_2, region_14' maintains analytical value while
   protecting individual privacy. Encrypt sensitive data at rest
   and in transit. Establish role-based access controls with
   documented access levels for sensitive data.
2. Apply privacy-preserving training techniques: Consider using
   differential privacy techniques to introduce controlled noise
   to the training process. For example, when processing customer
   transaction data, apply calculated variations to individual
   purchases while maintaining accurate aggregate patterns.
   Consider using federated learning to enable distributed model
   training where data remains at source locations.

For example, with federated learning, healthcare institutions
can improve diagnostic models by sharing only parameter updates
instead of raw patient data. Consider using gradient clipping to
block individual training examples from disproportionately
influencing model learning, maintaining both privacy and model
quality.

## Resources

**Related documents:**

- [Differentially
  Private Fair Learning](https://arxiv.org/abs/1812.02696 "https://arxiv.org/abs/1812.02696")
- [Remove
  PII from conversations by using sensitive information
  filters](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md")
- [ISO/IEC
  42001:2023 A.6.1.2 Objectives for responsible development of
  AI system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related video:**

- [Amazon
  Bedrock Guardrails: Implementing Custom Safeguards for
  Responsible AI Applications](https://aws.amazon.com/awstv/watch/02103dd95d3/ "https://aws.amazon.com/awstv/watch/02103dd95d3/")
- [AWS re:Inforce 2025 - Privacy-first generative AI: Establishing
  guardrails for compliance (COM224)](https://www.youtube.com/watch?v=GAjWNoxgkYY "https://www.youtube.com/watch?v=GAjWNoxgkYY")

**Related tools:**

- [Amazon
  Bedrock Guardrails and PII removal](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md")
