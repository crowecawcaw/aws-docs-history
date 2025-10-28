# Using CUDA-Q with Amazon Braket

NVIDIA's CUDA-Q is a software library designed for programming hybrid quantum algorithms that combine
CPUs, GPUs, and Quantum processing units (QPUs). It provides a unified programming model, allowing developers to express
both classical and quantum instructions within a single program, streamlining workflows. CUDA-Q accelerates quantum
program simulation and runtime with its built-in CPU and GPU simulators.

Using CUDA-Q on Amazon Braket Hybrid Jobs offers a flexible, on-demand computing environment. Computational
instances run only for the duration of your workload, ensuring you pay only for what you use. Amazon Braket Hybrid Jobs also
provides a scalable experience. Users can start with smaller instances for prototyping and testing, then scale up to larger
instances capable of handling greater workloads for full experiments.

Amazon Braket Hybrid Jobs support GPUs that are essential for maximizing CUDA-Q's potential. GPUs significantly
speed up quantum program simulations compared to CPU-based simulators, especially when working with high qubit count circuits.
Parallelization becomes straightforward when using CUDA-Q on Amazon Braket Hybrid Jobs. Hybrid Jobs simplifies
the distribution of circuit sampling and observable evaluations across multiple computational nodes. This seamless parallelization
of CUDA-Q workloads allows users to focus more on developing their workloads rather than setting up infrastructure
for large-scale experiments.

To get started, see the [CUDA-Q starter example](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/nvidia_cuda_q/0_hello_cudaq_jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/nvidia_cuda_q/0_hello_cudaq_jobs.ipynb")
on the Amazon Braket examples Github to use a CUDA-Q hybrid jobs container provided by Braket.

The following code snippet is a `hello-world` example for running a CUDA-Q program with Amazon Braket Hybrid Jobs.

```
image_uri = retrieve_image(Framework.CUDAQ, AwsSession().region)

@hybrid_job(device='local:nvidia/qpp-cpu', image_uri=image_uri)
def hello_quantum():
    import cudaq

    # define the backend
    device=get_job_device_arn()
    cudaq.set_target(device.split('/')[-1])

    # define the Bell circuit
    kernel = cudaq.make_kernel()
    qubits = kernel.qalloc(2)
    kernel.h(qubits[0])
    kernel.cx(qubits[0], qubits[1])

    # sample the Bell circuit
    result = cudaq.sample(kernel, shots_count=1000)
    measurement_probabilities = dict(result.items())

    return measurement_probabilities
```

The above example simulates a Bell circuit on a CPU simulator. This example runs locally on your laptop or Braket Jupyter notebook.
Because of the `local=True` setting, when you run this script, a container will start in your local environment to run the CUDA-Q program
for testing and debugging. After you finish testing, you can remove the `local=True` flag and run your job AWS. To learn more, see
[Getting started with Amazon Braket Hybrid Jobs](braket-build-jobs.md "braket-build-jobs.md").

If your workloads have a high qubit count, a large number of circuits or a large number of iterations, you can use more
powerful CPU computing resources by specifying the `instance_config` setting. The following code snippet shows how to configure
the `instance_config` setting in the `hybrid_job` decorator. For more information about supported instance types, see
[Configure the hybrid job instance
to run your script](braket-jobs-configure-job-instance-for-script.md "braket-jobs-configure-job-instance-for-script.md"). For a list of instance types, see [Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

```
@hybrid_job(
    device="local:nvidia/qpp-cpu",
    image_uri=image_uri,
    instance_config=InstanceConfig(instanceType="ml.c5.2xlarge"),
)
def my_job_script():
    ...
```

For more demanding workloads, you can run your workloads on a CUDA-Q GPU simulator. To enable a GPU simulator, use the backend
name `nvidia`. The `nvidia` backend operates as a CUDA-Q GPU simulator. Next, select an Amazon EC2 instance type that supports
an NVIDIA GPU. The following code snippet shows the GPU-configured `hybrid_job` decorator.

```
@hybrid_job(
    device="local:nvidia/nvidia",
    image_uri=image_uri,
    instance_config=InstanceConfig(instanceType="ml.p3.2xlarge"),
)
def my_job_script():
    ...
```

Amazon Braket Hybrid Jobs supports parallel GPU simulations with CUDA-Q. You can parallelize the evaluation of multiple observables
or multiple circuits to boost the performance of your workload. To parallelize multiple observables, make the following changes to your algorithm script.

Set the `mgpu` option of the `nvidia` backend. This is required to parallelize the observables.
The parallelization uses MPI for communication between GPUs, so MPI needs to be initialized before the execution and finalized after it.

Next, specify the execution mode by setting `execution=cudaq.parallel.mpi`. The following code snippet shows these changes.

```
cudaq.set_target("nvidia", option="mqpu")
cudaq.mpi.initialize()
result = cudaq.observe(
    kernel, hamiltonian, shots_count=n_shots, execution=cudaq.parallel.mpi
)
cudaq.mpi.finalize()
```

In the `hybrid_job` decorator specify an instance type that hosts multiple GPUs as shown in the following code snippet.

```
@hybrid_job(
    device="local:nvidia/nvidia-mqpu",
    instance_config=InstanceConfig(instanceType="ml.p3.8xlarge", instanceCount=1),
    image_uri=image_uri,
)
def parallel_observables_gpu_job(sagemaker_mpi_enabled=True):
    ...
```

The [parallel simulations notebook](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/nvidia_cuda_q/2_parallel_simulations.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/nvidia_cuda_q/2_parallel_simulations.ipynb")
in the Amazon Braket examples Github provide end-to-end examples that demonstrate how to run quantum program simulations on GPU backends and perform parallel simulations
of observables and circuit batches.

## Running your workloads on quantum computers

After completing simulator testing, you can transition to running experiments on QPUs. Just switch
the target to an Amazon Braket QPU, such as the IQM, IonQ, or Rigetti devices. The following
code snippet illustrates how to set the target to the IQM Garnet device. For a list of available QPUs, see the
[Amazon Braket Console](https://us-west-1.console.aws.amazon.com/braket/home?region=us-west-1#/dashboard "https://us-west-1.console.aws.amazon.com/braket/home?region=us-west-1#/dashboard").

```
device_arn = "arn:aws:braket:eu-north-1::device/qpu/iqm/Garnet"
cudaq.set_target("braket", machine=device_arn)
```

For more information about Amazon Braket Hybrid Jobs, see [Working with Amazon Braket Hybrid Jobs](braket-test-jobs.md "braket-test-jobs.md")
in the developer guide. To learn more about CUDA-Q, see the [CUDA-Q documentation](https://nvidia.github.io/cuda-quantum/latest/index.html "https://nvidia.github.io/cuda-quantum/latest/index.html").
