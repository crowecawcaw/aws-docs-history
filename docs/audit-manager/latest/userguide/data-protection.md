

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Data protection in AWS Audit Manager
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Audit Manager. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Audit Manager or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

In addition to the recommendation above, we recommend specifically that Audit Manager customers don't include sensitive identifying information in free-form fields when creating assessments, custom controls, custom frameworks, and delegation comments.

## Deletion of Audit Manager data
<a name="data-deletion-and-retention"></a>

There are several ways that Audit Manager data can be deleted. 

**Data deletion when disabling Audit Manager**  
When you [disable Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/disable.html), you can decide if you want to delete all of your Audit Manager data. If you choose to delete your data, it’s deleted within 7 days of disabling Audit Manager. After your data is deleted, you can’t recover it.

**Automatic data deletion**  
Some Audit Manager data is deleted automatically after a specific period of time. Audit Manager retains customer data as follows.


| Data type | Data retention period | Notes | 
| --- | --- | --- | 
| Evidence  | Data is retained for 2 years from the time of creation | Includes automated evidence and manual evidence | 
| Customer-created resources  | Data is retained indefinitely | Includes assessments, assessment reports, custom controls, and custom frameworks | 

**Manual data deletion**  
You can delete individual Audit Manager resources at any time. For instructions, see the following:
+ [Deleting an assessment in AWS Audit Manager](delete-assessment.md)
  + See also: [DeleteAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessment.html) in the *AWS Audit Manager API Reference*
+ [Deleting a custom framework in AWS Audit Manager](delete-custom-framework.md)
  + See also: [DeleteAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html) in the *AWS Audit Manager API Reference*
+ [Deleting share requests in AWS Audit Manager](deleting-shared-framework-requests.md)
  + See also: [DeleteAssessmentFrameworkShare](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFrameworkShare.html) in the *AWS Audit Manager API Reference*
+ [Deleting an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html#delete-assessment-report-steps)
  + See also: [DeleteAssessmentReport](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html) in the *AWS Audit Manager API Reference*
+ [Deleting a custom control in AWS Audit Manager](delete-controls.md)
  + See also: [DeleteControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteControl.html) in the *AWS Audit Manager API Reference*

To delete other resource data that you might have created when using Audit Manager, see the following: 
+ [Delete an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-lake-cli.html#lake-cli-delete-eds) in the *AWS CloudTrail User Guide*
+ [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the *Amazon Simple Storage Service (Amazon S3) User Guide*

## Encryption at rest
<a name="encryption-rest"></a>

To encrypt data at rest, Audit Manager uses server-side encryption with AWS managed keys for all its data stores and logs.

Your data is encrypted under a customer managed key or an AWS owned key, depending on your selected settings. If you don’t provide a customer managed key, Audit Manager uses an AWS owned key to encrypt your content. All service metadata in DynamoDB and Amazon S3 in Audit Manager is encrypted using an AWS owned key.

Audit Manager encrypts data as follows:
+ Service metadata stored in Amazon S3 is encrypted under an AWS owned key using SSE-KMS.
+ Service metadata stored in DynamoDB is server side encrypted using KMS and an AWS owned key.
+ Your content stored in DynamoDB is client-side encrypted using either a customer managed key or an AWS owned key. The KMS key is based on your chosen settings.
+ Your content stored in Amazon S3 in Audit Manager is encrypted using SSE-KMS. The KMS key is based on your selection, and could be either a customer managed key or an AWS owned key.
+ The assessment reports published to your S3 bucket are encrypted as follows:
  + If you provided a customer managed key, your data is encrypted using SSE-KMS.
  + If you used the AWS owned key, your data is encrypted using SSE-S3.

## Encryption in transit
<a name="encryption-transit"></a>

Audit Manager provides secure and private endpoints for encrypting data in transit. The secure and private endpoints allow AWS to protect the integrity of API requests to Audit Manager.

**Inter-service transit**  
 By default, all inter-service communications are protected by using Transport Layer Security (TLS) encryption.

## Key management
<a name="key-management"></a>

Audit Manager supports both AWS owned keys and customer managed keys for encrypting all Audit Manager resources (assessments, controls, frameworks, evidence, and assessment reports saved to S3 buckets in your accounts).

We recommend that you use a customer managed key. By doing so, you can view and manage the encryption keys that protect your data, including viewing logs of their use in AWS CloudTrail. When you choose a customer managed key, Audit Manager creates a grant on the KMS key so that it can be used to encrypt your content.

**Warning**  
After you delete or disable a KMS key that is used to encrypt Audit Manager resources, you can no longer decrypt the resource that was encrypted under that KMS key, which means that data becomes unrecoverable.   
Deleting a KMS key in AWS Key Management Service (AWS KMS) is destructive and potentially dangerous. For more information about deleting KMS keys, see [Deleting AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) in the *AWS Key Management Service User Guide*.

You can specify your encryption settings when you enable Audit Manager using the AWS Management Console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). For instructions, see [Enabling AWS Audit Manager](setup-audit-manager.md). 

You can review and change your encryption settings at any time. For instructions, see [Configuring your data encryption settings](settings-KMS.md).

For more information about how to set up customer managed keys, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service User Guide*.