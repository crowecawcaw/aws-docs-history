# Continued pre-training (CPT)

Continued Pre-Training (CPT) is a technique that extends a pre-trained language model's capabilities by training it on new domain-specific data while preserving its general language understanding. Unlike fine-tuning, CPT uses the same unsupervised objectives as the original pre-training (such as masked or causal language modeling) and doesn't modify the model's architecture.

CPT is particularly valuable when you have large amounts of unlabeled domain-specific data (like medical or financial text) and want to improve the model's performance in specialized areas without losing its general capabilities. This approach enhances zero-shot and few-shot performance in targeted domains without requiring extensive task-specific fine-tuning.

For detailed instructions about using CPT with Amazon Nova model customization, see the [Continued Pre-Training (CPT)](../../../sagemaker/latest/dg/nova-cpt.md "../../../sagemaker/latest/dg/nova-cpt.md") section from SageMaker user guide.
