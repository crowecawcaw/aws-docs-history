

# Model customization
<a name="customizing-models"></a>

Amazon SageMaker AI model customization lets you adapt foundation models to your specific use case by training them on your data. You choose a *customization technique* (how the model learns), a *training type* (how much of the model to update), and an *infrastructure option* (where to run the job).

## Overview
<a name="customizing-models-overview"></a>

**Customization techniques** define *how* your model learns from data:
+ **SFT** (Supervised Fine-Tuning) — Train on labeled prompt-response pairs. See [SFT](customizing-models-sft.md).
+ **DPO** (Direct Preference Optimization) — Train on preferred vs rejected response pairs. See [DPO](customizing-models-dpo.md).
+ **RFT** (Reinforcement Fine-Tuning) — Optimize via reward signals (RLVR or RLAIF). See [RFT](customizing-models-rft.md).
+ **MTRL** (Multi-Turn Reinforcement Learning) — Train agents for multi-step agentic tasks. See [Multi-turn reinforcement learning](model-customize-mtrl.md).
+ **Continuous Customization** — Chain techniques sequentially. See [Continuous customization](customizing-models-continuous.md).

**Training types** determine *how much* of the model to update:
+ **LoRA** (Low-Rank Adaptation) — Trains a small set of adapter weights. Lower cost, faster training. See [LoRA](customizing-models-lora.md).
+ **FFT** (Full Fine-Tuning) — Updates all model weights. Higher compute, deeper customization. See [FFT](customizing-models-fft.md).

**Infrastructure options** control *where* your training job runs:
+ **Serverless** — Fully managed, no instance selection. Best for quick experimentation and production jobs without ops overhead. See [Serverless model customization](customize-model.md).
+ **SageMaker AI Training Jobs** — Ephemeral jobs where you select instance type. Uses **Recipes** for pre-configured training. See [SageMaker AI Training Jobs](customizing-models-training-jobs.md).
+ **HyperPod** — Persistent clusters with fault recovery. Uses **Recipes** for distributed training on EKS or Slurm. See [HyperPod](customizing-models-hyperpod.md).

## Choosing your approach
<a name="customizing-models-choosing"></a>

Before fine-tuning, consider whether a simpler approach meets your needs:

Prompt Engineering  
Your model gives acceptable answers but needs better tone, format, or style. No training required — fast iteration. See [Prompt engineering for foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-prompt-engineering.html).

RAG (Retrieval Augmented Generation)  
Your model lacks knowledge about your specific domain. Augment with external knowledge sources without retraining. See [Retrieval Augmented Generation](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html).

Fine-tuning  
Your model needs to consistently learn new behaviors, styles, or domain expertise. Train on your data to change model weights. Continue reading this guide.

## Supported models for fine-tuning
<a name="customizing-models-supported"></a>

The following models are available for customization across serverless, SageMaker AI Training Jobs, and HyperPod infrastructure.


| Provider | Model | Model ID | Serverless | Training Jobs | HyperPod | 
| --- | --- | --- | --- | --- | --- | 
| Alibaba | Qwen3.6 27B | huggingface-vlm-qwen3-6-27b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3.5 27B | huggingface-vlm-qwen3-5-27b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3.5 9B | huggingface-vlm-qwen3-5-9b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3.5 4B | huggingface-vlm-qwen3-5-4b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 32B | huggingface-reasoning-qwen3-32b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 14B | huggingface-reasoning-qwen3-14b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 8B | huggingface-reasoning-qwen3-8b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 4B | huggingface-reasoning-qwen3-4b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 1.7B | huggingface-reasoning-qwen3-1-7b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 0.6B | huggingface-reasoning-qwen3-06b | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 72B | huggingface-llm-qwen2-5-72b-instruct | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 32B | huggingface-llm-qwen2-5-32b-instruct | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 14B | huggingface-llm-qwen2-5-14b-instruct | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 7B | huggingface-llm-qwen2-5-7b-instruct | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 32B | deepseek-llm-r1-distill-qwen-32b | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 14B | deepseek-llm-r1-distill-qwen-14b | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 7B | deepseek-llm-r1-distill-qwen-7b | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 1.5B | deepseek-llm-r1-distill-qwen-1-5b | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Llama 70B | deepseek-llm-r1-distill-llama-70b | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Llama 8B | deepseek-llm-r1-distill-llama-8b | ✓ | ✓ | ✓ | 
| Google | Gemma 4 31B | huggingface-vlm-gemma-4-31b-it | ✓ | ✓ | ✓ | 
| Google | Gemma 4 26B A4B | huggingface-vlm-gemma-4-26b-a4b-it | ✓ | ✓ | ✓ | 
| Google | Gemma 4 E4B | huggingface-vlm-gemma-4-e4b-it | ✓ | ✓ | ✓ | 
| Meta | Llama 3.3 Instruct 70B | meta-textgeneration-llama-3-3-70b-instruct | ✓ | ✓ | ✓ | 
| Meta | Llama 3.2 Instruct 3B | meta-textgeneration-llama-3-2-3b-instruct | ✓ | ✓ | ✓ | 
| Meta | Llama 3.2 Instruct 1B | meta-textgeneration-llama-3-2-1b-instruct | ✓ | ✓ | ✓ | 
| Meta | Llama 3.1 Instruct 8B | meta-textgeneration-llama-3-1-8b-instruct | ✓ | ✓ | ✓ | 
| NVIDIA | Nemotron 3 Super 120B (A12B) | huggingface-llm-nvidia-nemotron-3-super-120b-a12b-bf16 | ✓ | ✓ | ✓ | 
| NVIDIA | Nemotron 3 Nano 30B (A3B) | huggingface-reasoning-nvidia-nemotron-3-nano-30b-a3b-bf16 | ✓ | ✓ | ✓ | 
| OpenAI | GPT OSS 120B | openai-reasoning-gpt-oss-120b | ✓ | ✓ | ✓ | 
| OpenAI | GPT OSS 20B | openai-reasoning-gpt-oss-20b | ✓ | ✓ | ✓ | 

For Amazon Nova models, see the Nova walkthrough under [Serverless model customization](customize-model.md).