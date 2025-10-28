# Distributed training in Amazon SageMaker AI

SageMaker AI provides distributed training libraries and supports various distributed training
options for deep learning tasks such as computer vision (CV) and natural language processing
(NLP). With SageMaker AI’s distributed training libraries, you can run highly scalable and
cost-effective custom data parallel and model parallel deep learning training jobs. You can also
use other distributed training frameworks and packages such as PyTorch DistributedDataParallel
(DDP), `torchrun`, MPI (`mpirun`), and parameter server. The following
section gives information about fundamental distributed training concepts. Throughout the
documentation, instructions and examples focus on how to set up the distributed training options
for deep learning tasks using the SageMaker Python SDK.

###### Tip

To learn best practices for distributed computing of machine learning (ML) training and
processing jobs in general, see [Distributed computing with SageMaker AI best
practices](distributed-training-options.md "distributed-training-options.md").

## Distributed training concepts

SageMaker AI’s distributed training libraries use the following distributed training terms and
features.

**Datasets and Batches**

- **Training Dataset**: All of the data you use to train
  the model.
- **Global batch size**: The number of records selected
  from the training dataset in each iteration to send to the GPUs in the cluster. This is
  the number of records over which the gradient is computed at each iteration. If data
  parallelism is used, it is equal to the total number of model replicas multiplied by the
  per-replica batch size: `global batch size = (the number of model replicas) *
(per-replica batch size)`. A single batch of global batch size is often referred
  to as the _mini-batch_ in machine learning
  literature.
- **Per-replica batch size:** When data parallelism is
  used, this is the number of records sent to each model replica. Each model replica
  performs a forward and backward pass with this batch to calculate weight updates. The
  resulting weight updates are synchronized (averaged) across all replicas before the next
  set of per-replica batches are processed.
- **Micro-batch**: A subset of the mini-batch or, if hybrid
  model and data parallelism is used , it is a subset of the per-replica sized batch . When
  you use SageMaker AI’s distributed model parallelism library, each micro-batch is fed into
  the training pipeline one-by-one and follows an [execution schedule](model-parallel-core-features.md#model-parallel-pipeline-execution "model-parallel-core-features.md#model-parallel-pipeline-execution") defined by the library's runtime.

**Training**

- **Epoch**: One training cycle through the entire dataset.
  It is common to have multiple iterations per an epoch. The number of epochs you use in
  training is unique on your model and use case.
- **Iteration**: A single forward and backward pass
  performed using a global batch sized batch (a mini-batch) of training data. The number of
  iterations performed during training is determined by the global batch size and the number
  of epochs used for training. For example, if a dataset includes 5,000 samples, and you use
  a global batch size of 500, it will take 10 iterations to complete a single epoch.
- **Learning rate**: A variable that influences the amount
  that weights are changed in response to the calculated error of the model. The learning
  rate plays an important role in the model’s ability to converge as well as the speed and
  optimality of convergence.

**Instances and GPUs**

- **Instances**: An AWS [machine learning compute
  instance](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/"). These are also referred to as _nodes_.
- **Cluster size**: When using SageMaker AI's distributed training
  library, this is the number of instances multiplied by the number of GPUs in each
  instance. For example, if you use two ml.p3.8xlarge instances in a training job, which
  have 4 GPUs each, the cluster size is 8. While increasing cluster size can lead to faster
  training times, communication between instances must be optimized; Otherwise,
  communication between the nodes can add overhead and lead to slower training times. The
  SageMaker AI distributed training library is designed to optimize communication between Amazon EC2 ML
  compute instances, leading to higher device utilization and faster training times.

**Distributed Training Solutions**

- **Data parallelism**: A strategy in distributed training
  where a training dataset is split up across multiple GPUs in a compute cluster, which
  consists of multiple Amazon EC2 ML Instances. Each GPU contains a _replica_ of the model, receives different batches of training data, performs
  a forward and backward pass, and shares weight updates with the other nodes for
  synchronization before moving on to the next batch and ultimately another epoch.
- **Model parallelism**: A strategy in distributed training
  where the model partitioned across multiple GPUs in a compute cluster, which consists of
  multiple Amazon EC2 ML Instances. The model might be complex and have a large number of hidden
  layers and weights, making it unable to fit in the memory of a single instance. Each GPU
  carries a subset of the model, through which the data flows and the transformations are
  shared and compiled. The efficiency of model parallelism, in terms of GPU utilization and
  training time, is heavily dependent on how the model is partitioned and the execution
  schedule used to perform forward and backward passes.
- **Pipeline Execution Schedule** (**Pipelining**): The pipeline execution schedule determines the order in which
  computations (micro-batches) are made and data is processed across devices during model
  training. Pipelining is a technique to achieve true parallelization in model parallelism
  and overcome the performance loss due to sequential computation by having the GPUs compute
  simultaneously on different data samples. To learn more, see [Pipeline Execution Schedule](model-parallel-core-features.md#model-parallel-pipeline-execution "model-parallel-core-features.md#model-parallel-pipeline-execution").

### Advanced concepts

Machine Learning (ML) practitioners commonly face two scaling challenges when training
models: _scaling model size_ and _scaling training data_. While model size and complexity can result in better
accuracy, there is a limit to the model size you can fit into a single CPU or GPU.
Furthermore, scaling model size may result in more computations and longer training
times.

Not all models handle training data scaling equally well because they need to ingest all
the training data _in memory_ for training. They only scale
vertically, and to bigger and bigger instance types. In most cases, scaling training data
results in longer training times.

Deep Learning (DL) is a specific family of ML algorithms consisting of several layers of
artificial neural networks. The most common training method is with mini-batch Stochastic
Gradient Descent (SGD). In mini-batch SGD, the model is trained by conducting small iterative
changes of its coefficients in the direction that reduces its error. Those iterations are
conducted on equally sized subsamples of the training dataset called _mini-batches_. For each mini-batch, the model is run in each record of the
mini-batch, its error measured and the gradient of the error estimated. Then the average
gradient is measured across all the records of the mini-batch and provides an update direction
for each model coefficient. One full pass over the training dataset is called an _epoch_. Model trainings commonly consist of dozens to hundreds of
epochs. Mini-batch SGD has several benefits: First, its iterative design makes training time
theoretically linear of dataset size. Second, in a given mini-batch each record is processed
individually by the model without need for inter-record communication other than the final
gradient average. The processing of a mini-batch is consequently particularly suitable for
parallelization and distribution. 

Parallelizing SGD training by distributing the records of a mini-batch over different
computing devices is called *data parallel distributed
training*, and is the most commonly used DL distribution paradigm. Data parallel
training is a relevant distribution strategy to scale the mini-batch size and process each
mini-batch faster. However, data parallel training comes with the extra complexity of having
to compute the mini-batch gradient average with gradients coming from all the workers and
communicating it to all the workers, a step called _allreduce_ that can represent a growing overhead, as the training cluster is
scaled, and that can also drastically penalize training time if improperly implemented or
implemented over improper hardware subtracts. 

Data parallel SGD still requires developers to be able to fit at least the model and a
single record in a computing device, such as a single CPU or GPU. When training very large
models such as large transformers in Natural Language Processing (NLP), or segmentation models
over high-resolution images, there may be situations in which this is not feasible. An
alternative way to break up the workload is to partition the model over multiple computing
devices, an approach called _model-parallel distributed
training_.
