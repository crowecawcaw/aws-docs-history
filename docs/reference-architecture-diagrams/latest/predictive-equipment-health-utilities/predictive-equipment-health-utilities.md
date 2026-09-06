

# Predictive Equipment Health for Utilities
<a name="predictive-equipment-health-utilities"></a>

Publication date: **August 3, 2021 ([Diagram history](#peh-history))**

With this architecture, you can build a modern, end-to-end, field-to-cloud solution for ingesting near-real-time data from utility assets and devices. The solution uses [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) for asset modeling, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) and [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) for predictive health analysis, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) as the data lake.

## Predictive equipment health diagram
<a name="peh-diagram"></a>

![Reference architecture diagram showing how to ingest utility asset data and predict equipment health by using AWS IoT SiteWise, SageMaker AI, Forecast, and Amazon S3.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/predictive-equipment-health-utilities/images/predictive-equipment-health-utilities.png)


The following steps describe the data flow and analytics pipeline for this architecture:

1. Connect edge data sources by using [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) and AWS IoT SiteWise edge for seamless connectivity and data preparation from Supervisory Control and Data Acquisition (SCADA) systems, third-party protocol converters, Geographic Information Systems (GIS), data historians, and edge devices. Run compiled ML models on AWS IoT SiteWise edge for local inference and actioning.

1. 2A. Ingest data directly from assets to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for non-asset-modeled data.

   2B. Ingest data at scale with asset modeling in AWS IoT SiteWise.

1. View real-time operational dashboards of critical asset performance metrics through AWS IoT SiteWise monitor or [Amazon Managed Service for Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/).

1. Build detector models in [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/) to continuously monitor asset state. Issue immediate email and SMS alerts to operational staff through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Use Amazon S3 as the data lake and single version of truth for all consumers. Perform ETL functions and build the data catalog with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Move infrequently accessed data to Amazon S3 Glacier for cost-effective archival.

1. Use curated data from the data lake with AWS AI/ML services (such as SageMaker AI and Forecast) or third-party ML services for predictive health analysis and assessment. Consume results through asset owner applications or third-party asset management tools.

1. Produce detailed business intelligence (BI) reporting through [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) and third-party solutions (GIS, asset management, and Tableau).

1. Secure all communication with AWS Security, Identity, and Compliance services. Ensure that data is fully traceable, authenticated, and encrypted.

## Further reading
<a name="peh-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="peh-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#peh-history) | Reference architecture diagram first published. | August 3, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.