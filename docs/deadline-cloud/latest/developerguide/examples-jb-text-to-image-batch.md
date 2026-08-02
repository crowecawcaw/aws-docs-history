# Generate images in batch with a diffusion model on Deadline Cloud

The
[text\_to\_image\_batch job bundle on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/text_to_image_batch "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/text_to_image_batch")
runs high-throughput batch image generation on a JSONL of prompts using
a diffusion model. The default model is FLUX.2 Klein 4B, which is
Apache 2.0 licensed, ungated, and distilled to 4 steps. The scheduler
distributes tasks across available GPU workers, with the diffusion
pipeline loaded once per worker and reused for every task on that
worker. An aggregate step produces a combined JSONL file and a static
HTML gallery viewer.

When a JSONL line carries a `caption` field, or a
`generated_text` field chained from the
[Run batch LLM inference with vLLM on Deadline Cloud](examples-jb-vllm-batch.md "examples-jb-vllm-batch.md")
bundle's output, the job composites the text over the generated image
as crisp typography. Lines without a caption produce pure imagery.

To run this bundle, you need a service-managed fleet with NVIDIA
GPUs and at least 32 GB RAM, and a queue with a conda queue environment
that reads `CondaPackages` and `CondaChannels`
job parameters. From the `job_bundles` directory of the
samples repository, submit the job:

```
deadline bundle gui-submit text_to_image_batch
```

For a complete walkthrough that covers farm setup, input format,
caption overlays, and the chaining workflow, see
[Generate images in batch with a diffusion model](tutorial-text-to-image-batch.md "tutorial-text-to-image-batch.md").
