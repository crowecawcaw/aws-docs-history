

# Open weight model customization
<a name="model-customize-open-weight"></a>

This section walks you through the process to get started with open weight model customization.

**Topics**
+ [Supported models and customization types](#model-customize-open-weight-supported-models)
+ [Prerequisites](model-customize-open-weight-prereq.md)
+ [Creating assets for model customization in the UI](model-customize-open-weight-create-assets-ui.md)
+ [AI model customization job submission](model-customize-open-weight-job.md)
+ [Model evaluation job submission](model-customize-open-weight-evaluation.md)
+ [Model deployment](model-customize-open-weight-deployment.md)
+ [Sample datasets and evaluators](model-customize-open-weight-samples.md)

## Supported models and customization types
<a name="model-customize-open-weight-supported-models"></a>

The following table shows the supported fine-tuning recipes for each model, including SFT, DPO, RLVR, and RLAIF with LoRA or full fine-tuning (FFT).


| Provider | Model | Model ID | SFT (LoRA) | SFT (FFT) | DPO (LoRA) | DPO (FFT) | RLVR (LoRA) | RLVR (FFT) | RLAIF (LoRA) | RLAIF (FFT) | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Alibaba | Qwen3.6 27B | huggingface-vlm-qwen3-6-27b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3.5 27B | huggingface-vlm-qwen3-5-27b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3.5 9B | huggingface-vlm-qwen3-5-9b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3.5 4B | huggingface-vlm-qwen3-5-4b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 32B | huggingface-reasoning-qwen3-32b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 14B | huggingface-reasoning-qwen3-14b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 8B | huggingface-reasoning-qwen3-8b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 4B | huggingface-reasoning-qwen3-4b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen3 1.7B | huggingface-reasoning-qwen3-1-7b | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | 
| Alibaba | Qwen3 0.6B | huggingface-reasoning-qwen3-06b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 72B | huggingface-llm-qwen2-5-72b-instruct | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |  | 
| Alibaba | Qwen2.5 Instruct 32B | huggingface-llm-qwen2-5-32b-instruct | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 14B | huggingface-llm-qwen2-5-14b-instruct | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Alibaba | Qwen2.5 Instruct 7B | huggingface-llm-qwen2-5-7b-instruct | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 32B | deepseek-llm-r1-distill-qwen-32b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 14B | deepseek-llm-r1-distill-qwen-14b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 7B | deepseek-llm-r1-distill-qwen-7b | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | 
| DeepSeek | R1 Distill Qwen 1.5B | deepseek-llm-r1-distill-qwen-1-5b | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | 
| DeepSeek | R1 Distill Llama 70B | deepseek-llm-r1-distill-llama-70b | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |  | 
| DeepSeek | R1 Distill Llama 8B | deepseek-llm-r1-distill-llama-8b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Google | Gemma 4 31B | huggingface-vlm-gemma-4-31b-it | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Google | Gemma 4 26B A4B | huggingface-vlm-gemma-4-26b-a4b-it | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Google | Gemma 4 E4B | huggingface-vlm-gemma-4-e4b-it | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Meta | Llama 3.3 Instruct 70B | meta-textgeneration-llama-3-3-70b-instruct | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Meta | Llama 3.2 Instruct 3B | meta-textgeneration-llama-3-2-3b-instruct | ✓ |  | ✓ |  | ✓ |  | ✓ |  | 
| Meta | Llama 3.2 Instruct 1B | meta-textgeneration-llama-3-2-1b-instruct | ✓ |  | ✓ |  | ✓ |  | ✓ |  | 
| Meta | Llama 3.1 Instruct 8B | meta-textgeneration-llama-3-1-8b-instruct | ✓ |  | ✓ |  | ✓ |  | ✓ |  | 
| NVIDIA | Nemotron 3 Super 120B (A12B) | huggingface-llm-nvidia-nemotron-3-super-120b-a12b-bf16 | ✓ |  |  |  | ✓ |  | ✓ |  | 
| NVIDIA | Nemotron 3 Nano 30B (A3B) | huggingface-reasoning-nvidia-nemotron-3-nano-30b-a3b-bf16 | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | 
| OpenAI | GPT OSS 120B | openai-reasoning-gpt-oss-120b | ✓ |  | ✓ |  | ✓ |  | ✓ |  | 
| OpenAI | GPT OSS 20B | openai-reasoning-gpt-oss-20b | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 