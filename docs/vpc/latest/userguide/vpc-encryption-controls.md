

# Enforce VPC encryption in transit
<a name="vpc-encryption-controls"></a>

VPC Encryption Controls is a security and compliance feature that offers you centralized authoritative control to monitor the encryption status of your traffic flows, helps you identify resources that allow cleartext communication, and eventually gives you mechanisms to enforce encryption in transit within and across your VPCs in a region

VPC Encryption Controls uses both application-layer encryption and built-in encryption in transit capability of AWS nitro system hardware to ensure encryption enforcement. This feature also extends the native hardware-layer encryption beyond the modern Nitro instances to other AWS services including Fargate, Application Load Balancer, Transit Gateways and many others.

The feature is designed for anyone who wants to ensure visibility and control into the encryption status of all their traffic. It is especially useful in industries, where data encryption is paramount for meeting compliance standards such as HIPAA, FedRamp and PCI DSS. Security administrators and cloud architects can use it to centrally exercise encryption in transit policies across their AWS environment

This feature can be used in two modes: monitor mode and enforce mode.

## Encryption Controls Modes
<a name="encryption-controls-modes"></a>

**Monitor mode**  
In monitor mode, Encryption Controls provides visibility into the encryption status of traffic flows between your AWS resources inside and across VPCs. It also helps you identify VPC resources that are not enforcing encryption in transit. You can configure your VPC flow logs to emit the enriched field - `encryption-status` - that tells you whether your traffic is encrypted. You can also use console or `GetVpcResourcesBlockingEncryptionEnforcement` command to identify the resources that are not enforcing encryption in transit.

**Note**  
Existing VPCs can only be enabled in Monitor Mode first. This gives you visibility into the resources that are or may allow cleartext traffic. You can only turn on enforce mode on your VPC once these resources start enforcing encryption (or you create exclusions for them).

**Enforce mode**  
In enforce mode, VPC Encryption Controls prevents you from using any features or services that allow unencrypted traffic within the VPC boundary. You cannot enable Encryption Controls in enforce mode directly on your existing VPCs. You must first turn on Encryption Controls in monitor mode, identify and modify non-compliant resources to enforce encryption in transit and then turn on enforce mode. You can however turn on Encryption Controls in enforce mode for new VPCs during creation.

When enabled, enforce mode prevents you from creating or attaching unencrypted VPC resources such as old EC2 instances that do not support native in-built encryption, or internet gateways, etc. If you want to run a non-compliant resource in an encryption-enforced VPC, you must create an exclusion for that resource.

## Monitoring Encryption status of Traffic Flows
<a name="monitoring-encryption-status"></a>

You can audit the encryption status of traffic flows inside the VPC using the `encryption-status` field in your VPC Flow Logs. It can have the following values:
+ `0` = not encrypted
+ `1` = nitro-encrypted (managed by VPC Encryption Controls)
+ `2` = application-encrypted 
  +  flows on TCP port 443 for interface endpoint to AWS service \* 
  +  flows on TCP port 443 for gateway endpoint \* 
  +  flows to encrypted Redshift cluster through VPC endpoint \*\* 
+ `3` = both nitro AND application encrypted
+ `(-)` = Encryption Status Unknown or VPC encryption controls is off

**Note:**

\* For interface and gateway endpoints, AWS does not look at packet data to determine encryption status, we instead rely on the port used to assume encryption status.

\*\* For specified AWS managed endpoints, AWS determines encryption status based on the requirement for TLS in the service configuration.

**VPC Flow Log limitations**
+ For enabling flow logs for VPC Encryption Controls, you need to create new flow logs with the encryption-status field manually. The encryption-status field is not automatically added to existing flow logs.
+ It is recommended to add the ${traffic-path} and ${flow-direction} fields to the flow logs for more detailed information in the flow logs.

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
<a name="vpc-encryption-controls-exclusions"></a>

