# Run hybrid workloads with PennyLane embedded simulators

Lets look at how you can use embedded simulators from PennyLane on Amazon Braket Hybrid
Jobs to run hybrid workloads. Pennylane's GPU-based embedded simulator,
`lightning.gpu`, uses the [Nvidia cuQuantum library](https://developer.nvidia.com/cuquantum-sdk "https://developer.nvidia.com/cuquantum-sdk") to
accelerate circuit simulations. The embedded GPU simulator is pre-configured in all of the
Braket [job containers](https://github.com/amazon-braket/amazon-braket-containers "https://github.com/amazon-braket/amazon-braket-containers") that users can use out of the box. In this page, we show you how
to use `lightning.gpu` to speed up your hybrid workloads.

## Using `lightning.gpu` for QAOA workloads

Consider the Quantum Approximate Optimization Algorithm (QAOA) examples from this
[notebook](https://github.com/amazon-braket/amazon-braket-examples/tree/main/examples/hybrid_jobs/2_Using_PennyLane_with_Braket_Hybrid_Jobs "https://github.com/amazon-braket/amazon-braket-examples/tree/main/examples/hybrid_jobs/2_Using_PennyLane_with_Braket_Hybrid_Jobs"). To select an embedded simulator, you specify the
`device` argument to be a string of the form:
`"local:<provider>/<simulator_name>"`. For example, you would
set `"local:pennylane/lightning.gpu"` for `lightning.gpu`. The
device string you give to the Hybrid Job when you launch is passed to the job as the
environment variable `"AMZN_BRAKET_DEVICE_ARN"`.

```
device_string = os.environ["AMZN_BRAKET_DEVICE_ARN"]
prefix, device_name = device_string.split("/")
device = qml.device(simulator_name, wires=n_wires)
```

In this page, compare the two embedded PennyLane state vector simulators
`lightning.qubit` (which is CPU-based) and `lightning.gpu`
(which is GPU-based). Provide the simulators with custom gate
decompositions to compute various gradients.

Now you are ready to prepare the hybrid job launching script. Run the QAOA algorithm
using two instance types: `m5.2xlarge` and `p3.2xlarge`. The
`m5.2xlarge` instance type is comparable to a standard developer laptop.
The `p3.2xlarge` is an accelerated computing instance that has a single
NVIDIA Volta GPU with 16GB of memory.

The `hyperparameters` for all your hybrid jobs will be the same. All you need to
do to try out different instances and simulators is change two lines as follows.

```
# Specify device that the hybrid job will primarily be targeting
device = "local:pennylane/lightning.qubit"
# Run on a CPU based instance with about as much power as a laptop
instance_config = InstanceConfig(instanceType='ml.m5.2xlarge')
```

or:

```
# Specify device that the hybrid job will primarily be targeting
device = "local:pennylane/lightning.gpu"
# Run on an inexpensive GPU based instance
instance_config = InstanceConfig(instanceType='ml.p3.2xlarge')
```

###### Note

If you specify the `instance_config` as using a GPU-based instance, but
choose the `device` to be the embedded CPU-based simulator
(`lightning.qubit`), the GPU **will
not** be used. Make sure to use the embedded GPU-based simulator if you
wish to target the GPU!

First, you can create two hybrid jobs and solve Max-Cut with QAOA on a graph with 18
vertices. This translates to an 18-qubit circuit—relatively small and feasible to run
quickly on your laptop or the `m5.2xlarge` instance.

```
num_nodes = 18
num_edges = 24
seed = 1967

graph = nx.gnm_random_graph(num_nodes, num_edges, seed=seed)

# And similarly for the p3 job
m5_job = AwsQuantumJob.create(
    device=device,
    source_module="qaoa_source",
    job_name="qaoa-m5-" + str(int(time.time())),
    image_uri=image_uri,
    # Relative to the source_module
    entry_point="qaoa_source.qaoa_algorithm_script",
    copy_checkpoints_from_job=None,
    instance_config=instance_config,
    # general parameters
    hyperparameters=hyperparameters,
    input_data={"input-graph": input_file_path},
    wait_until_complete=True,
)
```

The mean iteration time for the `m5.2xlarge` instance is about 25 seconds,
while for the `p3.2xlarge` instance it is about 12 seconds. For this 18-qubit
workflow, the GPU instance gives us a 2x speedup. If you look at the Amazon Braket Hybrid
Jobs [pricing
page](https://aws.amazon.com/braket/pricing/ "https://aws.amazon.com/braket/pricing/"), you can see that the cost per minute for an `m5.2xlarge`
instance is $0.00768, while for the `p3.2xlarge` instance it is $0.06375. To
run for 5 total iterations, as you did here, would cost $0.016 using the CPU instance or
$0.06375 using the GPU instance — both pretty inexpensive!

Now solve a Max-Cut problem on a 24-vertex
graph, which will translate to 24 qubits. Run the hybrid jobs again on the same two instances
and compare the cost.

###### Note

Time to run this hybrid job on the CPU instance may be about five hours.

```
num_nodes = 24
num_edges = 36
seed = 1967

graph = nx.gnm_random_graph(num_nodes, num_edges, seed=seed)

# And similarly for the p3 job
m5_big_job = AwsQuantumJob.create(
    device=device,
    source_module="qaoa_source",
    job_name="qaoa-m5-big-" + str(int(time.time())),
    image_uri=image_uri,
    # Relative to the source_module
    entry_point="qaoa_source.qaoa_algorithm_script",
    copy_checkpoints_from_job=None,
    instance_config=instance_config,
    # general parameters
    hyperparameters=hyperparameters,
    input_data={"input-graph": input_file_path},
    wait_until_complete=True,
)
```

The mean iteration time for the `m5.2xlarge` instance is about an hour,
while the `p3.2xlarge` instance is about two minutes. For this larger
problem, the GPU instance is an order of magnitude faster. All you had to do to benefit
from this speedup was to change two lines of code, swapping out the instance type and
the local simulator used. To run for 5 total iterations, as was done here, would cost
about $2.27072 using the CPU instance or about $0.775625 using the GPU instance. The CPU
usage is not only more expensive, but also takes more time to run. Accelerating this
workflow with a GPU instance available on AWS, using PennyLane's embedded simulator
backed by NVIDIA CuQuantum, allows you to run workflows with intermediate qubit counts
(between 20 and 30) for less total cost and in less time. This means you can experiment
with quantum computing even for problems that are too big to run quickly on your laptop
or a similarly-sized instance.

## Quantum machine learning and data parallelism

If your workload type is quantum machine learning (QML) that trains on datasets, you
can further accelerate your workload using data parallelism. In QML, the model contains
one or more quantum circuits. The model may or may not also contain classical neural
nets. When training the model with the dataset, the parameters in the model are updated
to minimize the loss function. A loss function is usually defined for a single data
point, and the total loss for the average loss over the whole dataset. In QML, the
losses are usually computed in serial before averaging to total loss for gradient
computations. This procedure is time consuming, especially when there are hundreds of
data points.

Because the loss from one data point does not depend on other data points, the losses
can be evaluated in parallel! Losses and gradients associated with different data points
can be evaluated at the same time. This is known as data parallelism. With SageMaker's
distributed data parallel library, Amazon Braket Hybrid Jobs make it easier for you to
use data parallelism to accelerate your training.

Consider the following QML workload for data parallelism which uses the [Sonar dataset](https://archive.ics.uci.edu/dataset/151/connectionist+bench+sonar+mines+vs+rocks "https://archive.ics.uci.edu/dataset/151/connectionist+bench+sonar+mines+vs+rocks") dataset from the well-known UCI repository as an example for
binary classification. The Sonar dataset have 208 data points each with 60 features that
are collected from sonar signals bouncing off materials. Each data points is either
labeled as "M" for mines or "R" for rocks. Our QML model consists of an input layer, a
quantum circuit as a hidden layer, and an output layer. The input and output layers are
classical neural nets implemented in PyTorch. The quantum circuit is integrated with the
PyTorch neural nets using PennyLane's qml.qnn module. See our [example notebooks](https://github.com/aws/amazon-braket-examples "https://github.com/aws/amazon-braket-examples") for
more detail about the workload. Like the QAOA example above, you can harness the power
of GPU by using embedded GPU-based simulators like PennyLane's
`lightning.gpu` to improve the performance over embedded CPU-based
simulators.

To create a hybrid job, you can call `AwsQuantumJob.create` and specify the
algorithm script, device, and other configurations through its keyword arguments.

```
instance_config = InstanceConfig(instanceType='ml.p3.2xlarge')

hyperparameters={"nwires": "10",
                 "ndata": "32",
                 ...
}

job = AwsQuantumJob.create(
    device="local:pennylane/lightning.gpu",
    source_module="qml_source",
    entry_point="qml_source.train_single",
    hyperparameters=hyperparameters,
    instance_config=instance_config,
    ...
)
```

In order to use data parallelism, you need to modify few lines of code in the
algorithm script for the SageMaker distributed library to correctly parallelize the
training. First, you import the `smdistributed` package which does most of
the heavy-lifting for distributing your workloads across multiple GPUs and multiple
instances. This package is preconfigured in the Braket PyTorch and TensorFlow
containers. The `dist` module tells our algorithm script what the total
number of GPUs for the training (`world_size`) is as well as the
`rank` and `local_rank` of a GPU core. `rank` is the
absolute index of a GPU across all instances, while `local_rank` is the index
of a GPU within an instance. For example, if there are four instances each with eight
GPUs allocated for the training, the `rank` ranges from 0 to 31 and the
`local_rank` ranges from 0 to 7.

```
import smdistributed.dataparallel.torch.distributed as dist

dp_info = {
    "world_size": dist.get_world_size(),
    "rank": dist.get_rank(),
    "local_rank": dist.get_local_rank(),
}
batch_size //= dp_info["world_size"] // 8
batch_size = max(batch_size, 1)
```

Next, you define a `DistributedSampler` according to the
`world_size` and `rank` and then pass it into the data loader.
This sampler avoids GPUs accessing the same slice of a dataset.

```
train_sampler = torch.utils.data.distributed.DistributedSampler(
    train_dataset,
    num_replicas=dp_info["world_size"],
    rank=dp_info["rank"]
)
train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=False,
    num_workers=0,
    pin_memory=True,
    sampler=train_sampler,
)
```

Next, you use the `DistributedDataParallel` class to enable data
parallelism.

```
from smdistributed.dataparallel.torch.parallel.distributed import DistributedDataParallel as DDP

model = DressedQNN(qc_dev).to(device)
model = DDP(model)
torch.cuda.set_device(dp_info["local_rank"])
model.cuda(dp_info["local_rank"])
```

The above are the changes you need to use data parallelism. In QML, you often want to
save results and print training progress. If each GPU runs the saving and printing
command, the log will be flooded with the repeated information and the results will
overwrite each other. To avoid this, you can only save and print from the GPU that has
`rank` 0.

```
if dp_info["rank"]==0:
    print('elapsed time: ', elapsed)
    torch.save(model.state_dict(), f"{output_dir}/test_local.pt")
    save_job_result({"last loss": loss_before})
```

Amazon Braket Hybrid Jobs supports `ml.p3.16xlarge` instance types for the
SageMaker distributed data parallel library. You configure the instance type through the
`InstanceConfig` argument in Hybrid Jobs. For the SageMaker distributed
data parallel library to know that data parallelism is enabled, you need to add two
additional hyperparameters, `"sagemaker_distributed_dataparallel_enabled"`
setting to `"true"` and `"sagemaker_instance_type"` setting to the
instance type you are using. These two hyperparameters are used by
`smdistributed` package. Your algorithm script does not need to explicitly
use them. In Amazon Braket SDK, it provides a convenient keyword argument
`distribution`. With `distribution="data_parallel"` in hybrid job
creation, the Amazon Braket SDK automatically inserts the two hyperparameters for you. If
you use the Amazon Braket API, you need to include these two hyperparameters.

With the instance and data parallelism configured, you can now submit your hybrid job. There
are 8 GPUs in a `ml.p3.16xlarge` instance. When you set
`instanceCount=1` , the workload is distributed across the 8 GPUs in the
instance. When you set `instanceCount` greater than one, the workload is
distributed across GPUs available in all instances. When using multiple instances, each
instance incurs a charge based on how much time you use it. For example, when you use
four instances, the billable time is four times the run time per instance because there
are four instances running your workloads at the same time.

```
instance_config = InstanceConfig(instanceType='ml.p3.16xlarge',
                                 instanceCount=1,
)

hyperparameters={"nwires": "10",
                 "ndata": "32",
                 ...,
}

job = AwsQuantumJob.create(
    device="local:pennylane/lightning.gpu",
    source_module="qml_source",
    entry_point="qml_source.train_dp",
    hyperparameters=hyperparameters,
    instance_config=instance_config,
    distribution="data_parallel",
    ...
)
```

###### Note

In the above hybrid job creation, `train_dp.py` is the modified algorithm
script for using data parallelism. Keep in mind that data parallelism only works
correctly when you modify your algorithm script according to the above section. If
the data parallelism option is enabled without a correctly modified algorithm script,
the hybrid job may throw errors, or each GPU may repeatedly process the same data slice,
which is inefficient.

Compare the run time and cost in an example where when train a model with a
26-qubit quantum circuit for the binary classification problem mentioned above. The
`ml.p3.16xlarge` instance used in this example costs $0.4692 per minute.
Without data parallelism, it takes the simulator about 45 minutes to train the model for
1 epoch (that is, over 208 data points) and it costs about $20. With data parallelism
across 1 instance and 4 instances, it only takes 6 minutes and 1.5 minutes respectively,
which translates to roughly $2.8 for both. By using data parallelism across 4 instances,
you not only improve the run time by 30x, but also reduce costs by an order of
magnitude!
