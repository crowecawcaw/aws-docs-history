# MLCOST-15: Use distributed training

Enable distributed training for a faster training time, when an
algorithm allows it. Use multiple instances in a training
cluster. Use managed services to help ensure all training
instances are automatically shut down when training is
completed.

## Implementation plan

- **Use Amazon SageMaker AI Distributed
  training libraries** - The
  [distributed
  training libraries](https://aws.amazon.com/sagemaker/distributed-training/ "https://aws.amazon.com/sagemaker/distributed-training/")in Amazon SageMaker AI
  automatically split large deep learning models and
  training datasets across AWS GPU instances in a fraction
  of the time it takes to do manually. SageMaker AI achieves
  these efficiencies through two techniques: data
  parallelism and model parallelism. Model parallelism
  splits models too large to fit on a single GPU into
  smaller parts before distributing across multiple GPUs to
  train, and data parallelism splits large datasets to train
  concurrently to improve training speed.

## Documents

- [SageMaker AI's
  Distributed Data Parallel Library](../../../sagemaker/latest/dg/data-parallel.md "../../../sagemaker/latest/dg/data-parallel.md")
- [SageMaker AI's
  Distributed Model Parallel](../../../sagemaker/latest/dg/model-parallel.md "../../../sagemaker/latest/dg/model-parallel.md")
- [Distributed
  Training](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/index.html "https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/index.html")

## Blogs

- [New
  – Data Parallelism Library in Amazon SageMaker AI Simplifies
  Training on Large Datasets](https://aws.amazon.com/blogs/aws/managed-data-parallelism-in-amazon-sagemaker-simplifies-training-on-large-datasets/ "https://aws.amazon.com/blogs/aws/managed-data-parallelism-in-amazon-sagemaker-simplifies-training-on-large-datasets/")
- [How
  Latent Space used the Amazon SageMaker AI model parallelism
  library to push the frontiers of](https://aws.amazon.com/blogs/machine-learning/how-latent-space-used-the-amazon-sagemaker-model-parallelism-library-to-push-the-frontiers-of-large-scale-transformers/ "https://aws.amazon.com/blogs/machine-learning/how-latent-space-used-the-amazon-sagemaker-model-parallelism-library-to-push-the-frontiers-of-large-scale-transformers/")
  [large-scale
  transformers](https://aws.amazon.com/blogs/machine-learning/how-latent-space-used-the-amazon-sagemaker-model-parallelism-library-to-push-the-frontiers-of-large-scale-transformers/ "https://aws.amazon.com/blogs/machine-learning/how-latent-space-used-the-amazon-sagemaker-model-parallelism-library-to-push-the-frontiers-of-large-scale-transformers/")
- [The
  science behind Amazon SageMaker AI’s distributed-training
  engines](https://www.amazon.science/latest-news/the-science-of-amazon-sagemakers-distributed-training-engines "https://www.amazon.science/latest-news/the-science-of-amazon-sagemakers-distributed-training-engines")
- [Amazon SageMaker AI XGBoost now offers fully distributed GPU
  training](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/")

## Videos

- [AWS re:Invent 2020: Train billion-parameter models with model
  parallelism on Amazon SageMaker AI](https://www.youtube.com/watch?v=vv52RsBM8o4&ab_channel=AWSEvents "https://www.youtube.com/watch?v=vv52RsBM8o4&ab_channel=AWSEvents")
- [AWS re:Invent 2020: Fast training and near-linear scaling with
  Data Parallel in Amazon SageMaker AI](https://www.youtube.com/watch?v=EXmz5g8F2zU&ab_channel=AWSEvents "https://www.youtube.com/watch?v=EXmz5g8F2zU&ab_channel=AWSEvents")

## Examples

- [Distributed
  Training](https://github.com/aws/amazon-sagemaker-examples/blob/master/training/distributed_training/index.rst "https://github.com/aws/amazon-sagemaker-examples/blob/master/training/distributed_training/index.rst")
- [Distributed
  training using Amazon SageMaker AI Distributed Data Parallel
  library and debugging using](https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger "https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger")
  [Amazon SageMaker AI Debugger](https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger "https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger")
- [SageMaker AI
  developer guide on distributed training](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/distributed-training.md#distributed-training-optimize "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/distributed-training.md#distributed-training-optimize")
