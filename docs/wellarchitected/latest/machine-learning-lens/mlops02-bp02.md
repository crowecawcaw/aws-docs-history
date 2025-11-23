# MLOPS02-BP02 Prepare an ML profile template

Creating an ML profile template allows you to systematically capture
machine learning workload characteristics across different lifecycle
phases. Use this template to evaluate your ML workload's current
maturity status and strategically plan for improvements that align
with your business requirements.

**Desired outcome:** You gain a
comprehensive understanding of your ML workload's deployment
characteristics by creating templated profiles that capture critical
metrics and thresholds. By maintaining current and target profiles,
you can effectively track your ML workload maturity journey and make
data-driven decisions about architecture, resources, and deployment
options that best align with your business needs.

**Common anti-patterns:**

- Creating ML profiles without clear thresholds or maturity
  rankings.
- Failing to document rationale for architectural and deployment
  choices.
- Focusing on technical metrics without connecting to business
  requirements.
- Not considering future state or alternative deployment options.
- Ignoring cost implications of different deployment scenarios.

**Benefits of establishing this best
practice:**

- Enables objective assessment of ML workload maturity status.
- Provides a structured approach to planning ML workload
  improvements.
- Creates alignment between technical implementation and business
  requirements.
- Facilitates better resource planning and cost optimization.
- Supports strategic decision-making with documented rationale.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning workloads have unique characteristics that impact
their deployment architecture, infrastructure requirements, and
operational management. Create a standardized ML profile template
to document these characteristics systematically across the stages
of the ML lifecycle. By capturing key metrics and establishing
thresholds, you can objectively assess the maturity level of your
ML workloads and identify areas for improvement.

For each ML workload, you should maintain at least two profiles:
one representing the current state and another representing the
target or future state. This approach creates a clear path for
improvement while documenting the rationale behind architectural
and deployment decisions.

When developing your ML profile template, focus on the most
impactful characteristics that influence infrastructure choices,
deployment options, and operational considerations. Include
metrics that span model characteristics, architectural decisions,
and operational requirements. For each characteristic, establish a
spectrum from lower to higher ranges to position your workload on
a maturity scale.

### Implementation steps

1. **Capture ML workload deployment
   characteristics**. Identify and document the most
   impactful deployment characteristics of your ML workload.
   These characteristics can determine optimal deployment
   architecture, computing requirements, and instance sizing.
   Use
   [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md"), which includes more
   sophisticated instance selection algorithms and support for
   multi-model endpoints, to optimize instance selection based
   on your model's performance and cost requirements.
2. **Document model deployment
   characteristics**. Record key metrics about your ML
   models, including:
   - Model size (model.tar.gz) in bytes
   - Number of models deployed per endpoint
   - Instance size (for example,
     r5dn.4x.large) as suggested by the
     inference recommender
   - Retraining and model endpoint update frequency (hourly,
     daily, weekly, monthly, or per-event)
   - Model deployment location (on premises, Amazon EC2,
     container, serverless, or edge)

3. **Map architectural deployment
   characteristics**. Capture information about the
   internal architecture of your ML solution:
   - Inference pipeline architecture (single endpoint or
     chained endpoints)
   - Neural architecture (single framework like Scikit-learn
     or multi-framework like PyTorch, Scikit-learn,
     TensorFlow)
   - Containers (SageMaker AI prebuilt container, bring your
     own container)
   - Location of containers and models (on premises, cloud,
     or hybrid)
   - Serverless inferencing (pay as you go) options like
     Amazon SageMaker AI Serverless Inference
   - [Inference
     Components](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md") for modular inference pipeline
     architecture (mix and match pre-processing, model
     serving, and post-processing components)

4. **Define traffic pattern
   characteristics**. Document how your ML model will
   be used:
   - Traffic pattern (steady or spiky)
   - Input size (number of bytes)
   - Latency requirements (low, medium, high, or batch)
   - Concurrency needs (single thread or multi-thread)

5. **Determine cold start
   tolerance**. Document the acceptable latency for
   cold starts in milliseconds, as this impacts the choice
   between always-on and serverless deployment options.
6. **Evaluate network deployment
   characteristics**. Assess and document
   network-related requirements, including AWS KMS encryption
   needs, multi-variant endpoints, network isolation
   requirements, and use of third-party Docker repositories.
7. **Analyze cost
   considerations**. Document cost considerations for
   different deployment options, including the potential use of
   Amazon EC2 Spot Instances for non-critical workloads, Amazon SageMaker AI Serverless Inference for pay-per-use models, or
   multi-model endpoints for cost sharing.
8. **Create a provisioning
   matrix**. Develop a matrix of expected capacity
   requirements across different environments (development,
   staging, production) and regions. This should include the
   number and types of instances needed for training, batch
   inference, real-time inference, and development notebooks.
9. **Map workload characteristics across
   maturity spectrum**. For each characteristic in
   your profile, establish a spectrum from lower to higher
   maturity. This spectrum positions your current
   implementation and defines targets for improvement.
10. **Document rationale for target
    profile**. Provide clear justification for the
    values selected in your target profile, linking them to
    specific business requirements and expected outcomes.
11. **Evaluate and update profiles
    regularly**. Revisit your ML profiles periodically
    to check that they remain aligned with evolving business
    requirements and to incorporate learnings from production
    experience.
12. **Foundation model deployment
    considerations**. For generative AI workloads,
    include additional profile characteristics such as model
    quantization level, context window requirements, token
    processing speed, and memory footprint using
    [optimized
    foundation model containers](../../../sagemaker/latest/dg/large-model-inference.md "../../../sagemaker/latest/dg/large-model-inference.md") to properly size
    infrastructure for these resource-intensive models.

## Resources

**Related documents:**

- [SageMaker AI
  Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [AWS Pricing Calculator - SageMaker AI](https://calculator.aws/#/addService/SageMaker AI "https://calculator.aws/#/addService/SageMaker AI")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Multi-model
  endpoints](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md")
- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/")
- [What
  is Amazon SageMaker AI?](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md")
- [Improved
  ML model deployment using Amazon SageMaker AI Inference
  Recommender](https://aws.amazon.com/blogs/machine-learning/improved-ml-model-deployment-using-amazon-sagemaker-inference-recommender/ "https://aws.amazon.com/blogs/machine-learning/improved-ml-model-deployment-using-amazon-sagemaker-inference-recommender/")
- [Unlock
  cost savings with the new scale down to zero feature in
  SageMaker AI Inference](https://aws.amazon.com/blogs/machine-learning/unlock-cost-savings-with-the-new-scale-down-to-zero-feature-in-amazon-sagemaker-inference/ "https://aws.amazon.com/blogs/machine-learning/unlock-cost-savings-with-the-new-scale-down-to-zero-feature-in-amazon-sagemaker-inference/")
- [Beyond
  the basics: A comprehensive foundation model selection
  framework for generative AI](https://aws.amazon.com/blogs/machine-learning/beyond-the-basics-a-comprehensive-foundation-model-selection-framework-for-generative-ai/ "https://aws.amazon.com/blogs/machine-learning/beyond-the-basics-a-comprehensive-foundation-model-selection-framework-for-generative-ai/")
