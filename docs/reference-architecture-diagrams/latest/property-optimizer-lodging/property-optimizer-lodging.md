

# Property Optimizer for Lodging
<a name="property-optimizer-lodging"></a>

Publication date: **April 16, 2020 ([Diagram history](#propopt-history))**

With this architecture, you can forecast lodging demand and optimize property performance. Use airline schedules, shopping data, and booking information as inputs. Generate regional and property-level forecasts with artificial intelligence and machine learning (AI/ML). The solution uses [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) for ML-based forecasting, [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for data processing, and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) for visualization.

## Property optimizer diagram
<a name="propopt-diagram"></a>

![How to forecast lodging demand by using Amazon Forecast, AWS Glue, and Amazon Quick Sight.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/property-optimizer-lodging/images/property-optimizer-lodging.png)


The following steps describe the data pipeline and forecasting components for this architecture:

1. Collect daily airline arrivals and departures at each airport from OAG schedules.

1. Collect future airline shopping trends and booking data from sources such as Airline Reporting Corporation, 3Victors, and partner airlines.

1. Collect future lodging shopping trends and booking data for indirect channels from sources such as STR and TravelClick.

1. Use lodging booking engines as a source of shopping trends for direct booking.

1. Collect property data, booking, and stay data from the central reservations system (CRS) and property management system (PMS).

1. Use AWS Glue and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) to discover, catalog, and process inputs. Create processed data in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) in Parquet format.

1. Combine lodging and flight data to create accurate forecasts. Use Forecast to create AI/ML-based forecasting from historical recovery data.

1. Visualize reports by using on-demand [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) and Amazon Quick Sight. For standardized recovery reports, use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/) to create data marts.

1. (Optional) Build a configuration dashboard with microservices. Use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) to collect configuration changes and create what-if analyses.

1. Use public datasets from [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/) to enhance decision making.

## Further reading
<a name="propopt-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="propopt-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#propopt-history) | Reference architecture diagram first published. | April 16, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.