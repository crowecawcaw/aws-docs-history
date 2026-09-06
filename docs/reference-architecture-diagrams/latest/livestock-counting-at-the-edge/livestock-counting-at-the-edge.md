

# Livestock Counting at the Edge
<a name="livestock-counting-at-the-edge"></a>

Publication date: **July 12, 2022 ([Diagram history](#diagram-history))**

This architecture enables you to build a near real-time, automated counting application for livestock. Use **Amazon SageMaker AI** and **AWS IoT Greengrass** to build and deploy a livestock counting application at the edge.

## Livestock Counting at the Edge Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing livestock counting at the edge](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/livestock-counting-at-the-edge/images/livestock-counting-at-the-edge.png)


1. Upload videos and images to **Amazon Simple Storage Service** (Amazon S3) to train the livestock detection model.

1. Use **Amazon SageMaker AI** **Notebooks** to process these videos and create a labelling job using **Amazon SageMaker AI** **Ground Truth**.

1. Split the annotated dataset into training and validation sets, and use **Amazon SageMaker AI** distributed training for livestock detection.

1. Use **Amazon SageMaker AI** **Neo** to optimize the livestock detection model for specific target devices like NVIDIA Jetson Nano, TX2, Xavier, **AWS DeepLens** , or Raspberry Pi.

1. Deploy the machine learning model and counting application **AWS Lambda** function to the edge device using **AWS IoT Greengrass**.

1. Consume live video streams from a camera at the farm using real-time streaming protocol (RTSP) through camera serial interface (CSI) or through USB connected to the edge hardware.

1. Run ML Inference on the video frames from step 6 and pass the bounding box outputs to the counting application **Lambda** function.

1. Connect to the web server running on edge devices and control when to start/stop counting through a mobile application.

1. Submit near real-time counts to an inventory management system.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 12, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.