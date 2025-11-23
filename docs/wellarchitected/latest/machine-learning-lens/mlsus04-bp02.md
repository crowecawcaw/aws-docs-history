# MLSUS04-BP02 Select energy-efficient algorithms

Choosing energy-efficient algorithms minimizes resource usage while
maintaining performance, reducing your machine learning workloads'
environmental impact and operational costs.

**Desired outcome:** You establish a
systematic approach for selecting and optimizing algorithms that
deliver the necessary performance while minimizing computational
resources. Your ML workloads run more efficiently, reducing energy
consumption, carbon footprint, and infrastructure costs without
significant performance degradation.

**Common anti-patterns:**

- Defaulting to the most complex algorithm without evaluating
  simpler alternatives.
- Ignoring model compression techniques that could reduce resource
  requirements.
- Overlooking the environmental impact of computational resources.
- Focusing solely on model accuracy without considering resource
  efficiency.

**Benefits of establishing this best
practice:**

- Reduced energy consumption and carbon footprint.
- Faster inference times and improved user experience.
- Ability to deploy ML models on resource-constrained devices.
- Extended battery life for edge devices running ML workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Energy-efficient algorithm selection requires balancing model
performance with resource consumption. When developing machine
learning models, computational efficiency directly impacts
sustainability and cost. Starting with simpler algorithms provides
a baseline for comparison and often delivers sufficient results
without excessive resource demands. Modern approaches like model
distillation, pruning, and quantization enable you to achieve
near-equivalent results using significantly fewer resources.

The environmental impact of ML workloads increases with model
complexity, making optimization techniques essential for
sustainable AI development. By systematically evaluating algorithm
efficiency alongside performance metrics, you can make informed
decisions that reduce your carbon footprint while maintaining
service quality.

### Implementation steps

1. **Begin with a simple algorithm to
   establish a baseline:** Start your development
   process with straightforward algorithms that provide a
   reference point for performance and resource usage. Then
   [test
   different algorithms with increasing complexity](mlper-07.md "mlper-07.md") to
   observe whether performance improvements justify additional
   resource consumption. Measure both model accuracy and
   resource utilization metrics to make informed decisions
   about complexity trade-offs.
2. **Explore simplified versions of
   popular algorithms:** Research and implement
   distilled or optimized versions of standard algorithms that
   deliver similar performance with reduced computational
   requirements. For example, DistilBERT, a distilled version
   of
   [BERT](<https://en.wikipedia.org/wiki/BERT_(language_model)> "https://en.wikipedia.org/wiki/BERT_(language_model)"),
   has 40% fewer parameters, runs 60% faster, and preserves 97%
   of its performance. Similar approaches exist for many common
   model architectures.
3. **Implement model compression
   techniques:** Apply pruning to remove model weights
   that contribute minimally to predictions, reducing model
   size and computational requirements. Use quantization to
   represent numerical values with lower precision,
   significantly decreasing memory usage and processing demands
   while maintaining acceptable accuracy levels.
4. **Leverage AWS optimization
   services:** Deploy
   [Amazon SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md") to automatically optimize your ML
   models for inference on cloud resources and edge devices.
   SageMaker AI Neo analyzes your model and generates optimized
   code that maximizes performance while minimizing resource
   consumption, allowing you to deploy more efficient models
   across diverse deployment targets.
5. **Monitor and optimize resource
   utilization:** Track the
   [resources
   provisioned](../../../sagemaker/latest/APIReference/API_ResourceConfig.md "../../../sagemaker/latest/APIReference/API_ResourceConfig.md") for your training and inference jobs
   (InstanceCount, InstanceType, and VolumeSizeInGB) and their
   [efficient
   use](../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs "../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs") (CPUUtilization, GPUUtilization,
   GPUMemoryUtilization, MemoryUtilization, and
   DiskUtilization) through the
   [SageMaker AI
   Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm"),
   [CloudWatch
   Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw") or your
   [SageMaker AI
   Debugger Profiling Report](../../../sagemaker/latest/dg/debugger-profiling-report.md#debugger-profiling-report-walkthrough-system-usage "../../../sagemaker/latest/dg/debugger-profiling-report.md#debugger-profiling-report-walkthrough-system-usage"). Use these insights to
   right-size your resources and identify optimization
   opportunities.
6. **Consider hardware-specific
   optimizations:** Choose appropriate instance types
   for training and inference based on your model's
   characteristics. Some algorithms perform better on GPU
   instances, while others may be more efficient on CPU or
   specialized accelerators like AWS Inferentia. Matching your
   algorithm to the optimal hardware can significantly improve
   energy efficiency.
7. **Use optimized foundation model
   containers:** Deploy models using SageMaker AI's
   optimized foundation model containers that include
   pre-configured environments with built-in quantization and
   optimization techniques. These containers support frameworks
   like Hugging Face Transformers and provide automatic
   performance optimizations.
8. **Use AI-powered code generation for
   algorithm optimization**. Use AI-powered
   development tools like
   [Amazon Q Developer](https://aws.amazon.com/q/developer/ "https://aws.amazon.com/q/developer/") and
   [Kiro](https://kiro.ai/ "https://kiro.ai/") to generate
   optimized algorithm implementations, automate model
   compression code, and accelerate the development of
   energy-efficient ML solutions.
9. **Apply efficient architectures for
   foundation models:** When working with generative
   AI models, consider parameter-efficient fine-tuning
   approaches like LoRA (Low-Rank Adaptation) or P-tuning
   instead of full fine-tuning. These techniques can reduce the
   computational resources required while achieving comparable
   performance. Leverage pre-trained foundation models
   available through SageMaker AI JumpStart to avoid the
   energy-intensive process of training from scratch.

## Resources

**Related documents:**

- [SageMaker AI
  JumpStart pretrained models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
- [Multi-model
  endpoints](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md")
- [Model
  performance optimization with SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")
- [The
  AWS Inferentia Chip With DLAMI](../../../dlami/latest/devguide/tutorial-inferentia.md "../../../dlami/latest/devguide/tutorial-inferentia.md")
- [Prepare
  Model for Compilation](../../../sagemaker/latest/dg/neo-compilation-preparing-model.md "../../../sagemaker/latest/dg/neo-compilation-preparing-model.md")
- [Optimize
  AI/ML workloads for sustainability: Part 2, model
  development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/")

**Related videos:**

- [Deploy
  an ML model for best performance, cost, and prediction
  quality](https://www.youtube.com/watch?v=ftCFf57dQQY "https://www.youtube.com/watch?v=ftCFf57dQQY")
- [SageMaker AI
  HyperPod: Revolutionizing Foundation Model Training with
  Resilience and Performance](https://aws.amazon.com/awstv/watch/c60e1437f63/ "https://aws.amazon.com/awstv/watch/c60e1437f63/")
