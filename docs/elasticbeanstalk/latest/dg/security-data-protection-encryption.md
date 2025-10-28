# Protecting data using encryption

You can use different forms of data encryption to protect your Elastic Beanstalk data. Data protection refers to protecting data while _in
transit_ (as it travels to and from Elastic Beanstalk) and _at rest_ (while it is stored in AWS data centers).

## Encryption in transit

You can achieve data protection in transit in two ways: encrypt the connection using Secure Sockets Layer (SSL), or use client-side encryption
(where the object is encrypted before it is sent). Both methods are valid for protecting your application data. To secure the connection, encrypt it
using SSL whenever your application, its developers and administrators, and its end users send or receive any objects. For details about encrypting web
traffic to and from your application, see [Configuring HTTPS for your Elastic Beanstalk environment](configuring-https.md "configuring-https.md").

Client-side encryption isn't a valid method for protecting your source code in application versions and source bundles that you upload. Elastic Beanstalk needs
access to these objects, so they can't be encrypted. Therefore, be sure to secure the connection between your development or deployment environment and
Elastic Beanstalk.

## Encryption at rest

To protect your application's data at rest, learn about data protection in the storage service that your application uses. For example, see [Data Protection in Amazon RDS](../../../AmazonRDS/latest/UserGuide/DataDurability.md "../../../AmazonRDS/latest/UserGuide/DataDurability.md") in the _Amazon RDS User Guide_, [Data Protection in Amazon S3](../../../AmazonS3/latest/userguide/DataDurability.md "../../../AmazonS3/latest/userguide/DataDurability.md") in the _Amazon Simple Storage Service User Guide_, or [Encrypting Data and Metadata in EFS](../../../efs/latest/ug/encryption.md "../../../efs/latest/ug/encryption.md") in the _Amazon Elastic File System User Guide_.

Elastic Beanstalk stores various objects in an encrypted Amazon Simple Storage Service (Amazon S3) bucket that it creates for each AWS Region in which you create environments. Because
Elastic Beanstalk retains the default encryption provided by Amazon S3, it creates encrypted Amazon S3 buckets. For details, see [Using Elastic Beanstalk with Amazon S3](AWSHowTo.md "AWSHowTo.md"). You provide
some of the stored objects and send them to Elastic Beanstalk, for example, application versions and source bundles. Elastic Beanstalk generates other objects, for example, log
files. In addition to the data that Elastic Beanstalk stores, your application can transfer and/or store data as part of its operation.

To protect data stored on Amazon Elastic Block Store(Amazon EBS) volumes attached to your environment's instances, enable Amazon EBS encryption by default in your AWS
account and Region. When enabled, all new Amazon EBS volumes and their snapshots are automatically encrypted using AWS Key Management Service keys. For more information, see
[Encryption by default](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md") in the _Amazon EBS User
Guide_.

For more information about data protection, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security Blog_.

For other Elastic Beanstalk security topics, see [AWS Elastic Beanstalk security](security.md "security.md").
