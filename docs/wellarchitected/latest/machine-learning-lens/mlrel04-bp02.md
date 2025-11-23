# MLREL04-BP02 Use an appropriate deployment and testing

strategy

Select the right deployment and testing strategy for your machine
learning models to create smoother transitions to production,
minimize disruption, and allow for careful evaluation of model
performance before full implementation.

**Desired outcome:** You can
confidently deploy machine learning models to production using
strategies that minimize risk and maximize availability. You have
established processes to monitor model performance, allowing you to
make data-driven decisions about when to roll back to previous
versions or roll forward with new updates. Your deployment pipelines
include appropriate testing, validation, and metrics collection to
improve model quality and performance in production environments.

**Common anti-patterns:**

- Deploying new models directly to production without testing
  strategies.
- Lacking version control for model artifacts.
- Not implementing monitoring metrics to evaluate model
  performance.
- Using the same deployment strategy for models without
  considering specific use case requirements.
- Failing to plan for rollbacks when model performance degrades.

**Benefits of establishing this best
practice:**

- Minimizes disruption to production services during model
  updates.
- Enables testing models with real production traffic before full
  deployment.
- Reduces risk through controlled deployment strategies.
- Improves visibility into model performance.
- Provides better mechanisms for recovering from poor-performing
  model deployments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning models require special consideration when
deploying to production environments because their behavior can be
complex and sometimes unpredictable. Unlike traditional software
where functionality is explicitly coded, ML models learn patterns
from data, making it crucial to validate their performance with
production data before full deployment.

Different deployment strategies provide varying levels of risk
mitigation and testing capabilities. Blue/green deployments allow
for instantaneous rollback by maintaining two identical
environments. Canary deployments reduce risk by exposing only a
small portion of traffic to new models. A/B testing enables you to
compare performance metrics between model versions. Shadow
deployments let you test new models without affecting user
experience by running them alongside the production model but not
using their predictions.

Your choice of deployment strategy should be guided by your
specific requirements for availability, risk tolerance, and the
criticality of the ML application. For high-stakes applications
like fraud detection or medical diagnostics, more cautious
approaches like canary or shadow deployments may be appropriate.
For less critical applications, simpler strategies might suffice.

### Implementation steps

1. **Perform a deployment strategy
   trade-off analysis**. Evaluate your business
   requirements and risk tolerance to determine which
   deployment strategies are most appropriate for your ML
   models. Consider factors like required availability,
   acceptable downtime, criticality of predictions, and
   monitoring capabilities. Document your analysis and
   selection criteria for each model deployment.
2. **Implement robust model
   versioning**. Establish a system to version model
   artifacts, including the model itself, preprocessing
   components, and associated configurations. Use
   [Amazon SageMaker AI Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") to catalog models and track
   their lineage, approval status, and deployment history.
   Then, you can quickly identify what model version is running
   and roll back if needed.
3. **Set up blue/green deployments with
   SageMaker AI**. Implement blue/green deployments for
   your real-time inference endpoints to maximize availability
   during updates. SageMaker AI automatically provisions new
   infrastructure (green fleet) before transitioning traffic
   from the old infrastructure (blue fleet), providing nearly
   continuous service. Configure the appropriate
   [traffic
   shifting mode](../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md") based on your risk tolerance.
4. **Configure canary deployments for
   higher-risk updates**. For model updates where you
   want additional safety, implement canary deployments that
   route a small percentage of traffic to the new model version
   first. Use
   [SageMaker AI
   deployment guardrails](../../../sagemaker/latest/dg/deployment-guardrails-blue-green-canary.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green-canary.md") to set up canary testing with
   baking periods to monitor model performance before shifting
   the remaining traffic.
5. **Establish linear traffic shifting
   for granular control**. For the most controlled
   deployments, set up
   [linear
   traffic shifting](../../../sagemaker/latest/dg/deployment-guardrails-blue-green-linear.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green-linear.md") in SageMaker AI to gradually move
   traffic from the blue fleet to the green fleet in multiple
   steps. Define appropriate step sizes and baking periods
   between shifts to carefully monitor model behavior at each
   stage.
6. **Implement A/B testing for model
   comparison**. When you need to validate that a new
   model performs better than the existing one, set up A/B
   testing to compare metrics between versions with real
   production traffic. Use
   [SageMaker AI
   A/B testing](../../../sagemaker/latest/dg/model-ab-testing.md "../../../sagemaker/latest/dg/model-ab-testing.md") to route defined percentages of traffic
   to different model variants and collect performance data.
7. **Deploy shadow models to reduce the
   risk of testing**. For high-risk applications,
   consider implementing shadow deployments where the new model
   runs alongside the production model but doesn't affect
   customer-facing decisions. This allows you to compare how
   the new model would have performed using real production
   data while minimizing the risk.
8. **Define and implement model
   performance metrics**. Establish clear metrics to
   evaluate model performance in production, such as prediction
   accuracy, latency, throughput, and business KPIs. Set up
   monitoring with
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to track these metrics and create alarms
   that can run automatic or manual interventions when
   performance degrades.
9. **Create automatic rollback
   mechanisms**. Implement automated procedures to
   roll back to previous model versions when performance
   metrics indicate problems. Define specific thresholds for
   metrics that would trigger a rollback, and establish the
   process for rolling back with minimal disruption.
10. **Build comprehensive CI/CD
    pipelines**. Integrate your deployment strategies
    into complete CI/CD pipelines that automate the testing,
    deployment, and monitoring of models. Use
    [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") and
    [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/") in conjunction with SageMaker AI to create
    reliable deployment workflows.

## Resources

**Related documents:**

- [Deployment
  guardrails for updating models in production](../../../sagemaker/latest/dg/deployment-guardrails.md "../../../sagemaker/latest/dg/deployment-guardrails.md")
- [Blue/Green
  Deployments](../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md")
- [Testing
  models with production variants](../../../sagemaker/latest/dg/model-ab-testing.md "../../../sagemaker/latest/dg/model-ab-testing.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Take
  advantage of advanced deployment strategies using Amazon SageMaker AI deployment guardrails](https://aws.amazon.com/blogs/machine-learning/take-advantage-of-advanced-deployment-strategies-using-amazon-sagemaker-deployment-guardrails/ "https://aws.amazon.com/blogs/machine-learning/take-advantage-of-advanced-deployment-strategies-using-amazon-sagemaker-deployment-guardrails/")
- [A/B
  Testing ML models in production using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/")

**Related videos:**

- [Deliver
  high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc "https://www.youtube.com/watch?v=T9llSCYJXxc")
- [Canaries
  in the code mines: Monitoring deployment pipelines](https://www.youtube.com/watch?v=IHbY897uEbQ "https://www.youtube.com/watch?v=IHbY897uEbQ")

**Related examples:**

- [Amazon SageMaker AI Inference Deployment Guardrails](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-deployment-guardrails "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-deployment-guardrails")
- [Amazon SageMaker AI A/B Testing Pipeline](https://github.com/aws-samples/amazon-sagemaker-ab-testing-pipeline "https://github.com/aws-samples/amazon-sagemaker-ab-testing-pipeline")
- [Amazon SageMaker AI Safe Deployment Pipeline](https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline "https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline")
