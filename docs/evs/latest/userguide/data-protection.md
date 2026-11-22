

# Data protection for Amazon EVS

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Elastic VMware Service. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure, including the VMware Cloud Foundation (VCF) components. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR blog post](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr) on the * AWS Security Blog*.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management. That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the * AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through the AWS CLI or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

Amazon EVS doesn’t log user activity for non-AWS components, such as activity inside your VCF environment. VCF logs this activity in VMware consoles such as the vSphere Client and NSX Manager. For centralized VCF logging in VCF 5.2.x, you can configure a VCF monitoring solution, such as VMware Aria Operations or VMware Tanzu Observability. For more information, see [VMware Cloud Foundation with VMware Tanzu](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/working-with-workload-management-admin.html) and [VMware Aria Suite Lifecycle in VMware Cloud Foundation mode](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/vrealize-suite-lifecycle-manager-in-cloud-foundation-admin.html) in the Broadcom documentation.

Don’t put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon EVS or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names might be used for billing or diagnostic logs. Don’t include credentials in a URL that you provide to an external server.

## Encryption at rest
<a name="encryption-at-rest"></a>

Amazon EVS hosts are Amazon EC2 bare metal instances. How your data is encrypted at rest depends on where it is stored: the Amazon EBS boot volume, the NVMe instance store volumes, or external storage.

### Amazon EBS boot volume
<a name="encryption-at-rest-boot-volume"></a>

Amazon EVS instances use an Amazon EBS boot volume. The boot volume contains the operating system and other necessary files for the Amazon EC2 instance to boot and run. The boot volume is not encrypted, and Amazon EVS does not support boot volume encryption. The boot volume does not contain user data from your virtual machines.

### Hosts with local NVMe storage
<a name="encryption-at-rest-instance-store-volume"></a>

Amazon EVS instance types with local storage come with NVMe SSD instance store volumes, which are part of the instance’s hardware. On these hosts, Amazon EVS uses the NVMe instance store volumes as the disks for vSAN datastores. The vSAN datastore holds your management and workload virtual machines after you deploy your Amazon EVS environment.

The data on NVMe instance store volumes is encrypted using an XTS-AES-256 cipher, implemented on a hardware module on the instance. The keys that encrypt data written to locally attached NVMe storage devices are unique to each customer and each volume. For more information, see [Encryption at rest](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-rest) in the * Amazon EC2 User Guide*.

After you deploy VCF, you can enable vSAN data-at-rest encryption for all data stored in the vSAN datastore, for individual virtual machines (VMs), or for individual files within VMs. This granular control is useful when some VMs require encryption and others don’t, or when specific disks or files within a VM need to be encrypted. For more information, see [How vSAN Data-At-Rest Encryption Works](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/how-vsan-data-at-rest-encryption-works.html) in the Broadcom documentation.

### Diskless hosts
<a name="encryption-at-rest-diskless"></a>

This section applies to Self-deployed environments that run VCF 9.x.

Diskless hosts have no instance store volumes. For the instance types that are diskless, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions). Like other Amazon EVS hosts, they boot from an Amazon EBS boot volume. This volume isn’t encrypted and doesn’t contain user data from your virtual machines.

Your virtual machines are stored on external storage, and the encryption at rest of that data depends on the storage service that you use. For more information, see [External storage options for diskless hosts](external-storage-diskless.md) and the documentation of your storage service.

## Encryption in transit
<a name="encryption-in-transit"></a>

