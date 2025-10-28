# Using hyperparameters

You can define hyperparameters needed by your algorithm, such as the learning rate or
step size, when you create a hybrid job. Hyperparameter values are typically used to control
various aspects of the algorithm, and can often be tuned to optimize the algorithm's
performance. To use hyperparameters in a Braket hybrid job, you need to specify their
names and values explicitly as a dictionary. Specify the hyperparameter values to test when searching for
the optimal set of values. The first step to using hyperparameters is to set up and define
the hyperparameters as a dictionary, which can be seen in the following code.

```
from braket.devices import Devices

device_arn = Devices.Amazon.SV1

hyperparameters = {"shots": 1_000}
```

Then pass the hyperparameters defined in the code snippet given above to be used in the algorithm
of your choice. To run the following code example, create a directory named “src” in the same path as
your hyperparameter file. Inside of the "src" directory, add
[0_Getting_started_papermill.ipynb](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/0_Getting_started_papermill.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/0_Getting_started_papermill.ipynb"),
[notebook_runner.py](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/notebook_runner.py "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/notebook_runner.py"),
and [requirements.txt](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/requirements.txt "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/requirements.txt")
code files.

```
import time
from braket.aws import AwsQuantumJob

job = AwsQuantumJob.create(
    device=device_arn,
    source_module="src",
    entry_point="src.notebook_runner:run_notebook",
    input_data="src/0_Getting_started_papermill.ipynb",
    hyperparameters=hyperparameters,
    job_name=f"papermill-job-demo-{int(time.time())}",
)

# Print job to record the ARN
print(job)
```

To access your hyperparameters from _within_ your hybrid job script, see the
`load_jobs_hyperparams()` function in the
[notebook_runner.py](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/notebook_runner.py "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/7_Running_notebooks_as_hybrid_jobs/src/notebook_runner.py")
python file. To access your hyperparameters _outside_ of your hybrid job script, run the following code.

```
from braket.aws import AwsQuantumJob

# Get the job using the ARN
job_arn = "arn:aws:braket:us-east-1:111122223333:job/5eabb790-d3ff-47cc-98ed-b4025e9e296f"  # Replace with your job ARN
job = AwsQuantumJob(arn=job_arn)

# Access the hyperparameters
job_metadata = job.metadata()
hyperparameters = job_metadata.get("hyperParameters", {})
print(hyperparameters)
```

For more information on learning how to use hyperparamters, see the [QAOA with Amazon Braket Hybrid Jobs and PennyLane](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/2_Using_PennyLane_with_Braket_Hybrid_Jobs/Using_PennyLane_with_Braket_Hybrid_Jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/2_Using_PennyLane_with_Braket_Hybrid_Jobs/Using_PennyLane_with_Braket_Hybrid_Jobs.ipynb") and [Quantum machine learning in Amazon Braket Hybrid Jobs](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb") tutorials.
