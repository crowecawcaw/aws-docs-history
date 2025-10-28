# GENSUS01-BP01 Implement auto scaling and serverless

architectures to optimize resource utilization

Adopt efficient and sustainable AI/ML practices to minimize resource
usage, reduce costs, and lower environmental impact. Use serverless
architectures, auto scaling, and specialized hardware to optimize
resource utilization. This approach enhances performance efficiency,
aligns with cost optimization, and supports sustainability goals.
Implementing these practices enables responsible and economical
deployment of generative AI workloads and promotes effective scaling
without unnecessary resource waste.

**Desired outcome:** After
implementing this best practice, customers can improve the
elasticity of their generative AI workloads and benefit from the
efficiencies of scale of the AWS Cloud.

**Benefits of establishing this best
practice:**
[Optimize
resource utilization](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md") - Minimize environmental impact by
maximizing the efficiency of generative AI resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopting serverless architectures and auto-scaling capabilities is
essential for verifying that resources are provisioned and
consumed only when needed. This approach minimizes idle
consumption and reduces the associated environmental impact. While
training jobs may run overnight, the notebook and ML development
instances that are not in use can be shut down either through
configuring an idle time-out or through scheduling. You can
further enhance the efficiency of your workload's resource
utilization by using AWS managed services and managed offerings.

Amazon Bedrock and Amazon Q are fully-managed services, which
means that AWS handles the infrastructure management, scaling, and
maintenance. As a result, users can focus on model development
rather than infrastructure utilization. Similarly,
[Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") helps optimize the
deployment of machine learning models by automating load testing.
It assists in selecting the best instance type by considering
factors like instance count, container parameters, and model
optimizations. This tool provides recommendations for both
real-time and serverless inference endpoints, which helps you
verify that models are deployed with the best performance at the
lowest resource consumption.

For hosting and running generative AI models efficiently, consider
using Amazon EC2 Inferentia instances. These instances deliver
some of the highest compute power and accelerator memory in among
EC2 instance families, which is crucial for handling large
language models and other generative AI workloads. Inferentia
instances support scale-out distributed inference to optimize
compute consumption. The improved performance per watt translates
to more efficient use of resources. By integrating these AWS
services and features, organizations can achieve a more
sustainable and cost-effective approach to generative AI
workloads.

### Implementation steps

1. Adopt serverless or fully-managed architectures.
   - Use Amazon Bedrock for generative AI tasks to alleviate
     server management overhead
   - Use Amazon Q Business-related AI applications to
     streamline operations
   - Use Amazon SageMaker AI Serverless Inference for on-demand
     ML inference without managing servers

2. Configure auto scaling capabilities.
   - Set up auto scaling for Amazon SageMaker AI Endpoints to
     handle varying loads efficiently
   - Set up EC2 Auto Scaling for custom ML infrastructure to
     match resource allocation with demand

3. Optimize ML development environments.
   - For
     [SageMaker AI
     notebook instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md"), configure idle time-out to
     release resources when not in use
   - For ML development instances, schedule automatic
     shutdown for unused instances to conserve resources

4. Use SageMaker AI Inference Recommender.
   - Conduct automated load testing to assess model
     deployments under various loads
   - Select optimal instance types based on recommendations
     for cost-effective and performance
   - Consider both real-time and serverless inference

5. Implement efficient model hosting.
   - For model deployments, consider EC2 Inferentia instances
     for enhanced performance and efficiency
   - For large models, scale and distribute the load across
     multiple instances

6. Perform continuous monitoring and optimization.
   - Use Amazon CloudWatch to track resource metrics and
     identify optimization opportunities
   - Track token lengths of prompts and model responses to
     measure utilization
   - Identify idle time periods to scale down or suspend the
     inference endpoints
   - Set up SageMaker AI Model Monitor to continuously monitor
     model performance and data quality

7. Educate your team on sustainable AI practices.
   - Provide training to foster a culture of sustainability
   - Encourage the use of pre-trained models to reduce
     training time and resource consumption

## Resources

**Related practices:**

- [SUS02-BP01](../framework/sus_sus_user_a2.md "../framework/sus_sus_user_a2.md")
- [SUS05-BP02](../framework/sus_sus_hardware_a3.md "../framework/sus_sus_hardware_a3.md")
- [SUS02-BP03](../sustainability-pillar/sus_sus_user_a4.md "../sustainability-pillar/sus_sus_user_a4.md")

**Related guides, videos, and documentation:**

- [Sustainability pillar – Best practices](../machine-learning-lens/sustainability-pillar-best-practices-5.md "../machine-learning-lens/sustainability-pillar-best-practices-5.md")
- [Automatic
  scaling of Amazon SageMaker AI models](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [Amazon SageMaker AI Best Practices](../../../sagemaker/latest/dg/best-practices.md "../../../sagemaker/latest/dg/best-practices.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Optimizing Costs for Machine Learning with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/")
- [The
  executive's guide to generative AI for sustainability](https://aws.amazon.com/blogs/machine-learning/the-executives-guide-to-generative-ai-for-sustainability/ "https://aws.amazon.com/blogs/machine-learning/the-executives-guide-to-generative-ai-for-sustainability/")
- [Optimize
  generative AI workloads for environmental
  sustainability](https://aws.amazon.com/blogs/machine-learning/optimize-generative-ai-workloads-for-environmental-sustainability/ "https://aws.amazon.com/blogs/machine-learning/optimize-generative-ai-workloads-for-environmental-sustainability/")
- [Integrating
  generative AI effectively into sustainability
  strategies](https://www.youtube.com/watch?v=8vAMOPLnN-w "https://www.youtube.com/watch?v=8vAMOPLnN-w")
- [Optimize
  your AI/ML workloads with Amazon EC2 Graviton](https://www.youtube.com/watch?v=QIAaMlW1fVo "https://www.youtube.com/watch?v=QIAaMlW1fVo")

**Related examples:**

- [SageMaker AI
  Inference Recommender Example](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-recommender "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-recommender")
- [AWS can help reduce the carbon footprint of AI workloads by up to
  99%](https://www.aboutamazon.com/news/aws/aws-carbon-footprint-ai-workload "https://www.aboutamazon.com/news/aws/aws-carbon-footprint-ai-workload")
- [Carrier Uses
  Amazon Bedrock to Help Customers Achieve Their Sustainability Goals](https://aws.amazon.com/solutions/case-studies/carrier-bedrock-sustainability-testimonial/ "https://aws.amazon.com/solutions/case-studies/carrier-bedrock-sustainability-testimonial/")

**Related tools:**

- [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/ "https://aws.amazon.com/ec2/autoscaling/")
- [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/ "https://aws.amazon.com/ai/machine-learning/inferentia/")
- [New – Customer
  Carbon Footprint Tool](https://aws.amazon.com/blogs/aws/new-customer-carbon-footprint-tool/ "https://aws.amazon.com/blogs/aws/new-customer-carbon-footprint-tool/")
