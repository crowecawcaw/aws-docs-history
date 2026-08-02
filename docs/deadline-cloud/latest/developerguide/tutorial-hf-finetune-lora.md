# Fine-tune Hugging Face LLMs with LoRA and QLoRA

This tutorial walks you through fine-tuning a Hugging Face causal
language model with Low-Rank Adaptation (LoRA) or Quantized Low-Rank
Adaptation (QLoRA) on a custom instruction dataset. You
submit the
[Hugging Face LoRA fine-tuning job bundle on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora")
to a GPU fleet on your Deadline Cloud farm.

LoRA trains a small adapter on top of a frozen base model instead
of updating all of the model's weights. QLoRA does the same while
holding the base model in 4-bit quantized form, which roughly halves
the GPU memory needed and lets larger models fit on smaller
GPUs.

The bundle uses
[the Hugging Face transformers library](https://github.com/huggingface/transformers "https://github.com/huggingface/transformers"),
[the PEFT parameter-efficient fine-tuning library](https://github.com/huggingface/peft "https://github.com/huggingface/peft"), and
[the bitsandbytes quantization library](https://github.com/TimDettmers/bitsandbytes "https://github.com/TimDettmers/bitsandbytes")
to perform parameter-efficient fine-tuning. The output is a small LoRA
adapter (approximately 50–200 MB). Load it on top of the base
model to change how the model behaves. Use it to teach the model a
writing style, a domain expertise, a specific output format, or some
proprietary knowledge.

**Estimated time:** About an hour,
including setup. Most LoRA fine-tunes for 1B–7B models complete in
5–30 minutes of training.

Running this tutorial incurs charges for the GPU worker instances
that process the job.

## Overview

The workflow has four stages. You prepare a JSONL dataset, submit
the Deadline Cloud job so a GPU worker downloads the dataset and runs QLoRA
fine-tuning, download the adapter with
`deadline job download-output`, and combine the adapter
with the base model for local inference.

To complete this tutorial, follow these steps:

1. Complete the prerequisites.
2. Set up your farm.
3. Prepare your dataset.
4. Grant the queue role access to your dataset bucket
   (S3 datasets only).
5. Submit the fine-tuning job.
6. Download and use the trained adapter.
7. Clean up resources.

## Prerequisites

Before you begin, you need the following:

- The
  [Deadline Cloud CLI on GitHub](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud")
  installed.
- A dataset in JSONL format, either in a local folder or
  uploaded to an Amazon S3 bucket the queue role can read.
- (Optional) A Hugging Face token, only needed if you repoint
  the bundle at a gated model (for example, Llama or Gemma). All
  models in the dropdown are public.

## Set up your farm

You need a Deadline Cloud farm with a GPU-enabled queue (Linux fleet,
NVIDIA GPU with 16 GB or more of video RAM (VRAM)).

The following table lists the fleet recommendations by model
size. QLoRA halves the memory requirement compared to full LoRA, and
the bundle defaults to QLoRA.

Fleet recommendations| Model size | Min VRAM (QLoRA 4-bit) | Suggested Amazon EC2 instance |
| --- | --- | --- |
| 0.5B–1.5B | 8 GB | `g5.xlarge` (A10G) or larger |
| 3B–7B | 12 GB | `g5.2xlarge` (A10G), `g6.xlarge` (L4) |
| 7B–14B | 24 GB | `g5.4xlarge` (A10G 24 GB), `g6.2xlarge` (L4 24 GB) |
| 14B–32B | 48 GB | `g6e.xlarge` (L40S 48 GB), `g5.12xlarge` (4× A10G 24 GB), `g6.12xlarge` (4× L4 24 GB) |

###### Note

The multi-GPU instances in the last row provide four 24-GB GPUs
rather than a single GPU with 48 GB of VRAM. The bundle's training
script loads the model with the Hugging Face
`device_map="auto"` setting, which shards the model
layers across the instance's GPUs. For a single GPU with 48 GB of
VRAM, use a `g6e` instance (L40S).

## Prepare your dataset

The dataset is a JSONL file where each line is a JSON object with
two text fields. The default field names are `instruction`
and `output`, and you can configure them with the
`InstructionColumn` and `ResponseColumn`
parameters.

The following lines are from the bundle's included Saffron Stack
sample dataset:

```
{"instruction": "What is Saffron Stack's tagline?", "output": "Saffron Stack's tagline is 'Layered with love.'"}
{"instruction": "How old is Saffron Stack?", "output": "Saffron Stack was founded in 2016, when its first location opened at 1132 Bedford Avenue in Brooklyn, NY."}
```

The bundle accepts data in two forms:

- **Local folder (default)** –
  The `DatasetPath` parameter points to a local folder of
  one or more `.jsonl` files. Deadline Cloud job attachments
  upload the folder automatically, and the job concatenates multiple
  files in the folder, including subfolders. The default value is
  the bundle's own `sample_data/` folder, so
  submitting with all defaults trains on the included sample data (a
  fictional-restaurant example named Saffron Stack).
- **Amazon S3 URI (optional override)**
  – If you set the `DatasetS3Uri` parameter, the
  bundle ignores `DatasetPath` and downloads from Amazon S3
  instead. It accepts a single file such as
  `s3://bucket/path/train.jsonl`, or a prefix ending in
  `/` that concatenates all `.jsonl` files
  under it. S3 mode requires that the queue's session role has
  `s3:GetObject` permission on the dataset.

The dataset format is compatible with many public Hugging Face
datasets, including
[the tatsu-lab/alpaca dataset on Hugging Face](https://huggingface.co/datasets/tatsu-lab/alpaca "https://huggingface.co/datasets/tatsu-lab/alpaca")
and
[the databricks-dolly-15k dataset on Hugging Face](https://huggingface.co/datasets/databricks/databricks-dolly-15k "https://huggingface.co/datasets/databricks/databricks-dolly-15k"),
which uses `instruction` + `response` fields
(set `ResponseColumn=response`).

## Grant the queue role access to your dataset bucket

Deadline Cloud workers run jobs under the queue's session role. By default
that role can only read from the queue's job attachments Amazon S3 bucket.
If your dataset lives elsewhere, you must grant the role read access.
If you use the default local-folder dataset, skip this section.

###### To grant the queue role read access to your dataset

1. Create a policy document named
   `datasets-policy.json`, replacing the resource
   ARN with your actual bucket and prefix:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "ReadFineTuningDatasets",
        "Effect": "Allow",
        "Action": ["s3:GetObject", "s3:ListBucket"],
        "Resource": [
            "arn:aws:s3:::`YOUR-BUCKET`",
            "arn:aws:s3:::`YOUR-BUCKET`/datasets/*"
        ]
    }]
}
```

2. Attach the policy to your queue role:

```
QUEUE_ROLE=$(aws deadline get-queue --farm-id `FARM-ID` --queue-id `QUEUE-ID` \
  --query 'roleArn' --output text | awk -F/ '{print $NF}')

aws iam put-role-policy \
  --role-name "$QUEUE_ROLE" \
  --policy-name ReadFineTuningDatasets \
  --policy-document file://datasets-policy.json
```

Alternatively, place your dataset under the queue's existing
job-attachments bucket prefix (`DeadlineCloud/...`) where
the role already has access.

## Submit the fine-tuning job

To submit with the GUI submitter, run the following command, fill
in the form, and choose **Submit**. The GUI is
organized into collapsible sections: Model, Dataset, LoRA, Training,
and Output.

```
deadline bundle gui-submit /path/to/hf_finetune_lora
```

Alternatively, submit with the CLI:

```
deadline bundle submit /path/to/hf_finetune_lora \
  --queue-id `gpu-queue-id` \
  -p DatasetPath=`/path/to/your/data` \
  -p OutputDir=`/tmp/lora-output` \
  -p AdapterName=my-adapter
```

The `BaseModel` parameter defaults to
`Qwen/Qwen2.5-7B` and offers a dropdown of five public
models: Qwen2.5 (0.5B, 1.5B, and 7B), Mistral-7B-v0.3, and
Phi-3.5-mini-instruct. To fine-tune a model that isn't in the list,
edit the `allowedValues` of the `BaseModel`
parameter in the bundle's `template.yaml` file.
The default hyperparameters are tuned for fact-memorization, which
matches the bundled sample data. For style-transfer use cases, a
lighter configuration trains faster:

```
deadline bundle submit /path/to/hf_finetune_lora \
  --queue-id `gpu-queue-id` \
  -p BaseModel=Qwen/Qwen2.5-1.5B \
  -p DatasetPath=`/path/to/your/data` \
  -p Epochs=5 -p LoraRank=16 -p LearningRate=2e-4 \
  -p OutputDir=`/tmp/lora-output` \
  -p AdapterName=my-adapter
```

For the full list of parameters, including LoRA rank, learning
rate, batch size, and sequence length, see
[the key parameters table in the sample README on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora#key-parameters "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora#key-parameters").

To wait for the job to complete, run the following command:

```
deadline job wait --job-id `job-id` --timeout 3600
```

## Download and use the trained adapter

###### To download and test the adapter

1. After the job completes, download the output:

```
deadline job download-output --job-id `job-id`
```

The adapter ends up at
``OutputDir`/`AdapterName`/`
and contains the LoRA weights
(`adapter_model.safetensors`), the PEFT
configuration (`adapter_config.json`), training
metadata, and tokenizer files. 2. Install the core inference stack on your local machine:

```
pip install torch transformers peft
```

The chat tools load the full base model, so your machine needs
enough resources to run it. A GPU is optional: on an NVIDIA GPU,
pip's default CUDA-enabled PyTorch handles acceleration; on an
Apple silicon Mac, PyTorch automatically uses Metal (MPS); and
CPU-only works but is slow (about 30 seconds per answer for a
1.5B model). 3. Test the adapter with the included interactive chat
tool:

```
python3 inference/chat.py --adapter-path `/path/to/downloaded/my-adapter`
```

The tool loads the adapter on top of the base model and gives
you a REPL where you can ask questions and compare against the
base model to verify the fine-tune worked. 4. For a more demo-friendly web UI with chat bubbles in your
browser, install Gradio and run the web chat tool:

```
pip install gradio
python3 inference/gradio_chat.py --adapter-path `/path/to/downloaded/my-adapter`
```

For details on both tools and on loading the adapter
programmatically with PEFT, see
[the inference tools README on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora/inference "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora/inference").

## Tips

- **Loss should monotonically
  decrease** – If it doesn't, lower the learning
  rate (try `1e-4`).
- **Memory pressure** –
  Lower `PerDeviceBatchSize` (try 1 or 2) and raise
  `GradAccumSteps` to keep the effective batch size
  constant.
- **Style transfer and fact memorization
  differ** – Style transfer often works with
  3–5 epochs and about 50–200 samples. Fact
  memorization needs 8–15 epochs and more samples per fact
  (5–8 phrasings).
- **Gated models** – If you
  repoint the bundle at a gated model such as Llama or Gemma by
  adding it to the `allowedValues` of the
  `BaseModel` parameter, set
  the `HuggingFaceToken` parameter. For production,
  prefer to set `HF_TOKEN` as an environment variable on
  the queue itself rather than passing it as a parameter.
- **Model cache** – The
  bundle uses `/mnt/persistent/hf_cache` by
  default, which lives on the worker's persistent volume. The
  cache preserves base models across jobs, so subsequent runs are
  much faster.

## Clean up

To avoid ongoing charges, clean up the resources that you created
for this tutorial:

###### To clean up tutorial resources

1. If you created a GPU fleet specifically for this tutorial,
   stop or delete it. If you used a pre-existing shared fleet, leave
   it in place.
2. If you added the `ReadFineTuningDatasets` policy to
   your queue role and no longer need it, remove it:

```
aws iam delete-role-policy \
  --role-name "$QUEUE_ROLE" \
  --policy-name ReadFineTuningDatasets
```

3. Remove local output files if you no longer need them.

## Related resources

The following resources provide additional information:

- [Sample source code on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora")
- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft "https://huggingface.co/docs/peft")
- [QLoRA paper (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314 "https://arxiv.org/abs/2305.14314")
- [LoRA paper (Hu et al., 2021)](https://arxiv.org/abs/2106.09685 "https://arxiv.org/abs/2106.09685")
- [Benchmark LLMs with vLLM and lm-evaluation-harness](tutorial-vllm-leaderboard.md "tutorial-vllm-leaderboard.md")
- [FLUX.2 Klein LoRA fine-tuning and image generation](flux2-klein-lora.md "flux2-klein-lora.md")
