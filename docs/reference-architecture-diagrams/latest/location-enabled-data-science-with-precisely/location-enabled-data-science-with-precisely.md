

# Location-enabled Data Science with Precisely on AWS
<a name="location-enabled-data-science-with-precisely"></a>

Publication date: **September 06, 2023 ([Diagram history](#diagram-history))**

This reference architecture shows how customers can deploy [Precisely](https://www.precisely.com/solution/geocoding-and-data-enrichment-solutions) geo addressing capabilities on Amazon SageMaker AI or Amazon EMR Studio to enhance experiments with location-aware data.

## Location-enabled Data Science with Precisely on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how customers can deploy Precisely’s geo addressing capabilities on Amazon SageMaker AI or Amazon EMR Studio to enhance experiments with location-aware data.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/location-enabled-data-science-with-precisely/images/location-enabled-data-science-with-precisely.png)


1.  **Amazon CloudWatch** is scheduled to invoke **AWS Lambda** at a set intervals (such as monthly or quarterly). 

1.  **LambdaLambda** is invoked and starts to compute resources. 

1.  An **Amazon Elastic Compute Cloud** (Amazon EC2) compute instance is started. 

1.  Precisely datasets are updated at established intervals. Automatic Data Downloader monitors changes and automatically downloads data from Precisely Data Experience into **Amazon Simple Storage Service** (Amazon S3) in a variety of formats, including flat files (.txt, .csv), spatial data (.shp, .tab), and geocoding reference data (.spd). 

1.  Use **Amazon S3** to get the Geo Addressing SDK from Precisely Fulfillment. 

1.  Reference data is downloaded to your **Amazon S3** bucket. 

1.  Reference data and SDKs are ready to be used for geo addressing on **Amazon SageMaker AI** or **Amazon EMR** Studio. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Precisely - Geo addressing, geocoding, and data enrichment solutions](https://www.precisely.com/solution/geocoding-and-data-enrichment-solutions/) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Ayan Ray, Senior Partner Solutions Architect, Amazon Web Services 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | September 6, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.