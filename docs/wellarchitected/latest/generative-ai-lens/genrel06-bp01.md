# GENREL06-BP01 Design for fault-tolerance for high-performance

distributed computation tasks

Fault-tolerant infrastructure identifies issues in long-running,
high-performance distributed computation tasks and remediates them
before they can disrupt the task. Because these tasks are expensive
and time-consuming, use fault-tolerant infrastructure to reliably
perform model customization jobs.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
model customization workloads, automating recovery during
fine-tuning, pre-training, and other model customization workloads.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](../framework/rel-dp.md "../framework/rel-dp.md") - Fault-tolerant infrastructure can
automatically recover from failure, improving the reliability of
long-running, high-performance, distributed computation tasks like
model customization.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model pre-training, continuous pre-training, fine-tuning, and
distillation are some of the many high-performance distributed
computation tasks sometimes required to optimize foundation models
for generative AI workloads. These tasks require the orchestration
of dozens or hundreds of virtual machines, running workloads over
days, weeks, months or longer. These tasks are particularly
susceptible to disruptions, which could delay or stop training
progress. Consider a managed or automated process that provisions
and orchestrates the infrastructure on your behalf, handles
errors, and preserves the workload's integrity.

Amazon SageMaker AI HyperPod clusters allow customers to pre-train or
fine-tune large language models using managed infrastructure.
Amazon EC2 UltraClusters facilitate large language model hosting
for purpose-built machine learning accelerators. Additionally,
Amazon Bedrock offers managed fine-tuning, continuous
pre-training, or model distillation for a selection of third-party
models.

When implementing fault-tolerant distributed training manually,
evaluate options that can recover the training and customization
progress. Create training job recovery points by checkpointing
model training. Keep track of training progress, and determine
when to halt training based on observed metrics. Consider
leveraging performant storage solutions (like Amazon FSx for Lustre) that provide distributed compute tasks rapid access to
large data volumes at scale. Managed training and model
customization solutions provide these capabilities, but you can
also consider self-hosting for some model training and
customization initiatives.

### Implementation steps

1. In Amazon Bedrock, when using custom models:
   - Select a model customization job like fine-tuning or
     continued pre-training.
   - Follow the prompts to begin executing the job.
   - Test the output once the job has completed.

2. Alternatively, provision SageMaker AI HyperPod or EC2
   UltraClusters.
3. Configure object store for workload checkpointing.
4. Provision high performance Amazon FSx for Lustre containing
   your training and customization data.

## Resources

**Related practices:**

- [REL10-BP02](../reliability-pillar/rel_fault_isolation_single_az_system.md "../reliability-pillar/rel_fault_isolation_single_az_system.md")
- [REL11-BP01](../reliability-pillar/rel_withstand_component_failures_monitoring_health.md "../reliability-pillar/rel_withstand_component_failures_monitoring_health.md")
- [REL11-BP03](../reliability-pillar/rel_withstand_component_failures_auto_healing_system.md "../reliability-pillar/rel_withstand_component_failures_auto_healing_system.md")

**Related guides, videos, and documentation:**

- [Amazon SageMaker AI HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md")
- [Customize
  your model to improve its performance for your use case](../../../bedrock/latest/userguide/custom-models.md "../../../bedrock/latest/userguide/custom-models.md")

**Related examples:**

- [Speed
  up training on Amazon SageMaker AI using Amazon FSx for Lustre
  and Amazon EFS file systems](https://aws.amazon.com/blogs/machine-learning/speed-up-training-on-amazon-sagemaker-using-amazon-efs-or-amazon-fsx-for-lustre-file-systems/ "https://aws.amazon.com/blogs/machine-learning/speed-up-training-on-amazon-sagemaker-using-amazon-efs-or-amazon-fsx-for-lustre-file-systems/")
- [Customize
  models in Amazon Bedrock with your own data using fine-tuning
  and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/ "https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/")
- [Amazon BedrockModel Customization Workshop Notebooks](https://github.com/aws-samples/amazon-bedrock-customization-workshop "https://github.com/aws-samples/amazon-bedrock-customization-workshop")
- [Amazon SageMaker AI Hyperpod Recipes](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes")
- [Introducing Amazon SageMaker AI HyperPod: a purpose-built infrastructure for distributed training
  at scale](https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-hyperpod-a-purpose-built-infrastructure-for-distributed-training-at-scale/ "https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-hyperpod-a-purpose-built-infrastructure-for-distributed-training-at-scale/")
