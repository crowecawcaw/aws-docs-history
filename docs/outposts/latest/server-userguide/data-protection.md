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
required to decrypt the data on your Outposts server.

## Encryption in transit

AWS encrypts in-transit data between your Outpost and its AWS Region. For more information,
see [Connectivity through service link](service-links.md "service-links.md").

## Data deletion

When you terminate an EC2 instance, the memory allocated
to it is scrubbed (set to zero) by the hypervisor before it is allocated to a new instance, and every
block of storage is reset.

Destroying the Nitro Security Key cryptographically shreds the data on your Outpost.
For more information, see [Cryptographically shred server
data](outpost-maintenance.md#outpost-server-cryptographically-shred-data "outpost-maintenance.md#outpost-server-cryptographically-shred-data").
