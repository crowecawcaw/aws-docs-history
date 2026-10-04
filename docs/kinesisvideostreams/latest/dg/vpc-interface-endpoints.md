

# Access Amazon Kinesis Video Streams using AWS PrivateLink
<a name="vpc-interface-endpoints"></a>

You can access Amazon Kinesis Video Streams privately from your VPC using an interface VPC endpoint powered by AWS PrivateLink. With this endpoint, traffic between your VPC and Kinesis Video Streams does not traverse the public internet. The endpoint provides private access to the Kinesis Video Streams control plane and to the video ingestion and playback data planes.

**Contents**
+ [What is supported](#vpce-pl-supported)
+ [Prerequisites](#vpce-pl-prereqs)
+ [Finding the endpoint service name for your Region](#vpce-pl-finding)
+ [Creating an interface VPC endpoint for Kinesis Video Streams](#vpce-pl-creating)
+ [Private DNS](#vpce-pl-private-dns)
+ [Controlling access to Kinesis Video Streams over VPC endpoints](#vpce-pl-control-access)
+ [Quotas and throttling](#vpce-pl-quotas)
+ [Best practices](#vpce-pl-best-practices)
+ [Known limitations](#vpce-pl-limitations)
+ [Availability](#vpce-pl-availability)

## What is supported
<a name="vpce-pl-supported"></a>

The interface VPC endpoint supports the following:
+ Control plane – The [Kinesis Video Streams API](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_Operations_Amazon_Kinesis_Video_Streams.html) operations.
+ Ingestion and retrieval (data plane) – The [Kinesis Video Streams Media API](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_Operations_Amazon_Kinesis_Video_Streams_Media.html) operations (`PutMedia`, `GetMedia`).
+ Playback (data plane) – The [Kinesis Video Streams Archived Media API](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_Operations_Amazon_Kinesis_Video_Streams_Archived_Media.html) operations (`GetMediaForFragmentList` and the other retrieval operations).

**Important**  
AWS PrivateLink is not supported for any Kinesis Video Streams WebRTC component, including [signaling, STUN, TURN, media, and control plane](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-how-it-works.html). Do not route any Kinesis Video Streams WebRTC traffic through the Kinesis Video Streams interface endpoint.

## Prerequisites
<a name="vpce-pl-prereqs"></a>

Before you create an interface VPC endpoint for Kinesis Video Streams, make sure that you have the following:
+ A VPC.
+ Subnets in each Availability Zone that you want to use.
+ A security group that allows inbound HTTPS (443) from your clients.
+ The **Enable DNS hostnames** and **Enable DNS support** attributes enabled on the VPC (required to use a private DNS name). For more information, see [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html) in the AWS PrivateLink Guide.

## Finding the endpoint service name for your Region
<a name="vpce-pl-finding"></a>

The endpoint service name and private DNS name follow these patterns:
+ VPC endpoint service name – `com.amazonaws.{{region}}.kinesisvideo` (all Regions, all partitions)
+ Private DNS name – Varies by partition. For the private DNS name in each partition, see the following table.

The recommended way to find the exact service name, private DNS name, and Availability Zones for a Region is to run the following command. To run this command, you need permission to call `ec2:DescribeVpcEndpointServices`. This example uses the `us-east-1` Region. Replace it with your Region.

```
aws ec2 describe-vpc-endpoint-services \
    --filters Name=service-name,Values=com.amazonaws.us-east-1.kinesisvideo \
    --region us-east-1 \
    --query 'ServiceDetails[*].{ServiceName:ServiceName,PrivateDnsName:PrivateDnsName,AvailabilityZones:AvailabilityZones}'
```

The output is similar to the following.

```
[
    {
        "ServiceName": "com.amazonaws.us-east-1.kinesisvideo",
        "PrivateDnsName": "*.kinesisvideo.us-east-1.amazonaws.com",
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1b",
            "us-east-1c",
            "us-east-1d",
            "us-east-1f"
        ]
    }
]
```

For more information, see [describe-vpc-endpoint-services](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoint-services.html) in the AWS Command Line Interface Command Reference.

The endpoint service name is the same in every partition. The private DNS name is not—it follows the Region's own service endpoint domain.


**Private DNS name by partition**  

| Partition | Private DNS name | 
| --- | --- | 
| AWS Regions | \*.kinesisvideo.{{region}}.amazonaws.com | 
| AWS China Regions | \*.kinesisvideo.cn-north-1.amazonaws.com.cn | 
| AWS GovCloud (US) Regions | \*.kinesisvideo-fips.{{region}}.amazonaws.com | 

**Note**  
In AWS GovCloud (US) Regions, only the private DNS name contains `-fips`. The endpoint service name is still `com.amazonaws.{{region}}.kinesisvideo`—there is no separate `kinesisvideo-fips` endpoint service.

## Creating an interface VPC endpoint for Kinesis Video Streams
<a name="vpce-pl-creating"></a>

You create an interface VPC endpoint for Kinesis Video Streams the same way you create one for other AWS services. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the AWS PrivateLink Guide.

To create an interface VPC endpoint for Kinesis Video Streams by using the Amazon VPC console, do the following:

1. Open the Amazon VPC console. Under **Virtual private cloud**, choose **Endpoints**, and then choose **Create endpoint**.

1. (Optional) Under **Endpoint settings**, enter a **Name tag**.

1. For **Type**, choose **AWS services** (this is the default).

1. In the service search box, enter `kinesisvideo`, and then select the Kinesis Video Streams service for your Region.

1. For **VPC**, choose your VPC.

1. For **Subnets**, select an Availability Zone and then a subnet in that Availability Zone. Repeat for each Availability Zone that you want to use.

1. For **Security groups**, choose a security group that allows inbound HTTPS (443) from your clients.

1. Under **Additional settings**, for **Private DNS name**, keep **Enable private DNS name** selected. Private DNS is the only supported way to reach Kinesis Video Streams through the endpoint, so clearing it means no traffic in the VPC uses the endpoint at all. Clear it only to return traffic to the public path, or if the VPC contains Kinesis Video Streams WebRTC workloads. For more information, see [Private DNS](#vpce-pl-private-dns).

1. For **Policy**, choose **Full access** (the default), or choose **Custom** to restrict access. For more information, see [Controlling access to Kinesis Video Streams over VPC endpoints](#vpce-pl-control-access).

1. Choose **Create endpoint**.

## Private DNS
<a name="vpce-pl-private-dns"></a>

**Enable private DNS name** is selected by default when you create the endpoint. Selecting it associates a private hosted zone for your Region's private DNS name with the VPC, so requests from the VPC resolve to the endpoint's private IP addresses. This is what makes traffic use the endpoint. For your Region's private DNS name, see [Finding the endpoint service name for your Region](#vpce-pl-finding).

If you clear it, requests to the hostname resolve to the public IP addresses for Kinesis Video Streams, and traffic no longer uses the interface endpoint. Clients in the VPC must then be able to reach the public endpoint over the internet. For more information about giving your VPC internet access, see [Connect your VPC to other networks](https://docs.aws.amazon.com/vpc/latest/userguide/extend-intro.html) in the Amazon VPC User Guide.

**Important**  
When **Enable private DNS name** is selected, requests to your Region's private DNS name from anywhere in the VPC resolve to the interface endpoint. The endpoint does not serve WebRTC, so any WebRTC traffic in the VPC fails.

To return traffic to the public internet, modify the endpoint and clear the **Enable private DNS name** check box. The hostname then resolves to the public IP addresses for Kinesis Video Streams again. Because this is a DNS change, clients use the public path after their next DNS resolution.

**Note**  
To use AWS PrivateLink with Kinesis Video Streams, you must keep **Enable private DNS name** selected. Private DNS is required to reach Kinesis Video Streams through the interface endpoint. Using the VPC endpoint's public DNS names to reach Kinesis Video Streams results in errors. Those hostnames appear in the Amazon VPC console and resolve to the endpoint's private IP addresses, but requests sent to them are not served. Always use the standard Kinesis Video Streams hostname for your Region with private DNS enabled.

**Note**  
In AWS GovCloud (US) Regions, there is no non-FIPS private DNS name for Kinesis Video Streams. The FIPS hostname shown in the partition table (see [Finding the endpoint service name for your Region](#vpce-pl-finding)) is the only private DNS name that resolves within the VPC.

For more information, see [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html) in the AWS PrivateLink Guide.

## Controlling access to Kinesis Video Streams over VPC endpoints
<a name="vpce-pl-control-access"></a>

By default, the endpoint policy allows **Full access**. To restrict the actions, principals, and stream resources allowed through the endpoint, choose **Custom** and attach a VPC endpoint policy. An endpoint policy does not replace IAM identity-based policies; all applicable policies must allow the call.

For more information about restricting endpoint access, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the AWS PrivateLink Guide.

## Quotas and throttling
<a name="vpce-pl-quotas"></a>

Traffic through a VPC endpoint is subject to additional throttling. This quota is separate from the quota that applies to traffic over the public internet. All other Kinesis Video Streams quotas continue to apply to endpoint traffic. For more information, see [Amazon Kinesis Video Streams service quotas](limits.md).

**Request rate (transactions per second)** – Applied per AWS account, per VPC endpoint, across the ingestion and playback APIs. Requests above the limit are throttled, and the operation returns a `ClientLimitExceededException`. Use exponential backoff and retry.


**Request rate quota**  

| Quota | Value | 
| --- | --- | 
| Requests per second, per account, per VPC endpoint | 500 | 

**Note**  
This quota can differ from the corresponding quota for traffic over the public internet. To request a quota increase, contact AWS Support.

## Best practices
<a name="vpce-pl-best-practices"></a>

We recommend the following best practices:
+ Migrate traffic gradually. Create the endpoint in one VPC, or in a single Region, verify the results, and then expand. Enabling private DNS attaches a private hosted zone to the entire VPC. This overrides resolution of the Kinesis Video Streams hostname for every resource in that VPC. As a result, using the endpoint is an all-or-nothing decision for each VPC. You cannot put one application on the endpoint and leave another on the public path in the same VPC. That requires separate VPCs.
+ Keep the public path available for rollback. To roll back, modify the endpoint and clear the **Enable private DNS name** check box. The Kinesis Video Streams hostname then resolves to the public IP addresses for Kinesis Video Streams again.
+ Validate with a test stream before migrating production traffic.
+ Monitor error rates and latency for ingestion and playback, and monitor for throttling.

## Known limitations
<a name="vpce-pl-limitations"></a>

The following limitations apply:
+ WebRTC is not supported over VPC endpoints for any use case. For more information about why WebRTC traffic fails and why private DNS applies to an entire VPC, see [Private DNS](#vpce-pl-private-dns) and [Best practices](#vpce-pl-best-practices).
+ Traffic through a VPC endpoint is subject to a separate request-rate quota. For more information, see [Quotas and throttling](#vpce-pl-quotas).

## Availability
<a name="vpce-pl-availability"></a>

Interface VPC endpoints for Kinesis Video Streams are available in the following Regions.

Commercial Regions:
+ US East (N. Virginia) `us-east-1`
+ US East (Ohio) `us-east-2`
+ US West (Oregon) `us-west-2`
+ Canada (Central) `ca-central-1`
+ South America (São Paulo) `sa-east-1`
+ Europe (Ireland) `eu-west-1`
+ Europe (London) `eu-west-2`
+ Europe (Paris) `eu-west-3`
+ Europe (Frankfurt) `eu-central-1`
+ Europe (Spain) `eu-south-2`
+ Asia Pacific (Tokyo) `ap-northeast-1`
+ Asia Pacific (Seoul) `ap-northeast-2`
+ Asia Pacific (Singapore) `ap-southeast-1`
+ Asia Pacific (Sydney) `ap-southeast-2`
+ Asia Pacific (Malaysia) `ap-southeast-5`
+ Asia Pacific (Mumbai) `ap-south-1`
+ Asia Pacific (Hong Kong) `ap-east-1`
+ Africa (Cape Town) `af-south-1`
+ Israel (Tel Aviv) `il-central-1`

China Region (AWS China partition, accessed through China accounts and the console):
+ China (Beijing) `cn-north-1`

AWS GovCloud (US) Regions (accessed through AWS GovCloud (US) accounts):
+ AWS GovCloud (US-East) `us-gov-east-1`
+ AWS GovCloud (US-West) `us-gov-west-1`