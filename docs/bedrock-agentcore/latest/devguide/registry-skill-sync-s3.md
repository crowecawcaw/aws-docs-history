

# Synchronize a skill from Amazon S3

 AWS Agent Registry can read a skill’s content from an Amazon S3 object: a SKILL.md object, or a skill package ZIP object. The registry reads the object when you create the record, when you change its source or its bucket owner, and when you call `UpdateRegistryRecord` with `triggerSynchronization` set to `true`. It reads the object with an IAM role that you provide, or without credentials if the object is public.

## Source URL and mode
<a name="registry-skill-sync-s3-source"></a>

Set the source in `source.fromUrl.url`, as an `s3://<bucket>/<key>` URL. The member that holds the source determines what the registry reads:


| Member | Object | What the record gets | 
| --- | --- | --- | 
|  `descriptors.agentSkillsDefinition.additionalData.skillMd.source`  | A SKILL.md file. The last part of the key must be `SKILL.md` or `skill.md`, for example `s3://amzn-s3-demo-bucket/skills/my-skill/SKILL.md`. | The SKILL.md text, in `skillMd.data`. No package. | 
|  `descriptors.agentSkillsDefinition.additionalData.skillPackage.source`  | A skill package ZIP file, for example `s3://amzn-s3-demo-bucket/skills/my-skill.zip`. The key doesn’t need a `.zip` extension, but the object must be a ZIP archive. | The package, validated as described in [Skill package format and validation](registry-skill-package-format.md), and its SKILL.md in `skillMd.data`. | 

The URL must meet the following rules:
+ It names one object, in the form `s3://<bucket>/<key>`. The key can’t be empty or end with `/`, so you can’t name a prefix or a folder. The registry uses the key exactly as you write it, without URL decoding.
+ It uses a bucket name. Bucket ARNs, access point ARNs, and Multi-Region Access Points aren’t supported, and neither are directory buckets or Amazon S3 on Outposts.
+ The bucket is in the same AWS Region as the registry.
+ It names no object version. Each synchronization reads the object’s current version.
+ Don’t set `repositoryProvider` on an Amazon S3 source.

SKILL.md and package objects have maximum sizes. For the limits, see [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).

## Give the registry access to the object
<a name="registry-skill-sync-s3-access"></a>

Choose one of the following ways for the registry to read the object:
+  **An IAM role in your account** — The registry assumes the role to read the object. Use this for private objects, including objects in another account’s bucket.
+  **No credentials** — The registry reads a public object anonymously. The object must be publicly readable, and you must set the bucket owner’s account in the record, as described in [Read a public object](#registry-skill-sync-s3-public).

### Create the IAM role
<a name="registry-skill-sync-s3-role"></a>

Create a role in the account that you call AWS Agent Registry from. The role must be in your account, even when you write a record to a registry that another account shares with you.

The role’s trust policy allows the `agent-registry.amazonaws.com` service principal to assume the role. When it assumes the role, the registry identifies the record that the synchronization is for, so you can limit the trust policy with the `aws:SourceAccount` and `aws:SourceArn` condition keys. `aws:SourceAccount` is the account that owns the registry, and `aws:SourceArn` is the record’s ARN. The following trust policy allows the registry to assume the role for any record of any registry in account 111122223333 in US East (N. Virginia). To limit it to one registry, replace the first `*` in the ARN pattern with the registry ID.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowAgentRegistrySkillSync",
      "Effect": "Allow",
      "Principal": {
        "Service": "agent-registry.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:agent-registry:us-east-1:111122223333:registry/*/record/*"
        }
      }
    }
  ]
}
```

The role’s permissions policy allows it to read the objects:
+  `s3:GetObject` on the objects. `s3:GetObjectVersion` isn’t needed.
+  `s3:ListBucket` on the bucket. This permission is optional. Without it, Amazon S3 reports a missing object as access denied, and the record’s `statusReason` can’t tell the two cases apart.
+  `kms:Decrypt` on the AWS KMS key, if the objects use server-side encryption with AWS KMS keys (SSE-KMS). We recommend that you allow it only through Amazon S3, with the `kms:ViaService` condition key.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "ReadSkillObjects",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/skills/*"
    },
    {
      "Sid": "ListSkillBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
    },
    {
      "Sid": "DecryptSkillObjects",
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "s3.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}
```

