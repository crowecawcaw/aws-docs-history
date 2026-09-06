

# Data protection in Amazon AppFlow
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon AppFlow. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon AppFlow or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.



## Encryption at Rest
<a name="encryption-rest"></a>

When you configure an SaaS application as a source or destination, you create a connection. This includes information required for connecting to the SaaS applications, such as authentication tokens, user names, and passwords. Amazon AppFlow securely stores your connection data, encrypting it using [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms) customer master keys (CMK) and then storing it in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager).

When you delete a connection, all its metadata is permanently deleted.

When you use Amazon S3 as a destination, you can choose either an AWS managed CMK or a customer managed CMK for encrypting the data in the S3 bucket using [Amazon S3 SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html).

## Encryption in Transit
<a name="encryption-transit"></a>

When you configure a flow, you can choose either an AWS managed CMK or a customer managed CMK. When executing a flow, Amazon AppFlow stores data temporarily in an intermediate S3 bucket and encrypts it using this key. This intermediate bucket is deleted after 7 days, using a bucket lifecycle policy.

Amazon AppFlow secures all data in transit using Transport Layer Security (TLS) 1.2.

With some of the SaaS applications that are a supported source or destination, you can create a connection that does not send traffic over the public internet. For more information, see [Private Amazon AppFlow flows](private-flows.md).

## Key Management
<a name="key-management"></a>

Amazon AppFlow provides both AWS managed and customer managed CMKs for encrypting connection data and data stored in Amazon S3 when it is a destination. We recommend that you use a customer managed CMK, as it puts you in full control over your encrypted data. When you choose a customer managed CMK, Amazon AppFlow attaches a resource policy to the CMK that grants it access to the CMK.

## Connection credentials
<a name="connection-credentials"></a>

Amazon AppFlow stores the encrypted credentials that are used to connect to flow source and destination applications in your AWS Secrets Manager account. These credentials include OAuth tokens, Application and API keys, and passwords. To create a new connection, grant the following permissions to any custom IAM policies.

**Note**  
The [[`AmazonAppFlowFullAccess`](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#example-1)](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#policy-examples) policy includes these permissions.

```
{ 
          "Sid": "SecretsManagerCreateSecretAccess", 
          "Effect": "Allow", 
          "Action": "secretsmanager:CreateSecret", 
          "Resource": "*", 
          "Condition": { 
               "StringLike": { "secretsmanager:Name": "appflow!*" 
            }, 
            "ForAnyValue:StringEquals": { 
                  "aws:CalledVia": [ 
                         "appflow.amazonaws.com" 
                    ] 
               } 
          } 
}, 
{ 
          "Sid": "SecretsManagerPutResourcePolicyAccess", 
          "Effect": "Allow", 
          "Action": [
               "secretsmanager:PutResourcePolicy" 
          ], 
          "Resource": "*", 
          "Condition": { 
               "ForAnyValue:StringEquals": { 
                    "aws:CalledVia": [ 
                         "appflow.amazonaws.com" 
                    ] 
          }, 
          "StringEqualsIgnoreCase": { 
               "secretsmanager:ResourceTag/aws:secretsmanager:owningService": "appflow" 
          }
     }
}
```