# Data protection in AWS Outposts

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Outposts. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud.
You are responsible for maintaining control over your content that is hosted on this
infrastructure. This content includes the security configuration and management tasks
for the AWS services that you use.

For data protection purposes, we recommend that you protect AWS account credentials and
set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only
the permissions necessary to fulfill their job duties.

For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

## Encryption at rest

With AWS Outposts, all data is encrypted at rest. The key material is wrapped to an
external key stored in a removable device, the Nitro Security Key (NSK). The NSK is
required to decrypt the data on your Outposts rack.

You can use Amazon EBS encryption for your EBS volumes and snapshots.
Amazon EBS encryption uses AWS Key Management Service (AWS KMS) and KMS keys. For more information, see
[Amazon EBS Encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md")
in the _Amazon EBS User Guide_.

## Encryption in transit

AWS encrypts in-transit data between your Outpost and its AWS Region. For more information,
see [Connectivity through service link](service-links.md "service-links.md").

You can use an encryption protocol, such as Transport Layer Security (TLS),
to encrypt sensitive data in transit through the local gateway to your local network.

## Data deletion

When you stop or terminate an EC2 instance, the memory allocated
to it is scrubbed (set to zero) by the hypervisor before it is allocated to a new instance, and every
block of storage is reset.

Destroying the Nitro Security Key cryptographically shreds the data on your Outpost.