VPC encryption controls enforce mode requires that all your resources in the VPC enforce encryption. This ensures encryption within AWS in a region. However, you may have resources like internet gateway, NAT gateway or virtual private gateway that allow connectivity outside AWS's networks where you're responsible for configuring and maintaining end-to-end encryption. To run these resources in encryption enforced VPCs, you can create resource exclusions. An exclusion creates an auditable exception for resources where the customer is responsible for maintaining encryption (typically at the application layer).

There are only 8 supported exclusions for VPC Encryption Controls. If you have these resources in your VPC and want to move to enforce mode, you must add these exclusions when switching from monitor to enforce mode. No other resources are excludable. You can migrate your VPC to enforce mode by creating exclusions for these resources. You are responsible for encryption of traffic flows to and from these resources
+ Internet Gateway
+ NAT Gateway
+ Egress-only Internet Gateway
+ VPC Peering connections to encryption un-enforced VPCs (see VPC peering support section for detailed scenarios)
+ Virtual Private Gateway
+ Lambda functions inside your VPC
+ VPC Lattice
+ Elastic File System

## Implementation workflow
<a name="implementation-workflow"></a>

1. **Enable monitoring** - Create VPC encryption control in monitor mode

1. **Analyze traffic** - Review Flow Logs to monitor encryption status of traffic flow

1. **Analyze Resources** - Use console or `GetVpcResourcesBlockingEncryptionEnforcement` command to identify the resources that are not enforcing encryption in transit.

1. **Prepare [Optional]** - Plan resource migrations and required exclusions if you want to turn on enforce mode

1. **Enforce [Optional]** - Switch to enforce mode with required exclusions configured

1. **Audit** - Ongoing compliance monitoring through Flow Logs

For detailed setup instructions, see the blog [Introducing VPC encryption controls: enforce encryption in transit within and across VPCs in a region](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region).

## VPC Encryption Controls States
<a name="vpc-encryption-controls-states"></a>

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
<a name="aws-service-support-compatibility"></a>

To be encryption compliant, a resource must always enforce encryption in transit, either at the hardware layer or at the application layer. For most resources, no action is required from you.

### Services with automatic compliance
<a name="services-automatic-compliance"></a>

Most AWS services supported by PrivateLink, including Cross-Region PrivateLinks will accept traffic encrypted at the application layer. You are not required to make any changes to these resources. AWS automatically drops any traffic that is not application-layer-encrypted. Some exceptions include Redshift clusters (both provisioned and serverless - where you need to manually migrate the underlying resources)

### Resources that migrate automatically
<a name="resources-migrate-automatically"></a>

Network Load Balancers, Application Load Balancers, Fargate clusters, EKS Control Plane will automatically migrate to hardware that natively supports encryption once you turn on monitor mode. You are not required to modify these resources. AWS handles the migration automatically.

### Resources requiring manual migration
<a name="resources-requiring-manual-migration"></a>

Certain VPC resources and services require that you select the underlying instance types. All modern EC2 instances support encryption in transit. You do not have to make any changes if your services already use modern EC2 instances. You can use console or the GetVpcResourcesBlockingEncryptionEnforcement command to identify if any of these services is using older instances. If you identify such resources, you must upgrade them to any of the modern EC2 instances that supports native encryption of the nitro system hardware. These services include EC2 instances, Auto Scaling Groups, RDS (All Databases and Document-DB), Elasticache Provisioned, Amazon Redshift Provisioned Clusters, EKS, ECS-EC2, OpenSearch Provisioned and EMR.

**Compatible resources:**  
The following resources are compatible with VPC Encryption Controls:
+ [Nitro-based EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit)
+ Network Load Balancers (with limitations)
+ Application Load Balancers
+ AWS Fargate clusters
+ Amazon Elastic Kubernetes Service (EKS)
+ Amazon EC2 Auto Scaling Groups
+ Amazon Relational Database Service (RDS - All Databases)
+ Amazon ElastiCache node-based clusters
+ Amazon Redshift Provisioned and Serverless Clusters
+ Amazon Elastic Container Service (ECS) - EC2 container instances
+ Amazon OpenSearch Service
+ Amazon Elastic MapReduce (EMR)
+ Amazon Managed Streaming for Apache Kafka (Amazon MSK)
+ VPC Encryption controls enforce encryption on the application layer for all AWS services accessed through PrivateLink. Any traffic that is not encrypted at the application layer is dropped by PrivateLink endpoints hosted inside the VPC with Encryption controls in enforce mode

