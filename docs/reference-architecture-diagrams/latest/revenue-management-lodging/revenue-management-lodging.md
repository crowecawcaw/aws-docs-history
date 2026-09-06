

# Revenue Management Architecture for Lodging
<a name="revenue-management-lodging"></a>

Publication date: **October 5, 2022 ([Diagram history](#revmgmt-history))**

With this architecture, you can migrate an on-premises revenue management system to AWS. On-premises systems often limit your ability to add real-time data feeds and respond to booking changes quickly. Reduce infrastructure costs and improve forecasting accuracy by using [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) for demand forecasting, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for advanced analytics, and [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Spot Instances for cost-efficient compute.

## Revenue management diagram
<a name="revmgmt-diagram"></a>

![How to migrate revenue management to AWS by using Amazon Forecast, Amazon SageMaker AI, and Amazon Elastic Compute Cloud Spot Instances.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/revenue-management-lodging/images/revenue-management-lodging.png)


The following steps describe the architecture:

1. Build a tiered data lake by using [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Ingest and process data from batch and near real-time feeds. Add new data feeds and propagate data changes.

1. Migrate existing revenue management modules to use Amazon EC2 Spot Instances. Reduce infrastructure cost without code changes. Use [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/) to replicate the file structure required by the modules.

1. Convert outputs from the revenue management modules and store them in the data lake. Use these stored outputs for reporting and analytics.

1. Run near real-time booking controls on Amazon EC2 On-Demand Instances. Adjust booking and pricing controls dynamically.

1. Provide flexible, on-demand reporting by using the data lake with [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/) and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/). Access raw, processed, and optimized data.

1. Use Forecast for regional demand forecasting models. Use SageMaker AI for advanced revenue analytics.

1. Build a revenue management dashboard for reporting, analytics, and adjustments to configurations and user overrides.

## Further reading
<a name="revmgmt-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="revmgmt-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#revmgmt-history) | Reference architecture diagram first published. | October 5, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.