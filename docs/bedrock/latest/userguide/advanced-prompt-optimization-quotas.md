

# Supported Regions, models, and quotas
<a name="advanced-prompt-optimization-quotas"></a>

## Supported Regions
<a name="advanced-prompt-optimization-quotas-regions"></a>

Advanced Prompt Optimization is available in the following AWS Regions:
+ US East (N. Virginia) (us-east-1)
+ US East (Ohio) (us-east-2)
+ US West (Oregon) (us-west-2)
+ Canada (Central) (ca-central-1)
+ South America (São Paulo) (sa-east-1)
+ Europe (Ireland) (eu-west-1)
+ Europe (London) (eu-west-2)
+ Europe (Frankfurt) (eu-central-1)
+ Europe (Zurich) (eu-central-2)
+ Asia Pacific (Mumbai) (ap-south-1)
+ Asia Pacific (Tokyo) (ap-northeast-1)
+ Asia Pacific (Seoul) (ap-northeast-2)
+ Asia Pacific (Singapore) (ap-southeast-1)
+ Asia Pacific (Sydney) (ap-southeast-2)

## Supported target models
<a name="advanced-prompt-optimization-quotas-models"></a>

Advanced Prompt Optimization supports Amazon Bedrock models that output text modality as optimization targets. New text-output models are added as optimization targets as they become available. There can be a short delay between a model's launch on Amazon Bedrock and its availability in Advanced Prompt Optimization. The model must also be available in the Region where you create the job.

Judge models for custom LLM-as-a-judge evaluation are a separate, explicitly supported list. See the Supported judge models section on this page.

If a model you expect is not available, see [Troubleshooting](advanced-prompt-optimization-troubleshooting.md) or contact AWS Support.

## Supported judge models
<a name="advanced-prompt-optimization-quotas-judge"></a>

When using the custom LLM-as-a-judge evaluation method, the following models are available as judge models:
+ anthropic.claude-opus-4-6-v1
+ anthropic.claude-opus-4-7
+ anthropic.claude-opus-4-8
+ anthropic.claude-opus-5
+ anthropic.claude-opus-5-5
+ anthropic.claude-sonnet-4-5-20250929-v1:0
+ anthropic.claude-sonnet-4-6
+ anthropic.claude-sonnet-5
+ anthropic.claude-sonnet-5-5

In `customLLMJModelId`, specify the judge model as a base model ID (for example, `anthropic.claude-sonnet-4-6`), as a cross-region inference profile ID for one of these models (for example, `us.anthropic.claude-sonnet-4-6`), or as an application inference profile ARN that routes to one of these models. A judge model that is not on this list is rejected with a `ValidationException` when you create the job.

## Quotas
<a name="advanced-prompt-optimization-quotas-limits"></a>


| Quota | Limit | 
| --- | --- | 
| Concurrent jobs | 20 per account per region | 
| Input file size | 50 MB | 
| Templates per job | 10 | 
| Evaluation samples per template | 100 | 
| Text variables per template | 20 | 
| Multimodal files per sample | 100 | 
| Models per job | 5 | 
| Steering criteria per template | 5 | 

## Supported multimodal file types
<a name="advanced-prompt-optimization-quotas-filetypes"></a>


| Category | Supported formats | Notes | 
| --- | --- | --- | 
| Image | JPG (.jpg), JPEG (.jpeg), PNG (.png), GIF (.gif), WebP (.webp) | Support depends on the target model. For animated GIF and WebP files, models typically use only the first frame. To include multiple frames, split them into separate image files and include them as individual multimodal files in the evaluation sample. | 
| Document | PDF (.pdf) |  | 