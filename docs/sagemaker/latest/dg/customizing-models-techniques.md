

# Customization techniques
<a name="customizing-models-techniques"></a>

Customization techniques define *how* your model learns from data. Each technique requires a different dataset format and has its own hyperparameters. Choose based on what data you have and what behavior you want to achieve.

For Python SDK examples, see the example section in each technique page and [Serverless trainers](customizing-models-access.md#access-serverless-trainers).
+ **[SFT](customizing-models-sft.md)** (Supervised Fine-Tuning) — Train on labeled prompt-response pairs. Best for teaching a model specific style, format, or domain knowledge. For the expected training data structure, see [Dataset format](customizing-models-sft.md#customizing-models-sft-dataset).
+ **[DPO](customizing-models-dpo.md)** (Direct Preference Optimization) — Train on preferred vs rejected response pairs. Best for aligning with human preferences and avoiding undesirable outputs. For dataset requirements, see [Dataset format](customizing-models-dpo.md#customizing-models-dpo-dataset).
+ **[RFT](customizing-models-rft.md)** (Reinforcement Fine-Tuning) — Optimize via reward signals: code-based verification (**RLVR**) or an LLM judge (**RLAIF**). Best for improving factual accuracy or subjective quality. For RLVR dataset requirements, see [Dataset format](customizing-models-rft.md#rlvr-dataset-format). For RLAIF dataset requirements, see [Dataset format](customizing-models-rft.md#rlaif-dataset-format).
+ **[Sequence lengths](customizing-models-sequence-lengths.md)** — Maximum sequence lengths supported for each open weight model, technique, and training type in serverless customization.
+ **[Multi-turn reinforcement learning](model-customize-mtrl.md)** (Multi-Turn Reinforcement Learning) — Train agents for multi-step agentic tasks with growing context. For setup requirements, see [Prerequisites](model-customize-mtrl-prereqs.md).
+ **[Continuous customization](customizing-models-continuous.md)** (Continuous Customization) — Chain multiple techniques sequentially (for example, SFT → DPO → RLVR). Requires [LoRA](customizing-models-lora.md) training type.
+ **[Distillation](customizing-models-distillation.md)** — Transfer knowledge from a *teacher* model to a *student* model. Best when you have a specific high-volume task that the student can be trained on. When the student is smaller than the teacher, you also get lower inference latency of the student model.

Each technique can be combined with either [LoRA](customizing-models-lora.md) or [FFT](customizing-models-fft.md) training type. See [Training types](customizing-models-training-types.md) for details on choosing between them.


| Technique | Dataset format | SDK trainer | FFT | Notes | 
| --- | --- | --- | --- | --- | 
| [SFT](customizing-models-sft.md) | messages or prompt/completion JSONL | SFTTrainer | Yes | LoRA and FFT use the same dataset schema. See [Dataset format](customizing-models-sft.md#customizing-models-sft-dataset). | 
| [DPO](customizing-models-dpo.md) | chosen/rejected message pairs or prompt/chosen/rejected JSONL | DPOTrainer | Yes | LoRA and FFT use the same dataset schema. See [Dataset format](customizing-models-dpo.md#customizing-models-dpo-dataset). | 
| RLVR | prompt with reward\_model metadata JSONL | RLVRTrainer | Yes | LoRA and FFT use the same dataset schema. See [Dataset format](customizing-models-rft.md#rlvr-dataset-format). | 
| RLAIF | prompt with LLM-judge reward\_model metadata JSONL | RLAIFTrainer | Yes | LoRA and FFT use the same dataset schema. See [Dataset format](customizing-models-rft.md#rlaif-dataset-format). | 
| [Multi-turn reinforcement learning](model-customize-mtrl.md) | prompt column in Parquet, JSONL, JSON, or CSV | MultiTurnRLTrainer | No | MTRL training uses prompt datasets and a multi-turn agent environment. See [Prompt dataset format](model-customize-mtrl-assets.md#model-customize-mtrl-assets-prompt-dataset-format) and [SageMaker AI Python SDK](model-customize-mtrl-job.md#model-customize-mtrl-job-sdk). | 