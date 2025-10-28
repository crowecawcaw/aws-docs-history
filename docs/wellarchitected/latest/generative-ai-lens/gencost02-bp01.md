# GENCOST02-BP01 Balance cost and performance when selecting

inference paradigms

Hosting a foundation model for inference requires many choices, and
many of these decisions can affect the cost of your workload. One of
these choices includes the selection of a managed, serverless
deployment of a foundation model against a self-hosted option.

**Desired outcome:** When
implemented, this best practice describes a relationship between
cost and performance contextualized against model hosting and
inference paradigms. This relationship helps you evaluate
cost-benefit choices associated with the selection of an inference
paradigm.

**Benefits of establishing this best
practice:**

- [Measure
  overall efficiency](../framework/cost-dp.md "../framework/cost-dp.md") - It is helpful to understand
  inference and hosting costs associated with the performance
  requirements of foundation model.
- [Lower
  spend on undifferentiated heavy lifting](../framework/cost-dp.md "../framework/cost-dp.md") - More often than
  not, it is beneficial to opt for a managed or serverless hosting
  paradigm, due to the intractability of the total cost of
  ownership for foundation model hosting.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Throughput sensitive workloads often require additional resources
to service inference requests at the rate they are being
submitted. Provisioned throughput, available through Amazon Bedrock, provides increased throughput capability for large
language models supporting generative AI workloads. If your
workload requires provisioned throughput to meet its performance
requirements, consider preferring longer commitment terms for
better unit costs. Validate your scaling requirements with shorter
duration commitments to avoid over-provisioning your workload.
Provisioned throughput is available for purchase in Amazon Bedrock. If the model you are using has throughput performance
needs or continuous model inference scale supports provisioned
throughput, consider purchasing a short-term. Test the improvement
and determine if the provisioned throughput improves your
application's performance. If there is a strong case for
provisioned throughput, consider purchasing a six-month plan, as
the unit cost for six months is usually lower than purchasing
month-over-month.

### Implementation steps

1. Identify the nature of the demand for this workload.
2. Compare the demand to the available hosting options, and
   remove the high-cost options that do not satisfy the
   workloads hosting requirements.
3. Select the most appropriate, lowest-cost hosting option.

## Resources

**Related practices:**

- [COST06-BP01](../cost-optimization-pillar/cost_type_size_number_resources_cost_modeling.md "../cost-optimization-pillar/cost_type_size_number_resources_cost_modeling.md")
- [COST06-BP02](../cost-optimization-pillar/cost_type_size_number_resources_data.md "../cost-optimization-pillar/cost_type_size_number_resources_data.md")
- [COST09-BP01](../cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.md "../cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.md")

**Related guides, videos, and documentation:**

- [Tagging
  Amazon Bedrock resources](../../../bedrock/latest/userguide/tagging.md "../../../bedrock/latest/userguide/tagging.md")
- [Inference
  cost optimization best practices](../../../sagemaker/latest/dg/inference-cost-optimization.md "../../../sagemaker/latest/dg/inference-cost-optimization.md")

**Related examples:**

- [Track,
  allocate and manage your generative AI cost and usage with
  Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/")
- [Optimizing
  costs of generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/ "https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/")
- [Analyze
  Amazon SageMaker AI spend and determine cost optimization
  opportunities based on usage, Part 1](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/ "https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/")