Whatever the role allows, the registry limits each session that it gets from the role to `s3:GetObject` and `s3:ListBucket` on buckets that the expected bucket owner owns, and to `kms:Decrypt` through Amazon S3. Every read also checks that the bucket belongs to the expected owner: the account in `sourceConfiguration.s3.bucketOwnerAccountId` if you set it, or otherwise the role’s account.

### Allow the caller to pass the role
<a name="registry-skill-sync-s3-passrole"></a>

When a `CreateRegistryRecord` or `UpdateRegistryRecord` request includes an Amazon S3 source with an IAM role, the caller needs `iam:PassRole` on the role, even if the request sends the record’s stored role unchanged. The registry passes the role to `agent-registry.amazonaws.com`, for a record of the registry. On `CreateRegistryRecord`, the associated resource is the record ARN pattern `arn:aws:agent-registry:<region>:<account-id>:registry/<registryId>/record/*`, and on `UpdateRegistryRecord`, the record’s ARN. A condition that names one record’s ARN therefore fails on `CreateRegistryRecord`. Use a pattern instead, as in the following policy:

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "PassSkillSourceRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "agent-registry.amazonaws.com"
        },
        "StringLike": {
          "iam:AssociatedResourceARN": "arn:aws:agent-registry:us-east-1:111122223333:registry/*/record/*"
        }
      }
    }
  ]
}
```
+ If the role isn’t in the caller’s account, the request fails with an `AccessDeniedException` and the message `Cross-account pass role is not allowed`.
+ An `UpdateRegistryRecord` request that only sets `triggerSynchronization`, and keeps the stored role, passes no role and needs no `iam:PassRole`.
+ If the registry is encrypted with a customer managed key, a request that sets or synchronizes a full-package source also needs `kms:GenerateDataKey` on the registry’s key. A SKILL.md-only source doesn’t. For more information, see [Set customer managed key policy](registry-kms-key-policy.md).

For all of the permissions that publishers need, see [IAM Permissions](registry-iam-permissions.md).

### Read from a bucket in another account
<a name="registry-skill-sync-s3-cross-account"></a>

The registry can read a bucket that another account owns, with a role in your account:

1. In the bucket’s account, add a bucket policy statement that allows your role `s3:GetObject` on the objects, and optionally `s3:ListBucket` on the bucket.

1. If the objects are encrypted with a customer managed key, allow your role `kms:Decrypt` in the key policy. The registry can’t read an object in another account that is encrypted with the AWS managed key `aws/s3`. For such objects, use server-side encryption with Amazon S3 managed keys (SSE-S3) or a customer managed key.

1. In the record, set `sourceConfiguration.s3.bucketOwnerAccountId` to the bucket’s account ID. Without it, the registry expects the bucket to be in the role’s account, and the read fails.

The following bucket policy, in account 444455556666, allows the role from account 111122223333 to read the skills:

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowRegistrySkillSourceRole",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/skills/*"
    },
    {
      "Sid": "AllowRegistrySkillSourceRoleList",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
    }
  ]
}
```

### Read a public object
<a name="registry-skill-sync-s3-public"></a>

To read a publicly readable object without credentials, omit `credentialProviderConfigurations`, and set `sourceConfiguration.s3.bucketOwnerAccountId` to the 12-digit ID of the account that owns the bucket. A source without credentials and without `bucketOwnerAccountId` fails with a `ValidationException`. The registry can’t read an object anonymously if the object is encrypted with SSE-KMS.

In the console, for **Credential type**, choose **No authorization**. For **Bucket owner account ID**, enter the bucket owner’s account ID. The console prefills that field with the account that you’re signed in to, so change it for a bucket in another account.

```json
{
  "agentSkillsDefinition": {
    "additionalData": {
      "skillMd": {
        "source": {
          "fromUrl": {
            "url": "s3://amzn-s3-demo-bucket/skills/my-skill/SKILL.md"
          }
        }
      },
      "sourceConfiguration": {
        "s3": {
          "bucketOwnerAccountId": "444455556666"
        }
      }
    }
  }
}
```

