# Encrypting Resources in Amazon Verified Permissions

Amazon Verified Permissions provides encryption by default to protect sensitive customer data at rest using AWS owned encryption keys.
As an extra layer of protection, Amazon Verified Permissions allows you to encrypt your policy stores using AWS Key Management Service (AWS KMS) customer managed keys (CMK).
This functionality ensures protection of sensitive data via encryption at rest, which helps you:

- Reduce the operational burden on your application's end to protect sensitive data
- Maintain control over who can see details of your authorization policies via your own AWS KMS customer managed keys
- Build security-sensitive applications that meet strict encryption compliance and regulatory requirements
  The following sections explain how to configure encryption for new policy stores and managing your encryption keys.

## AWS KMS Key Types for Amazon Verified Permissions

Amazon Verified Permissions integrates with AWS KMS to manage encryption keys used for encrypting/decrypting customer data. To learn more about
key types and states, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts-intro.md "../../../kms/latest/developerguide/concepts-intro.md") in the _AWS KMS Developer Guide_.
When you create a new policy store, you can choose from the following AWS KMS key types to encrypt your data:

### AWS Owned Key

The default encryption type. Amazon Verified Permissions owns the key at no additional charge to you and encrypts resource data at rest upon creation.
No additional configuration is required in your code or applications to encrypt/decrypt your data using the key owned by Verified Permissions.

### Customer Managed Key

You create, own, and manage the key in your AWS account. You have full control over the AWS KMS key. AWS KMS charges apply for customer managed keys.
For more information, see the [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/") page. For more information about key types,
see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-mgn-key "../../../kms/latest/developerguide/concepts.md#customer-mgn-key") in the _AWS KMS Developer Guide_.

