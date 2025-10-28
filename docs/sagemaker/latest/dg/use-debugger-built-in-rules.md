# How to configure Debugger built-in rules

In the following topics, you'll learn how to use the SageMaker Debugger built-in
rules. Amazon SageMaker Debugger's built-in rules analyze tensors emitted during the training of a model. SageMaker AI
Debugger offers the `Rule` API operation that monitors training job progress and
errors for the success of training your model. For example, the rules can detect whether
gradients are getting too large or too small, whether a model is overfitting or
overtraining, and whether a training job does not decrease loss function and improve. To see
a full list of available built-in rules, see [List of Debugger built-in rules](debugger-built-in-rules.md "debugger-built-in-rules.md").

###### Topics

- [Use Debugger built-in rules with
  the default parameter settings](debugger-built-in-rules-configuration.md "debugger-built-in-rules-configuration.md")
- [Use Debugger built-in
  rules with custom parameter values](debugger-built-in-rules-configuration-param-change.md "debugger-built-in-rules-configuration-param-change.md")
- [Example notebooks and code samples to
  configure Debugger rules](debugger-built-in-rules-example.md "debugger-built-in-rules-example.md")
  For an advanced configuration of the Debugger built-in rules using the `CreateTrainingJob` API,
  see [Configure Debugger using SageMaker API](debugger-createtrainingjob-api.md "debugger-createtrainingjob-api.md").
