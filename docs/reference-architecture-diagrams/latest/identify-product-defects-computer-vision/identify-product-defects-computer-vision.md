

# Identify Product Defects using Industrial Computer Vision
<a name="identify-product-defects-computer-vision"></a>

Publication date: **October 10, 2024 ([Diagram history](#ipd-diagram-history))**

With this architecture, you can detect anomalies such as casting metal defects, damage, and irregularities in X-ray images. You use [Amazon Lookout for Vision](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for quality inspection in manufacturing.

## Product defects computer vision architecture diagram
<a name="ipd-diagram"></a>

![Architecture diagram for detecting product defects with computer vision and Amazon Lookout for Vision on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/identify-product-defects-computer-vision/images/identify-product-defects-using-industrial-computer-vision-ra.png)


The following steps describe the architecture:

1. Capture images under consistent conditions with X-ray machines, cameras, and other devices.

1. Transfer product images to AWS with [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/), or [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) for edge devices.

1. Store product images in Amazon S3 separated into train and test datasets.

1. Use Amazon Lookout for Vision on the training dataset to label, train, tune, and deploy the defect detection model.

1. Expose the model through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) and Lambda for admins and data scientists to manage.

1. For runtime inference, use Lambda to start the model. Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) with Lambda to orchestrate a serverless workflow.

1. For batch anomaly detection, submit a batch job to [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/) with [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) for compute.

1. Notify users on confidence level through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS). If the minimum confidence threshold is not met, the user provides input to label undetected data.

1. Store final results in Amazon S3 for [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) visualization. Write results back to the manufacturing execution system (MES) on the shop floor.

## Further reading
<a name="ipd-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipd-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ipd-diagram-history) | Reference architecture diagram first published. | October 10, 2024 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.