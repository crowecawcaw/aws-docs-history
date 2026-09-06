

# Customization techniques
<a name="customizing-models-techniques"></a>

Customization techniques define *how* your model learns from data. Each technique requires a different dataset format and has its own hyperparameters. Choose based on what data you have and what behavior you want to achieve.
+ **[SFT](customizing-models-sft.md)** (Supervised Fine-Tuning) — Train on labeled prompt-response pairs. Best for teaching a model specific style, format, or domain knowledge.
+ **[DPO](customizing-models-dpo.md)** (Direct Preference Optimization) — Train on preferred vs rejected response pairs. Best for aligning with human preferences and avoiding undesirable outputs.
+ **[RFT](customizing-models-rft.md)** (Reinforcement Fine-Tuning) — Optimize via reward signals: code-based verification (**RLVR**) or an LLM judge (**RLAIF**). Best for improving factual accuracy or subjective quality.
+ **[Multi-turn reinforcement learning](model-customize-mtrl.md)** (Multi-Turn Reinforcement Learning) — Train agents for multi-step agentic tasks with growing context.
+ **[Continuous customization](customizing-models-continuous.md)** (Continuous Customization) — Chain multiple techniques sequentially (for example, SFT → DPO → RLVR). Requires [LoRA](customizing-models-lora.md) training type.

Each technique can be combined with either [LoRA](customizing-models-lora.md) or [FFT](customizing-models-fft.md) training type. See [Training types](customizing-models-training-types.md) for details on choosing between them.