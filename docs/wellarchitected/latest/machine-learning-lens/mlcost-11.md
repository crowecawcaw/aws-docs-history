# MLCOST-11: Select local training for small scale experiments

Evaluate the requirements to train an ML model in the cloud
versus on a local machine. Use local option when experimenting
across different algorithms and configurations with small data
sizes. For large data, launch a cloud-based training cluster
with one or more compute instances. Right size the compute
instances in the training cluster based on the workload.

## Implementation plan

- **Use Amazon SageMaker AI** - While experimenting with training a model with small datasets, use Amazon SageMaker AI notebook [local](https://aws.amazon.com/blogs/machine-learning/use-the-amazon-sagemaker-local-mode-to-train-on-your-notebook-instance/ "https://aws.amazon.com/blogs/machine-learning/use-the-amazon-sagemaker-local-mode-to-train-on-your-notebook-instance/") mode. This will train your model on the notebook instance itself, instead of on a separate managed training cluster. You can iterate and test your work without having to wait for a new training or hosting cluster each time. This saves both time and cost associated with creating a managed training cluster.

Experimentation can also occur outside of a notebook, for example on a local machine. From your local machine, you can use the [SageMaker AI SDK](https://github.com/aws/sagemaker-python-sdk "https://github.com/aws/sagemaker-python-sdk") to train and deploy models on AWS.

## Blogs

- [Use
  the Amazon SageMaker AI local mode to train on your notebook
  instance](https://aws.amazon.com/blogs/machine-learning/use-the-amazon-sagemaker-local-mode-to-train-on-your-notebook-instance/ "https://aws.amazon.com/blogs/machine-learning/use-the-amazon-sagemaker-local-mode-to-train-on-your-notebook-instance/")

## Videos

- [Train
  with Amazon SageMaker AI on your local machine](https://www.youtube.com/watch?v=K3ngZKF31mc "https://www.youtube.com/watch?v=K3ngZKF31mc")

## Examples

- [Multiple
  examples showing how to run SageMaker AI in local mode](https://github.com/aws-samples/amazon-sagemaker-local-mode "https://github.com/aws-samples/amazon-sagemaker-local-mode")
