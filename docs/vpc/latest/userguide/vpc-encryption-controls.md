# Enforce VPC encryption in transit

VPC Encryption Controls is a security and compliance feature that offers you centralized authoritative control to monitor the encryption status of your traffic flows, helps you identify resources that allow cleartext communication, and eventually gives you mechanisms to enforce encryption in transit within and across your VPCs in a region

VPC Encryption Controls uses both application-layer encryption and built-in encryption in transit capability of AWS nitro system hardware to ensure encryption enforcement. This feature also extends the native hardware-layer encryption beyond the modern Nitro instances to other AWS services including Fargate, Application Load Balancer, Transit Gateways and many others.

The feature is designed for anyone who wants to ensure visibility and control into the encryption status of all their traffic. It is especially useful in industries, where data encryption is paramount for meeting compliance standards such as HIPAA, FedRamp and PCI DSS. Security administrators and cloud architects can use it to centrally exercise encryption in transit policies across their AWS environment

This feature can be used in two modes: monitor mode and enforce mode.

## Encryption Controls Modes

###### Monitor mode

In monitor mode, Encryption Controls provides visibility into the encryption status of traffic flows between your AWS resources inside and across VPCs. It also helps you identify VPC resources that are not enforcing encryption in transit. You can configure your VPC flow logs to emit the enriched field - `encryption-status` - that tells you whether your traffic is encrypted. You can also use console or `GetVpcResourcesBlockingEncryptionEnforcement` command to identify the resources that are not enforcing encryption in transit.

###### Note

Existing VPCs can only be enabled in Monitor Mode first. This gives you visibility into the resources that are or may allow cleartext traffic. You can only turn on enforce mode on your VPC once these resources start enforcing encryption (or you create exclusions for them).

###### Enforce mode

In enforce mode, VPC Encryption Controls prevents you from using any features or services that allow unencrypted traffic within the VPC boundary. You cannot enable Encryption Controls in enforce mode directly on your existing VPCs. You must first turn on Encryption Controls in monitor mode, identify and modify non-compliant resources to enforce encryption in transit and then turn on enforce mode. You can however turn on Encryption Controls in enforce mode for new VPCs during creation.

When enabled, enforce mode prevents you from creating or attaching unencrypted VPC resources such as old EC2 instances that do not support native in-built encryption, or internet gateways, etc. If you want to run a non-compliant resource in an encryption-enforced VPC, you must create an exclusion for that resource.

## Monitoring Encryption status of Traffic Flows

You can audit the encryption status of traffic flows inside the VPC using the `encryption-status` field in your VPC Flow Logs. It can have the following values:

- `0` = not encrypted
- `1` = nitro-encrypted (managed by VPC Encryption Controls)
- `2` = application-encrypted
  - flows on TCP port 443 for interface endpoint to AWS service \*
  - flows on TCP port 443 for gateway endpoint \*
  - flows to encrypted Redshift cluster via VPC endpoint \*\*

- `3` = both nitro AND application encrypted
- `(-)` = Encryption Status Unknown or VPC encryption controls is off

**Note:**

\* For interface and gateway endpoints, AWS does not look at packet data to determine encryption status, we instead rely on the port used to assume encryption status.

\*\* For specified AWS managed endpoints, AWS determines encryption status based on the requirement for TLS in the service configuration.

**VPC Flow Log limitations**

- For enabling flow logs for VPC Encryption Controls, you need to create new flow logs with the encryption-status field manually. The encryption-status field is not automatically added to existing flow logs.
- It is recommended to add the ${traffic-path} and ${flow-direction} fields to the flow logs for more detailed information in the flow logs.

Example:

```
aws ec2 create-flow-logs \
--resource-type VPC \
--resource-ids vpc-12345678901234567 \
--traffic-type ALL \
--log-group-name my-flow-logs \
--deliver-logs-permission-arn arn:aws:iam::123456789101:role/publishFlowLogs
--log-format '${encryption-status} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${traffic-path} ${flow-direction} ${reject-reason}'
```

## VPC Encryption Controls Exclusions

VPC encryption controls enforce mode requires that all your resources in the VPC enforce encryption. This ensures encryption within AWS in a region. However, you may have resources like internet gateway, NAT gateway or virtual private gateway that allow connectivity outside AWS's networks where you're responsible for configuring and maintaining end-to-end encryption. To run these resources in encryption enforced VPCs, you can create resource exclusions. An exclusion creates an auditable exception for resources where the customer is responsible for maintaining encryption (typically at the application layer).

There are only 8 supported exclusions for VPC Encryption Controls. If you have these resources in your VPC and want to move to enforce mode, you must add these exclusions when switching from monitor to enforce mode. No other resources are excludable. You can migrate your VPC to enforce mode by creating exclusions for these resources. You are responsible for encryption of traffic flows to and from these resources