When you specify a customer managed key for encryption for top-level resources (i.e. policy store), Verified Permissions encrypts the resource, as well as its child resources, with that key.
To encrypt a policy store using a customer managed key, you need to grant access to Verified Permissions in your key policy. A key policy is a [resource-based policy](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based")
that you attach to your customer managed key to control access to it. See [Authorizing use of your AWS KMS key for Amazon Verified Permissions](#authorizing-kms-key-use "#authorizing-kms-key-use") for more details.

In addition, to create an encrypted policy store with a customer managed key, or to make API calls to a policy store encrypted by a customer managed key, the IAM user or role which makes the call must also have access to the key.
If Verified Permissions is unable to access the key, any authorization decisions that involve resources encrypted by that key may be stale or inaccurate. When you do not have access to the key,
you will not be able to read/update/delete resources encrypted by that key, and any create calls to utilize the key for encryption will fail.

###### Note

Verified Permissions encryption at rest is available in all AWS Regions where Verified Permissions is available.

###### Important

Once a customer managed key has been used to encrypt a policy store, you CANNOT update the resource to use a different key for encryption or remove the key from that policy store.

## Using AWS KMS and data keys with Amazon Verified Permissions

The Amazon Verified Permissions encryption at rest feature uses an AWS KMS key and a hierarchy of data keys to protect your resource data.

###### Note

Amazon Verified Permissions supports only symmetric AWS KMS keys. You can't use an asymmetric AWS KMS key to encrypt your Amazon Verified Permissions resources.

### Using AWS Owned Keys

Amazon Verified Permissions encrypts all resources by default with AWS owned keys. These keys are free to use and rotate annually to protect
your account resources. You don't need to view, manage, use, or audit these keys, so there's no action required for data protection.
For more information about AWS owned keys, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-key "../../../kms/latest/developerguide/concepts.md#aws-owned-key") in the _AWS KMS Developer Guide_.

### Using Customer Managed Keys

Selecting a customer managed key for encryption provides the following benefits:

- You create and manage the AWS KMS key, including setting the key policies and IAM policies to
  control access to the AWS KMS key. You can enable and disable the AWS KMS key, enable and disable automatic
  key rotation, and delete the AWS KMS key when it is no longer in use.
- You can use a customer managed key with imported key material or a customer managed key in a custom key store that you own and manage.
- You can audit the encryption and decryption of your Verified Permissions resources by examining the Amazon Verified Permissions API calls to AWS KMS in AWS CloudTrail logs.

For Amazon Verified Permissions to use your customer managed keys for encryption/decryption, you will need to add specific key policies to allow Amazon Verified Permissions to encrypt/decrypt resources on your behalf.

## Authorizing use of your AWS KMS key for Amazon Verified Permissions

At a minimum, Amazon Verified Permissions requires the following permissions on a customer managed key:

- `kms:Encrypt`
- `kms:GenerateDataKeyWithoutPlaintext`
- `kms:DescribeKey`
- `kms:ReEncryptTo`
- `kms:ReEncryptFrom`
- `kms:Decrypt`

An example key policy can be seen below:

```
{
    "Sid": "Enable AVP to use the KMS key for encrypting project J.A.K. policy resources",
    "Effect": "Allow",
    "Principal": {
        "Service": "verifiedpermissions.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Encrypt",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo",
        "kms:DescribeKey"
    ],
    "Resource": "*"
}
```

### Understanding Source Context

Source context provides information on the source caller attempting to make AWS KMS actions against a given key.
This prevents confusion or misuse of encrypted data by binding context to the source of the data.

Customers can utilize source context as additional conditions on their key policy such as the following key policy statements:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Enable this account full access to this key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Enable AVP to retrieve this key's metadata",
            "Effect": "Allow",
            "Principal": {
                "Service": "verifiedpermissions.amazonaws.com"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "StringLike": {
                    "aws:SourceArn": "arn:aws:verifiedpermissions::111122223333:policy-store/*"
                }
            }
        },
        {
            "Sid": "Enable AVP to encrypt/decrypt resources utilizing this key",
            "Effect": "Allow",
            "Principal": {
                "Service": "verifiedpermissions.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:Encrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "StringLike": {
                    "aws:SourceArn": "arn:aws:verifiedpermissions::111122223333:policy-store/*"
                }
            }
        }
    ]
}
```

This key policy allows Verified Permissions to make AWS KMS calls on your behalf, if the source account is the same as the account
that this AWS KMS key lives in. These values should be verifiable when checking AWS CloudTrail audit logs for the CMK key.
For more information on global AWS condition keys, see [Using `aws:SourceArn`
or `aws:SourceAccount` condition keys](../../../kms/latest/developerguide/least-privilege.md#key-policy-least-privilege "../../../kms/latest/developerguide/least-privilege.md#key-policy-least-privilege").

### Understanding Encryption Context

Encryption context is a set of key-value pairs that contain additional authenticated data for encryption integrity checks.
When you include an encryption context in a request to encrypt data, AWS KMS cryptographically binds the encryption context to the
encrypted data. In order to decrypt the data, you must pass the same encryption context.

Amazon Verified Permissions uses the same encryption context in all AWS KMS cryptographic operations and can be verified within AWS CloudTrail
logs when Verified Permissions makes AWS KMS calls on your behalf for encryption/decryption processes. By default, Verified Permissions utilizes the following
encryption context key-value pairs when encrypting your resources:

```
{
    "aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/PSt123456789012"
}
```

Amazon Verified Permissions also allows for you to append custom encryption context as part of additional metadata you
wish to include during encryption/decryption processes. This means that your key policy can be more fine-grained in granting permissions such as the example below:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Enable this account full access to this key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Enable AVP to retrieve this key's metadata",
            "Effect": "Allow",
            "Principal": {
                "Service": "verifiedpermissions.amazonaws.com"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*"
        },
        {
            "Sid": "Enable AVP to encrypt/decrypt resources utilizing this key",
            "Effect": "Allow",
            "Principal": {
                "Service": "verifiedpermissions.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:Encrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/*",
                    "kms:EncryptionContext:policy_owner": "Tim"
                }
            }
        }
    ]
}
```

