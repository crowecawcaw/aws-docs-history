# Training types

Training types determine how model weights are updated during customization. Every
[customization technique](customizing-models-techniques.md "customizing-models-techniques.md") (SFT, DPO,
RFT) can be combined with either training type. Choose based on your quality
requirements, compute budget, and use case.

[LoRA](customizing-models-lora.md "customizing-models-lora.md") — Low-Rank Adaptation
Trains a small set of adapter weights. Lower cost, faster training.
Required for [continuous
customization](customizing-models-continuous.md "customizing-models-continuous.md").

[FFT](customizing-models-fft.md "customizing-models-fft.md") — Full Fine-Tuning
Updates all model weights. Higher compute, deeper customization.
Best for large domain shifts.
