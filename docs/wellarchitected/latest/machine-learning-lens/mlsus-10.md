# MLSUS-10: Use efficient model tuning methods

Implement an efficient strategy to optimize hyperparameter
values to minimize the resources required to complete model
training. Avoid a brute force strategy wherever possible, as it
tests hyperparameter values without concern for the number of
resources used. 

## Implementation plan

- **Adopt sustainable tuning job
  strategy** -
  [Prefer
  Hyperband or Bayesian search over random search](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md")
  (and
  [avoid
  grid search](https://arxiv.org/pdf/1910.09700.pdf "https://arxiv.org/pdf/1910.09700.pdf")). Bayesian search makes intelligent
  guesses about the next set of parameters to pick based on
  the prior set of trials. It typically requires
  [10
  times fewer jobs](https://d1.awsstatic.com/events/reinvent/2019/NEW_LAUNCH_REPEAT_1_Optimizing_Your_Machine_Learning_Models_on_Amazon_SageMaker AI_AIM361-R1.pdf "https://d1.awsstatic.com/events/reinvent/2019/NEW_LAUNCH_REPEAT_1_Optimizing_Your_Machine_Learning_Models_on_Amazon_SageMaker AI_AIM361-R1.pdf") than random search, and thus 10
  times less compute resources, to find the best
  hyperparameters. SageMaker AI Automatic Model Tuning now
  supports Hyperband, a new search strategy that can find
  the optimal set of hyperparameters up to three times
  faster than Bayesian search for large-scale models such as
  deep neural networks that address computer vision
  problems.
- **Limit the maximum number of
  concurrent training jobs** - Running
  hyperparameter tuning jobs concurrently gets more work
  done quickly. However, with the Bayesian optimization
  strategy, a tuning job improves only through successive
  rounds of experiments. Typically, running one training job
  at a time achieves the best results with the least amount
  of compute resources.
- **Carefully choose the number of
  hyperparameters and their ranges** - You get
  better results and use less compute resources by limiting
  your search to a few parameters and small ranges of
  values. If you know that a hyperparameter is log-scaled,
  convert it to further improve the optimization.

## Documents

- [Perform
  Automatic Model Tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [Choosing
  the Best Number of Concurrent Training Jobs](../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-parallelism "../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-parallelism")
- [Choosing
  Hyperparameter Ranges](../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-choosing-ranges "../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-choosing-ranges")
- [Amazon SageMaker AI Automatic Model Tuning now provides up to 3x
  faster hyperparameter tuning with Hyperband as a new
  search strategy](https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-sagemaker-automatic-model-tuning-provides-faster-hyperparameter-tuning-hyperband-search-strategy/ "https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-sagemaker-automatic-model-tuning-provides-faster-hyperparameter-tuning-hyperband-search-strategy/")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 2, model
  development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/")
- [Amazon SageMaker AI automatic model tuning produces better models,
  faster](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-produces-better-models-faster/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-produces-better-models-faster/")
- [Amazon SageMaker AI Automatic Model Tuning: Using Machine Learning
  for Machine Learning](https://aws.amazon.com/blogs/aws/sagemaker-automatic-model-tuning/ "https://aws.amazon.com/blogs/aws/sagemaker-automatic-model-tuning/")
- [Amazon SageMaker AI Automatic Model Tuning now provides up to three times faster hyperparameter tuning with Hyperband](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-now-provides-up-to-three-times-faster-hyperparameter-tuning-with-hyperband/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-now-provides-up-to-three-times-faster-hyperparameter-tuning-with-hyperband/")

## Metrics

- Track the metrics related to the
  [resources
  provisioned for your hyperparameter tuning jobs](../../../sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.md#sagemaker-Type-HyperParameterTrainingJobDefinition-ResourceConfig "../../../sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.md#sagemaker-Type-HyperParameterTrainingJobDefinition-ResourceConfig") (InstanceCount, InstanceType, and VolumeSizeInGB)
- Measure
  the [efficient
  use of these resources](../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs "../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs") (CPUUtilization,
  GPUUtilization, GPUMemoryUtilization, MemoryUtilization,
  and DiskUtilization) in the
  [SageMaker AI Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm") and the
  [CloudWatch Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw")
