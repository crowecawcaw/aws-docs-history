

# AWS Industrial IoT Predictive Maintenance ML Model
<a name="industrial-iot-predictive-maintenance-ml"></a>

Publication date: **July 8, 2020 ([Diagram history](#pdm-diagram-history))**

With this architecture, you can create a Predictive Maintenance (PdM) machine learning (ML) model by using [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) and [AWS IoT Analytics](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-analytics). AWS IoT SiteWise collects, organizes, and stores data from factory equipment. This makes clean, contextual, and structured data sets available for data scientists to train ML models.

## Predictive maintenance ML model architecture diagram
<a name="pdm-diagram"></a>

![Reference architecture diagram for creating a predictive maintenance ML model by using AWS IoT SiteWise and AWS IoT Analytics on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-iot-predictive-maintenance-ml/images/aws-industrial-PdM-ML-storage-RA.png)


The following steps describe the architecture:

1. Configure the AWS IoT SiteWise Connector on [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) to connect and collect data from factory machines by using OPC Unified Architecture (OPC-UA).

1. Use AWS IoT SiteWise to model assets that represent on-premises devices, equipment, and processes.

1. Create a custom web portal with AWS IoT SiteWise Monitor to visualize factory data in near real time. IAM Identity Center provides user authentication for the portal.

1. Use the [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) Rules Engine to route data to AWS IoT Analytics.

1. For other industrial data, use AWS IoT Greengrass stream manager to publish data to AWS IoT Core.

1. Build a Docker image and add it to [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) (Amazon ECR).

1. In AWS IoT Analytics, create a Container Data set from the AWS IoT SiteWise Data store. Link it to the Docker container in Amazon ECR.

1. Create a Jupyter Notebook for the data set to build a PdM ML model. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for model training and deployment.

1. Visualize analysis with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) on the AWS IoT Analytics data source.

## Further reading
<a name="pdm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="pdm-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#pdm-diagram-history) | Reference architecture diagram first published. | July 8, 2020 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.