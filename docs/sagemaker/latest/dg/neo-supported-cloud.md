# Supported Instance Types and Frameworks

Amazon SageMaker Neo supports popular deep learning frameworks for both compilation and
deployment. You can deploy your model to cloud instances or AWS Inferentia instance
types.

The following describes frameworks SageMaker Neo supports and the target cloud instances you
can compile and deploy to. For information on how to deploy your compiled model to a cloud
or Inferentia instance, see [Deploy a Model with Cloud Instances](neo-deployment-hosting-services.md "neo-deployment-hosting-services.md").

## Cloud Instances

SageMaker Neo supports the following deep learning frameworks for CPU and GPU cloud
instances:

| Framework  | Framework Version                           | Model Version                                         | Models                                                                                                      | Model Formats (packaged in \*.tar.gz)                                                                                                                  | Toolkits       |
| ---------- | ------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| MXNet      | 1.8.0                                       | Supports 1.8.0 or earlier                             | Image Classification, Object Detection, Semantic Segmentation, Pose Estimation, Activity Recognition        | One symbol file (.json) and one parameter file (.params)                                                                                               | GluonCV v0.8.0 |
| ONNX       | 1.7.0                                       | Supports 1.7.0 or earlier                             | Image Classification, SVM                                                                                   | One model file (.onnx)                                                                                                                                 |                |
| Keras      | 2.2.4                                       | Supports 2.2.4 or earlier                             | Image Classification                                                                                        | One model definition file (.h5)                                                                                                                        |                |
| PyTorch    | 1.4, 1.5, 1.6, 1.7, 1.8, 1.12, 1.13, or 2.0 | Supports 1.4, 1.5, 1.6, 1.7, 1.8, 1.12, 1.13, and 2.0 | Image Classification<br>Versions 1.13 and 2.0 support Object Detection, Vision Transformer, and HuggingFace | One model definition file (.pt or .pth) with input dtype of<br>float32                                                                                 |                |
| TensorFlow | 1.15.3 or 2.9                               | Supports 1.15.3 and 2.9                               | Image Classification                                                                                        | For saved models, one .pb or one .pbtxt file and a variables<br>directory that contains variables<br>For frozen models, only one .pb or<br>.pbtxt file |                |
| XGBoost    | 1.3.3                                       | Supports 1.3.3 or earlier                             | Decision Trees                                                                                              | One XGBoost model file (.model) where the number of nodes in a tree<br>is less than 2^31                                                               |                |

###### Note

“Model Version” is the version of the framework used to train and export the
model.

## Instance Types

You can deploy your SageMaker AI compiled model to one of the cloud instances listed below:

| Instance  | Compute Type          |
| --------- | --------------------- |
| `ml_c4`   | Standard              |
| `ml_c5`   | Standard              |
| `ml_m4`   | Standard              |
| `ml_m5`   | Standard              |
| `ml_p2`   | Accelerated computing |
| `ml_p3`   | Accelerated computing |
| `ml_g4dn` | Accelerated computing |

For information on the available vCPU, memory, and price per hour
for each instance type, see
[Amazon
SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

###### Note

When compiling for `ml_*` instances using PyTorch framework, use **Compiler options** field in **Output Configuration** to provide the
correct data type (`dtype`) of the model’s input.

The default is set to `"float32"`.

## AWS Inferentia

SageMaker Neo supports the following deep learning frameworks for Inf1:

| Framework  | Framework Version | Model Version                  | Models                                                                                               | Model Formats (packaged in \*.tar.gz)                                                                                                                  | Toolkits       |
| ---------- | ----------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| MXNet      | 1.5 or 1.8        | Supports 1.8, 1.5 and earlier  | Image Classification, Object Detection, Semantic Segmentation, Pose Estimation, Activity Recognition | One symbol file (.json) and one parameter file (.params)                                                                                               | GluonCV v0.8.0 |
| PyTorch    | 1.7, 1.8 or 1.9   | Supports 1.9 and earlier       | Image Classification                                                                                 | One model definition file (.pt or .pth) with input dtype of<br>float32                                                                                 |                |
| TensorFlow | 1.15 or 2.5       | Supports 2.5, 1.15 and earlier | Image Classification                                                                                 | For saved models, one .pb or one .pbtxt file and a variables<br>directory that contains variables<br>For frozen models, only one .pb or<br>.pbtxt file |                |

###### Note

“Model Version” is the version of the framework used to train and export the
model.

You can deploy your SageMaker Neo-compiled model to AWS Inferentia-based Amazon EC2 Inf1
instances. AWS Inferentia is Amazon's first custom silicon chip designed to accelerate
deep learning. Currently, you can use the `ml_inf1` instance to deploy your
compiled models.

### AWS Inferentia2 and AWS Trainium

Currently, you can deploy your SageMaker Neo-compiled model to AWS Inferentia2-based
Amazon EC2 Inf2 instances (in US East (Ohio) Region), and to AWS Trainium-based Amazon EC2 Trn1
instances (in US East (N. Virginia) Region). For more information about supported models
on these instances, see [Model Architecture Fit Guidelines](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/model-architecture-fit.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/model-architecture-fit.html") in the AWS Neuron documentation, and the examples in the
[Neuron Github repository](https://github.com/aws-neuron/aws-neuron-sagemaker-samples "https://github.com/aws-neuron/aws-neuron-sagemaker-samples").
