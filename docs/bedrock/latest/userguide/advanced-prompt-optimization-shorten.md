

# Shorten prompts
<a name="advanced-prompt-optimization-shorten"></a>

By default, Advanced Prompt Optimization optimizes your prompt for quality only. There is no constraint on prompt length. An optimized prompt can be longer than the original. A longer prompt increases input token costs and can increase time to first token (TTFT). If you are cost-sensitive or latency-constrained, you can enable prompt shortening. When enabled, the optimizer looks for a prompt that is shorter than your original and scores at least as high on your evaluation.

## How prompt shortening works
<a name="advanced-prompt-optimization-shorten-how"></a>

When you enable the `shortenPrompt` field, the optimizer prefers concise phrasing during the rewriting loop. Shortening is gradual. In each iteration, the optimizer targets a prompt slightly shorter than its current best candidate, so prompt length decreases step by step across iterations rather than in one large cut. The shortened prompt may not preserve the structure and level of detail of your original prompt.

Prompt shortening does not change how evaluation works. Your evaluation samples and evaluation method still steer the optimization. Shortening adds a second requirement: to be returned, the optimized prompt must be shorter than the original and score at least as high on your evaluation. If it does not meet both requirements, the original prompt is returned. The result is therefore not always shorter than your original prompt. For details, see [Return logic](#advanced-prompt-optimization-shorten-return-logic).

Prompt shortening reduces the length of your prompt template, not the length of the responses your model produces. If you use the default evaluation, its Expression Quality criterion separately rewards concise model responses. For more information, see [Define evaluation methods](advanced-prompt-optimization-evaluation.md).

Prompt shortening works with every evaluation method: the system default, steering criteria, custom LLM-as-a-judge, and custom Lambda evaluator. Enabling shortening does not change what your evaluator receives. Custom LLM-as-a-judge prompts continue to receive the fully rendered prompt through the `{{prompt}}` placeholder. Custom Lambda evaluators continue to receive only the predictions and ground truths; the Lambda function does not receive the prompt itself. Shortening does not depend on your evaluator seeing the prompt, because length is measured inside the optimizer.

If your prompt template uses selective optimization tags, shortening applies only to the sections the optimizer is allowed to rewrite. Any content the optimizer cannot rewrite is preserved as written, including everything inside `<advpo:exclude>` tags. For more information, see [Selective optimization](advanced-prompt-optimization-selective.md).

## Enable prompt shortening
<a name="advanced-prompt-optimization-shorten-enable"></a>

Prompt shortening is off by default. You enable it per prompt template by adding the `optimizationConfig` object to that template's line in your input JSONL file. This follows the same pattern as evaluation configuration: the setting lives in the input file, not in the `CreateAdvancedPromptOptimizationJob` request.

`shortenPrompt` is a boolean. Omitting `optimizationConfig`, or setting `shortenPrompt` to `false`, leaves shortening off. When shortening is off, Advanced Prompt Optimization optimizes for evaluation score only, with no length constraint.

Because the setting is per template, you can enable shortening for some templates in a job and leave it off for others.

### Input file format
<a name="advanced-prompt-optimization-shorten-input-format"></a>

The following example shows a single line of an input JSONL file with prompt shortening enabled:

```
{
  "version": "bedrock-2026-05-14",
  "templateId": "customer-support-v1",
  "promptTemplate": "You are a customer support agent.\n\nProduct info:\n{{productInfo}}\n\nQuestion:\n{{customerQuestion}}\n\nProvide a helpful response.",
  "optimizationConfig": {
    "shortenPrompt": true
  },
  "steeringCriteria": ["PROFESSIONAL"],
  "evaluationSamples": [
    {
      "inputVariables": [
        {"productInfo": "Product: Sony WH-1000XM5. Battery: 30 hours."},
        {"customerQuestion": "How long does the battery last?"}
      ],
      "referenceResponse": "The battery lasts up to 30 hours on a single charge."
    }
  ]
}
```


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| optimizationConfig | object | No | Container for optimization settings. | 
| optimizationConfig.shortenPrompt | boolean | No | Enables prompt shortening for this template. Omitting the field or setting it to false leaves shortening off. | 

For the full input file schema, see [Prepare your input dataset](advanced-prompt-optimization-input.md).

### Console
<a name="advanced-prompt-optimization-shorten-console"></a>

The console does not have a separate control for prompt shortening. You enable it in the input JSONL file, in the same way you specify your evaluation method.

Before you upload your input file, add `optimizationConfig` with `"shortenPrompt": true` to each template you want shortened. To review the schema, choose **View required input file format** on the **Create prompt optimization** page. For the full job creation procedure, see [Create and manage optimization jobs](advanced-prompt-optimization-jobs.md).

**Note**  
There may be a trade-off between shorter prompts and improvement on your evaluation scores. This may take some iteration if you enable prompt shortening. If the optimized prompt is not both shorter and at least as high scoring as the original, the original prompt is returned as the result.

### API and SDKs
<a name="advanced-prompt-optimization-shorten-api"></a>

The API request does not change when you enable prompt shortening. Continue to call `CreateAdvancedPromptOptimizationJob` with `jobName`, `modelConfigurations`, `inputConfig`, and `outputConfig`. The optimizer reads `optimizationConfig` from each line of the input file at `inputConfig.s3Uri`.

The following Python example creates a job whose input file enables prompt shortening. Note that the shortening setting appears in the file written to Amazon S3, not in the API call:

```
import boto3
import json

s3 = boto3.client('s3', region_name='us-west-2')
bedrock = boto3.client('bedrock', region_name='us-west-2')

# The shortening setting lives here, in the input file.
record = {
    'version': 'bedrock-2026-05-14',
    'templateId': 'customer-support-v1',
    'promptTemplate': 'You are a customer support agent.\n\nQuestion:\n{{customerQuestion}}\n\nProvide a helpful response.',
    'optimizationConfig': {'shortenPrompt': True},
    'steeringCriteria': ['PROFESSIONAL'],
    'evaluationSamples': [
        {
            'inputVariables': [{'customerQuestion': 'How long does the battery last?'}],
            'referenceResponse': 'The battery lasts up to 30 hours on a single charge.'
        }
    ]
}

s3.put_object(
    Bucket='my-bucket',
    Key='input/dataset.jsonl',
    Body=json.dumps(record) + '\n'
)

# The API call is unchanged.
response = bedrock.create_advanced_prompt_optimization_job(
    jobName='my-optimization-job',
    modelConfigurations=[
        {'modelId': 'us.anthropic.claude-sonnet-4-6'}
    ],
    inputConfig={'s3Uri': 's3://my-bucket/input/dataset.jsonl'},
    outputConfig={'s3Uri': 's3://my-bucket/output/'}
)
```

The equivalent AWS CLI command is also unchanged:

```
aws bedrock create-advanced-prompt-optimization-job \
    --job-name "my-optimization-job" \
    --model-configurations '[{"modelId": "us.anthropic.claude-sonnet-4-6"}]' \
    --input-config '{"s3Uri": "s3://my-bucket/input/dataset.jsonl"}' \
    --output-config '{"s3Uri": "s3://my-bucket/output/"}' \
    --region us-west-2
```

## Return logic
<a name="advanced-prompt-optimization-shorten-return-logic"></a>

When prompt shortening is enabled, the optimized prompt is returned only if it meets both of the following conditions:

1. It is shorter than the original prompt.

1. It scores at least as high as the original prompt on your evaluation.

If the optimized prompt fails either condition, the original prompt is returned instead and `compressionRatio` is 1.0.

This return logic guarantees that enabling `shortenPrompt` never returns a prompt that is longer than your original, and never trades evaluation quality for brevity.

## Compression ratio in results
<a name="advanced-prompt-optimization-shorten-compression-ratio"></a>

When prompt shortening is enabled, each per-model entry in `promptOptimizationResults` includes three additional fields: `compressionRatio`, `originalTokenCount`, and `optimizedTokenCount`. The following example is abbreviated; for the complete output schema, see [View and interpret results](advanced-prompt-optimization-results.md).

```
{
  "promptTemplateId": "customer-support-v1",
  "promptTemplate": "...",
  "promptOptimizationResults": [
    {
      "modelId": "us.anthropic.claude-sonnet-4-6",
      "status": "SUCCESS",
      "originalPromptMetrics": { "averageInputTokens": 1680, "averageScore": 2.1, "...": "..." },
      "optimizedPromptTemplateId": "customer-support-v1-optimized-for-us.anthropic.claude-sonnet-4-6",
      "optimizedPromptTemplate": "...",
      "optimizedPromptMetrics": { "averageInputTokens": 1274, "averageScore": 2.6, "...": "..." },
      "compressionRatio": 0.72,
      "originalTokenCount": 1450,
      "optimizedTokenCount": 1044,
      "dataset": [ "..." ]
    }
  ]
}
```

These three fields are present only when prompt shortening is enabled for the template.

The compression ratio is defined as:

`compressionRatio = optimizedTokenCount / originalTokenCount`
+ A ratio of 1.0 means the original prompt was returned, because the optimized prompt was not both shorter and at least as high scoring.
+ A ratio below 1.0 means the prompt was shortened. For example, 0.72 means the optimized prompt uses 28% fewer tokens.
+ A ratio above 1.0 cannot occur when `shortenPrompt` is enabled. If the optimizer produces a longer prompt, the original is returned instead.

Token counts are measured on the prompt template, not on the rendered prompts with variable values substituted. The count covers the whole template. If your template uses selective optimization tags, the `<advpo:optimize>` and `<advpo:exclude>` tag markers themselves are excluded from the count, matching the tag stripping that already happens in the returned prompt. The compression ratio therefore reflects the whole prompt you receive, not just the sections the optimizer was allowed to rewrite.

On the console results page, the Summary tables tab shows the compression ratio and the original and optimized template token counts for each model. The Graphs tab shows the token counts in the Prompt template length chart.

## Limitations
<a name="advanced-prompt-optimization-shorten-limitations"></a>
+ **No exact token budget.** You cannot target a specific length, such as "optimize to exactly 500 tokens." Shortening is on or off per template.
+ **No per-section compression control.** When your template has multiple `<advpo:optimize>` sections, all of them are eligible for shortening. You cannot enable shortening for one optimized section while leaving another at its original length. The compression ratio is reported for the whole template, not per section.
+ **Short prompts may not compress.** A prompt that is already concise may produce a compression ratio of 1.0 because the optimized prompt is not both shorter and at least as high scoring.

## Best practices
<a name="advanced-prompt-optimization-shorten-best-practices"></a>
+ **Expect iteration.** There can be a trade-off between prompt brevity and evaluation score improvement. If the job returns your original prompt, meaning a compression ratio of 1.0, consider refining your evaluation method or dataset and running the job again.
+ **Validate on held-out data.** As with any optimization run, test the shortened prompt on data the optimizer has not seen to confirm quality gains hold.
+ **Protect content that must not change.** If sections of your prompt must remain verbatim, such as safety constraints or legal language, leave them outside your `<advpo:optimize>` tags, or use `<advpo:exclude>` tags if you are not using `<advpo:optimize>` at all. Every `<advpo:optimize>` section is eligible for shortening.