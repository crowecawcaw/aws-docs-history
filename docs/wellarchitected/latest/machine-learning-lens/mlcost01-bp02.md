# MLCOST01-BP02 Use managed services to reduce total cost of

ownership (TCO)

Using managed machine learning services enables organizations to
operate more efficiently with reduced resources and costs compared
to self-managed options. This approach reduces undifferentiated
heavy lifting, reduces operational burden, and allows teams to focus
on delivering business value.

**Desired outcome:** By adopting
managed services and pay-per-usage models, you significantly reduce
your total cost of ownership while gaining access to a comprehensive
suite of AI/ML tools. You can use pre-built capabilities instead of
developing custom solutions, automatically scale resources based on
demand, and benefit from AWS's continuous innovations without
additional investment. Your teams can focus on creating business
value rather than managing infrastructure.

**Common anti-patterns:**

- Building and maintaining custom ML infrastructure on EC2 or
  Kubernetes.
- Overprovisioning resources for peak ML workloads.
- Failing to use commitment discounts for persistent workloads.
- Developing proprietary AI services when managed services would
  suffice.
- Not analyzing workload patterns to optimize instance selection.

**Benefits of establishing this best
practice:**

- Significantly lower total cost of ownership compared to
  self-managed options.
- Reduced operational overhead and simplified management.
- Increased team productivity with focus on core business
  problems.
- Access to continuously updated and improved AI/ML capabilities.
- Flexibility to scale resources based on actual demand.
- Ability to use commitment-based pricing for additional savings.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Managed services remove the operational burden of maintaining
infrastructure, allowing you to concentrate on developing ML
models and applications that drive business value. Using AWS's
managed ML services provides a comprehensive environment for
building, training, and deploying models with significantly lower
costs than self-managed options.

When evaluating your ML strategy, consider the total cost of
ownership including infrastructure, operational personnel,
maintenance, scaling, and upgrades. Amazon SageMaker AI provides a
fully managed service that avoids many of these costs while
offering advanced ML capabilities. Similarly, AWS's pre-trained AI
services can address common use cases without requiring ML
expertise, further reducing implementation time and costs.

To maximize cost efficiency, analyze your workload patterns and
determine which components would benefit from commitment
discounts. By using Savings Plans, you can significantly reduce
your AWS usage costs while maintaining flexibility across instance
families, sizes, regions, and components.

### Implementation steps

1. **Use Amazon SageMaker AI as your
   fully managed ML solution.**
   [Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md") enables building, training, and
   deploying models at scale with significantly lower costs.
   The total cost of ownership (TCO) of SageMaker AI over a
   three-year period is much lower than other self-managed
   cloud-based ML options, such as
   [Amazon Elastic Compute Cloud](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") (Amazon EC2) and
   [Amazon Elastic Kubernetes Service](../../../eks/latest/userguide/getting-started.md "../../../eks/latest/userguide/getting-started.md") (Amazon EKS). SageMaker AI
   includes technologies such as
   [Autopilot](https://aws.amazon.com/sagemaker/autopilot/ "https://aws.amazon.com/sagemaker/autopilot/"),
   [Feature
   Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/"),
   [Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/"),
   [Debugger](https://aws.amazon.com/sagemaker/debugger/ "https://aws.amazon.com/sagemaker/debugger/"),
   [Studio](https://aws.amazon.com/sagemaker/studio/ "https://aws.amazon.com/sagemaker/studio/"),
   [Training](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md"),
   Model deployment,
   [Monitoring](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md"),
   and
   [Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/").
2. **Use Amazon managed AI services for
   common use cases.** AWS pre-trained AI services
   provide ready-made intelligence for your applications and
   workflows. These services address common use cases such as
   personalized recommendations, contact center modernization,
   safety and security improvement, and customer engagement
   enhancement. They don't require machine learning expertise,
   are fully managed, and offer pay-as-you-go pricing with no
   upfront commitment.
3. **Perform pricing model analysis for
   cost optimization.** Analyze each component of your
   ML workload to determine if it will run for extended
   periods, making it eligible for commitment discounts such as
   [AWS Savings Plans](../../../savingsplans/latest/userguide/what-is-savings-plans.md "../../../savingsplans/latest/userguide/what-is-savings-plans.md"). You can use Savings Plans to reduce
   AWS usage costs by committing to a consistent amount of
   usage.
   [Amazon SageMaker AI Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/ "https://aws.amazon.com/savingsplans/ml-pricing/") offer flexible attributes
   such as instance family, instance size, AWS Region, and
   component for your SageMaker AI instance usage.
4. **Implement right-sizing strategies
   for ML resources.** Evaluate your actual ML
   workload resource requirements and adjust instance types and
   sizes accordingly. This blocks overprovisioning and assists
   to control costs while maintaining performance. Use
   SageMaker AI's automatic scaling capabilities to match
   resources with demand.
5. **Use serverless options when
   appropriate.** For intermittent workloads or those
   with variable demand, consider serverless options like
   [Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md") to avoid paying for
   idle resources.
6. **Use Amazon Bedrock for foundation
   model access.**
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") provides a unified API for accessing various
   foundation models, making it simple to experiment with and
   integrate generative AI capabilities without investing in
   model training infrastructure. This fully managed service
   assists to reduce costs while allowing flexibility to choose
   the right model for your use case.
7. **Use Foundation Model Hub for
   centralized model access**. Use the Foundation
   Model Hub to access a centralized catalog of popular
   foundation models with simplified deployment and performance
   benchmarking tools, reducing the time and cost of model
   selection and deployment.
8. **Use AI-powered code generation
   tools.** Use
   [Amazon Q Developer](https://aws.amazon.com/q/developer/ "https://aws.amazon.com/q/developer/") and AI-powered IDEs like Kiro to
   accelerate ML development through AI-assisted coding,
   automated code generation, and intelligent troubleshooting,
   significantly reducing developer time and associated costs.

## Resources

**Related documents:**

- [Amazon
  managed AI services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/")
- [AWS AI Services overview](https://aws.amazon.com/machine-learning/ "https://aws.amazon.com/machine-learning/")
- [ML
  Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/ "https://aws.amazon.com/savingsplans/ml-pricing/")
- [AWS Pricing Calculator for SageMaker AI](https://calculator.aws/#/createCalculator/SageMaker AI "https://calculator.aws/#/createCalculator/SageMaker AI")
- [Viewing
  resource recommendations](../../../compute-optimizer/latest/ug/viewing-recommendations.md "../../../compute-optimizer/latest/ug/viewing-recommendations.md")
- [What
  is Amazon Bedrock?](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md")
- [What
  is AWS Migration Hub?](../../../migrationhub/latest/ug/whatishub.md "../../../migrationhub/latest/ug/whatishub.md")
- [What
  are AWS Cost and Usage Reports?](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md")
