# AMS Managed Active Directory

AMS is now offering a new service called Managed Active Directory (aka Managed AD) that allows AMS to take care
of your Active Directory (AD) infrastructure operations, while keeping you in control of your Active Directory administration.

AMS support for Managed AD is similar to AMS support for the Amazon Relational Database Service (Amazon RDS). In both cases, AWS (including AMS) supports the creation and management of the
infrastructure running the service, while you perform access control and all administration functions. This model has the following advantages:

- Limits security risks: AWS and AMS don't need administrative privileges to your domain.
- Direct integrations: You can use your current authorization model and integrate it with AD
  without needing to interface with AMS.
  **Notes**:

- Neither AMS nor you will have access to your Managed AD domain controllers, so no software
  can be installed on the domain controllers. This is important because third-party
  solutions that require software to be installed on domain controllers is not allowed.

Access works like this:

    + AWS Directory Service team: Has access to domain controllers.
    + AMS: Has access to Directory Service APIs to perform certain actions on the domain. These
     actions include taking AD snapshots, changing AD schema, and others actions.
    + You: Have access to the domain (AD) for creating users, groups, and so on.

- We recommend that you perform a proof of concept on Managed AD before migrating your corporate AD, because not all functionality
  from a traditional AD environment is available in a Managed AD environment.
- AMS will not manage or provide guidance on your AD management. For example, AMS will not provide guidance on Organizational Unit structure,
  group policy structure, AD user naming conventions, and so forth.
  It works like this:

1. AMS onboards a new AWS account for you, separate from and in addition to your AMS account, and
   provisions an Active Directory (AD) environment through AWS Directory Service (see also
   [What Is AWS Directory Service?](../../../directoryservice/latest/admin-guide/what_is.md "../../../directoryservice/latest/admin-guide/what_is.md")).

The following is the information a systems integrator would need to gather from you in order for AMS to on board Managed AD:

    * Account information




    	+ Account ID of the AWS account that was created for your AMS-Managed AD: AWS account number
    	+ Region to onboard your Managed AD to: AWS Region
    * Managed Active Directory information:




    	+ Microsoft AD Edition: Standard/Enterprise. AWS Microsoft AD (Standard Edition) includes 1 GB of directory object storage. This
    	 capacity can support up to 5,000 users or 30,000 directory objects, including users, groups, and computers. AWS Microsoft AD (Enterprise
    	 Edition) includes 17 GB of directory object storage, which can support up to 100,000 users or 500,000 objects.


    	For more information, see
    	 [AWS Directory Service FAQs](https://aws.amazon.com/directoryservice/faqs/ "https://aws.amazon.com/directoryservice/faqs/").
    	+ Domain FQDN: The FQDN for your AMS Managed AD domain.
    	+ Domain NetBIOS name: The NetBIOS name for your AMS Managed AD domain.
    	+ Account numbers of AMS-standard accounts you would like Managed AD integration to (AMS configures a one way trust from the
    	 AMS-standard account's AD to the Managed AD)
    	+ Are Active Directory Schema modifications required and if so, what modifications?
    	+ By default, two domain controllers are provisioned. Do you require more? If so, how many do you require and for what reason?
    * Networking for Managed Active Directory information:




    	+ Managed AD VPC CIDR for domain controllers (a CIDR in your private subnet range for the Managed AD domain controllers):




    		- Subnet CIDR 1 for domain controllers: [your CIDR, needs to be part of AMS Managed AD VPC CIDR]
    		- Subnet CIDR 2 for domain controllers: [your CIDR, needs to be part of AMS Managed AD VPC CIDR]
    	For example:




    		- Managed AD VPC CIDR: 192.168.0.0/16
    		- CIDR 1 for domain controllers: 192.168.1.0/24
    		- CIDR 2 for domain controllers: 192.168.2.0/24
    	To avoid IP address conflicts, be sure that the Managed AD VPC CIDR you specify does not conflict with any other private subnet
    	 CIDR you are using in your corporate network.
    	+ VPN Technology (optional): [Direct Connect/Direct Connect and VPN]




    		- Your gateway's BGP Autonomous System Number (ASN): [Customer-provided ASN]
    		- The Internet-routable IP address for your gateway's outside interface, the address must be static: [Customer
    		 Provided IP Address]
    		- Whether or not your VPN connection requires static routes: [yes/no]

2. AMS provides you with the Admin account password for the AD environment and asks you to reset the password so
   AMS engineers can no longer access your AD environment.
3. To reset the Admin account password, connect to your Active Directory environment using Active Directory Users and Computers (ADUC).
   ADUC and other Remote Server Administration Tools (RSAT) should be installed and run on Administrative hosts provisioned by you
   on non-AMS infrastructure. Microsoft has best practices for securing such administrative hosts. For information, see
   [Implementing Secure Administrative Hosts](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts"). You manage your Active Directory environment using these Administrative hosts.
4. In daily operations, AMS manages the AWS account up to the AWS Directory Service side of things; for example, VPC configuration,
   AD backups, AD trust creation and deletion, and so forth. You use, and manage, your AD environment; for example, user creation,
   group creation, group policy creation, and so forth.
   For the most recent RACI table, see the "Roles and Responsibilities" section in the
   See [Service description](../userguide/ams-sd.md "../userguide/ams-sd.md").