### Supported encryption and storage classes
<a name="registry-skill-sync-s3-encryption"></a>


| Object | Supported | 
| --- | --- | 
| Encrypted with SSE-S3 | Yes. | 
| Encrypted with SSE-KMS and a customer managed key | Yes. The role needs `kms:Decrypt` on the key, and a key in another account must allow the role in its key policy. | 
| Encrypted with SSE-KMS and the AWS managed key `aws/s3`  | Only when the bucket is in the role’s account. | 
| Encrypted with SSE-C (customer-provided keys) | No. | 
| In an archived storage class that requires a restore before you can read the object | No. Restore the object, or copy it to a storage class that isn’t archived. | 

## Create a record that synchronizes from Amazon S3
<a name="registry-skill-sync-s3-create"></a>

### Console
<a name="registry-skill-sync-s3-create-console"></a>

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. In the **Record source** section, choose **Synchronize from source**.

1. In the **Record details** section, for **Type**, choose **Skills**. The **Descriptor** is set to **Agent skills definition**.

1. For **Source**, choose **Amazon S3**.

1. For **Content type**, choose **Skill markdown** to read a SKILL.md object, or **Skill package** to read a skill package .zip object.

1. For **S3 URI**, choose the object in the Amazon S3 object browser, or enter the URI.

   The object browser lists objects of every kind. You can select only an object that **Content type** accepts: an object named exactly `SKILL.md` or `skill.md` for **Skill markdown**, or an object with the `.zip` extension for **Skill package**.

   If the object browser can’t load, the console warns you and shows a plain **S3 URI** field instead, where you enter the URI yourself. Changing **Content type** clears the object that you chose, because it can no longer meet the new rule.

