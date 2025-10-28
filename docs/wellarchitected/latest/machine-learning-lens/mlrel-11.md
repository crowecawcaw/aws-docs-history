# MLREL-11: Use an appropriate deployment and testing strategy

Run a trade-off analysis across available and relevant
deployment/testing strategies (such as blue/green, canary,
shadow, and A/B testing) and select the one that meets your
business requirements. 

Implement metrics that evaluate model performance to identify
when a rollback or roll-forward is required. When architecting
for rollback or roll-forward, evaluate the following for each
model:

- Where is the model artifact stored?
- Are model artifacts versioned?
- What changes are included in each version?
- What version of the model is deployed for a deployed
  endpoint?

## Implementation plan

- **Deployment/testing in Amazon SageMaker AI:** SageMaker AI provides managed
  deployment strategies for testing new versions of your
  models in production.
  - See the explanation associated with Figure 16 for
    details of **blue/green, canary,
    and A/B deployment/testing.**
  - **Blue/green deployments using
    Amazon SageMaker AI:** Amazon SageMaker AI
    automatically uses a blue/green deployment to maximize
    the availability of your endpoints when updating a
    SageMaker AI real-time endpoint. The various traffic
    shifting modes in blue/green deployment give you more
    granular control over shifting traffic between the
    blue and green fleet. For more details, see
    [Blue/Green
    deployments in SageMaker AI](../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md").
  - **Canary deployment using Amazon SageMaker AI:** The canary deployment option
    lets you shift one small portion of your traffic (a
    canary) to the green fleet and monitor it for a baking
    period. If the canary succeeds on the green fleet, the
    rest of the traffic is shifted from the blue fleet to
    the green fleet before stopping the blue fleet.

For more information, review
[canary
traffic shifting in SageMaker AI](../../../sagemaker/latest/dg/deployment-guardrails-blue-green-canary.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green-canary.md").

- **Linear deployment using Amazon SageMaker AI:**
  [Linear
  traffic shifting](../../../sagemaker/latest/dg/deployment-guardrails-blue-green-linear.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green-linear.md") allows you to gradually shift
  traffic from your old fleet (blue fleet) to your new fleet
  (green fleet). With linear traffic shifting, you can shift
  traffic in multiple steps, minimizing the chance of a
  disruption to your endpoint. This blue/green deployment
  option gives you the most granular control over traffic
  shifting.
- **A/B testing using Amazon SageMaker AI:** Performing A/B testing between a new
  model and an old model with production traffic can be an
  effective final step in the validation process for a new
  model. In A/B testing, you test different variants of your
  models and compare how each variant performs. If the newer
  version of the model delivers better performance than the
  previously-existing version, replace the old version of
  the model with the new version in production. For more
  details, review
  [test
  models in production](../../../sagemaker/latest/dg/model-ab-testing.md "../../../sagemaker/latest/dg/model-ab-testing.md") in the SageMaker AI
  documentation.

## Documents

- [Deployment
  guardrails: a set of model deployment options in Amazon SageMaker AI Inference to update your machine learning models
  in production](../../../sagemaker/latest/dg/deployment-guardrails.md "../../../sagemaker/latest/dg/deployment-guardrails.md")
- [Blue/Green
  deployments in Amazon SageMaker AI](../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md "../../../sagemaker/latest/dg/deployment-guardrails-blue-green.md")
- [Blue/Green
  Deployment on AWS](../../../whitepapers/latest/blue-green-deployments/welcome.md "../../../whitepapers/latest/blue-green-deployments/welcome.md")
- [Perform
  a canary-based deployment using the blue/green strategy
  and AWS Lambda](../../../prescriptive-guidance/latest/patterns/perform-a-canary-based-deployment-using-the-blue-green-strategy-and-aws-lambda.md "../../../prescriptive-guidance/latest/patterns/perform-a-canary-based-deployment-using-the-blue-green-strategy-and-aws-lambda.md")
- [Amazon SageMaker AI – Testing models in production – Model A/B test
  example](../../../sagemaker/latest/dg/model-ab-testing.md "../../../sagemaker/latest/dg/model-ab-testing.md")

## Blogs

- [Take
  advantage of advanced deployment strategies using Amazon SageMaker AI deployment guardrails](https://aws.amazon.com/blogs/machine-learning/take-advantage-of-advanced-deployment-strategies-using-amazon-sagemaker-deployment-guardrails/ "https://aws.amazon.com/blogs/machine-learning/take-advantage-of-advanced-deployment-strategies-using-amazon-sagemaker-deployment-guardrails/")
- [A/B
  Testing ML models in production using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/")
- [Dynamic
  A/B testing for machine learning models with Amazon SageMaker AI MLOps projects](https://aws.amazon.com/blogs/machine-learning/dynamic-a-b-testing-for-machine-learning-models-with-amazon-sagemaker-mlops-projects/ "https://aws.amazon.com/blogs/machine-learning/dynamic-a-b-testing-for-machine-learning-models-with-amazon-sagemaker-mlops-projects/")
- [Deploy
  shadow ML models in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/deploy-shadow-ml-models-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/deploy-shadow-ml-models-in-amazon-sagemaker/")
- [Safely
  deploying and monitoring Amazon SageMaker AI endpoints with
  AWS CodePipeline and AWS CodeDeploy](https://aws.amazon.com/blogs/machine-learning/safely-deploying-and-monitoring-amazon-sagemaker-endpoints-with-aws-codepipeline-and-aws-codedeploy/ "https://aws.amazon.com/blogs/machine-learning/safely-deploying-and-monitoring-amazon-sagemaker-endpoints-with-aws-codepipeline-and-aws-codedeploy/")

## Videos

- [AWS re:Invent 2020: Canaries in the code mines: Monitoring
  deployment pipelines](https://www.youtube.com/watch?v=IHbY897uEbQ "https://www.youtube.com/watch?v=IHbY897uEbQ")

## Examples

- [Amazon SageMaker AI Inference Deployment Guardrails](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-deployment-guardrails "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-deployment-guardrails")
- [Amazon SageMaker AI A/B Testing Pipeline](https://github.com/aws-samples/amazon-sagemaker-ab-testing-pipeline "https://github.com/aws-samples/amazon-sagemaker-ab-testing-pipeline")
- [Amazon SageMaker AI Safe Deployment Pipeline](https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline "https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline")
- [ML
  Model Shadow Deployment Strategy on AWS](https://github.com/aws-samples/aws-shadow-deployment "https://github.com/aws-samples/aws-shadow-deployment")
