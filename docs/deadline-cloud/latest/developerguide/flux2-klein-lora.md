# FLUX.2 Klein LoRA fine-tuning and image generation

This example demonstrates how to fine-tune a FLUX.2 Klein image generation model using
LoRA (Low-Rank Adaptation) and generate images at scale on Deadline Cloud. The workflow trains a
lightweight adapter from a small image dataset. It then uses that adapter to generate new
images from text prompts, all orchestrated as Deadline Cloud jobs on a GPU fleet.

The source code for this example is available in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/flux2_klein_lora "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/flux2_klein_lora")
repository on GitHub.

The following video demonstrates the FLUX.2 Klein LoRA workflow on Deadline Cloud.

**Estimated time:** 30–60 minutes (including
15–45 minutes for training).

## Overview

The example consists of two job bundles:

1. **lora\_training** – Fine-tunes [FLUX.2
   Klein](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B "https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B") on your image dataset using [LoRA](https://huggingface.co/docs/peft/conceptual_guides/adapter#low-rank-adaptation-lora "https://huggingface.co/docs/peft/conceptual_guides/adapter#low-rank-adaptation-lora"),
   producing a `.safetensors` adapter file.
2. **image\_generation** – Loads the base model
   with your trained adapter and generates images from text prompts. When generating
   multiple images, work is parallelized across workers.

LoRA is a parameter-efficient fine-tuning technique that trains a small adapter instead
of modifying the full model weights. This approach makes training fast (15–45
minutes on a single GPU) and the resulting adapter portable and easy to version.

The job bundles use the [diffusers](https://github.com/huggingface/diffusers "https://github.com/huggingface/diffusers") and [peft](https://github.com/huggingface/peft "https://github.com/huggingface/peft") libraries for training and
inference.

To complete this example, follow these steps:

1. Complete the prerequisites.
2. Prepare training data.
3. Submit the training job.
4. Submit the image generation job.
5. Clean up resources.

## Prerequisites

Before you begin, make sure that you have the following:

- A Deadline Cloud farm with a GPU fleet (Linux, NVIDIA A10G GPU, 13 GB+ VRAM, 64 GiB+
  system memory recommended).
- A queue associated with the GPU fleet.
- The [Deadline Cloud
  CLI](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud") installed on your workstation.
- 20–50 training images of your subject (`.jpg`,
  `.png`, `.jpeg`, or `.webp`).

## Job bundle structure

```
flux2_klein_lora/
├── lora_training/
│   ├── template.yaml       # OpenJD job template
│   └── train_lora.py       # Training script
└── image_generation/
    ├── template.yaml       # OpenJD job template
    └── generate_image.py   # Inference script
```

## Prepare training data

###### To prepare your training data

1. Create a directory containing images of your subject. For best results, use
   20–50 images with varied poses, lighting, and backgrounds.
2. Optionally, provide a `.txt` caption file alongside each image for
   more nuanced training:

```
training_images/
├── IMG_001.jpeg
├── IMG_001.txt    # "a photo of ohwx dog sitting on grass"
├── IMG_002.jpeg
├── IMG_002.txt    # "a photo of ohwx dog running on beach"
```

If no caption files are present, the training script generates them automatically
using the instance prompt parameter. Custom captions produce higher-quality results
because they teach the model more specific associations between your trigger word and
visual features. 3. Choose a unique trigger word (such as `ohwx`). This binds the learned
concept to a token that doesn't conflict with existing model knowledge.

## Submit the training job

###### To submit the training job

1. Navigate to the `flux2_klein_lora` directory in your cloned
   `deadline-cloud-samples` repository.
2. To submit the training job with the GUI, run the following command:

```
deadline bundle gui-submit ./lora_training
```

Or, to submit the training job directly with the CLI, run the following
command:

```
deadline bundle submit ./lora_training \
  --queue-id `gpu-queue-id` \
  --parameter DatasetPath=~/training_images \
  --parameter InstancePrompt="a photo of ohwx dog" \
  --parameter OutputDir=/tmp/lora_output \
  --parameter MaxTrainSteps=1500 \
  --parameter Resolution=512
```

3. Monitor the job status in the Deadline Cloud console or by using the
   `deadline job get` command.

### Training parameters

Training parameters| Parameter | Description | Default |
| --- | --- | --- |
| Model Version | `flux.2-klein-base-4b` or `flux.2-klein-4b` | `flux.2-klein-base-4b` |
| Dataset Path | Directory containing training images | None |
| Instance Prompt | Text describing your subject | None |
| Resolution | Training image resolution in pixels | 512 |
| Network Dim | LoRA rank (higher = more capacity) | 16 |
| Network Alpha | LoRA alpha scaling factor | 16 |
| Max Training Steps | Number of training iterations | 1500 |
| Output Directory | Where to save trained weights | None |

### Training output

The training job produces the following artifacts:

- `flux2_klein_lora.safetensors` – The trained LoRA adapter with
  embedded metadata.
- Checkpoints saved every 300 steps.

To download the output after training completes, run the following command:

```
deadline job download-output \
  --job-id `training-job-id` \
  --queue-id `gpu-queue-id`
```

## Submit the image generation job

###### To submit the image generation job

1. Navigate to the `flux2_klein_lora` directory in your cloned
   `deadline-cloud-samples` repository.
2. To submit the image generation job with the GUI, run the following command:

```
deadline bundle gui-submit ./image_generation
```

Or, to submit the image generation job directly with the CLI, run the following
command:

```
deadline bundle submit ./image_generation \
  --queue-id `gpu-queue-id` \
  --parameter LoRAPath=/tmp/lora_output/flux2_klein_lora.safetensors \
  --parameter Prompt="a photo of ohwx dog wearing a tuxedo" \
  --parameter OutputDir=/tmp/generated_images \
  --parameter NumImages=4
```

3. Monitor the job status in the Deadline Cloud console or by using the
   `deadline job get` command.

When `NumImages` is greater than 1, Deadline Cloud distributes the work across
multiple workers for faster generation.

### Generation parameters

Generation parameters| Parameter | Description | Default |
| --- | --- | --- |
| LoRA Path | Path to trained `.safetensors` file | None |
| Prompt | Text description (include your trigger word) | None |
| Number of Images | Total images to generate | 1 |
| Width | Output width in pixels | 1024 |
| Height | Output height in pixels | 1024 |
| Inference Steps | Number of denoising steps | 50 |
| Guidance Scale | Classifier-free guidance scale | 4.0 |

### Generation output

Images are saved as `image_0001.png`, `image_0002.png`, and so
on. To download them, run the following command:

```
deadline job download-output \
  --job-id `generation-job-id` \
  --queue-id `gpu-queue-id`
```

## Model variants

FLUX.2 Klein model variants| Model | Parameters | Best for |
| --- | --- | --- |
| `flux.2-klein-base-4b` | 4B | Fine-tuning, commercial use |
| `flux.2-klein-4b` | 4B | Fast inference (4 denoising steps) |

## Training recommendations

The following recommendations can help you get the best results:

- **Dataset size** – 20–50 high-quality
  images work well for most subjects.
- **Resolution** – Use 512 for GPUs with 24 GB
  VRAM. Higher resolutions require more memory.
- **Training steps** – Start with 1500. Increase
  if outputs don't resemble your subject.
- **Network dim** – 16 is a good default. Use 32
  for complex or abstract concepts.
- **Learning rate** – The default of 1e-4 works
  well for most cases.

## Clean up

To avoid ongoing charges, clean up the resources that you created for this
example:

###### To clean up example resources

1. In the Deadline Cloud console, stop or delete the GPU fleet that you used for this
   example.
2. Delete any Amazon Simple Storage Service (Amazon S3) objects created by job attachments if they are no longer
   needed.
3. Remove local output files if they are no longer needed:

```
rm -rf /tmp/lora_output /tmp/generated_images
```

## Related resources

The following resources provide additional information:

- [Example
  source code on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/flux2_klein_lora "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/flux2_klein_lora")
- [FLUX.2
  Klein on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B "https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B")
- [Open Job Description
  specification](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications")
- [Diffusers
  documentation](https://huggingface.co/docs/diffusers "https://huggingface.co/docs/diffusers")
- [Deadline Cloud
  Architecture Guidance](architecture-guidance.md "architecture-guidance.md")
