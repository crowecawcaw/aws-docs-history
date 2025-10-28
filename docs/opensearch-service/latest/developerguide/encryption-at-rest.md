# Encryption of data at rest for Amazon OpenSearch Service

OpenSearch Service domains offer encryption of data at rest, a security feature that helps prevent
unauthorized access to your data. The feature uses AWS Key Management Service (AWS KMS) to store and manage your
encryption keys and the Advanced Encryption Standard algorithm with 256-bit keys (AES-256) to
perform the encryption. If enabled, the feature encrypts the following aspects of a
domain:

- All indexes (including those in UltraWarm storage)
- OpenSearch logs
- Swap files
- All other data in the application directory
- Automated snapshots
  The following are _not_ encrypted when you enable
  encryption of data at rest, but you can take additional steps to protect them:

- Manual snapshots: You currently can't use AWS KMS keys to encrypt manual snapshots. You
  can, however, use server-side encryption with S3-managed keys or KMS keys to encrypt the
  bucket you use as a snapshot repository. For instructions, see [Registering a manual snapshot
  repository](managedomains-snapshot-registerdirectory.md "managedomains-snapshot-registerdirectory.md").
- Slow logs and error logs: If you [publish logs](createdomain-configure-slow-logs.md "createdomain-configure-slow-logs.md") and want to encrypt them, you can encrypt their CloudWatch Logs log group
  using the same AWS KMS key as the OpenSearch Service domain. For more information, see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the _Amazon CloudWatch Logs User Guide_.

###### Note

You can't enable encryption at rest on an existing domain if UltraWarm or cold storage
is enabled on the domain. You must first disable UltraWarm or cold storage, enable
encryption at rest, and then re-enable UltraWarm or cold storage. If you want to retain
indexes in UltraWarm or cold storage, you must move them to hot storage before disabling
UltraWarm or cold storage.

OpenSearch Service supports only symmetric encryption KMS keys, not asymmetric ones. To learn how to
create symmetric keys, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_.

Regardless of whether encryption at rest is enabled, all domains automatically encrypt
[custom packages](custom-packages.md "custom-packages.md") using AES-256 and OpenSearch Service-managed
keys.

## Permissions

To use the OpenSearch Service console to configure encryption of data at rest, you must have read
permissions to AWS KMS, such as the following identity-based policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:List*",
 "kms:Describe*"
 ],
 "Resource": "*"
 }
 ]
}`

```

If you want to use a key other than the AWS owned key, you must also have permissions
to create [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") for the key. These permissions typically take the form of a resource-based
policy that you specify when you create the key.

If you want to keep your key exclusive to OpenSearch Service, you can add the [kms:ViaService](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service") condition to that key policy:

```
"Condition": {
  "StringEquals": {
    "kms:ViaService": "es.`us-west-1`.amazonaws.com"
  },
  "Bool": {
    "kms:GrantIsForAWSResource": "true"
  }
}
```

For more information, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

## Enabling encryption of data at rest

Encryption of data at rest on new domains requires either OpenSearch or Elasticsearch 5.1
or later. Enabling it on existing domains requires either OpenSearch or Elasticsearch 6.7 or
later.

###### To enable encryption of data at rest (console)

1. Open the domain in the AWS console, then choose **Actions** and
   **Edit security configuration**.
2. Under **Encryption**, select **Enable encryption of data at
   rest**.
3. Choose an AWS KMS key to use, then choose **Save changes**.

You can also enable encryption through the configuration API. The following request
enables encryption of data at rest on an existing domain:

```
{
   "ClusterConfig":{
      "EncryptionAtRestOptions":{
         "Enabled": true,
         "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:alias/my-key"
      }
   }
}
```

## Disabled or deleted KMS key

If you disable or delete the key that you used to encrypt a domain, the domain becomes
inaccessible. OpenSearch Service sends you a [notification](managedomains-notifications.md "managedomains-notifications.md") informing you that it can't access the KMS key. Re-enable the key
immediately to access your domain.

The OpenSearch Service team can't help you recover your data if your key is deleted. AWS KMS deletes
keys only after a waiting period of at least seven days. If your key is pending deletion,
either cancel deletion or take a [manual
snapshot](managedomains-snapshots.md "managedomains-snapshots.md") of the domain to prevent loss of data.

## Disabling encryption of data at rest

After you configure a domain to encrypt data at rest, you can't disable the setting.
Instead, you can take a [manual snapshot](managedomains-snapshots.md "managedomains-snapshots.md") of
the existing domain, [create another domain](createupdatedomains.md#createdomains "createupdatedomains.md#createdomains"), migrate
your data, and delete the old domain.

## Monitoring domains that encrypt data at rest

Domains that encrypt data at rest have two additional metrics: `KMSKeyError`
and `KMSKeyInaccessible`. These metrics appear only if the domain encounters a
problem with your encryption key. For full descriptions of these metrics, see [Cluster
metrics](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-cluster-metrics "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-cluster-metrics"). You can view them using
either the OpenSearch Service console or the Amazon CloudWatch console.

###### Tip

Each metric represents a significant problem for a domain, so we recommend that you
create CloudWatch alarms for both. For more information, see [Recommended CloudWatch alarms for Amazon OpenSearch Service](cloudwatch-alarms.md "cloudwatch-alarms.md").

## Other considerations

- Automatic key rotation preserves the properties of your AWS KMS keys, so the rotation
  has no effect on your ability to access your OpenSearch data. Encrypted OpenSearch Service domains
  don't support manual key rotation, which involves creating a new key and updating any
  references to the old key. To learn more, see [Rotate AWS KMS keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the _AWS Key Management Service Developer Guide_.
- Certain instance types don't support encryption of data at rest. For details, see
  [Supported instance types in Amazon OpenSearch Service](supported-instance-types.md "supported-instance-types.md").
- Domains that encrypt data at rest use a different repository name for their
  automated snapshots. For more information, see [Restoring snapshots](managedomains-snapshot-restore.md "managedomains-snapshot-restore.md").
- While we highly recommend enabling encryption at rest, it can add additional CPU
  overhead and a few milliseconds of latency. Most use cases aren't sensitive to these
  differences, however, and the magnitude of impact depends on the configuration of your
  cluster, clients, and usage profile.
