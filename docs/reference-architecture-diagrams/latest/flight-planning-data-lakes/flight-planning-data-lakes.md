

# Flight Planning Using Data Lakes and AI/ML
<a name="flight-planning-data-lakes"></a>

Publication date: **July 16, 2020 ([Diagram history](#flight-planning-history))**

With this architecture, you can improve hold time prediction and departure clearance time estimation. Use published schedules, flight information, airport weather, historical hold times, and aircraft data. You combine batch and real-time feeds in a tiered data lake for predictive modeling.

## Flight planning data lakes diagram
<a name="flight-planning-diagram"></a>

![Architecture for flight planning using Amazon S3, AWS Glue, Amazon EMR, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/flight-planning-data-lakes/images/flight-planning-using-data-lakes-and-ai-ml-ra.png)


The following steps describe the architecture:

1. Use published schedules from OAG for a full picture of arriving flights by time of day.

1. Augment with actual flight data through real-time flight information feeds.

1. Use flight plans, surface movement, and on-route information from FAA System Wide Information Management (SWIM). This provides an airspace and taxiway picture.

1. Use Meteorological Aerodrome Report (METAR) weather observations and Terminal Aerodrome Forecast (TAF) data. Correlate hold time to weather conditions.

1. Use historical hold times to build predictive models. Train models by airport, time of day, and weather conditions.

1. Build a tiered data lake on [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Ingest and process both batch and real-time feeds.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) to discover, catalog, and process data into Apache Parquet format.

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to build, train, tune, and deploy predictive models. Use Debugger and Model Monitor for model quality.

1. Build an operational data store for real-time predictions. Integrate predictions into flight planning systems.

## Further reading
<a name="flight-planning-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="flight-planning-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#flight-planning-history) | Reference architecture diagram first published. | July 16, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.