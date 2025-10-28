End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Supported computer vision models and cameras

AWS Panorama supports models built with PyTorch, Apache MXNet, and TensorFlow. When you deploy an application, AWS Panorama compiles your model in
SageMaker AI Neo. You can build models in Amazon SageMaker AI or in your development environment, as long as you use layers that are
compatible with SageMaker AI Neo.

To process video and get images to send to a model, the AWS Panorama Appliance connects to an H.264 encoded video stream
with the RTSP protocol. AWS Panorama tests a variety of common cameras for compatibility.

###### Sections

- [Supported models](#gettingstarted-compatibility-models "#gettingstarted-compatibility-models")
- [Supported cameras](#gettingstarted-compatibility-cameras "#gettingstarted-compatibility-cameras")

## Supported models

When you build an application for AWS Panorama, you provide a machine learning model that the application uses for
computer vision. You can use pre-built and pre-trained models provided by model frameworks, [a sample model](gettingstarted-sample.md#gettingstarted-sample-model "gettingstarted-sample.md#gettingstarted-sample-model"), or a model that you build and train
yourself.

###### Note

For a list of pre-built models that have been tested with AWS Panorama, see [Model compatibility](https://github.com/awsdocs/aws-panorama-developer-guide/blob/main/resources/model-compatibility.md "https://github.com/awsdocs/aws-panorama-developer-guide/blob/main/resources/model-compatibility.md").

When you deploy an application, AWS Panorama uses the SageMaker AI Neo compiler to compile your computer vision model. SageMaker AI
Neo is a compiler that optimizes models to run efficiently on a target platform, which can be an instance in
Amazon Elastic Compute Cloud (Amazon EC2), or an edge device such as the AWS Panorama Appliance.

AWS Panorama supports the versions of PyTorch, Apache MXNet, and TensorFlow that are supported for edge devices by SageMaker AI Neo. When you build
your own model, you can use the framework versions listed in the [SageMaker AI Neo
release notes](https://aws.amazon.com/releasenotes/sagemaker-neo-supported-frameworks-and-operators/ "https://aws.amazon.com/releasenotes/sagemaker-neo-supported-frameworks-and-operators/"). In SageMaker AI, you can use the built-in [image classification algorithm](../../../sagemaker/latest/dg/image-classification.md "../../../sagemaker/latest/dg/image-classification.md").

For more information about using models in AWS Panorama, see [Computer vision models](applications-models.md "applications-models.md").

## Supported cameras

The AWS Panorama Appliance supports H.264 video streams from cameras that output RTSP over a local network. For camera
streams greater than 2 megapixels, the appliance scales down the image to 1920x1080 pixels or an equivalent size
that preserves the stream's aspect ratio.

The following camera models have been tested for compatibility with the AWS Panorama Appliance:

- [Axis](https://www.axis.com/ "https://www.axis.com/") – M3057-PLVE, M3058-PLVE, P1448-LE, P3225-LV Mk
  II
- [LaView](https://www.laviewsecurity.com/ "https://www.laviewsecurity.com/") – LV-PB3040W
- [Vivotek](https://www.vivotek.com/ "https://www.vivotek.com/") – IB9360-H
- [Amcrest](https://amcrest.com/ "https://amcrest.com/") – IP2M-841B
- **Anpviz** – IPC-B850W-S-3X, IPC-D250W-S
- **WGCC** – Dome PoE 4MP ONVIF

For the appliance's hardware specifications, see [AWS Panorama Appliance specifications](gettingstarted-hardware.md "gettingstarted-hardware.md").