1. For **Credential type**, choose one of the following:
   +  **IAM Role** – The registry assumes a role to read the object. For **Role ARN**, choose or enter the role. The role must be in your own AWS account. This applies even when another account shared the registry with you. Its trust policy must allow AWS Agent Registry to assume the role. The role must also grant read access to the object. For more information about the role and its policies, see [Create the IAM role](#registry-skill-sync-s3-role).
   +  **No authorization** – The registry reads the object anonymously, so the object must be publicly readable. For more information, see [Read a public object](#registry-skill-sync-s3-public).

1. For **Bucket owner account ID**, enter the 12-digit ID of the AWS account that owns the bucket. The field is optional with **IAM Role**: leave it empty for a bucket in the role’s own account, and fill it in for a bucket in another account. It’s required with **No authorization**, and the console prefills it with the account that you’re signed in to.

1. (Optional) In the **Tags** section, add tags to the record.

1. Choose **Create record**.

The record is in `CREATING` status while the registry reads the object and, for **Skill package**, validates the package. Then it moves to `DRAFT`, or to `CREATE_FAILED`. To see the reason, choose the record’s **Status** in the **Record details** section of the record detail page. The record takes its name and description from the `name` and `description` in SKILL.md, and takes them again on every synchronization.

**Note**  
The console sets the source’s signing service to `s3`, and the registry determines the AWS Region. The **Service** and **Region** fields of an MCP or agent endpoint therefore don’t appear for a skill source.

### AWS CLI
<a name="registry-skill-sync-s3-create-cli"></a>

Save the descriptors in a file, such as `descriptors.json`. This example synchronizes a full skill package:

```json
{
  "agentSkillsDefinition": {
    "additionalData": {
      "skillPackage": {
        "source": {
          "fromUrl": {
            "url": "s3://amzn-s3-demo-bucket/skills/my-skill.zip",
            "credentialProviderConfigurations": [
              {
                "credentialProviderType": "IAM",
                "credentialProvider": {
                  "iamCredentialProvider": {
                    "roleArn": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead"
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

To synchronize only SKILL.md, use `skillMd` in place of `skillPackage`, and a URL that names the SKILL.md object. To read from a bucket in another account, add `"sourceConfiguration": {"s3": {"bucketOwnerAccountId": "444455556666"}}` to `additionalData`.

For an Amazon S3 source, `iamCredentialProvider` takes only `roleArn`. If you set `service`, it must be `s3`, and if you set `region`, it must be the registry’s Region.

Create the record:

```bash
aws agent-registry-control create-registry-record \
  --registry-id <registryId> \
  --name "my-skill" \
  --record-type SKILL \
  --record-version "1.0" \
  --descriptors file://descriptors.json \
  --region us-east-1
```

The response has the status `CREATING`. To see the result, call `get-registry-record` until the status is `DRAFT` or `CREATE_FAILED`.

### AWS SDK
<a name="registry-skill-sync-s3-create-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to create the record and wait for the synchronization to finish:

```python
import time

import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry_record(
    registryId='<registryId>',
    name='my-skill',
    recordType='SKILL',
    recordVersion='1.0',
    descriptors={
        'agentSkillsDefinition': {
            'additionalData': {
                'skillPackage': {
                    'source': {
                        'fromUrl': {
                            'url': 's3://amzn-s3-demo-bucket/skills/my-skill.zip',
                            'credentialProviderConfigurations': [{
                                'credentialProviderType': 'IAM',
                                'credentialProvider': {
                                    'iamCredentialProvider': {
                                        'roleArn': 'arn:aws:iam::111122223333:role/RegistrySkillSourceRead'
                                    }
                                }
                            }]
                        }
                    }
                }
            }
        }
    },
)
record_arn = response['recordArn']

while True:
    record = client.get_registry_record(registryId='<registryId>', recordId=record_arn)
    if record['status'] not in ('CREATING', 'UPDATING'):
        break
    time.sleep(5)

print(record['status'], record.get('statusReason', ''))
print(record.get('synchronizedSource'))
```

## Synchronize again or change the source
<a name="registry-skill-sync-s3-resync"></a>

The registry doesn’t watch the object for changes. To read it again, request a synchronization. An update that sets a different source URL or role, or sets, changes, or removes the bucket’s owner, also starts a synchronization on its own. An update that sends the stored source back unchanged doesn’t start one.

A synchronization runs asynchronously, like the first one. The record moves to `UPDATING`, and then to `DRAFT` if the content changed, back to its previous status if the SKILL.md and package didn’t change, or to `UPDATE_FAILED`. If an `APPROVED` record’s content changes, the update creates a new `DRAFT` revision, and discovery keeps returning the approved revision until the new one is approved. A failed synchronization keeps the record’s previous content and package. If the synchronization was to replace an uploaded package, `GetRegistryRecord` returns no download URL until a synchronization succeeds. For more information, see [Packages during an update](registry-skill-packages.md#registry-skill-packages-update-in-progress).

### Console
<a name="registry-skill-sync-s3-resync-console"></a>

To synchronize an unchanged source again, choose **Manage**, choose **Synchronization**, and then choose **Sync** to confirm.

Use the edit form to point the record at another object, to change how the registry reads it, or to give an existing record its first Amazon S3 source. The form holds a skill record’s source in the **Skill content** section, along with the record’s other content sources.

1. On the record detail page, choose **Manage**, and then choose **Edit**.

1. In the **Skill content** section, for **Skill content source**, choose **Synchronize from source**. The console warns you that saving with a different source replaces the record’s content and removes the previous source, including an uploaded package.

1. For **Additional content**, choose **Skill definition** to keep or add a structured skill definition in JSON, or **None**. SKILL.md always comes from the source, so the editor for it isn’t offered here. If the record has a definition and you choose **None**, saving removes it.

1. For **Source**, choose **Amazon S3**.

1. Set **Content type**, **S3 URI**, **Credential type**, and **Bucket owner account ID**, as described in [Create a record that synchronizes from Amazon S3](#registry-skill-sync-s3-create-console).

   The form opens on the record’s stored source, and keeps each source’s location separately, so you can switch between **Amazon S3** and **GitHub** without losing either one.

1. (Optional) Select **Trigger synchronization** to read the source on save. A new or changed source synchronizes on its own, so you need this only to read an unchanged source again.

1. Choose **Save changes**.

Because the save starts a synchronization, **Save and submit for approval** isn’t available, and the console explains why. Save your changes, wait for the synchronization to finish, and then submit the record for approval.

### AWS CLI
<a name="registry-skill-sync-s3-resync-cli"></a>

To read the object again, update the record with `triggerSynchronization`:

```bash
aws agent-registry-control update-registry-record \
  --registry-id <registryId> \
  --record-id <recordId> \
  --trigger-synchronization \
  --region us-east-1
```

On `UpdateRegistryRecord`, you wrap each level of the descriptors in `optionalValue`. The following `--descriptors` value moves a full-package source to another object:

```json
{
  "optionalValue": {
    "agentSkillsDefinition": {
      "optionalValue": {
        "additionalData": {
          "optionalValue": {
            "skillPackage": {
              "optionalValue": {
                "source": {
                  "fromUrl": {
                    "url": "s3://amzn-s3-demo-bucket/skills/my-skill-v2.zip",
                    "credentialProviderConfigurations": [
                      {
                        "credentialProviderType": "IAM",
                        "credentialProvider": {
                          "iamCredentialProvider": {
                            "roleArn": "arn:aws:iam::111122223333:role/RegistrySkillSourceRead"
                          }
                        }
                      }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

When you move the source to another bucket, the record keeps its `sourceConfiguration`. If the new bucket has a different owner, send the new owner in the same request, as `"sourceConfiguration": {"optionalValue": {"s3": {"bucketOwnerAccountId": "444455556666"}}}` in `additionalData`. Or send `"sourceConfiguration": {}` so that the registry expects the role’s account.

To switch between a SKILL.md source and a package source, set the new source and remove the other one in the same request. Send `"skillPackage": {}` in `additionalData` to remove a package source, or `"skillMd": {"optionalValue": {"source": {}}}` to remove a SKILL.md source.

## Check what the registry read
<a name="registry-skill-sync-s3-result"></a>

After a successful synchronization, `GetRegistryRecord` returns `synchronizedSource.s3` with the following members:
+  `url` — The source URL that the registry read.
+  `synchronizedAt` — When the registry read it.
+  `versionId` — The object’s version ID, if the bucket has versioning enabled.
+  `eTag` — The object’s entity tag, without quotes, when there’s no version ID. For a SKILL.md source on a registry that is encrypted with a customer managed key, the registry doesn’t record the entity tag.

```json
"synchronizedSource": {
    "s3": {
        "url": "s3://amzn-s3-demo-bucket/skills/my-skill.zip",
        "synchronizedAt": "2026-11-19T17:00:18Z",
        "eTag": "9b2cf535f27731c974343645a3985328"
    }
}
```

A failed synchronization leaves `synchronizedSource` as it was. After you change the source, it shows the previous source until a synchronization of the new one succeeds.

## Troubleshoot an Amazon S3 source
<a name="registry-skill-sync-s3-errors"></a>

When a synchronization fails, the record moves to `CREATE_FAILED` or `UPDATE_FAILED`, and `statusReason` starts with `Unable to read the S3 source object:`, `Unable to assume the provided IAM role`, or `Unable to process the registry record because the KMS key associated with the registry`, or describes the problem with the package or SKILL.md. The status reasons never name the bucket, the key, or the role. The following table lists common causes.


| Status reason mentions | What to check | 
| --- | --- | 
| Unable to assume the provided IAM role | The role exists, its trust policy allows `agent-registry.amazonaws.com`, and the `aws:SourceAccount` and `aws:SourceArn` conditions match the record. | 
| Access was denied | The role allows `s3:GetObject` on the object, a bucket in another account allows the role in its bucket policy, and `bucketOwnerAccountId` (or the role’s account, if you didn’t set it) owns the bucket. Without `s3:ListBucket`, a missing object is also reported as access denied. | 
| The bucket or the object does not exist | The URL names the right bucket and key. | 
| The bucket must be in the registry’s Region | The bucket is in the same Region as the registry. | 
| The AWS KMS key could not be used | The key is enabled, the role is allowed `kms:Decrypt` through Amazon S3, and a key in another account allows the role. | 

For package and SKILL.md problems, see [How validation failures appear](registry-skill-package-format.md#registry-skill-package-format-failures).