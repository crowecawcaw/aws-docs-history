# RAIBR02-BP04 Identify potential harmful events impacting

privacy

Harmful events can result from using data that is confidential or
personal in ways that do not align with the rules for correctly
handling such data.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Review the types of data that you expect to appear in
   development and operations (including user inputs and system
   outputs), and categorize the data as confidential, personal or
   other, as advised by your legal counsel. Consider harmful
   events resulting from errors in handling this data. For
   example, could data that is licensed only for training be
   accidentally output to a user?
2. Consider what types of data might unexpectedly appear in
   training or operations, whether the unexpected data could be
   confidential or personal, and what harms might result if this
   data was not blocked from flowing into development or
   operational pipelines.

## Resources

**Related documents:**

- [Differentially
  Private Fair Learning](https://arxiv.org/abs/1812.02696 "https://arxiv.org/abs/1812.02696")
- [Remove
  PII from conversations by using sensitive information
  filters](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.5.4 Assessing AI system impact on
  individuals or groups of individuals
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.3 Acquisition of data

**Related video:**

- [Amazon
  Bedrock Guardrails: Implementing Custom Safeguards for
  Responsible AI Applications](https://aws.amazon.com/awstv/watch/02103dd95d3/ "https://aws.amazon.com/awstv/watch/02103dd95d3/")
- [AWS re:Inforce 2025 - Privacy-first generative AI: Establishing
  guardrails for compliance (COM224)](https://www.youtube.com/watch?v=GAjWNoxgkYY "https://www.youtube.com/watch?v=GAjWNoxgkYY")
