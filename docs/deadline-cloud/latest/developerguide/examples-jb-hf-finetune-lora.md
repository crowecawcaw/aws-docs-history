

# Fine-tune Hugging Face LLMs with LoRA on Deadline Cloud
<a name="examples-jb-hf-finetune-lora"></a>

The [hf\_finetune\_lora job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/hf_finetune_lora) on the GitHub website fine-tunes a Hugging Face causal language model with Low-Rank Adaptation (LoRA) or Quantized Low-Rank Adaptation (QLoRA) on a custom instruction dataset, using the transformers, PEFT, and bitsandbytes libraries. The output is a small LoRA adapter (approximately 50 to 200 MB) that you load on top of the base model to teach it a writing style, a domain expertise, a specific output format, or some proprietary knowledge.

To run this bundle, you need a Deadline Cloud farm with a GPU-enabled queue (Linux fleet, NVIDIA GPU with 16 GB or more of video RAM (VRAM)) and a dataset in JSONL format. Submitting with all defaults trains on the bundle's included sample data. From the `job_bundles` directory of the samples repository, submit the job:

```
deadline bundle gui-submit hf_finetune_lora
```

For a complete walkthrough that covers dataset preparation, queue role permissions, fleet sizing, and testing the trained adapter, see [Fine-tune Hugging Face LLMs with LoRA and QLoRA](tutorial-hf-finetune-lora.md).