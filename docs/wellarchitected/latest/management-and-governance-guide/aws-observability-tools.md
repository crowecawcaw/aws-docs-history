# AWS observability tools

The following AWS services can be used to help you meet the
prescribed benefits of the M&G Guide:

[AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") provides event history of your AWS API activity,
including actions taken through the AWS Management Console, AWS
SDKs, command line tools, and other AWS services that you
specifically enable. By default, AWS Control Tower uses AWS CloudTrail where it is enabled as a multi-account guardrail
control, and stores control plane logs in a centralized account.
Use the central account to store and analyze all trails.

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") is a monitoring and observability service built
for DevOps engineers, developers, site reliability engineers, and
IT managers. CloudWatch provides you with data and actionable
insights to monitor your applications, respond to system-wide
performance changes, optimize resource utilization, and get a
unified view of operational health. CloudWatch collects monitoring
and operational data as logs, metrics, and events, providing you
with a unified view of AWS resources, applications, and services
that run on AWS and on-premises servers. CloudWatch should be used
to integrate AWS service, resource, and application logs.

With [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/"), you can understand how your application and its
underlying services are performing to identify and troubleshoot
the root cause of performance issues and errors. X-Ray provides an
end-to-end view of requests as they travel through your
application, and shows a map of your application’s underlying
components. You can use X-Ray to analyze both applications in
development and in production, from simple three-tier applications
to complex microservices applications consisting of thousands of
services.

To visualize, query, and correlate your metrics, logs, and traces
at scale, and to provide a deeper analysis of your observability
data, we recommend [Amazon Managed Grafana](https://aws.amazon.com/grafana/ "https://aws.amazon.com/grafana/"). Developed in
collaboration with Grafana Labs, Amazon Managed Grafana manages
the provisioning, setup, scaling, and maintenance of Grafana
servers, decreasing the need for you to manage the underlying
infrastructure. Based on open source Grafana with enhanced
features such as single sign-on support, Amazon Managed Grafana
enables you to query, visualize, alert on, and understand your
observability metrics, logs, and traces no matter where the data
is stored, such as querying container metrics stored in
[Amazon
Managed Service for Prometheus](https://aws.amazon.com/prometheus/ "https://aws.amazon.com/prometheus/").

Amazon Managed Service for Prometheus is a fully managed,
Prometheus-compatible service that enables you to securely ingest,
store, and query metrics from container environments. Amazon
Managed Service for Prometheus scales on demand, collecting and
accessing performance and operational data from container
workloads on AWS and on premises. With Amazon Managed Service for
Prometheus, you can use the open source Prometheus query language
(PromQL) to monitor the performance of containerized workloads
without having to manage the underlying infrastructure. Amazon
Managed Service for Prometheus automatically scales as your
workloads grow or shrink, and uses AWS security services to enable
fast and secure access to data. You can use Amazon Managed Service
for Prometheus to collect and query metrics from AWS container
services including Amazon Elastic Kubernetes Service (EKS) and
Amazon Elastic Container Service (Amazon ECS), via AWS Distro for
OpenTelemetry or Prometheus servers as the collection agents.

[Amazon
OpenSearch Service](https://aws.amazon.com/opensearch-service/the-elk-stack/what-is-opensearch/ "https://aws.amazon.com/opensearch-service/the-elk-stack/what-is-opensearch/") (successor to Amazon Elasticsearch Service) is a distributed,
open-source search and analytics suite used for a broad set of use cases, such as real-time
application monitoring, log analytics, and website search. Amazon OpenSearch Service
provides a highly scalable system for providing fast access and response to large volumes of
data with an integrated visualization tool, OpenSearch Dashboards, that makes it easy for
users to explore their data. Like Elasticsearch and Apache Solr, OpenSearch Service is
powered by the Apache Lucene search library. OpenSearch Service and OpenSearch Dashboards
were originally derived from Elasticsearch 7.10.2 and Kibana 7.10.2.

If you would like support implementing this guidance, or assisting
you with building the foundational elements prescribed by the
M&G Guide, we recommend you review the offerings provided by
[AWS Professional Services](https://aws.amazon.com/professional-services/ "https://aws.amazon.com/professional-services/") or the AWS Partners in the
[Built
on Control Tower program](https://aws.amazon.com/controltower/partners/ "https://aws.amazon.com/controltower/partners/").

If you are seeking help to operate your workloads in AWS following
this guidance,
[AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/") can augment your operational
capabilities as a short-term accelerator or a long-term solution,
letting you focus on transforming your applications and businesses
in the cloud.
