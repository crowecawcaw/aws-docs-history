# Encryption at rest

By default, Amazon Managed Grafana automatically provides you with encryption at rest and does this using AWS owned encryption keys.

- **AWS owned keys** – Amazon Managed Grafana uses these keys to automatically encrypt data of your workspace. You can't view, manage or use AWS owned keys, or audit their use. However, you don't have to take any action or change any programs to protect the keys that encrypt your data. For more information, see [AWS-owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS KMS Developer Guide_.
  Encryption of data at rest helps reduce the operational overhead and complexity that goes into protecting sensitive customer data, such as personally identifiable information. It allows you to build secure applications that meet strict encryption compliance and regulatory requirements.

You can alternatively choose to use a customer managed key when you create your workspace:

- **Customer managed keys** – Amazon Managed Grafana supports the use of a symmetric customer managed key that you create, own, and manage to encrypt the data in your workspace. Because you have full control of this encryption, you can perform such tasks as:

      + Establishing and maintaining key policies
      + Establishing and maintaining IAM policies and grants
      + Enabling and disabling key policies
      + Rotating key cryptographic material
      + Adding tags
      + Creating key aliases
      + Scheduling keys for deletion

  For more information, see [customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS KMS Developer Guide_ and [What is AWS KMS?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

Choose whether to use customer managed keys or AWS owned keys carefully. Workspaces created with customer managed keys can't be converted to use AWS owned keys later (and vice versa).

###### Note

- Amazon Managed Grafana automatically enables encryption at rest using AWS owned keys to protect your data at no charge.
- However, AWS KMS charges apply for using a customer managed key. For more information about pricing, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

###### Important

- If you disable or delete the customer managed key, your workspace will become inaccessible. The workspace will remain in an `ACTIVE` state but will be functionally unavailable for 7 days. After 7 days, the workspace will transition to a `FAILED` state and can only be deleted.
- Customer managed key encryption is only available for new workspaces. Existing workspaces cannot be converted to use customer managed keys.
- You cannot update the customer managed key for a workspace after creation.

## How Amazon Managed Grafana uses grants in AWS KMS

Amazon Managed Grafana requires grants to use your customer managed key.

When you create an Amazon Managed Grafana workspace encrypted with a customer managed key, Amazon Managed Grafana creates grants on your behalf by sending [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") requests to AWS KMS. Grants in AWS KMS are used to give Amazon Managed Grafana access to the KMS key in your account, even when not called directly on your behalf (for example, when storing dashboard data or user configurations).

Amazon Managed Grafana requires the grants to use your customer managed key for the following internal operations:

- Send [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") requests to AWS KMS to create additional grants as needed.
- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to AWS KMS to verify that the symmetric customer managed KMS key given when creating a workspace is valid.
- Send [ReEncryptTo and ReEncryptFrom](../../../kms/latest/APIReference/API_ReEncrypt.md "../../../kms/latest/APIReference/API_ReEncrypt.md") requests to AWS KMS to re-encrypt data when moving between different encryption contexts.
- Send [Encrypt](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md") requests to AWS KMS to encrypt data directly with your customer managed key.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS to decrypt the encrypted data keys so that they can be used to encrypt your data.
- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") requests to AWS KMS to generate data keys encrypted by your customer managed key.
- Send [GenerateDataKeyWithoutPlaintext](../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md "../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md") requests to AWS KMS to generate encrypted data keys without returning the plaintext version.
- Send [RetireGrant](../../../kms/latest/APIReference/API_RetireGrant.md "../../../kms/latest/APIReference/API_RetireGrant.md") requests to AWS KMS to retire grants that are no longer needed.

Amazon Managed Grafana creates grants to the AWS KMS key that allow Amazon Managed Grafana to use the key on your behalf. You can remove access to the key by changing the key policy, by disabling the key, or by revoking the grant. You should understand the consequences of these actions before performing them. This can cause data loss in your workspace.

If you remove access to any of the grants in any way, Amazon Managed Grafana won't be able to access any of the data encrypted by the customer managed key, nor store new data sent to the workspace, which affects operations that are dependent on that data. New update to the workspace will not be accessible and may be permanently lost.

###### Warning

- If you disable the key, or remove Amazon Managed Grafana access in the key policy, the workspace data is no longer accessible. The workspace will remain in an `ACTIVE` state but will be functionally unavailable. New update being sent to the workspace will not be accessible and may be permanently lost. You can get access to the workspace data and start receiving new data again by restoring Amazon Managed Grafana access to the key within 7 days. After 7 days, the workspace will transition to a `FAILED` state.
- If you revoke a grant, it can't be recreated, and the data in the workspace is lost permanently.
- Amazon Managed Grafana creates additional child grants through Amazon RDS due to its dependency on RDS for data storage. Revoking these RDS-related grants will have the same permanent data loss effect as revoking the primary Grafana grants.

## Step 1: Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs. The key must be in the same region as the Amazon Managed Grafana workspace and must be a symmetric key with `ENCRYPT_DECRYPT` key usage.

###### To create a symmetric customer managed key

- Follow the steps for [Creating symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS KMS Developer Guide_.

###### Key policy

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Managing access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS KMS Developer Guide_.

To use your customer managed key with your Amazon Managed Grafana workspaces, the following API operations must be permitted in the key policy:

- [kms:CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") – Adds a grant to a customer managed key. Grants control access to a specified KMS key, which allows access to grant operations Amazon Managed Grafana requires. For more information, see [Using Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS KMS Developer Guide_. This allows Amazon Managed Grafana to do the following:
  - Call `GenerateDataKey` to generate an encrypted data key and store it, because the data key isn't immediately used to encrypt.
  - Call `Decrypt` to use the stored encrypted data key to access encrypted data.

- [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – Provides the customer managed key details to allow Amazon Managed Grafana to validate the key.

The following are policy statement examples you can add for Amazon Managed Grafana:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Allow IAM Users and Roles to validate KMS key",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/root"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": [
            "grafana.<region>.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "Allow IAM Users and Roles to create grant on KMS key",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/root"
      },
      "Action": "kms:CreateGrant",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": [
            "grafana.<region>.amazonaws.com"
          ],
          "kms:GrantConstraintType": "EncryptionContextSubset"
        },
        "ForAllValues:StringEquals": {
          "kms:GrantOperations": [
            "CreateGrant",
            "RetireGrant",
            "Decrypt",
            "Encrypt",
            "GenerateDataKey",
            "GenerateDataKeyWithoutPlaintext",
            "ReEncryptFrom",
            "ReEncryptTo"
          ]
        }
      }
    }
  ]
}
```

- For more information about specifying permissions in a policy, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").
- For more information about troubleshooting key access, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

## Step 2: Specifying a customer managed key for Amazon Managed Grafana

When you create a workspace, you can specify the customer managed key by entering a KMS Key ARN, which Amazon Managed Grafana uses to encrypt the data stored by the workspace.

###### Using the AWS Management Console

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/ "https://console.aws.amazon.com/grafana/").
2. Choose **Create workspace**.
3. In the **Encryption** section, select **Customer managed key**.
4. Enter the ARN of your customer managed key in the **KMS Key ARN** field.
5. Complete the remaining workspace configuration and choose **Create workspace**.

###### Using the AWS CLI

You can specify a customer managed key when creating a workspace using the `--kms-key-id` parameter:

```
aws grafana create-workspace \
    --workspace-name "my-encrypted-workspace" \
    --workspace-description "Workspace with customer managed encryption" \
    --account-access-type "CURRENT_ACCOUNT" \
    --authentication-providers "AWS_SSO" \
    --permission-type "SERVICE_MANAGED" \
    --kms-key-id "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
```

## Monitoring your encryption keys for Amazon Managed Grafana

When you use an AWS KMS customer managed key with your Amazon Managed Grafana workspaces, you can use AWS CloudTrail or Amazon CloudWatch Logs to track requests that Amazon Managed Grafana sends to AWS KMS.

The following examples are AWS CloudTrail events for `CreateGrant`, `DescribeKey`, `GenerateDataKey`, and `Decrypt` to monitor KMS operations called by Amazon Managed Grafana to access data encrypted by your customer managed key:

###### CreateGrant

When you use an AWS KMS customer managed key to encrypt your workspace, Amazon Managed Grafana sends `CreateGrant` requests on your behalf to access the KMS key you specified. The grants that Amazon Managed Grafana creates are specific to the resource associated with the AWS KMS customer managed key.

The following example event records a `CreateGrant` operation:

```
{
"eventVersion": "1.08",
"userIdentity": {
"type": "AssumedRole",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"accessKeyId": "EXAMPLE-KEY-ID1",
"sessionContext": {
"sessionIssuer": {
"type": "Role",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"userName": "Admin"
},
"webIdFederationData": {},
"attributes": {
"mfaAuthenticated": "false",
"creationDate": "2021-04-22T17:02:00Z"
}
},
"invokedBy": "grafana.amazonaws.com"
},
"eventTime": "2021-04-22T17:07:02Z",
"eventSource": "kms.amazonaws.com",
"eventName": "CreateGrant",
"awsRegion": "us-west-2",
"sourceIPAddress": "172.12.34.56",
"userAgent": "ExampleDesktop/1.0 (V1; OS)",
"requestParameters": {
"retiringPrincipal": "grafana.amazonaws.com",
"operations": [
"CreateGrant",
"DescribeKey",
"ReEncryptTo",
"ReEncryptFrom",
"Encrypt",
"Decrypt",
"GenerateDataKey",
"GenerateDataKeyWithoutPlaintext",
"RetireGrant"
],
"keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
"granteePrincipal": "grafana.amazonaws.com"
},
"responseElements": {
"grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE"
},
"requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"readOnly": false,
"resources": [
{
"accountId": "111122223333",
"type": "AWS::KMS::Key",
"ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
}
],
"eventType": "AwsApiCall",
"managementEvent": true,
"eventCategory": "Management",
"recipientAccountId": "111122223333"
}
```

###### DescribeKey

Amazon Managed Grafana uses the `DescribeKey` operation to verify if the AWS KMS customer managed key associated with your workspace exists in the account and region.

The following example event records the `DescribeKey` operation:

```
{
"eventVersion": "1.08",
"userIdentity": {
"type": "AssumedRole",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"accessKeyId": "EXAMPLE-KEY-ID1",
"sessionContext": {
"sessionIssuer": {
"type": "Role",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"userName": "Admin"
},
"webIdFederationData": {},
"attributes": {
"mfaAuthenticated": "false",
"creationDate": "2021-04-22T17:02:00Z"
}
},
"invokedBy": "grafana.amazonaws.com"
},
"eventTime": "2021-04-22T17:07:02Z",
"eventSource": "kms.amazonaws.com",
"eventName": "DescribeKey",
"awsRegion": "us-west-2",
"sourceIPAddress": "172.12.34.56",
"userAgent": "ExampleDesktop/1.0 (V1; OS)",
"requestParameters": {
"keyId": "00dd0db0-0000-0000-ac00-b0c000SAMPLE"
},
"responseElements": null,
"requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"readOnly": true,
"resources": [
{
"accountId": "111122223333",
"type": "AWS::KMS::Key",
"ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
}
],
"eventType": "AwsApiCall",
"managementEvent": true,
"eventCategory": "Management",
"recipientAccountId": "111122223333"
}
```

###### GenerateDataKey

Amazon Managed Grafana uses the `GenerateDataKey` operation to generate data keys that are used to encrypt workspace data.

The following example event records the `GenerateDataKey` operation:

```
{
"eventVersion": "1.08",
"userIdentity": {
"type": "AssumedRole",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"accessKeyId": "EXAMPLE-KEY-ID1",
"sessionContext": {
"sessionIssuer": {
"type": "Role",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"userName": "Admin"
},
"webIdFederationData": {},
"attributes": {
"mfaAuthenticated": "false",
"creationDate": "2021-04-22T17:02:00Z"
}
},
"invokedBy": "grafana.amazonaws.com"
},
"eventTime": "2021-04-22T17:07:02Z",
"eventSource": "kms.amazonaws.com",
"eventName": "GenerateDataKey",
"awsRegion": "us-west-2",
"sourceIPAddress": "172.12.34.56",
"userAgent": "ExampleDesktop/1.0 (V1; OS)",
"requestParameters": {
"keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
"keySpec": "AES_256"
},
"responseElements": null,
"requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"readOnly": false,
"resources": [
{
"accountId": "111122223333",
"type": "AWS::KMS::Key",
"ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
}
],
"eventType": "AwsApiCall",
"managementEvent": true,
"eventCategory": "Management",
"recipientAccountId": "111122223333"
}
```

###### Decrypt

Amazon Managed Grafana uses the `Decrypt` operation to decrypt encrypted data keys so that they can be used to decrypt workspace data.

The following example event records the `Decrypt` operation:

```
{
"eventVersion": "1.08",
"userIdentity": {
"type": "AssumedRole",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"accessKeyId": "EXAMPLE-KEY-ID1",
"sessionContext": {
"sessionIssuer": {
"type": "Role",
"principalId": "TESTANDEXAMPLE:Sampleuser01",
"arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
"accountId": "111122223333",
"userName": "Admin"
},
"webIdFederationData": {},
"attributes": {
"mfaAuthenticated": "false",
"creationDate": "2021-04-22T17:02:00Z"
}
},
"invokedBy": "grafana.amazonaws.com"
},
"eventTime": "2021-04-22T17:07:02Z",
"eventSource": "kms.amazonaws.com",
"eventName": "Decrypt",
"awsRegion": "us-west-2",
"sourceIPAddress": "172.12.34.56",
"userAgent": "ExampleDesktop/1.0 (V1; OS)",
"requestParameters": {
"encryptionContext": {
"aws:grafana:workspace-id": "g-1234567890abcdef0"
}
},
"responseElements": null,
"requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
"readOnly": true,
"resources": [
{
"accountId": "111122223333",
"type": "AWS::KMS::Key",
"ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
}
],
"eventType": "AwsApiCall",
"managementEvent": true,
"eventCategory": "Management",
"recipientAccountId": "111122223333"
}
```

## Learn more

The following resources provide more information about data encryption at rest.

- For more information about AWS KMS basic concepts, see the [AWS KMS Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").
- For more information about Security best practices for AWS KMS, see the [AWS KMS Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").
