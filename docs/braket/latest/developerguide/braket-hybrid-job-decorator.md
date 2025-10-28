# Run your local code as a hybrid job

Amazon Braket Hybrid Jobs provides a fully managed orchestration of hybrid quantum-classical
algorithms, combining Amazon EC2 compute resources with Amazon Braket Quantum Processing Unit (QPU) access. Quantum tasks
created in a hybrid job have priority queueing over individual quantum tasks so that your
algorithms won't be interrupted by fluctuations in the quantum task queue. Each QPU maintains
a separate hybrid jobs queue, ensuring that only one hybrid job can run at any given time.

###### In this section:

- [Create a hybrid job from local Python code](#create-hybrid-job-from-local-python-code "#create-hybrid-job-from-local-python-code")
- [Install additional Python packages and source code](#install-python-packages-and-code "#install-python-packages-and-code")
- [Save and load data into a hybrid job instance](#save-load-data-into-instance "#save-load-data-into-instance")
- [Best practices for hybrid job decorators](#best-practices "#best-practices")

## Create a hybrid job from local Python code

You can run your local Python code as an Amazon Braket Hybrid Job. You can do this by annotating
your code with an `@hybrid_job` decorator, as shown in the following code example.
For custom environments, you can opt to [use a custom container](braket-jobs-byoc.md "braket-jobs-byoc.md")
from Amazon Elastic Container Registry (ECR).

###### Note

Only Python 3.10 is supported by default.

You can use the `@hybrid_job` decorator to annotate a function. Braket transforms
the code inside the decorator into a Braket hybrid job [algorithm script](braket-jobs-first.md "braket-jobs-first.md").
The hybrid job then invokes the function inside the decorator on an Amazon EC2 instance. You can monitor
the progress of the job with `job.state()` or with the Braket console. The following
code example shows how to run a sequence of five states on the State Vector Simulator (SV1) device.

```
from braket.aws import AwsDevice
from braket.circuits import Circuit, FreeParameter, Observable
from braket.devices import Devices
from braket.jobs.hybrid_job import hybrid_job
from braket.jobs.metrics import log_metric

device_arn = Devices.Amazon.SV1


@hybrid_job(device=device_arn)  # Choose priority device
def run_hybrid_job(num_tasks=1):
    device = AwsDevice(device_arn)  # Declare AwsDevice within the hybrid job

    # Create a parametric circuit
    circ = Circuit()
    circ.rx(0, FreeParameter("theta"))
    circ.cnot(0, 1)
    circ.expectation(observable=Observable.X(), target=0)

    theta = 0.0  # Initial parameter

    for i in range(num_tasks):
        task = device.run(circ, shots=100, inputs={"theta": theta})  # Input parameters
        exp_val = task.result().values[0]

        theta += exp_val  # Modify the parameter (possibly gradient descent)

        log_metric(metric_name="exp_val", value=exp_val, iteration_number=i)

    return {"final_theta": theta, "final_exp_val": exp_val}
```

You create the hybrid job by invoking the function as you would normal Python functions.
However, the decorator function returns the hybrid job handle rather than the result of the function.
To retrieve the results after it has completed, use `job.result()`.

```
job = run_hybrid_job(num_tasks=1)
result = job.result()
```

The device argument in the `@hybrid_job` decorator specifies the device that the
hybrid job has priority access to - in this case, the SV1 simulator. To get QPU priority,
you must ensure that the device ARN used within the function matches that specified in the decorator.
For convenience, you can use the helper function `get_job_device_arn()` to capture the device
ARN declared in `@hybrid_job`.

###### Note

Each hybrid job has at least a one minute startup time since it creates a containerized environment on Amazon EC2.
So for very short workloads, such as a single circuit or a batch of circuits, it may suffice for you to use quantum tasks.

**Hyperparameters**

The `run_hybrid_job()` function takes the argument `num_tasks` to control the number of
quantum tasks created. The hybrid job automatically captures this as a [hyperparameter](braket-jobs-hyperparameters.md "braket-jobs-hyperparameters.md").

###### Note

Hyperparameters are displayed in the Braket console as strings, that are limited to 2500 characters.

**Metrics and logging**

Within the `run_hybrid_job()` function, metrics from iterative algorithms are recorded with
`log_metrics`. Metrics are automatically plotted in the Braket console page under the hybrid job tab.
You can use metrics to track the quantum task costs in near-real time during the hybrid job run with the
[Braket cost tracker](braket-pricing.md "braket-pricing.md"). The example above uses the metric name “probability”
that records the first probability from the [result type](braket-result-types.md "braket-result-types.md").

**Retrieving results**

After the hybrid job has completed, you use `job.result()` to retrieve the hybrid jobs results.
Any objects in the return statement are automatically captured by Braket. Note that the objects returned by
the function must be a tuple with each element being serializable. For example, the following code shows a
working, and a failing example.

```
import numpy as np


# Working example
@hybrid_job(device=Devices.Amazon.SV1)
def passing():
    np_array = np.random.rand(5)
    return np_array  # Serializable

# # Failing example
# @hybrid_job(device=Devices.Amazon.SV1)
# def failing():
#     return MyObject() # Not serializable
```

**Job name**

By default, the name for this hybrid job is inferred from the function name.
You may also specify a custom name up to 50 characters long. For
example, in the following code the job name is "my-job-name".

```
@hybrid_job(device=Devices.Amazon.SV1, job_name="my-job-name")
def function():
    pass
```

**Local mode**

[Local jobs](braket-jobs-local-mode.md "braket-jobs-local-mode.md") are be created by adding the argument `local=True`
to the decorator. This runs the hybrid job in a containerized environment on your local compute environment, such as your
laptop. Local jobs **do not** have priority queueing for quantum tasks. For advanced cases
such as multi-node or MPI, local jobs may have access to the required Braket environment variables. The following code creates
a local hybrid job with the device as the SV1 simulator.

```
@hybrid_job(device=Devices.Amazon.SV1, local=True)
def run_hybrid_job(num_tasks=1):
    return ...
```

All other hybrid job options are supported. For a list of options see the
[braket.jobs.quantum_job_creation module](https://amazon-braket-sdk-python.readthedocs.io/en/stable/_apidoc/braket.jobs.quantum_job_creation.html "https://amazon-braket-sdk-python.readthedocs.io/en/stable/_apidoc/braket.jobs.quantum_job_creation.html").

## Install additional Python packages and source code

You can customize your runtime environment to use your preferred Python packages. You can use
either a `requirements.txt` file, a list of package names, or [bring your own container (BYOC)](braket-jobs-byoc.md "braket-jobs-byoc.md").
For example, the `requirements.txt` file may include other packages to install.

```
qiskit
pennylane >= 0.31
mitiq == 0.29
```

To customize a runtime environment using a `requirements.txt` file, refer to the following code example.

```
@hybrid_job(device=Devices.Amazon.SV1, dependencies="requirements.txt")
def run_hybrid_job(num_tasks=1):
    return ...
```

Alternatively, you may supply the package names as a Python list as follows.

```
@hybrid_job(device=Devices.Amazon.SV1, dependencies=["qiskit", "pennylane>=0.31", "mitiq==0.29"])
def run_hybrid_job(num_tasks=1):
    return ...
```

Additional source code can be specified either as a list of modules, or a single module as in the following code example.

```
@hybrid_job(device=Devices.Amazon.SV1, include_modules=["my_module1", "my_module2"])
def run_hybrid_job(num_tasks=1):
    return ...
```

## Save and load data into a hybrid job instance

**Specifying input training data**

When you create a hybrid job, you may provide an input training datasets by specifying an Amazon Simple Storage Service
(Amazon S3) bucket. You may also specify a local path, then Braket automatically uploads the
data to Amazon S3 at `s3://<default_bucket_name>/jobs/<job_name>/<timestamp>/data/<channel_name>` .
If you specify a local path, the channel name defaults to “input”. The following code shows a numpy file from the local path `data/file.npy`.

```
import numpy as np


@hybrid_job(device=Devices.Amazon.SV1, input_data="data/file.npy")
def run_hybrid_job(num_tasks=1):
    data = np.load("data/file.npy")
    return ...
```

For S3, you must use the `get_input_data_dir()` helper funciton.

```
import numpy as np
from braket.jobs import get_input_data_dir

s3_path = "s3://amazon-braket-us-east-1-123456789012/job-data/file.npy"


@hybrid_job(device=None, input_data=s3_path)
def job_s3_input():
    np.load(get_input_data_dir() + "/file.npy")


@hybrid_job(device=None, input_data={"channel": s3_path})
def job_s3_input_channel():
    np.load(get_input_data_dir("channel") + "/file.npy")
```

You can specify multiple input data sources by providing a dictionary of channel values and S3 URIs or local paths.

```
import numpy as np
from braket.jobs import get_input_data_dir

input_data = {
    "input": "data/file.npy",
    "input_2": "s3://amzn-s3-demo-bucket/data.json"
}


@hybrid_job(device=None, input_data=input_data)
def multiple_input_job():
    np.load(get_input_data_dir("input") + "/file.npy")
    np.load(get_input_data_dir("input_2") + "/data.json")
```

###### Note

When the input data is large (>1GB), there is a long wait time before the job is created.
This is due to the local input data when it is first uploaded to an S3 bucket, then the
S3 path is added to the job request. Finally, the job request is submitted to the Braket
service.

**Saving results to S3**

To save results not included in the return statement of the decorated function, you must append the
correct directory to all file writing operations. The following example, shows saving a numpy array and a
matplotlib figure.

```
import matplotlib.pyplot as plt
import numpy as np


@hybrid_job(device=Devices.Amazon.SV1)
def run_hybrid_job(num_tasks=1):
    result = np.random.rand(5)

    # Save a numpy array
    np.save("result.npy", result)

    # Save a matplotlib figure
    plt.plot(result)
    plt.savefig("fig.png")
    return ...
```

All results are compressed into a file named `model.tar.gz`. You can download the results with the
Python function `job.result()` , or by navigating to the results folder from the hybrid job
page in the Braket management console.

**Saving and resuming from checkpoints**

For long-running hybrid jobs, its recommended to periodically save the intermediate state of the algorithm.
You can use the built-in `save_job_checkpoint()` helper function, or save files to the
`AMZN_BRAKET_JOB_RESULTS_DIR` path. The later is available with the helper function `get_job_results_dir()`.

The following is a minimal working example for saving and loading checkpoints with a hybrid job decorator:

```
from braket.jobs import save_job_checkpoint, load_job_checkpoint, hybrid_job


@hybrid_job(device=None, wait_until_complete=True)
def function():
    save_job_checkpoint({"a": 1})


job = function()
job_name = job.name
job_arn = job.arn


@hybrid_job(device=None, wait_until_complete=True, copy_checkpoints_from_job=job_arn)
def continued_function():
    load_job_checkpoint(job_name)


continued_job = continued_function()
```

In the first hybrid job, `save_job_checkpoint()` is called with a dictionary containing the data we want to save.
By default, every value must be serializable as text. For checkpointing more complex Python objects, such as numpy arrays, you
can set `data_format = PersistedJobDataFormat.PICKLED_V4`. This code creates and overwrites a checkpoint file with
default name `<jobname>.json` in your hybrid job artifacts under a subfolder called "checkpoints".

To create a new hybrid job to continue from the checkpoint, we need to pass `copy_checkpoints_from_job=job_arn`
where `job_arn` is the hybrid job ARN of the previous job. Then we use `load_job_checkpoint(job_name)` to
load from the checkpoint.

## Best practices for hybrid job decorators

**Embrace asynchronicity**

Hybrid jobs created with the decorator annotation are asynchronous - they run once the
classical and quantum resources are available. You monitor the progress of the algorithm using the Braket
Management Console or Amazon CloudWatch. When you submit your algorithm to run, Braket runs your algorithm in
a scalable containerized environment and results are retrieved when the algorithm is complete.

**Run iterative variational algorithms**

Hybrid jobs gives you the tools to run iterative quantum-classical algorithms. For purely quantum problems, use
[quantum tasks](braket-submit-tasks.md "braket-submit-tasks.md") or a [batch of quantum tasks](braket-batching-tasks.md "braket-batching-tasks.md").
The priority access to certain QPUs is most beneficial for long-running variational algorithms requiring multiple
iterative calls to the QPUs with classical processing in between.

**Debug using local mode**

Before you run a hybrid job on a QPU, its recommended to first run on the simulator SV1 to confirm it runs as expected.
For small scale tests, you can run with local mode for rapid iteration and debugging.

**Improve reproducibility with [Bring your own container (BYOC)](braket-jobs-byoc.md "braket-jobs-byoc.md")**

Create a reproducible experiment by encapsulating your software and its dependencies within a containerized environment.
By packaging all your code, dependencies, and settings in a container, you prevent potential conflicts and versioning issues.

**Multi-instance distributed simulators**

To run a large number of circuits, consider using built-in MPI support to run local simulators on multiple
instances within a single hybrid job. For more information, see [embedded simulators](pennylane-embedded-simulators.md "pennylane-embedded-simulators.md").

**Use parametric circuits**

Parametric circuits that you submit from a hybrid job are automatically compiled on certain QPUs using
[parametric compilation](braket-jobs-parametric-compilation.md "braket-jobs-parametric-compilation.md") to improve the runtimes of your algorithms.

**Checkpoint periodically**

For long-running hybrid jobs, its recommended to periodically save the intermediate state of the algorithm.

**For further examples, use cases, and best-practices, see
[Amazon Braket examples GitHub](https://github.com/amazon-braket/amazon-braket-examples "https://github.com/amazon-braket/amazon-braket-examples").**
