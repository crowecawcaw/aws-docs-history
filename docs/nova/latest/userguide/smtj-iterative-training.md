# Iterative training

Iterative training is a systematic approach to fine-tuning models through multiple training cycles, where each round builds on the previous checkpoint by addressing specific weaknesses discovered through evaluation. This method enables targeted improvements to model performance by incorporating curated examples that address failure modes, adapting to changing requirements, and validating enhancements incrementally rather than committing to a single long training run. The process typically follows patterns like SFT (Supervised Fine-Tuning) followed by RFT (Reward-based Fine-Tuning), with checkpoints stored in AWS-managed escrow S3 buckets that can be referenced for subsequent training iterations while maintaining consistency in model type and training technique throughout the pipeline.

For more details, refer to [Iterative Training](nova-iterative-training.md "nova-iterative-training.md").
