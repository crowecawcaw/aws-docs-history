# MLCOST04-BP01 Select optimal computing instance size

Right size your machine learning training instances according to the
algorithm and workload requirements to maximize efficiency and
reduce costs. By selecting the most appropriate computing resources,
you can improve performance while minimizing unnecessary expenses.

**Desired outcome:** You can identify
and select the optimal computing instance types for your machine
learning workloads based on actual resource utilization metrics. You
can systematically evaluate different instance options, understand
their cost implications, and optimize your machine learning
infrastructure spending while maintaining or improving performance.

**Common anti-patterns:**

- Using oversized instances for training jobs regardless of model
  complexity.
- Ignoring resource utilization metrics during training.
- Failing to experiment with different instance types to find the
  optimal cost-performance balance.
- Not considering the communication overhead in distributed
  training scenarios.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs for machine learning workloads.
- Improved resource utilization and efficiency.
- Better understanding of ML workload performance characteristics.
- Optimization of price-performance ratio for different model
  types.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning training workloads vary significantly in their
resource requirements based on model complexity, dataset size, and
algorithm characteristics. Simple models might not train faster on
larger instances because they cannot effectively utilize
additional compute resources, and might even train slower due to
high GPU communication overhead. By evaluating your workload's
resource needs, you can identify the most cost-effective instance
configuration.

The key to optimizing instance selection is understanding the
actual resource utilization patterns of your machine learning
workloads. Start with smaller instances and scale up only when
necessary based on performance data. Amazon SageMaker AI provides
tools like Debugger to monitor resource utilization and
Experiments to compare training performance across different
instance configurations. This data-driven approach assists you to
avoid paying for unused resources while maintaining optimal
training performance.

### Implementation steps

1. **Understand your algorithm's resource
   requirements**. Begin by analyzing whether your
   machine learning algorithm is compute-bound, memory-bound,
   or I/O-bound. Different algorithms have different scaling
   characteristics and resource needs. For deep learning
   workloads, consider whether GPU acceleration would provide
   significant benefits or if CPU instances would be more
   cost-effective for your specific model.
2. **Use Amazon SageMaker AI
   Experiments**.
   [Amazon EC2](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") provides a wide selection of instance types
   optimized to fit different use cases. Machine learning
   workloads can use either a CPU or a GPU instance. Select an
   instance type from
   [the
   available EC2 instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") depending on the needs
   of your ML algorithm. Experiment with both CPU and GPU
   instances to learn which one gives you the best cost
   configuration. Amazon SageMaker AI lets you use a single
   instance or a distributed cluster of GPU instances. Use
   [Amazon SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/ "https://aws.amazon.com/sagemaker/ai/experiments/") to evaluate alternative
   options, and identify the size resulting in optimal outcome.
   With the pricing broken down by time and resources, you can
   optimize the cost of Amazon SageMaker AI and only pay for
   what is needed.
3. **Use Amazon SageMaker AI
   Debugger**.
   [Amazon SageMaker AI Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md") automatically monitors the
   utilization of system resources, such as GPUs, CPUs,
   network, and memory, and profiles your training jobs to
   collect detailed ML framework metrics. You can inspect
   resource metrics visually through SageMaker AI Studio and
   take corrective actions if the resource is under-utilized to
   optimize cost.
4. **Start small and scale
   gradually**. Begin with smaller instance sizes for
   new models and monitor performance. Only increase instance
   size when you have data showing that your workload can
   benefit from additional resources. This approach assists you
   to avoid overprovisioning and unnecessary costs.
5. **Consider the communication
   overhead**. For distributed training across
   multiple GPUs or instances, evaluate the communication
   overhead between nodes. In some cases, adding more compute
   resources might actually slow down training due to increased
   coordination requirements.
6. **Monitor and analyze training
   metrics**. Track key metrics like CPU/GPU
   utilization, memory usage, I/O patterns, and training
   throughput across different instance types to identify
   bottlenecks and optimization opportunities.
7. **Use Spot Instances for cost
   savings**. For non-critical training jobs, consider
   using
   [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/ "https://aws.amazon.com/ec2/spot/") through SageMaker AI to reduce costs
   by up to 90%. Configure your training jobs to checkpoint
   regularly to minimize the impact of potential interruptions.
8. **Use SageMaker AI Inference Recommender
   for optimal instance selection**. Use
   [SageMaker AI
   Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") with enhanced algorithms and
   support for multi-model endpoints to get sophisticated cost
   optimization recommendations for your specific workloads.
9. **For generative AI workloads, use
   foundation model optimization techniques**. For
   generative AI workloads, consider techniques like
   quantization, distillation, and efficient fine-tuning
   methods to reduce the computational resources needed while
   maintaining model quality.
   [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") provides optimized foundation
   models that can significantly reduce training time and
   resource requirements.

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md")
- [Accelerate
  generative AI development with Amazon SageMaker AI and
  MLflow](https://aws.amazon.com/sagemaker/ai/experiments/ "https://aws.amazon.com/sagemaker/ai/experiments/")
- [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/")
- [Managed
  Spot Training in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md")
- [Amazon SageMaker AI Training Compiler](../../../sagemaker/latest/dg/training-compiler.md "../../../sagemaker/latest/dg/training-compiler.md")
