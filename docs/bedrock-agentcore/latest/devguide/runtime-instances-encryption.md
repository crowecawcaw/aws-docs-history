

# Encryption at rest for Runtime Instances
<a name="runtime-instances-encryption"></a>

When you host agents on the **Instances** compute type, your data at rest lives on the Amazon EBS volumes that a capacity provider attaches to your sessions. Amazon EBS creates these volumes in your own AWS account, so EBS encryption protects them.

## Options for encryption at rest
<a name="runtime-instances-encryption-options"></a>

By default, Instances relies on the [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) setting of your AWS account. If you enable EBS encryption by default in a Region, the volumes that your capacity providers create in that Region are encrypted with the default key you configured, with no additional configuration on the capacity provider.

You can also provide a customer managed AWS KMS key on the capacity provider’s volume configuration. Use a customer managed key when you need to control or audit the key that protects your volumes. With a customer managed key you can rotate the key on your own schedule, control access to it through key policies, and audit its use through AWS CloudTrail.

## Encrypting capacity provider volumes with a customer managed KMS key
<a name="runtime-instances-encryption-cmk"></a>

A capacity provider defines its persistent storage as EBS volume configurations. Each volume configuration accepts an `encrypted` flag and a `kmsKeyId`. When AgentCore creates the volume on the session’s first launch, EBS encrypts it with the key you specified. Because the encryption is EBS encryption in your account, the same key protects the volume’s data, any snapshots that EBS creates from it, and any volumes that EBS restores from those snapshots. EBS encryption uses symmetric KMS keys.

### Configuring permissions to use a customer managed KMS key
<a name="runtime-instances-encryption-permissions"></a>

Two principals need permissions on the key:
+  **The principal that calls `CreateCapacityProvider` ** must be able to call `kms:DescribeKey` on each key that you pass in a volume configuration. AgentCore uses this to validate the key when it creates the capacity provider.
+  **The capacity provider operator role** must be able to use the key to create encrypted EBS volumes. For the KMS permissions that EBS requires to create and attach encrypted volumes, see [Requirements for Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html) in the Amazon EBS User Guide.

### Creating a capacity provider with a customer managed KMS key
<a name="runtime-instances-encryption-create"></a>

Specify `encrypted` and `kmsKeyId` in the volume’s `ebsConfiguration` when you create the capacity provider:

```
aws bedrock-agentcore-control create-capacity-provider \
  --name "my-encrypted-capacity-provider" \
  --permissions-configuration '{"capacityProviderOperatorRoleArn": "arn:aws:iam::111122223333:role/CapacityProviderOperatorRole"}' \
  --compute-configuration '{
    "ec2Configuration": {
      "launchTemplateSource": {
        "launchParameters": {
          "operatingSystem": "LINUX_X86_64",
          "instanceRequirements": { "allowedInstanceTypes": ["m5.large"] }
        }
      },
      "vpcConfiguration": {
        "subnets": ["subnet-0123456789abcdef0"],
        "securityGroups": ["sg-0123456789abcdef0"]
      },
      "volumes": [
        {
          "ebsConfiguration": {
            "name": "scratch",
            "sizeGiB": 50,
            "volumeType": "gp3",
            "encrypted": true,
            "kmsKeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
          }
        }
      ]
    }
  }'
```

### Changing the encryption configuration
<a name="runtime-instances-encryption-change"></a>

After a capacity provider is created, only its description can be edited. To use a different key or change the encryption settings, create a new capacity provider with the updated volume configuration and associate your runtimes with it. Existing volumes keep the encryption configuration they were created with.

## Monitoring key use
<a name="runtime-instances-encryption-monitoring"></a>

 AWS CloudTrail logs the KMS API calls made against your customer managed key when EBS creates and attaches encrypted volumes for your sessions. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the AWS Key Management Service Developer Guide.