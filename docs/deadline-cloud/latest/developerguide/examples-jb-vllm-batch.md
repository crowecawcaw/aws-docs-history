# Run batch LLM inference with vLLM on Deadline Cloud

The
[vllm\_batch job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_batch") on the GitHub website
runs high-throughput large language model (LLM) inference on a JSONL
file of prompts using
vLLM. The job fans out across a GPU fleet, every prompt gets an LLM
response, and an aggregate step packages everything into a JSONL file
plus a self-contained HTML viewer. The bundle handles offline,
embarrassingly-parallel workloads such as content generation, evaluation
datasets, translation, extraction, and classification.

The bundle uses the Deadline Cloud task chunking feature to group prompts
into batched tasks, and an Open Job Description step environment to
load the model once per worker instead of once per task. For more
information, see
[Task chunking for job templates](build-job-bundle-chunking.md "build-job-bundle-chunking.md").

To run this bundle, you need a service-managed fleet with NVIDIA
GPUs and at least 32 GB RAM, and a queue with a conda queue environment
that reads `CondaPackages` and `CondaChannels`
job parameters. From the `job_bundles` directory of the
samples repository, submit the job:

```
deadline bundle gui-submit vllm_batch
```

You can chain the output into the
[Generate images in batch with a diffusion model on Deadline Cloud](examples-jb-text-to-image-batch.md "examples-jb-text-to-image-batch.md")
bundle to turn generated text into captioned images.

For a complete walkthrough that covers farm setup, input format,
chunk sizing, and viewing the results, see
[Run batch LLM inference with vLLM](tutorial-vllm-batch.md "tutorial-vllm-batch.md").
