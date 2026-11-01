

# Wafer Inspection with Machine Learning
<a name="wafer-inspection-with-machine-learning-architecture"></a>

Publication date: **September 16, 2022 ([Diagram history](diagram-history.md))**

This architecture shows you how computer vision wafer inspection accelerates defect detection and reduces human error in detecting (ring/scratch and so on), improving fab productivity.

## Wafer Inspection with Machine Learning diagram
<a name="wafer-inspection-with-machine-learning-architecture-diagram1"></a>

![Reference architecture diagram showing how computer vision wafer inspection accelerates defect detection and reduces human error in detecting (ring/scratch and so on), improving fab productivity.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/wafer-inspection-with-machine-learning-architecture.png)


1. Users upload images from wafer inspection to an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) bucket through a web user interface (UI) using transfer acceleration. 

1. Amazon S3 calls an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function, logging the new image location in an [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) table. 

1. The web interface calls an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) instance with the images metadata, which is stored in Amazon DynamoDB by a second Lambda function. 

1. The Lambda function calls [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for inference. Amazon Elastic Inference lowers the cost of inference by only attaching a graphics processing unit (GPU) when data needs to be processed. 

1. The Lambda function adds the Inference results to the Amazon DynamoDB table. 

1. Users are notified in the UI of detected defects. The UI fetches the image and metadata of the defected wafer from Amazon API Gateway. Wafers without defects move faster to the next step. 

1. To accelerate user access to the image and inference results [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) caches both static content and API calls. 

1. Amazon S3 lifecycle policies move older images to cold storage for cost optimization. 

1. Images analyzed by engineers are added to the next model-training datasets to improve inference accuracy. 

## Further reading
<a name="wafer-inspection-with-machine-learning-architecture-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 