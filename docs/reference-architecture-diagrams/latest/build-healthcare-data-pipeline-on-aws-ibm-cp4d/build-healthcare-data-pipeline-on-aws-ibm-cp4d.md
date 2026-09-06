

# Build a Healthcare Data Pipeline on AWS with IBM Cloud Pak for Data
<a name="build-healthcare-data-pipeline-on-aws-ibm-cp4d"></a>

Publication date: **April 19, 2023 ([Diagram history](#diagram-history))**

This architecture helps you build data pipelines and use machine learning (ML) models to predict patient treatment outcome, readmission rate, or disease progression. 

## Build a Healthcare Data Pipeline on AWS with IBM Cloud Pak for Data Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing a data pipeline on AWS with IBM Cloud Pak for Data.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/build-healthcare-data-pipeline-on-aws-ibm-cp4d/images/build-healthcare-data-pipeline-on-aws-ibm-cp4d.png)


1. Connected medical devices stream patient health information to **Amazon Data Firehose**. 

1. **AWS Lambda** applies data format transformations on the stream data. 

1. If the transformation fails, **Amazon Simple Notification Service** (Amazon SNS) receives a notification and invokes a re-processing API to rectify the failure. 

1. After successful format transformation, **Firehose** persists data on **Amazon Simple Storage Service** (Amazon S3). 

1. [IBM Cloud Pak for Data](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-watson-studio) (CP4D) uses its connection services to access data in **Amazon S3** and on-premises. 

1. You can use [IBM Watson Knowledge Catalog](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-watson-knowledge-catalog) to create a data governance framework, perform data enrichment, and train ML models. You can create data protection rules for data access and mask sensitive information. 

1. With [IBM DataStage](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-datastage), you can create, edit, load, and run data transformation jobs to generate enriched and tailored information. 

1. Use [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio) to analyze data, and build and train ML models. 

1. Trained models are deployed to [IBM Watson Machine Learning](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-watson-machine-learning) and are exposed as endpoints. These endpoints are integrated within a healthcare application to provide insights into patient condition. 

1. Dashboards provide information for patient treatment, outcome prediction, readmission rate and disease progression. 

1. [IBM Security QRadar XDR](https://www.ibm.com/qradar) on **Amazon Elastic Compute Cloud** (Amazon EC2) collects, processes and aggregates **Amazon VPC** flow logs, **AWS CloudTrail** logs and IBM CP4D logs. It uses these to manage security and provide near real-time monitoring and threat alerts. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [IBM Cloud Pak for Data ](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x) 
+  [IBM Watson Knowledge Catalog ](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-watson-knowledge-catalog) 
+  [IBM DataStage](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-datastage) 
+  [IBM Watson Studio ](https://www.ibm.com/cloud/watson-studio) 
+  [IBM Watson Machine Learning ](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.6.x?topic=services-watson-machine-learning) 
+  [IBM Security QRadar XDR](https://www.ibm.com/qradar) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 19, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.