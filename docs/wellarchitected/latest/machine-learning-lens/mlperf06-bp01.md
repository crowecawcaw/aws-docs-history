# MLPERF06-BP01 Include human-in-the-loop monitoring

Including human-in-the-loop monitoring is an effective method for
efficiently tracking and maintaining model performance. By
incorporating human review into automated decision processes,
organizations can establish a reliable quality assurance mechanism
that validates model inferences and detects performance degradation
over time.

**Desired outcome:** You implement a
robust human-in-the-loop monitoring system that enables continuous
assessment of your machine learning models. You can compare human
labels with model inferences to detect model drift and performance
degradation, allowing timely mitigation through retraining or other
remediation actions. This creates a feedback loop that maintains
high model quality and reliability in production environments.

**Common anti-patterns:**

- Relying solely on automated metrics without human validation.
- Ignoring edge cases and low-confidence predictions.
- Not establishing a systematic review process for model outputs.
- Failing to incorporate human feedback into model retraining
  cycles.
- Using untrained reviewers without subject matter expertise.

**Benefits of establishing this best
practice:**

- Early detection of model drift and performance degradation.
- Higher quality assurance for critical model predictions.
- Better understanding of edge cases and model limitations.
- Continuous improvement of model performance through expert
  feedback.
- Increased trust in AI systems through human oversight.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Human-in-the-loop monitoring provides a crucial safety net for
your machine learning systems by adding appropriate human
oversight to important decisions. This approach is particularly
valuable when automated systems make predictions that impact
critical business processes or customer experiences. By
establishing a workflow where human experts review model outputs,
particularly those with low confidence or selected randomly for
quality assurance, you create a reliable mechanism to evaluate
model performance in real-world scenarios.

Avoid relying solely on automated metrics without human
validation. Many organizations ignore edge cases and
low-confidence predictions, don't establish a systematic review
process for model outputs, fail to incorporate human feedback into
model retraining cycles, and use untrained reviewers without
subject matter expertise.

This monitoring approach can identify when models begin to drift
or perform poorly on new data. The comparison between human labels
and model predictions serves as a key indicator of model health,
signaling when retraining or other interventions are necessary.
This feedback loop is essential for maintaining high-quality,
reliable AI systems over time.

### Implementation steps

1. **Design a quality assurance system
   for model inferences**. Create a comprehensive plan
   for how human review will integrate with your machine
   learning workflow. Determine which predictions will be sent
   for human review (low-confidence predictions, random
   samples, or high-risk categories) and establish clear
   guidelines for reviewers to follow when evaluating model
   outputs.
2. **Establish a team of subject matter
   experts**. Identify and recruit individuals with
   domain expertise who can accurately evaluate model
   inferences. These reviewers should understand both the
   technical aspects of your models and the business context in
   which they operate, allowing them to provide valuable
   feedback on model performance and identify potential issues.
3. **Implement Amazon Augmented AI for
   human review workflows**. Use
   [Amazon
   Augmented AI](../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md "../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md") (Amazon A2I) to create and manage human
   review workflows for your machine learning models. Amazon
   A2I integrates with other AWS services like
   [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md"),
   [Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md"), and
   [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") to handle the entire review process.
4. **Configure review criteria and
   thresholds**. Define the conditions that initiate
   human review, such as confidence score thresholds or types
   of predictions that require human validation. Set up rules
   in Amazon A2I to automatically route these cases to your
   human reviewers while allowing high-confidence, routine
   predictions to proceed without review.
5. **Develop feedback integration
   mechanisms**. Create systems to incorporate human
   feedback into your model improvement cycle. This includes
   storing human labels alongside model predictions, analyzing
   disagreement patterns, and using this information to
   identify areas where your model needs improvement.
6. **Monitor and analyze human-model
   agreement rates**. Track how often human reviewers
   agree with model predictions and analyze patterns in
   disagreements. This data can identify systematic issues with
   your model so that you can prioritize areas for improvement.
7. **Implement model retraining based on
   feedback**. Use the labeled data gathered through
   human review to periodically retrain your models. This
   creates a continuous improvement loop where your models
   learn from past mistakes and adapt to changing patterns in
   your data.
8. **Measure and optimize
   cost-effectiveness**. Analyze the ROI of your
   human-in-the-loop system by comparing the costs of human
   review with the benefits of improved model accuracy. Adjust
   your review sampling strategy to focus human attention where
   it provides the most value.

## Resources

**Related documents:**

- [Using
  Amazon Augmented AI for Human Review](../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md "../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md")
- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Customized
  model monitoring for near real-time batch inference with
  Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/customized-model-monitoring-for-near-real-time-batch-inference-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/customized-model-monitoring-for-near-real-time-batch-inference-with-amazon-sagemaker/")-
- [Human-in-the-loop
  review of model explanations with Amazon SageMaker AI Clarify and
  Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/")

**Related videos:**

- [Easily
  Implement Human in the Loop into Your Machine Learning
  Predictions with Amazon A2I](https://www.youtube.com/watch?v=jNUp1SO_0YU "https://www.youtube.com/watch?v=jNUp1SO_0YU")
- [Accelerate
  foundation model evaluation with Amazon SageMaker AI
  Clarify](https://www.youtube.com/watch?v=9X2oDkOBYyA "https://www.youtube.com/watch?v=9X2oDkOBYyA")
