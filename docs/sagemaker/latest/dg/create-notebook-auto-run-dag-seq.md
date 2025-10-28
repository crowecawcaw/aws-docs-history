# Pass information to and from your

notebook step

The following sections describe ways to pass information to your notebook as environment
variables and parameters.

## Pass environment

variables

Pass environment variables as a dictionary to the `environment_variable`
argument of your `NotebookJobStep`, as shown in the following example:

```
environment_variables = {"RATE": 0.0001, "BATCH_SIZE": 1000}

notebook_job_step = NotebookJobStep(
    ...
    environment_variables=environment_variables,
    ...
)
```

You can use the environment variables in the notebook using `os.getenv()`,
as shown in the following example:

```
# inside your notebook
import os
print(f"ParentNotebook: env_key={os.getenv('env_key')}")
```

## Pass parameters

When you pass parameters to the first Notebook Job step in your
`NotebookJobStep` instance, you might optionally want to tag a cell in your
Jupyter notebook to indicate where to apply new parameters or parameter overrides. For
instructions about how to tag a cell in your Jupyter notebook, see [Parameterize your notebook](notebook-auto-run-troubleshoot-override.md "notebook-auto-run-troubleshoot-override.md").

You pass parameters through the Notebook Job step's `parameters` parameter,
as shown in the following snippet:

```
notebook_job_parameters = {
    "company": "Amazon",
}

notebook_job_step = NotebookJobStep(
    ...
    parameters=notebook_job_parameters,
    ...
)
```

Inside your input notebook, your parameters are applied after the cell tagged with
`parameters` or at the beginning of the notebook if you don’t have a tagged
cell.

```
# this cell is in your input notebook and is tagged with 'parameters'
# your parameters and parameter overrides are applied after this cell
company='default'
```

```
# in this cell, your parameters are applied
# prints "company is Amazon"
print(f'company is {company}')
```

## Retrieve information from a

previous step

The following discussion explains how you can extract data from a previous step to to
pass to your Notebook Job step.

**Use `properties` attribute**

You can use the following properties with the previous step's `properties`
attribute:

- `ComputingJobName`—The training job name
- `ComputingJobStatus`—The training job status
- `NotebookJobInputLocation`—The input Amazon S3 location
- `NotebookJobOutputLocationPrefix`—The path to your training job
  outputs, more specifically
  `{`NotebookJobOutputLocationPrefix`}/{`training-job-name`}/output/output.tar.gz`.
  containing outputs
- `InputNotebookName`—The input notebook file name
- `OutputNotebookName`—The output notebook file name (which may
  not exist in the training job output folder if the job fails)

The following code snippet shows how to extract parameters from the properties
attribute.

```
notebook_job_step2 = NotebookJobStep(
    ....
    parameters={
        "step1_JobName": notebook_job_step1.properties.ComputingJobName,
        "step1_JobStatus": notebook_job_step1.properties.ComputingJobStatus,
        "step1_NotebookJobInput": notebook_job_step1.properties.NotebookJobInputLocation,
        "step1_NotebookJobOutput": notebook_job_step1.properties.NotebookJobOutputLocationPrefix,
    }
```

**Use JsonGet**

If you want to pass parameters other than the ones previously mentioned and the JSON
outputs of your previous step reside in Amazon S3, use `JsonGet`.
`JsonGet` is a general mechanism that can directly extract data from JSON
files in Amazon S3.

To extract JSON files in Amazon S3 with `JsonGet`, complete the following
steps:

1. Upload your JSON file to Amazon S3. If your data is already uploaded to
   Amazon S3, skip this step. The following example demonstrates uploading a JSON
   file to Amazon S3.

```
import json
from sagemaker.s3 import S3Uploader

output = {
    "key1": "value1",
    "key2": [0,5,10]
}

json_output = json.dumps(output)

with open("notebook_job_params.json", "w") as file:
    file.write(json_output)

S3Uploader.upload(
    local_path="notebook_job_params.json",
    desired_s3_uri="s3://`path`/`to`/`bucket`"
)
```

2. Provide your S3 URI and the JSON path to the value you want to extract. In the
   following example, `JsonGet` returns an object representing index 2 of the
   value associated with key `key2` (`10`).

```
NotebookJobStep(
    ....
    parameters={
        # the key job_key1 returns an object representing the value 10
        "job_key1": JsonGet(
            s3_uri=Join(on="/", values=["s3:/", ..]),
            json_path="key2[2]" # value to reference in that json file
        ),
        "job_key2": "Amazon"
    }
)
```
