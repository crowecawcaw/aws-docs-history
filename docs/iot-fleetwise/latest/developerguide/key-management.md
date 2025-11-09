# Key management in AWS IoT FleetWise

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

## AWS IoT FleetWise cloud key management

By default, AWS IoT FleetWise uses AWS managed keys to protect your data in the AWS Cloud. You
can update your settings to use a customer managed key to encrypt data in AWS IoT FleetWise. You can create,
manage, and view your encryption key through AWS Key Management Service (AWS KMS).

AWS IoT FleetWise supports server-side encryption with customer managed keys stored in AWS KMS to encrypt data for the following resources.

| AWS IoT FleetWise resource     | Data type                                                                                                               | Fields that are encrypted at rest with customer managed keys |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Signal catalog                 |                                                                                                                         | description                                                  |
| Attribute                      | description, allowedValues, defaultValue, min, max                                                                      |
| Actuator                       | description, allowedValues, min, max                                                                                    |
| Sensor                         | description, allowedValues, min, max                                                                                    |
| Vehicle model (model manifest) |                                                                                                                         | description                                                  |
| Decoder manifest               |                                                                                                                         | description                                                  |
| CanInterface                   | protocolName, protocolVersion                                                                                           |
| ObdInterface                   | requestMessageId, dtcRequestIntervalSeconds, hasTransmissionEcu, obdStandard, pidRequestIntervalSeconds, useExtendedIds |
| CanSignal                      | factor, isBigEndian, isSigned, length, messageId, offset, startBit                                                      |
| ObdSignal                      | byteLength, offset, pid, pidResponseLength, scaling, serviceMode, startByte, bitMaskLength, bitRightShift               |
| Vehicle                        |                                                                                                                         | attributes                                                   |
| Campaign                       |                                                                                                                         | description                                                  |
| conditionBasedCollectionScheme | expression, conditionLanguageVersion, minimumTriggerIntervalMs, triggerMode                                             |
| TimeBasedCollectionScheme      | periodMs                                                                                                                |
| State template                 |                                                                                                                         | description                                                  |

###### Note

Other data and resources are encrypted using the default encryption with keys managed by AWS IoT FleetWise. This key is created and stored in the AWS IoT FleetWise account.

For more information, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_.

## Enable encryption using KMS keys (console)

To use customer managed keys with AWS IoT FleetWise, you must update your AWS IoT FleetWise settings.

###### To enable encryption using KMS keys (console)

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise/ "https://console.aws.amazon.com/iotfleetwise/").
2. Navigate to **Settings**.
3. In **Encryption**, choose **Edit** to open the **Edit encryption** page.
4. For **Encryption key type**, choose **Choose a different AWS KMS key**. This enables encryption with customer managed keys stored in AWS KMS.

###### Note

You can only use customer managed key encryption for AWS IoT FleetWise resources. This includes the
signal catalog, vehicle model (model manifest), decoder manifest, vehicle, fleet, and
campaign. 5. Choose your KMS key with one of the following options:

    * **To use an existing KMS key** – Choose your KMS key
     alias from the list.
    * **To create a new KMS key** – Choose
     **Create an AWS KMS key**.


    ###### Note

    This opens the AWS KMS console. For more information about creating a KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.

6. Choose **Save** to update your settings.

## Enable encryption using KMS keys (AWS CLI)

You can use the [PutEncryptionConfiguration](../APIReference/API_GetEncryptionConfiguration.md "../APIReference/API_GetEncryptionConfiguration.md") API
operation to enable encryption for your AWS IoT FleetWise account. The following example uses AWS CLI.

To enable encryption, run the following command.

- Replace `kms_key_id` with the ID of the KMS key.

```
aws iotfleetwise put-encryption-configuration \
      --encryption-type KMS_BASED_ENCRYPTION \
      --kms-key-id `kms_key_id`
```

###### Example response

```
{
 "kmsKeyId": "customer_kms_key_id",
 "encryptionStatus": "PENDING",
 "encryptionType": "KMS_BASED_ENCRYPTION"
}

```

## KMS key policy

After you create a KMS key, you must, at minimum, add
the following statement to your KMS key policy for it to work with AWS IoT FleetWise. The AWS IoT FleetWise service principal `iotfleetwise.amazonaws.com` in the KMS key policy statement allows AWS IoT FleetWise to access the KMS key.

