# Invoke another notebook in your notebook

job

You can set up a pipeline in which one notebook job calls another notebook.
The following sets up an example of a pipeline with a Notebook Job step in
which the notebook calls two other notebooks. The input notebook contains the following
lines:

```
%run 'subfolder/notebook_to_call_in_subfolder.ipynb'
%run 'notebook_to_call.ipynb'
```

Pass these notebooks into your `NotebookJobStep` instances with
`additional_dependencies`, as shown in the following snippet. Note that the
paths provided for the notebooks in `additional_dependencies` are provided from
the root location. For information about how SageMaker AI uploads your dependent files and folders
to Amazon S3 so you can correctly provide paths to your dependencies, see the
description for `additional_dependencies` in [NotebookJobStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep").

```
input_notebook = "inputs/input_notebook.ipynb"
simple_notebook_path = "inputs/notebook_to_call.ipynb"
folder_with_sub_notebook = "inputs/subfolder"

notebook_job_step = NotebookJobStep(
    image_uri=`image-uri`,
    kernel_name=`kernel-name`,
    role=`role-name`,
    input_notebook=input_notebook,
    additional_dependencies=[simple_notebook_path, folder_with_sub_notebook],
    tags=`tags`,
)
```
