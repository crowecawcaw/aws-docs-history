

# Search and Booking Metrics in Travel and Hospitality
<a name="search-booking-metrics"></a>

Publication date: **October 15, 2020 ([Diagram history](#sbm-history))**

With this architecture, you can build a content delivery network (CDN) platform for customer-facing websites to gather traffic data in real time. Understand search and purchase patterns through enriched analytics data. The solution presents real-time data in [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) and historical and aggregated data in [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html).

## Search and booking metrics diagram
<a name="sbm-diagram"></a>

![How to gather traffic data in real time by using Amazon CloudFront, Amazon Kinesis, and Amazon OpenSearch Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/search-booking-metrics/images/search-booking-metrics.png)


The following steps describe the architecture:

1. Website users search for availability on the website served through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/).

1. CloudFront sends the request log to an [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) Data Streams in real time.

1. Amazon Data Firehose extracts data from the Kinesis data stream for processing and delivery. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) maps the log properties to their respective tags such as IP, headers, and cookies.

1. Amazon Data Firehose delivers the transformed logs as JSON to an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake and an Amazon OpenSearch Service cluster.

1. An [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) crawler runs on a schedule, deriving a schema from the data. It updates a Data Catalog in [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. As new purchases happen, the cookie header or session ID value and purchase information flow to the data lake and Amazon OpenSearch Service cluster.

1. Data analysts visualize historical and aggregated data through Amazon Quick Sight. They view real-time data in Amazon OpenSearch Service.

## Further reading
<a name="sbm-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="sbm-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sbm-history) | Reference architecture diagram first published. | October 15, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.