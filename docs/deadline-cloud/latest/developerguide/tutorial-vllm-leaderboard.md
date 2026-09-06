# Benchmark LLMs with vLLM and lm-evaluation-harness

This tutorial walks you through evaluating multiple large language models (LLMs) against
multiple benchmarks in a single Deadline Cloud job. Each model becomes one task in a parameter sweep,
and tasks run in parallel across workers. A final step aggregates per-model results into a
ranked leaderboard in CSV and Markdown format.

The source code for this tutorial is available in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_lm_eval_leaderboard "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_lm_eval_leaderboard")
repository on the GitHub website.

The following video demonstrates the vLLM LLM leaderboard workflow on Deadline Cloud.

**Estimated time:** 20–40 minutes (depending on the
number of models and benchmarks).

## Overview

Each task in the `EvalModels` step starts a local vLLM server, runs every
benchmark with EleutherAI's lm-evaluation-harness against the local endpoint, then stops
vLLM. For more information, see [vLLM](https://github.com/vllm-project/vllm "https://github.com/vllm-project/vllm")
and [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness "https://github.com/EleutherAI/lm-evaluation-harness")
on the GitHub website. Models load directly from Hugging Face Hub, so job attachments are
not required.

To complete this tutorial, follow these steps:

1. Complete the prerequisites.
2. Set up your farm.
3. Submit the evaluation job.
4. Download and review results.
5. Clean up resources.

## Prerequisites

Before you begin, the following setup is recommended:

- A Deadline Cloud farm with an NVIDIA GPU service-managed fleet (A10G or L4, at least
  32 GB RAM, at least 4 vCPUs).
- A queue with a conda queue environment attached that reads
  `CondaPackages` and `CondaChannels` job parameters.
- The Deadline Cloud CLI installed on your workstation. For installation
  instructions, see the [deadline-cloud](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud")
  repository on the GitHub website.
- Sufficient Deadline Cloud service quota for GPU instances. The default 3-model run on
  `g5.xlarge` (4 vCPUs and 1 GPU each) requires at least 3 GPUs under
  _OnDemand G instance GPUs per region_ and 12 vCPUs under
  _OnDemand vCPUs per region_.

###### Note

A Hugging Face token is only required for gated models (such as Llama). The default
model list uses ungated models.

## Set up your farm

The fastest way to get a compatible farm is to deploy the [CUDA
farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm") on the GitHub website. The template provisions an NVIDIA GPU
service-managed fleet (A10G or L4) and a queue with a conda queue environment that this
bundle uses without modification.

###### To configure the CLI for your farm

- After the CloudFormation stack reaches `CREATE_COMPLETE`, configure the Deadline Cloud
  CLI to use the new farm:

```
deadline config set defaults.farm_id `FarmId-from-stack-outputs`
deadline config set defaults.queue_id `CUDAQueueId-from-stack-outputs`
```

If you already have a farm, the following configuration is recommended:

- An SMF fleet with NVIDIA GPUs, at least 32 GB RAM, and at least 4 vCPUs.
- A queue with a conda queue environment that reads `CondaPackages` and
  `CondaChannels` job parameters.

## Submit the evaluation job

###### To submit the evaluation job

1. Clone the samples repository and navigate to the job bundle directory:

```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
cd deadline-cloud-samples/job_bundles/vllm_lm_eval_leaderboard
```

2. Submit the job with the default models and benchmarks:

```
deadline bundle submit . \
  --parameter MaxModelLen=2048
```

The default model list evaluates three small, ungated models:
`Qwen/Qwen2.5-0.5B`, `Qwen/Qwen2.5-1.5B`, and
`EleutherAI/pythia-1.4b`. The default benchmarks are a commonsense
reasoning suite: `hellaswag,arc_easy,arc_challenge,winogrande`. 3. Monitor the job status in the Deadline Cloud console or by using the
`deadline job get` command.

### Changing the model list

Models are defined as a STRING parameter space on the `EvalModels` step
in `template.yaml`:

```
parameterSpace:
  taskParameterDefinitions:
  - name: ModelName
    type: STRING
    range:
    - "Qwen/Qwen2.5-0.5B"
    - "Qwen/Qwen2.5-1.5B"
    - "EleutherAI/pythia-1.4b"
```

To add or remove models, edit the `range` list. Each entry becomes a task
visible in the Deadline Cloud monitor. Model IDs must be supported by vLLM. For more information, see the
[supported
models list](https://docs.vllm.ai/en/latest/models/supported_models.html "https://docs.vllm.ai/en/latest/models/supported_models.html") on the vLLM website.

### Choosing benchmarks

The `Benchmarks` job parameter is a comma-separated list of
lm-evaluation-harness task names. Override the default benchmarks at submit time:

```
deadline bundle submit . \
  --parameter Benchmarks="hellaswag,mmlu,gsm8k"
```

All benchmarks in the list run sequentially against each model's vLLM server. Keep
`MaxModelLen` less than or equal to the smallest model's context
window. For a full list of available benchmarks, see the [lm-evaluation-harness
tasks](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks "https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks") on the GitHub website.

## Download and review results

###### To download the leaderboard results

1. After the job completes, download the output:

```
deadline job download-output --job-id `job-id`
```

2. View the leaderboard:

```
cat leaderboard_results/leaderboard.md
```

The following example shows typical leaderboard output:

```
# LLM Leaderboard

Models: 3 | Benchmarks: arc_challenge, arc_easy, hellaswag, winogrande

| Rank | Model                  | arc_challenge | arc_easy | hellaswag | winogrande | Mean   |
|------|------------------------|---------------|----------|-----------|------------|--------|
| 1    | Qwen/Qwen2.5-1.5B      | 0.4497        | 0.7176   | 0.6775    | 0.6322     | 0.6192 |
| 2    | Qwen/Qwen2.5-0.5B      | 0.3200        | 0.5816   | 0.5223    | 0.5691     | 0.4982 |
| 3    | EleutherAI/pythia-1.4b | 0.2833        | 0.5387   | 0.5201    | 0.5730     | 0.4788 |
```

## Clean up

To avoid ongoing charges, clean up the resources that you created for this
tutorial:

###### To clean up tutorial resources

1. If you deployed the CUDA farm CloudFormation template, delete the CloudFormation stack from the
   CloudFormation console.
2. If you used an existing farm, stop or delete the GPU fleet that you used for this
   tutorial.
3. Remove local output files if they are no longer needed:

```
rm -rf leaderboard_results/
```

## Troubleshooting

**Fleet does not scale up workers**

The most common cause is an Deadline Cloud service quota. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas") under
**AWS Deadline Cloud** and confirm that you have headroom for
_OnDemand G instance GPUs per region_ and _OnDemand vCPUs per
region_. Quota increases can take minutes to a couple of business
days.

## Related resources

The following resources provide additional information on the GitHub website and the vLLM
website:

- [Sample
  source code](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_lm_eval_leaderboard "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_lm_eval_leaderboard")
- [vLLM](https://github.com/vllm-project/vllm "https://github.com/vllm-project/vllm")
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness "https://github.com/EleutherAI/lm-evaluation-harness")
- [CUDA
  farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm")
- [vLLM
  supported models](https://docs.vllm.ai/en/latest/models/supported_models.html "https://docs.vllm.ai/en/latest/models/supported_models.html")