### Service-specific limitations
<a name="service-specific-limitations"></a>

**Network Load Balancer limitations**  
TLS Configuration: You cannot use a TLS listener to offload the work of encryption and decryption to your load balancer when enforcing Encryption Controls on the containing VPC. You can however configure your targets to perform TLS encryption and decryption

**Redshift Provisioned and Serverless**  
Customers cannot move to Enforce mode on a VPC that has an existing cluster / endpoint. To use VPC Encryption Controls with Redshift, you must restore your cluster or namespace from a snapshot. For Provisioned Clusters, create a snapshot of your existing Redshift cluster and then restore from the snapshot using the restore from cluster snapshot operation. For Serverless, create a snapshot of your existing namespace and then restore from the snapshot using the restore from snapshot operation on your serverless workgroup. Note that VPC Encryption Controls cannot be enabled on existing clusters or namespaces without performing the snapshot and restore process. Refer to [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) for snapshot creation.

**Amazon MSK (Managed streaming for Apache Kafka)**  
This functionality is supported in new clusters for 4.1 in their own VPC. The following steps will help you use VPC Encryption with MSK.
+ Customer enables VPC Encryption on a VPC with no other MSK clusters
+ Customer creates cluster with Kafka version 4.1 and instancetype as M7g

**Gateway Load Balancer and AWS Network Firewall**  
Gateway Load Balancer and AWS Network Firewall are not supported with VPCs in enforce mode. If these resources are present in your VPC, you must run your VPC in monitor mode.

### Regional and zone limitations
<a name="regional-zone-limitations"></a>
+ **Local Zone Subnets**: Not supported in enforce mode - must be deleted from VPC

### VPC peering support
<a name="vpc-peering-support"></a>

To ensure encryption in transit with VPC peering between two VPCs, the two VPCs must reside in the same region and have encryption controls turned on in enforce mode without any exclusions. You must create a peering exclusion if you want to peer an encryption enforced VPC to another VPC that either resides in a different region or does not have encryption controls enabled in enforce mode (without exclusions).

If two VPCs are in enforce mode and peering with each other, you cannot change the mode from enforce to monitor. You would have to create a peering exclusion first, before modifying the VPC Encryption Controls mode to monitor.

### Transit Gateway encryption support
<a name="transit-gateway-encryption-support"></a>

You must enable encryption support on a Transit Gateway explicitly to encrypt traffic between your VPCs that have encryption controls turned on. Enabling encryption on existing Transit Gateway is non-disruptive to existing traffic flows and migration of VPC attachments to encrypted lanes will happen seamlessly and automatically. Traffic between two VPCs in enforce mode (without exclusions) through the Transit Gateway traverses 100% encrypted lanes. Encryption on Transit Gateway also allows you to connect two VPCs that are in different Encryption Controls modes as well. You should use it when you want to enforce encryption controls in a VPC that is connected to a non-encryption-enforced VPC. In such a scenario, all your traffic inside your encryption-enforced VPC, including the inter-VPC traffic is encrypted. The inter-VPC traffic is encrypted between the resources in the encryption-enforced VPC and the Transit Gateway. Beyond that, encryption depends on the resources to which the traffic is going to in the non-enforced VPC and is not guaranteed to be encrypted (since the VPC is not in enforce mode). All VPCs must be in the same region.(see details [here](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-encryption-support.html)).