- Internet Gateway
- NAT Gateway
- Egress-only Internet Gateway
- VPC Peering connections to encryption un-enforced VPCs (see VPC peering support section for detailed scenarios)
- Virtual Private Gateway
- Lambda functions inside your VPC
- VPC Lattice
- Elastic File System

## Implementation workflow

1. **Enable monitoring** - Create VPC encryption control in monitor mode
2. **Analyze traffic** - Review Flow Logs to monitor encryption status of traffic flow
3. **Analyze Resources** - Use console or `GetVpcResourcesBlockingEncryptionEnforcement` command to identify the resources that are not enforcing encryption in transit.
4. **Prepare [Optional]** - Plan resource migrations and required exclusions if you want to turn on enforce mode
5. **Enforce [Optional]** - Switch to enforce mode with required exclusions configured
6. **Audit** - Ongoing compliance monitoring through Flow Logs

For detailed setup instructions, see the blog [Introducing VPC encryption controls: enforce encryption in transit within and across VPCs in a region](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region "https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region").

## VPC Encryption Controls States

VPC Encryption controls can have one of the following states:

**creating**

VPC encryption controls is being created on the VPC.

**modify-in-progress**

VPC Encryption controls is being modified on the VPC

**deleting**

VPC Encryption controls is being deleted on the VPC

**available**

VPC Encryption controls succeeded in implementing monitor mode or enforce mode on the VPC

## AWS service support and compatibility

To be encryption compliant, a resource must always enforce encryption in transit, either at the hardware layer or at the application layer. For most resources, no action is required from you.

### Services with automatic compliance

Most AWS services supported by PrivateLink, including Cross-Region PrivateLinks will accept traffic encrypted at the application layer. You are not required to make any changes to these resources. AWS automatically drops any traffic that is not application-layer-encrypted. Some exceptions include Redshift clusters (both provisioned and serverless - where you need to manually migrate the underlying resources)

### Resources that migrate automatically

Network Load Balancers, Application Load Balancers, Fargate clusters, EKS Control Plane will automatically migrate to hardware that natively supports encryption once you turn on monitor mode. You are not required to modify these resources. AWS handles the migration automatically.

### Resources requiring manual migration

Certain VPC resources and services require that you select the underlying instance types. All modern EC2 instances support encryption in transit. You do not have to make any changes if your services already use modern EC2 instances. You can use console or the GetVpcResourcesBlockingEncryptionEnforcement command to identify if any of these services is using older instances. If you identify such resources, you must upgrade them to any of the modern EC2 instances that supports native encryption of the nitro system hardware. These services include EC2 Instances, Auto Scaling Groups, RDS (All Databases and Document-DB), Elasticache Provisioned, Amazon Redshift Provisioned Clusters, EKS, ECS-EC2, OpenSearch Provisioned and EMR.

###### Compatible resources:

The following resources are compatible with VPC Encryption Controls:

