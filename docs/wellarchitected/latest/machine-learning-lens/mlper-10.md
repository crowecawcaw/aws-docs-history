# MLPER-10: Detect performance issues when using transfer learning

Monitor and ensure that the inherited prediction weights from a
transferred model yield the desired results. This approach helps
minimize the risk of weak learning and incorrect outputs using
pre-trained models.

## Implementation plan

- **Use Amazon SageMaker AI
  Debugger** - Transfer learning is a machine
  learning technique where a model pre-trained on one task
  is fine-tuned on a new task. When using the transfer
  learning approach,
  use [Amazon SageMaker AI Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md") to detect hidden problems that
  might have serious consequences. Examine model predictions
  to see what mistakes were made. Validate the robustness of
  your model, and consider how much of this robustness is
  from the inherited capabilities. Validate input and
  preprocesses to the model for realistic expectations.

## Blogs

- [When
  does transfer learning work?](https://www.amazon.science/blog/when-does-transfer-learning-work "https://www.amazon.science/blog/when-does-transfer-learning-work")
- [Detecting
  hidden but non-trivial problems in transfer learning
  models using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/detecting-hidden-but-non-trivial-problems-in-transfer-learning-models-using-amazon-sagemaker-debugger/ "https://aws.amazon.com/blogs/machine-learning/detecting-hidden-but-non-trivial-problems-in-transfer-learning-models-using-amazon-sagemaker-debugger/")
  [Debugger](https://aws.amazon.com/blogs/machine-learning/detecting-hidden-but-non-trivial-problems-in-transfer-learning-models-using-amazon-sagemaker-debugger/ "https://aws.amazon.com/blogs/machine-learning/detecting-hidden-but-non-trivial-problems-in-transfer-learning-models-using-amazon-sagemaker-debugger/")
