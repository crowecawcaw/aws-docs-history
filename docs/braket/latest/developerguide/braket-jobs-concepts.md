# Key concepts for Hybrid Jobs

This section explains the key concepts of the `AwsQuantumJob.create` function
provided by the Amazon Braket Python SDK and mapping to the container file structure.

In addition to the file or files that makes up your complete algorithm script, your hybrid job
can have additional inputs and outputs. When your hybrid job starts, Amazon
Braket copies inputs provided as part of the hybrid job creation into the container that runs
the algorithm script. When the hybrid job completes, all outputs defined during the algorithm are
copied to the Amazon S3 location specified.

###### Note

_Algorithm metrics_ are reported in real time and do not follow this
output procedure.

Amazon Braket also provides several environment variables and helper
functions to simplify the interactions with container inputs and outputs. For more information, see the
[braket.jobs package](https://amazon-braket-sdk-python.readthedocs.io/en/latest/_apidoc/braket.jobs.html "https://amazon-braket-sdk-python.readthedocs.io/en/latest/_apidoc/braket.jobs.html")
in the _Amazon Braket SDK_.

###### In this section:

- [Inputs](#braket-jobs-inputs "#braket-jobs-inputs")
- [Outputs](#braket-jobs-outputs "#braket-jobs-outputs")
- [Environmental variables](#braket-jobs-environmental-variables "#braket-jobs-environmental-variables")
- [Helper functions](#braket-jobs-helper-functions "#braket-jobs-helper-functions")

## Inputs

**Input data**: Input data can be provided to the hybrid
algorithm by specifying the input data file, which is set up as a dictionary, with the
`input_data` argument. The user defines the `input_data`
argument within the `AwsQuantumJob.create` function in the SDK. This copies
the input data to to the container file system at the location given by the environment
variable `"AMZN_BRAKET_INPUT_DIR"`. For a couple examples of how input data
is used in a hybrid algorithm, see the [QAOA with Amazon Braket Hybrid Jobs and PennyLane](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/2_Using_PennyLane_with_Braket_Hybrid_Jobs/Using_PennyLane_with_Braket_Hybrid_Jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/2_Using_PennyLane_with_Braket_Hybrid_Jobs/Using_PennyLane_with_Braket_Hybrid_Jobs.ipynb") and [Quantum machine learning in Amazon Braket Hybrid Jobs](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb") Jupyter
notebooks.

###### Note

When the input data is large (>1GB), there will be a long wait time before the
hybrid job is submitted. This is due to the fact that the local input data will first be
uploaded to an S3 bucket, then the S3 path will be added to the hybrid job request, and,
finally, the hybrid job request is submitted to Braket service.

**Hyperparameters**: If you pass in
`hyperparameters`, they are available under the environment variable
`"AMZN_BRAKET_HP_FILE"`.

###### Note

For more information about how to create hyperparameters and input data and then
pass this information to the hybrid job script, see the [Use hyperparameters](braket-jobs-hyperparameters.md "braket-jobs-hyperparameters.md") section and this
github [page](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/qcbm/qcbm.py "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/qcbm/qcbm.py").

**Checkpoints**: To specify a `job-arn` whose
checkpoint you want to use in a new hybrid job, use the `copy_checkpoints_from_job`
command. This command copies over the checkpoint data to the
`checkpoint_configs3Uri` of the new hybrid job, making it available at the path
given by the environment variable `AMZN_BRAKET_CHECKPOINT_DIR` while the job
runs. The default is `None`, meaning checkpoint data from another hybrid job will
not be used in the new hybrid job.

## Outputs

**Quantum Tasks**: Quantum task results are stored in the S3 location
`s3://amazon-braket-<region>-<accountID>/jobs/<job-name>/tasks`.

**Job results**: Everything that your algorithm script
saves to the directory given by the environment variable
`"AMZN_BRAKET_JOB_RESULTS_DIR"` is copied to the S3 location specified in
`output_data_config`. If the value is not specified, it defaults to
`s3://amazon-braket-<region>-<accountID>/jobs/<job-name>/<timestamp>/data`.
We provide the SDK helper function **`save_job_result`**, which you can use to store results conveniently in the form of a dictionary
when called from your algorithm script.

**Checkpoints**: If you want to use checkpoints, you can
save them in the directory given by the environment variable
`"AMZN_BRAKET_CHECKPOINT_DIR"`. You can also use the SDK helper function
`save_job_checkpoint` instead.

**Algorithm metrics**: You can define algorithm metrics
as part of your algorithm script that are emitted to Amazon CloudWatch and displayed in real time
in the Amazon Braket console while your hybrid job is running. For an example
of how to use algorithm metrics, see [Use
Amazon Braket Hybrid Jobs to run a QAOA algorithm](braket-jobs-run-qaoa-algorithm.md "braket-jobs-run-qaoa-algorithm.md").

For more information on saving your job outputs, see
[Save your results](braket-jobs-first.md#braket-jobs-save-results "braket-jobs-first.md#braket-jobs-save-results")
in the Hybrid Jobs documentation.

## Environmental variables

Amazon Braket provides several environment variables to simplify the
interactions with container inputs and outputs. The folllowing code lists the
environmental variables that Braket uses.

- `AMZN_BRAKET_INPUT_DIR` – The input data directory opt/braket/input/data.
- `AMZN_BRAKET_JOB_RESULTS_DIR` – The output directory opt/braket/model
  to write job results to.
- `AMZN_BRAKET_JOB_NAME` – The name of the job.
- `AMZN_BRAKET_CHECKPOINT_DIR` – The checkpoint directory.
- `AMZN_BRAKET_HP_FILE` – The file containing the hyperparameters.
- `AMZN_BRAKET_DEVICE_ARN` – The device ARN (AWS Resource Name).
- `AMZN_BRAKET_OUT_S3_BUCKET` – The output Amazon S3 bucket, as specified in
  the `CreateJob` request's `OutputDataConfig`.
- `AMZN_BRAKET_SCRIPT_ENTRY_POINT` – The entry point as specified in the
  `CreateJob` request's `ScriptModeConfig`.
- `AMZN_BRAKET_SCRIPT_COMPRESSION_TYPE` – The compression type as specified
  in the `CreateJob` request's `ScriptModeConfig`.
- `AMZN_BRAKET_SCRIPT_S3_URI` – The Amazon S3 location of the user's script as
  specified in the `CreateJob` request's `ScriptModeConfig`.
- `AMZN_BRAKET_TASK_RESULTS_S3_URI` – The Amazon S3 location where the SDK would
  store the quantum task results by default for the job.
- `AMZN_BRAKET_JOB_RESULTS_S3_PATH` – The Amazon S3 location where the job results
  would be stored, as specified in `CreateJob` request's `OutputDataConfig`.
- `AMZN_BRAKET_JOB_TOKEN` – The string that should be passed to
  `CreateQuantumTask`'s `jobToken` parameter for quantum tasks created in the
  job container.

## Helper functions

Amazon Braket provides several helper functions to simplify the
interactions with container inputs and outputs. These helper functions would be called
from within the algorithm script that is used to run your Hybrid Job. The following
example demonstrates how to use them.

```
from braket.jobs import get_checkpoint_dir, get_hyperparameters, get_input_data_dir, get_job_device_arn, get_job_name, get_results_dir, save_job_result, save_job_checkpoint, load_job_checkpoint

get_checkpoint_dir() # Get the checkpoint directory
get_hyperparameters() # Get the hyperparameters as strings
get_input_data_dir() # Get the input data directory
get_job_device_arn() # Get the device specified by the hybrid job
get_job_name() # Get the name of the hybrid job.
get_results_dir() # Get the path to a results directory
save_job_result(result_data='data') # Save hybrid job results
save_job_checkpoint(checkpoint_data={'key': 'value'}) # Save a checkpoint
load_job_checkpoint() # Load a previously saved checkpoint
```
