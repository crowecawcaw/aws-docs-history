# RAIRC02-BP02 Consider strength and limitation trade-offs when

choosing metrics

Before selecting a metric to measure a release criterion, assess its
strengths and weaknesses. Validate model-derived metrics (such as
LLM-as-a-judge or -jury) through correlation with human assessors,
and document limitations that affect reproducibility (for example,
random seed or model version used in LLM-as-a-judge). Evaluate
metrics derived from human assessors and annotators for unwanted
bias, assessor variance, and consistency. Consider trade-offs
between automated metrics, which are generally consistent but may
miss context, compared to human evaluation, which may be more
nuanced but subjective and harder to scale.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Track what each potential metric does well and what it might
   miss before you choose it. For example, automated accuracy
   scores are consistent and fast, but might not catch responses
   that are technically correct but unhelpful to users.
   Understanding these trade-offs upfront assists you to pick the
   right combination of metrics.
2. Test LLM-based or model-derived metrics against human
   evaluators to see how well they agree. Run a set of examples
   through both your LLM judge and human reviewers, then
   calculate correlation scores to see if the LLM is measuring
   what you think it is. This validation catches cases where LLMs
   might have different responses than humans.
3. Check your human evaluators for bias and consistency by having
   multiple people evaluate the same examples and comparing their
   scores. Look for patterns where certain evaluators
   consistently rate things higher or lower or where people
   disagree a lot on similar examples. This assists you to spot
   when human judgment might be unreliable or a task is too
   subjective.
4. Balance the trade-offs between automated metrics that are
   consistent but might miss nuance and human evaluation that may
   be more representative of your users but increases costs and
   time. Use automated metrics for things you can measure
   objectively and human evaluation when human feedback is vital.
5. Document your final metric choices and why you picked them,
   including what limitations you're accepting. This assists
   future team members understand your reasoning and alerts them
   to potential blind spots in your measurements.

## Resources

**Related documents:**

- [Evaluate
  the performance of Amazon Bedrock Resources](../../../bedrock/latest/userguide/evaluation.md "../../../bedrock/latest/userguide/evaluation.md")
- [Review
  metrics for an automated model evaluation job in Amazon
  Bedrock (console)](../../../bedrock/latest/userguide/model-evaluation-report-programmatic.md "../../../bedrock/latest/userguide/model-evaluation-report-programmatic.md")
- [Create
  a model evaluation job with Amazon Bedrock](../../../sagemaker-unified-studio/latest/userguide/model-evaluation-jobs-management-create.md "../../../sagemaker-unified-studio/latest/userguide/model-evaluation-jobs-management-create.md")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation
