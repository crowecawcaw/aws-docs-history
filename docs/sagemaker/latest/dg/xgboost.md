# XGBoost algorithm with Amazon SageMaker AI

The [XGBoost](https://github.com/dmlc/xgboost "https://github.com/dmlc/xgboost") (eXtreme Gradient
Boosting) is a popular and efficient open-source implementation of the gradient boosted
trees algorithm. Gradient boosting is a supervised learning algorithm that tries to
accurately predict a target variable by combining multiple estimates from a set of simpler
models. The XGBoost algorithm performs well in machine learning competitions for the
following reasons:

- Its robust handling of a variety of data types, relationships,
  distributions.
- The variety of hyperparameters that you can fine-tune.
  You can use
  XGBoost for regression, classification (binary and multiclass), and ranking problems.

You can use the new release of the XGBoost algorithm as either:

- A Amazon SageMaker AI built-in algorithm.
- A framework to run training scripts in your local environments.
  This implementation has a smaller memory footprint, better logging, improved
  hyperparameter validation, and an bigger set of metrics than the original versions. It
  provides an XGBoost `estimator` that runs a training script in a managed XGBoost
  environment. The current release of SageMaker AI XGBoost is based on the original XGBoost versions
  1.0, 1.2, 1.3, 1.5, and 1.7.

For more information about the Amazon SageMaker AI XGBoost algorithm, see the following blog
posts:

