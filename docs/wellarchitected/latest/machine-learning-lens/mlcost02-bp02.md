# MLCOST02-BP02 Perform a tradeoff analysis between custom and

pre-trained models

Optimize machine learning costs by carefully analyzing the tradeoffs
between developing custom models and using pre-trained models. This
analysis should maintain security and performance efficiency within
acceptable thresholds while minimizing unnecessary expenses.

**Desired outcome:** You achieve
optimal cost efficiency in your machine learning initiatives by
making informed decisions about when to use pre-trained models
versus developing custom solutions. You balance development costs,
time-to-market, model performance, and specific business
requirements while maintaining appropriate security standards. This
strategic approach allows you to accelerate ML development while
optimizing your investment in AI/ML resources.

**Common anti-patterns:**

- Building custom models for every use case without considering
  available pre-trained alternatives.
- Using pre-trained models without evaluating if they meet your
  specific business requirements.
- Ignoring the total cost of ownership including data scientist
  time, infrastructure, and ongoing maintenance.
- Overlooking security and compliance requirements when selecting
  pre-trained models.

**Benefits of establishing this best
practice:**

- Reduced time-to-market for ML solutions.
- Lower development and operational costs.
- Ability to use state-of-the-art models without needing extensive
  expertise.
- More efficient use of data scientist and ML engineer resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing machine learning solutions, the decision between
building custom models and using pre-trained ones significantly
impacts costs, time-to-market, and solution effectiveness. Custom
models offer greater flexibility and potential performance
advantages for specialized tasks but require substantial
investment in data collection, training infrastructure, and
expertise. Pre-trained models provide rapid deployment and reduced
initial costs but may not perfectly align with specific business
needs.

Your analysis should consider factors including data availability,
task specificity, performance requirements, available expertise,
and long-term maintenance costs. For many common use cases like
sentiment analysis, image classification, or document processing,
pre-trained models can deliver excellent results without the
overhead of custom development. For highly specialized domains or
when competitive advantage depends on model performance, custom
development may justify the additional investment.

### Implementation steps

1. **Assess your machine learning
   needs**. Begin by clearly defining your business
   use case, required model accuracy, latency requirements, and
   available data. Understand whether your use case is standard
   (for example, image classification or sentiment analysis) or
   highly specialized to guide your decision-making process.
2. **Use Amazon SageMaker AI built-in
   algorithms and AWS Marketplace**.
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/?nc=sn&loc=1 "https://aws.amazon.com/sagemaker/ai/?nc=sn&loc=1") provides a suite of built-in algorithms
   for data scientists and machine learning practitioners to
   get started on training and deploying machine learning
   models. Pre-trained ML models are ready-to-use models that
   can be quickly deployed on Amazon SageMaker AI. By pre-training
   the ML models for you, solutions in the
   [AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models "https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models") take care of the heavy lifting so that
   you can deliver AI- and ML-powered features faster and at a
   lower cost. Evaluate the cost of your data scientists' time
   and other resource requirements to develop your own custom
   model vs. bringing a pre-trained model and deploying it on
   SageMaker AI for inferencing. The advantage of a custom model
   is the flexibility to fine-tune it to match the needs of
   your business use case. A pre-trained model can be difficult
   to modify and you might have to use it as is.
3. **Use Amazon SageMaker AI
   JumpStart**. Use
   [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") to access pre-trained models and
   accelerate the ML development process. SageMaker AI JumpStart
   provides a set of solutions for the most common use cases
   that can be deployed readily with just a few clicks. The
   solutions are fully customizable and showcase the use of AWS CloudFormation templates and reference architectures so you
   can accelerate your ML journey. Amazon SageMaker AI JumpStart
   also supports one-click deployment and fine-tuning of more
   than 150 popular open-source models such as natural language
   processing, object detection, and image classification
   models.
4. **Conduct a cost-benefit
   analysis**. Calculate the total cost of ownership
   for both custom and pre-trained approaches, including
   development time, infrastructure costs, and ongoing
   maintenance. Consider factors such as data preparation,
   training resources, and the expertise required. Compare
   these costs against expected business value and performance
   requirements to determine the most cost-effective approach.
5. **Implement cost monitoring and
   optimization**. Use
   [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") and
   [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/") to monitor and manage your ML workload costs.
   Implement automatic shutdown of idle resources to reduce
   unnecessary expenses. Consider using
   [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") to get cost optimization
   recommendations for your ML infrastructure.
6. **Explore model customization
   options**. When pre-trained models don't fully meet
   your requirements, explore customization options like
   fine-tuning or transfer learning before committing to full
   custom development. This approach can provide a middle
   ground between cost and performance and access to existing
   models while adapting them to your specific needs.
7. **Implement a multi-model
   approach**. For complex use cases, consider using
   different models for different components of your solution
   based on their requirements. This allows you to optimize
   costs by using simpler, more economical models where
   appropriate while reserving more powerful models for tasks
   that require them.
8. **Evaluate foundation models in Amazon
   Bedrock**.
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") provides a fully managed service that offers
   foundation models from leading AI companies through a single
   API. Consider using these models for text, image, and
   multimodal generative AI applications instead of building
   custom models. You can customize these models to your
   specific needs using retrieval-augmented generation (RAG) or
   fine-tuning while maintaining cost efficiency.
9. **Use expanded pre-trained model
   libraries**. Use the expanded
   [SageMaker AI
   JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") catalog which now includes broader
   selection of pre-trained models and industry-specific
   solutions, reducing the need for custom model development
   and associated costs.
10. **For generative AI workloads,
    consider retrieval-augmented generation (RAG)**.
    For many generative AI applications, implementing RAG can
    enhance the performance of foundation models by providing
    them with relevant context from your organization's data.
    This approach can be more cost-effective than fine-tuning
    and still provide customized outputs tailored to your
    business domain.

## Resources

**Related documents:**

- [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/")
- [Pre-trained
  machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models "https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models")
- [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/")
- [Cloud
  Financial Management with AWS](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/")
