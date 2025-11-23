# RAIBR02-BP01 Identify potential harmful events impacting

fairness

Examine how the proposed AI system might affect different
stakeholder groups and subgroups throughout the entire system
lifecycle. A fairness assessment may consider harms to individuals
(for example, wrongful denials) and to groups (for example,
performance variations across demographic groups).

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Consider how different demographic groups are represented in
   the inputs (for example, by geography).
2. Consider whether some inputs could unintentionally represent
   or misrepresent different demographic groups (for example,
   proxy a demographic attribute).
3. Consider whether training data might inappropriately represent
   the expected users and whether a wider variety of inputs could
   impact performance. For example, a facial recognition system
   trained primarily on certain skin tones might not perform as
   well on other skin tones.
4. Assess potential impacts at the levels of individuals, groups,
   and society. For example, a job candidate screening tool might
   impact individual candidates, demographic group success rates,
   and overall workforce representation.

## Resources

**Related documents:**

- [Preventing
  Fairness Gerrymandering: Auditing and Learning for Subgroup
  Fairness](https://arxiv.org/abs/1711.05144 "https://arxiv.org/abs/1711.05144")
- [Equality
  Of Odds](https://mlu-explain.github.io/equality-of-odds/ "https://mlu-explain.github.io/equality-of-odds/")
- [Fairness,
  model explainability and bias detection with SageMaker AI
  Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.5.4 Assessing AI system impact on
  individuals or groups of individuals
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
