# Configuring SageMaker Debugger to save

tensors

_Tensors_ are data collections of updated parameters from the
backward and forward pass of each training iteration. SageMaker Debugger collects the
output tensors to analyze the state of a training job. SageMaker Debugger's [`CollectionConfig`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.CollectionConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.CollectionConfig") and [`DebuggerHookConfig`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DebuggerHookConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DebuggerHookConfig") API operations provide methods for
grouping tensors into _collections_ and saving them to a target S3
bucket. The following topics show how to use the `CollectionConfig` and
`DebuggerHookConfig` API operations, followed by examples of how to use
Debugger hook to save, access, and visualize output tensors.

While constructing a SageMaker AI estimator, activate SageMaker Debugger by specifying the
`debugger_hook_config` parameter. The following topics include examples of
how to set up the `debugger_hook_config` using the
`CollectionConfig` and `DebuggerHookConfig` API operations to
pull tensors out of your training jobs and save them.

###### Note

After properly configured and activated, SageMaker Debugger saves the output tensors in a
default S3 bucket, unless otherwise specified. The format of the default S3 bucket
URI is
`s3://amzn-s3-demo-bucket-sagemaker-<region>-<12digit_account_id>/<training-job-name>/debug-output/`.

###### Topics

- [Configure tensor collections
  using the CollectionConfig API](debugger-configure-tensor-collections.md "debugger-configure-tensor-collections.md")
- [Configure the
  DebuggerHookConfig API to save tensors](debugger-configure-tensor-hook.md "debugger-configure-tensor-hook.md")
- [Example notebooks and code samples to configure
  Debugger hook](debugger-save-tensors.md "debugger-save-tensors.md")
