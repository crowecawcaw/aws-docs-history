AWS Systems Manager Incident Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Incident Manager,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Data protection in Incident Manager

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Systems Manager Incident Manager. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Incident Manager or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

By default, Incident Manager encrypts data in transit using SSL/TLS.

## Data encryption

Incident Manager uses AWS Key Management Service (AWS KMS) keys to encrypt your Incident Manager resources. For more
information about AWS KMS, see the [AWS KMS Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md"). AWS KMS
combines secure, highly available hardware and software to provide a key management system
scaled for the cloud. Incident Manager encrypts your data using your specified key and encrypts
metadata using an AWS owned key. To use Incident Manager, you must set up your replication set,
which includes setting up encryption. Incident Manager requires data encryption for use.

You can use an AWS owned key to encrypt your replication set or you can use your own
customer managed key that you created in AWS KMS to encrypt the Regions in your replication
set. Incident Manager only supports symmetric encryption AWS KMS keys to encrypt your data created
within AWS KMS. Incident Manager doesn’t support AWS KMS keys with imported key material, custom key
stores, Hash-based Message Authentication Code (HMAC), or other types of keys. If you use
customer managed keys, you use the [AWS KMS console](https://console.aws.amazon.com/kms/ "https://console.aws.amazon.com/kms/") or
AWS KMS APIs to centrally create the customer managed keys and define the key policies that
control how Incident Manager can use the customer managed keys. When you use a customer managed
key for encryption with Incident Manager, the AWS KMS customer managed key must be in the same
Region as the resources. To learn more about setting up data encryption in Incident Manager, see
[Get prepared wizard](getting-started.md#getting-started-wizard "getting-started.md#getting-started-wizard").

There are additional charges for using AWS KMS customer managed keys. For more
information, see [AWS KMS concepts -
KMS keys](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") in the _AWS Key Management Service Developer Guide_ and
[AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

###### Important

If you use a AWS KMS key (KMS key) to encrypt your replication set and
Incident Manager data, but later decide to delete the replication set, make sure to delete the
replication set _before_ disabling or deleting the
KMS key.

To allow Incident Manager to use your customer managed key to encrypt your data, you must add
the following policy statements to the key policy of your customer managed key. To learn
more about setting up and changing the key policy in your account, see [Using key policies
in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_. The
policy provides the following permissions:

- Allows Incident Manager to perform read-only operations to find the AWS KMS key for
  Incident Manager in your account.
- Allows Incident Manager to use the KMS key to create grants and describe the key, but
  only when it's acting on behalf of principals in the account who have permission to use
  Incident Manager. If the principals specified in the policy statement don't have permission
  to use the KMS keys and to use Incident Manager, the call fails, even when it comes from
  the Incident Manager service.

```
       {
       "Sid": "Allow CreateGrant through AWS Systems Manager Incident Manager",
       "Effect": "Allow",
       "Principal": {
         "AWS": "`arn:aws:iam::111122223333:user/ssm-lead`"
       },
       "Action": [
         "kms:CreateGrant",
         "kms:DescribeKey"
       ],
       "Resource": "*",
       "Condition": {
         "StringLike": {
           "kms:ViaService": [
             "ssm-incidents.`us-east-2`.amazonaws.com",
             "ssm-contacts.`us-east-2`.amazonaws.com"
           ]
         }
       }
      }
```

Replace the `Principal` value with the IAM principal that created your
replication set.

Incident Manager uses an [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
in all requests to AWS KMS for cryptographic operations. You can use this encryption context
to identify CloudTrail log events where Incident Manager uses your KMS keys. Incident Manager uses the
following encryption context:

- `contactArn=`ARN of the contact or escalation
  plan``
