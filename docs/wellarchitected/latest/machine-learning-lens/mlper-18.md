# MLPER-18: Include human-in-the-loop monitoring

Use human-in-the-loop monitoring to monitor model performance
efficiently. When automating decision processes, the human
labeling of model results is a reliable quality test for model
inferences.

Compare human labels with model inferences to estimate model performance degradation.
Perform mitigation as model re-training.

## Implementation plan

- **Use Amazon Augmented AI to get
  human review** - Learn how to design a quality
  assurance system for model inferences. Establish a team
  of subject matter experts to audit model inference in
  production. Use
  [Amazon
  Augmented AI](https://aws.amazon.com/augmented-ai/ "https://aws.amazon.com/augmented-ai/") (Amazon A2I) to get human review of
  low-confidence predictions or random prediction samples.
  Amazon A2I uses resources in
  [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md"),
  [SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md"),
  and
  [Amazon](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")
  [S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")
  to create and run your human review workﬂows.

## Documents

- [Using
  Amazon Augmented AI for Human Review](../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md "../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md")

## Blogs

- [Human-in-the-loop
  review of model explanations with Amazon SageMaker AI
  Clarify and Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/")
- [Verifying
  and adjusting your data labels to create higher quality
  training datasets with Amazon](https://aws.amazon.com/blogs/machine-learning/verifying-and-adjusting-your-data-labels-to-create-higher-quality-training-datasets-with-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/verifying-and-adjusting-your-data-labels-to-create-higher-quality-training-datasets-with-amazon-sagemaker-ground-truth/")
  [SageMaker AI
  Ground Truth](https://aws.amazon.com/blogs/machine-learning/verifying-and-adjusting-your-data-labels-to-create-higher-quality-training-datasets-with-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/verifying-and-adjusting-your-data-labels-to-create-higher-quality-training-datasets-with-amazon-sagemaker-ground-truth/")

## Videos

- [Easily
  Implement Human in the Loop into Your Machine Learning
  Predictions with Amazon A2I](https://www.youtube.com/watch?v=jNUp1SO_0YU "https://www.youtube.com/watch?v=jNUp1SO_0YU")
