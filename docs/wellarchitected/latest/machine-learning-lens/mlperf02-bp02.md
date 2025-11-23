# MLPERF02-BP02 Use purpose-built AI and ML services and

resources

Consider how the workload could be handled by pre-built AI services
or ML resources. Better performance can often be delivered more
efficiently by using pre-optimized components included in AI and ML
managed services. Select an optimal mix of bespoke and pre-built
components to meet the workload requirements.

**Desired outcome:** You achieve a
balanced approach to your machine learning workloads by implementing
purpose-built AI and ML services and resources. You leverage
pre-built components where appropriate to accelerate development,
reduce management overhead, and improve performance while
maintaining the flexibility to create custom solutions where your
business needs demand it. This approach optimizes both your team's
productivity and the overall effectiveness of your AI/ML solutions.

**Common anti-patterns:**

- Building ML components from scratch when suitable pre-built
  solutions exist.
- Failing to evaluate the full range of AWS AI and ML services
  before starting development.
- Over-customizing solutions when standard services would
  adequately meet requirements.
- Underutilizing AWS marketplace solutions and pre-trained models.
- Not considering hybrid approaches that combine managed services
  with custom ML models.

**Benefits of establishing this best
practice:**

- Accelerated time-to-market for ML solutions.
- Reduced operational overhead for maintaining ML infrastructure.
- Lower development costs through leveraging pre-built components.
- Access to continuously improved and updated AI technologies.
- Ability to focus resources on high-value business
  differentiators.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement purpose-built AI and ML services to focus on business
outcomes rather than infrastructure management. AWS provides a
comprehensive portfolio of AI services, ranging from ready-to-use
APIs to fully customizable ML solutions. Each service addresses
different levels of complexity and customization requirements.

When evaluating your ML workloads, assess which components could
benefit from managed services. Tasks like image classification,
regression, clustering, or time series forecasting can often be
accomplished with
[SageMaker AI
built-in algorithms](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") without requiring custom algorithm
development. For more specialized needs, you can leverage
pre-trained models through services like
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") or develop custom models using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/").

Resist the temptation to over-customize solutions when standard
services would adequately meet requirements. Organizations often
underutilize AWS marketplace solutions and pre-trained models,
missing opportunities to accelerate development. The key is
finding the right balance between using managed services for
common ML tasks and building custom solutions for your unique
business requirements. Consider hybrid approaches that combine
managed services with custom ML models rather than pursuing an
all-or-nothing strategy.

Consider your team's capabilities when making these decisions. If
you lack specialized ML expertise, starting with fully managed AI
services provides immediate value while your team builds skills.
As your team's capabilities grow, you can selectively add custom
components where they provide strategic advantage.

### Implementation steps

1. **Assess your ML use cases and
   requirements**. Begin by clearly defining your
   business use cases and understanding the ML capabilities
   needed. Evaluate whether your requirements can be met by
   pre-built services or require custom development. Consider
   factors like accuracy requirements, latency needs, and the
   availability of training data.