This key policy allows Verified Permissions to make AWS KMS calls on your behalf, if the encryption context map contains a key `aws:verifiedpermissions:policy-store-arn`,
whose value follows the format of `arn:aws:verifiedpermissions::111122223333:policy-store/*` and also contains a key-value pair `"policy_owner": "Tim"`.
See [Creating an Encrypted Policy store](#creating-encrypted-policy-store "#creating-encrypted-policy-store") for how to set custom encryption context.

###### Note

It is recommended for key policies with conditions based on encryption context to be for a subset of the encryption context map, rather than
checking for each key-value pair. The service and its dependencies upstream may add additional key-value pairs that are not visible to you, and can affect Verified Permissions' key access
if the key policy conditionally allows based on the **exact** look of the encryption context map.

### Understanding kms:ViaService

The `kms:ViaService` condition key limits use of an AWS KMS key to requests from specified AWS services.
This condition key only applies for [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") (FAS).
For more information on `kms:ViaService`, see [kms:ViaService](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service")
in the _AWS KMS Developer Guide_.

For example, the following key policy statement uses the `kms:ViaService` condition key to allow a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-mgn-key "../../../kms/latest/developerguide/concepts.md#customer-mgn-key")
to be used for the specified actions only when the request comes from Amazon Verified Permissions in the US East (N. Virginia) region on behalf of `BrentRole`.

```
{
    "Sid": "Enable AVP to encrypt/decrypt resources using credentials of BrentRole",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/BrentRole"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Encrypt",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "verifiedpermissions.us-east-1.amazonaws.com"
            ]
        }
    }
}
```

This is necessary for Verified Permissions to be able to pass your identity, permissions, and session attributes when Verified Permissions makes a request to AWS KMS on your behalf for encryption/decryption.
For more information on FAS requests, see [Forward Access Sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") in the _IAM User Guide_.

### Complete AWS KMS Key Policy

Based on the concepts in the previous sections, this is an example key policy that will allow Amazon Verified Permissions to use a CMK for encryption/decryption:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Enable this account full access to this key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Enable AVP to retrieve this key's metadata",
            "Effect": "Allow",
            "Principal": {
                "Service": "verifiedpermissions.amazonaws.com"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "StringLike": {
                    "aws:SourceArn": "arn:aws:verifiedpermissions::111122223333:policy-store/*"
                }
            }
        },
        {
            "Sid": "Enable AVP to encrypt/decrypt resources utilizing this key",
            "Effect": "Allow",
            "Principal": {
                "Service": "verifiedpermissions.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom",
                "kms:Encrypt",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/*",
                    "kms:EncryptionContext:policy_owner": "Tim",
                    "aws:SourceArn": "arn:aws:verifiedpermissions::111122223333:policy-store/*"
                },
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "Enable AVP to encrypt/decrypt resources using credentials of BrentRole",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/BrentRole"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:Encrypt",
                "kms:ReEncryptFrom",
                "kms:ReEncryptTo",
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "verifiedpermissions.us-east-1.amazonaws.com"
                    ]
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/*",
                    "kms:EncryptionContext:policy_owner": "Tim"
                }
            }
        }
    ]
}
```

###### Warning

Exercise caution when modifying AWS KMS key policies for keys already in use by Amazon Verified Permissions. While Verified Permissions validates encryption and
decryption permissions when you initially configure an AWS KMS key during top-level resource creation, it cannot verify subsequent policy
changes on demand. Inadvertently removing necessary permissions could disrupt your authorization decisions and regular Verified Permissions service flows.
For guidance troubleshooting common errors related to customer managed keys in Amazon Verified Permissions, refer to [Troubleshoot Customer Managed Keys in Amazon Verified Permissions](#troubleshoot-cmk "#troubleshoot-cmk").

### Necessary IAM Policies for Encrypted Resources

Customers that call Verified Permissions via an IAM role within their account will need to ensure that the corresponding IAM policy has
proper permissions to utilize the customer managed key for encryption and decryption of resources.

For creating policy stores that are encrypted by a customer managed key, the following IAM policy illustrates the bare-minimum necessary AWS KMS and Verified Permissions actions to do so:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "verifiedpermissions:CreatePolicyStore",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom",
                "kms:DescribeKey",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}

```

###### Note

For retrieving (Get\* and List\* operations) and deleting policy stores that are encrypted by a customer managed key, no additional permissions are needed.

For updating a policy store encrypted by a customer managed key, retrieving (Get\* and List\* operations), updating, and deleting child resources of a policy store encrypted by a customer managed key, the following IAM policy illustrates
the bare-minimum necessary AWS KMS and Verified Permissions actions do to so:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "verifiedpermissions:*",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}

```

As a single IAM policy, customers can simply add the following to their IAM role policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "verifiedpermissions:*",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom",
                "kms:DescribeKey",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}

```

## Managing Encrypted Policy stores

Policy stores are the entry-level container that will contain all related policy resources. For more information about policy stores
and the hierarchy of child resources, see [Amazon Verified Permissions policy stores](policy-stores.md "policy-stores.md")
in the _Amazon Verified Permissions User Guide_.

When you create a policy store in Verified Permissions, you can enable encryption at rest using AWS KMS keys. This ensures that:

- All read, update, and delete operations on policy stores, and their child resources, will utilize the provided customer managed key for decryption processes
- Any authorization decision calls (i.e. IsAuthorized, BatchIsAuthorized, IsAuthorizedWithToken, etc.) will use the provided customer managed key for decryption processes

### Creating an Encrypted Policy store

Before creating an encrypted policy store, ensure that the customer managed key you are using has the proper key policy statements set for Amazon Verified Permissions to utilize the key for encryption/decryption.
See [Authorizing use of your AWS KMS key for Amazon Verified Permissions](#authorizing-kms-key-use "#authorizing-kms-key-use") for what permissions are necessary.

Using AWS CLI:

```
aws verifiedpermissions create-policy-store --region us-east-1 --encryption-settings file://encrypted.json --validation-settings "{\"mode\": \"OFF\"}"
```

Where `encrypted.json` looks like:

```
{
    "kmsEncryptionSettings": {
        "key": "`arn:aws:kms:us-east-1:111122223333:key/12345678-90ab-cdef-ghij-klmnopqrstuv`",
        "encryptionContext": {
            "`<ENCRYPTION_CONTEXT_KEY_1>`": "`<ENCRYPTION_CONTEXT_VALUE_1>`",
            "`<ENCRYPTION_CONTEXT_KEY_2>`": "`<ENCRYPTION_CONTEXT_VALUE_2>`",
            ...
        }
    }
}
```

Making sure to replace `key` with your customer managed key ARN and replacing `<ENCRYPTION_CONTEXT_KEY>`
and `<ENCRYPTION_CONTEXT_VALUE>` pairs with the desired `encryptionContext` key-value pairs. `encryptionContext` can be omitted completely if no key-value pair additions are desired.

###### Important

Do not include the key-value pair `aws:verifiedpermissions:policy-store-arn` in your custom encryption context. This is automatically added and will result
in validation errors if it is part of your passed custom encryption context key-value pairs.

For more information of the available APIs of child resources of a policy store, see [Actions](../apireference/API_Operations.md "../apireference/API_Operations.md") in the _Amazon Verified Permissions
API Reference Guide_.

###### Note

If the AWS KMS customer managed key in use by your Amazon Verified Permissions resources is deleted, disabled, or inaccessible due to an incorrect AWS KMS key policy, decryption of resources will fail, and thus resulting
in stale authorization decisions. The loss of access can be temporary (a key policy can be corrected) or permanent (a deleted key cannot be restored) depending on the circumstances. We recommend you
[restrict access](../../../kms/latest/developerguide/deleting-keys-adding-permission.md "../../../kms/latest/developerguide/deleting-keys-adding-permission.md") to critical operations, such as deleting or disabling the AWS KMS key. Also, we recommend that your
organization set up [AWS break-glass access procedures](../../../wellarchitected/latest/devops-guidance/ag.sad.md "../../../wellarchitected/latest/devops-guidance/ag.sad.md") to ensure your privileged users can
access AWS in the unlikely event that Amazon Verified Permissions is inaccessible.

## Monitoring Amazon Verified Permissions Interaction with AWS KMS

You can monitor Amazon Verified Permissions' use of your customer managed key through AWS CloudTrail. Each request to AWS KMS via Verified Permissions includes the encryption context and the key ARN being utilized (your customer managed key) in the request parameters:

Example AWS CloudTrail log entry for `GenerateDataKeyWithoutPlaintext`:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "verifiedpermissions.amazonaws.com"
    },
    "eventTime": "2025-09-28T16:51:04Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyWithoutPlaintext",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "verifiedpermissions.amazonaws.com",
    "userAgent": "verifiedpermissions.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/abcdefgh-0123-ijkl-4567-mnopqrstuvwx",
        "encryptionContext": {
            "aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/PSt123456789012",
            "policy_store_editor": "Janus"
        },
        ...
    },
    ...
}
```

Example AWS CloudTrail log entry for `Decrypt`:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "verifiedpermissions.amazonaws.com"
    },
    "eventTime": "2025-09-28T16:53:21Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "verifiedpermissions.amazonaws.com",
    "userAgent": "verifiedpermissions.amazonaws.com",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/abcdefgh-0123-ijkl-4567-mnopqrstuvwx",
        "encryptionContext": {
            "aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/PSt123456789012",
            "policy_store_owner": "Elias"
        }
    },
    ...
}
```

Example AWS CloudTrail log entry for `ReEncrypt`:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "verifiedpermissions.amazonaws.com"
    },
    "eventTime": "2025-09-28T16:51:04Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "ReEncrypt",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "verifiedpermissions.amazonaws.com",
    "userAgent": "verifiedpermissions.amazonaws.com",
    "requestParameters": {
        "sourceKeyId": "arn:aws:kms:us-east-1:111122223333:key/abcdefgh-0123-ijkl-4567-mnopqrstuvwx",
        "destinationEncryptionContext": {
            "aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::111122223333:policy-store/PSt123456789012"
        },
        "sourceEncryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "destinationKeyId": "arn:aws:kms:us-east-1:111122223333:key/abcdefgh-0123-ijkl-4567-mnopqrstuvwx",
        "sourceEncryptionContext": {
            "aws:verifiedpermissions:policy_store_arn": "arn:aws:verifiedpermissions::111122223333:policy-store/PSt123456789012"
        },
        "destinationEncryptionAlgorithm": "SYMMETRIC_DEFAULT",
        ...
    },
    ...
}
```

Notice that the log entries include `invokedBy` referencing Amazon Verified Permissions' principal, and
`encryptionContext/sourceEncryptionContext/destinationEncryptionContext` being included in the `requestParameters` map.

Example AWS CloudTrail log entry for `DescribeKey`:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "verifiedpermissions.amazonaws.com"
    },
    "eventTime": "2025-09-28T16:51:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "verifiedpermissions.amazonaws.com",
    "userAgent": "verifiedpermissions.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/abcdefgh-0123-ijkl-4567-mnopqrstuvwx"
    },
    ...
}
```

Notice that the log entry includes `invokedBy` referencing Amazon Verified Permissions' principal.

For more information on AWS CloudTrail log entries, see [Understanding AWS CloudTrail events](../../../awscloudtrail/latest/userguide/cloudtrail-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-events.md")
in the _AWS CloudTrail User Guide_.

## Limitations

This topic describes the current limitations of Verified Permissions and utilizing customer managed keys for encryption of resources.

- You cannot disable encryption for a policy store once enabled
- After you create a policy store without encryption, you cannot update the policy store to be encrypted by a customer managed key
- After you revoke Verified Permissions access to a customer managed key for an existing encrypted policy store, there is a potential for stale authorization decisions
- After you create a policy store with a customer managed key, you cannot modify custom encryption context values; they are static values set during encrypted policy store creation

## Troubleshoot Customer Managed Keys in Amazon Verified Permissions

This topic describes common customer managed key related errors you might encounter when using Amazon Verified Permissions and provides troubleshooting steps to resolve them.

### Access Denied: AWS KMS Permission Issue

**Error:** "Service or caller is not authorized to use the provided AWS KMS key, because the resource
does not exist in this Region, no resource-based policies allow access, or a resource-based policy explicitly denies access"

This could either mean that the service or the caller lacks the required `kms:*` action(s) permissions in their IAM policy/AWS KMS
key policy or that the key being referenced does not exist or no longer exists.

#### Troubleshooting with AWS CloudTrail:

- Look for `kms.amazonaws.com` events in AWS CloudTrail
- Search for event name of the AWS KMS operation that was identified to not be allowed (i.e. `Decrypt`, `ReEncrypt`,
  `GenerateDataKeyWithoutPlaintext`, `DescribeKey`, etc.)
- Review the `errorCode` and `errorMessage` fields
- Check `userIdentity` to confirm which principal attempted the operation

To resolve this issue, grant the user or IAM principal the proper AWS KMS operation access permissions in their IAM policy and AWS KMS key policy.
For more information, see [Complete AWS KMS Key Policy](#complete-kms-key-policy "#complete-kms-key-policy").

### Validation Exception: AWS KMS Key Configuration

**Error:** "Configured AWS KMS key does not have a valid configuration"

This means that the key being referenced cannot be used by the service for customer managed key encryption due to its current configuration.
Reasons might include the key being disabled, the key has an unsupported EncryptionAlgorithm, or the key has an unsupported KeyUsage type.

### Throttling Exception: AWS KMS Rate Limits

**Error:** "You have exceeded the rate at which you may call AWS KMS"

This error means that you have exceeded the AWS KMS limit for cryptographic operations for your key:
[https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html](../../../kms/latest/developerguide/requests-per-second.md "../../../kms/latest/developerguide/requests-per-second.md").

## Related Information

- [Managing Verified Permissions Policy stores](policy-stores.md "policy-stores.md")
- [AWS KMS Best Practices](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md")
- [AWS KMS Encryption Context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md")
- [AWS CloudTrail Integration](logging-monitoring.md "logging-monitoring.md")
- [AWS CloudTrail Log Entry Examples](../../../awscloudtrail/latest/userguide/cloudtrail-log-file-examples.md "../../../awscloudtrail/latest/userguide/cloudtrail-log-file-examples.md")
