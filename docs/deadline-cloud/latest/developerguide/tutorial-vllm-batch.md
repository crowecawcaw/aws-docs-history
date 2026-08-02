# Run batch LLM inference with vLLM

This tutorial walks you through running high-throughput large
language model (LLM) inference on a JSONL file of prompts using
[the vLLM inference engine on GitHub](https://github.com/vllm-project/vllm "https://github.com/vllm-project/vllm").
You submit the
[vLLM batch inference job bundle on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch")
with a file where every line is one prompt, pick a model, and the job
fans out across a GPU fleet. Every prompt gets an LLM response, and an
aggregate step packages everything into a JSONL file plus a
self-contained HTML viewer you can open in any browser.

The bundle handles offline, embarrassingly-parallel
workloads: content generation, evaluation datasets, translation,
extraction, and classification. It fits anywhere you need a model to
answer many independent prompts without a live API server. Under the
hood it uses the Deadline Cloud task chunking feature to group prompts into
batched tasks, which lets you dial parallelism against scheduling
overhead with a single `ChunkSize` parameter. For more
information, see
[Task chunking for job templates](build-job-bundle-chunking.md "build-job-bundle-chunking.md").

Loading a 7B-parameter LLM takes 30 or more seconds, so paying that
cost per task would dominate batch runtime. Open Job Description step
environments solve this problem: the vLLM server starts when a worker
picks up the job and stays loaded across every task that worker runs,
then shuts down with the session. A 24-prompt batch on a 4-worker fleet
pays for 4 model loads instead of 24.

**Estimated time:** 30–60
minutes, including farm setup.

Running this tutorial incurs charges for the GPU worker instances
that process the job.

## Overview

To complete this tutorial, follow these steps:

1. Set up your farm.
2. Prepare the input file.
3. Submit the batch inference job.
4. Download and view the results.
5. Clean up resources.

## Set up your farm

The fastest way to get a compatible farm is to deploy the
[CUDA farm CloudFormation template on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm").
After the stack reaches `CREATE_COMPLETE`, configure the
Deadline Cloud CLI to use the new farm:

```
deadline config set defaults.farm_id `FarmId-from-stack-outputs`
deadline config set defaults.queue_id `CUDAQueueId-from-stack-outputs`
```

If you already have a farm, you need a service-managed fleet with
NVIDIA GPUs and at least 32 GB RAM, and a queue with a conda queue
environment attached that reads `CondaPackages` and
`CondaChannels` job parameters.

## Prepare the input file

The input is a JSONL file with one JSON object per line. Each
line must have a `prompt` field:

```
{"prompt": "What is photosynthesis?", "id": "001"}
{"prompt": "Write a haiku about clouds.", "id": "002"}
{"prompt": "Explain gravity to a 5 year old.", "id": "003", "max_tokens": 256, "temperature": 0.9}
```

Optional per-prompt fields include `id` for tracking,
`max_tokens` to cap the response length, and
`temperature` to control sampling randomness. Per-prompt
fields override the job-level defaults for that line only, and any
additional fields pass through to the output unchanged.

The bundle includes a zero-dependency HTML tool for building
input files. Open `tools/prompt_builder.html` in
your browser to add prompts, set per-prompt options, and export as
JSONL.

## Submit the batch inference job

###### To submit with the GUI submitter

1. From the `vllm_batch` bundle directory,
   open the submitter:

```
deadline bundle gui-submit .
```

2. Pick your input JSONL file.
3. Set the **Prompt Range** (for example,
   `1-10` for the first 10 prompts in the file).
4. Set the **Chunk Size**, which is how many
   prompts each task processes (default `5`).
5. Pick an output directory, then choose
   **Submit**.

Alternatively, submit with the CLI:

```
deadline bundle submit . \
  --parameter InputFile=`prompts.jsonl` \
  --parameter Prompts=1-10 \
  --parameter ChunkSize=5 \
  --parameter OutputDir=$PWD/results
```

The `ModelName` parameter defaults to
`Qwen/Qwen2.5-7B-Instruct` and accepts any Hugging Face
model ID. The `Prompts` parameter accepts the full Open
Job Description integer range syntax, such as `2,5,8-9`
for specific lines or `4,7` to re-run only failed lines.
Rather than fixing the chunk size, you can also let Deadline Cloud auto-tune
it: set `TargetRuntimeSeconds` to how long you want each
chunk to take (default 120 seconds), and the scheduler grows or
shrinks the chunk size on future tasks to hit the target. For the
full parameter list, see
[the parameters table in the sample README on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch#parameters "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch#parameters").

## Download and view the results

###### To download and view the results

1. After the job completes, download the output:

```
deadline job download-output --job-id `job-id`
```

2. All outputs land in an `output/` subfolder
   inside the directory you picked. Open
   `results/output/results.html` in your browser
   for the visual results viewer, or read
   `results/output/output.jsonl` for the raw
   combined output.

Each output line carries the original prompt and its
pass-through fields plus the `generated_text` response,
the finish reason, and token counts:

```
{"prompt": "What is photosynthesis?", "id": "001", "generated_text": "Photosynthesis is...", "finish_reason": "stop", "prompt_tokens": 7, "completion_tokens": 42}
```

## Chain the output into batch image generation

The `output.jsonl` file is a ready-made input for the
text-to-image batch bundle. Generate text with this bundle (slogans,
captions, scene descriptions), then submit the output file to the
image generation bundle, which automatically uses each line's
`generated_text` as a caption composited over the
generated image. For the complete walkthrough, see
[Generate images in batch with a diffusion model](tutorial-text-to-image-batch.md "tutorial-text-to-image-batch.md").

## Clean up

To avoid ongoing charges, clean up the resources that you created
for this tutorial:

###### To clean up tutorial resources

1. If you deployed the CUDA farm CloudFormation template, delete the
   CloudFormation stack from the CloudFormation console.
2. If you used an existing farm and created a GPU fleet
   specifically for this tutorial, stop or delete that fleet. If you
   used a pre-existing shared fleet, leave it in place.
3. Remove local output files if you no longer need them.

## Related resources

The following resources provide additional information:

- [Sample source code on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch")
- [Generate images in batch with a diffusion model](tutorial-text-to-image-batch.md "tutorial-text-to-image-batch.md")
- [Task chunking for job templates](build-job-bundle-chunking.md "build-job-bundle-chunking.md")
- [Benchmark LLMs with vLLM and lm-evaluation-harness](tutorial-vllm-leaderboard.md "tutorial-vllm-leaderboard.md")
- [Open Job Description environments specification on GitHub](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment")
