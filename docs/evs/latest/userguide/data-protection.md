# Data protection in Amazon EVS

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon Elastic VMware Service.
As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud.
You are responsible for maintaining control over your content that is hosted on this infrastructure, including the VMware Cloud Foundation (VCF) components.
You are also responsible for the security configuration and management tasks for the AWS services that you use.
For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq").
For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR blog post](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr") on the _AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management.
That way, each user is given only the permissions necessary to fulfill their job duties.
We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail.
  For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.

###### Note

Amazon EVS does not log user activity for non-AWS components, such as activity within your VCF environment.
These activities are logged in various VMware consoles such as vSphere and NSX Manager.
If centralized VCF logging is desired, you can configure VCF monitoring solutions such as VMware Aria Operations or VMware Tanzu Observability to achieve this result.
For more information, see [VMware Cloud Foundation with VMware Tanzu](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/working-with-workload-management-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/working-with-workload-management-admin.html") and [VMware Aria Suite Lifecyle in VMware Cloud Foundation mode](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/vrealize-suite-lifecycle-manager-in-cloud-foundation-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/vrealize-suite-lifecycle-manager-in-cloud-foundation-admin.html") in the VCF documentation.

- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint.
  For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put sensitive identifying information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field.
  This includes when you work with Amazon EVS or other AWS services using the console, API, AWS CLI, or AWS SDKs.
  Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs.
  If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Encryption at rest

Amazon EVS deploys i4i.metal EC2 instances that use transparent AES-256 encryption by default for data stored on the instance store volume.
Amazon EVS does not support EBS boot volume encryption at this time.

### Amazon EBS boot volume

Amazon EVS i4i.metal instances use an Amazon EBS boot volume.
The boot volume contains the operating system and other necessary files for the EC2 instance to boot and run.
The boot volume is not encrypted.
Amazon EVS does not support boot volume encryption at this time.
The boot volume does not contain user data from your virtual machines.

### Instance store volume

Amazon EVS i4i.metal EC2 instances come with local NVMe SSD storage, which is part of the instance’s hardware.
Amazon EVS uses NVMe instance store volumes as the disks for vSAN datastores.
The vSAN datastore holds your management and workload virtual machines after you deploy your Amazon EVS environment.

The data on NVMe instance store volumes is encrypted using an XTS-AES-256 cipher, implemented on a hardware module on the instance.
The keys that are used to encrypt data that’s written to locally-attached NVMe storage devices are per-customer, and per volume.
For more information, see [Encryption at rest](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-rest "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-rest") in the _Amazon EC2 User Guide_.

After you deploy the Amazon EVS environment, you can enable vSAN data-at-rest encryption for all data stored in the vSAN datastore, for individual virtual machines (VMs), or for individual files within VMs.
This granular control can be useful when some VMs require encryption while others do not, or when specific disks or files within a VM need to be encrypted.
For more information, see [How vSAN Data-At-Rest Encryption Works](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/how-vsan-data-at-rest-encryption-works.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/how-vsan-data-at-rest-encryption-works.html") in the VMware vSAN documentation.

## Encryption in transit

Amazon EVS does not encrypt your in-transit traffic by default.
To encrypt the data in transit that traverses Amazon EVS, you can use application layer encryption with a protocol like Transport Layer Security (TLS).
To learn about EC2 instance traffic encryption, see [Encryption in Transit](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit") in the _Amazon EC2 User Guide_.

###### Note

Nitro network encryption does not apply for the EC2 instances that Amazon EVS deploys.
Amazon EVS does not support in-transit encryption of inter-host traffic.

### In-transit encryption options for on-premises connectivity

To encrypt traffic between your on-premises data center and Amazon EVS, you can combine use of AWS Direct Connect and AWS Site-To-Site VPN with AWS Transit Gateway.
This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections.
For more information, see [Private IP AWS Site-to-Site VPN with AWS Direct Connect](../../../vpn/latest/s2svpn/private-ip-dx.md "../../../vpn/latest/s2svpn/private-ip-dx.md").

###### Note

Amazon EVS does not support connectivity via an AWS Direct Connect private virtual interface (VIF), or via an AWS Site-to-Site VPN connection that terminates directly into the underlay VPC.
Amazon EVS does support IPSec VPN termination on the NSX Edge Tier-0 or Tier-1 gateway.
For more information, see [Add an NSX IPSec VPN Service](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-1/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html "https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-1/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html") in the VMware NSX documentation.

MAC Security (MACsec) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity.
You can use AWS Direct Connect connections that support MACsec to encrypt your data from your corporate data center to the AWS Direct Connect location.
For more information, see [MAC Security in AWS Direct Connect](../../../directconnect/latest/UserGuide/MACsec.md "../../../directconnect/latest/UserGuide/MACsec.md") in the _AWS Direct Connect User Guide_.

### Encryption in transit for VMware network data

After the Amazon EVS environment deploys, you have multiple options to enforce data in transit encryption at the VMware VCF layer:

- VMware vDefend Distributed Firewall - Allows you to implement fine-grained network segmentation and enforce TLS/SSL encryption between virtual machines.
  For more information, see [Configure Security Settings for Distributed Firewall by Using the User Interface](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/security-and-compliance-configuration-for-vmware-cloud-foundation-5-2/securing-nsx-t-data-center/security-configurations-for-further-evaluation/configure-security-settings.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/security-and-compliance-configuration-for-vmware-cloud-foundation-5-2/securing-nsx-t-data-center/security-configurations-for-further-evaluation/configure-security-settings.html") in the VMware VCF documentation.
- vSAN data-in-transit encryption - Can be used to encrypt all data and metadata between hosts in your vSAN cluster.
  For more information, see [vSAN Data-In-Transit Encryption](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-in-transit-encryption.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-in-transit-encryption.html") in the VMware vSAN documentation.
- Encrypted vSphere vMotion - secures confidentiality, integrity, and authenticity of data that is transferred with vSphere vMotion.
  For more information, see [What is Encrypted vSphere vMotion](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security-8-0/virtual-machine-encryption/encrypted-vsphere-vmotion.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security-8-0/virtual-machine-encryption/encrypted-vsphere-vmotion.html") in the vSphere documentation.

## Key and secret management

During Amazon EVS environment deployment, Amazon EVS uses AWS Secrets Manager to create, encrypt, and store secrets that contain the VCF credentials needed to install and access VMware VCF management appliances, as well as the ESX root password.
Amazon EVS also deletes managed secrets on your behalf when the EVS environment is deleted.
For more information, see [What’s in a Secrets Manager secret](../../../secretsmanager/latest/userguide/whats-in-a-secret.md "../../../secretsmanager/latest/userguide/whats-in-a-secret.md") in the _AWS Secrets Manager User Guide_.

Secrets Manager uses envelope encryption with AWS KMS keys and data keys to protect each secret value.
The default AWS managed key for Secrets Manager is used unless otherwise specified.
Alternatively, you can specify a customer managed key during environment creation to encrypt your secrets.
For more information, see [Secret encryption and decryption in AWS Secrets Manager](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md") in the _AWS Secrets Manager User Guide_.

###### Note

There are additional usage charges for customer managed keys.
The default AWS managed key is provided at no cost.
For more information, see [Pricing](../../../secretsmanager/latest/userguide/intro.md#asm_pricing "../../../secretsmanager/latest/userguide/intro.md#asm_pricing") in the _AWS Secrets Manager User Guide_.

Amazon EVS does not synchronize credentials between AWS Secrets Manager and your VCF software post-deployment.
You are responsible for ensuring that the secrets associated with your Amazon EVS environment are kept in sync with the credentials in SDDC Manager to avoid VCF password expiration and loss of access to VCF software.

Amazon EVS does not rotate secrets on your behalf.
You are responsible for rotating the secrets associated with your environment.
We strongly recommend that rotate your secrets as soon as the environment is created, and implement a rotation schedule to update your secrets on a regular interval.
For more information about rotating AWS Secrets Manager secrets, see [Rotation by Lambda function](../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md "../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md") in the _AWS Secrets Manager User Guide_.
For more information about VCF password management, see [Password Management](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/4-5/administering/manage-passwords-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/4-5/administering/manage-passwords-admin.html") in the VMware Cloud Foundation documentation.

###### Important

Amazon EVS does not synchronize credentials between AWS Secrets Manager and your VCF software post-deployment.
If using AWS Secrets Manager post-deployment, you must keep credentials between AWS Secrets Manager and SDDC Manager in sync to avoid VCF password expiration issues.
You may lose access to VCF software if SDDC Manager credentials are not kept up to date.

###### Note

Amazon EVS does not provide managed rotation of secrets.

###### Note

There are costs to using a Lambda function for AWS Secrets Manager secret rotation.
For more information, see [Pricing](../../../secretsmanager/latest/userguide/intro.md#asm_pricing "../../../secretsmanager/latest/userguide/intro.md#asm_pricing") in the _AWS Secrets Manager User Guide_.

## Internetwork traffic privacy

Amazon EVS uses a customer-provided VPC to create boundaries between resources in the Amazon EVS environment and control traffic between them, your on-premises network, and the internet.
For more information about Amazon VPC security, see [Ensure internetwork traffic privacy in Amazon VPC](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md") in the _Amazon VPC User Guide_.

By default, Amazon EVS creates private VLAN subnets during environment creation that deny direct internet access.
To add another layer of security to your VPC, you can create a custom network access control list for your VPC with rules that further restrict internet connectivity.
For more information, see [Create a network ACL for your VPC](../../../vpc/latest/userguide/create-network-acl.md "../../../vpc/latest/userguide/create-network-acl.md") in the _Amazon VPC User Guide_.

###### Important

EC2 security groups do not function on elastic network interfaces that are attached to Amazon EVS VLAN subnets.
To control traffic to and from Amazon EVS VLAN subnets, you must use a network access control list.

If you are an NSX administrator, you can configure the following NSX features to secure network traffic:

- VMware vDefend Gateway Firewall - Secures the network perimeter, protecting against external threats (north-south traffic).
  For more information, see [Add a Gateway Firewall Policy and Rule](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/gateway-firewall/add-a-gateway-firewall-policy-and-rule.html "https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/gateway-firewall/add-a-gateway-firewall-policy-and-rule.html") in the VMware NSX documentation.
- VMware vDefend Distributed Firewall - Protects against attacks originating from within an internal network (east-west traffic).
  For more information, see [Add a Distributed Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/distributed-firewall/add-a-distributed-firewall.html "https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/distributed-firewall/add-a-distributed-firewall.html") in the VMware NSX documentation.
