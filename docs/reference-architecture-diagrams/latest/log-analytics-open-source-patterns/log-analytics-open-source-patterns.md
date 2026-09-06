

# Log Analytics with Open Source Patterns
<a name="log-analytics-open-source-patterns"></a>

Publication date: **December 13, 2022 ([Diagram history](#diagram-history))**

This architecture uses FluentBit and Data Prepper to collect, aggregate, and transform logs into OpenSearch.

## Log Analytics with Open Source Patterns
<a name="diagram1"></a>

![Architecture diagram showing log analytics with open source patterns by using FluentBit and Data Prepper.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/log-analytics-open-source-patterns/images/log-analytics-open-source-patterns.png)


1. The application, container system, and associated services generate logs. These include Docker containers, Kubernetes pods, [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instances, Elastic Load Balancer logs, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and relational database systems.

1. FluentBit, a popular Apache-licensed log forwarder, reads the log files and forwards them to Data Prepper over HTTP.

1. Data Prepper is a server-side data collector. It filters, enriches, transforms, normalizes, and aggregates data for downstream analytics. Data Prepper receives the logs, buffers them, then optionally structures the data through a grok prepper.

1. Data Prepper creates the service map and assembles the traces into trace groups. It then sends the log lines, formatted for easy searching and analysis, to [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).

1. The user logs into OpenSearch Dashboards (or another open source visualization tool like Grafana) to perform interactive log analytics.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [ product page](https://aws.amazon.com/opensearch-service/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | December 13, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.