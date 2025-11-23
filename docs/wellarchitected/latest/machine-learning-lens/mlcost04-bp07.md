# MLCOST04-BP07 Use distributed training

Accelerate your machine learning model training process by utilizing
distributed computing resources, which can significantly reduce
training time and optimize costs. Amazon SageMaker AI distributed
training capabilities enable efficient processing of large models
and datasets across multiple compute instances.

**Desired outcome:** You achieve
faster training times for your machine learning models by
distributing the workload across multiple instances. You optimize
resource utilization and reduce overall training costs by using
SageMaker AI's managed distributed training capabilities, which
automatically handle infrastructure provisioning and termination
when training completes. This approach allows you to train complex
models that may be too large for a single machine or train standard
models much faster through parallel processing.

**Common anti-patterns:**

- Training large models on a single instance even when they could
  benefit from distribution.
- Manually managing distributed training infrastructure rather
  than using managed services.
- Keeping training instances running after training is complete.
- Implementing custom distributed training code when built-in
  libraries would suffice.

**Benefits of establishing this best
practice:**

- Significantly reduced training time for large models and
  datasets.
- Cost optimization through efficient resource utilization.
- Ability to train models that are too large to fit on a single
  GPU.
- Automatic infrastructure management with no need to maintain
  distributed training clusters.
- Enhanced team productivity by reducing waiting time for model
  results.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Distributed training allows you to split your machine learning
workloads across multiple compute instances to accelerate the
training process. This approach is particularly valuable when
working with large models or datasets that would otherwise take
too long to train on a single instance. Amazon SageMaker AI provides
built-in support for distributed training through its specialized
libraries that handle the complexity of distributing workloads
efficiently.

When implementing distributed training, you need to consider the
most appropriate approach based on your model architecture and
data size. Data parallelism works by dividing your dataset across
multiple GPUs, with each GPU having a complete copy of the model.
This approach is ideal for scenarios where your model fits on a
single GPU but training on the full dataset is time-consuming.
Alternatively, model parallelism is designed for situations where
your model is too large to fit on a single GPU. In this case, the
model itself is partitioned across multiple GPUs.

SageMaker AI's distributed training libraries automatically handle
the communication between nodes and optimize the distribution
strategy, making it straightforward to scale your training
workloads without managing the underlying infrastructure.

### Implementation steps

1. **Evaluate your workload for
   distributed training suitability**. Assess if your
   training job would benefit from distribution by considering
   factors like model size, dataset size, and current training
   times. Ideal candidates are models that take hours or days
   to train on a single instance or models too large to fit in
   a single GPU's memory.
2. **Choose the appropriate distributed
   training approach**. Select between data
   parallelism and model parallelism based on your specific
   needs. Use data parallelism when your model fits on a single
   GPU but you want to process data faster. Use model
   parallelism when your model is too large to fit on a single
   GPU.
3. **Utilize Amazon SageMaker AI distributed
   training libraries**. Implement distributed
   training using
   [SageMaker AI's
   distributed training libraries](https://aws.amazon.com/sagemaker/distributed-training/ "https://aws.amazon.com/sagemaker/distributed-training/"), which automatically
   handle the complexities of distributing workloads across
   multiple instances. These libraries provide optimized
   implementations for both data parallelism and model
   parallelism strategies.
4. **Configure your training
   cluster**. Define the number and type of instances
   for your training cluster in your SageMaker AI training job
   configuration. Consider using GPU-optimized instance types
   like P3, P4d, or G4dn based on your model requirements and
   budget constraints.
5. **Adapt your training script for
   distributed processing**. Modify your training code
   to work with SageMaker AI's distributed training libraries. For
   data parallelism, you'll need to use the SageMaker AI data
   parallelism library to distribute data across workers. For
   model parallelism, you'll integrate the SageMaker AI model
   parallelism library to partition your model across devices.
6. **Monitor and optimize training
   performance**. Use
   [Amazon SageMaker AI Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md") to monitor your distributed
   training jobs, identify bottlenecks, and optimize resource
   utilization. Analyze metrics like GPU utilization,
   communication overhead, and training throughput to fine-tune
   your distributed training configuration.
7. **Consider Amazon SageMaker AI HyperPod
   for persistent training clusters of foundation
   models**. For workloads requiring long-running or
   repeated distributed training jobs, use
   [Amazon SageMaker AI HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md") to create persistent, managed
   clusters that can handle multiple training jobs efficiently
   while maintaining cost optimization through automatic
   scaling and resource management.
8. **Use SageMaker AI HyperPod for
   persistent training clusters**. Use
   [SageMaker AI
   HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md") for workloads requiring long-running or
   repeated distributed training jobs, providing persistent,
   managed clusters with automatic scaling, checkpoint storage
   and recovery, and support for various instance types
   including P5e, G6, and Trn2.
9. **Use AI-powered code generation for
   distributed training implementation**. Use
   AI-powered development tools like
   [Amazon Q Developer](https://aws.amazon.com/q/developer/ "https://aws.amazon.com/q/developer/") and
   [Kiro](https://kiro.ai/ "https://kiro.ai/") to generate
   complex distributed training code, automate infrastructure
   setup scripts, and accelerate the implementation of
   distributed training workflows.
10. **Consider Amazon Bedrock for
    fine-tuning foundation models**. For generative AI
    applications, consider using
    [Amazon
    Bedrock](../../../bedrock/latest/userguide/custom-model-fine-tuning.md "../../../bedrock/latest/userguide/custom-model-fine-tuning.md") for fine-tuning foundation models, model
    distillation, or continued pretraining, which provides
    optimized distributed training capabilities specifically
    designed for large language models.

## Resources

**Related documents:**

- [Run
  distributed training with the SageMaker AI distributed data
  parallelism library](../../../sagemaker/latest/dg/data-parallel.md "../../../sagemaker/latest/dg/data-parallel.md")
- [SageMaker AI
  model parallelism library v2](../../../sagemaker/latest/dg/model-parallel-v2.md "../../../sagemaker/latest/dg/model-parallel-v2.md")
- [Amazon SageMaker AI HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md")
- [Distributed
  Training](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/index.html "https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/index.html")
- [Amazon SageMaker AI XGBoost now offers fully distributed GPU
  training](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/")

**Related examples:**

- [Distributed
  Training](https://github.com/aws/amazon-sagemaker-examples/blob/master/training/distributed_training/index.rst "https://github.com/aws/amazon-sagemaker-examples/blob/master/training/distributed_training/index.rst")
- [Distributed
  training using Amazon SageMaker AI Distributed Data Parallel
  library and debugging using Amazon SageMaker AI Debugger](https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger "https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger")
- [SageMaker AI
  developer guide on distributed training](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/distributed-training.md#distributed-training-optimize "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/distributed-training.md#distributed-training-optimize")
- [Distributed
  Training Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training "https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training")
