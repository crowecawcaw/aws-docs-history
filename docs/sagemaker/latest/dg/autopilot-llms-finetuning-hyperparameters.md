# Hyperparameters for optimizing

the learning process of your text generation models

You can optimize the learning process of your base model by adjusting any combination of
the following hyperparameters. These parameters are available for all models.

- **Epoch Count**: The `epochCount`
  hyperparameter determines how many times the model goes through the entire training
  dataset. It influences the training duration and can prevent overfitting when set
  appropriately. Large number of epochs may increase the overall runtime of fine-tuning
  jobs. We recommend setting a large `MaxAutoMLJobRuntimeInSeconds` within the
  `CompletionCriteria` of the `TextGenerationJobConfig` to avoid fine-tuning jobs from stopping
  prematurely.
- **Batch Size**: The `batchSize`
  hyperparameter defines the number of data samples used in each iteration of training. It
  can affect the convergence speed and memory usage. With large batch size, the risk of out
  of memory (OOM) errors increases, which may surface as an internal server error in Autopilot.
  To check for such error, check the `/aws/sagemaker/TrainingJobs` log group for
  the training jobs launched by your Autopilot job. You can access those logs in CloudWatch from in
  the AWS management console. Choose **Logs**, and then choose the
  `/aws/sagemaker/TrainingJobs`
  **log group**. To remedy OOM errors, reduce the batch size.

We recommend starting with a batch size of 1, then incrementally increase it until an
out of memory error occurs. As a reference, 10 epochs typically takes up to 72h to
complete.

- **Learning Rate**: The `learningRate`
  hyperparameter controls the step size at which a model's parameters are updated during
  training. It determines how quickly or slowly the model's parameters are updated during
  training. A high learning rate means that the parameters are updated by a large step size,
  which can lead to faster convergence but may also cause the optimization process to
  overshoot the optimal solution and become unstable. A low learning rate means that the
  parameters are updated by a small step size, which can lead to more stable convergence but
  at the cost of slower learning.
- **Learning Rate Warmup Steps**: The
  `learningRateWarmupSteps` hyperparameter specifies the number of training
  steps during which the learning rate gradually increases before reaching its target or
  maximum value. This helps the model converge more effectively and avoid issues like
  divergence or slow convergence that can occur with an initially high learning rate.
  To learn about how to adjust hyperparameters for your fine-tuning experiment in Autopilot and
  discover their possible values, see [How to set hyperparameters
  to optimize the learning process of a model](autopilot-create-experiment-finetune-llms.md#autopilot-llms-finetuning-set-hyperparameters "autopilot-create-experiment-finetune-llms.md#autopilot-llms-finetuning-set-hyperparameters").
