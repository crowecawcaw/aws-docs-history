

# What is Amazon OpenSearch Service?
<a name="what-is"></a>

Amazon OpenSearch Service is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters in the AWS Cloud. An OpenSearch Service domain is synonymous with an OpenSearch cluster. Domains are clusters with the settings, instance types, instance counts, and storage resources that you specify. Amazon OpenSearch Service supports OpenSearch and legacy Elasticsearch OSS (up to 7.10, the final open source version of the software). When you create a domain, you have the option of which search engine to use.

***OpenSearch*** is a fully open-source search and analytics engine for use cases such as log analytics, real-time application monitoring, and clickstream analysis. For more information, see the [OpenSearch documentation](https://opensearch.org/docs/).

***Amazon OpenSearch Service*** provisions all the resources for your OpenSearch cluster and launches it. It also automatically detects and replaces failed OpenSearch Service nodes, reducing the overhead associated with self-managed infrastructures. You can scale your cluster with a single API call or a few clicks in the console.

![Data sources flow into OpenSearch Service , which outputs to monitoring, SIEM, and search uses.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/whatis.png)


To get started using OpenSearch Service, you create an OpenSearch Service *domain*, which is equivalent to an OpenSearch *cluster*. Each EC2 instance in the cluster acts as one OpenSearch Service node.

You can use the OpenSearch Service console to set up and configure a domain in minutes. If you prefer programmatic access, you can use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/), the [AWS SDKs](http://aws.amazon.com/code), or [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opensearch_domain).

## Features of Amazon OpenSearch Service
<a name="what-is-features"></a>

OpenSearch Service includes the following features:

**Scale**
+ Numerous configurations of CPU, memory, and storage capacity known as *instance types*, including cost-effective Graviton instances
+ Supports up to 1002 data nodes
+ Up to 25 PB of attached storage
+ Cost-effective [UltraWarm](ultrawarm.md) and [cold storage](cold-storage.md) for read-only data

**Security**
+ AWS Identity and Access Management (IAM) access control
+ Easy integration with Amazon VPC and VPC security groups
+ Encryption of data at rest and node-to-node encryption
+ Amazon Cognito, HTTP basic, or SAML authentication for OpenSearch Dashboards
+ Index-level, document-level, and field-level security
+ Audit logs
+ Dashboards multi-tenancy

**Stability**
+ Numerous geographical locations for your resources, known as *Regions* and *Availability Zones*
+ Node allocation across two or three Availability Zones in the same AWS Region, known as *Multi-AZ*
+ Dedicated master nodes to offload cluster management tasks
+ Automated snapshots to back up and restore OpenSearch Service domains

**Flexibility**
+ SQL support for integration with business intelligence (BI) applications
+ Custom packages to improve search results

**Integration with popular services**
+ Data visualization using OpenSearch Dashboards
+ Integration with Amazon CloudWatch for monitoring OpenSearch Service domain metrics and setting alarms
+ Integration with AWS CloudTrail for auditing configuration API calls to OpenSearch Service domains
+ Integration with Amazon S3, Amazon Kinesis, and Amazon DynamoDB for loading streaming data into OpenSearch Service
+ Alerts from Amazon SNS when your data exceeds certain thresholds

## When to use OpenSearch versus Amazon OpenSearch Service
<a name="whatis-whentouse"></a>

Use the following table to help you decide whether provisioned Amazon OpenSearch Service or self-managed OpenSearch is the correct choice for you.


| OpenSearch | Amazon OpenSearch Service | 
| --- | --- | 
|  +  Your organization is willing to, and has people with the correct skills to, manually monitor and maintain self-provisioned clusters. <br />+  You want full, compile-level control of your code. <br />+  Your organization prefers, or uniquely uses, open source software. <br />+  You have a multi-cloud strategy, requiring technologies that aren't vendor-specific. <br />+  Your team is capable of addressing any critical production issues. <br />+  You want the flexibility to use, modify, and extend the product however you want. <br />+  You want immediate access to new features as soon as they’re released.   |  +  You don’t want to manually manage, monitor, and maintain your infrastructure. <br />+  You want simple ways to manage growing analytics costs by layering your data across storage tiers, taking advantage of the durability and low cost of Amazon S3. <br />+  You want to take advantage of integrations with other AWS services such as DynamoDB, Amazon DocumentDB (with MongoDB compatibility), IAM, CloudWatch, and CloudFormation. <br />+  You want easy access to assistance from Support for preventative maintenance and during production issues. <br />+  You want to take advantage of features such as self-healing, proactive maintenance, resiliency, and backups.   | 

## Supported versions of Elasticsearch and OpenSearch
<a name="choosing-version"></a>

OpenSearch Service supports the following versions of **OpenSearch**:
+ 3.5, 3.3, 3.1, 2.19, 2.17, 2.15, 2.13, 2.11, 2.9, 2.7, 2.5, 2.3, 1.3, 1.2, 1.1, and 1.0

OpenSearch Service supports the following versions of legacy **Elasticsearch**:
+ 7.10, 7.9, 7.8, 7.7, 7.4, 7.1, 6.8, 6.7, 6.5, 6.4, 6.3, 6.2, 6.0, 5.6, 5.5, 5.3, 5.1, 2.3, and 1.5

We recommend upgrading to the latest available OpenSearch version to get the best use of OpenSearch Service, in terms of price-performance, feature richness, and security improvements. For information about upgrade paths, breaking changes, and version-specific considerations, see [Upgrading Amazon OpenSearch Service domains](version-migration.md).

## Standard and extended support
<a name="end-of-support"></a>

AWS provides bug fixes and security updates for versions under standard support. For versions in extended support, AWS offers critical security fixes for at least 12 months after standard support ends. Extended support charges apply automatically when a domain runs a version that is no longer under standard support. To avoid these charges, upgrade to a supported version. For running version on Extended Support, you will either be charged, equal to your instance costs (storage costs are not affected), or a flat fee per Normalized Instance Hour (NIH), in addition to the standard instance cost. NIH is computed as a factor of the instance size (e.g. medium, large), and number of instance hours. For versions where the originally published extended support date has passed, and there has been an additional extension to the end of support date, extended support fee will be equal to your instance cost (in addition to the instance cost) and storage costs are not affected. See [Calculating extended support charges](#calculating-charges) below for details and examples.

The following tables show the end of support schedule for OpenSearch and legacy Elasticsearch versions.

**Elasticsearch versions**


| Software Version | End of Standard Support | Original End of Extended Support | Updated End of Extended Support | 
| --- | --- | --- | --- | 
| Elasticsearch versions 1.5 and 2.3 | November 7, 2025 | November 7, 2026 | November 7, 2027 | 
| Elasticsearch versions 5.1 to 5.5 | November 7, 2025 | November 7, 2026 | November 7, 2027 | 
| Elasticsearch version 5.6 | November 7, 2025 | November 7, 2028 | No change | 
| Elasticsearch versions 6.0 to 6.7 | November 7, 2025 | November 7, 2026 | November 7, 2027 | 
| Elasticsearch version 6.8 | November 7, 2027 | Not announced | November 7, 2030 | 
| Elasticsearch versions 7.1 to 7.8 | November 7, 2025 | November 7, 2026 | November 7, 2027 | 
| Elasticsearch version 7.9 | November 7, 2027 | Not announced | November 7, 2028 | 
| Elasticsearch version 7.10 | November 7, 2027 | Not announced | November 7, 2030 | 

**OpenSearch versions**


| Software Version | End of Standard Support | Original End of Extended Support | Updated End of Extended Support | 
| --- | --- | --- | --- | 
| OpenSearch versions 1.0 to 1.2 | November 7, 2025 | November 7, 2026 | November 7, 2027 | 
| OpenSearch version 1.3 | November 7, 2027 | Not announced | November 7, 2030 | 
| OpenSearch versions 2.3 to 2.9 | November 7, 2025 | November 7, 2026 | November 7, 2027 | 
| OpenSearch version 2.11 to 2.17 | November 7, 2027 | Not announced | November 7, 2028 | 
| OpenSearch version 2.19 | November 7, 2027 | Not announced | November 7, 2030 | 
| OpenSearch version 3.1 and above | Not announced | Not announced | Not applicable | 

For more information about extended support charges, see the [pricing page](https://aws.amazon.com/opensearch-service/pricing/#Extended_support_costs). For general information about extended support, see the [Extended Support FAQ](https://aws.amazon.com/opensearch-service/faqs/#awt-content-topics#ams#c111#extended-support-9).

## Calculating extended support charges
<a name="calculating-charges"></a>

For version you are running on Extended Support, you will be charged a **flat fee per Normalized Instance Hour (NIH)**, in addition to the standard instance cost. NIH is computed as a factor of the instance size (e.g. medium, large), and number of instance hours. For versions where the originally published extended support date has passed, and there has been an additional extension to the end of support date, extended support fee will be equal to your instance cost (in addition to the instance cost) and storage costs are not affected. Please see below for Extended Support pricing.

**Extended Support charges for Elasticsearch versions 1.5, 2.3, 5.1–5.5, 6.0–6.7, 7.1–7.8, OpenSearch versions 1.0–1.2, and OpenSearch versions 2.3–2.9 (from November 7, 2026):** For these versions, the Extended Support charges are equal to your instance pricing for the extension period. Storage costs are not affected. This extended period gives you additional time to plan and complete your upgrades to the latest OpenSearch versions. **Example:** If you are running an m7g.medium.search instance priced at $0.068/hr (on-demand) in US East (N. Virginia) for 24 hours, your standard instance cost is $1.632/day ($0.068×24). The Extended Support surcharge for the extension period will be equal to your instance cost ($1.632/day), effectively doubling your instance pricing to \~$3.264/day. Storage costs remain unchanged.

**For Elasticsearch version 5.6 (till November 7, 2028)** you will be charged the standard Extended Support rate of $0.0065 per Normalized Instance Hour (NIH) in US East (N. Virginia). See the [pricing page](https://aws.amazon.com/opensearch-service/pricing/#Extended_support_costs) for exact pricing by Region.

**Extended Support charges for Elasticsearch versions 6.8, 7.9, and 7.10, OpenSearch version 1.3, and OpenSearch versions 2.11–2.19 (from November 2027):** For these versions, you will be charged the standard Extended Support rate of $0.0065 per Normalized Instance Hour (NIH) in US East (N. Virginia). See the [pricing page](https://aws.amazon.com/opensearch-service/pricing/#Extended_support_costs) for rates in other Regions. **Example:** If you are running an m7g.medium.search instance for 24 hours in US East (N. Virginia), priced at $0.068/hr (on-demand), you will pay $1.632/day ($0.068×24) as the standard instance cost. The Extended Support charge is $0.0065 × 24 (instance hours) × 2 (normalization factor for medium) = $0.312/day. Total = $1.944/day ($1.632 \+ $0.312, excluding storage cost).

See the [pricing page](https://aws.amazon.com/opensearch-service/pricing/#Extended_support_costs) for exact pricing by Region.

The table below shows the normalization factor for various instance sizes in OpenSearch Service.


| Instance size | Normalization Factor | 
| --- | --- | 
| nano | 0.25 | 
| micro | 0.5 | 
| small | 1 | 
| medium | 2 | 
| large | 4 | 
| xlarge | 8 | 
| 2xlarge | 16 | 
| 4xlarge | 32 | 
| 8xlarge | 64 | 
| 9xlarge | 72 | 
| 10xlarge | 80 | 
| 12xlarge | 96 | 
| 16xlarge | 128 | 
| 18xlarge | 144 | 
| 24xlarge | 192 | 
| 32xlarge | 256 | 

## Pricing for Amazon OpenSearch Service
<a name="pricing"></a>

For OpenSearch Service, you pay for each hour of use of an EC2 instance and for the cumulative size of any EBS storage volumes attached to your instances. [Standard AWS data transfer charges](https://aws.amazon.com/ec2/pricing/) also apply.

However, some notable data transfer exceptions exist. If a domain uses [multiple Availability Zones](managedomains-multiaz.md), OpenSearch Service does not bill for traffic between the Availability Zones. Significant data transfer occurs within a domain during shard allocation and rebalancing. OpenSearch Service neither meters nor bills for this traffic. Similarly, OpenSearch Service does not bill for data transfer between [UltraWarm](ultrawarm.md)/[cold](cold-storage.md) nodes and Amazon S3.

For full pricing details, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/elasticsearch-service/pricing/). For information about charges incurred during configuration changes, see [Charges for configuration changes](managedomains-configuration-changes.md#managedomains-config-charges).

## Understanding billing and usage reports
<a name="billing-usage-reports"></a>

Amazon OpenSearch Service usage appears in your AWS billing reports with specific usage type codes. Understanding these codes helps you analyze costs across deployment types.

**Usage type codes**
+ `ESInstance` – Instance hours for managed OpenSearch Service domains.
+ `EBS` – EBS storage volumes attached to domain instances.
+ `ServerlessOCU` – OpenSearch Compute Units consumed by OpenSearch Serverless collections.
+ `IngestionOCU` – OpenSearch Compute Units consumed by OpenSearch Ingestion pipelines.

**Region abbreviations in usage type codes**

Usage type codes are prefixed with a region abbreviation. The following table shows common examples:


| Abbreviation | Region | 
| --- | --- | 
| USE1 | US East (N. Virginia) | 
| USE2 | US East (Ohio) | 
| USW1 | US West (N. California) | 
| USW2 | US West (Oregon) | 
| EUW1 | Europe (Ireland) | 
| EUC1 | Europe (Frankfurt) | 
| APS1 | Asia Pacific (Singapore) | 
| APS2 | Asia Pacific (Sydney) | 
| APN1 | Asia Pacific (Tokyo) | 

For example, a usage type of `USE1-ESInstance:r6g.large.search` represents an `r6g.large.search` instance hour in US East (N. Virginia). For full details on billing, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/elasticsearch-service/pricing/).

## Related services
<a name="related-services"></a>

OpenSearch Service commonly is used with the following services:

[Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)  
OpenSearch Service domains automatically send metrics to CloudWatch so that you can monitor domain health and performance. For more information, see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](managedomains-cloudwatchmetrics.md).  
CloudWatch Logs can also go the other direction. You might configure CloudWatch Logs to stream data to OpenSearch Service for analysis. To learn more, see [Loading streaming data from Amazon CloudWatch](integrations-cloudwatch.md).

[AWS CloudTrail](https://docs.aws.amazon.com/cloudtrail/)  
Use AWS CloudTrail to get a history of the OpenSearch Service configuration API calls and related events for your account. For more information, see [Monitoring Amazon OpenSearch Service API calls with AWS CloudTrail](managedomains-cloudtrailauditing.md).

[Amazon Kinesis](https://docs.aws.amazon.com/kinesis/)  
Kinesis is a managed service for real-time processing of streaming data at a massive scale. For more information, see [Loading streaming data from Amazon Kinesis Data Streams](integrations-kinesis.md) and [Loading streaming data from Amazon Data Firehose](integrations-fh.md).

[Amazon S3](https://docs.aws.amazon.com/s3/)  
Amazon Simple Storage Service (Amazon S3) provides storage for the internet. This guide provides Lambda sample code for integration with Amazon S3. For more information, see [Loading streaming data from Amazon S3](integrations-s3-lambda.md).

[AWS IAM](https://aws.amazon.com/iam/)  
AWS Identity and Access Management (IAM) is a web service that you can use to manage access to your OpenSearch Service domains. For more information, see [Identity and Access Management in Amazon OpenSearch Service](ac.md).

[AWS Lambda](https://docs.aws.amazon.com/lambda/)  
AWS Lambda is a compute service that lets you run code without provisioning or managing servers. This guide provides Lambda sample code to stream data from DynamoDB, Amazon S3, and Kinesis. For more information, see [Loading streaming data into Amazon OpenSearch Service](integrations.md).

[Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/)  
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. To learn more about streaming data to OpenSearch Service, see [Loading streaming data from Amazon DynamoDB](integrations-dynamodb.md).

[Amazon Quick](https://docs.aws.amazon.com/quicksight/)  
You can visualize data from OpenSearch Service using Quick dashboards. For more information, see [Using Amazon OpenSearch Service with Quick](https://docs.aws.amazon.com/quicksight/latest/user/connecting-to-es.html) in the *Quick User Guide*.

**Note**  
OpenSearch includes certain Apache-licensed Elasticsearch code from Elasticsearch B.V. and other source code. Elasticsearch B.V. is not the source of that other source code. ELASTICSEARCH is a registered trademark of Elasticsearch B.V.