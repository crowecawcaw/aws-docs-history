# Actions on rules using Amazon CloudWatch and

AWS Lambda

Amazon CloudWatch collects Amazon SageMaker AI model training job logs and Amazon SageMaker Debugger rule processing job
logs. Configure Debugger with Amazon CloudWatch Events and AWS Lambda to take action based on Debugger rule
evaluation status.

## Example notebooks

You can run the following example notebooks, which are prepared for experimenting
with stopping a training job using actions on Debugger's built-in rules using Amazon CloudWatch
and AWS Lambda.

- [Amazon SageMaker Debugger - Reacting to CloudWatch Events from Rules](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_action_on_rule/tf-mnist-stop-training-job.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_action_on_rule/tf-mnist-stop-training-job.html")

This example notebook runs a training job that has a vanishing gradient
issue. The Debugger [VanishingGradient](debugger-built-in-rules.md#vanishing-gradient "debugger-built-in-rules.md#vanishing-gradient") built-in rule is used while
constructing the SageMaker AI TensorFlow estimator. When the Debugger rule detects the
issue, the training job is terminated.

- [Detect Stalled Training and Invoke Actions Using SageMaker Debugger Rule](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_action_on_rule/detect_stalled_training_job_and_actions.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_action_on_rule/detect_stalled_training_job_and_actions.html")

This example notebook runs a training script with a code line that forces
it to sleep for 10 minutes. The Debugger [StalledTrainingRule](debugger-built-in-rules.md#stalled-training "debugger-built-in-rules.md#stalled-training") built-in rule invokes issues and
stops the training job.

###### Topics

- [Access CloudWatch logs for Debugger rules and training
  jobs](debugger-cloudwatch-metric.md "debugger-cloudwatch-metric.md")
- [Set up Debugger for automated training job
  termination using CloudWatch and Lambda](debugger-stop-training.md "debugger-stop-training.md")
- [Disable the CloudWatch Events rule to stop using the
  automated training job termination](debugger-disable-cw.md "debugger-disable-cw.md")
