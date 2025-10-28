# Sustainability pillar – Best practices

The sustainability pillar focuses on environmental impacts,
especially energy consumption and efficiency, since they are
important levers for architects to inform direct action to reduce
resource usage. This section includes best practices to consider
while developing models that includes training, tuning, and model
performance evaluation.

###### Best practices

- [MLSUS-07: Define sustainable performance criteria](mlsus-07.md "mlsus-07.md")
- [MLSUS-08: Select energy-efficient algorithms](mlsus-08.md "mlsus-08.md")
- [MLSUS-09: Archive or delete unnecessary training artifacts](mlsus-09.md "mlsus-09.md")
- [MLSUS-10: Use efficient model tuning methods](mlsus-10.md "mlsus-10.md")

**Related best practices**

- **Tradeoff analysis on custom versus
  pre-trained models** (MLCOST-04) - Consider whether
  the workload needs to be developed as a custom model. Many
  workloads can use the managed
  [AWS AI services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/"). Using these services means that you
  won’t need the associated resources to collect, store, and
  process data and to prepare, train, tune, and deploy an ML
  model. If adopting a fully managed AI service is not
  appropriate, evaluate if you can use pre-existing datasets,
  algorithms, or models.
  [AWS Marketplace](https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1 "https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1") offers over 1,400 ML-related assets that
  customers can subscribe to. You can also
  [fine-tune
  an existing model](https://aws.amazon.com/fr/blogs/machine-learning/fine-tune-and-host-hugging-face-bert-models-on-amazon-sagemaker/ "https://aws.amazon.com/fr/blogs/machine-learning/fine-tune-and-host-hugging-face-bert-models-on-amazon-sagemaker/") starting from a pre-trained model,
  like those available on
  [Hugging
  Face](https://huggingface.co/ "https://huggingface.co/") or
  [SageMaker AI
  JumpStart](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md"). Using pre-trained models from third
  parties can reduce the resources you need for data
  preparation and model training.
- **Enable debugging and
  logging** (MLCOST-23) - A debugger like
  [SageMaker AI
  Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md") can identify training problems like system
  bottlenecks, overfitting and saturated activation functions.
  It provides
  [built-in
  rules](../../../sagemaker/latest/dg/debugger-built-in-rules.md "../../../sagemaker/latest/dg/debugger-built-in-rules.md") like LowGPUUtilization or Overfit to monitor
  your workload and automatically stop a training job as soon
  as it detects an issue (such as bug, job failing to
  converge…). SageMaker AI Debugger also provides profiler
  capabilities to
  detect [under-utilization
  of system resources](https://aws.amazon.com/fr/blogs/machine-learning/identifying-training-bottlenecks-and-system-resource-under-utilization-with-amazon-sagemaker-debugger/ "https://aws.amazon.com/fr/blogs/machine-learning/identifying-training-bottlenecks-and-system-resource-under-utilization-with-amazon-sagemaker-debugger/") and help right-size your
  environment. This helps avoid unnecessary carbon emissions.
- **Select optimal computing instance
  size** (MLCOST-09) - Use SageMaker AI Studio to switch
  instance types on the fly based on your needs (for example,
  use a low power type for exploratory data analysis, and then
  switch to GPU only to prototype some neural network code).
  Right size your training jobs with
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch") metrics that monitor resources, such as
  CPU, GPU, memory, and disk utilization.
- **Select local training for small
  scale experiments** (MLCOST-11) and
  **Start training with small
  datasets** (MLCOST-17) - Experiment with smaller
  datasets in your development notebook. This approach allows
  you to iterate quickly with limited carbon emission.
- **Stop resources when not in
  use** (MLCOST-16) - When building your model, use
  [lifecycle
  configuration scripts](../../../sagemaker/latest/dg/notebook-lifecycle-config.md "../../../sagemaker/latest/dg/notebook-lifecycle-config.md") to
  [automatically
  stop](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/tree/master/scripts/auto-stop-idle "https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/tree/master/scripts/auto-stop-idle") idle SageMaker AI Notebook instances. If you are
  using
  [SageMaker AI
  Studio](https://aws.amazon.com/sagemaker/studio/ "https://aws.amazon.com/sagemaker/studio/"), install the
  [auto-shutdown
  Jupyter extension](https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/") to detect and stop idle resources.
  Use the
  [fully
  managed training process](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md") provided by SageMaker AI to
  automatically launch training instances and shut them down
  as soon as the training job is complete. This minimizes idle
  compute resources and thus limits the environmental impact
  of your training job.
