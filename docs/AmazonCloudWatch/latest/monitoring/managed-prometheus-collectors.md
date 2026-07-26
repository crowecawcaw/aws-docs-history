# Amazon CloudWatch managed Prometheus collectors

Amazon CloudWatch managed Prometheus collectors provides a fully managed, agentless scraper, or
collector, that automatically discovers and pulls Prometheus-compatible metrics. With
Amazon CloudWatch managed Prometheus collectors, you eliminate the operational overhead of running
and scaling your own metric collection infrastructure. The collectors automatically discover
targets in your VPC, scrape Prometheus-compatible metrics, and deliver them to CloudWatch. You
don't have to manage, install, patch, or maintain agents, collectors or scrapers for
Prometheus metrics. Managed collectors automatically scale to provide highly available,
reliable metric collection for your AWS infrastructure.

A managed collector creates an Elastic Network Interface (ENI) for each subnet that you
specify when you create the scraper. The collector scrapes metrics through these ENIs using
OpenTelemetry Protocol (OTLP). It delivers the metrics to your CloudWatch dataset through a VPC
endpoint. The scraped data never travels on the public internet. You can query metrics in
CloudWatch with PromQL (Prometheus Query Language) for flexible and scalable analytics.

###### Note

Scraping metrics might incur VPC data transfer charges between the collector and your
targets. To reduce this network transfer cost, configure your Prometheus
`/metrics` endpoint to compress responses (for example, with gzip).
Compression lowers the volume of data that the collector transfers across the network.
It does not change the number of metrics that CloudWatch ingests.

We charge for Prometheus collectors by the hour, and CloudWatch OpenTelemetry metric ingestion pricing applies. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Integrate Amazon MSK](managed-prometheus-collectors-msk-setup.md "managed-prometheus-collectors-msk-setup.md")
- [Integrate Amazon EKS](managed-prometheus-collectors-eks-setup.md "managed-prometheus-collectors-eks-setup.md")
- [VPC-connected managed collector](managed-prometheus-collectors-vpc-setup.md "managed-prometheus-collectors-vpc-setup.md")
- [Scraper configuration](managed-prometheus-collectors-scraper-configuration.md "managed-prometheus-collectors-scraper-configuration.md")
- [Monitor collectors](managed-prometheus-collectors-monitor.md "managed-prometheus-collectors-monitor.md")
