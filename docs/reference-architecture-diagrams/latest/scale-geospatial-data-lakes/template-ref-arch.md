

# Scale Geospatial Data Lakes on AWS
<a name="template-ref-arch"></a>

Publication date: **August 14, 2023 ([Diagram history](#diagram-history))**

Repositories of geospatial data are becoming [increasingly important](https://www.youtube.com/watch?v=74ayGG6SZLw) in many organizations – for use in everything from logistics and insurance to supply chain optimization. This reference architecture shows you how to build scalable geospatial data repositories on AWS. It simplifies the design of geospatial data pipelines, allowing accelerated access to raw data by integrating AWS-managed datasets from the [Registry of Open Data on AWS](https://registry.opendata.aws/), eliminating the need to store it on your data lake. It integrates with a variety of dissemination mechanisms and supports diverse processing demands.

## Scale Geospatial Data Lakes on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to build scalable geospatial data repositories on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/scale-geospatial-data-lakes/images/scale-geospatial-data-lakes.png)


1. Initiate a data ingestion pipeline based on new scene detection.  Subscribe to **Amazon Simple Notification Service** (Amazon SNS) topics for managed datasets with appropriate filters. 

    A time-based event can be configured using **Amazon CloudWatch** rules to begin ingestion during specific time windows. 

1.  **AWS Lambda** queries the [SpatioTemporal Asset Catalogs (STAC) API](https://stacspec.org/en) for a respective dataset to get product details. It initiates the data processing pipeline through **AWS Step Functions**. 

1.  **Step Functions** orchestrates the processing tasks. Parallel or sequential processing can be configured based on task characteristics and requirements. 

1.  **Amazon Elastic Container Service** (Amazon ECS) runs containerized tasks to: 
   +  Download the products from datasets hosted on the Registry of Open Data on AWS. 
   +  Process (crop and geomosiac) the tiles to area of interest and store them in **Amazon Simple Storage Service** (Amazon S3) aoi-processed bucket. Build metadata and store them in **Amazon DynamoDB**. Store vector data in **Amazon Aurora** Postgres with PostGIS extensions. 

1.  **Step Functions** initiates the next processing task with **Amazon SageMaker AI**. 

1.  **SageMaker AI**-hosted ML models perform cloud removal and band math. 

1.  **Amazon WorkSpaces** hosted GIS workbenches can be used for visualization. The data is stored in an **Amazon S3** preprocessed bucket. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Video, AWS Summit, Brussels 2022](https://www.youtube.com/watch?v=74ayGG6SZLw) 
+  [Registry of Open Data on AWS](https://registry.opendata.aws/) 
+  [SpatioTemporal Asset Catalogs (STAC) API](https://stacspec.org/en) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Ajit Rajdeosingh, Senior Solutions Architect, Amazon Web Services 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 14, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.