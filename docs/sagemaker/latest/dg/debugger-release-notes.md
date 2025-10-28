# Release notes for debugging capabilities of Amazon SageMaker AI

See the following release notes to track the latest updates for debugging capabilities of Amazon SageMaker AI.

## December 21, 2023

**New features**

Released a remote debugging functionality, a new debugging capability of SageMaker AI that
gives you a shell-level access to training containers. With this release, you can debug
training jobs by logging into the job containers running on SageMaker AI ML instances. To learn
more, see [Access a training container through AWS Systems Manager for
remote debugging](train-remote-debugging.md "train-remote-debugging.md").

## September 7, 2023

**New features**

Added a new utility module
`sagemaker.interactive_apps.tensorboard.TensorBoardApp` that provides a
function called `get_app_url()`. The `get_app_url()` function
generates unsigned or presigned URLs to open the TensorBoard application in any
environment in SageMaker AI or Amazon EC2. This is to provide a unified experience for both Studio Classic
and non-Studio Classic users. For the Studio Classic environment, you can open TensorBoard by running
the `get_app_url()` function as it is, or you can also specify a job name to
start tracking as the TensorBoard application opens. For non-Studio Classic environments, you
can open TensorBoard by providing your domain information to the utility function.
With this functionality, regardless of where or how you run training code and launch
training jobs, you can directly access TensorBoard by running the
`get_app_url` function in your Jupyter notebook or terminal. This
functionality is available in the SageMaker Python SDK v2.184.0 and later. For more
information, see [Accessing the TensorBoard application on
SageMaker AI](debugger-htb-access-tb.md "debugger-htb-access-tb.md").

## April 4, 2023

**New features**

Released SageMaker AI with TensorBoard, a capability that hosts TensorBoard on SageMaker AI.
TensorBoard is available as an application through SageMaker AI domain, and the SageMaker AI
Training platform supports TensorBoard output data collection to S3 and loading them
automatically to the hosted TensorBoard on SageMaker AI. With this capability, you can run
training jobs set up with TensorBoard summary writers in SageMaker AI, save the TensorBoard
output files in Amazon S3, open the TensorBoard application directly from the SageMaker AI
console, and load the output files using SageMaker AI Data Manager plugin implemented to
the hosted TensorBoard interface. You don't need to install TensorBoard manually and
host locally on the SageMaker AI IDEs or local machine. To learn more, see [TensorBoard in Amazon SageMaker AI](tensorboard-on-sagemaker.md "tensorboard-on-sagemaker.md").

## March 16, 2023

###### Deprecation notes

SageMaker Debugger deprecates the framework profiling feature starting from
TensorFlow 2.11 and PyTorch 2.0. You can still use the feature in the previous
versions of the frameworks and SDKs as follows.

- SageMaker Python SDK <= v2.130.0
- PyTorch >= v1.6.0, < v2.0
- TensorFlow >= v2.3.1, < v2.11

With the deprecation, SageMaker Debugger also discontinues support for the following three
`ProfilerRules` for framework profiling.

- [MaxInitializationTime](debugger-built-in-rules.md#max-initialization-time "debugger-built-in-rules.md#max-initialization-time")
- [OverallFrameworkMetrics](debugger-built-in-rules.md#overall-framework-metrics "debugger-built-in-rules.md#overall-framework-metrics")
- [StepOutlier](debugger-built-in-rules.md#step-outlier "debugger-built-in-rules.md#step-outlier")

## February 21, 2023

###### Other changes

- The XGBoost report tab has been removed from the SageMaker Debugger's profiler
  dashboard. You can still access the XGBoost report by downloading it as a Jupyter
  notebook or a HTML file. For more information, see [SageMaker Debugger
  XGBoost Training Report](debugger-report-xgboost.md "debugger-report-xgboost.md").
- Starting from this release, the built-in profiler rules are not activated by
  default. To use the SageMaker Debugger profiler rules to detect certain computational
  problems, you need to add the rules when you configure a SageMaker training job
  launcher.

## December 1, 2020

Amazon SageMaker Debugger launched deep profiling features at re:Invent 2020.

## December 3, 2019

Amazon SageMaker Debugger initially launched at re:Invent 2019.