```
{
  "Sid": "Allow FleetWise to encrypt and decrypt data when customer managed KMS key based encryption is enabled",
  "Effect": "Allow",
  "Principal": {
    "Service": "iotfleetwise.amazonaws.com"
  },
  "Action": [
    "kms:GenerateDataKey*",
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:DescribeKey",
    "kms:CreateGrant",
    "kms:RetireGrant",
    "kms:RevokeGrant"
  ],
  "Resource": "*"
}
```

As a security best practice, add `aws:SourceArn` and `aws:SourceAccount` condition keys to the KMS key policy. The IAM global condition key `aws:SourceArn` helps ensure that AWS IoT FleetWise uses the KMS key only for service-specific resource Amazon Resource Names (ARNs).

If you set the value of `aws:SourceArn`, it must always be `arn:aws:iotfleetwise:us-east-1:account_id:*`. This allows the KMS key to access all AWS IoT FleetWise resources for this AWS account. AWS IoT FleetWise supports one KMS key per account for all resources in that AWS Region. Using any other value for the `SourceArn`, or not using the wildcard (\*) for the ARN resource field, prevents AWS IoT FleetWise from accessing the KMS key.

The value of `aws:SourceAccount` is your account ID, which is used to further restrict the KMS key so that it can only be used for your specific account. If you add `aws:SourceAccount` and `aws:SourceArn` condition keys to the KMS key, make sure the key is not used by any other service or account. This helps avoid failures.

The following policy includes a service principal (an identifier for a service), as well as `aws:SourceAccount` and `aws:SourceArn` set up for use based on the AWS Region and your account ID.

```
{
  "Sid": "Allow use of the key",
  "Effect": "Allow",
  "Principal": {
    "Service": "iotfleetwise.amazonaws.com"
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "aws:SourceAccount": "AWS-account-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:iotfleetwise:region:AWS-account-ID:*"
    }
  }
}
```

For more information about editing a KMS key policy for use with AWS IoT FleetWise, see [Changing a
key policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in the _AWS Key Management Service Developer Guide_.

###### Important

When you add the new sections to your KMS key policy, don't change any existing
sections in the policy. AWS IoT FleetWise can’t perform operations to your data if encryption is enabled for AWS IoT FleetWise and any of the following is true:

- The KMS key is disabled or deleted.
- The KMS key policy isn't correctly configured for the service.

## Permissions for AWS KMS encryption

If you enabled AWS KMS encryption, you must specify permissions in the role policy so that you can call AWS IoT FleetWise APIs. The following policy allows access to all AWS IoT FleetWise actions, as well as AWS KMS specific permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotfleetwise:*",
 "kms:GenerateDataKey*",
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:DescribeKey"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy statement is required for your role to invoke encryption APIs. This policy statement allows `PutEncryptionConfiguration` and `GetEncryptionConfiguration` actions from AWS IoT FleetWise.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotfleetwise:GetEncryptionConfiguration",
 "iotfleetwise:PutEncryptionConfiguration",
 "kms:GenerateDataKey*",
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:DescribeKey"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Recovery after AWS KMS key deletion

If you delete an AWS KMS key after enabling encryption with AWS IoT FleetWise, you must reset your account by deleting all data before using AWS IoT FleetWise again. You can use the list and delete API operations to clean up resources in your account.

###### To clean up resources in your account

1. Use list APIs with the `listResponseScope` parameter set to `METADATA_ONLY`. This provides a list of resources, including resource names and other metadata such as ARNs and timestamps.
2. Use delete APIs to remove individual resources.

You must clean up resources in the following order.

1. Campaigns
   1. List all campaigns with the `listResponseScope` parameter set to `METADATA_ONLY`.
   2. Delete the campaigns.

2. Fleets and vehicles
   1. List all fleets with the `listResponseScope` parameter set to `METADATA_ONLY`.
   2. List all vehicles for each fleet with the `listResponseScope` parameter set to `METADATA_ONLY`.
   3. Disassociate all vehicles from each fleet.
   4. Delete the fleets.
   5. Delete the vehicles.

3. Decoder manifests
   1. List all decoder manifests with the `listResponseScope` parameter set to `METADATA_ONLY`.
   2. Delete all decoder manifests.

4. Vehicle models (model manifests)
   1. List all vehicle models with the `listResponseScope` parameter set to `METADATA_ONLY`.
   2. Delete all vehicle models.

5. State templates
   1. List all state templates with the `listResponseScope` parameter set to `METADATA_ONLY`.
   2. Delete all state templates.

6. Signal catalogs
   1. List all signal catalogs.
   2. Delete all signal catalogs.
