End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# AWS Panorama concepts

In AWS Panorama, you create computer vision applications and deploy them to the AWS Panorama Appliance or a compatible device
to analyze video streams from network cameras. You write application code in Python and build application containers
with Docker. You use the AWS Panorama Application CLI to import machine learning models locally or from Amazon Simple Storage Service (Amazon S3). Applications
use the AWS Panorama Application SDK to receive video input from a camera and interact with a model.

###### Concepts

- [The AWS Panorama Appliance](#gettingstarted-concepts-appliance "#gettingstarted-concepts-appliance")
- [Compatible devices](#gettingstarted-concepts-devices "#gettingstarted-concepts-devices")
- [Applications](#gettingstarted-concepts-application "#gettingstarted-concepts-application")
- [Nodes](#gettingstarted-concepts-node "#gettingstarted-concepts-node")
- [Models](#gettingstarted-concepts-model "#gettingstarted-concepts-model")

## The AWS Panorama Appliance

The AWS Panorama Appliance is the hardware that runs your applications. You use the AWS Panorama console to register an
appliance, update its software, and deploy applications to it. The software on the AWS Panorama Appliance
connects to camera streams, sends frames of video to your application, and displays video output on an attached
display.

The AWS Panorama Appliance is an _edge device_
[powered by Nvidia Jetson AGX Xavier](gettingstarted-hardware.md "gettingstarted-hardware.md"). Instead of sending images to
the AWS Cloud for processing, it runs applications locally on optimized hardware. This enables you to analyze
video in real time and process the results locally. The appliance requires an internet connection to report its
status, to upload logs, and to perform software updates and deployments.

For more information, see [Managing the AWS Panorama Appliance](panorama-appliance.md "panorama-appliance.md").

## Compatible devices

In addition to the AWS Panorama Appliance, AWS Panorama supports compatible devices from AWS Partners. Compatible devices
support the same features as the AWS Panorama Appliance. You register and manage compatible devices with the AWS Panorama console
and API, and build and deploy applications in the same way.

######

- [Lenovo ThinkEdge® SE70](https://techtoday.lenovo.com/us/en/solutions/smb/thinkedge "https://techtoday.lenovo.com/us/en/solutions/smb/thinkedge") – Powered by Nvidia Jetson Xavier NX

The content and sample applications in this guide are developed with the AWS Panorama Appliance. For more information
about specific hardware and software features for your device, refer to the manufacturer's documentation.

## Applications

Applications run on the AWS Panorama Appliance to perform computer vision tasks on video streams. You can build
computer vision applications by combining Python code and machine learning models, and deploy them to the AWS Panorama Appliance over the
internet. Applications can send video to a display, or use the AWS SDK to send results to AWS services.

To build and deploy applications, you use the AWS Panorama Application CLI. The AWS Panorama Application CLI is a command-line tool that generates
default application folders and configuration files, builds containers with Docker, and uploads assets. You can
run multiple applications on one device.

For more information, see [Managing AWS Panorama applications](panorama-applications.md "panorama-applications.md").

## Nodes

An application comprises multiple components called _nodes_, which represent inputs,
outputs, models, and code. A node can be configuration only (inputs and outputs), or include artifacts (models and
code). An application's code node are bundled in _node packages_ that you upload to an Amazon S3
access point, where the AWS Panorama Appliance can access them. An _application manifest_ is a
configuration file that defines connections between the nodes.

For more information, see [Application nodes](applications-nodes.md "applications-nodes.md").

## Models

A computer vision model is a machine learning network that is trained to process images. Computer vision models
can perform various tasks such as classification, detection, segmentation, and tracking. A computer vision model takes an image as input
and outputs information about the image or objects in the image.

AWS Panorama supports models built with PyTorch, Apache MXNet, and TensorFlow. You can build models with Amazon SageMaker AI or in your development
environment. For more information, see [Computer vision models](applications-models.md "applications-models.md").
