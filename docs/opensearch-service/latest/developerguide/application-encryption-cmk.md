# Encrypting OpenSearch UI application metadata with customer managed keys

Visual assets and configurations are stored as metadata for your OpenSearch UI applications. This includes saved queries, visualizations, and dashboards. Data from the associated data sources is not stored in the metadata. For information about encrypting data in your data sources, see [Data protection in Amazon OpenSearch Service](data-protection.md "data-protection.md") for OpenSearch domains and [Encryption in Amazon OpenSearch Serverless](serverless-encryption.md "serverless-encryption.md") for serverless collections.

Your OpenSearch UI metadata is protected with encryption at rest. This prevents unauthorized access. The encryption uses AWS Key Management Service (AWS KMS) to store and manage the encryption keys. By default, OpenSearch UI metadata is encrypted with AWS owned keys.

You can also use the customer managed key (CMK) feature to manage your own encryption keys. This helps you meet regulatory and compliance requirements. To use CMK, you must create a new OpenSearch UI application and enable CMK in the creation process. It is not currently supported to update an existing OpenSearch UI application from AWS owned key to CMK.

When to use customer managed keys:

- Your organization has regulatory compliance requirements for key management
- You need audit trails for encryption key usage
- You want to control key rotation schedules
- You need to integrate with existing key management workflows
  When you use a customer managed key, you have full control over the key. This includes the ability to:

- Establish and maintain key policies
- Establish and maintain IAM policies and grants
- Enable and disable the key
- Rotate the key's cryptographic material
- Add tags to the key
- Create key aliases
- Schedule the key for deletion

###### Note

The customer managed key must be in the same AWS Region as the OpenSearch UI application. You cannot use a key from a different Region.

###### Topics

- [Prerequisites for using customer managed keys](#application-encryption-cmk-prerequisites "#application-encryption-cmk-prerequisites")
- [Creating an application with customer managed key encryption using the console](#application-encryption-cmk-create-console "#application-encryption-cmk-create-console")
- [Creating an application with customer managed key encryption using the AWS CLI](#application-encryption-cmk-create-cli "#application-encryption-cmk-create-cli")
- [Monitoring customer managed key usage](#application-encryption-cmk-monitoring "#application-encryption-cmk-monitoring")
- [Updating encryption settings](#application-encryption-cmk-update "#application-encryption-cmk-update")

## Prerequisites for using customer managed keys

Before you can use a customer managed key to encrypt your OpenSearch UI application metadata, you must create a symmetric encryption key in AWS KMS. For instructions on creating keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS KMS Developer Guide_.

The key policy for your customer managed key must grant OpenSearch UI permission to use the key. Use the following key policy, replacing the `placeholder values` with your own information:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOpenSearchUIToUseKey",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "application.opensearchservice.amazonaws.com"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowKeyAdministration",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`account-id`:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        }
    ]
}
```

The policy includes two statements:

- The first statement allows OpenSearch UI to use the key for encryption operations.
- The second statement allows users in your AWS account to administer the key. This includes permissions to update the key policy, enable or disable the key, and schedule the key for deletion. You can further restrict these permissions by replacing the root principal with specific IAM users or roles.

For more information about key policies, see [Using key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS KMS Developer Guide_.

## Creating an application with customer managed key encryption using the console

When you create an OpenSearch UI application in the console, you can specify a customer managed key for encrypting the application's metadata.

###### To create an OpenSearch UI application with customer managed key encryption using the console

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation pane, choose **OpenSearch UI (Dashboards)**.
3. Choose **Create application**.
4. For **Application name**, enter a name for the application.
5. Configure authentication and administrator settings as needed. For more information, see [Getting started with the OpenSearch user
   interface in Amazon OpenSearch Service](application-getting-started.md "application-getting-started.md").
6. In the **Encryption** section, for **Encryption at rest**, choose **Use customer managed key**.
7. Select an existing customer managed key from the list, or choose **Create a key** to create a new key in AWS KMS.

###### Note

The key must be in the same AWS Region as the application you are creating. 8. (Optional) Add tags to the application. 9. Choose **Create**.

## Creating an application with customer managed key encryption using the AWS CLI

To create an OpenSearch UI application with customer managed key encryption using the AWS CLI, use the [create-application](../../../cli/latest/reference/opensearch/create-application.md "../../../cli/latest/reference/opensearch/create-application.md") command with the `--kms-key-arn` parameter.

Replace the `placeholder values` with your own information.

```
aws opensearch create-application \
    --name `my-application` \
    --kms-key-arn arn:aws:kms:`us-east-1`:`123456789012`:key/`12345678-1234-1234-1234-123456789012`
```

If you don't specify the `--kms-key-arn` parameter, OpenSearch uses an AWS-managed key to encrypt the application's metadata.

## Monitoring customer managed key usage

When you use a customer managed key with an OpenSearch UI application, AWS KMS records every use of the key in AWS CloudTrail logs. You can use these logs to monitor how and when your key is used. The logs show which user or service accessed the key.

AWS AWS KMS automatically rotates customer managed keys every year. You can also manually rotate keys as needed. For more information about key rotation, see [Rotating KMS keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the _AWS KMS Developer Guide_.

For more information about monitoring key usage, see [Logging AWS KMS API calls with AWS CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md "../../../kms/latest/developerguide/logging-using-cloudtrail.md") in the _AWS KMS Developer Guide_.

###### Note

Using customer managed keys incurs AWS KMS charges. Charges are based on the number of API requests and keys stored. For pricing details, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## Updating encryption settings

After you create an OpenSearch UI application, you cannot change its encryption settings. If you need to use a different customer managed key, you must create a new application. If you need to switch between AWS-managed and customer managed keys, you must also create a new application with the desired encryption settings.

###### Important

Before you disable or delete a customer managed key, consider the following:

- If you disable the key, the application will lose access to its encrypted metadata. You must re-enable the same key to restore access.
- If you delete the key, the application's saved objects become permanently inaccessible. This includes queries, visualizations, and dashboards. Deleted keys cannot be recovered.
- We recommend documenting your key ARN before making any changes to the key status.

###### Next steps

After you configure CMK encryption for your application, you can:

- Associate data sources with your application. For more information, see [Managing data source associations and
  Virtual Private Cloud access permissions](application-data-sources-and-vpc.md "application-data-sources-and-vpc.md").
- Create workspaces for your team. For more information, see [Using Amazon OpenSearch Service workspaces](application-workspaces.md "application-workspaces.md").
- Set up AWS CloudTrail monitoring for key usage. For more information, see [Monitoring customer managed key usage](#application-encryption-cmk-monitoring "#application-encryption-cmk-monitoring").
