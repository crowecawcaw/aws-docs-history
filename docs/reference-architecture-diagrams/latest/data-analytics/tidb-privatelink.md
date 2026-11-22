

# Securely access TiDB using AWS PrivateLink

Publication date: **February 22, 2023 ([Diagram history](diagram-history.md))**

TiDB is an open-source MySQL-compatible database that supports hybrid transactional and analytical processing (HTAP). TiDB Cloud supports highly secure and unidirectional access to the TiDB Cloud service hosted in an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) by using [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/). PingCAP sets up the AWS PrivateLink service for TiDB Cloud.

## Securely access TiDB using AWS PrivateLink diagram
<a name="tidb-privatelink-diagram1"></a>

![Architecture diagram showing secure access to TiDB Cloud using AWS PrivateLink with Amazon VPC interface endpoints.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/tidb-privatelink.png)


The following steps describe the architecture:

1. Create an Amazon VPC interface endpoint to the TiDB Cloud AWS PrivateLink endpoint service.

1. Powered by AWS PrivateLink, the endpoint connection is secure and private, and does not expose data to the public internet. The AWS PrivateLink connection also supports a secure connection between VPCs with overlapping Classless Inter-Domain Routing (CIDR).

1. Amazon EC2 customer instances securely connect to the TiDB Cloud service hosted in the provider Amazon VPC through VPC endpoints, without traffic traversing the public internet. With private DNS enabled, consumers use the same public DNS when connecting over AWS PrivateLink.

## Further reading
<a name="tidb-privatelink-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)