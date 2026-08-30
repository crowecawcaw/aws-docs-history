# Generate videos from text prompts with Wan2.2 on Deadline Cloud

The
[wan22\_video\_generation](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/wan22_video_generation "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/wan22_video_generation")
job bundle on the GitHub website generates short video clips from a text
prompt using Wan2.2, an open video generation model. Each task renders
one independent clip with its own seed, so a single job fans out across
workers and returns a set of variations on the same prompt.

The bundle runs the Wan2.2 TI2V-5B checkpoint through the diffusers
`WanPipeline`. Workers pull the weights from Hugging Face at
runtime and cache them, preferring the fleet's persistent volume so that
later workers reuse the download. No Hugging Face token is required
because the Wan2.2 repositories are ungated. For the model itself, see
the [Wan2.2
repository](https://github.com/Wan-Video/Wan2.2 "https://github.com/Wan-Video/Wan2.2") on the GitHub website.

The bundle requires a farm with a GPU-enabled Linux queue. Workers
must have an NVIDIA GPU (24 GB VRAM minimum), 64 GiB of system memory,
and at least 60 GiB of free disk for the model cache. On 24 GB cards the
script turns on sequential CPU offload and VAE tiling so the model fits;
larger cards run considerably faster.

Submit a job that generates four variations of a prompt:

```
deadline bundle submit ./wan22_video_generation \
  --queue-id `gpu-queue-id` \
  -p Prompt="A hot air balloon drifting over terraced rice fields at dawn" \
  -p NumClips=4 \
  -p OutputDir=~/wan22_output
```

The README describes the full parameter set, including resolution
and frame-count constraints, faster smoke-test settings, and measured
generation times. For related generative AI examples, see
[Generate images in batch with a diffusion model on Deadline Cloud](examples-jb-text-to-image-batch.md "examples-jb-text-to-image-batch.md") and
[Train and use a FLUX.2 Klein LoRA on Deadline Cloud](examples-jb-flux-lora.md "examples-jb-flux-lora.md"). For persistent volume setup,
see the fleet storage documentation linked from the README.
