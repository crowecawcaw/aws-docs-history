

# Connectivity patterns for multi-cloud
<a name="rise-multi-cloud"></a>

In complex multi-cloud scenarios, your RISE with SAP environment might need to connect with on-premises systems, AWS-hosted workloads, SaaS solutions, and other cloud service providers.

Managing connectivity directly from AWS removes dependencies on on-premises networking infrastructure, improving the availability and resiliency of your overall landscape.

You can connect multi-cloud environments to RISE using either public or private connectivity.

![Connectivity patterns for multi-cloud to RISE.](http://docs.aws.amazon.com/sap/latest/general/images/rise-multi1.png)


## Public connectivity
<a name="_public_connectivity"></a>

Connectivity is routed over the internet. This pattern is typically used for connectivity from RISE with SAP to SaaS solutions that runs across multiple clouds. When building connectivity routed over the internet, consider the following:
+ ensure that all communication is encrypted
+ protect end-points by using AWS services, such as Elastic Load Balancers and AWS Shield
+ monitor endpoints using Amazon CloudWatch
+ ensure that traffic between two public IP addresses hosted on AWS is routed over the AWS network

## Private connectivity
<a name="_private_connectivity"></a>

The following options are available to establish private connectivity between cloud service providers:
+ Site-to-site VPN encrypted tunnel routed over public internet
+ Private interconnect using AWS Direct Connect in a managed infrastructure (use Azure ExpressRoute for Azure and Google Dedicated Interconnect for Google Cloud Platform)
+ Private interconnect using an AWS Direct Connect in a facility with a multi-cloud connectivity provider
+ Using AWS Interconnect Service to connect privately to other Cloud Providers (currently only Google Cloud)

With AWS Interconnect, you can establish direct private connectivity between AWS and other clouds (currently Google Cloud). You don’t need physical routers or on-premises routing, and AWS Interconnect includes built-in Media Access Control Security (MACsec) encryption.

For more information about supported regions, see [Region availability](https://docs.aws.amazon.com/interconnect/latest/userguide/interconnect-region-availability.html).

## Example use case 1: RISE on AWS to GCP BigQuery
<a name="example_use_case_1_rise_on_shared_aws_to_gcp_bigquery"></a>

If you run SAP S/4HANA on RISE with AWS and use Google Cloud BigQuery for analytics and machine learning, you can benefit from real-time data replication over a private, high-speed connection. This connection continuously streams data from the SAP application layer to the Google Cloud data warehouse without exposing it to the public internet.

After you establish AWS Interconnect and deliver traffic from AWS RISE into GCP, complete the remaining connectivity configuration on the Google Cloud side. This ensures that data stays within the Google Cloud network.

![Interconnect connecting RISE with SAP to Google Cloud BigQuery.](http://docs.aws.amazon.com/sap/latest/general/images/rise-interconnect-aws-rise-gcp-big-query.png)


## Example use case 2: RISE on GCP to AWS services
<a name="example_use_case_2_rise_on_gcp_to_shared_aws_services"></a>

If you run SAP S/4HANA on RISE on Google Cloud, you can use the AWS SDK for SAP ABAP to natively consume AWS services, such as Amazon Bedrock, Amazon Textract, and Amazon S3, directly from your ABAP application layer. With this integration, you can extend your core business processes with intelligent cloud services that drive automation, document processing, and scalable data management.

 AWS Interconnect connects the Google Cloud RISE environment to an AWS VPC. VPC endpoints (AWS PrivateLink) expose the required AWS services. All traffic between the SAP system on Google Cloud and AWS remains on private network infrastructure and does not traverse the public internet. This delivers low-latency, secure cross-cloud service consumption.

Complete the necessary routing configuration on the Google Cloud side to direct traffic from the RISE environment toward AWS Interconnect.

For more information, see [Custom VPC Endpoints in the AWS SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/custom-vpc-endpoints.html).

![Interconnect connecting RISE on Google Cloud to Amazon VPC endpoints for the SDK for SAP ABAP.](http://docs.aws.amazon.com/sap/latest/general/images/rise-interconnect-gcp-rise-aws-sdk.png)


 AWS Interconnect is a fully managed service that provides private, high-speed connectivity between AWS and other cloud providers. Unlike Site-to-Site VPN or self-managed AWS Direct Connect, it requires no colocation facilities, physical routers, cross-connects, or BGP peering configuration.

 AWS Interconnect provides the following benefits:
+ Media Access Control Security (MACsec) Layer 2 encryption by default.
+ Low latency and dedicated bandwidth.
+ Built-in redundancy through pre-provisioned capacity pools between cloud provider points of presence (PoPs).
+ Reduced operational complexity.
+ Performance and reliability that exceed internet-based VPN connections or self-managed AWS Direct Connect implementations.

The following table compares AWS Interconnect with traditional connectivity approaches.


| Criteria |  AWS Interconnect | Traditional (VPN / Self-managed Direct Connect) | 
| --- | --- | --- | 
| Setup | Fully managed, turnkey. No physical routers, cross-connects, or BGP peering to configure. | Requires ordering cross-connects, configuring routers, managing BGP sessions, and often contracting with colocation facilities. | 
| Encryption | MACsec (Layer 2) enabled by default, no manual tunnel or encryption setup needed. | VPN requires IPSec tunnel configuration; Direct Connect requires optional MACsec setup by the customer. | 
| Infrastructure |  AWS and the partner cloud pre-build large pools of capacity between PoPs, eliminating the need to maintain physical connections. | Customer must provision and maintain dedicated physical links or rely on colocation providers. | 
| Performance | Private, dedicated bandwidth with consistent low latency (no internet routing variability). | VPN traverses the public internet (variable latency). Self-managed Direct Connect offers similar performance but with operational overhead. | 
| Colocation requirement | None required. Connections are established directly between cloud providers. | Typically requires presence in a colocation facility where both providers have a PoP. | 
| Complexity | Minimal. A simplified provisioning process handles routing and physical connectivity. | Significant. Teams must manage equipment, contracts, and networking configurations across providers. | 
| Resilience | Built-in redundancy across pre-provisioned capacity pools. | Customer is responsible for designing redundancy (multiple connections, failover). | 

For more information, see [What is AWS Interconnect](https://docs.aws.amazon.com/interconnect/latest/userguide/what-is-interconnect.html).

The following diagram describes the factors to choose a multi-cloud connectivity method.

![Connectivity patterns for multi-cloud to RISE.](http://docs.aws.amazon.com/sap/latest/general/images/rise-multi2.png)


For more information, see [Designing private network connectivity between AWS and Microsoft Azure](https://aws.amazon.com/blogs/modernizing-with-aws/designing-private-network-connectivity-aws-azure/).