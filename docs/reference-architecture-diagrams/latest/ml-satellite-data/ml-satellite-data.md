

# Run Machine Learning Algorithms with Satellite Data
<a name="ml-satellite-data"></a>

Publication date: **May 24, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to use [AWS Ground Station](https://docs.aws.amazon.com/ground-station/latest/ug/what-is-aws-ground-station.html) to ingest satellite imagery. With [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), you can label image data, train an ML model, and deploy inferences for automated image analysis.

## Run Machine Learning Algorithms with Satellite Data
<a name="diagram1"></a>

![Architecture diagram showing machine learning algorithms with satellite data by using AWS Ground Station and SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ml-satellite-data/images/ml-satellite-data.png)


The following steps describe the architecture:

1. The satellite sends data and imagery to the AWS Ground Station antenna.

1. AWS Ground Station delivers baseband or digitized RF-over-IP data to an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance.

1. The Amazon EC2 instance receives and processes the data, and then stores it in an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

1. A Jupyter Notebook ingests data from the Amazon S3 bucket to prepare the data for training.

1. SageMaker AI Ground Truth labels the images.

1. The labeled images are stored in the Amazon S3 bucket.

1. The Jupyter Notebook hosts the training algorithm and code.

1. SageMaker AI runs the training algorithm on the data and trains the ML model.

1. SageMaker AI deploys the ML models to an endpoint.

1. The SageMaker AI ML model processes image data and stores the generated inferences and metadata in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

1. Image data received into Amazon S3 automatically triggers an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function to run ML services on the image data.

1. Applications interact with [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) to access the ML algorithm and database.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Ground Station product page](https://aws.amazon.com/ground-station/)
+ [Amazon SageMaker AI product page](https://aws.amazon.com/sagemaker/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 24, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.