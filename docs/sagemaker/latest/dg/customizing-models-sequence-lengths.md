

# Supported sequence lengths for open weight model serverless customization
<a name="customizing-models-sequence-lengths"></a>

The following table shows the maximum sequence lengths (in tokens) supported for serverless customization of open weight models. For more information about serverless customization of open weight models, see [Open weight model customization](model-customize-open-weight.md). For each open weight model, each populated cell shows the maximum sequence length that you can set for that customization technique and training type by using the overridable sequence-length parameters.

## How to think about sequence length
<a name="customizing-models-sequence-lengths-how-to"></a>

The sequence length is the sum of the prompt length and the response length, and you set them independently:
+ **SFT and DPO** – Set `dataset_max_len` (the full prompt and completion length) up to the maximum in the following table.
+ **RLVR and RLAIF (GRPO)** – Set `max_prompt_length` (input budget) and `max_response_length` (generation budget). Their sum must stay within the model's maximum in the following table.

Keep the following tips in mind:
+ Response length can affect quality for tasks that require extended generation, such as coding or mathematical reasoning. Allocate enough `max_response_length` for the expected output while reserving sufficient `max_prompt_length` for the input.
+ Longer sequences can increase memory and compute requirements per example. Actual training time and cost depend on factors such as batching, packing, hardware utilization, and the training configuration.
+ The maximums in the following table are current ceilings. You can set any value up to that ceiling.


