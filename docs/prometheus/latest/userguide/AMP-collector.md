# Ingest metrics with AWS managed collectors

A common use case for Amazon Managed Service for Prometheus is to monitor Kubernetes clusters managed by Amazon Elastic Kubernetes Service
(Amazon EKS). Kubernetes clusters, and many applications that run within Amazon EKS, automatically
export their metrics for Prometheus-compatible scrapers to access.

###### Note

Amazon EKS exposes API server metrics, `kube-controller-manager` metrics, and
`kube-scheduler` metrics in a cluster. Many other technologies and
applications running in Kubernetes environments provide Prometheus-compatible metrics.
For a list of well-documented exporters, see [Exporters and
integrations](https://prometheus.io/docs/instrumenting/exporters/ "https://prometheus.io/docs/instrumenting/exporters/") in the Prometheus documentation.

Amazon Managed Service for Prometheus provides a fully managed, agent less scraper, or _collector_,
that automatically discovers and pulls Prometheus-compatible metrics. You don't have to
manage, install, patch, or maintain agents or scrapers. An Amazon Managed Service for Prometheus collector provides
reliable, stable, highly available, automatically scaled collection of metrics for your
Amazon EKS cluster. Amazon Managed Service for Prometheus managed collectors work with Amazon EKS clusters, including EC2 and
Fargate.

An Amazon Managed Service for Prometheus collector creates an Elastic Network Interface (ENI) per subnet specified
when creating the scraper. The collector scrapes the metrics through these ENIs, and uses
`remote_write` to push the data to your Amazon Managed Service for Prometheus workspace using a VPC
endpoint. The scraped data never travels on the public internet.

The following topics provide more information about how to use an Amazon Managed Service for Prometheus collector in
your Amazon EKS cluster, and about the collected metrics.

###### Topics

- [Using an AWS managed collector](AMP-collector-how-to.md "AMP-collector-how-to.md")
- [What are Prometheus-compatible
  metrics?](prom-compatible-metrics.md "prom-compatible-metrics.md")
- [Monitor collectors with vended logs](AMP-collector-vended-logs.md "AMP-collector-vended-logs.md")
