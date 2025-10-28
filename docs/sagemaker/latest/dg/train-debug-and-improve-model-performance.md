# Debugging and improving model

performance

The essence of training machine learning models, deep learning neural networks,
transformer models is in achieving stable model convergence, and as such, state-of-the-art
models have millions, billions, or trillions of model parameters. The number of operations
to update the gigantic number of model parameters during each iteration can easily become
astronomical. To identify model convergence issues, it is important to be able to access the
model parameters, activations, and gradients computed during optimization processes.

Amazon SageMaker AI provides two debugging tools to help identify such convergence issues and gain
visibility into your models.

**Amazon SageMaker AI with TensorBoard**

To offer greater compatibility with the open-source community tools within the SageMaker AI
Training platform, SageMaker AI hosts TensorBoard as an application in [SageMaker AI domain](sm-domain.md "sm-domain.md"). You can bring your
training jobs to SageMaker AI and keep using the TensorBoard summary writer to collect the model
output tensors. Because TensorBoard is implemented into [SageMaker AI domain](sm-domain.md "sm-domain.md"), it also gives you more
options to manage user profiles under the SageMaker AI domain in your AWS account, and
provides fine control over the user profiles by granting access to specific actions and
resources. To learn more, see [TensorBoard in Amazon SageMaker AI](tensorboard-on-sagemaker.md "tensorboard-on-sagemaker.md").

**Amazon SageMaker Debugger**

Amazon SageMaker Debugger is a capability of SageMaker AI that provides tools to register hooks to callbacks to
extract model output tensors and save them in Amazon Simple Storage Service. It provides [built-in rules](debugger-built-in-rules.md "debugger-built-in-rules.md") for detecting model convergence issues, such as overfitting,
saturated activation functions, vanishing gradients, and more. You can also set up the
built-in rules with Amazon CloudWatch Events and AWS Lambda for taking automated actions against detected
issues, and set up Amazon Simple Notification Service to receive email or text notifications. To learn more, see
[Amazon SageMaker Debugger](train-debugger.md "train-debugger.md").

###### Topics

- [TensorBoard in Amazon SageMaker AI](tensorboard-on-sagemaker.md "tensorboard-on-sagemaker.md")
- [Amazon SageMaker Debugger](train-debugger.md "train-debugger.md")
- [Access a training container through AWS Systems Manager for
  remote debugging](train-remote-debugging.md "train-remote-debugging.md")
- [Release notes for debugging capabilities of Amazon SageMaker AI](debugger-release-notes.md "debugger-release-notes.md")
