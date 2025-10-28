# Prerequisites

This tutorial assumes you already have the following:

###### Note

AWS Managed Microsoft AD does not support trust with [Single label domains](https://support.microsoft.com/en-us/help/2269810/microsoft-support-for-single-label-domains "https://support.microsoft.com/en-us/help/2269810/microsoft-support-for-single-label-domains").

- An AWS Managed Microsoft AD directory created on AWS. If you need help doing this, see [Getting started with AWS Managed Microsoft AD](ms_ad_getting_started.md "ms_ad_getting_started.md").
- An EC2 instance running Windows added to that AWS Managed Microsoft AD. If you need help doing this, see [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD
  Active Directory](launching_instance.md "launching_instance.md").

###### Important

The admin account for your AWS Managed Microsoft AD must have administrative access to this
instance.

- The following Windows Server tools installed on that instance:

      + AD DS and AD LDS Tools
      + DNS

  If you need help doing this, see [Installing Active Directory Administration
  Tools for AWS Managed Microsoft AD](ms_ad_install_ad_tools.md "ms_ad_install_ad_tools.md").

- A self-managed (on-premises) Microsoft Active Directory

You must have administrative access to this directory. The same Windows Server
tools as listed above must also be available for this directory.

- An active connection between your self-managed network and the VPC containing your AWS Managed Microsoft AD.
  If you need help doing this, see [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-vpc-connectivity-options.md").
- A correctly set local security policy. Check `Local Security Policy > Local Policies > Security Options > Network access: Named Pipes that can be accessed anonymously`
  and ensure that it contains at least the following three named pipes:
  - netlogon
  - samr
  - lsarpc

- The NetBIOS and domain names must be unique and cannot be the same to establish a trust relationship
  For more information about the prerequisites for creating a trust relationship, see [Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](ms_ad_setup_trust.md "ms_ad_setup_trust.md").

## Tutorial configuration

For this tutorial, we've already created a AWS Managed Microsoft AD and a self-managed domain. The self-managed network is connected to the AWS Managed Microsoft AD's VPC. Following are the properties of the two directories:

### AWS Managed Microsoft AD running on AWS

- Domain name (FQDN): MyManagedAD.example.com
- NetBIOS name: MyManagedAD
- DNS Addresses: 10.0.10.246, 10.0.20.121
- VPC CIDR: 10.0.0.0/16

The AWS Managed Microsoft AD resides in VPC ID: vpc-12345678.

### Self-managed or AWS Managed Microsoft AD domain

- Domain name (FQDN):
  corp.example.com
- NetBIOS name: CORP
- DNS Addresses: 172.16.10.153
- Self-managed CIDR: 172.16.0.0/16

**Next Step**

[Step 1: Prepare your
self-managed AD Domain](ms_ad_tutorial_setup_trust_prepare_onprem.md "ms_ad_tutorial_setup_trust_prepare_onprem.md")
