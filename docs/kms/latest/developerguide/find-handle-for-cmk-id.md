# Find the AWS CloudHSM key for a KMS key

You can use the KMS key ID of a KMS key in an AWS CloudHSM key store to identify the key in
your AWS CloudHSM cluster that serves as its key material.

When AWS KMS creates the key material for a KMS key in your AWS CloudHSM cluster, it writes the
Amazon Resource Name (ARN) of the KMS key in the key label. Unless you have changed the
label value, you can use the [**key
list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI to find the key-resource and id of the key
material for the KMS key.

All CloudTrail log entries for cryptographic operation with a KMS key in an AWS CloudHSM key store
include an `additionalEventData` field with the `customKeyStoreId` and
`backingKeyId`. The value returned in the `backingKeyId` field is the
`id` AWS CloudHSM key attribute. You can filter the **key list** AWS CloudHSM
CLI operation by KMS key ARN to identify the CloudHSM key `id` attribute
associated with a specific KMS key.

To run this procedure, you need to disconnect the AWS CloudHSM key store temporarily so you can
log in as the `kmsuser` CU.

###### Notes

The following procedures use the AWS CloudHSM Client SDK 5 command line tool, [CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli.md "../../../cloudhsm/latest/userguide/cloudhsm_cli.md"). The CloudHSM CLI replaces
`key-handle` with `key-reference`.

On January 1, 2025, AWS CloudHSM will end support for the Client SDK 3 command line tools, the CloudHSM
Management Utility (CMU) and the Key Management Utility (KMU). For more information on the
differences between the Client SDK 3 command line tools and the Client SDK 5 command line
tool, see [Migrate from Client SDK 3 CMU and KMU to
Client SDK 5 CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md") in the _AWS CloudHSM User Guide_.

1. Disconnect the AWS CloudHSM key store, if it is not already disconnected, then log in as
   `kmsuser`, as explained in [How to disconnect and log in](fix-keystore.md#login-kmsuser-1 "fix-keystore.md#login-kmsuser-1").

###### Note

While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in cryptographic operations will
fail. This action can prevent users from storing and accessing sensitive data. 2. Use the [**key
list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI and filter by `label` to
find the KMS key for a particular key in your AWS CloudHSM cluster. Specify the
`verbose` argument to include all attributes and key information for the
matched key. If you don't specify the `verbose` argument, the **key
list** operation only returns the matched key's key-reference and label
attributes.

The following example demonstrates how to filter by the `label` attribute
that stores the KMS key ARN. Before running this command, replace the example KMS key
ARN with a valid one from your account.

```
`aws-cloudhsm >` `key list --filter attr.label="`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`" --verbose`
`{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000120034",
 "key-info": {
 "key-owners": [
 {
 "username": "kmsuser",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "aes",
 "label": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "id": "`**0x**backing-key-id`",
 "check-value": "0x29bbd1",
 "class": "my_test_key",
 "encrypt": true,
 "decrypt": true,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": false,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": false,
 "trusted": false,
 "unwrap": true,
 "verify": false,
 "wrap": true,
 "wrap-with-trusted": false,
 "key-length-bytes": 32
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`

```

3. Log out and reconnect the AWS CloudHSM key store as described in [How to log out and reconnect](fix-keystore.md#login-kmsuser-2 "fix-keystore.md#login-kmsuser-2").