- [Nitro-based EC2 instances](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit")
- Network Load Balancers (with limitations)
- Application Load Balancers
- AWS Fargate clusters
- Amazon Elastic Kubernetes Service (EKS)
- Amazon EC2 Auto Scaling Groups
- Amazon Relational Database Service (RDS - All Databases)
- Amazon ElastiCache node-based clusters
- Amazon Redshift Provisioned and Serverless Clusters
- Amazon Elastic Container Service (ECS) - EC2 container instances
- Amazon OpenSearch Service
- Amazon Elastic MapReduce (EMR)
- Amazon Managed Streaming for Apache Kafka (Amazon MSK)
- VPC Encryption controls enforce encryption on the application layer for all AWS services accessed via PrivateLink. Any traffic that is not encrypted at the application layer is dropped by PrivateLink endpoints hosted inside the VPC with Encryption controls in enforce mode

### Service-specific limitations

###### Network Load Balancer limitations

TLS Configuration: You cannot use a TLS listener to offload the work of encryption and decryption to your load balancer when enforcing Encryption Controls on the containing VPC. You can however configure your targets to perform TLS encryption and decryption

###### Redshift Provisioned and Serverless

Customers cannot move to Enforce mode on a VPC that has an existing cluster / endpoint. To use VPC Encryption Controls with Redshift, you must restore your cluster or namespace from a snapshot. For Provisioned Clusters, create a snapshot of your existing Redshift cluster and then restore from the snapshot using the restore from cluster snapshot operation. For Serverless, create a snapshot of your existing namespace and then restore from the snapshot using the restore from snapshot operation on your serverless workgroup. Note that VPC Encryption Controls cannot be enabled on existing clusters or namespaces without performing the snapshot and restore process. Refer to [Amazon Redshift documentation](../../../redshift/latest/mgmt/welcome.md "../../../redshift/latest/mgmt/welcome.md") for snapshot creation.

###### Amazon MSK (Managed streaming for Apache Kafka)

This functionality is supported in new clusters for 4.1 in their own VPC. The following steps will help you use VPC Encryption with MSK.

- Customer enables VPC Encryption on a VPC with no other MSK clusters
- Customer creates cluster with Kafka version 4.1 and instancetype as M7g

### Regional and zone limitations

- **Local Zone Subnets**: Not supported in enforce mode - must be deleted from VPC

### VPC peering support

To ensure encryption in transit with VPC peering between two VPCs, the two VPCs must reside in the same region and have encryption controls turned on in enforce mode without any exclusions. You must create a peering exclusion if you want to peer an encryption enforced VPC to another VPC that either resides in a different region or does not have encryption controls enabled in enforce mode (without exclusions).

If two VPCs are in enforce mode and peering with each other, you cannot change the mode from enforce to monitor. You would have to create a peering exclusion first, before modifying the VPC Encryption Controls mode to monitor.

### Transit Gateway encryption support

You must enable encryption support on a Transit Gateway explicitly to encrypt traffic between your VPCs that have encryption controls turned on. Enabling encryption on existing Transit Gateway is non-disruptive to existing traffic flows and migration of VPC attachments to encrypted lanes will happen seamlessly and automatically. Traffic between two VPCs in enforce mode (without exclusions) via the Transit Gateway traverses 100% encrypted lanes. Encryption on Transit Gateway also allows you to connect two VPCs that are in different Encryption Controls modes as well. You should use it when you want to enforce encryption controls in a VPC that is connected to a non-encryption-enforced VPC. In such a scenario, all your traffic inside your encryption-enforced VPC, including the inter-VPC traffic is encrypted. The inter-VPC traffic is encrypted between the resources in the encryption-enforced VPC and the Transit Gateway. Beyond that, encryption depends on the resources to which the traffic is going to in the non-enforced VPC and is not guaranteed to be encrypted (since the VPC is not in enforce mode). All VPCs must be in the same region.(see details [here](../tgw/tgw-encryption-support.md "../tgw/tgw-encryption-support.md")).

![Traffic flow between VPCs with different encryption control status](images/vpc-enc-control-arch.png)

- In this diagram, VPC 1, VPC 2 and VPC3 have encryption controls in enforce mode and they are connected to VPC 4 which has Encryption Controls running in monitor mode.
- All traffic between VPC1, VPC2 and VPC3 will be encrypted.
- To elaborate, any traffic between a resource in VPC 1 and a resource in VPC 4 will be encrypted until the Transit Gateway using the encryption offered by the nitro system hardware. Beyond that encryption status depends on the resource in VPC 4 and is not guaranteed to be encrypted.

For more details on Transit Gateway encryption support, see [the transit gateway documentation](../tgw/tgw-encryption-support.md "../tgw/tgw-encryption-support.md").

## Pricing

For pricing information, see the [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

## AWS CLI command reference

### Setup and configuration

- [aws ec2 create-vpc-encryption-control](../../../cli/latest/reference/ec2/create-vpc-encryption-control.md "../../../cli/latest/reference/ec2/create-vpc-encryption-control.md")
- [aws ec2 modify-vpc-encryption-control](../../../cli/latest/reference/ec2/modify-vpc-encryption-control.md "../../../cli/latest/reference/ec2/modify-vpc-encryption-control.md")
- [aws ec2 tgw modify-transit-gateway](../../../cli/latest/reference/ec2/modify-transit-gateway.md "../../../cli/latest/reference/ec2/modify-transit-gateway.md")

### Monitoring and troubleshooting

- [aws ec2 describe-vpc-encryption-controls](../../../cli/latest/reference/ec2/describe-vpc-encryption-controls.md "../../../cli/latest/reference/ec2/describe-vpc-encryption-controls.md")
- [aws ec2 get-vpc-resources-blocking-encryption-enforcement](../../../cli/latest/reference/ec2/get-vpc-resources-blocking-encryption-enforcement.md "../../../cli/latest/reference/ec2/get-vpc-resources-blocking-encryption-enforcement.md")
- [aws ec2 create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md")
- [aws ec2 describe-flow-logs](../../../cli/latest/reference/ec2/describe-flow-logs.md "../../../cli/latest/reference/ec2/describe-flow-logs.md")
- [aws logs query](../../../cli/latest/reference/logs/query.md "../../../cli/latest/reference/logs/query.md")

### Cleanup

- [aws ec2 delete-vpc-encryption-control](../../../cli/latest/reference/ec2/delete-vpc-encryption-control.md "../../../cli/latest/reference/ec2/delete-vpc-encryption-control.md")

## Additional resources

For detailed setup instructions, see the blog [Introducing VPC encryption controls: enforce encryption in transit within and across VPCs in a region](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region "https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region").

For more detailed API information, see the [EC2 API Reference Guide](../../../AWSEC2/latest/APIReference/Welcome.md "../../../AWSEC2/latest/APIReference/Welcome.md").
