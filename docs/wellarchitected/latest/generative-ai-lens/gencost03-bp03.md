# GENCOST03-BP03 Implement prompt caching to reduce token costs

Implement prompt caching for supported foundation models to
reduce inference response latency and input token costs. This
best practice helps organizations optimize costs by caching
frequently used portions of prompts to avoid recomputation,
while maintaining performance and reliability.

**Desired outcome:** Reduce
inference costs by caching commonly used prompt components and
using cached tokens at a reduced rate.

**Benefits of establishing this best
practice:**

- [Control
  resource consumption parameters](../framework/cost-dp.md "../framework/cost-dp.md") - Reduce token costs by
  reusing cached prompt components.
- [Optimize
  model and inference selection](../framework/cost-dp.md "../framework/cost-dp.md") - Decrease latency by
  avoiding recomputation of cached prompt sections.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Prompt caching is an optional feature available on supported
models in Amazon Bedrock that can reduce inference response
latency and input token costs. By caching portions of your
context, the model can use the cache to skip recomputation,
allowing Bedrock to achieve cost savings through lower token
rates.

Prompt caching can help when you have workloads with long and
repeated contexts that are frequently reused across multiple
queries. For example, if you have a chatbot where users can
upload documents and ask questions about them, caching the
document content avoids reprocessing it for each user query.

When using prompt caching, cached tokens are charged at a
reduced rate. Depending on the model, tokens written to cache
may be charged at a higher rate than uncached input tokens.
Tokens not read from or written to cache are charged at the
standard input token rate.

Cache checkpoints have model-specific minimum and maximum
token requirements. You can only create a checkpoint if your
prompt prefix meets the minimum token count. For example,
Claude 3.7 Sonnet requires at least 1,024 tokens per
checkpoint. The cache has a five minute TTL that resets with
each successful hit.

### Implementation steps

1. Identify opportunities for caching:
   - Review workload for repeated prompt components
   - Verify prompts meet minimum token requirements
   - Assess potential cost savings from reduced token
     rates

2. Enable prompt caching for supported models:
   - Turn on caching in Amazon Bedrock console
   - For APIs, set appropriate caching flags
   - Configure cache checkpoints at optimal locations

3. Monitor caching metrics:
   - Track cache hit and miss rates
   - Monitor token costs for cached compared to uncached
     content
   - Analyze latency improvements

4. Optimize cache usage:
   - Tune checkpoint placement
   - Adjust prompt structure to maximize cache hits
   - Balance cache write costs with read savings

## Resources

**Related best practices:**

- [COST10-BP01](../cost-optimization-pillar/cost_evaluate_new_services_review_process.md "../cost-optimization-pillar/cost_evaluate_new_services_review_process.md")

**Related documents:**

- [Effectively
  use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/")
- [Prompt
  caching for faster model inference](../../../bedrock/latest/userguide/prompt-caching.md "../../../bedrock/latest/userguide/prompt-caching.md")

**Related examples:**

- [Effectively
  use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/")
- [Supercharge
  your development with Claude Code and Amazon Bedrock prompt
  caching](https://aws.amazon.com/blogs/machine-learning/supercharge-your-development-with-claude-code-and-amazon-bedrock-prompt-caching/ "https://aws.amazon.com/blogs/machine-learning/supercharge-your-development-with-claude-code-and-amazon-bedrock-prompt-caching/")
- [Reduce
  costs and latency with Amazon Bedrock Intelligent Prompt
  Routing and prompt caching (preview)](https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/ "https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/")
- [Amazon
  Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/")
