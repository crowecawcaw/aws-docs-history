# MLCOST04-BP06 Use managed training capabilities

Machine learning model training can be an iterative,
compute-intensive, and time-consuming process. Instead of using the
notebook itself, which might be running on a small instance,
offloading the training to a managed cluster of compute resources
including both CPUs and GPUs enables more efficient and
cost-effective model training.

**Desired outcome:** By using managed
training capabilities, you optimize your machine learning training
workflows and infrastructure management. You gain access to scalable
computing resources that automatically adjust based on your workload
needs, from single GPUs to thousands, without managing the
underlying infrastructure. You can significantly reduce training
costs through specialized hardware options, compiler optimizations,
and spot instance utilization while maintaining visibility into
metrics and logs for proper monitoring and governance.

**Common anti-patterns:**

- Running complex model training jobs on notebook instances,
  leading to resource constraints and inefficiency.
- Managing your own GPU clusters for training, requiring
  significant operational overhead.
- Using exclusively on-demand instances for training jobs,
  resulting in higher costs.
- Not using specialized training optimizations like distributed
  training or compiler acceleration.

**Benefits of establishing this best
practice:**

- Lower training costs by up to 90% using managed spot instances.
- Accelerate training time by up to 50% with training compiler
  optimizations.
- Scale resources automatically based on training job
  requirements.
- Track and monitor training experiments and resource utilization
  effectively.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning training is computationally intensive and can
become prohibitively expensive when not optimized properly. Using
managed training capabilities allows you to focus on model
development while the infrastructure scales and optimizes
automatically to your needs. Managed training services provide a
range of optimization options from distributed training across
multiple GPUs to cost-saving options through spot instances.
Additionally, these services integrate with monitoring tools to
track resource utilization, model metrics, and training progress
to continually refine your training approach.

For example, when training large language models, you can use
SageMaker AI's distributed training libraries to split the model
across multiple GPUs and instances, reducing training time from
weeks to days while maintaining control over your training costs
through automatic scaling and spot instance usage.

### Implementation steps

1. **Use Amazon SageMaker AI managed
   training capabilities**. Amazon SageMaker AI
   reduces the time and cost to train and tune ML models
   without the need to manage infrastructure. With SageMaker AI, you can train and tune ML models using built-in tools to
   manage and track training experiments, automatically choose
   optimal hyperparameters, debug training jobs, and monitor
   the utilization of system resources such as GPUs, CPUs, and
   network bandwidth. SageMaker AI can automatically scale
   infrastructure up or down based on your training job
   requirements, from one GPU to thousands, or from terabytes
   to petabytes of storage. SageMaker AI also offers the
   highest-performing ML compute infrastructure currently
   available-including
   [Amazon EC2 P4d instances](https://aws.amazon.com/ec2/instance-types/p4/ "https://aws.amazon.com/ec2/instance-types/p4/"), which can reduce ML training costs
   by up to 60% compared with previous generations. And, since
   you pay only for what you use, you can manage your training
   costs more effectively.
2. **Use Spot Instances for cost
   optimization**. Amazon SageMaker AI makes it simple
   to train machine learning models using managed Amazon EC2
   Spot Instances. Managed Spot training can optimize the cost
   of training models up to 90% over On-demand Instances.
   SageMaker AI manages the Spot interruptions on your behalf.
   You can specify which training jobs use Spot Instances and a
   stopping condition that specifies how long SageMaker AI
   waits for a job to run using Spot Instances. Metrics and
   logs generated during training runs are available in Amazon CloudWatch.
3. **Configure optimal data
   sources**. Select the appropriate data source for
   your training job to optimize performance and cost. Consider
   using [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") for persistent storage,
   [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/ "https://aws.amazon.com/fsx/lustre/") for high-performance file systems, or
   [Amazon EFS](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") based on your specific training requirements and
   dataset characteristics.
4. **Implement experiment tracking and
   management**. Use
   [Amazon SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/ "https://aws.amazon.com/sagemaker/ai/experiments/") to track training jobs, compare
   results, and manage different versions of your models. This
   provides visibility into model performance, resource
   utilization, and training metrics to optimize future
   iterations.
5. **Use SageMaker AI HyperPod for
   large-scale training**. Use
   [SageMaker AI
   HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/ "https://aws.amazon.com/sagemaker/ai/hyperpod/") to scale and accelerate generative AI model
   development across thousands of AI accelerators with
   purpose-built infrastructure, automatic checkpoint storage
   and recovery, and support for both Slurm and Amazon EKS for
   cluster orchestration.
6. **For generative AI, optimize large
   language model training**. Use
   [SageMaker AI
   Model Parallelism](../../../sagemaker/latest/dg/model-parallel-v2.md "../../../sagemaker/latest/dg/model-parallel-v2.md") to efficiently distribute model
   parameters across multiple devices and instances. Consider
   using
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") for foundation model access and fine-tuning
   capabilities to further reduce the computational cost of
   training generative AI models from scratch.

## Resources

**Related documents:**

- [SageMaker AI
  HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md")
- [Managed
  Spot Training in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md")
- [Train
  a Model with Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md")
- [Model
  training](../../../sagemaker/latest/dg/train-model.md "../../../sagemaker/latest/dg/train-model.md")
- [Distributed
  training in Amazon SageMaker AI](../../../sagemaker/latest/dg/distributed-training.md "../../../sagemaker/latest/dg/distributed-training.md")
- [Accelerate
  generative AI development with Amazon SageMaker AI and
  MLflow](https://aws.amazon.com/sagemaker/ai/experiments/ "https://aws.amazon.com/sagemaker/ai/experiments/")

**Related examples:**

- [SageMaker AI
  Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples")
- [SageMaker AI
  Training Workshop](https://github.com/aws-samples/amazon-sagemaker-immersion-day "https://github.com/aws-samples/amazon-sagemaker-immersion-day")
