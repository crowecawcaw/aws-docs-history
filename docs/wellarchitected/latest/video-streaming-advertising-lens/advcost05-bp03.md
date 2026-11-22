

# ADVCOST05-BP03 Implement prompt caching and optimize prompt design to minimize token consumption

 Advertising agents frequently process similar campaign briefs, audience data schemas, and inventory structures. You reduce token consumption and inference costs by caching common context blocks and designing concise prompts. Prompt caching can reduce costs for cached tokens by up to 90% compared to standard input token pricing. 

 **Desired outcome:** 
+  Common context blocks (campaign taxonomies, channel definitions, brand safety rule sets) are marked as cacheable prefix segments and reused at up to 90% reduced token cost. 
+  Prompts are concise and well-structured, with unnecessary context stripped from agent inputs. 
+  Application-level result caching using ElastiCache or DynamoDB avoids inference costs for repeated identical queries. 

 **Common anti-patterns:** 
+  Sending full campaign taxonomies, channel definitions, and audience schemas in every agent invocation without using prompt caching, so full input token costs land on identical context repeatedly. 
+  Writing verbose, unstructured prompts that include unnecessary context, instructions, or examples that inflate input token counts without improving output quality. 
+  Allowing unbounded model responses when the agent produces structured outputs (JSON plans, classification labels), which generates excessive output tokens that add cost without value. 
+  Invoking the foundation model for identical queries that have been answered recently, when an application-level cache could return the same result at near-zero cost. 
+  Never iterating on prompt formulations after initial deployment. 

 **Benefits of establishing this best practice:** 
+  Amazon Bedrock prompt caching reduces costs for cached tokens by up to 90% compared to standard input token pricing for repeated context blocks. 
+  Concise prompts and constrained responses reduce both input and output token costs per invocation. 
+  Application-level result caching avoids inference costs entirely for repeated identical queries. 
+  Faster response times from cached prompts and pre-computed results improve agent orchestration latency. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising agents pay for context tokens (the prompt input) and generation tokens (the model output). Context tokens cost the most in advertising workflows because agents send the same structural information with every invocation, such as campaign taxonomies and audience schemas. If 80% of a prompt is identical across invocations, teams pay the full input token pricing for information the model has already processed. [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) addresses this by storing common prefix segments and charging up to 90% less for cached tokens on subsequent requests. 

 The cacheable portion must appear as a contiguous prefix. Variable, per-request content must follow after the cached block. Restructure prompts so that stable context (taxonomy definitions, rule sets, system instructions) appears first, and request-specific content (the individual campaign brief, the specific ad slot to evaluate) appears last. Prompts that interleave static and dynamic content can't use caching. A minimum token threshold applies per cached segment (model-dependent, typically 1,024 tokens for Claude models), so short prompts gain nothing from caching. 

 You can also cut the verbosity in the prompts themselves. Advertising agents often inherit verbose prompt templates from development that include excessive examples, redundant instructions, or explanatory context the model doesn't need. Aggressive compression can degrade output quality by removing needed context. [Amazon Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) supports versioned prompt libraries with A/B testing, so teams can measure whether a shorter prompt produces equivalent outputs before committing to the change. 

 Output tokens also accumulate cost, particularly when agents produce structured outputs (JSON campaign plans, classification labels) but the model generates verbose explanations or formatting around the structured data. Set maxTokens to the expected output length for each agent task to bound responses without truncating valid outputs. 

 Application-level result caching operates at a different layer than prompt caching. When the same query recurs within a time window (identical campaign taxonomy lookups, repeated brand safety checks for the same creative), a cache hit from [Amazon ElastiCache](https://aws.amazon.com/elasticache/) or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with TTL returns the previous result at near-zero cost. The main risk is stale results. If the underlying data changes faster than the TTL, cached responses become inaccurate. TTL must match the data source's actual change frequency. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify cacheable context blocks:** Analyze agent invocation logs to find common context elements repeated across invocations: campaign taxonomy definitions, standard audience schemas, channel definitions, brand safety rule sets. These are candidates for prompt caching prefix segments. 

1.  **Enable Bedrock prompt caching and mark cacheable segments:** Structure prompts with stable context as the prefix (cacheable) and variable per-request content as the suffix. Enable prompt caching for supported models. Verify that cached segments meet minimum token requirements (Claude 3.7 Sonnet requires at least 1,024 tokens per checkpoint). Monitor cache hit and miss rates through Bedrock metrics. 

1.  **Create a prompt library with optimized formulations:** Use Amazon Bedrock Prompt Management to version and A/B test prompt formulations. Find the most token-efficient prompts that maintain output quality. Strip unnecessary context from agent inputs. Set maxTokens limits on responses to limit verbose outputs that don't add value. 

1.  **Implement application-level caching for repeated queries:** For advertising workflows where the same query recurs (campaign taxonomy lookup, brand safety rule retrieval), implement cache-aside using ElastiCache with TTL aligned to the data source's update frequency. Check the cache before invoking Bedrock. Cached results cost orders of magnitude less than inference. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST05-BP02 Select the right foundation model for each advertising agent's task complexity](advcost05-bp02.md) 

 **Related documents:** 
+  [Effectively use prompt caching on Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) 
+  [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 