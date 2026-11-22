

# Prepare your AWS account

Before you build the network for Amazon Elastic VMware Service, complete these one-time tasks in the AWS account where you plan to deploy. The tasks are the same for both deployment modes. After you finish, continue with [Build the network foundation](network-foundation.md).

Before you begin, review your network plan. For the VPC CIDR block size and the VLAN subnets, see [Plan your VPC and VLAN subnets](plan-network-sizing.md). For a full list of requirements, see [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md).

Complete the following tasks in order. The sections after this list describe each task.

1.  [Sign up for an AWS account](#sign-up-for-aws) 

1.  [Sign up for a supported AWS Support plan](#setting-up-aws-business-support) 

1.  [Check quotas](#check-quotas) 

1.  [Reserve Amazon EC2 capacity](#ec2-future-capacity-reservation) 

1.  [Set up the AWS CLI](#set-up-cli) 

1.  [Create an Amazon EC2 key pair](#create-ec2-key-pair) 

1.  [Create an IAM role for Amazon EVS administrators](#setting-up-iam) 

1.  [Prepare for VMware Cloud Foundation](#setting-up-vcf) 

1.  [Acquire a VCF subscription and license keys](#setting-up-vcf-licensing) 

When you have completed these tasks, your account is ready for Amazon EVS. Next, build the network. For instructions, see [Build the network foundation](network-foundation.md).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the * AWS Account Management Reference Guide*.

You must create the VPC, the subnets, and the Amazon EVS environment in the same AWS account. Amazon EVS does not support cross-account sharing of VPC subnets or Amazon EVS environments.

## Sign up for a supported AWS Support plan
<a name="setting-up-aws-business-support"></a>

Amazon EVS requires that you enroll in an AWS Business, AWS Enterprise On-Ramp, or AWS Enterprise Support plan. These plans give you continuous access to technical support and architectural guidance. AWS Business Support is the minimum AWS Support tier that meets Amazon EVS requirements. If you run business-critical workloads, we recommend AWS Enterprise On-Ramp or AWS Enterprise Support, because these plans add faster response times and architectural guidance. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans).

**Important**  
Amazon EVS environment creation fails if you do not sign up for an AWS Business, AWS Enterprise On-Ramp, or AWS Enterprise Support plan.

## Check quotas
<a name="check-quotas"></a>

Your account must have the required minimum account-level quotas before you create an environment. For the quotas and how to request an increase, see [Service quotas for Amazon EVS](service-quotas-evs.md).

**Important**  
Amazon EVS environment creation fails if the host count per environment quota is too low for your VCF deployment topology. For host count requirements, see the Broadcom documentation for [VCF 9.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html) or [VCF 5.2.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2.html).

## Reserve Amazon EC2 capacity
<a name="ec2-future-capacity-reservation"></a>

Amazon EVS launches Amazon EC2 bare metal instances that become the ESX hosts in your environment. We recommend that you request an Amazon EC2 Capacity Reservation, so that capacity is available when you add hosts. You can request a Capacity Reservation for immediate use or for a future date. For more information, see [Reserve capacity for hosts](plan-capacity.md) and [Reserve compute capacity with EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.

## Set up the AWS CLI
<a name="set-up-cli"></a>

The AWS Command Line Interface (AWS CLI) is a command line tool for working with AWS services, including Amazon EVS. You also use it to authenticate IAM users or roles for access to Amazon EVS and other AWS resources from your local machine. To use the AWS CLI, you get an access key ID and a secret access key, and then you configure these credentials in the AWS CLI. For instructions, see [Set up the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) in the * AWS Command Line Interface User Guide for Version 2*.

## Create an Amazon EC2 key pair
<a name="create-ec2-key-pair"></a>

Amazon EVS uses an Amazon EC2 key pair to connect to your hosts. You provide it when you create the environment in EVS-deployed mode, and when you add a host in Self-deployed mode. To create a key pair, see [Create a key pair for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) in the *Amazon EC2 User Guide*.

## Create an IAM role for Amazon EVS administrators
<a name="setting-up-iam"></a>

Create an IAM role with a permissions policy that allows Amazon EVS operations, and let your administrators assume it. For instructions, see [Create an IAM role for Amazon EVS administrators](setup-iam-role.md).

## Prepare for VMware Cloud Foundation
<a name="setting-up-vcf"></a>

Your environment must meet the VMware Cloud Foundation (VCF) infrastructure requirements for the VCF version that you deploy. For the VCF versions that Amazon EVS provides in each mode, see [Supported VCF versions and instance types](versions-provided.md). For the VCF planning requirements, see the Planning and Preparation Workbook in the Broadcom documentation for [VCF 9.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/planning-and-preparation.html) or [VCF 5.2.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/planning-and-preparation-workbook-5-2.html).

If you plan to use diskless hosts, which have no local storage, you must provide external storage. The storage must be in the same VPC and Availability Zone as your environment. Diskless hosts are available only with VCF 9.x in Self-deployed mode. For the VCF versions and instance types that support diskless hosts, see [Supported VCF versions and instance types](versions-provided.md). For storage options, requirements, and sizing, see [External storage options for diskless hosts](external-storage-diskless.md).

If you plan to migrate workloads with VMware HCX, see [Plan HCX connectivity](plan-hcx-connectivity.md) before you build the network. HCX internet connectivity needs a public IPAM pool and Elastic IP addresses that you prepare in advance.

## Acquire a VCF subscription and license keys
<a name="setting-up-vcf-licensing"></a>

You bring your own VCF subscription to run VCF on Amazon EVS, in both deployment modes. When and where you provide the license keys depends on the deployment mode and the instance type. For the license requirements and the steps for each mode, see [VCF licensing](vcf-license-mgmt.md).

**Topics**