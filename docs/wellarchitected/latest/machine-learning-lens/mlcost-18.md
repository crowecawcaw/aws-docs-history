# MLCOST-18: Use warm-start and checkpointing hyperparameter tuning

Where feasible, use warm start hyperparameter tuning. Warm start
can consist of using a parent job for a model trained previously
or using transfer learning. Warm start of hyperparameter tuning
jobs eliminates the need to start a tuning job from scratch.
Create a new hyperparameter tuning job that is based on selected
parent jobs or pre-trained models. Use checkpointing
capabilities to restart a training job from the last saved
checkpoint. Reuse previous trainings as prior knowledge, or use
checkpointing to accelerate the tuning process and reduce the
cost.

## Implementation plan

- **Use warm-start hyperparameter
  tuning** - Use
  [warmstart
  to start a hyperparameter tuning job](../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md "../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md") using one or
  more previous tuning jobs as a starting point. The results
  of previous tuning jobs are used to inform which
  combinations of hyperparameters to search over in the new
  tuning job. Hyperparameter tuning uses Bayesian or random
  search to choose combinations of hyperparameter values
  from ranges that you specify.
- **Use checkpointing hyperparameter
  tuning** - Use
  [checkpoints
  in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-checkpoints.md "../../../sagemaker/latest/dg/model-checkpoints.md") to save the state of ML models
  during training. Checkpoints are snapshots of the model
  and can be configured by the callback functions of ML
  frameworks. You can use the saved checkpoints to restart a
  training job from the last saved checkpoint.

## Blogs

- [Amazon SageMaker AI Automatic Model Tuning becomes more efficient
  with warm start of](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-becomes-more-efficient-with-warm-start-of-hyperparameter-tuning-jobs/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-becomes-more-efficient-with-warm-start-of-hyperparameter-tuning-jobs/")
  [hyperparameter
  tuning jobs](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-becomes-more-efficient-with-warm-start-of-hyperparameter-tuning-jobs/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-becomes-more-efficient-with-warm-start-of-hyperparameter-tuning-jobs/")
- [Running
  multiple HPO jobs in parallel on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/")

## Videos

- [Tune
  Your ML Models to the Highest Accuracy with Amazon SageMaker AIAutomatic Model Tuning](https://www.youtube.com/watch?v=xpZFNIOaQns "https://www.youtube.com/watch?v=xpZFNIOaQns")

## Examples

- [Automatic
  Model Tuning : Warm Starting Tuning Jobs](https://github.com/aws/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/image_classification_warmstart/hpo_image_classification_warmstart.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/image_classification_warmstart/hpo_image_classification_warmstart.ipynb")
