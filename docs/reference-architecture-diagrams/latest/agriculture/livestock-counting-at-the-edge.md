

# Livestock Counting at the Edge
<a name="livestock-counting-at-the-edge"></a>

Publication date: **July 12, 2022 ([Diagram history](diagram-history.md))**

This architecture enables you to build a near real-time, automated counting application for livestock. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) and [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) to build and deploy a livestock counting application at the edge.

## Livestock Counting at the Edge diagram
<a name="livestock-counting-at-the-edge-diagram1"></a>

![Reference architecture diagram showing livestock counting at the edge](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/agriculture/images/livestock-counting-at-the-edge.png)


1. Upload videos and images to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) to train the livestock detection model.

1. Use Amazon SageMaker AI Notebooks to process these videos and create a labeling job using Amazon SageMaker AI Ground Truth.

1. Split the annotated dataset into training and validation sets, and use Amazon SageMaker AI distributed training for livestock detection.

1. Use Amazon SageMaker AI Neo to optimize the livestock detection model for specific target devices like NVIDIA Jetson Nano, TX2, Xavier, AWS DeepLens , or Raspberry Pi.

1. Deploy the machine learning model and counting application [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function to the edge device using AWS IoT Greengrass.

1. Consume live video streams from a camera at the farm using real-time streaming protocol (RTSP) through camera serial interface (CSI) or through USB connected to the edge hardware.

1. Run ML Inference on the video frames from step 6 and pass the bounding box outputs to the counting application Lambda function.

1. Connect to the web server running on edge devices and control when to start/stop counting through a mobile application.

1. Submit near real-time counts to an inventory management system.

## Further reading
<a name="livestock-counting-at-the-edge-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 