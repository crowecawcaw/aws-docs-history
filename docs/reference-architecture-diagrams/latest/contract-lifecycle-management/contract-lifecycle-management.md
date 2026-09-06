

# Contract Lifecycle Management and Modeling
<a name="contract-lifecycle-management"></a>

Publication date: **March 10, 2021 ([Diagram history](#contract-lifecycle-management-history))**

With this architecture, you can improve contract lifecycle management and facilitate contract modeling. You can access current and historical transactions, competitive market data, agency data, and contract data in one place. You combine these data sources with analytics tools and elastic compute.

If your airline sales team manages agency and corporate contracts, you might rely on manual processes and spreadsheets today. This workflow models contracts with scenario analysis and automates the negotiation process. It aggregates required data and uses elastic compute during the contract negotiation period.

This architecture uses Amazon Simple Storage Service (Amazon S3), AWS Glue, and Amazon EMR for data storage and processing. It also uses AWS Step Functions (Step Functions), Amazon DynamoDB (DynamoDB), and AWS Lambda (Lambda) to build the contract modeling platform.

## Contract lifecycle management and modeling diagram
<a name="contract-lifecycle-management-diagram"></a>

![Architecture for airline contract lifecycle management using Amazon S3, AWS Glue, Amazon EMR, Step Functions, DynamoDB, and Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/contract-lifecycle-management/images/contract-lifecycle-management-ra.png)


The following steps describe the architecture:

1. Use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) to create a data lake with all required data. Maintain raw, curated, and transformed data for processing efficiency.

1. Store transformed data separately by using business rules. This separation allows you to recompute results when business rules change.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for transformation, business rules application, and payment processing.

1. Process performance and payments periodically. Store the results in Amazon S3 for payment processing and performance reporting.

1. Build the contract modeling user interface with [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/).

1. Facilitate contract scenarios through Amazon EMR, Step Functions, Amazon S3, and [Amazon Athena (Athena)](https://docs.aws.amazon.com/athena/latest/ug/).

1. Manage contract negotiation and payment workflows through capabilities in the Apttus/Salesforce platform.

## Further reading
<a name="contract-lifecycle-management-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="contract-lifecycle-management-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#contract-lifecycle-management-history) | Reference architecture diagram first published. | March 10, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.