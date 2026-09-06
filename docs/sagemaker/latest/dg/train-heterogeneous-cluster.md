

# Running training jobs on a heterogeneous cluster
<a name="train-heterogeneous-cluster"></a>

Using the heterogeneous cluster feature of SageMaker Training, you can run a training job with multiple types of ML instances for a better resource scaling and utilization for different ML training tasks and purposes. For example, if your training job on a cluster with GPU instances suffers low GPU utilization and CPU bottleneck problems due to CPU-intensive tasks, using a heterogeneous cluster can help offload CPU-intensive tasks by adding more cost-efficient CPU instance groups, resolve such bottleneck problems, and achieve a better GPU utilization.

**Note**  
This feature is available in the SageMaker Python SDK v2.98.0 and later.

**Note**  
This feature is available through the SageMaker AI [ModelTrainer](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) class. Supported frameworks are PyTorch v1.10 or later and TensorFlow v2.6 or later.

See also the blog [Improve price performance of your model training using Amazon SageMaker AI heterogeneous clusters](https://aws.amazon.com/blogs/machine-learning/improve-price-performance-of-your-model-training-using-amazon-sagemaker-heterogeneous-clusters/).

**Topics**
+ [Configure a training job with a heterogeneous cluster in Amazon SageMaker AI](train-heterogeneous-cluster-configure.md)
+ [Run distributed training on a heterogeneous cluster in Amazon SageMaker AI](train-heterogeneous-cluster-configure-distributed.md)
+ [Modify your training script to assign instance groups](train-heterogeneous-cluster-modify-training-script.md)