

# Data protection in AWS Parallel Computing Service
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Parallel Computing Service. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS PCS or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.



## Encryption at rest
<a name="encryption-rest"></a>

Encryption is enabled by default for data at rest when you create an AWS Parallel Computing Service (AWS PCS) cluster with the AWS Management Console, AWS CLI, AWS PCS API, or AWS SDKs. AWS PCS uses an **AWS owned KMS key** to encrypt data at rest. For more information, see [ Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) in the *AWS KMS Developer Guide*. You can also use a customer managed key. For more information, see [Required KMS key policy for use with encrypted EBS volumes in AWS PCS](security-key-policy-for-encrypted-volumes.md).

 The **cluster secret** is stored in AWS Secrets Manager and is encrypted with the Secrets Manager managed KMS key. For more information, see [Working with cluster secrets in AWS PCS](working-with_clusters_secrets.md).

In an AWS PCS cluster, the following data is *at rest*:
+ **Scheduler state** – It includes data on running jobs and provisioned nodes in the cluster. This is the data that Slurm persists in the `StateSaveLocation` defined in your `slurm.conf`. For more information, see the description of [StateSaveLocation](https://slurm.schedmd.com/slurm.conf.html#OPT_StateSaveLocation) in the Slurm documentation. AWS PCS deletes job data after a job completes.
+ **Scheduler auth secret** – AWS PCS uses it to authenticate all scheduler communications in the cluster.

For scheduler state information, AWS PCS automatically encrypts data and metadata before it writes them to the file system. The encrypted file system uses industry standard AES-256 encryption algorithm for data at rest.

## Encryption in transit
<a name="encryption-transit"></a>

Your connections to the AWS PCS API use TLS encryption with the Signature Version 4 signing process, regardless of whether you use the AWS Command Line Interface (AWS CLI) or AWS SDKs. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *AWS Identity and Access Management User Guide*. AWS manages access control through the API with the IAM policies for the security credentials you use to connect.

AWS PCS uses TLS to connect to other AWS services.

Within a Slurm cluster, the scheduler is configured with the `auth/slurm` authentication plug-in that provides authentication for all scheduler communications. Slurm doesn't provide encryption at the application level for its communications, all data flowing across cluster instances stays local to the EC2 VPC and therefore is subject to VPC encryption if those instances support encryption in transit. For more information, see [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the *Amazon Elastic Compute Cloud User Guide*. Communication is encrypted between the controller (provisioned in a service account) the cluster nodes in your account.

## Key management
<a name="key-management"></a>

AWS PCS uses an **AWS owned KMS key** to encrypt data. For more information, see [ Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) in the *AWS KMS Developer Guide*. You can also use a customer managed key. For more information, see [Required KMS key policy for use with encrypted EBS volumes in AWS PCS](security-key-policy-for-encrypted-volumes.md).

 The **cluster secret** is stored in AWS Secrets Manager and is encrypted with the Secrets Manager managed KMS key. For more information, see [Working with cluster secrets in AWS PCS](working-with_clusters_secrets.md).

## Inter-network traffic privacy
<a name="inter-network-traffic-privacy"></a>

AWS PCS compute resources for a cluster reside within 1 VPC in the customer’s account. Therefore, all internal AWS PCS service traffic within a cluster stays within the AWS network and doesn't travel across the internet. Communication between the user and AWS PCS nodes can travel across the internet and we recommend using SSH or Systems Manager to connect to the nodes. For more information, see [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) in the *AWS Systems Manager User Guide*.

You can also use the following offerings to connect your on-premises network to AWS:
+ AWS Site-to-Site VPN. For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *AWS Site-to-Site VPN User Guide*.
+ An AWS Direct Connect. For more information, see [What is AWS Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) in the *AWS Direct Connect User Guide*.

You access the AWS PCS API to perform administrative tasks for the service. You and your users access the Slurm endpoint ports to interact with the scheduler directly.

## Encrypting API traffic
<a name="encrypting-api-traffic"></a>

To access the AWS PCS API, clients must support Transport Layer Security (TLS) 1.2 or later. We require TLS 1.2 and recommend TLS 1.3. Clients must also support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems such as Java 7 and later support these modes. Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. You can also use AWS Security Token Service (AWS STS) to generate temporary security credentials to sign requests.

## Encrypting data traffic
<a name="ecrypting-data-traffic"></a>

Encryption of data in transit is enabled from supported EC2 instances accessing the scheduler endpoint and between ComputeNodeGroup instances from within the AWS Cloud. For more information, see [Encryption in transit](#encryption-transit).