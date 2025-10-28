# Encryption at rest for Amazon WorkSpaces Secure Browser

_Encryption at rest_ is configured by default and all customer data
(for example, browser policy statements, usernames, logging, or IP addresses) used in WorkSpaces Secure Browser
is encrypted using AWS KMS. By default, WorkSpaces Secure Browser enables encryption with an AWS-owned key. You
can also use a Customer Managed Key (CMK) by specifying your CMK on resource creation. This
is currently only supported via the CLI.

If you choose to pass a CMK, the key provided must be a symmetric encryption AWS KMS key
and you, as the administrator, must have the following permissions:

```
kms:DescribeKey

kms:GenerateDataKey

kms:GenerateDataKeyWithoutPlaintext

kms:Decrypt

kms:ReEncryptTo
kms:ReEncryptFrom
```

If you use a CMK, you will need to allowlist the WorkSpaces Secure Browser external service principal
to access to the key.
For more information, see Example of Scoped CMK Key Policy with
aws:SourceAccount

Whenever possible, WorkSpaces Secure Browser will use Forward Access Sessions (FAS) credentials to access
your key. For more information about FAS, see [Forward access
sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").
There are cases where WorkSpaces Secure Browser may need to access your key asynchronously.
By allowlisting the WorkSpaces Secure Browser external service principal in your key policy, WorkSpaces Secure Browser will be able
to perform the allowlisted set of cryptographic operations with your key.

After a resource is created, the key can no longer be removed or changed. If you used a CMK,
you, as the administrator accessing the resource, must have the following permissions:

```
kms:GenerateDataKey
kms:GenerateDataKeyWithoutPlaintext
kms:Decrypt

kms:ReEncryptTo
kms:ReEncryptFrom
```

If you see an **Access Denied** error when using the console, it is
likely that the user accessing the console doesn't have the required permissions to use the
CMK on the key that is being used.

## Key policy and scoping examples for WorkSpaces Secure Browser

CMKs require the following key policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
  ...,
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      }
    ]
}
```

The following permissions are required by WorkSpaces Secure Browser:

- `kms:DescribeKey` — Validates that the provided AWS KMS key is
  configured correctly.
- `kms:GenerateDataKeyWithoutPlaintext` and `kms:GenerateDataKey`
  — Request for the AWS KMS key to create data keys used to encrypt objects.
- `kms:Decrypt` — Requests the AWS KMS key to decrypt the encrypted
  data keys. These data keys are used to encrypt your data.
- `kms:ReEncryptTo` and `kms:ReEncryptFrom` — Request
  for the AWS KMS key to permit re-encryption from or to a KMS key.

### Scoping WorkSpaces Secure Browser permissions on your AWS KMS key

When the principal in a key policy statement is an [AWS service principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), we strongly recommend that you use the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") or [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys, in addition to the Encryption
Context.

The Encryption Context used for a resource will always contain an entry in the
format `aws:workspaces-web:RESOURCE_TYPE:id` and the corresponding resource
ID.

The source ARN and source account values are included in the authorization context
only when a request comes to AWS KMS from another AWS service. This combination of
conditions implements least privileged permissions and avoids a potential [confused deputy
scenario](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). For more information, see [Permissions for AWS services in key policies](../../../kms/latest/developerguide/key-policy-services.md "../../../kms/latest/developerguide/key-policy-services.md").

```
   "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`AccountId`",
          "kms:EncryptionContext:aws:workspaces-web:`resourceType`:id": "`resourceId`"
        },
        "ArnEquals": {
          "aws:SourceArn": [
            "arn:aws:workspaces-web:`Region`:`AccountId`:`resourceType`/`resourceId`"
          ]
        },
      }
```

###### Note

Before resource creation, the key policy should only use the `aws:SourceAccount`
Condition, as the full resource arn will not exist yet. Following resource creation,
the key policy can be updated to include the `aws:SourceArn` and
`kms:EncryptionContext` Conditions.

### Example of Scoped CMK key policy with `aws:SourceAccount`

```
{
  "Version": "2012-10-17",
  "Statement": [
  ...,
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "<AccountId>"
        }
      }
    }
  ]
}
```

### Example of scoped CMK key policy with `aws:SourceArn` and resource wildcard

```
{
  "Version": "2012-10-17",
  "Statement": [
  ...,
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:workspaces-web:<Region>:<AccountId>:*/*"
        }
      }
    }
  ]
}
```

### Example of scoped CMK key policy with `aws:SourceArn`

```
{
  "Version": "2012-10-17",
  "Statement": [
  ...,
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:workspaces-web:<Region>:<AccountId>:portal/*",
            "arn:aws:workspaces-web:<Region>:<AccountId>:browserSettings/*",
            "arn:aws:workspaces-web:<Region>:<AccountId>:userSettings/*",
            "arn:aws:workspaces-web:<Region>:<AccountId>:ipAccessSettings/*"
          ]
        }
    }
  ]
}
```

###### Note

After you create the resource, you can update the wildcard in `SourceArn` for it.
If you use WorkSpaces Secure Browser to create a new resource that requires CMK access, ensure you update its key policy accordingly.

### Example of scoped CMK key policy with `aws:SourceArn` and resource-specific `EncryptionContext`

```
{
  "Version": "2012-10-17",
  "Statement": [
  ...,
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt portal",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "<AccountId>",
            "kms:EncryptionContext:aws:workspaces-web:portal:id": "<portalId>>"
        }
      }
    },
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt userSettings",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
         "StringEquals": {
            "aws:SourceAccount": "<AccountId>",
            "kms:EncryptionContext:aws:workspaces-web:userSetttings:id": "<userSetttingsId>"
        }
      }
    },
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt browserSettings",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
         "StringEquals": {
            "aws:SourceAccount": "<AccountId>",
            "kms:EncryptionContext:aws:workspaces-web:browserSettings:id": "<browserSettingsId>"
        }
      }
    },
    {
      "Sid": "Allow WorkSpaces Secure Browser to encrypt/decrypt ipAccessSettings",
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces-web.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
       ],
      "Resource": "*",
      "Condition": {
         "StringEquals": {
            "aws:SourceAccount": "<AccountId>",
            "kms:EncryptionContext:aws:workspaces-web:ipAccessSettings:id": "<ipAccessSettingsId>"
        }
      }
    },
  ]
}
```

###### Note

Ensure you create separate statements when including a resource specific
`EncryptionContext` on the same key policy. For more information, see the
Using multiple encryption context pairs section under [kms:EncryptionContext:_context-key_](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-encryption-context "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-encryption-context").
