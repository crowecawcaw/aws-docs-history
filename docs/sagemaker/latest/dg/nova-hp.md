# Amazon Nova customization on Amazon SageMaker HyperPod

You can customize Amazon Nova models using [Amazon Nova
recipes](nova-model-recipes.md "nova-model-recipes.md") and train them on Amazon SageMaker HyperPod. A recipe is a YAML configuration file
that provides details to SageMaker AI on how to run your model customization job.

Amazon SageMaker HyperPod offers high-performance computing with optimized GPU instances and
Amazon FSx for Lustre storage, robust monitoring through integration with tools like TensorBoard,
flexible checkpoint management for iterative improvement, seamless deployment to Amazon Bedrock for
inference, and efficient scalable multi-node distributed training-all working together to
provide organizations with a secure, performant, and flexible environment to tailor Nova models
to their specific business requirements.

Amazon Nova customization on Amazon SageMaker HyperPod stores model artifacts including model checkpoints
in a service-managed Amazon S3 bucket. Artifacts in the service-managed bucket are encrypted with
SageMaker-managed AWS KMS keys. Service-managed Amazon S3 buckets don't currently support data encryption
using customer-managed KMS keys. You can use this checkpoint location for evaluation jobs or Amazon Bedrock
inference.

Standard pricing can apply for compute instances, Amazon S3 storage, and FSx for Lustre. For pricing
details, see [SageMaker HyperPod pricing](https://aws.amazon.com/sagemaker-ai/pricing/ "https://aws.amazon.com/sagemaker-ai/pricing/"), [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"), and [FSx for Lustre pricing](https://aws.amazon.com/fsx/lustre/pricing/ "https://aws.amazon.com/fsx/lustre/pricing/").

###### Compute requirements

The following tables summarize the computational requirements for SageMaker HyperPod
training.

| Pre-training                                     | Model  | Sequence length | Nodes          | Instance                             | Accelerator                          |
| ------------------------------------------------ | ------ | --------------- | -------------- | ------------------------------------ | ------------------------------------ | -------------- | --------------------------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------- | ------------------- | -------- | ------------- |
| Amazon Nova Micro                                | 8,192  | 8               | ml.p5.48xlarge | GPU H100                             |
| Amazon Nova Lite                                 | 8,192  | 16              | ml.p5.48xlarge | GPU H100                             |
| Amazon Nova Pro                                  | 8,192  | 24              | ml.p5.48xlarge | GPU H100                             | Direct preference optimization (DPO) | Model          | Sequence length             | Number of nodes             | Instance                    | Accelerator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                              | ---    | ---             | ---            | ---                                  |
| Direct Preference Optimization (Full)            | 32,768 | 2, 4, or 6      | ml.p5.48xlarge | GPU H100                             |
| Direct Preference Optimization (LoRA)            | 32,768 | 2, 4, or 6      | ml.p5.48xlarge | GPU H100                             | Fine-tuning                          | Model          | Sequence length             | Number of nodes             | Instance                    | Accelerator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                              | ---    | ---             | ---            | ---                                  |
| Supervised Fine-Tuning (LoRA)                    | 65,536 | 2               | ml.p5.48xlarge | GPU H100                             |
| Supervised Fine-Tuning (Full)                    | 65,536 | 2               | ml.p5.48xlarge | GPU H100                             |
| Supervised Fine-Tuning (LoRA)                    | 32,768 | 4               | ml.p5.48xlarge | GPU H100                             |
| Supervised Fine-Tuning (Full)                    | 65,536 | 4               | ml.p5.48xlarge | GPU H100                             |
| Supervised Fine-Tuning (LoRA)                    | 65,536 | 6               | ml.p5.48xlarge | GPU H100                             |
| Supervised Fine-Tuning (Full)                    | 65,536 | 6               | ml.p5.48xlarge | GPU H100                             | Distillation                         | Model          | Nodes                       | Instance                    |
| ---                                              | ---    | ---             |                | Model Distillation for Post-Training | 1                                    | ml.r5.24xlarge | Evaluation                  | Model                       | Sequence length             | Nodes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Instance         | Accelerator         |
| ---                                              | ---    | ---             | ---            | ---                                  |
| General Text Benchmark Recipe                    | 8,192  | 1               | ml.p5.48xlarge | GPU H100                             |
| Bring your own dataset (gen_qa) benchmark Recipe | 8,192  | 1               | ml.p5.48xlarge | GPU H100                             |
| Amazon Nova LLM as a Judge Recipe                | 8,192  | 1               | ml.p5.48xlarge | GPU H100                             |
| Standard Text Benchmarks                         | 8,192  | 1               | ml.p5.48xlarge | GPU H100                             |
| Custom Dataset Evaluation                        | 8,192  | 1               | ml.p5.48xlarge | GPU H100                             |
| Multi-Modal Benchmarks                           | 8,192  | 1               | ml.p5.48xlarge | GPU H100                             | Proximal policy optimization         | Model          | Critic Model Instance Count | Reward Model Instance Count | Anchor Model Instance Count | Actor Train                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Actor Generation | Number of Instances | Total Hours Per Run | P5 Hours | Instance Type |
| ---                                              | ---    | ---             | ---            | ---                                  | ---                                  | ---            | ---                         | ---                         | ---                         |
| Amazon Nova Micro                                | 1      | 1               | 1              | 2                                    | 2                                    | 7              | 8                           | 56                          | ml.p5.48xlarge              |
| Amazon Nova Lite                                 | 1      | 1               | 1              | 2                                    | 2                                    | 7              | 16                          | 112                         | ml.p5.48xlarge              |
| Amazon Nova Pro                                  | 1      | 1               | 1              | 6                                    | 2                                    | 11             | 26                          | 260                         | ml.p5.48xlarge              | ###### Topics <br>• [Creating a HyperPod EKS cluster with restricted instance group (RIG)](nova-hp-cluster.md "nova-hp-cluster.md") <br>• [Continued pre-training (CPT)](nova-cpt.md "nova-cpt.md") <br>• [Supervised fine-tuning (SFT)](nova-fine-tune.md "nova-fine-tune.md") <br>• [Direct preference optimization (DPO)](nova-dpo.md "nova-dpo.md") <br>• [Proximal policy optimization (PPO)](nova-ppo.md "nova-ppo.md") <br>• [Starting a training job using the HyperPod CLI](nova-hp-train.md "nova-hp-train.md") <br>• [Evaluating your trained model](nova-hp-evaluate.md "nova-hp-evaluate.md") |
