# Improve the security of EC2 instances by using VPC

endpoints for Systems Manager

You can improve the security posture of your managed nodes (including non-EC2 machines
in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment) by configuring AWS Systems Manager to use an interface VPC endpoint
in Amazon Virtual Private Cloud (Amazon VPC). By using an interface VPC endpoint (interface endpoint), you can
connect to services powered by AWS PrivateLink. AWS PrivateLink is a technology that allows
you to privately access Amazon Elastic Compute Cloud (Amazon EC2) and Systems Manager APIs by using private IP addresses.

AWS PrivateLink restricts all network traffic between your managed instances, Systems Manager, and
Amazon EC2 to the Amazon network. This means that your managed instances don't have access to
the Internet. If you use AWS PrivateLink, you don't need an internet gateway, a NAT
device, or a virtual private gateway.

You aren't required to configure AWS PrivateLink, but it's recommended. For more
information about AWS PrivateLink and VPC endpoints, see [AWS PrivateLink and VPC
endpoints](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md").

###### Note

The alternative to using a VPC endpoint is to allow outbound internet access on
your managed instances. In this case, the managed instances must also allow HTTPS
(port 443) outbound traffic to the following endpoints:

- `ssm.`region`.amazonaws.com`
- `ssmmessages.`region`.amazonaws.com`
- `ec2messages.`region`.amazonaws.com`
  SSM Agent initiates all connections to the Systems Manager service in the cloud. For this
  reason, you don't need to configure your firewall to allow inbound traffic to your
  instances for Systems Manager.

For more information about calls to these endpoints, see [Reference: ec2messages,
ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md "systems-manager-setting-up-messageAPIs.md").

If you are using Systems Manager in an environment that supports _only_ IPv6, you must also allow outbound traffic to the following
endpoints:

- `ssm.region.api.aws`
- `ssmmessages.region.api.aws`
- `ec2messages.region.api.aws`
  For more information about dual-stack service endpoints, see [Dual stack endpoints](../../../general/latest/gr/rande.md#dual-stack-endpoints "../../../general/latest/gr/rande.md#dual-stack-endpoints") in the _AWS General Reference
  Guide_.

You must also ensure that the patch operation buckets are reachable from your
nodes, as described in [Reference: Amazon S3 buckets for patching operations](patch-operations-s3-buckets.md "patch-operations-s3-buckets.md").

###### About Amazon VPC

You can use Amazon Virtual Private Cloud (Amazon VPC) to define a virtual network in your own
logically isolated area within the AWS Cloud, known as a
_virtual private cloud (VPC)_. You can launch your
AWS resources, such as instances, into your VPC. Your VPC closely resembles a
traditional network that you might operate in your own data center, with the
benefits of using the scalable infrastructure of AWS. You can configure your VPC;
you can select its IP address range, create subnets, and configure route tables,
network gateways, and security settings. You can connect instances in your VPC
to the internet. You can connect your VPC to your own corporate data center,
making the AWS Cloud an extension of your data center. To protect the resources
in each subnet, you can use multiple layers of security, including security groups
and network access control lists. For more information, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

###### Topics

- [VPC endpoint restrictions and
  limitations](#vpc-requirements-and-limitations "#vpc-requirements-and-limitations")
- [Creating VPC endpoints for Systems Manager](#create-vpc-endpoints "#create-vpc-endpoints")
- [Create an interface VPC
  endpoint policy](#create-vpc-interface-endpoint-policies "#create-vpc-interface-endpoint-policies")

## VPC endpoint restrictions and

limitations

Before you configure VPC endpoints for Systems Manager, be aware of the following
restrictions and limitations.

###### VPC peering connections

VPC interface endpoints can be accessed through both _intra-Region_ and _inter-Region_
VPC peering connections. For more information about VPC peering connection
requests for VPC interface endpoints, see [VPC
peering connections (Quotas)](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-peering "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-peering") in the _Amazon Virtual Private Cloud User
Guide_.

VPC gateway endpoint connections can't be extended out of a VPC. Resources on the
other side of a VPC peering connection in your VPC can't use the gateway endpoint to
communicate with resources in the gateway endpoint service. For more information
about VPC peering connection requests for VPC gateway endpoints, see [VPC
endpoints (Quotas)](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-endpoints "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-endpoints") in the _Amazon Virtual Private Cloud User
Guide_

###### Incoming connections

The security group attached to the VPC endpoint must allow incoming
connections on port 443 from the private subnet of the managed instance. If
incoming connections aren't allowed, then the managed instance can't connect to
the SSM and EC2 endpoints.

###### DNS resolution

If you use a custom DNS server, you must add a conditional forwarder for any
queries to the `amazonaws.com` domain to the Amazon DNS server for
your VPC.

###### S3 buckets

Your VPC endpoint policy must allow access to at least the Amazon S3 buckets listed
in [SSM Agent communications with
AWS managed S3 buckets](ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions "ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions").

###### Note

If you use an on-premises firewall and plan to use Patch Manager, that firewall
must also allow access to the appropriate patch baseline endpoint.

###### Amazon CloudWatch Logs

If you don't allow your instances to access the internet, create a VPC
endpoint for CloudWatch Logs to use features that send logs to CloudWatch Logs. For more information
about creating an endpoint for CloudWatch Logs, see [Creating a VPC endpoint for CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md#create-VPC-endpoint-for-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md#create-VPC-endpoint-for-CloudWatchLogs") in the
_Amazon CloudWatch Logs User Guide_.

###### DNS in hybrid and multicloud environment

For information about configuring DNS to work with AWS PrivateLink endpoints in
[hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environments, see [Private
DNS for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns") in the
_Amazon VPC User Guide_. If you want to use your own DNS, you
can use Route 53 Resolver. For more information, see [Resolving DNS queries
between VPCs and your network](../../../Route53/latest/DeveloperGuide/resolver.md "../../../Route53/latest/DeveloperGuide/resolver.md") in the
_Amazon Route 53 Developer Guide_.

## Creating VPC endpoints for Systems Manager

Use the following information to create VPC interface endpoints for AWS Systems Manager.
This topic links to procedures in the _Amazon VPC User Guide_.

###### Note

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

Follow the steps in [Create an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") to create the following interface
endpoints:

- **`com.amazonaws.`region`.ssm`**
  – The endpoint for the Systems Manager service.
- **`com.amazonaws.`region`.ec2messages`**
  – Systems Manager uses this endpoint to make calls from SSM Agent to the Systems Manager
  service. Beginning with version 3.3.40.0 of SSM Agent, Systems Manager began using the
  `ssmmessages:*` endpoint (Amazon Message Gateway
  Service) whenever available instead of the `ec2messages:*` endpoint (Amazon Message Delivery
  Service).
- **`com.amazonaws.`region`.ec2`**
  – If you're using Systems Manager to create VSS-enabled snapshots, you need to
  ensure that you have an endpoint to the EC2 service. Without the EC2
  endpoint defined, a call to enumerate attached Amazon EBS volumes fails, which
  causes the Systems Manager command to fail.
- **`com.amazonaws.`region`.s3`**
  – Systems Manager uses this endpoint to update SSM Agent. Systems Manager also uses this
  endpoint if, optionally, you choose to retrieve scripts or other files
  stored in buckets or upload output logs to a bucket. If the security group
  associated with your instances restricts outbound traffic, you must add a
  rule to allow traffic to the prefix list for Amazon S3. For more information, see
  [Modify your security group](../../../vpc/latest/privatelink/vpce-gateway.md#vpc-endpoints-security "../../../vpc/latest/privatelink/vpce-gateway.md#vpc-endpoints-security") in the
  _AWS PrivateLink Guide_.
- **`com.amazonaws.`region`.ssmmessages`**
  – This endpoint is required for SSM Agent to communicate with the
  Systems Manager service, for Run Command, and if you're connecting to your instances
  through a secure data channel using Session Manager. For more information, see
  [AWS Systems Manager Session Manager](session-manager.md "session-manager.md") and
  [Reference: ec2messages,
  ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md "systems-manager-setting-up-messageAPIs.md").
- (Optional)
  **`com.amazonaws.`region`.kms`**
  – Create this endpoint if you want to use AWS Key Management Service (AWS KMS)
  encryption for Session Manager or Parameter Store parameters.
- (Optional)
  **`com.amazonaws.`region`.logs`**
  – Create this endpoint if you want to use Amazon CloudWatch Logs (CloudWatch Logs) for
  Session Manager, Run Command, or SSM Agent logs.

For information about the AWS managed S3 buckets that SSM Agent must be able to
access, see [SSM Agent communications with
AWS managed S3 buckets](ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions "ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions"). If you're using a virtual
private cloud (VPC) endpoint in your Systems Manager operations, you must provide explicit
permission in an EC2 instance profile for Systems Manager, or in a service role for non-EC2
managed nodes in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment.

## Create an interface VPC

endpoint policy

You can create policies for VPC interface endpoints for AWS Systems Manager in which you can
specify:

- The principal that can perform actions
- The actions that can be performed
- The resources that can have actions performed on them

For more information, see [Control access to
services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_Amazon VPC User Guide_.
