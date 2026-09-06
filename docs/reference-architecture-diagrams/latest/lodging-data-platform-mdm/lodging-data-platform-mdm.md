

# Lodging Data Platform with Master Data Management
<a name="lodging-data-platform-mdm"></a>

Publication date: **October 7, 2022 ([Diagram history](#ldpmdm-history))**

With this architecture, you can enhance the lodging data platform with MDM tools. Identify unique travelers and deduplicate loyalty membership records. Use the ML Transform feature in [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to identify duplicate customers. Build a single view of each customer that extends beyond loyalty members.

## Lodging data platform with MDM diagram
<a name="ldpmdm-diagram"></a>

![How to enhance the lodging data platform with MDM by using AWS Glue ML Transform.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/lodging-data-platform-mdm/images/lodging-data-platform-mdm.png)


The following steps describe the architecture:

1. Augment the single view of customer data as a service by using an MDM tool. Create a unified customer record. Use the ML Transform feature in AWS Glue to identify duplicates in loyalty membership and customers who have not signed up for loyalty.

1. Adapt the operations data stores, data lakes, and analytics platforms to new customer data feeds. Deliver new capabilities as new versions of customer-centric microservices and events.

1. Enhance the data lake by changing to a customer-centric view for lifetime value, revenue index, and service index.

1. Add new microservices to consume and publish the new customer-centric services by using [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/).

1. Augment the enterprise data warehouse (EDW) with new customer-centric domain schemas and data marts in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/).

1. Use existing raw and curated data and new customer data to build new models in [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Further reading
<a name="ldpmdm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ldpmdm-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ldpmdm-history) | Reference architecture diagram first published. | October 7, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.