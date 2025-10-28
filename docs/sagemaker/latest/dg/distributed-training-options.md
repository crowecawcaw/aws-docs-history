# Distributed computing with SageMaker AI best

practices

This best practices page presents various flavors of distributed computing for machine
learning (ML) jobs in general. The term _distributed computing_
in this page encompasses distributed training for machine learning tasks and parallel
computing for data processing, data generation, feature engineering, and reinforcement
learning. In this page, we discuss about common challenges in distributed computing, and
available options in SageMaker Training and SageMaker Processing. For additional reading materials
about distributed computing, see [What Is Distributed Computing?](https://aws.amazon.com/what-is/distributed-computing/ "https://aws.amazon.com/what-is/distributed-computing/").

You can configure ML tasks to run in a distributed manner across multiple nodes
(instances), accelerators (NVIDIA GPUs, AWS Trainium chips), and vCPU cores. By running
distributed computation, you can achieve a variety of goals such as computing operations
faster, handling large datasets, or training large ML models.

The following list covers common challenges that you might face when you run an ML
training job at scale.

- You need to make decisions on how to distribute computation depending on ML tasks,
  software libraries you want to use, and compute resources.
- Not all ML tasks are straightforward to distribute. Also, not all ML libraries
  support distributed computation.
- Distributed computation might not always result in a linear increase in compute
  efficiency. In particular, you need to identify if data I/O and inter-GPU
  communication have bottlenecks or cause overhead.
- Distributed computation might disturb numerical processes and change model
  accuracy. Specifically to data-parallel neural network training, when you change the
  global batch size while scaling up to a larger compute cluster, you also need to
  adjust the learning rate accordingly.
  SageMaker AI provides distributed training solutions to ease such challenges for various use
  cases. Choose one of the following options that best fits your use case.

###### Topics

- [Option 1: Use a SageMaker AI built-in algorithm
  that supports distributed training](#distributed-training-options-1 "#distributed-training-options-1")
- [Option 2: Run a custom ML code in the
  SageMaker AI managed training or processing environment](#distributed-training-options-2 "#distributed-training-options-2")
- [Option 3: Write your own custom
  distributed training code](#distributed-training-options-3 "#distributed-training-options-3")
- [Option 4: Launch multiple jobs in
  parallel or sequentially](#distributed-training-options-4 "#distributed-training-options-4")

## Option 1: Use a SageMaker AI built-in algorithm

that supports distributed training

SageMaker AI provides [built-in algorithms](algos.md "algos.md") that you can use out of the box through the SageMaker AI
console or the SageMaker Python SDK. Using the built-in algorithms, you don’t need to spend
time for code customization, understanding science behind the models, or running Docker
on provisioned Amazon EC2 instances.

A subset of the SageMaker AI built-in algorithms support distributed training. To check if the
algorithm of your choice supports distributed training, see the
**Parallelizable** column in the [Common Information About
Built-in Algorithms](common-info-all-im-models.md "common-info-all-im-models.md") table. Some of the algorithms support multi-instance
distributed training, while the rest of the parallelizable algorithms support
parallelization across multiple GPUs in a single instance, as indicated in the
**Parallelizable** column.

## Option 2: Run a custom ML code in the

SageMaker AI managed training or processing environment

SageMaker AI jobs can instantiate distributed training environment for specific use cases and
frameworks. This environment acts as a ready-to-use whiteboard, where you can bring and
run your own ML code.

### If your ML code uses a deep

learning framework

You can launch distributed training jobs using the [Deep Learning Containers
(DLC)](https://github.com/aws/deep-learning-containers "https://github.com/aws/deep-learning-containers") for SageMaker Training, which you can orchestrate either through the
dedicated Python modules in the [SageMaker AI
Python SDK](http://sagemaker.readthedocs.io/ "http://sagemaker.readthedocs.io/"), or through the SageMaker APIs with [AWS CLI](../../../cli/latest/reference/sagemaker/index.md "../../../cli/latest/reference/sagemaker/index.md"), [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html"). SageMaker AI provides training containers for machine learning
frameworks, including [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/index.html"), [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/index.html"), [Hugging Face Transformers](https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html"), and [Apache MXNet](https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/index.html"). You have two options to write deep learning code for
distributed training.

- **The SageMaker AI distributed training
  libraries**

The SageMaker AI distributed training libraries propose AWS-managed code for
neural network data parallelism and model parallelism. SageMaker AI distributed
training also comes with launcher clients built into the SageMaker Python SDK,
and you don’t need to author parallel launch code. To learn more, see [SageMaker AI's
data parallelism library](data-parallel.md "data-parallel.md") and [SageMaker AI's model parallelism
library](model-parallel.md "model-parallel.md").

- **Open-source distributed training
  libraries**

Open source frameworks have their own distribution mechanisms such as
[DistributedDataParallelism (DDP) in PyTorch](https://pytorch.org/docs/stable/notes/ddp.html "https://pytorch.org/docs/stable/notes/ddp.html") or
`tf.distribute` modules in TensorFlow. You can choose to run these
distributed training frameworks in the SageMaker AI-managed framework containers.
For example, the sample code for [training
MaskRCNN in SageMaker AI](https://github.com/aws-samples/amazon-sagemaker-cv "https://github.com/aws-samples/amazon-sagemaker-cv") shows how to use both PyTorch DDP in the SageMaker AI
PyTorch framework container and [Horovod](https://horovod.readthedocs.io/en/stable/ "https://horovod.readthedocs.io/en/stable/") in the
SageMaker TensorFlow framework container.

SageMaker AI ML containers also come with [MPI](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/mpi_on_sagemaker/intro/mpi_demo.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/mpi_on_sagemaker/intro/mpi_demo.ipynb") preinstalled, so you can parallelize your entry point script using
[mpi4py](https://mpi4py.readthedocs.io/en/stable/ "https://mpi4py.readthedocs.io/en/stable/"). Using the
MPI integrated training containers is a great option when you launch a third-party
distributed training launcher or write ad-hoc parallel code in the SageMaker AI managed
training environment.

Notes for data-parallel neural network training on
GPUs

- **Scale to multi-GPU and multi-machine parallelism
  when appropriate**

We often run neural network training jobs on multiple-CPU or multiple-GPU
instances. Each GPU-based instance usually contains multiple GPU devices.
Consequently, distributed GPU computing can happen either within a single
GPU instance with multiple GPUs (single-node multi-GPU training), or across
multiple GPU instances with multiple GPU cores in each (multi-node multi-GPU
training). Single-instance training is easier to write code and debug, and
the intra-node GPU-to-GPU throughput is usually faster than the inter-node
GPU-to-GPU throughput. Therefore, it is a good idea to scale data
parallelism vertically first (use one GPU instance with multiple GPUs) and
expand to multiple GPU instances if needed. This might not apply to cases
where the CPU budget is high (for example, a massive workload for data
pre-processing) and when the CPU-to-GPU ratio of a multi-GPU instance is too
low. In all cases, you need to experiment with different combinations of
instance types based on your own ML training needs and workload.

- **Monitor the quality of convergence**

When training a neural network with data parallelism, increasing the
number of GPUs while keeping the mini-batch size per GPU constant leads to
increasing the size of global mini-batch for the mini-batch stochastic
gradient descent (MSGD) process. The size of mini-batches for MSGD is known
to impact the descent noise and convergence. For properly scaling while
preserving accuracy, you need to adjust other hyperparameters such as the
learning rate [[Goyal et
al.](https://arxiv.org/abs/1706.02677 "https://arxiv.org/abs/1706.02677") (2017)].

- **Monitor I/O bottlenecks**

As you increase the number of GPUs, the throughput for reading and writing
storage should also increase. Make sure that your data source and pipeline
don’t become bottlenecks.

- **Modify your training script as
  needed**

Training scripts written for single-GPU training must be modified for
multi-node multi-GPU training. In most data parallelism libraries, script
modification is required to do the following.

    + Assign batches of training data to each GPU.
    + Use an optimizer that can deal with gradient computation and
     parameter updates across multiple GPUs.
    + Assign responsibility of checkpointing to a specific host and GPU.

### If your ML code involves tabular

data processing

PySpark is a Python frontend of Apache Spark, which is an open-source distributed
computing framework. PySpark has been widely adopted for distributed tabular data
processing for large-scale production workloads. If you want to run tabular data
processing code, consider using the [SageMaker Processing
PySpark containers](use-spark-processing-container.md "use-spark-processing-container.md") and running parallel jobs. You can also run data
processing jobs in parallel using SageMaker Training and SageMaker Processing APIs in
Amazon SageMaker Studio Classic, which is integrated with [Amazon EMR](https://aws.amazon.com/blogs/machine-learning/part-1-create-and-manage-amazon-emr-clusters-from-sagemaker-studio-to-run-interactive-spark-and-ml-workloads/ "https://aws.amazon.com/blogs/machine-learning/part-1-create-and-manage-amazon-emr-clusters-from-sagemaker-studio-to-run-interactive-spark-and-ml-workloads/") and [AWS Glue](https://aws.amazon.com/about-aws/whats-new/2022/09/sagemaker-studio-supports-glue-interactive-sessions/?nc1=h_ls "https://aws.amazon.com/about-aws/whats-new/2022/09/sagemaker-studio-supports-glue-interactive-sessions/?nc1=h_ls").

## Option 3: Write your own custom

distributed training code

When you submit a training or processing job to SageMaker AI, SageMaker Training and SageMaker AI
Processing APIs launch Amazon EC2 compute instances. You can customize training and
processing environment in the instances by running your own Docker container or
installing additional libraries in the AWS managed containers. For more information
about Docker with SageMaker Training, see [Adapting your own
Docker container to work with SageMaker AI](docker-containers-adapt-your-own.md "docker-containers-adapt-your-own.md") and [Create a container with your
own algorithms and models](docker-containers-create.md "docker-containers-create.md"). For more information about Docker with SageMaker AI
Processing, see [Use Your Own Processing
Code](use-your-own-processing-code.md "use-your-own-processing-code.md").

Every SageMaker training job environment contains a configuration file at
`/opt/ml/input/config/resourceconfig.json`, and every SageMaker Processing job
environment contains a similar configuration file at
`/opt/ml/config/resourceconfig.json`. Your code can read this file to
find `hostnames` and establish inter-node communications. To learn more,
including the schema of the JSON file, see [Distributed Training Configuration](your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training "your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training") and [How
Amazon SageMaker Processing Configures Your Processing Container](build-your-own-processing-container.md#byoc-config "build-your-own-processing-container.md#byoc-config"). You can also
install and use third-party distributed computing libraries such as [Ray](https://github.com/aws-samples/aws-samples-for-ray/tree/main/sagemaker "https://github.com/aws-samples/aws-samples-for-ray/tree/main/sagemaker") or DeepSpeed in SageMaker AI.

You can also use SageMaker Training and SageMaker Processing to run custom distributed
computations that do not require inter-worker communication. In the computing
literature, those tasks are often described as _embarrassingly
parallel_ or _share-nothing_. Examples
include parallel processing of data files, training models in parallel on different
configurations, or running batch inference on a collection of records. You can trivially
parallelize such share-nothing use cases with Amazon SageMaker AI. When you launch a SageMaker Training
or SageMaker Processing job on a cluster with multiple nodes, SageMaker AI by default replicates and
launches your training code (in Python or Docker) on all the nodes. Tasks requiring
random spread of input data across such multiple nodes can be facilitated by setting
`S3DataDistributionType=ShardedByS3Key` in the data input configuration
of the SageMaker AI `TrainingInput` API.

## Option 4: Launch multiple jobs in

parallel or sequentially

You can also distribute an ML compute workflow into smaller parallel or sequential
compute tasks, each represented by its own SageMaker Training or SageMaker Processing job.
Splitting a task into multiple jobs can be beneficial for the following situations or
tasks:

- When you have specific [data channels](model-train-storage.md "model-train-storage.md") and
  metadata entries (such as hyperparameters, model configuration, or instance
  types) for each sub-tasks.
- When you implement retry steps at a sub-task level.
- When you vary the configuration of the sub-tasks over the course of the
  workload, such as when training on increasing batch sizes.
- When you need to run an ML task that takes longer than the maximum training
  time allowed for a single training job (28 days maximum).
- When different steps of a compute workflow require different instance
  types.

For the specific case of hyperparameter search, use [SageMaker AI Automated Model
Tuning](automatic-model-tuning.md "automatic-model-tuning.md"). SageMaker AI Automated Model Tuning is a serverless parameter search
orchestrator that launches multiple training jobs on your behalf, according to a search
logic that can be random, Bayesian, or HyperBand.

Additionally, to orchestrate multiple training jobs, you can also consider workflow
orchestration tools, such as [SageMaker Pipelines](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/index.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/index.html"), [AWS Step Functions](../../../step-functions/latest/dg/connect-sagemaker.md "../../../step-functions/latest/dg/connect-sagemaker.md"),
and Apache Airflow supported by [Amazon Managed
Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/ "https://aws.amazon.com/managed-workflows-for-apache-airflow/") and [SageMaker AI Workflows](https://sagemaker.readthedocs.io/en/stable/workflows/airflow/using_workflow.html "https://sagemaker.readthedocs.io/en/stable/workflows/airflow/using_workflow.html").
