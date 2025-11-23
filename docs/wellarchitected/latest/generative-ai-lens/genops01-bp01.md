# GENOPS01-BP01 Periodically evaluate functional

performance

Implement periodic evaluations using stratified sampling and custom
metrics to maintain the performance and reliability of large
language models. This practice verifies that models remain accurate
and relevant over time by regularly assessing their performance
against ground truth data and specific evaluation criteria. By
employing stratified sampling, organizations can obtain a
representative subset of data that reflects the diversity of
real-world inputs, leading to more reliable performance metrics.
Custom metrics allow for tailored assessments that align with
specific business goals and user expectations. This practice helps
customers achieve consistent model performance, detect and address
model drift promptly, and integrate evaluation results into
continuous improvement processes.

**Desired outcome:** When
implemented, this best practice improves the ability to identify and
remediate performance degradation issues in model responses.

**Benefits of establishing this best
practice:**

- [Implement
  observability for actionable insights](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Model responses
  to prompts can be observed using key performance indicators
  (KPIs) to determine adherence to or deviation from acceptable
  performance levels.
- [Anticipate
  failure](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Periodic review of the model's performance
  levels helps you proactively identify deviations in its
  performance. This is because foundation models are inherently
  non-deterministic with a realistic chance of failure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Evaluations can be conducted by periodically running ground truth
data and applying sampling techniques to run metrics for
monitoring purposes. Feed your prompts into the model to generate
outputs, compare those outputs to the known ground truth values,
and analyze the results to track the model's performance over
time, identifying potential drifts or degradation.

You can employ stratified sampling techniques to verify diverse
data representation within the sample set. Divide your ground
truth data into relevant categories (for example, different user
personas), and randomly sample from each category to provide a
balanced representation in the evaluation set. Consider
periodically updating your ground truth dataset as the inputs and
usage of your workload change over time. Address data drift where
actual usage diverges from your initial ground truth set.

You can use the model evaluation feature built-in with Amazon Bedrock or open-source libraries like
[fmeval](https://github.com/aws/fmeval "https://github.com/aws/fmeval") or
[ragas](https://docs.ragas.io/en/stable/ "https://docs.ragas.io/en/stable/").
Use Amazon Bedrock model invocation logging to collect metadata,
requests, and responses for model invocations in your account.

For Amazon SageMaker AI, you can set up manual evaluations for a
human workforce using Studio, automatically evaluate your model
with an algorithm using Studio, or automatically evaluate your
model with a customized workflow using the fmeval library.

The fmeval library provides a framework for defining and using
custom metrics. By creating a custom metric class, you can
encapsulate the logic for calculating a specific evaluation
criterion tailored to your use case. Use this to continuously
assess your language models using both standard metrics provided
by fmeval and your own specialized metrics.

Your organization’s AI policy should define the effective minimum performance levels for generative AI workloads, as well as how to validate performance on an ongoing basis. Consider identifying a single-threaded workload owner responsible for the operational considerations pertaining to ongoing performance evaluations. Run these evaluations when new candidate models are available, or when model customization techniques are applied. For example, fine-tuned and customized models should be subject to the same evaluation criteria and cadence as non-customized models.

### Implementation steps

1. Create a ground truth dataset.
   - Verify that you have diverse data representation
   - Consider various user personas and use cases

2. Apply stratified sampling techniques.
   - Categorize ground truth data into relevant groups
   - Randomly sample from each group to achieve balanced
     representation

3. Establish periodic evaluation processes.
   - For Amazon Bedrock:
     - Use the built-in model evaluation feature
     - Implement model invocation logging

   - For Amazon SageMaker AI:
     - Configure manual evaluations using Amazon SageMaker AI
       Studio.
     - Set up automatic evaluations using Amazon SageMaker AI
       Studio or the fmeval library

4. Define custom metrics.
   - Use the fmeval library to create custom metric classes
   - Encapsulate logic for calculating specific evaluation
     criteria

5. Perform model evaluations.
   - Input prompts into the model
   - Generate outputs and compare them to ground truth values
   - Analyze results to track performance over time

6. Monitor for performance drifts.
   - Identify potential degradation in model performance
   - Address data drift where actual usage diverges from the
     initial ground truth

7. Regularly update the ground truth dataset.
   - Reflect changes in workload inputs and usage patterns
   - Maintain the relevance of evaluation data

**Additional recommendations**

- Use open-source libraries.
  - Consider using libraries like ragas for additional
    evaluation capabilities
  - Explore complementary metrics and evaluation techniques

- Implement automated workflows.
  - Integrate evaluation processes into CI/CD pipelines
  - Set up alerts for significant performance changes

## Resources

**Related best practices:**

- [OPS11-BP11](../operational-excellence-pillar/ops_evolve_ops_metrics_review.md "../operational-excellence-pillar/ops_evolve_ops_metrics_review.md")

**Related documents:**

- [Amazon SageMaker AI Model Evaluation](../../../sagemaker/latest/dg/model-optimize-evaluate.md "../../../sagemaker/latest/dg/model-optimize-evaluate.md")
- [Evaluating
  Models in Amazon Bedrock](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")

**Related videos:**

- [AWS re:Invent 2024 - Streamline RAG and model evaluation with
  Amazon Bedrock (AIM359)](https://www.youtube.com/watch?v=7BP9nwFlFws "https://www.youtube.com/watch?v=7BP9nwFlFws")

**Related examples:**

- [SageMaker AI
  Model Evaluation Examples](../../../sagemaker/latest/dg/ex1-test-model.md "../../../sagemaker/latest/dg/ex1-test-model.md")
- [Bedrock
  Model Evaluation Demo](https://aws.amazon.com/awstv/watch/1a5442fac30/ "https://aws.amazon.com/awstv/watch/1a5442fac30/")
- [Examples
  with fmeval](https://github.com/aws/fmeval/tree/main/examples "https://github.com/aws/fmeval/tree/main/examples")

**Related tools:**

- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [fmeval
  library](https://github.com/aws/fmeval "https://github.com/aws/fmeval")
- [Amazon CloudWatch](../../../sagemaker/latest/dg/monitoring-cloudwatch.md "../../../sagemaker/latest/dg/monitoring-cloudwatch.md")
- [AWS Step Functions](https://aws.amazon.com/blogs/aws/build-generative-ai-apps-using-aws-step-functions-and-amazon-bedrock/ "https://aws.amazon.com/blogs/aws/build-generative-ai-apps-using-aws-step-functions-and-amazon-bedrock/")
