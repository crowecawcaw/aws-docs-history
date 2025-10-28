# Debugging training jobs using Amazon SageMaker Debugger

To prepare your training script and run training jobs with SageMaker Debugger to debug model
training progress, you follow the typical two-step process: modify your training script
using the `sagemaker-debugger` Python SDK, and construct a SageMaker AI estimator using
the SageMaker Python SDK. Go through the following topics to learn how to use SageMaker Debugger's
debugging functionality.

###### Topics

- [Adapting your training script to register a
  hook](debugger-modify-script.md "debugger-modify-script.md")
- [Launch training jobs with Debugger
  using the SageMaker Python SDK](debugger-configuration-for-debugging.md "debugger-configuration-for-debugging.md")
- [SageMaker Debugger interactive report for XGBoost](debugger-report-xgboost.md "debugger-report-xgboost.md")
- [Action on Amazon SageMaker Debugger rules](debugger-action-on-rules.md "debugger-action-on-rules.md")
- [Visualize Amazon SageMaker Debugger output tensors in
  TensorBoard](debugger-enable-tensorboard-summaries.md "debugger-enable-tensorboard-summaries.md")
