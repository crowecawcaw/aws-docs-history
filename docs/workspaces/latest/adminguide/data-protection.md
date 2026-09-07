

# Data protection in Amazon WorkSpaces
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon WorkSpaces. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with WorkSpaces or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

For more information about WorkSpaces and FIPS endpoint encryption, see [Configure FedRAMP authorization or DoD SRG compliance for WorkSpaces Personal](fips-encryption.md).

## Encryption at rest
<a name="encryption-rest"></a>

You can encrypt the storage volumes for your WorkSpaces using AWS KMS Key from AWS Key Management Service. For more information, see [Encrypted WorkSpaces in WorkSpaces Personal](encrypt-workspaces.md).

When you create WorkSpaces with encrypted volumes, WorkSpaces uses Amazon Elastic Block Store (Amazon EBS) to create and manage those volumes. EBS encrypts your volumes with a data key using the industry-standard AES-256 algorithm. For more information, see [ Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the *Amazon EC2 User Guide*.

## Encryption in transit
<a name="encryption-transit"></a>

For PCoIP, data in-transit is encrypted using TLS 1.2 encryption and SigV4 request signing. The PCoIP protocol uses encrypted UDP traffic, with AES encryption, for streaming pixels.The streaming connection, using port 4172 (TCP and UDP), is encrypted by using AES-128 and AES-256 ciphers, but the encryption defaults to 128-bit. You can change this default to 256-bit, either by using the **Configure PCoIP Security Settings** Group Policy setting for Windows WorkSpaces, or by modifying the **PCoIP Security Settings** in the `pcoip-agent.conf` file for Amazon Linux WorkSpaces.

To learn more about Group Policy administration for Amazon WorkSpaces, see [Configure PCoIP security settings](group_policy.md#gp_security) in [Manage your Windows WorkSpaces in WorkSpaces Personal](group_policy.md). To learn more about modifying the `pcoip-agent.conf` file, see [Control PCoIP Agent behavior on Amazon Linux WorkSpaces](manage_linux_workspace.md#pcoip_agent_linux) and [ PCoIP Security Settings](https://www.teradici.com/web-help/pcoip_agent/standard_agent/linux/21.03/admin-guide/configuring/configuring/#pcoip-security-settings) in the Teradici documentation.

For DCV, streaming and control data in-transit is encrypted using TLS 1.3 encryption for UDP traffic and TLS 1.2 encryption for TCP traffic, with AES-256 ciphers.