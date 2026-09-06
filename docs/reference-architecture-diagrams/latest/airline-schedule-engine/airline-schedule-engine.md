

# Airline Schedule Engine
<a name="airline-schedule-engine"></a>

Publication date: **May 3, 2021 ([Diagram history](#schedule-engine-history))**

An airline schedule engine aggregates batch and real-time flight data to support fast flight and schedule lookups. With this architecture, you can create a scalable, configurable, and fault-tolerant tier-0 system. It uses purpose-built databases, serverless compute, and a data lake to reduce total cost of ownership.

This architecture uses the [Airport Terminal Optimizer](../airport-terminal-optimizer/airport-terminal-optimizer.html) as a source for schedule data context. You can combine batch inputs with real-time data feeds to build complete flight schedules.

## Airline schedule engine diagram
<a name="schedule-engine-diagram"></a>

![Architecture for airline schedule engine using Amazon DynamoDB, Amazon Neptune, and AWS Glue.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/airline-schedule-engine/images/airline-schedule-builder-ra.png)


The following steps describe the architecture:

1. Load all batch inputs such as Standard Schedules Information Manual (SSIM) into a batch staging bucket in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Load all real-time data feeds such as Standard Schedule Messages (SSM) and flight information (FLIFO) into a real-time staging bucket in Amazon S3.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) processes to discover, catalog, and process inputs. Create processed data in Amazon S3. Combine batch and real-time data.

1. Create flight data by converting schedule files into individual flights. Load the data into [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for direct flight lookup.

1. Run flight lookups through [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and DynamoDB with in-memory caching from DynamoDB Accelerator (DAX). Ingest and serve FLIFO events with flight data.

1. Process routes with mileage, day of week, seasonality, and airline type. Load the data into [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) graph database for route lookups by origin and destination.

1. Apply duration and mileage rules. Retrieve flights for each route and combine them with connection rules to create the full schedule. Use [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/) for Redis for performance.

1. Maintain connection rules in DynamoDB for fast retrieval. Manage these rules with a connection rules dashboard.

1. Use [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to improve route building and schedule lookup performance.

## Further reading
<a name="schedule-engine-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="schedule-engine-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#schedule-engine-history) | Reference architecture diagram first published. | May 3, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.