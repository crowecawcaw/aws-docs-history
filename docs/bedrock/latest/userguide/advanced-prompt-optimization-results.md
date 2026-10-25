

# View and interpret results
<a name="advanced-prompt-optimization-results"></a>

## Output location
<a name="advanced-prompt-optimization-results-location"></a>

After a job completes, results are written to your output S3 path:

`{{output-s3-uri}}/{{job-id}}/advanced_prompt_optimization_results.jsonl`

The job ID is the last segment of the job ARN.

## Console results page
<a name="advanced-prompt-optimization-results-console"></a>

**Warning**  
If you move the results files away from the output S3 location after the job is complete, the console results page will not render.

To see estimated cost per request for the original and optimized prompts, choose **Configure pricing** and enter per-token input and output prices for each model. Cost is calculated in the console from the prices you enter and is not included in the output file.

## Output format
<a name="advanced-prompt-optimization-results-format"></a>

The output file is JSONL with per-template results. Each line contains:
+ `promptTemplateId`: correlates to your input templateId
+ `promptOptimizationResults`: array with one entry per target model, each containing:
  + `modelId`: the target model
  + `status`: optimization status for this model. The value is `SUCCESS` or `FAILED`. This is separate from the job-level `jobStatus` returned by `GetAdvancedPromptOptimizationJob`.
  + `optimizedPromptTemplate`: the rewritten prompt template
  + Evaluation scores per sample
  + Latency: average and median time to first token (`averageTtftInSec`, `medianTtftInSec`) and average and median end-to-end latency (`averageLatencyInSec`, `medianLatencyInSec`), in seconds, in `originalPromptMetrics` and `optimizedPromptMetrics`. Per-sample values (`ttftInSec`, `latencyInSec`) are in each `dataset[]` entry under `originalPromptDetails.originalPromptMetrics` and `optimizedPromptDetails.optimizedPromptMetrics`.
  + `compressionRatio`, `originalTokenCount`, and `optimizedTokenCount`, present only when prompt shortening is enabled for the template

**Note**  
Median time to first token, average latency, and median latency are available for jobs created on or after August 4, 2026. They are not computed for earlier jobs. The console results page shows average and median values in the Summary tables tab, average values in the Graphs tab, and per-sample values in the Detailed results tab.

## Reading results programmatically
<a name="advanced-prompt-optimization-results-code"></a>

```
import boto3
import json

s3 = boto3.client('s3', region_name='us-west-2')

# Job ID is the last segment of the job ARN
job_id = job_arn.split('/')[-1]
output_key = f'output/{job_id}/advanced_prompt_optimization_results.jsonl'

response = s3.get_object(Bucket='my-bucket', Key=output_key)
content = response['Body'].read().decode('utf-8')

for line in content.strip().split('\n'):
    result = json.loads(line)
    print(f"Template: {result['promptTemplateId']}")
    for opt in result.get('promptOptimizationResults', []):
        print(f"  Model: {opt['modelId']}")
        print(f"  Status: {opt['status']}")
        print(f"  Optimized: {opt['optimizedPromptTemplate'][:100]}...")
```

## Interpreting scores
<a name="advanced-prompt-optimization-results-scores"></a>

Scores are normalized; higher is better. The service normalizes all evaluation scores regardless of the original grading scale you defined in your evaluation method.

You can always see the raw LLM-as-a-judge output in your S3 bucket and on the console results page in the detailed results tab. Due to the nature of merging custom LLMJ prompts with the service-provided default prompt, the numerical score may not exactly match the discrete steps in your custom LLMJ rubric. If you want binary evaluation results or exact matching, it may be better to use a Lambda evaluator.

## Interpreting the compression ratio
<a name="advanced-prompt-optimization-results-compression-ratio"></a>

The compression ratio appears in results only when prompt shortening was enabled for the template. Evaluation scores are normalized so that a higher number is better. The compression ratio works the other way: a lower number means a shorter prompt.
+ A ratio below 1.0 means the returned prompt is shorter than the original. For example, 0.72 means the optimized prompt uses 28% fewer tokens.
+ A ratio of 1.0 means the original prompt was returned, because the optimized prompt was not both shorter than the original and at least as high scoring on your evaluation.
+ A ratio above 1.0 does not occur when prompt shortening is enabled.

On the console results page, the Summary tables tab shows the compression ratio and the original and optimized template token counts for each model. The Graphs tab shows the token counts in the Prompt template length chart.