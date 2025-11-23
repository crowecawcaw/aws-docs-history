# GENCOST03-BP04 Annotate user input to enable cost-aware content filtering

Annotate specific sections of input prompts to selectively apply
content filtering and reduce token usage costs. By using input
tags to mark only the user-provided content for filtering, you
can avoid unnecessary processing of system prompts, search
results, and conversation history while maintaining essential
safeguards.

**Desired outcome:** Enable more
efficient and cost-effective content filtering by processing
only the relevant portions of input that require guardrails
evaluation.

**Benefits of establishing this best
practice:**

- [Control
  resource consumption parameters](../framework/cost-dp.md "../framework/cost-dp.md") - By filtering only
  selected content rather than entire prompts, you minimize the
  number of tokens processed by content filters.
- [Optimize
  model and inference selection](../framework/cost-dp.md "../framework/cost-dp.md") - Selective filtering
  reduces the volume of text evaluated, leading to faster response
  times.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

By implementing selective content filtering through input
tags, you can significantly reduce token costs while
preserving the effectiveness of your content safeguards.
Please note that the input tags are not supported when using
ApplyGuardrail API, so you need to
implement content filtering on your application side to derive
the benefits of input tags.

- Review your application architecture to identify where
  content filtering is needed.
- Determine which content sections require filtering or
  trusted content.
- Implement input tagging following the Amazon Bedrock
  documentation.
- Test filtering effectiveness and performance impact.
- Monitor costs and adjust tag usage to optimize spend while
  maintaining safety.

### Implementation steps

1. Use XML-style tags to mark specific sections of input
   prompts for content filtering. Add tags using the
   format:

```
<amazon-bedrock-guardrails-guardContent_xyz>
[Content to be filtered]
</amazon-bedrock-guardrails-guardContent_xyz>
```

Generate a unique random tag suffix (xyz)
for each request to reduce prompt injection attacks. Use
alphanumeric characters between 1-20 characters.

Include the tag suffix in the
guardrailConfig:

```
{
    "amazon-bedrock-guardrailConfig": {
        "tagSuffix": "xyz"
    }
}
```

1. Apply tags selectively to user queries and input,
   current conversation turns, and new or unverified
   content.
2. Leave system prompts, verified search result, historical
   conversation context, and other trusted content
   untagged.
3. Define a minimalist response scheme (for example,
   0 for affirmative and
   1 for rejection).
4. Inform the model in the prompt of the requested model
   response scheme, and ask the model to respond in kind.
5. Set a hard limit on the response length by configuring
   the response length hyperparameter accordingly.
6. Continue testing and optimizing the model's response to
   verify it satisfies the workload requirements. Monitor
   and optimize your implementation by:
   - Tracking token usage with and without selective
     filtering
   - Measuring latency impact across different tag
     configurations
   - Verifying filtering effectiveness on tagged vs
     untagged content
   - Adjusting tag placement based on application needs

**Example implementation**

The following use cases are well-suited for input tagging:

- **RAG applications:**
  Tag only user queries while leaving retrieved passages
  unfiltered .
- **Chat applications:**
  Tag new user messages while preserving conversation
  history.
- **Content moderation:**
  Tag user-generated content while allowing verified
  content to pass through.
- **Document
  processing:** Tag extracted text portions
  needing review while trusting source material.

## Resources

**Related best practices:**

- [COST10-BP01](../cost-optimization-pillar/cost_evaluate_new_services_review_process.md "../cost-optimization-pillar/cost_evaluate_new_services_review_process.md")

**Related videos:**

- [AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on
  Amazon Bedrock (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY "https://www.youtube.com/watch?v=jlqgGkh1wzY")

**Related examples:**

- [Amazon
  Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/")