| Provider | Model | Model ID | SFT (LoRA) | SFT (FFT) | DPO (LoRA) | DPO (FFT) | RLVR (LoRA) | RLVR (FFT) | RLAIF (LoRA) | RLAIF (FFT) | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Alibaba | Qwen3.8 27B | huggingface-vlm-qwen3-8-27b | 16K | 16K | 16K | 16K | 16K | 8K | 16K | 8K | 
| Alibaba | Qwen3.6 27B | huggingface-vlm-qwen3-6-27b | 16K | 16K | 16K | 16K | 16K | 8K | 16K | 8K | 
| Alibaba | Qwen3.6 A3B 35B | huggingface-vlm-qwen3-6-35b-a3b | 32K | 16K | — | — | 16K | 16K | 16K | 16K | 
| Alibaba | Qwen3.5 27B | huggingface-vlm-qwen3-5-27b | 16K | 16K | 16K | 16K | 32K | 8K | 32K | 8K | 
| Alibaba | Qwen3.5 9B | huggingface-vlm-qwen3-5-9b | 16K | 16K | 16K | 16K | 32K | 16K | 32K | 16K | 
| Alibaba | Qwen3.5 4B | huggingface-vlm-qwen3-5-4b | 16K | 16K | 16K | 16K | 32K | 16K | 32K | 16K | 
| Alibaba | Qwen3 32B | huggingface-reasoning-qwen3-32b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 16K | 
| Alibaba | Qwen3 14B | huggingface-reasoning-qwen3-14b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 32K | 8K | 
| Alibaba | Qwen3 8B | huggingface-reasoning-qwen3-8b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| Alibaba | Qwen3 4B | huggingface-reasoning-qwen3-4b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| Alibaba | Qwen3 1.7B | huggingface-reasoning-qwen3-1-7b | \*4K | \*4K | \*4K | \*4K | 16K | 32K | 16K | 8K | 
| Alibaba | Qwen3 0.6B | huggingface-reasoning-qwen3-06b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| Alibaba | Qwen2.5 Instruct 72B | huggingface-llm-qwen2-5-72b-instruct | \*4K | \*4K | \*4K | — | 16K | — | 16K | — | 
| Alibaba | Qwen2.5 Instruct 32B | huggingface-llm-qwen2-5-32b-instruct | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| Alibaba | Qwen2.5 Instruct 14B | huggingface-llm-qwen2-5-14b-instruct | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 16K | 
| Alibaba | Qwen2.5 Instruct 7B | huggingface-llm-qwen2-5-7b-instruct | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| DeepSeek | R1 Distill Qwen 32B | deepseek-llm-r1-distill-qwen-32b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| DeepSeek | R1 Distill Qwen 14B | deepseek-llm-r1-distill-qwen-14b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| DeepSeek | R1 Distill Qwen 7B | deepseek-llm-r1-distill-qwen-7b | \*4K | \*4K | \*4K | \*4K | 16K | 32K | 16K | 8K | 
| DeepSeek | R1 Distill Qwen 1.5B | deepseek-llm-r1-distill-qwen-1-5b | \*4K | \*4K | \*4K | \*4K | 16K | — | 16K | 8K | 
| DeepSeek | R1 Distill Llama 70B | deepseek-llm-r1-distill-llama-70b | \*4K | \*4K | \*4K | — | 16K | — | 16K | — | 
| DeepSeek | R1 Distill Llama 8B | deepseek-llm-r1-distill-llama-8b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| Google | Gemma 4 31B | huggingface-vlm-gemma-4-31b-it | 32K | 32K | 32K | 32K | 16K | 16K | 16K | 16K | 
| Google | Gemma 4 26B A4B | huggingface-vlm-gemma-4-26b-a4b-it | 32K | 32K | 32K | 32K | 16K | 16K | 16K | 16K | 
| Google | Gemma 4 E4B | huggingface-vlm-gemma-4-e4b-it | 32K | 32K | 32K | 32K | 16K | 16K | 16K | 16K | 
| Meta | Llama 3.3 Instruct 70B | meta-textgeneration-llama-3-3-70b-instruct | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 
| Meta | Llama 3.2 Instruct 3B | meta-textgeneration-llama-3-2-3b-instruct | \*4K | — | \*4K | — | 16K | — | 16K | — | 
| Meta | Llama 3.2 Instruct 1B | meta-textgeneration-llama-3-2-1b-instruct | \*4K | — | \*4K | — | 16K | — | 16K | — | 
| Meta | Llama 3.1 Instruct 8B | meta-textgeneration-llama-3-1-8b-instruct | \*4K | — | \*4K | — | 16K | — | 16K | — | 
| Mistral AI | Ministral 3 Instruct 2512 BF16 14B | huggingface-vlm-ministral-3-14b-instruct-2512-bf16 | 16K | 16K | 16K | 16K | 16K | 16K | 16K | 16K | 
| Mistral AI | Ministral 3 Instruct 2512 BF16 8B | huggingface-vlm-ministral-3-8b-instruct-2512-bf16 | 16K | 16K | 16K | 16K | 32K | 16K | 32K | 16K | 
| Mistral AI | Ministral 3 Instruct 2512 BF16 3B | huggingface-vlm-ministral-3-3b-instruct-2512-bf16 | 16K | 16K | 16K | 16K | 32K | 32K | 32K | 32K | 
| NVIDIA | Nemotron 3 Super 120B (A12B) | huggingface-llm-nvidia-nemotron-3-super-120b-a12b-bf16 | 16K | — | 8K | — | 8K | — | 16K | — | 
| NVIDIA | Nemotron 3 Nano 30B (A3B) | huggingface-reasoning-nvidia-nemotron-3-nano-30b-a3b-bf16 | 32K | 16K | 8K | 16K | 16K | 16K | 16K | 16K | 
| NVIDIA | Nemotron 3.5 Lightning 30B (A3B) | huggingface-reasoning-nemotron-3-5-lightning-30b-a3b-bf16 | 16K | 16K | 8K | 16K | 16K | 16K | 16K | 16K | 
| OpenAI | GPT OSS 120B | openai-reasoning-gpt-oss-120b | \*4K | — | \*4K | — | 32K | — | 32K | — | 
| OpenAI | GPT OSS 20B | openai-reasoning-gpt-oss-20b | \*4K | \*4K | \*4K | \*4K | 16K | 8K | 16K | 8K | 

In the preceding table, `*` means the sequence length is fixed at 4K and is not overridable. An em dash (—) means that the technique and training type are not supported for serverless customization on that model.