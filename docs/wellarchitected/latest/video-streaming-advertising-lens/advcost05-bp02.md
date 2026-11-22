

# ADVCOST05-BP02 Select the right foundation model for each advertising agent's task complexity

 Not every advertising agent requires the most capable and expensive foundation model. Matching model capability to task complexity is a high impact cost optimization for agentic AI advertising workloads. Basic classification tasks such as brand safety detection and ad format matching can run on lightweight models at a fraction of the cost of flagship models. 

 **Desired outcome:** 
+  Each advertising agent uses the least expensive foundation model that meets its quality threshold, validated through benchmarking. 
+  Basic tasks run on lightweight models, complex multi-step reasoning tasks use more capable models, and high-volume repetitive tasks use distilled models. 

 **Common anti-patterns:** 
+  Assigning the same high-capability model to all agents regardless of task complexity. 
+  Selecting models based on general reputation rather than benchmarking against your specific advertising tasks and quality requirements. 
+  Never re-evaluating model assignments after initial deployment. 

 **Benefits of establishing this best practice:** 
+  Large reduction in per-agent inference costs by avoiding overpowered model assignments for basic tasks. 
+  Maintained output quality where it matters: complex agents retain capable models while basic agents use proportionally cheaper alternatives. 
+  Distilled models deliver faster response times alongside lower costs for high-volume tasks. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Foundation model pricing scales with capability. Flagship models such as Claude Sonnet and Amazon Nova Pro cost 5 to 20 times more per token than lightweight alternatives such as Claude Haiku and Amazon Nova Lite. In multi-agent advertising systems where dozens of agents run continuously, the cumulative cost difference between appropriate and overpowered model assignments can exceed 70% of total inference spend. For each task, assign the least expensive model that meets the quality threshold. 

 Task complexity varies widely across advertising agents. Brand safety classification requires pattern matching against known categories, a task where lightweight models perform within 1 to 2 percentage points of flagship models. Media planning with multi-channel budget allocation involves multi-step reasoning, constraint satisfaction, and creative synthesis, tasks where model capability directly affects output quality. 

 Benchmarking requires a representative dataset of actual advertising prompts with human-evaluated expected outputs. Running candidates against this dataset produces a quality score and a cost per invocation for each model. Use metrics to compare models directly. 

 Use [Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) to compare models. [Intelligent Prompt Routing](https://docs.aws.amazon.com/bedrock/latest/userguide/intelligent-prompt-routing.html) applies when a single agent processes queries of varying complexity within one workflow. Routing directs each query to the appropriate model based on estimated complexity. Routing adds latency to each call, so it benefits agents with high invocation volume and wide complexity variance more than agents with uniform task difficulty. 

 [Amazon Bedrock Model Distillation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-distillation.html) applies when a task is both high-volume and repetitive. Distillation transfers the behavior of a larger model into a smaller, cheaper one using task-specific training data. The resulting model retains accuracy on that narrow task at a fraction of the inference cost. If the task definition drifts or expands, the distilled model loses accuracy without any obvious signal. Monitor accuracy continuously and re-distill when performance drops below threshold. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify each advertising agent by task complexity:** Create a complexity matrix: low (brand safety classification, ad format detection, audience segment matching), medium (inventory scoring, bid adjustment recommendations), high (multi-channel media planning, creative strategy generation). Document the quality threshold required for each based on business impact. 

1.  **Benchmark at least three candidate models per agent:** Run your representative advertising task dataset through each candidate model using Amazon Bedrock model evaluation. Record output quality scores alongside cost-per-invocation. Compare lightweight models (Amazon Nova Lite and Claude Haiku) against more capable options (Amazon Nova Pro and Claude Sonnet) for each task type. 

1.  **Assign the least expensive model meeting quality threshold:** For brand safety classifiers and audience segment matchers, assign lightweight models. For media planning agents generating multi-channel strategies, use more capable models. Document the model assignments and quality scores in a decision record. 

1.  **Configure Bedrock Intelligent Prompt Routing for variable-complexity agents:** For agents that handle queries of varying complexity, configure Intelligent Prompt Routing to automatically direct simpler queries to smaller models and complex queries to more capable models within the same model family. 

1.  **Use Model Distillation for high-volume repetitive tasks:** For tasks running at advertising scale (thousands of ad format classifications per minute), use Amazon Bedrock Model Distillation to create smaller, task-specific models. AWS reports less than 2% accuracy loss for use cases like RAG, at much lower cost and latency. Validate accuracy on your specific classification task before cutover. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST05-BP03 Implement prompt caching and optimize prompt design to minimize token consumption](advcost05-bp03.md) 

 **Related documents:** 
+  [Reduce costs and latency with Amazon Bedrock Intelligent Prompt Routing and prompt caching](https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/) 
+  [Amazon Bedrock Cost Optimization](https://aws.amazon.com/bedrock/cost-optimization/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 