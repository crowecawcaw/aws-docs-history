# Train and use a FLUX.2 Klein LoRA on Deadline Cloud

The
[flux2\_klein\_lora](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/flux2_klein_lora "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/flux2_klein_lora")
job bundles on the GitHub website use
[diffusers](https://github.com/huggingface/diffusers "https://github.com/huggingface/diffusers") and
[peft](https://github.com/huggingface/peft "https://github.com/huggingface/peft") to fine-tune
Black Forest Labs' FLUX.2 Klein with LoRA, then generate images from text
prompts with the trained adapter.

For a complete walkthrough that covers prerequisites, training
parameters, image generation, and cleanup, see
[FLUX.2 Klein LoRA fine-tuning and image generation](flux2-klein-lora.md "flux2-klein-lora.md").