![Traffic flow between VPCs with different encryption control status.](http://docs.aws.amazon.com/vpc/latest/userguide/images/vpc-enc-control-arch.png)

+ In this diagram, VPC 1, VPC 2 and VPC3 have encryption controls in enforce mode and they are connected to VPC 4 which has Encryption Controls running in monitor mode.
+ All traffic between VPC1, VPC2 and VPC3 will be encrypted.
+ To elaborate, any traffic between a resource in VPC 1 and a resource in VPC 4 will be encrypted until the Transit Gateway using the encryption offered by the nitro system hardware. Beyond that encryption status depends on the resource in VPC 4 and is not guaranteed to be encrypted.

For more details on Transit Gateway encryption support, see [the transit gateway documentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-encryption-support.html).

### Enable VPC Encryption Controls at the Account level
<a name="account-level-encryption-controls"></a>

Account-level VPC Encryption Controls allow you to set the encryption control mode and resource exclusions that apply to all VPCs in your account. This provides centralized management of encryption policies without needing to configure each VPC individually.

Account-level encryption controls support the same eight resource exclusions as VPC-level controls: Internet Gateway, NAT Gateway, Egress-only Internet Gateway, VPC Peering, Virtual Private Gateway, Lambda, VPC Lattice, and Elastic File System.

#### Account-level Encryption Controls modes
<a name="account-encryption-controls-modes"></a>

You can set the following modes at the account level:

**Unmanaged**  
VPC Encryption Controls remain in their current mode and can be managed at the VPC level.

**Attempt Monitor**  
Attempts to transition all VPCs in the account to monitor mode. Identifies unencrypted resources without blocking creation.

**Attempt Enforce**  
Attempts to transition all VPCs in the account to enforce mode. Blocks creation of unencrypted resources.

#### Account-level Encryption Controls states
<a name="account-encryption-controls-states"></a>

Account-level VPC Encryption Controls can have one of the following states:

**default-state**  
The account-level VPC Encryption Control has not been enabled.

**transitions-in-progress**  
The VPCs in the account are being transitioned to the specified mode.

**transitions-partially-successful**  
One or more VPCs did not transition to the expected mode.

**transitions-successful**  
All VPCs successfully transitioned to the expected mode.

**transitions-failed**  
All VPCs failed to transition to the expected mode.

### Enable VPC Encryption Controls at the Organization level
<a name="organization-level-encryption-controls"></a>

If you are using AWS Organizations to manage accounts in your organization, you can use an [AWS Organizations declarative policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_policies.html) to enforce VPC Encryption Controls on the accounts in the organization. For more information about the VPC Encryption Controls declarative policy, see [Supported declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ec2_syntax.html#declarative-policy-vpc-block-public-access) in the AWS Organizations User Guide.

## Pricing
<a name="pricing"></a>

For pricing information, see the [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/).

## AWS CLI command reference
<a name="cli-commands-reference"></a>

### Setup and configuration
<a name="setup-configuration"></a>
+ [aws ec2 create-vpc-encryption-control](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-encryption-control.html)
+ [aws ec2 modify-vpc-encryption-control](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-encryption-control.html)
+ [aws ec2 modify-account-vpc-encryption-control](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-account-vpc-encryption-control.html)
+ [aws ec2 describe-account-vpc-encryption-control](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-account-vpc-encryption-control.html)
+ [aws ec2 tgw modify-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway.html)

### Monitoring and troubleshooting
<a name="monitoring-troubleshooting"></a>
+ [aws ec2 describe-vpc-encryption-controls](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-encryption-controls.html)
+ [aws ec2 get-vpc-resources-blocking-encryption-enforcement](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-vpc-resources-blocking-encryption-enforcement.html)
+ [aws ec2 create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html)
+ [aws ec2 describe-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-flow-logs.html)
+ [aws logs query](https://docs.aws.amazon.com/cli/latest/reference/logs/query.html)

### Cleanup
<a name="cleanup"></a>
+ [aws ec2 delete-vpc-encryption-control](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-encryption-control.html)

## Additional resources
<a name="additional-resources"></a>

For detailed setup instructions, see the blog [Introducing VPC encryption controls: enforce encryption in transit within and across VPCs in a region](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region).

For more detailed API information, see the [EC2 API Reference Guide](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html).