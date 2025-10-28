# Running training jobs on a heterogeneous

cluster

Using the heterogeneous cluster feature of SageMaker Training, you can run a training job with
multiple types of ML instances for a better resource scaling and utilization for different
ML training tasks and purposes. For example, if your training job on a cluster with GPU
instances suffers low GPU utilization and CPU bottleneck problems due to CPU-intensive
tasks, using a heterogeneous cluster can help offload CPU-intensive tasks by adding more
cost-efficient CPU instance groups, resolve such bottleneck problems, and achieve a better
GPU utilization.

###### Note

This feature is available in the SageMaker Python SDK v2.98.0 and later.

###### Note

This feature is available through the SageMaker AI [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html") and [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator") framework estimator classes. Supported frameworks are PyTorch
v1.10 or later and TensorFlow v2.6 or later.

See also the blog [Improve price performance of your model training using Amazon SageMaker AI heterogeneous clusters](https://aws.amazon.com/blogs/machine-learning/improve-price-performance-of-your-model-training-using-amazon-sagemaker-heterogeneous-clusters/ "https://aws.amazon.com/blogs/machine-learning/improve-price-performance-of-your-model-training-using-amazon-sagemaker-heterogeneous-clusters/").

###### Topics

- [Configure a training job with a
  heterogeneous cluster in Amazon SageMaker AI](train-heterogeneous-cluster-configure.md "train-heterogeneous-cluster-configure.md")
- [Run distributed
  training on a heterogeneous cluster in Amazon SageMaker AI](train-heterogeneous-cluster-configure-distributed.md "train-heterogeneous-cluster-configure-distributed.md")
- [Modify your
  training script to assign instance groups](train-heterogeneous-cluster-modify-training-script.md "train-heterogeneous-cluster-modify-training-script.md")
