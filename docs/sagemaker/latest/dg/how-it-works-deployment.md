# Model deployment options in Amazon SageMaker AI

After you train your machine learning model, you can deploy it using Amazon SageMaker AI to get predictions. Amazon SageMaker AI supports the following
ways to deploy a model, depending on your use case:

- For persistent, real-time endpoints that make one prediction at a time, use SageMaker AI
  real-time hosting services. See [Real-time inference](realtime-endpoints.md "realtime-endpoints.md").
- Workloads that have idle periods between traffic spikes and can tolerate cold
  starts, use Serverless Inference. See [Deploy models with Amazon SageMaker Serverless Inference](serverless-endpoints.md "serverless-endpoints.md").
- Requests with large payload sizes up to 1GB, long processing times, and near real-time latency requirements,
  use Amazon SageMaker Asynchronous Inference. See [Asynchronous inference](async-inference.md "async-inference.md").
- To get predictions for an entire dataset, use SageMaker AI batch transform. See [Batch transform for inference with Amazon SageMaker AI](batch-transform.md "batch-transform.md").
  SageMaker AI also provides features to manage resources and optimize inference performance when deploying machine learning models:

- To manage models on edge devices so that you can optimize, secure, monitor,
  and maintain machine learning models on fleets of edge devices, see [Model deployment at the edge with SageMaker Edge Manager](edge.md "edge.md"). This applies to edge devices like smart
  cameras, robots, personal computers, and mobile devices.
- To optimize Gluon, Keras, MXNet, PyTorch, TensorFlow, TensorFlow-Lite, and ONNX models for inference on Android, Linux,
  and Windows machines based on processors from Ambarella, ARM, Intel, Nvidia, NXP, Qualcomm,
  Texas Instruments, and Xilinx, see [Model performance optimization with SageMaker Neo](neo.md "neo.md").
  For more information about all deployment options, see [Deploy models for inference](deploy-model.md "deploy-model.md").
