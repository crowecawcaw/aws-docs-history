# RAIDP03-BP04 Include both intrinsic and confounding variations

in your datasets

Revisit your release criteria and use case description to confirm
that your definitions of intrinsic and confounding input variations
(respectively, variations the system should attend to, and
variations it should ignore). Include coverage of relevant
variations for your use case in your datasets. If you have
robustness release criteria, label what type of variation is present
in each example in your evaluation set so you can measure how well
your system handles different kinds of variations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Update your lists of intrinsic and confounding input
   variations (respectively, variations the system should attend
   to and variations it should ignore) based on your release
   criteria.
2. Determine ways to get examples of intrinsic variations.
   Consider whether your samples cover the full distribution of
   values possible (for example, the full range of nose
   geometries) if designing a system to recognize dogs.
3. Determine ways to get examples of confounding variations.
   Consider whether your samples cover the full distribution of
   values possible (for example, the full range of head poses) if
   designing a system to recognize dogs.
4. Label variation types in your evaluation datasets to enable
   robustness measurements against your release criteria. For
   instance, tag each example with metadata indicating whether it
   contains lighting variations, formatting changes, or
   background differences.

## Resources

**Related documents:**

- [What
  is Data Augmentation?](https://aws.amazon.com/what-is/data-augmentation/ "https://aws.amazon.com/what-is/data-augmentation/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.2 Data for development and enhancement
  of AI system
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems

**Related videos:**

- [Augmenting
  Datasets using Generative AI and Amazon Sagemaker for
  Autonomous Driving Use Cases on AWS](https://aws.amazon.com/blogs/industries/augmenting-datasets-using-generative-ai-and-amazon-sagemaker-for-autonomous-driving-use-cases-on-aws/ "https://aws.amazon.com/blogs/industries/augmenting-datasets-using-generative-ai-and-amazon-sagemaker-for-autonomous-driving-use-cases-on-aws/")

**Related tools:**

- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [Data
  transformation workloads with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [Transform
  data with SageMaker AI Data Wrangler](../../../sagemaker/latest/dg/data-wrangler-transform.md "../../../sagemaker/latest/dg/data-wrangler-transform.md")
