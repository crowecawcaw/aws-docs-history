# GENCOST03-BP01 Reduce prompt token length

Long prompts tend to be filled with lots of context, additional
information, and requests for a foundation model when it is
conducting inference. Reducing prompt length lowers the amount of
compute needed to serve inference.

**Desired outcome:** When
implemented, this best practices encourages prompts to be as short
as possible while meeting performance requirements.

**Benefits of establishing this best
practice:**
[Adopt
a consumption model](../framework/cost-dp.md "../framework/cost-dp.md") - Foundation models on a consumption
based pricing model charge by the token. Reducing prompt length has
the effect of reducing the cost of processing the prompt.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Whether your foundation model charges by tokens processed or not,
prompt length can directly or indirectly contribute to the cost of
inference. For self-hosted model infrastructure or provisioned
throughput, longer prompts require increased computation time and
increase the scale of infrastructure required to host your
workload. For managed model infrastructure, the increased token
count of longer prompts results in higher per-inference costs.
Consider shortening prompts through rigorous testing. You may even
use a separate large language model to shorten a prompt without
reduction in performance. Reducing even a few tokens off the
prompt contributes to cost optimization in the long-run.

### Implementation steps

1. Select a prompt to reduce.
2. Engineer the prompt to reduce as many unnecessary words as
   possible.
3. Consider using a separate LLM to offer a shortened prompt
   that satisfies the end goal.
4. Continue testing and optimizing the prompt to validate it
   meets the workload requirements.
   - Experiment with zero-shot prompting techniques for
     common knowledge tasks.
   - Consider chain-of-thought or tree-of-thought for logical
     reasoning.
   - Evaluate the benefits of least-to-most prompting for
     complex problems with nuanced solutions.
   - Research prompt engineering techniques to find the most
     cost-effective approach to your problem.

## Resources

**Related practices:**

- [COST10-BP01](../cost-optimization-pillar/cost_evaluate_new_services_review_process.md "../cost-optimization-pillar/cost_evaluate_new_services_review_process.md")

**Related guides, videos, and documentation:**

- [AWS re:Invent 2023

* Prompt Engineering Best Practices for LLMs on Amazon Bedrock
  (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY "https://www.youtube.com/watch?v=jlqgGkh1wzY")

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/")
- [Prompt
  Engineering Guide](https://www.promptingguide.ai/ "https://www.promptingguide.ai/")
