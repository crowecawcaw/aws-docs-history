# Troubleshooting Oracle Database@AWS

Use the following sections to help troubleshoot networking issues you may encounter with
Oracle Database@AWS.

###### Topics

- [Creation of ODB network fails](#odb_troubleshooting.creating "#odb_troubleshooting.creating")
- [Connectivity issues between your VPC and ODB network
  or VM clusters](#odb_troubleshooting.vpctoodb "#odb_troubleshooting.vpctoodb")
- [Unresolvable hostnames or scannames of
  VM clusters from VPC](#odb_troubleshooting.unreshostname "#odb_troubleshooting.unreshostname")
- [Getting support for Oracle Database@AWS](#oracle-database-aws-support "#oracle-database-aws-support")

## Creation of ODB network fails

When you can't create a ODB network, the following are common causes:

**Restricted CIDR Ranges**

The ODB network uses specific CIDR ranges for the client and backup subnets. Ensure that
the CIDR ranges you've chosen for these subnets do not overlap with any restricted or
reserved IP address ranges.

The following CIDR ranges are reserved and cannot be used for the ODB network:

- Oracle cloud reserved range: 169.254.0.0/16
- Reserved Class D: 224.0.0.0 - 239.255.255.255
- Reserved Class E: 240.0.0.0 - 255.255.255.255
- Future OCI use: 100.105.0.0/16

Follow the EC2 rules for CIDR ranges as outlined in the VPC documentation. To learn
more, see [CIDR block
association restrictions](../../../vpc/latest/userguide/vpc-cidr-blocks.md#add-cidr-block-restrictions "../../../vpc/latest/userguide/vpc-cidr-blocks.md#add-cidr-block-restrictions").

Additionally, avoid overlap between specified CIDR ranges and those used for VPC
connectivity to the ODB network.

**Overlapping VPC CIDR**

The CIDR range you've specified for the ODB network should not overlap with the CIDR
ranges used by any of your existing VPCs. Overlapping CIDR ranges can cause routing
conflicts and prevent the successful creation of the ODB network. Check the CIDR ranges of
ODB peering VPCs and ensure the ODB network CIDR is unique and non-overlapping.

**Ownership of VPCs**

The ODB network and the VPC you're connecting to must be owned by the same AWS account.
If you're trying to peer the ODB network to a VPC owned by a different account, the creation
will fail. Verify that the ODB network and VPC are both owned by the same AWS
account.

**Lack of a transit gateway**

If you add a CIDR range to the ODB network peered CIDR list without attaching a transit
gateway to the VPC, the create or update operation fails. There is no requirement about
the CIDR ranges that the attachment is used for.

## Connectivity issues between your VPC and ODB network

or VM clusters

When you can't connect from your VPC to the ODB network or the VM clusters within it, the following
are common causes:

- **Verifying VPC configuration** – In the Oracle Database@AWS
  console, locate the VPC that is peered with the ODB network. Confirm the VPC ID matches the one
  shown in the ODB network details.
- **Inspecting route tables** – In the Amazon VPC
  console, find the route table attached to the subnet where your application is running.
  Check for a route with a destination CIDR that matches the client subnet CIDR of the
  ODB network. Confirm that this route points to the correct ODB network ARN. If the route is missing,
  add a new one to the ODB network's client subnet CIDR.
- **Validating peered CIDRs** – Review the
  `Peered CIDRs` section in the ODB network details. Confirm all the relevant CIDR
  blocks from your VPC are listed. If a required CIDR is missing, update the peered
  CIDRs.
- **Checking security group rules** – In the Amazon
  EC2 console, locate the security groups for resources in your VPC. Review the inbound and
  outbound rules, updating them as needed to permit the necessary traffic.
- **Confirming Availability Zones** – In the Amazon
  VPC console, identify the Availability Zone (AZ) of your subnet. Verify that the ODB network is
  also deployed in the same AZ as your subnet.
- **Avoiding multiple ODB network peering connections** –
  Check your VPC peering connections in the Oracle Database@AWS Console. Make sure you have only one
  active connection to an ODB network. If you see more than one ODB network peering, remove the extra
  ones.

## Unresolvable hostnames or scannames of

VM clusters from VPC

If the hostnames or scannames of the VM clusters are not resolvable from your VPC, configure
DNS forwarding on the VPC and the following resources to resolve DNS records hosted on the
ODB network:

- An outbound endpoint to send DNS queries to the ODB network. For more information, see
  [Configuring an outbound endpoint in an ODB network in
  Oracle Database@AWS](configuring.md#configuring.endpoint "configuring.md#configuring.endpoint").
- A resolver rule to specify the domain name of the DNS queries that the resolver
  forwards to the DNS for ODB network. For more information, see [Configuring a resolver rule in Oracle Database@AWS](configuring.md#configuring.resolver "configuring.md#configuring.resolver").

## Getting support for Oracle Database@AWS

Learn how to get information and support for Oracle Database@AWS.

### Oracle support scope and contact information

Oracle Cloud Support is the first line of support for all Oracle Database@AWS questions. To contact
support, sign in to the Oracle Cloud Infrastructure (OCI) Console, then select the life raft icon. If
you don't have a My Oracle Cloud Support account, see [My Oracle Cloud Support accounts and access](#oracle-cloud-support-accounts "#oracle-cloud-support-accounts").

Examples of issues that Oracle Support can help you with include the following:

- Database connection issues (Oracle TNS)
- Oracle Database performance issues
- Oracle Database error resolution
- Networking issues related to communications with the OCI tenancy associated with the service
- Quota (limits) increases to receive more capacity (for more information, see
  [Requesting a Limit Increase for Database Resources](https://docs.oracle.com/iaas/Content/multicloud/multicloud-limits-increase.htm "https://docs.oracle.com/iaas/Content/multicloud/multicloud-limits-increase.htm"))
- Scaling to add more compute and storage capacity to your Oracle Database infrastructure
- New generation hardware upgrades
- Billing issues related to your AWS Marketplace charges

If you need to contact Oracle Support outside of the OCI Console, tell your Oracle
Support agent that your issue is related to Oracle Database@AWS. This is because requests for this
service are handled by an OCI support team that specializes with these deployments.

###### Contacting Oracle support by phone

1. Call **1-800-223-1711**. If you are outside of
   the United States, visit [Oracle Support Contacts Global Directory](https://www.oracle.com/support/contact.html "https://www.oracle.com/support/contact.html") to find contact
   information for your country or region.
2. Choose option "2" to open a new Service Request (SR).
3. Choose option "4" for "unsure".
4. Let the agent know that you have an issue with your multicloud system, and the
   name of the product. An internal Service Request will be opened on your behalf
   and an OCI support engineer will contact you directly.

You can also submit a question to the Multicloud forum in Oracle's [Cloud Customer Connect](https://community.oracle.com/customerconnect/categories/oracle-cloud-infrastructure-and-platform "https://community.oracle.com/customerconnect/categories/oracle-cloud-infrastructure-and-platform") community. This option is available to all
customers.

### My Oracle Cloud Support accounts and access

To create My Oracle Cloud Support service request tickets, the administrator of your
organization's Oracle Database@AWS service must approve your request. If you're the Oracle Database@AWS
administrator, complete the My Oracle Cloud Support onboarding instructions included in
the Oracle Database@AWS service activation email.

You can find instructions for onboarding with My Oracle Cloud Support in the following topics:

- [Configuring Your Oracle Support Account](https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm "https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm")
- [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm "https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm")

For instructions on approving users to open My Oracle Cloud Support support requests,
see [Administrator Tasks for Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm#usingsupport_administrators "https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm#usingsupport_administrators").

### AWS Support scope and contact information

AWS Support is your first line of support for all AWS-related issues and questions.
Create an AWS Support case for your issue, as you do with other AWS services. The
AWS Support team collaborates with OCI Support as needed.

Examples of Oracle Database@AWS issues that AWS Support can help you with include the following:

- Virtual networking issues including those involving network address
  translation (NAT), firewalls, DNS and traffic management, and AWS
  subnets
- Bastion and virtual machine (VM) issues including database host connection,
  software installation, latency, and host performance
- Exadata VM cluster metrics reporting within Amazon CloudWatch
- Billing issues related to AWS services

For information on AWS Support, see [Getting started with
AWS Support](../../../awssupport/latest/user/getting-started.md "../../../awssupport/latest/user/getting-started.md").

### Oracle service level agreements

If you have questions about Oracle Database@AWS Service Level Agreements (SLAs), or want to request
service credits for SLA breaches, contact your Oracle account manager. See [Service Level Agreements](https://docs.oracle.com/iaas/Content/General/Reference/slastatement.htm "https://docs.oracle.com/iaas/Content/General/Reference/slastatement.htm") for more information.
