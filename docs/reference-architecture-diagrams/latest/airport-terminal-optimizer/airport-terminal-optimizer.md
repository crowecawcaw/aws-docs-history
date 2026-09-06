

# Airport Terminal Optimizer
<a name="airport-terminal-optimizer"></a>

Publication date: **April 16, 2020 ([Diagram history](#terminal-optimizer-history))**

With this architecture, you can optimize terminal and gate openings for airports with multiple terminals. Use schedules from OAG (up to 330 days ahead), operating costs, and terminal configurations. You can determine the most cost-effective terminal and gate assignments during reduced schedules.

## Airport terminal optimizer diagram
<a name="terminal-optimizer-diagram"></a>

![Architecture for airport terminal optimization using AWS Glue, Amazon EMR, Amazon Athena, and Amazon Quick Sight.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/airport-terminal-optimizer/images/airport-terminal-optimizer-ra.png)


The following steps describe the architecture:

1. Airline schedules from OAG provide daily arrivals and departures. Schedules extend up to 330 days ahead.

1. The airport provides terminal and gate configurations. These include airline-specific compared to common-use gates, domestic compared to international, and capacity by aircraft type.

1. The airport provides operating costs by terminal.

1. Load batch inputs into [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Inputs include Standard Schedules Information Manual (SSIM), Standard Schedule Messages (SSM), configurations, and costs.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) to discover, catalog, and process inputs. Store results in Amazon S3 in Apache Parquet format.

1. Create flight data from the schedule files.

1. Create hourly and daily passenger traffic and landing slots from flight data.

1. Create optimized terminal and gate assignments from configurations and costs.

1. Visualize results with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

1. (Optional) Build a configuration dashboard with [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for what-if analyses.

## Further reading
<a name="terminal-optimizer-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="terminal-optimizer-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#terminal-optimizer-history) | Reference architecture diagram first published. | April 16, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.