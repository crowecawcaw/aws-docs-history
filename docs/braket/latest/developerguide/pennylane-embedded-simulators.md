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
using two instance types: `ml.m5.2xlarge` and `ml.g4dn.xlarge`. The
`ml.m5.2xlarge` instance type is comparable to a standard developer laptop.
The `ml.g4dn.xlarge` is an accelerated computing instance that has a single
NVIDIA T4 GPU with 16GB of memory.

To run the GPU, we first need to specify a compatible image and the correct instance
(which defaults to a `ml.m5.2xlarge` instance).

```
from braket.aws import AwsSession
from braket.jobs.image_uris import Framework, retrieve_image

image_uri = retrieve_image(Framework.PL_PYTORCH, AwsSession().region)
instance_config = InstanceConfig(instanceType="ml.g4dn.xlarge")
```

We then need to input these to the hybrid job decorator, along with updated
device parameters in both the system and hybrid job arguments.

```
@hybrid_job(
        device="local:pennylane/lightning.gpu",
        input_data=input_file_path,
        image_uri=image_uri,
        instance_config=instance_config)
def run_qaoa_hybrid_job_gpu(p=1, steps=10):
    params = np.random.rand(2, p)

    braket_task_tracker = Tracker()

    graph = nx.read_adjlist(input_file_path, nodetype=int)
    wires = list(graph.nodes)
    cost_h, _mixer_h = qaoa.maxcut(graph)

    device_string = os.environ["AMZN_BRAKET_DEVICE_ARN"]
    prefix, device_name = device_string.split("/")
    dev= qml.device(simulator_name, wires=len(wires))
    ...
```

###### Note

If you specify the `instance_config` as using a GPU-based instance, but choose the
`device` to be the embedded CPU-based simulator (`lightning.qubit`), the
GPU will not be used. Make sure to use the embedded GPU-based simulator if you wish to target the GPU!

The mean iteration time for the `m5.2xlarge` instance is about 73 seconds, while for
the `ml.g4dn.xlarge` instance it is about 0.6 seconds. For this 21-qubit workflow, the
GPU instance gives us a 100x speedup. If you look at the Amazon Braket Hybrid Jobs
[pricing page](https://aws.amazon.com/braket/pricing/ "https://aws.amazon.com/braket/pricing/"), you can see that the cost per
minute for an `m5.2xlarge` instance is $0.00768, while for the `ml.g4dn.xlarge` instance
it is $0.01227. In this instance it is faster and cheaper to run on the GPU instance.

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
instance_config = InstanceConfig(instanceType='ml.g4dn.xlarge')

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

Amazon Braket Hybrid Jobs supports `ml.g4dn.12xlarge` instance types for the
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
are 4 GPUs in a `ml.g4dn.12xlarge` instance. When you set
`instanceCount=1` , the workload is distributed across the 8 GPUs in the
instance. When you set `instanceCount` greater than one, the workload is
distributed across GPUs available in all instances. When using multiple instances, each
instance incurs a charge based on how much time you use it. For example, when you use
four instances, the billable time is four times the run time per instance because there
are four instances running your workloads at the same time.

```
instance_config = InstanceConfig(instanceType='ml.g4dn.12xlarge',
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

If used correctly, using multiple instances can lead to orders of magnitude reduction in
both time and cost. See the [example notebook for more details](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/5_Parallelize_training_for_QML/Parallelize_training_for_QML.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/5_Parallelize_training_for_QML/Parallelize_training_for_QML.ipynb").
