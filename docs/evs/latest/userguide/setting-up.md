# Setting up Amazon Elastic VMware Service

To use Amazon EVS, you will need to configure other AWS services, as well as set up your environment to meet VMware Cloud Foundation (VCF) requirements.
For a summary checklist of deployment prerequisites, see [Amazon EVS deployment prerequisite checklist](evs-deployment-prereq-checklist.md "evs-deployment-prereq-checklist.md").

###### Topics

- [Sign up for AWS](#setting-up-aws-sign-up "#setting-up-aws-sign-up")
- [Create an IAM user](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [Create an IAM role to delegate Amazon EVS permission to an IAM user](#setting-up-create-iam-role "#setting-up-create-iam-role")
- [Sign up for an AWS Business, AWS Enterprise On-Ramp, or AWS Enterprise Support plan](#setting-up-aws-business-support "#setting-up-aws-business-support")
- [Check quotas](#check-quotas "#check-quotas")
- [Plan VPC CIDR sizes](#vpc-planning "#vpc-planning")
- [Create a VPC with subnets](#vpc-create "#vpc-create")
- [Configure the VPC main route table](#vpc-main-rt "#vpc-main-rt")
- [Configure your VPC’s DHCP option set](#vpc-dhcp "#vpc-dhcp")
- [Create and configure VPC Route Server infrastructure](#route-server "#route-server")
- [Create a transit gateway for on-premises connectivity](#transit-gateway "#transit-gateway")
- [Create an Amazon EC2 Capacity Reservation](#ec2-future-capacity-reservation "#ec2-future-capacity-reservation")
- [Set up the AWS CLI](#set-up-cli "#set-up-cli")
- [Create an Amazon EC2 key pair](#create-ec2-key-pair "#create-ec2-key-pair")
- [Prepare your environment for VMware Cloud Foundation (VCF)](#setting-up-vcf "#setting-up-vcf")
- [Acquire VCF license keys](#setting-up-vcf-licensing "#setting-up-vcf-licensing")
- [VMware HCX prerequisites](#hcx-prereqs "#hcx-prereqs")
- [Amazon EVS deployment prerequisite checklist](evs-deployment-prereq-checklist.md "evs-deployment-prereq-checklist.md")

## Sign up for AWS

If you don’t have an AWS account, complete the following steps to create one.

1. Open https://portal.aws.amazon.com/billing/signup.
2. Follow the online instructions.

## Create an IAM user

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

###### Note

We strongly recommend that you adhere to the best practice of using the `Administrator` IAM user below and securely lock away the root user credentials. Sign in as the root user only to perform a few [account and service management tasks](../../../general/latest/gr/aws_tasks-that-require-root.md "../../../general/latest/gr/aws_tasks-that-require-root.md"). 2. In the navigation pane, choose **Users** and then choose **Create user**. 3. For **User name**, enter `Administrator`. 4. Select the check box next to **AWS Management Console access**. Then select **Custom password**, and then enter your new password in the text box. 5. (Optional) By default, AWS requires the new user to create a new password when first signing in. You can clear the check box next to **User must create a new password at next sign-in** to allow the new user to reset their password after they sign in. 6. Choose **Next: Permissions**. 7. Under **Set permissions**, choose **Add user to group**. 8. Choose **Create group**. 9. In the **Create group** dialog box, for **Group name** enter `Administrators`. 10. Choose **Filter policies**, and then select **AWS managed -job function** to filter the table contents. 11. In the policy list, select the check box for **AdministratorAccess**. Then choose **Create group**.

###### Note

You must activate IAM user and role access to Billing before you can use the `AdministratorAccess` permissions to access the AWS Billing and Cost Management console. To do this, follow the instructions in [step 1 of the tutorial about delegating access to the billing console](../../../IAM/latest/UserGuide/tutorial_billing.md "../../../IAM/latest/UserGuide/tutorial_billing.md"). 12. Back in the list of groups, select the check box for your new group. Choose **Refresh** if necessary to see the group in the list. 13. Choose **Next: Tags**. 14. (Optional) Add metadata to the user by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM Entities](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 15. Choose **Next: Review** to see the list of group memberships to be added to the new user. When you are ready to proceed, choose **Create user**.

You can use this same process to create more groups and users and to give your users access to your AWS account resources. To learn about using policies that restrict user permissions to specific AWS resources, see [Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") and [Example Policies](../../../IAM/latest/UserGuide/access_policies_examples.md "../../../IAM/latest/UserGuide/access_policies_examples.md").

## Create an IAM role to delegate Amazon EVS permission to an IAM user

You can use roles to delegate access to your AWS resources.
With IAM roles, you can establish trust relationships between your trusting account and other AWS trusted accounts.
The trusting account owns the resource to be accessed, and the trusted account contains the users who need access to the resource.

After you create the trust relationship, an IAM user or an application from the trusted account can use the AWS Security Token Service (AWS STS) `AssumeRole` API operation.
This operation provides temporary security credentials that enable access to AWS resources in your account.
For more information, see [Create a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _AWS Identity and Access Management User Guide_.

Follow these steps to create an IAM role with a permissions policy that allows access to Amazon EVS operations.

###### Note

Amazon EVS does not support the use of an instance profile to pass an IAM role to an EC2 instance.

IAM console

1. Go the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. On the left menu, choose **Policies**.
3. Choose **Create policy**.
4. In the policy editor, create a permissions policy that enables Amazon EVS operations.
   For an example policy, see [Create and manage an Amazon EVS environment](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env "security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env").
   To view all available Amazon EVS actions, resources, and condition keys, see [Actions](../../../service-authorization/latest/reference/list_amazonelasticvmwareservice.md "../../../service-authorization/latest/reference/list_amazonelasticvmwareservice.md") in the _Service Authorization Reference_.
5. Choose **Next**.
6. Under **Policy name**, enter a meaningful policy name to identify this policy.
7. Review the permissions defined in this policy.
8. (Optional) Add tags to help identify, organize, or search for this resource.
9. Choose **Create policy**.
10. On the left menu, choose **Roles**.
11. Choose **Create role**.
12. For **Trusted entity type**, choose AWS account.
13. Under **An AWS account** , specify the account that you want to perform Amazon EVS actions and choose **Next**.
14. On the **Add permissions** page, select the permissions policy that you previously created and choose **Next**.
15. Under **Role name**, enter a meaningful name to identify this role.
16. Review the trust policy and ensure that the correct AWS account is listed as the principal.
17. (Optional) Add tags to help identify, organize, or search for this resource.
18. Choose **Create role**.

AWS CLI

1. Copy the following contents to a trust policy JSON file.
   For the principal ARN, replace the example AWS account ID and `service-user` name with your own AWS account ID and IAM user name.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/service-user"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

2. Create the role.
   Replace `evs-environment-role-trust-policy.json` with your trust policy file name.

```
aws iam create-role \
  --role-name myAmazonEVSEnvironmentRole \
  --assume-role-policy-document file://"evs-environment-role-trust-policy.json"
```

3. Create a permissions policy that enables Amazon EVS operations and attach the policy to the role.
   Replace `myAmazonEVSEnvironmentRole` with your role name.
   For an example policy, see [Create and manage an Amazon EVS environment](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env "security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env").
   To view all available Amazon EVS actions, resources, and condition keys, see [Actions](../../../service-authorization/latest/reference/list_amazonelasticvmwareservice.md "../../../service-authorization/latest/reference/list_amazonelasticvmwareservice.md") in the _Service Authorization Reference_.

```
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEVSEnvironmentPolicy \
  --role-name myAmazonEVSEnvironmentRole
```

## Sign up for an AWS Business, AWS Enterprise On-Ramp, or AWS Enterprise Support plan

Amazon EVS requires that customers are enrolled in an AWS Business, AWS Enterprise On-Ramp, or AWS Enterprise Support plan to receive continuous access to technical support and architectural guidance.
AWS Business Support is the minimum AWS Support tier that meets Amazon EVS requirements.
If you have business-critical workloads, we recommend enrolling in AWS Enterprise On-Ramp or AWS Enterprise Support plans.
For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans "https://aws.amazon.com/premiumsupport/plans").

###### Important

Amazon EVS environment creation fails if you do not sign up for an AWS Business, AWS Enterprise On-Ramp, or an AWS Enterprise Support plan.

## Check quotas

To enable Amazon EVS environment creation, ensure that your account has the required minimum account-level quotas.
For more information, see [Amazon EVS service quotas](service-quotas-evs.md "service-quotas-evs.md").

###### Important

Amazon EVS environment creation fails if the host count per EVS environment quota value is not at least 4.

## Plan VPC CIDR sizes

When you create an Amazon EVS environment, you are required to specify a VPC CIDR block.
The VPC CIDR block cannot be changed after the environment is created, and will need to have enough space reserved to accommodate the required EVS subnets and hosts that Amazon EVS creates during environment deployment.
As a result, it is critical to carefully plan out the CIDR block size, taking into account Amazon EVS requirements and your future scaling needs prior to deployment.
Amazon EVS requires a VPC CIDR block with a minimum size of /22 netmask to allow sufficient space for the required EVS subnets and hosts.
For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets "architecture.md#evs-subnets").

###### Important

Ensure that you have sufficient IP address space for both your VPC subnet and the VLAN subnets that Amazon EVS creates for VCF appliances.
The VPC CIDR block must have a minimum size of /22 netmask to allow sufficient space for the required EVS subnets and hosts.

###### Note

Amazon EVS does not support IPv6 at this time.

## Create a VPC with subnets

Amazon EVS deploys your environment into a VPC that you provide.
This VPC must contain a subnet for Amazon EVS service access ([Service access subnet](concepts.md#concepts-service-access-subnet "concepts.md#concepts-service-access-subnet")).
For steps to create a VPC with subnets for Amazon EVS, see [Create a VPC with subnets and route tables](getting-started.md#getting-started-create-vpc "getting-started.md#getting-started-create-vpc").

## Configure the VPC main route table

Amazon EVS VLAN subnets are implicitly associated to the VPC main route table.
To enable connectivity to dependent services such as DNS or on-premises systems for successful environment deployment, you must configure the main route table to allow traffic to these systems.
For more information, see [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](getting-started.md#getting-started-associate-vlans "getting-started.md#getting-started-associate-vlans").

###### Important

Amazon EVS supports the use of a custom route table only after the Amazon EVS environment is created.
Custom route tables should not be used during Amazon EVS environment creation, as this may result in connectivity issues.

### Gateway route requirements

Configure routes for these gateway types based on your connectivity requirements:

- **NAT gateway (NGW)**
  - Optional for outbound-only internet access.
  - Must be in a public subnet with internet gateway access.
  - Add routes from private subnets and EVS VLAN subnets to the NAT gateway.
  - For more information, see [Work with NAT gateways](../../../vpc/latest/userguide/nat-gateway-working-with.md "../../../vpc/latest/userguide/nat-gateway-working-with.md") in the _Amazon VPC User Guide_.

- **Transit gateway (TGW)**
  - Required for on-premises connectivity via both AWS Direct Connect and AWS Site-to-Site VPN.
  - Add routes for on-premises network ranges.
  - Configure route propagation if using BGP.
  - For more information, see [Transit gateways in Amazon VPC Transit Gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in the _Amazon VPC User Guide_.

### Best practices

- Document all route table configurations.
- Use consistent naming conventions.
- Regularly audit your route tables.
- Test connectivity after making changes.
- Back up route table configurations.
- Monitor route health and propagation.

For more information about working with route tables, see [Configure route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon VPC User Guide_.

## Configure your VPC’s DHCP option set

###### Important

Your environment deployment fails if you don’t meet these Amazon EVS requirements:

- Include a primary DNS server IP address and a secondary DNS server IP address in the DHCP option set.
- Include a DNS forward lookup zone with A records for each VCF management appliance and Amazon EVS host in your deployment.
- Include a DNS reverse lookup zone with PTR records for each VCF management appliance and Amazon EVS host in your deployment.
- Configure the VPC’s main route table to ensure a route to your DNS servers exist.
- Ensure that your domain name registration is valid and unexpired, and no duplicate hostnames or IP addresses exist.
- Configure your security groups and network access control lists (ACLs) to allow Amazon EVS to communicate with:
  - DNS servers over TCP/UDP port 53.
  - Host management VLAN subnet over HTTPS and SSH.
  - Management VLAN subnet over HTTPS and SSH.

For more information, see [Configure DNS and NTP servers using the VPC DHCP option set](getting-started.md#getting-started-config-dns-ntp-dhcp "getting-started.md#getting-started-config-dns-ntp-dhcp").

## Create and configure VPC Route Server infrastructure

Amazon EVS uses Amazon VPC Route Server to to enable BGP-based dynamic routing to your VPC underlay network.
You must specify a route server that shares routes to at least two route server endpoints in the service access subnet.
The peer ASN configured on the route server peers must match, and the peer IP addresses must be unique.

###### Important

Your environment deployment fails if you don’t meet these Amazon EVS requirements for VPC Route Server configuration:

- You must configure at least two route server endpoints in the service access subnet.
- When configuring Border Gateway Protocol (BGP) for the Tier-0 gateway, the VPC Route Server peer ASN value must match the NSX Edge peer ASN value.
- When creating the two route server peers, you must use a unique IP address from the NSX uplink VLAN for each endpoint.
  These two IP addresses will be assigned to the NSX edges during Amazon EVS environment deployment.
- When enabling Route Server propagation, you must ensure that all route tables being propagated have at least one explicit subnet association.
  BGP route advertisement fails if propagated route tables do not have an explicit subnet association.

###### Note

For Route Server peer liveness detection, Amazon EVS only supports the default BGP keepalive mechanism.
Amazon EVS does not support multi-hop Bidirectional Forwarding Detection (BFD).

### Prerequisites

Before you begin, you need:

- A VPC subnet for your route server.
- IAM permissions to manage VPC Route Server resources.
- A BGP ASN value for route server (Amazon-side ASN).
  This value must be in the range of 1-4294967295.
- A peer ASN to peer your route server with the NSX Tier-0 gateway.
  Peer ASN values entered in the route server and NSX Tier-0 gateway must match.
  The default ASN for an NSX Edge appliance is 65000.

### Steps

For steps to set up VPC Route Server, see the [Route Server get started tutorial](../../../vpc/latest/userguide/route-server-tutorial.md "../../../vpc/latest/userguide/route-server-tutorial.md").

###### Note

If you are using a NAT gateway or a transit gateway, ensure that your route server is configured correctly to propagate NSX routes to the VPC route table(s).

###### Note

We recommend that you enable persistent routes for the route server instance with a persist duration between 1-5 minutes.
If enabled, routes will be preserved in the route server’s routing database even if all BGP sessions end.

###### Note

BGP connectivity status will be down until the Amazon EVS environment is deployed and operational.

## Create a transit gateway for on-premises connectivity

You can configure connectivity for your on-premises data center to your AWS infrastructure using Direct Connect with an associated transit gateway, or using an AWS Site-to-Site VPN attachment to a transit gateway.
For more information, see [Configure on-premises network connectivity (optional)](getting-started.md#getting-started-connect-on-prem "getting-started.md#getting-started-connect-on-prem").

## Create an Amazon EC2 Capacity Reservation

Amazon EVS launches Amazon EC2 i4i.metal instances that represent ESX hosts in your Amazon EVS environment.
To ensure that you have sufficient i4i.metal instance capacity available when you need it, we recommend that you request an Amazon EC2 Capacity Reservation.
You can create a Capacity Reservation at any time, and you can choose when it starts.
You can request a Capacity Reservation for immediate use, or you can request a Capacity Reservation for a future date.
For more information, see [Reserve compute capacity with EC2 On-Demand Capacity Reservations](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") in the _Amazon Elastic Compute Cloud User Guide_.

## Set up the AWS CLI

The AWS CLI is a command line tool for working with AWS services, including Amazon EVS. It is also used to authenticate IAM users or roles for access to the Amazon EVS virtualization environment and other AWS resources from your local machine.
To provision AWS resources from the command line, you need to obtain an AWS access key ID and secret key to use in the command line.
Then you need to configure these credentials in the AWS CLI.
For more information, see [Set up the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md") in the _AWS Command Line Interface User Guide for Version 2_.

## Create an Amazon EC2 key pair

Amazon EVS uses an Amazon EC2 key pair that you provide during environment creation to connect to your hosts.
To create a key pair, follow the steps on [Create a key pair for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/create-key-pairs.md "../../../AWSEC2/latest/UserGuide/create-key-pairs.md") in the Amazon Elastic Compute Cloud User Guide.

## Prepare your environment for VMware Cloud Foundation (VCF)

Before you deploy your Amazon EVS environment, your environment must meet VMware Cloud Foundation (VCF) infrastructure requirements.
For detailed VCF prerequisites, see the [Planning and Preparation Workbook](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/planning-and-preparation-workbook-5-2.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/planning-and-preparation-workbook-5-2.html") in the VMware Cloud Foundation product documentation.

You should also familiarize yourself with VCF 5.2.x requirements. See the [VCF 5.2.x release notes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html") for relevant release information.

###### Note

For information about VCF versions provided by Amazon EVS, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md "versions-provided.md").

## Acquire VCF license keys

To use Amazon EVS, you need to provide a VCF solution key and a vSAN license key.
The VCF solution key must have at least 256 cores.
The vSAN license key must have at least 110 TiB of vSAN capacity.
For more information about VCF licenses, see [Managing License Keys in VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/license-management-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/license-management-admin.html") in the _VMware Cloud Foundation Administration Guide_.

###### Important

Use the SDDC Manager user interface to manage VCF solution and vSAN license keys.
Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly.

###### Note

Your VCF license will be available to Amazon EVS across all AWS Regions for license compliance.
Amazon EVS does not validate license keys.
To validate license keys, visit [Broadcom support](https://support.broadcom.com/web/ecx "https://support.broadcom.com/web/ecx").

## VMware HCX prerequisites

You can use VMware HCX to migrate your existing VMware-based workloads to Amazon EVS.
Before you use VMware HCX with Amazon EVS, make sure that the following prerequiste tasks have been completed.

###### Note

VMware HCX is not installed in the EVS environment by default.

- Before you can use VMware HCX with Amazon EVS, minimum network underlay requirements must be met.
  For more information, see [Network Underlay Minimum Requirements](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/preparing-for-hcx-installations/network-underlay-minimum-requirements.html "https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/preparing-for-hcx-installations/network-underlay-minimum-requirements.html") in the _VMware HCX User Guide_.
- Confirm that VMware NSX is installed and configured in the environment.
  For more information, see the [VMware NSX Installation Guide](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide.html "https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide.html").
- Ensure that VMware HCX is activated and installed in the environment.
  For more information about activating and installing VMware HCX, see [About Getting Started with VMware HCX](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/getting-started-with-vmware-hcx-4-11/about-getting-started-with-vmware-hcx.html "https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/getting-started-with-vmware-hcx-4-11/about-getting-started-with-vmware-hcx.html") in the _Getting Started with VMware HCX Guide_.
- If you need HCX internet connectivity, you must complete the following prerequisite tasks:
  - Ensure that your IPAM quota for Amazon-provided contiguous public IPv4 CIDR block netmask length is /28 or greater.

  ###### Important

  For HCX internet connectivity, Amazon EVS requires use of IPv4 CIDR block from a public IPAM pool with a netmask length of /28 or greater.
  Use of any CIDR block with a netmask length smaller than /28 will result in HCX connectivity issues.
  For more information about increasing IPAM quotas, see [Quotas for your IPAM](../../../vpc/latest/ipam/quotas-ipam.md "../../../vpc/latest/ipam/quotas-ipam.md").
  - Create an IPAM and a public IPv4 IPAM pool with CIDR that has a a minimum netmask length of /28.
  - Allocate at least two Elastic IP addresses (EIPs) from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances.
    Allocate an additional Elastic IP address for each HCX network appliance that you need to deploy.
  - Add the public IPv4 CIDR block as an additional CIDR to your VPC.

For more information about HCX setup, see [Choose your HCX connectivity option](getting-started.md#hcx-connectivity-choice "getting-started.md#hcx-connectivity-choice") and [HCX connectivity options](migrate-evs-hcx.md#migrate-evs-hcx-connectivity "migrate-evs-hcx.md#migrate-evs-hcx-connectivity").
