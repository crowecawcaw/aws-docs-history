

# AWS Cloud WAN Flow Logs
<a name="cwan-flow-logs"></a>

Cloud WAN Flow Logs is a feature of AWS Cloud WAN that enables you to capture information about the IP traffic going to and from your core networks. Flow log data can be published to Amazon CloudWatch Logs, Amazon S3, or Firehose. After you create a flow log, you can retrieve and view its data in the chosen destination. Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance. Cloud WAN Flow Logs capture information related only to core networks, described in [Cloud WAN Flow Log records](#cwan-flow-log-records). If you want to capture information about IP traffic going to and from network interfaces in your VPCs, use VPC Flow Logs. See [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide* for more information.

Cloud WAN Flow Logs capture end-to-end, attachment-to-attachment flows over your core network. A flow log record is written at each attachment where traffic enters (ingress) or leaves (egress) the core network. A flow might not be correlated end-to-end because of an internal system error or an internal log propagation delay. For how this appears in flow log records, see the `INCOMPLETEDATA` value of the log-status field in [Cloud WAN Flow Log records](#cwan-flow-log-records).

**Note**  
To create a Cloud WAN flow log, you must be the owner of the core network and have `networkmanager:GetCoreNetwork` permissions for the core network of the resource you are subscribing on.

Flow log data for a monitored core network is recorded as *flow log records*, which are log events consisting of fields that describe the traffic flow. For more information, see [Cloud WAN Flow Log records](#cwan-flow-log-records).

To create a flow log, you specify:
+ The resource for which to create the flow log, such as a core network, core network edge, or attachment
+ The destinations to which you want to publish the flow log data, such as Amazon S3, CloudWatch Logs, or Amazon Data Firehose

After you create a flow log, it can take several minutes to begin collecting and publishing data to the chosen destinations. Flow logs do not capture real-time log streams for your core networks. 

You can apply tags to your flow logs. Each tag consists of a key and an optional value, both of which you define. Tags can help you organize your flow logs, for example by purpose or owner.

If you no longer require a flow log, you can delete it. Deleting a flow log disables the flow log service for the resource, and no new flow log records are created or published to CloudWatch Logs or Amazon S3. Deleting the flow log does not delete any existing flow log records or log streams (for CloudWatch Logs) or log file objects (for Amazon S3) for a core network. To delete an existing log stream, use the CloudWatch Logs console. To delete existing log file objects, use the Amazon S3 console. After you've deleted a flow log, it can take several minutes to stop collecting data. For more information, see [Delete an AWS Cloud WAN Flow Logs record](cwan-delete-flow-log.md).

You can create flow logs for your core networks that can publish data to CloudWatch Logs, Amazon S3, or Amazon Data Firehose. For more information, see the following:
+  [Create a Flow Log that publishes to CloudWatch Logs ](cwan-flow-logs-cwl-create-flow-log.md)
+ [Create a Flow Log that publishes to Amazon S3](cwan-flowlog-s3-create.md)
+ [Create a Flow Log that publishes to Firehose](cwan-flow-logs-kinesis-create.md)

## Limitations
<a name="cwan-flow-logs-limits"></a>

The following limitations apply to Cloud WAN Flow Logs:
+ Cloud WAN Flow Logs supports a maximum of 250 subscriptions per resource per account. To create additional subscriptions on a resource that has reached this limit, you must first delete existing subscriptions.
+ Tunnel-less Connect (TLC) attachments are not supported. Flows traversing a TLC attachment appear on the underlying transport (VPC) attachment. To capture these flows, create a flow log on the transport attachment.
+ Route Table attachments are not supported. Flows traversing a Route Table attachment appear on the underlying peering connection.
+ Segment IDs may be briefly stale during initial propagation.
+ When you create a subscription, it is placed in the PROVISIONING state until logs can be delivered. Even after the subscription reaches the ACTIVE state, it can take a few minutes before log vending is fully enabled for the resource.
+ After you create your first subscription on a AWS Cloud WAN resource, your core network moves to the UPDATING state while some resources are provisioned. During that period, the flow logs subscription is in the PROVISIONING state. After your core network returns to the AVAILABLE state, it can still take several minutes before the flow logs subscription changes to ACTIVE and you begin to see log delivery.
+ Subscriptions can only be created in AWS Cloud WAN home Regions. For more information, see [Home Region](what-is-cloudwan.md#cloudwan-home-region).

## Cloud WAN Flow Log records
<a name="cwan-flow-log-records"></a>

A flow log record represents a network flow in your core network. Each record is a string with fields separated by spaces. A record includes values for the different components of the traffic flow, for example, the source, destination, and protocol.

When you create a flow log, you can use the default format for the flow log record, or you can specify a custom format.

**Topics**
+ [Default format](#cwan-flow-logs-default)
+ [Custom format](#cwan-flow-logs-custom)
+ [Available fields](#cwan-flow-logs-fields)

### Default format
<a name="cwan-flow-logs-default"></a>

With the default format, the flow log records include all version 2 to version 13 fields except the 1:1 NAT fields (src-nat-addr and dst-nat-addr). You cannot customize or change the default format. To capture the 1:1 NAT fields or a different subset of fields, specify a custom format instead.

### Custom format
<a name="cwan-flow-logs-custom"></a>

With a custom format, you specify which fields are included in the flow log records and in which order. This enables you to create flow logs that are specific to your needs, and to omit fields that are not relevant. Using a custom format can reduce the need for separate processes to extract specific information from the published flow logs. You can specify any number of the available flow log fields, but you must specify at least one.

### Available fields
<a name="cwan-flow-logs-fields"></a>

The following table describes all of the available fields for a core network flow log record. The **Version** column indicates which version the field was introduced in.

When publishing flow log data to Amazon S3, the data type for the fields depends on the flow log format. If the format is plain text, all fields are of type STRING. If the format is Parquet, see the table for the field data types.

If a field is not applicable or could not be computed for a specific record, the record displays a '-' symbol for that entry. Metadata fields that do not come directly from the packet header are best effort approximations, and their values might be missing or inaccurate.


| Field | Description | Version | 
| --- | --- | --- | 
| version | The version of the flow log record. Cloud WAN Flow Logs use version 13 fields.<br />**Parquet data type:** INT\_32 | 2 | 
| account-id | The AWS account ID of the owner of the source core network.<br />**Parquet data type:** STRING | 2 | 
| srcaddr | The source address for incoming traffic. <br />**Parquet data type: ** STRING | 2 | 
| srcport | The source port of the traffic.<br />**Parquet data type: **INT\_32  | 2 | 
| dstaddr | The destination address for outgoing traffic.<br />**Parquet data type: ** STRING | 2 | 
| dstport | The destination port of the traffic.<br />**Parquet data type: ** INT\_32 | 2 | 
| protocol | The IANA protocol number of the traffic. For more information, see [ Assigned Internet Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).<br />**Parquet data type: ** INT\_64 | 2 | 
| packets | The number of packets transferred during the flow.<br />**Parquet data type:** INT\_64 | 2 | 
| bytes | The number of bytes transferred during the flow.<br />**Parquet data type: ** INT\_64 | 2 | 
| start | The time, in Unix seconds, when the first packet of the flow was received within the aggregation interval. This might be up to 60 seconds after the packet was transmitted or received on the core network.<br />**Parquet data type: ** INT\_64 | 2 | 
| end | The time, in Unix seconds, when the last packet of the flow was received within the aggregation interval. This might be up to 60 seconds after the packet was transmitted or received on the core network.<br />**Parquet data type: ** INT\_64 | 2 | 
| log-status | The status of the flow log:+   OK — Data is logging normally to the chosen destinations.  <br />+  NODATA — There was no network traffic to or from the core network during the aggregation interval.  <br />+  SKIPDATA — Some flow log records were skipped during the aggregation interval. This might be because of an internal capacity constraint, or an internal error. <br />+  INCOMPLETEDATA — The flow could not be fully captured during the aggregation interval, so the delivered flow record might be only partially complete. This can be caused by an internal system error or an internal log propagation delay. <br />**Parquet data type:** STRING | 2 | 
| type | The type of traffic. Possible values are IPv4 \| IPv6 \| EFA. For more information, see [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the *Amazon EC2 User Guide*.<br />**Parquet data type:** STRING | 3 | 
| tcp-flags | The bitmask value for the following TCP flags:+  FIN — 1 <br />+  SYN — 2 <br />+  RST — 4 <br />+  PSH — 8 <br />+  ACK — 16 <br />+  SYN-ACK — 18 <br />+  URG — 32  When a flow log entry consists of only ACK packets, the flag value is 0, not 16. <br />For general information about TCP flags (such as the meaning of flags like FIN, SYN, and ACK), see [TCP segment structure ](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure) on Wikipedia.<br />TCP flags can be OR-ed during the aggregation interval. For short connections, the flags might be set on the same line in the flow log record, for example, 19 for SYN-ACK and FIN, and 3 for SYN and FIN.<br />**Parquet data type:** INT\_32 | 3 | 
| pkt-src-aws-service | The name of the subset of [IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html) for the srcaddr if the source IP address is for an AWS service. The possible values are: AMAZON \| AMAZON\_APPFLOW \| AMAZON\_CONNECT \| API\_GATEWAY \| CHIME\_MEETINGS \| CHIME\_VOICECONNECTOR \| CLOUD9 \| CLOUDFRONT \| CODEBUILD \| DYNAMODB \| EBS \| EC2 \| EC2\_INSTANCE\_CONNECT \| GLOBALACCELERATOR \| KINESIS\_VIDEO\_STREAMS \| ROUTE53 \| ROUTE53\_HEALTHCHECKS \| ROUTE53\_HEALTHCHECKS\_PUBLISHING \| ROUTE53\_RESOLVER \| S3 \| WORKSPACES\_GATEWAYS.<br />**Parquet data type:** STRING | 5 | 
| pkt-dst-aws-service | The name of the subset of IP address ranges for the dstaddr field, if the destination IP address is for an AWS service. For a list of possible values, see the pkt-src-aws-service field.Parquet data type: STRING | 5 | 
| flow-direction | The direction of the flow with respect to the core network. The possible values are: ingress \| egress.<br />**Parquet data type:** STRING | 5 | 
| resource-type | The type of resource on which the subscription is created. For Cloud WAN Flow Logs, this will be CloudWAN.Parquet data type: STRING | 6 | 
| packets-lost-no-route | The packets lost due to no route being specified.<br />**Parquet data type: **INT\_64  | 6 | 
| packets-lost-blackhole | The packets lost due to a black hole.<br />**Parquet data type: **INT\_64  | 6 | 
| packets-lost-mtu-exceeded | The packets lost due to the size exceeding the MTU.<br />**Parquet data type:** INT\_64  | 6 | 
| packets-lost-ttl-expired | The packets lost due to the expiration of time-to-live.<br />**Parquet data type:** INT\_64  | 6 | 
| src-nat-addr | The source address of the traffic after 1:1 NAT translation.<br />**Parquet data type:** STRING | 13 | 
| dst-nat-addr | The destination address of the traffic after 1:1 NAT translation.<br />**Parquet data type:** STRING | 13 | 
| core-network-id | The ID of the core network for which traffic is being recorded.**Parquet data type: **STRING | 13 | 
| cwan-attachment-id | The ID of the attachment on which the flow log is recorded (the local side of the flow).**Parquet data type: ** STRING | 13 | 
| cwan-pair-attachment-id | The ID of the attachment on the other side of the flow. Depending on the flow direction, this is either the ingress or egress attachment of the flow.<br />**Parquet data type:** STRING | 13 | 
| src-account-id | The AWS account ID of the owner of the attachment on the source side of the flow.<br />**Parquet data type:** STRING  | 13 | 
| dst-account-id | The AWS account ID of the owner of the attachment on the destination side of the flow.<br />**Parquet data type:** STRING  | 13 | 
| src-vpc-id |  The ID of the VPC on the source side of the flow, when that side is a VPC attachment. **Parquet data type:** STRING  | 13 | 
| dst-vpc-id | The ID of the VPC on the destination side of the flow, when that side is a VPC attachment.<br />**Parquet data type:** STRING  | 13 | 
| src-subnet-id | The ID of the subnet on the source side of the flow, when that side is a VPC attachment.<br />**Parquet data type:** STRING  | 13 | 
| dst-subnet-id | The ID of the subnet on the destination side of the flow, when that side is a VPC attachment.<br />**Parquet data type:** STRING  | 13 | 
| src-eni | The ID of the elastic network interface on the source side of the flow, when that side is a VPC attachment.<br />**Parquet data type:** STRING  | 13 | 
| dst-eni | The ID of the elastic network interface on the destination side of the flow, when that side is a VPC attachment.**Parquet data type:** STRING  | 13 | 
| src-az-id | The ID of the Availability Zone of the attachment on the source side of the flow. If the source side is not associated with a specific Availability Zone, the record displays a '-' symbol for this field.<br />**Parquet data type:** STRING | 13 | 
| dst-az-id | The ID of the Availability Zone of the attachment on the destination side of the flow. If the destination side is not associated with a specific Availability Zone, the record displays a '-' symbol for this field.<br />**Parquet data type:** STRING | 13 | 
| src-region | The Region of the core network edge for the attachment on the source side of the flow.<br />**Parquet data type:** STRING | 13 | 
| dst-region | The Region of the core network edge for the attachment on the destination side of the flow.<br />**Parquet data type:** STRING | 13 | 
| src-segment-name | The name of the core network segment for the source traffic.<br />**Parquet data type:** STRING | 13 | 
| dst-segment-name | The name of the core network segment for the destination traffic.<br />**Parquet data type:** STRING | 13 | 
| src-attachment-type | The type of the attachment on the source side of the flow, for example vpc.<br />**Parquet data type:** STRING | 13 | 
| dst-attachment-type | The type of the attachment on the destination side of the flow, for example vpc.<br />**Parquet data type:** STRING | 13 | 
| network-function-group-attachment-ids | A comma-separated list of the IDs of the network function group attachments that the flow traversed.<br />**Parquet data type:** STRING | 13 | 

## Control the use of flow logs
<a name="cwan-controlling-use-of-flow-logs"></a>

By default, users do not have permission to work with flow logs. You can create a user policy that grants users the permissions to create, describe, and delete flow logs. For more information, see [Granting IAM Users Required Permissions for Amazon EC2 Resources](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ec2-api-permissions.html) in the *Amazon EC2 API Reference*.

Some additional IAM role and permission configuration is required, depending on whether you're publishing to CloudWatch Logs or Amazon S3. For more information, see [AWS Cloud WAN Flow Logs records in Amazon CloudWatch Logs](cwan-flow-logs-cwl.md) and [AWS Cloud WAN Flow Logs records in Amazon S3](cwan-flow-logs-s3.md).

## Cloud WAN Flow Logs pricing
<a name="cwan-flow-logs-pricing"></a>

Data ingestion and storage charges for vended logs apply when you publish Cloud WAN flow logs. For more information about pricing when publishing vended logs, open [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/), and then under **Paid tier**, select **Logs** and find **Vended Logs**.

Cloud WAN does not introduce any additional charges for this feature.