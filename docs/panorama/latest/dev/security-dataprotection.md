End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Data protection in AWS Panorama

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Panorama. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Panorama or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

###### Sections

- [Encryption in transit](#security-privacy-intransit "#security-privacy-intransit")
- [AWS Panorama Appliance](#security-privacy-atrest "#security-privacy-atrest")
- [Applications](#security-privacy-applications "#security-privacy-applications")
- [Other services](#security-privacy-services "#security-privacy-services")

## Encryption in transit

AWS Panorama API endpoints support secure connections only over HTTPS. When you manage AWS Panorama resources with the
AWS Management Console, AWS SDK, or the AWS Panorama API, all communication is encrypted with Transport Layer Security (TLS).
Communication between the AWS Panorama Appliance and AWS is also encrypted with TLS. Communication between the AWS Panorama Appliance
and cameras over RTSP is not encrypted.

For a complete list of API endpoints, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in
the _AWS General Reference_.

## AWS Panorama Appliance

The AWS Panorama Appliance has physical ports for Ethernet, HDMI video, and USB storage. The SD card slot, Wi-Fi, and
Bluetooth are not usable. The USB port is only used during provisioning to transfer a configuration archive to the
appliance.

The contents of the configuration archive, which includes the appliance's provisioning certificate and network
configuration, are not encrypted. AWS Panorama does not store these files; they can only be retrieved when you register
an appliance. After you transfer the configuration archive to an appliance, delete it from your computer and USB
storage device.

The entire file system of the appliance is encrypted. Additionally, the appliance applies several system-level
protections, including rollback protection for required software updates, signed kernel and bootloader, and
software integrity verification.

When you stop using the appliance, perform a [full reset](appliance-buttons.md#appliance-buttons-reset "appliance-buttons.md#appliance-buttons-reset") to
delete your application data and reset the appliance software.

## Applications

You control the code that you deploy to your appliance. Validate all application code for security issues
before deploying it, regardless of its source. If you use 3rd party libraries in your application, carefully
consider the licensing and support policies for those libraries.

Application CPU, memory, and disk usage are not constrained by the appliance software. An application using
too many resources can negatively impact other applications and the device’s operation. Test applications
separately before combining or deploying to production environments.

Application assets (codes and models) are not isolated from access within your account, appliance, or build
environment. The container images and model archives generated by the AWS Panorama Application CLI are not encrypted. Use separate
accounts for production workloads and only allow access on an as-needed basis.

## Other services

To store your models and application containers securely in Amazon S3, AWS Panorama uses server-side encryption with a key
that Amazon S3 manages. For more information, see [Protecting data using
encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the Amazon Simple Storage Service User Guide.

Camera stream credentials are encrypted at rest in AWS Secrets Manager. The appliance's IAM role grants it permission to
retrieve the secret in order to access the stream's username and password.

The AWS Panorama Appliance sends log data to Amazon CloudWatch Logs. CloudWatch Logs encrypts this data by default, and can be configured to use
a customer managed key. For more information, see [Encrypt log data in CloudWatch Logs using
AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the Amazon CloudWatch Logs User Guide.
