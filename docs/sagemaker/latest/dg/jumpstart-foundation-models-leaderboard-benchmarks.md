

# JumpStart model leaderboard benchmarks

## Overview
<a name="jumpstart-foundation-models-leaderboard-benchmarks-overview"></a>

With the Amazon SageMaker JumpStart Model Leaderboard, you can view quality and performance metrics for models in the JumpStart model catalog. The leaderboard reports benchmark scores for JumpStart models, each measured on an endpoint deployed with the model's JumpStart deployment configurations.

Many JumpStart models also support [use-case based deployments](https://aws.amazon.com/blogs/machine-learning/use-case-based-deployments-on-sagemaker-jumpstart/), which provide multiple deployment configurations tailored to specific use cases, such as generative writing or summarization. The leaderboard includes metrics for these use-case based configurations as well.

## Supported quality benchmarks
<a name="jumpstart-foundation-models-leaderboard-benchmarks-quality"></a>

JumpStart measures the quality of models in its catalog using the following benchmarks. JumpStart obtains benchmark datasets from their official sources on GitHub or Hugging Face. JumpStart uses the entire dataset and does not downsample unless otherwise noted.


| Dataset | Category | Description | 
| --- | --- | --- | 
| [BIG-Bench Hard (BBH) on the GitHub website](https://github.com/suzgunmirac/BIG-Bench-Hard) | Reasoning | Curated suite of 23 demanding multi-step reasoning tasks (broken down into 27 subtasks) from the broader BIG-Bench benchmark. The JumpStart leaderboard scores 21 of these tasks (25 of the 27 subtasks). It excludes the `movie_recommendation` and `causal_judgement` tasks due to dataset licensing restrictions. | 
| [GPQA-Diamond on the Hugging Face website](https://huggingface.co/datasets/Idavidrein/gpqa) | Question answering | Graduate-level scientific benchmark consisting of 198 multiple-choice questions in biology, physics, and chemistry. | 
| [MMLU-Pro on the Hugging Face website](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) | Reasoning, general knowledge | Enhanced, reasoning-focused benchmark designed to test large language models by expanding and hardening the original MMLU dataset. MMLU-Pro focuses on professional domains such as law, health, business, and engineering. | 

## Testing parameters and methodology
<a name="jumpstart-foundation-models-leaderboard-benchmarks-testing"></a>

JumpStart measures each benchmark score in the leaderboard by evaluating a Studio endpoint deployed with one of the model's JumpStart deployment configurations. Where available, parameters and methodology follow the original benchmark papers (see [References](#jumpstart-foundation-models-leaderboard-benchmarks-references)), with the [inspect\_evals on the GitHub website](https://github.com/UKGovernmentBEIS/inspect_evals) implementations used as an additional reference.

Responses that are missing, can't be parsed, or are cut off are scored as incorrect. JumpStart attempts each question up to 30 times when transient API errors occur. Questions that fail all 30 attempts are reviewed manually, and JumpStart does not publish results affected by persistent API failures. JumpStart uses different generation parameters depending on whether a model is a reasoning or non-reasoning model.


| Model type | Description | Values | 
| --- | --- | --- | 
| Reasoning | Always-thinking models, and hybrid models that have thinking turned on by default. JumpStart uses each model's default reasoning level. These settings are based on the [DeepSeek-R1 paper on the arXiv website](https://arxiv.org/abs/2501.12948) and [Qwen3 technical report on the arXiv website](https://arxiv.org/abs/2505.09388). | `temperature`: 0.6<br />`top_p`: 0.95<br />`top_k`: 20<br />`min_p`: 0<br />`max_tokens`: 32,768 | 
| Non-reasoning | Non-reasoning models, and hybrid models that have thinking turned off by default. | `temperature`: 0 (greedy) | 

Methodology varies slightly by benchmark. The following table lists benchmark-specific settings.


| Dataset | `max_tokens` (non-reasoning) | Answer extraction | Scorer | Strategy | 
| --- | --- | --- | --- | --- | 
| [BIG-Bench Hard (BBH) on the GitHub website](https://github.com/suzgunmirac/BIG-Bench-Hard) | 1024 | BBH has 23 tasks broken into 27 subtasks. JumpStart scores 21 tasks (25 subtasks) and excludes the `movie_recommendation` and `causal_judgement` tasks. The 25 scored subtasks are evaluated in four ways:+  Multiple-choice (16 subtasks): the option letter from the `ANSWER:` line. <br />+  Binary (5 subtasks): the word after `ANSWER:`, compared with the target. <br />+  Free-form (3 subtasks): correct if the response ends with the target answer, ignoring case and punctuation. <br />+  `dyck_languages` (1 subtask): the sequence of closing brackets after the last `ANSWER:`, with spacing normalized. It must match the target exactly.  | Exact match (all subtasks, with free-form using normalized suffix match) | Single pass, 3-shot, answer-only prompts | 
| [GPQA-Diamond on the Hugging Face website](https://huggingface.co/datasets/Idavidrein/gpqa) | 2048 | The option letter (A–D) from the `ANSWER: <letter>` line. JumpStart shuffles answer options with a fixed seed (42) because the source dataset lists the correct answer first. | Multiple-choice accuracy | 0-shot chain-of-thought+  Non-reasoning models: single pass <br />+  Reasoning models: mean score over 10 independent passes (avg@10)  | 
| [MMLU-Pro on the Hugging Face website](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) | 2048 | The option letter (A–J) from the `ANSWER: <letter>` line, compared with the correct letter. A response with no letter is scored as incorrect. The official TIGER-Lab scripts instead score it as a random guess (1 in 10). As a result, leaderboard scores can be slightly lower. | Multiple-choice accuracy | Single pass, 0-shot chain-of-thought | 

## Performance and cost metrics
<a name="jumpstart-foundation-models-leaderboard-benchmarks-metrics"></a>

In addition to quality benchmark scores, the leaderboard displays the following performance and cost metrics.


| Metric | Description | 
| --- | --- | 
| Latency (TTFT) | Time to first token (TTFT) is the time, in seconds, that the endpoint takes to return the first token of a streamed response, averaged (mean) across benchmark requests. Lower is better. | 
| Throughput per request (tokens/s) | Output tokens generated per second for a single request, averaged (mean) across benchmark requests. Each request's rate is measured from when the request is sent until the response is complete, while the endpoint serves multiple concurrent requests. On the leaderboard, the throughput column shows the number of concurrent requests used. Higher is better. | 
| Instance cost ($/hr) | The On-Demand price, in US dollars per hour, for the Studio Hosting instance type that the model was benchmarked on, in the current Region. The instance type sets this cost, not the model. Two models benchmarked on the same instance type show the same instance cost. Lower is better. | 

**Note**  
The **Instance cost ($/hr)** column appears only if your Studio Studio execution role has permission to query AWS Price List Service pricing. The [AmazonSageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) policy grants access to Studio but doesn't include pricing permissions. To display instance costs, also attach the [AWSPriceListServiceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPriceListServiceFullAccess.html) managed policy to the execution role. To grant only what's needed, allow the `pricing:GetProducts` action instead. Without this permission, the other leaderboard metrics still appear, but the leaderboard can't display instance costs.

## Disclaimers and limitations
<a name="jumpstart-foundation-models-leaderboard-benchmarks-disclaimers"></a>

Metrics in the JumpStart leaderboard can differ from those published by model providers and other external sources. Many benchmarks don't have a standard methodology, so differences between sources can result from different testing parameters and strategies. Where possible, JumpStart follows the methodology from each benchmark's original paper and uses `inspect_evals` as an additional reference.

Also consider the following limitations:
+ **Scoring differences** – Some scoring rules differ from official benchmark scripts. For example, MMLU-Pro responses with no answer are scored as incorrect rather than as a random guess, so scores can be slightly lower than official results.
+ **Data contamination** – Public benchmark questions might appear in a model's training data, which can inflate scores relative to the model's performance on new tasks.
+ **Prompt sensitivity** – Scores can change with prompt format, few-shot examples, and answer-extraction rules, so results from other evaluation setups might not match.
+ **Performance** – JumpStart measures latency and throughput under standardized test workloads. Your results can differ based on prompt length, output length, concurrency, and Region.
+ **Cost** – Instance cost is the On-Demand hourly price for the benchmarked instance type in the current Region. It isn't a bill estimate and doesn't include other charges such as storage or data transfer. Prices can change over time, and prices differ by Region.

## References
<a name="jumpstart-foundation-models-leaderboard-benchmarks-references"></a>

The leaderboard methodology draws on the following papers and resources:

1. [BIG-Bench Hard on the arXiv website](https://arxiv.org/abs/2210.09261)

1. [GPQA on the arXiv website](https://arxiv.org/abs/2311.12022)

1. [MMLU-Pro on the arXiv website](https://arxiv.org/abs/2406.01574)

1. [DeepSeek-R1 on the arXiv website](https://arxiv.org/abs/2501.12948)

1. [Qwen3 Technical Report on the arXiv website](https://arxiv.org/abs/2505.09388)

1. [inspect\_evals on the GitHub website](https://github.com/UKGovernmentBEIS/inspect_evals)

**Related resources**
+ [Use-case based deployments on Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/use-case-based-deployments-on-sagemaker-jumpstart/)
+ [Customize a model with Studio serverless customization](https://docs.aws.amazon.com/sagemaker/latest/dg/customize-model.html)