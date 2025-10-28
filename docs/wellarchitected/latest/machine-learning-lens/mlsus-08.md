# MLSUS-08: Select energy-efficient algorithms

To minimize resource usage, replace algorithms with more
efficient versions that produce the same result. 

## Implementation plan

- **Begin with a simple algorithm to
  establish a baseline** - Then
  [test
  different algorithms with increasing complexity](mlper-07.md "mlper-07.md") to
  observe whether performance has improved. If so, compare
  the performance gain against the difference in resources
  required.
- **Try to find simplified versions of
  algorithms** - This approach helps you use less
  resources to achieve a similar outcome. For example,
  [DistilBERT](https://blog.tensorflow.org/2020/05/how-hugging-face-achieved-2x-performance-boost-question-answering.html "https://blog.tensorflow.org/2020/05/how-hugging-face-achieved-2x-performance-boost-question-answering.html"),
  a distilled version of
  [BERT](<https://en.wikipedia.org/wiki/BERT_(language_model)> "https://en.wikipedia.org/wiki/BERT_(language_model)"),
  has 40% fewer parameters, runs 60% faster, and preserves
  97% of its performance.
- **Compress models size without
  significant loss of accuracy** - Use
  [pruning](https://aws.amazon.com/blogs/machine-learning/pruning-machine-learning-models-with-amazon-sagemaker-debugger-and-amazon-sagemaker-experiments/ "https://aws.amazon.com/blogs/machine-learning/pruning-machine-learning-models-with-amazon-sagemaker-debugger-and-amazon-sagemaker-experiments/")
  to remove weights that don’t contribute much to the model.
  Use
  [quantization](https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/ "https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/")
  to represent numbers with the low-bit integers without
  incurring significant loss in accuracy. These techniques
  speed up inference and save energy with limited impact on
  accuracy.
- **Employ
  [Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/ "https://aws.amazon.com/sagemaker/neo/")** - Optimize ML models for
  inference on SageMaker AI in the cloud and supported devices
  at the edge.

## Documents

- [Explore
  alternatives for performance improvement](mlper-07.md "mlper-07.md")
- [DistilBERT,
  a distilled version of BERT: smaller, faster, cheaper and
  lighter](https://arxiv.org/abs/1910.01108 "https://arxiv.org/abs/1910.01108")
- [Optimize
  model performance using Amazon SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 2, model
  development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/")
- [Pruning
  machine learning models with Amazon SageMaker AI Debugger and
  Amazon SageMaker AI Experiments](https://aws.amazon.com/blogs/machine-learning/pruning-machine-learning-models-with-amazon-sagemaker-debugger-and-amazon-sagemaker-experiments/ "https://aws.amazon.com/blogs/machine-learning/pruning-machine-learning-models-with-amazon-sagemaker-debugger-and-amazon-sagemaker-experiments/")
- [Reduce
  ML inference costs on Amazon SageMaker AI with hardware and
  software acceleration](https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/ "https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/")
- [Unlock
  near 3x performance gains with XGBoost and Amazon SageMaker AI Neo](https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/ "https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/")

## Metrics

- Track the metrics related to the
  [resources
  provisioned](../../../sagemaker/latest/APIReference/API_ResourceConfig.md "../../../sagemaker/latest/APIReference/API_ResourceConfig.md") for your training and inference jobs
  (InstanceCount, InstanceType, and VolumeSizeInGB) and the
  [efficient
  use of these resources](../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs "../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs") (CPUUtilization,
  GPUUtilization, GPUMemoryUtilization, MemoryUtilization,
  and DiskUtilization) in the
  [SageMaker AI
  Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm"), the
  [CloudWatch
  Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw") or your
  [SageMaker AI
  Debugger Profiling Report](../../../sagemaker/latest/dg/debugger-profiling-report.md#debugger-profiling-report-walkthrough-system-usage "../../../sagemaker/latest/dg/debugger-profiling-report.md#debugger-profiling-report-walkthrough-system-usage")
