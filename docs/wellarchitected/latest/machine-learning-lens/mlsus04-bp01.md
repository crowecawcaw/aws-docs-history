# MLSUS04-BP01 Define sustainable performance criteria

Creating machine learning models that balance accuracy with
environmental impact is essential for sustainable AI development.
When we focus exclusively on model accuracy, we overlook the
economic, environmental, and social costs of achieving marginal
performance improvements. Since the relationship between model
accuracy and complexity is logarithmic at best, continuing to train
a model longer or searching extensively for better hyperparameters
often yields only minimal gains while significantly increasing
resource consumption.

**Desired outcome:** You establish
balanced performance criteria for your ML models that satisfy your
business requirements without excessive resource usage. You
implement mechanisms to optimize training efficiency, reducing
carbon footprint and costs while maintaining appropriate model
performance. Your machine learning lifecycle incorporates
sustainability as a core consideration alongside traditional metrics
like accuracy.

**Common anti-patterns:**

- Pursuing maximum model accuracy without considering
  environmental impact.
- Using oversized models when smaller models would be sufficient.
- Allowing training jobs to run indefinitely with minimal
  performance improvements.
- Ignoring resource utilization metrics during model development.

**Benefits of establishing this best
practice:**

- Reduced energy consumption and carbon footprint from ML
  operations.
- Lower computational costs for model training and deployment.
- Faster development cycles with earlier training completion.
- Better alignment between business requirements and model
  capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning models, balancing accuracy with
sustainability requires deliberate consideration of how much
performance is actually needed. The incremental gains in accuracy
often diminish significantly beyond certain thresholds, while
computational costs continue to rise. By defining sustainable
performance criteria upfront, you create guardrails that reduce
unnecessary environmental impact.

These criteria should reflect your specific business needs rather
than abstract notions of best possible performance. For many
applications, a model that is 95% accurate may provide the same
business value as one that is 96% accurate but requires twice the
computational resources to train. Understand this relationship to
make informed trade-offs.

Early stopping mechanisms represent one practical implementation
of sustainable criteria. These techniques automatically terminate
training when improvement plateaus, avoiding wasted computation.
Tools like SageMaker AI Debugger and Automatic Model Tuning
provide built-in capabilities to implement early stopping without
compromising model quality.

Regularly measuring and monitoring resource utilization can
identify opportunities for optimization. Tracking metrics like CPU
and GPU utilization, memory consumption, and training duration
provides visibility into your model development's environmental
impact and can identify inefficiencies.

### Implementation steps

1. **Establish sustainable performance
   criteria**. Define concrete performance thresholds
   that meet your business requirements without excessive
   resource consumption. Consider both the absolute performance
   levels needed and the point at which additional gains become
   negligible. Include both accuracy and efficiency metrics in
   your criteria, such as inference latency, model size, and
   training resource requirements.
2. **Analyze the accuracy-resource
   tradeoff**. Conduct experiments to understand the
   relationship between model performance and resource
   consumption for your specific use case. Plot accuracy
   against training time, model size, or computational
   resources to identify the point of diminishing returns. Use
   this data to set reasonable stopping criteria for your
   training jobs.
3. **Configure early stopping in training
   jobs**. Set up SageMaker AI Automatic Model Tuning
   with early stopping to terminate training jobs that are not
   showing significant improvement. Navigate to the SageMaker AI
   console, create a hyperparameter tuning job, and enable the
   early stopping option. Alternatively, configure early
   stopping programmatically using the SageMaker AI Python SDK by
   setting the early_stopping_type parameter
   to **Auto**.
4. **Implement debugging
   rules**. Use SageMaker AI Debugger to automatically
   stop training when specific conditions are met. Add rules
   like LossNotDecreasing to your training
   script to detect when your model stops improving. For
   example, configure the rule to stop training if the loss
   doesn't decrease by at least 0.01% over the last ten epochs.
5. **Monitor resource
   utilization**. Track the efficiency of your
   training jobs using CloudWatch metrics or SageMaker AI
   Debugger's Profiling Report. Monitor metrics such as
   CPUUtilization,
   GPUUtilization,
   GPUMemoryUtilization,
   MemoryUtilization, and
   DiskUtilization. Identify patterns of
   resource underutilization that might indicate opportunities
   for right-sizing your infrastructure.
6. **Right-size your training
   infrastructure**. Based on utilization metrics,
   adjust the instance types and counts for your training jobs.
   Select the most efficient instance type that meets your
   performance requirements rather than defaulting to the most
   powerful option. For distributed training jobs, verify that
   you're using an appropriate number of instances to maximize
   utilization.
7. **Validate against business
   requirements**. Before finalizing your model,
   verify that it meets the business requirements while
   adhering to your sustainable performance criteria. Document
   the tradeoffs made and the rationale behind them to provide
   transparency to stakeholders.
8. **Use no-code ML for rapid
   prototyping**. Use
   [SageMaker AI
   Canvas](https://aws.amazon.com/sagemaker/canvas/ "https://aws.amazon.com/sagemaker/canvas/") with natural language support for data
   exploration and model development to quickly validate ML
   approaches before investing in resource-intensive custom
   development. Canvas can generate models with minimal
   computational overhead for initial feasibility testing.
   Export Canvas-generated models and code to notebooks for
   further optimization and sustainable development practices.
9. **Use AI-powered code generation for
   sustainable development**. Use AI-powered
   development tools like
   [Amazon Q Developer](https://aws.amazon.com/q/developer/ "https://aws.amazon.com/q/developer/") and
   [Kiro](https://kiro.ai/ "https://kiro.ai/") to generate
   efficient ML code, automate performance optimization
   scripts, and accelerate the implementation of sustainable ML
   practices while reducing development resource consumption.
10. **Consider smaller specialized
    models**. For generative AI applications, evaluate
    whether smaller, domain-specific models can meet your needs
    instead of using large general-purpose models. Techniques
    like retrieval-augmented generation (RAG) can enhance
    smaller models' capabilities while maintaining lower
    resource requirements. Fine-tuning a smaller base model on
    your specific data often provides better sustainability
    outcomes than using larger generic models.

## Resources

**Related documents:**

- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Stop
  Training Jobs Early](../../../sagemaker/latest/dg/automatic-model-tuning-early-stopping.md "../../../sagemaker/latest/dg/automatic-model-tuning-early-stopping.md")
- [Model
  Explainability](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md")
- [Amazon SageMaker AI Debugger - Built-in Rules:
  LossNotDecreasing](../../../sagemaker/latest/dg/debugger-built-in-rules.md#loss-not-decreasing "../../../sagemaker/latest/dg/debugger-built-in-rules.md#loss-not-decreasing")
- [SageMaker AI job metrics](../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs "../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs")
