# MLCOST-19: Use hyperparameter optimization technologies

Use automatic hyperparameter tuning to run many training jobs
and find the best version of your model. Use the algorithm and
ranges of hyperparameters that you specify. Use appropriate
hyperparameter ranges, as well as metrics that are realistic and
meet the business requirements.

## Implementation plan

- **Use SageMaker AI automatic model
  tuning** -
  [SageMaker AI
  automatic model tuning](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md"), also known as
  hyperparameter tuning, finds the optimal model by running
  many training jobs on your dataset. It uses the algorithm
  and ranges of hyperparameters that you specify. It then
  chooses the hyperparameter values that result in a model
  that performs the best, as measured by a metric that you
  choose. To create a new
  [hyperparameter
  optimization](../../../sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.md "../../../sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.md") (HPO) tuning job for one or more
  algorithms, you need to define the settings for the tuning
  job. Create training job definitions for each algorithm
  being tuned, and configure the resources for the tuning
  job.

## Documents

- [Create
  a HPO tuning job](../../../sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.md "../../../sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.md")

## Blogs

- [Running
  multiple HPO jobs in parallel on SageMaker AI](https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker "https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker")

## Videos

- [Automatic
  model tuning with SageMaker AI](https://www.youtube.com/watch?v=ynYnZywayC4 "https://www.youtube.com/watch?v=ynYnZywayC4")

## Examples

- [Large
  HPO polling examples](https://github.com/aws-samples/amazon-sagemaker-large-hpo-polling-examples "https://github.com/aws-samples/amazon-sagemaker-large-hpo-polling-examples")