Amazon EVS does not encrypt your in-transit traffic by default. To encrypt the data in transit that traverses Amazon EVS, you can use application layer encryption with a protocol like Transport Layer Security (TLS). To learn about Amazon EC2 instance traffic encryption, see [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the * Amazon EC2 User Guide*.

**Note**  
Nitro network encryption does not apply to the Amazon EC2 instances that Amazon EVS deploys. Amazon EVS does not support in-transit encryption of inter-host traffic.

### In-transit encryption options for on-premises connectivity
<a name="encryption-in-transit-on-prem"></a>

To encrypt traffic between your on-premises data center and Amazon EVS, you can combine AWS Direct Connect and AWS Site-to-Site VPN with AWS Transit Gateway. This combination provides an IPsec-encrypted private connection. It also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections. For more information, see [Private IP AWS Site-to-Site VPN with AWS Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html) in the * AWS Site-to-Site VPN User Guide*.

**Note**  
Not every connection type to the underlay VPC is supported. Amazon EVS does support IPsec VPN termination on the NSX Edge Tier-0 or Tier-1 gateway. For more information, see [Add an NSX IPSec VPN Service](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-1/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html) in the Broadcom documentation. For the network connections that Amazon EVS supports, see [Supported network configurations](plan-network-supported.md).

MAC Security (MACsec) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity. You can use AWS Direct Connect connections that support MACsec to encrypt your data from your corporate data center to the AWS Direct Connect location. For more information, see [MAC Security in AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) in the * AWS Direct Connect User Guide*.

### Encryption in transit for VMware network data
<a name="vcf-encryption-in-transit"></a>

After you deploy VCF, you have multiple options to enforce data in transit encryption at the VCF layer:
+ With the VMware vDefend Distributed Firewall, you can implement fine-grained network segmentation and enforce TLS/SSL encryption between virtual machines. For more information, see [Configure Security Settings for Distributed Firewall by Using the User Interface](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/security-and-compliance-configuration-for-vmware-cloud-foundation-5-2/securing-nsx-t-data-center/security-configurations-for-further-evaluation/configure-security-settings.html) in the Broadcom documentation.
+ vSAN data-in-transit encryption encrypts all data and metadata between hosts in your vSAN cluster. For more information, see [vSAN Data-In-Transit Encryption](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-in-transit-encryption.html) in the Broadcom documentation.
+ Encrypted vSphere vMotion secures the confidentiality, integrity, and authenticity of data that is transferred with vSphere vMotion. For more information, see [What is Encrypted vSphere vMotion](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security-8-0/virtual-machine-encryption/encrypted-vsphere-vmotion.html) in the Broadcom documentation.

## Key and secret management
<a name="key-management"></a>

During environment deployment, Amazon EVS uses AWS Secrets Manager to create, encrypt, and store secrets. The secrets contain the VCF credentials needed to install and access the VCF management appliances, and the ESX root password. Amazon EVS also deletes the secrets that it manages on your behalf when you delete the environment. For more information, see [What’s in a Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/whats-in-a-secret.html) in the * AWS Secrets Manager User Guide*.

Secrets Manager uses envelope encryption with AWS KMS keys and data keys to protect each secret value. Secrets Manager uses its default AWS managed key unless you specify a customer managed key when you create the environment. For more information, see [Secret encryption and decryption in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the * AWS Secrets Manager User Guide*.

**Note**  
There are additional usage charges for customer managed keys. The default AWS managed key is provided at no cost. For more information, see [Pricing](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html#asm_pricing) in the * AWS Secrets Manager User Guide*.

Amazon EVS does not rotate secrets on your behalf and does not provide managed rotation of secrets. You are responsible for rotating the secrets associated with your environment.

We strongly recommend that you rotate your secrets as soon as the environment is created, and that you rotate them on a regular schedule after that. For more information about rotating Secrets Manager secrets, see [Rotation by Lambda function](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda.html) in the * AWS Secrets Manager User Guide*. For more information about VCF password management, see [Password Management](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/manage-passwords-admin.html) in the Broadcom documentation. For the secrets that Amazon EVS uses with connectors, see [Manage secrets](evs-env-secret-rotation.md).

**Important**  
Amazon EVS doesn’t synchronize credentials between Secrets Manager and your VCF software after deployment. If you use Secrets Manager after deployment, you must keep the credentials in Secrets Manager and SDDC Manager in sync. If you don’t, VCF passwords can expire and you can lose access to VCF software.

**Note**  
There are costs to using a Lambda function for Secrets Manager secret rotation. For more information, see [Pricing](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html#asm_pricing) in the * AWS Secrets Manager User Guide*.

## Internetwork traffic privacy
<a name="internetwork-traffic-privacy"></a>

Amazon EVS uses an Amazon VPC that you provide to create boundaries between resources in the Amazon EVS environment. The VPC also controls traffic between those resources, your on-premises network, and the internet. For more information about Amazon VPC security, see [Ensure internetwork traffic privacy in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) in the * Amazon VPC User Guide*.

For how Amazon EVS isolates VLAN subnets and how to control their traffic, see [Infrastructure security for Amazon EVS](infrastructure-security.md).

If you are an NSX administrator, you can configure the following NSX features to secure network traffic:
+ VMware vDefend Gateway Firewall secures the network perimeter and protects against external threats (north-south traffic). For more information, see [Add a Gateway Firewall Policy and Rule](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/gateway-firewall/add-a-gateway-firewall-policy-and-rule.html) in the Broadcom documentation.
+ vDefend Distributed Firewall protects against attacks that originate from within an internal network (east-west traffic). For more information, see [Add a Distributed Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/distributed-firewall/add-a-distributed-firewall.html) in the Broadcom documentation.

For how Amazon EVS isolates its own service traffic, see [Infrastructure security for Amazon EVS](infrastructure-security.md).