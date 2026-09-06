

# Securely Access TiDB Using AWS PrivateLink
<a name="tidb-privatelink"></a>

Publication date: **February 22, 2023 ([Diagram history](#diagram-history))**

TiDB is an open-source MySQL-compatible database that supports hybrid transactional and analytical processing (HTAP). TiDB Cloud supports highly secure and unidirectional access to the TiDB Cloud service hosted in an Amazon VPC by using [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). PingCAP sets up the AWS PrivateLink service for TiDB Cloud.

## Securely Access TiDB Using AWS PrivateLink
<a name="diagram1"></a>

![Architecture diagram showing secure access to TiDB Cloud using AWS PrivateLink with Amazon VPC interface endpoints.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/tidb-privatelink/images/tidb-privatelink.png)


The following steps describe the architecture:

1. Create an Amazon VPC interface endpoint to the TiDB Cloud AWS PrivateLink endpoint service.

1. Powered by AWS PrivateLink, the endpoint connection is secure and private, and does not expose data to the public internet. The AWS PrivateLink connection also supports a secure connection between VPCs with overlapping Classless Inter-Domain Routing (CIDR).

1. Amazon EC2 customer instances securely connect to the TiDB Cloud service hosted in the provider Amazon VPC through VPC endpoints, without traffic traversing the public internet. With private DNS enabled, consumers use the same public DNS when connecting over AWS PrivateLink.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.