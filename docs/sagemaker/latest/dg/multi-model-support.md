# Supported algorithms, frameworks, and instances for multi-model endpoints

For information about the algorithms, frameworks, and instance types that you can use with
multi-model endpoints, see the following sections.

## Supported algorithms, frameworks, and instances

for multi-model endpoints using CPU backed instances

The inference containers for the following algorithms and frameworks support multi-model
endpoints:

- [XGBoost algorithm with Amazon SageMaker AI](xgboost.md "xgboost.md")
- [K-Nearest Neighbors (k-NN) Algorithm](k-nearest-neighbors.md "k-nearest-neighbors.md")
- [Linear Learner Algorithm](linear-learner.md "linear-learner.md")
- [Random Cut Forest (RCF) Algorithm](randomcutforest.md "randomcutforest.md")
- [Resources for using TensorFlow with Amazon SageMaker AI](tf.md "tf.md")
- [Resources for using Scikit-learn with Amazon SageMaker AI](sklearn.md "sklearn.md")
- [Resources for using Apache MXNet with Amazon SageMaker AI](mxnet.md "mxnet.md")
- [Resources for using PyTorch with Amazon SageMaker AI](pytorch.md "pytorch.md")

To use any other framework or algorithm, use the SageMaker AI inference toolkit to build a
container that supports multi-model endpoints. For information, see [Build Your Own Container for SageMaker AI
Multi-Model Endpoints](build-multi-model-build-container.md "build-multi-model-build-container.md").

Multi-model endpoints support all of the CPU instance types.

## Supported algorithms, frameworks, and instances

for multi-model endpoints using GPU backed instances

Hosting multiple GPU backed models on multi-model endpoints is supported through the
[SageMaker AI Triton Inference
server](triton.md "triton.md"). This supports all major inference frameworks such as NVIDIA® TensorRT™,
PyTorch, MXNet, Python, ONNX, XGBoost, scikit-learn, RandomForest, OpenVINO, custom C++, and
more.

To use any other framework or algorithm, you can use Triton backend for Python or C++ to
write your model logic and serve any custom model. After you have the server ready, you can
start deploying 100s of Deep Learning models behind one endpoint.

Multi-model endpoints support the following GPU instance types:

| Instance family | Instance type    | vCPUs | GiB of memory per vCPU | GPUs | GPU memory |
| --------------- | ---------------- | ----- | ---------------------- | ---- | ---------- |
| p2              | ml.p2.xlarge     | 4     | 15.25                  | 1    | 12         |
| p3              | ml.p3.2xlarge    | 8     | 7.62                   | 1    | 16         |
| g5              | ml.g5.xlarge     | 4     | 4                      | 1    | 24         |
| g5              | ml.g5.2xlarge    | 8     | 4                      | 1    | 24         |
| g5              | ml.g5.4xlarge    | 16    | 4                      | 1    | 24         |
| g5              | ml.g5.8xlarge    | 32    | 4                      | 1    | 24         |
| g5              | ml.g5.16xlarge   | 64    | 4                      | 1    | 24         |
| g4dn            | ml.g4dn.xlarge   | 4     | 4                      | 1    | 16         |
| g4dn            | ml.g4dn.2xlarge  | 8     | 4                      | 1    | 16         |
| g4dn            | ml.g4dn.4xlarge  | 16    | 4                      | 1    | 16         |
| g4dn            | ml.g4dn.8xlarge  | 32    | 4                      | 1    | 16         |
| g4dn            | ml.g4dn.16xlarge | 64    | 4                      | 1    | 16         |
