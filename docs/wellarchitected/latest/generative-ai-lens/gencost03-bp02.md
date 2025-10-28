# GENCOST03-BP02 Control model response length

The costs of a foundation model are often measured in the lengths of
the model's responses. This best practice describes how to control
model responses to reduce costs.

**Desired outcome:** When
implemented, this best practices encourages model responses to be as
short as possible without sacrificing usability.

**Benefits of establishing this best
practice:**
[Adopt
a consumption model](../framework/cost-dp.md "../framework/cost-dp.md") - Foundation models on a consumption
based pricing model charge by the token. Reducing model response
length has the effect of reducing the cost of inference.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Model response length should be kept as concise as possible, so
long as it satisfies the use case. In Amazon Bedrock, consider
specifying a response length hyperparameter to control and predict
the upper-limit of the response length. Additionally, you may
consider adding a phrase to your prompts which encourages the
model to be succinct, further reducing the length of the model's
response while encouraging the model to maintain a high degree of
performance. Small optimizations in token count for model
responses can improve model's generated output cost.

### Implementation steps

1. Understand how the model response is to be used, defined a
   minimalist response scheme (for example, 0 for affirmative
   and 1 for rejection).
2. Inform the model in the prompt of the requested model
   response scheme, and ask the model to respond in kind.
3. Set a hard limit on the response length by configuring the
   response length hyperparameter accordingly.
4. Continue testing and optimizing the model's response to
   verify it satisfies the workload requirements.

## Resources

**Related practices:**

- [COST10-BP01](../cost-optimization-pillar/cost_evaluate_new_services_review_process.md "../cost-optimization-pillar/cost_evaluate_new_services_review_process.md")

**Related guides, videos, and documentation:**

- [AWS re:Invent 2023

* Prompt Engineering Best Practices for LLMs on Amazon Bedrock
  (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY "https://www.youtube.com/watch?v=jlqgGkh1wzY")

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/")
