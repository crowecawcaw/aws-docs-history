# Livestock Counting at the Edge

Publication date: **July 12, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables you to build a near real-time, automated counting application for
livestock. Use **Amazon SageMaker AI** and **AWS IoT Greengrass** to build and deploy a livestock counting application at the edge.

## Livestock Counting at the Edge Diagram

![Reference architecture diagram showing livestock counting at the edge](images/livestock-counting-at-the-edge.png)

1. Upload videos and images to **Amazon Simple Storage Service** (Amazon S3) to train
   the livestock detection model.
2. Use **Amazon SageMaker AI**
   **Notebooks** to process these videos and create a labelling
   job using **Amazon SageMaker AI**
   **Ground Truth**.
3. Split the annotated dataset into training and validation sets, and use **Amazon SageMaker AI** distributed training for livestock detection.
4. Use **Amazon SageMaker AI**
   **Neo** to optimize the livestock detection model for
   specific target devices like NVIDIA Jetson Nano, TX2, Xavier, **AWS DeepLens** , or Raspberry Pi.
5. Deploy the machine learning model and counting application **AWS Lambda** function to the edge device using **AWS IoT Greengrass**.
6. Consume live video streams from a camera at the farm using real-time streaming
   protocol (RTSP) through camera serial interface (CSI) or through USB connected to the edge
   hardware.
7. Run ML Inference on the video frames from step 6 and pass the bounding box outputs to
   the counting application **Lambda** function.
8. Connect to the web server running on edge devices and control when to start/stop
   counting through a mobile application.
9. Submit near real-time counts to an inventory management system.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/livestock-counting-at-the-edge.md "samples/livestock-counting-at-the-edge.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- |
| Initial publication | Reference architecture diagram first published. | July 12, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
