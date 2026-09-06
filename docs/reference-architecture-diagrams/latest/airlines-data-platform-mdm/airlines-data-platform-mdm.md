

# Airline Data Platform with Master Data Management
<a name="airlines-data-platform-mdm"></a>

Publication date: **September 1, 2022 ([Diagram history](#airlines-data-platform-mdm-history))**

This reference architecture enhances the airline customer data platform with master data management (MDM) tools. Airlines use this architecture to identify unique travelers and detect duplicate records in loyalty membership databases. You can develop a single view of the customer beyond loyalty members.

Without MDM, airlines maintain fragmented customer profiles across multiple systems. Duplicate records reduce the accuracy of segmentation models and personalization efforts. This architecture adds MDM capabilities using ML transforms in AWS Glue to identify and merge duplicate customer records automatically.

This architecture uses the [Airlines Data Platform](../airlines-data-platform/airlines-data-platform.html) as its foundation.

## Airline data platform with MDM diagram
<a name="airlines-data-platform-mdm-diagram"></a>

![Architecture for airline MDM using AWS Glue ML transforms, Amazon S3, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/airlines-data-platform-mdm/images/svoc_data_platform_mdm_ra.png)


The following steps describe the architecture:

1. Augment the single view of customer data as a service by using an MDM tool. Build simple MDM with customer identification and deduplication. Use ML transforms in [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to identify duplicates in loyalty membership and customers without loyalty signups.

1. Adapt the operations data stores, data lakes, and analytics platforms to new customer data feeds. Deliver new capabilities as new versions of customer-centric microservices and events.

1. Enhance the data lake by changing to a customer-centric view. Store lifetime value, revenue index, and service index data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Agile development teams quickly add new microservices. These microservices consume and publish customer-centric services.

1. Agile data teams quickly augment the enterprise data warehouse (EDW). Add customer-centric domain schemas and data marts in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/).

1. Data scientists use existing raw and curated data plus new customer data. Build models in [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for segmentation and lifetime value.

## Further reading
<a name="airlines-data-platform-mdm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="airlines-data-platform-mdm-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#airlines-data-platform-mdm-history) | Reference architecture diagram first published. | September 1, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.