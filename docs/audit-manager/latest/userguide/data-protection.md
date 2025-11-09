# Data protection in AWS Audit Manager

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Audit Manager. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Audit Manager or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

In addition to the recommendation above, we recommend specifically that Audit Manager customers
don't include sensitive identifying information in free-form fields when creating assessments,
custom controls, custom frameworks, and delegation comments.

## Deletion of Audit Manager data

There are several ways that Audit Manager data can be deleted.

###### Data deletion when disabling Audit Manager

When you [disable Audit Manager](disable.md "disable.md"),
you can decide if you want to delete all of your Audit Manager data. If you choose to delete your
data, it’s deleted within 7 days of disabling Audit Manager. After your data is deleted, you can’t
recover it.

###### Automatic data deletion

Some Audit Manager data is deleted automatically after a specific period of time.
Audit Manager retains customer data as follows.

| Data type                  | Data retention period                                  | Notes                                                                               |
| -------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Evidence                   | Data is retained for 2 years from the time of creation | Includes automated evidence and manual evidence                                     |
| Customer-created resources | Data is retained indefinitely                          | Includes assessments, assessment reports, custom controls, and custom<br>frameworks |

###### Manual data deletion

You can delete individual Audit Manager resources at any time. For instructions, see the following:

- [Deleting an assessment in AWS Audit Manager](delete-assessment.md "delete-assessment.md")
  - See also: [DeleteAssessment](../APIReference/API_DeleteAssessment.md "../APIReference/API_DeleteAssessment.md") in the _AWS Audit Manager
    API Reference_

- [Deleting a custom framework in AWS Audit Manager](delete-custom-framework.md "delete-custom-framework.md")
  - See also: [DeleteAssessmentFramework](../APIReference/API_DeleteAssessmentFramework.md "../APIReference/API_DeleteAssessmentFramework.md") in the _AWS Audit Manager API Reference_

- [Deleting share requests in
  AWS Audit Manager](deleting-shared-framework-requests.md "deleting-shared-framework-requests.md")
  - See also: [DeleteAssessmentFrameworkShare](../APIReference/API_DeleteAssessmentFrameworkShare.md "../APIReference/API_DeleteAssessmentFrameworkShare.md") in the _AWS Audit Manager API Reference_

- [Deleting an assessment report](download-center.md#delete-assessment-report-steps "download-center.md#delete-assessment-report-steps")
  - See also: [DeleteAssessmentReport](../APIReference/API_DeleteAssessmentReport.md "../APIReference/API_DeleteAssessmentReport.md") in the _AWS Audit Manager API Reference_

- [Deleting a custom control in AWS Audit Manager](delete-controls.md "delete-controls.md")
  - See also: [DeleteControl](../APIReference/API_DeleteControl.md "../APIReference/API_DeleteControl.md") in the _AWS Audit Manager API
    Reference_

To delete other resource data that you might have created when using Audit Manager, see the
following:

- [Delete an event data store](../../../awscloudtrail/latest/userguide/query-lake-cli.md#lake-cli-delete-eds "../../../awscloudtrail/latest/userguide/query-lake-cli.md#lake-cli-delete-eds") in the _AWS CloudTrail
  User Guide_
- [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md") in the _Amazon Simple Storage Service (Amazon S3)
  User Guide_

## Encryption at rest

To encrypt data at rest, Audit Manager uses server-side encryption with AWS managed keys for all
its data stores and logs.

Your data is encrypted under a customer managed key or an AWS owned key, depending on your
selected settings. If you don’t provide a customer managed key, Audit Manager uses an AWS owned key to encrypt
your content. All service metadata in DynamoDB and Amazon S3 in Audit Manager is encrypted using an
AWS owned key.

Audit Manager encrypts data as follows:

- Service metadata stored in Amazon S3 is encrypted under an AWS owned key using
  SSE-KMS.
- Service metadata stored in DynamoDB is server side encrypted using KMS and an AWS owned key.
- Your content stored in DynamoDB is client-side encrypted using either a customer managed key or an AWS owned key. The KMS key is based on your chosen settings.
- Your content stored in Amazon S3 in Audit Manager is encrypted using SSE-KMS. The KMS key is based
  on your selection, and could be either a customer managed key or an AWS owned key.
- The assessment reports published to your S3 bucket are encrypted as follows:
  - If you provided a customer managed key, your data is encrypted using
    SSE-KMS.
  - If you used the AWS owned key, your data is encrypted using SSE-S3.

## Encryption in transit

Audit Manager provides secure and private endpoints for encrypting data in transit. The secure
and private endpoints allow AWS to protect the integrity of API requests to Audit Manager.

###### Inter-service transit

By default, all inter-service communications are protected by using Transport Layer
Security (TLS) encryption.

## Key management

Audit Manager supports both AWS owned keys and customer managed keys for encrypting all Audit Manager resources
(assessments, controls, frameworks, evidence, and assessment reports saved to S3 buckets in
your accounts).

We recommend that you use a customer managed key. By doing so, you can view and manage the
encryption keys that protect your data, including viewing logs of their use in AWS CloudTrail. When
you choose a customer managed key, Audit Manager creates a grant on the KMS key so that it can be used
to encrypt your content.

###### Warning

After you delete or disable a KMS key that is used to encrypt Audit Manager resources, you can
no longer decrypt the resource that was encrypted under that KMS key, which means that data
becomes unrecoverable.

Deleting a KMS key in AWS Key Management Service (AWS KMS) is destructive and potentially dangerous. For more
information about deleting KMS keys, see [Deleting AWS KMS keys](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md")
in the _AWS Key Management Service User Guide_.

You can specify your encryption settings when you enable Audit Manager using the AWS Management Console,
the Audit Manager API, or the AWS Command Line Interface (AWS CLI). For instructions, see [Enabling AWS Audit Manager](setup-audit-manager.md "setup-audit-manager.md").

You can review and change your encryption settings at any time. For instructions, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").

For more information about how to set up customer managed keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
in the _AWS Key Management Service User Guide_.
