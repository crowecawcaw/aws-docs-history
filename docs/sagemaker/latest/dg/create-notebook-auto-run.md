# Where you can create a notebook job

If you want to create a notebook job, you have multiple options. The following provides
the SageMaker AI options for you to create a notebook job.

You can create a job in your JupyterLab notebook in the Studio UI, or you can
programmatically create a job with the SageMaker Python SDK:

- If you create your notebook job in the Studio UI, you supply details about the image
  and kernel, security configurations, and any custom variables or scripts, and your job is
  scheduled. For details about how to schedule your job using SageMaker Notebook Jobs, see [Create a notebook job in Studio](create-notebook-auto-run-studio.md "create-notebook-auto-run-studio.md").
- To create a notebook job with the SageMaker Python SDK, you create a pipeline with a Notebook
  Job step and initiate an on-demand run or optionally use the pipeline scheduling feature to
  schedule future runs. The SageMaker SDK gives you the flexibility to customize your
  pipeline—you can expand your pipeline to a workflow with multiple notebook job steps.
  Since you create both a SageMaker Notebook Job step and a pipeline, you can track your pipeline
  execution status in the SageMaker Notebook Jobs job dashboard and also view your pipeline graph in
  Studio. For details about how to schedule your job with the SageMaker Python SDK and links to
  example notebooks, see [Create notebook job with SageMaker AI Python
  SDK example](create-notebook-auto-run-sdk.md "create-notebook-auto-run-sdk.md").