- [Introducing the open-source Amazon SageMaker AI XGBoost algorithm container](https://aws.amazon.com/blogs/machine-learning/introducing-the-open-source-amazon-sagemaker-xgboost-algorithm-container/ "https://aws.amazon.com/blogs/machine-learning/introducing-the-open-source-amazon-sagemaker-xgboost-algorithm-container/")
- [Amazon SageMaker AI XGBoost now offers fully distributed GPU training](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/")

## Supported versions

- Framework (open source) mode: 1.2-1, 1.2-2, 1.3-1, 1.5-1, 1.7-1
- Algorithm mode: 1.2-1, 1.2-2, 1.3-1, 1.5-1, 1.7-1

###### Warning

Due to required compute capacity, version 1.7-1 of SageMaker AI XGBoost is not compatible with
GPU instances from the P2 instance family for training or inference.

###### Important

When you retrieve the SageMaker AI XGBoost image URI, do not use `:latest` or
`:1` for the image URI tag. You must specify one of the Supported versions to choose the SageMaker AI-managed XGBoost container with the native XGBoost package
version that you want to use. To find the package version migrated into the SageMaker AI
XGBoost containers, see [Docker Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"). Then choose your AWS Region,
and navigate to the **XGBoost (algorithm)**
section.

###### Warning

The XGBoost 0.90 versions are deprecated. Supports for security updates or bug fixes for
XGBoost 0.90 is discontinued. We highly recommend that you upgrade the XGBoost
version to one of the newer versions.

###### Note

XGBoost v1.1 is not supported on SageMaker AI. XGBoost 1.1 has a broken capability to run prediction
when the test input has fewer features than the training data in LIBSVM inputs. This
capability has been restored in XGBoost v1.2. Consider using SageMaker AI XGBoost 1.2-2 or
later.

###### Note

You can use XGBoost v1.0-1, but it's not officially supported.

## EC2 instance recommendation for the XGBoost

algorithm

SageMaker AI XGBoost supports CPU and GPU training and inference. Instance recommendations
depend on training and inference needs, as well as the version of the XGBoost algorithm.
Choose one of the following options for more information:

- [CPU training](#Instance-XGBoost-training-cpu "#Instance-XGBoost-training-cpu")
- [GPU training](#Instance-XGBoost-training-gpu "#Instance-XGBoost-training-gpu")
- [Distributed CPU training](#Instance-XGBoost-distributed-training-cpu "#Instance-XGBoost-distributed-training-cpu")
- [Distributed GPU training](#Instance-XGBoost-distributed-training-gpu "#Instance-XGBoost-distributed-training-gpu")
- [Inference](#Instance-XGBoost-inference "#Instance-XGBoost-inference")

### Training

The SageMaker AI XGBoost algorithm supports CPU and GPU training.

#### CPU training

SageMaker AI XGBoost 1.0-1 or earlier only trains using CPUs. It is a memory-bound (as
opposed to compute-bound) algorithm. So, a general-purpose compute instance (for
example, M5) is a better choice than a compute-optimized instance (for example,
C4). Further, we recommend that you have enough total memory in selected
instances to hold the training data. It supports the use of disk space to handle
data that does not fit into main memory. This is a result of the out-of-core
feature available with the libsvm input mode. Even so, writing cache files onto
disk slows the algorithm processing time.

#### GPU training

SageMaker AI XGBoost version 1.2-2 or later supports GPU training. Despite higher
per-instance costs, GPUs train more quickly, making them more cost effective.

SageMaker AI XGBoost version 1.2-2 or later supports P2, P3, G4dn, and G5 GPU instance families.

SageMaker AI XGBoost version 1.7-1 or later supports P3, G4dn, and G5 GPU instance families. Note that due to compute capacity requirements, version 1.7-1 or later does not support the P2 instance family.

To take advantage of GPU training:

- Specify the instance type as one of the GPU instances (for example, P3)
- Set the `tree_method` hyperparameter to `gpu_hist` in your
  existing XGBoost script

### Distributed training

SageMaker AI XGBoost supports CPU and GPU instances for distributed training.

#### Distributed CPU training

To run CPU training on multiple instances, set the `instance_count`
parameter for the estimator to a value greater than one. The input data must be
divided between the total number of instances.

##### Divide input data across instances

Divide the input data using the following steps:

1. Break the input data down into smaller files. The number of files
   should be at least equal to the number of instances used for distributed
   training. Using multiple smaller files as opposed to one large file also
   decreases the data download time for the training job.
2. When creating your [TrainingInput](https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html "https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html"), set the distribution parameter to
   `ShardedByS3Key`. With this, each instance gets
   approximately _1/n_ of the number of files in S3
   if there are _n_ instances specified in the
   training job.

#### Distributed GPU training

You can use distributed training with either single-GPU or multi-GPU instances.

**Distributed training with single-GPU instances**

SageMaker AI XGBoost versions 1.2-2 through 1.3-1 only support single-GPU
instance training. This means that even if you select a multi-GPU instance, only
one GPU is used per instance.

You must divide your input data between the total number of instances if:

- You use XGBoost versions 1.2-2 through 1.3-1.
- You do not need to use multi-GPU instances.

For more information, see [Divide input data across instances](#Instance-XGBoost-distributed-training-divide-data "#Instance-XGBoost-distributed-training-divide-data").

###### Note

Versions 1.2-2 through 1.3-1 of SageMaker AI XGBoost only use one GPU per instance
even if you choose a multi-GPU instance.

**Distributed training with multi-GPU
instances**

Starting with version 1.5-1, SageMaker AI XGBoost offers distributed GPU training
with [Dask](https://www.dask.org/ "https://www.dask.org/"). With Dask you can utilize
all GPUs when using one or more multi-GPU instances. Dask also works when using
single-GPU instances.

Train with Dask using the following steps:

1. Either omit the `distribution` parameter in your [TrainingInput](https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html "https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html") or set it to
   `FullyReplicated`.
2. When defining your hyperparameters, set `use_dask_gpu_training` to
   `"true"`.

###### Important

Distributed training with Dask only supports CSV and Parquet input formats. If you use other
data formats such as LIBSVM or PROTOBUF, the training job fails.

For Parquet data, ensure that the column names are saved as strings.
Columns that have names of other data types will fail to load.

###### Important

Distributed training with Dask does not support pipe mode. If pipe mode is
specified, the training job fails.

There are a few considerations to be aware of when training SageMaker AI XGBoost with
Dask. Be sure to split your data into smaller files. Dask reads each Parquet
file as a partition. There is a Dask worker for every GPU. As a result, the
number of files should be greater than the total number of GPUs (instance count \* number of GPUs per instance). Having a very large number of files can also
degrade performance. For more information, see [Dask Best
Practices](https://docs.dask.org/en/stable/best-practices.html "https://docs.dask.org/en/stable/best-practices.html").

#### Variations in output

The specified `tree_method` hyperparameter determines the algorithm
that is used for XGBoost training. The tree methods `approx`,
`hist` and `gpu_hist` are all approximate methods and
use sketching for quantile calculation. For more information, see [Tree
Methods](https://xgboost.readthedocs.io/en/stable/treemethod.html "https://xgboost.readthedocs.io/en/stable/treemethod.html") in the XGBoost documentation. Sketching is an approximate
algorithm. Therefore, you can expect variations in the model depending on
factors such as the number of workers chosen for distributed training. The
significance of the variation is data-dependent.

### Inference

SageMaker AI XGBoost supports CPU and GPU instances for inference. For information about the
instance types for inference, see [Amazon SageMaker AI ML Instance
Types](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
