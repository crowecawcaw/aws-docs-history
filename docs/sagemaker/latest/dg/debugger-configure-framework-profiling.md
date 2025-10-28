# Estimator configuration for

framework profiling

###### Warning

In favor of [Amazon SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md"), SageMaker AI
Debugger deprecates the framework profiling feature starting from TensorFlow 2.11 and
PyTorch 2.0. You can still use the feature in the previous versions of the
frameworks and SDKs as follows.

- SageMaker Python SDK <= v2.130.0
- PyTorch >= v1.6.0, < v2.0
- TensorFlow >= v2.3.1, < v2.11
  See also [March 16, 2023](debugger-release-notes.md#debugger-release-notes-20230315 "debugger-release-notes.md#debugger-release-notes-20230315").

To enable Debugger framework profiling, configure the
`framework_profile_params` parameter when you construct an estimator.
Debugger framework profiling collects framework metrics, such as data from initialization
stage, data loader processes, Python operators of deep learning frameworks and training
scripts, detailed profiling within and between steps, with cProfile or Pyinstrument
options. Using the `FrameworkProfile` class, you can configure custom
framework profiling options.

###### Note

Before getting started with Debugger framework profiling, verify that the framework
used to build your model is supported by Debugger for framework profiling. For more
information, see [Supported frameworks and
algorithms](debugger-supported-frameworks.md "debugger-supported-frameworks.md").

Debugger saves the framework metrics in a default S3 bucket. The format of the
default S3 bucket URI is
`s3://sagemaker-<region>-<12digit_account_id>/<training-job-name>/profiler-output/`.

###### Topics

- [Default framework
  profiling](debugger-configure-framework-profiling-basic.md "debugger-configure-framework-profiling-basic.md")
- [Default system
  monitoring and customized framework profiling for target steps or a target time
  range](debugger-configure-framework-profiling-range.md "debugger-configure-framework-profiling-range.md")
- [Default system
  monitoring and customized framework profiling with different profiling
  options](debugger-configure-framework-profiling-options.md "debugger-configure-framework-profiling-options.md")