2. **Learn about AWS managed AI
   services**. Determine whether
   [AWS managed AI services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/") are applicable to the business
   use case. Understand how managed AWS AI services can relieve
   the burden of training and maintaining an ML pipeline. Use
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to develop in the cloud and understand the
   roles and responsibilities needed to maintain the ML
   workload. Consider combining managed AI services with custom
   ML models built on Amazon SageMaker AI.
3. **Explore SageMaker AI built-in
   algorithms and automated ML capabilities**. Learn
   about
   [SageMaker AI
   built-in algorithms](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") for supervised learning tasks
   like classification, regression, and forecasting. Consider
   [SageMaker AI
   Autopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development.md "../../../sagemaker/latest/dg/autopilot-automate-model-development.md") for automated machine learning that handles
   data analysis, feature engineering, algorithm selection, and
   hyperparameter tuning. Explore
   [Amazon SageMaker AI JumpStart](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md") for pre-trained models across
   various ML domains, including
   [foundation
   models](../../../sagemaker/latest/dg/jumpstart-foundation-models.md "../../../sagemaker/latest/dg/jumpstart-foundation-models.md") that can be fine-tuned for your specific ML
   tasks. For enterprise environments, implement
   [SageMaker AI
   JumpStart Private Model Hubs](../../../sagemaker/latest/dg/jumpstart-curated-hubs.md "../../../sagemaker/latest/dg/jumpstart-curated-hubs.md") to create curated
   repositories of both prebuilt and custom models with
   centralized governance and version management.
4. **Investigate marketplace
   solutions**. Learn about
   [SageMaker AI
   Algorithms and Models in AWS Marketplace](../../../sagemaker/latest/dg/sagemaker-marketplace.md "../../../sagemaker/latest/dg/sagemaker-marketplace.md"), a curated
   digital catalog that makes it simple for you to find, buy,
   deploy, and manage third-party software and services.
   Explore specialized algorithms or pre-trained models that
   might be relevant to your use case.
5. **Implement a hybrid approach where
   appropriate**. Design your ML architecture to
   leverage the most suitable services for each component. Use
   AWS managed services for standard ML tasks and focus custom
   development on business differentiators. This balanced
   approach optimizes both development efficiency and solution
   effectiveness.
6. **Establish a model evaluation
   framework**. Create a systematic process for
   evaluating pre-built models against your requirements.
   Define clear metrics for accuracy, latency, cost, and other
   relevant factors. Use this framework to make data-driven
   decisions about which components to build versus buy.
7. **Plan for operational
   integration**. Verify that your chosen ML services
   can integrate effectively with your existing systems and
   workflows. Design appropriate data pipelines, APIs, and
   monitoring systems to support your hybrid ML architecture.
   For development flexibility, leverage remote IDE
   connectivity to securely connect third-party developer
   environments such as VS Code to SageMaker AI Studio, enabling
   professional MLOps workflows while maintaining centralized
   governance. Consider security, regulatory adherence, and
   governance requirements when implementing these
   integrations.
8. **Optimize model performance and
   deployment**. Use
   [SageMaker AI
   model optimization](../../../sagemaker/latest/dg/model-optimize.md "../../../sagemaker/latest/dg/model-optimize.md") capabilities including
   quantization, compilation, and speculative decoding to
   improve inference performance. Use
   [SageMaker AI
   Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") to automatically benchmark and
   select optimal instance types, configurations, and
   parameters for your inference endpoints. Deploy using
   [SageMaker AI
   deployment options](../../../sagemaker/latest/dg/how-it-works-deployment.md "../../../sagemaker/latest/dg/how-it-works-deployment.md") such as real-time hosting,
   serverless inference, or batch transform based on your
   latency and throughput requirements.
9. **Implement model monitoring and
   governance**. Establish monitoring for model
   performance, data drift, and model drift using
   [SageMaker AI
   Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md"). Implement proper model versioning, A/B
   testing capabilities, and rollback procedures to maintain
   model quality and reliability in production environments.

## Resources

**Related documents:**

- [Built-in
  algorithms and pretrained models in Amazon SageMaker AI](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md")
- [SageMaker AI
  JumpStart Foundation Models](../../../sagemaker/latest/dg/jumpstart-foundation-models.md "../../../sagemaker/latest/dg/jumpstart-foundation-models.md")
- [Private
  curated hubs for foundation model access control in
  JumpStart](../../../sagemaker/latest/dg/jumpstart-curated-hubs.md "../../../sagemaker/latest/dg/jumpstart-curated-hubs.md")
- [Best
  practices for deploying models on SageMaker AI Hosting
  Services](../../../sagemaker/latest/dg/deployment-best-practices.md "../../../sagemaker/latest/dg/deployment-best-practices.md")
- [Inference
  optimization for Amazon SageMaker AI models](../../../sagemaker/latest/dg/model-optimize.md "../../../sagemaker/latest/dg/model-optimize.md")
- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [Model
  deployment options in Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-deployment.md "../../../sagemaker/latest/dg/how-it-works-deployment.md")
- [Distributed
  training optimization](../../../sagemaker/latest/dg/distributed-training-optimize.md "../../../sagemaker/latest/dg/distributed-training-optimize.md")
- [SageMaker AI
  JumpStart pretrained models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
- [Machine
  Learning on AWS](https://aws.amazon.com/machine-learning/ "https://aws.amazon.com/machine-learning/")
- [Architecture
  Best Practices for Machine Learning](https://aws.amazon.com/architecture/machine-learning/ "https://aws.amazon.com/architecture/machine-learning/")
- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [SageMaker AI
  Algorithms and Models in AWS Marketplace](../../../sagemaker/latest/dg/sagemaker-marketplace.md "../../../sagemaker/latest/dg/sagemaker-marketplace.md")
- [Docker
  containers for training and deploying models](../../../sagemaker/latest/dg/docker-containers.md "../../../sagemaker/latest/dg/docker-containers.md")
- [Train
  a Model with Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md")

**Related videos:**

- [Building
  and Deploying ML Models Fast with Amazon SageMaker AI
  JumpStart](https://www.youtube.com/watch?v=i4W7SfP6_38 "https://www.youtube.com/watch?v=i4W7SfP6_38")
