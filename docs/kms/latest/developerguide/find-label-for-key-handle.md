# Find the KMS key for an AWS CloudHSM key

If you know the key reference or ID of a key that the `kmsuser` owns in the
cluster, you can use that value to identify the associated KMS key in your AWS CloudHSM key
store.

When AWS KMS creates the key material for a KMS key in your AWS CloudHSM cluster, it writes the
Amazon Resource Name (ARN) of the KMS key in the key label. Unless you have changed the
label value, you can use the [key
list](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI to identify the KMS key associated with the AWS CloudHSM
key.

###### Notes

The following procedures use the AWS CloudHSM Client SDK 5 command line tool, [CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli.md "../../../cloudhsm/latest/userguide/cloudhsm_cli.md"). The CloudHSM CLI replaces
`key-handle` with `key-reference`.

On January 1, 2025, AWS CloudHSM will end support for the Client SDK 3 command line tools, the CloudHSM
Management Utility (CMU) and the Key Management Utility (KMU). For more information on the
differences between the Client SDK 3 command line tools and the Client SDK 5 command line
tool, see [Migrate from Client SDK 3 CMU and KMU to
Client SDK 5 CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md") in the _AWS CloudHSM User Guide_.

To run these procedures you need to disconnect the AWS CloudHSM key store temporarily so you can
log in as the `kmsuser` CU.

###### Note

While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in cryptographic operations will
fail. This action can prevent users from storing and accessing sensitive data.

###### Topics

- [Identify the KMS key associated with a key
  reference](#key-reference-filter "#key-reference-filter")
- [Identify the KMS key associated with a backing key
  ID](#backing-key-id-filter "#backing-key-id-filter")

## Identify the KMS key associated with a key

reference

The following procedures demonstrate how to use the [**key
list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI with the `key-reference` attribute filter to find
the key in your cluster that serves as key material for a particular KMS key in your
AWS CloudHSM key store.

1. Disconnect the AWS CloudHSM key store, if it is not already disconnected, then log in as
   `kmsuser`, as explained in [How to disconnect and log in](fix-keystore.md#login-kmsuser-1 "fix-keystore.md#login-kmsuser-1").
2. Use the [**key
   list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI to filter by the `key-reference`
   attribute. Specify the `verbose` argument to include all attributes
   and key information for the matched key. If you don't specify the `verbose`
   argument, the **key list** operation only returns the matched key's
   key-reference and label attribute.

Before running this command, replace the example `key-reference`
with a valid one from your account.

```
`aws-cloudhsm >` `key list --filter attr.key-reference="`0x0000000000120034`" --verbose`
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
 "**label": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab**",
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

[Show moreShow less](# "#")

## Identify the KMS key associated with a backing key

ID

All CloudTrail log entries for cryptographic operations with a KMS key in an AWS CloudHSM key store
include an `additionalEventData` field with the `customKeyStoreId` and
`backingKeyId`. The value returned in the `backingKeyId` field
correlates to the CloudHSM key `id` attribute. You can filter the [**key
list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") operation by the `id` attribute to identify the KMS key
associated with a specific `backingKeyId`.

1. Disconnect the AWS CloudHSM key store, if it is not already disconnected, then log in as
   `kmsuser`, as explained in [How to disconnect and log in](fix-keystore.md#login-kmsuser-1 "fix-keystore.md#login-kmsuser-1").
2. Use the [**key
   list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI with the attribute filter to find
   the key in your cluster that serves as key material for a particular KMS key in your
   AWS CloudHSM key store.

The following example demonstrates how to filter by the `id` attribute.
AWS CloudHSM recognizes the `id` value as a hexadecimal value. To filter the
**key list** operation by the `id` attribute, you must
first convert the `backingKeyId` value that you identified in your CloudTrail log
entry into a format that AWS CloudHSM recognizes.

    1. Use the following Linux command to convert the `backingKeyId` into a
     hexadecimal representation.



    ```
    `echo `backingKeyId` | tr -d '\n' | xxd -p`
    ```

    The following example demonstrates how to convert the
     `backingKeyId` byte array into a hexadecimal representation.



    ```
    `echo `5890723622dc15f699aa9ab2387a9f744b2b884c18b2186ee8ada4f556a2eb9d` | tr -d '\n' | xxd -p`
    `35383930373233363232646331356636393961613961623233383761396637343462326238383463313862323138366565386164613466353536613265623964`
    ```
    2. Prepend the hexadecimal representation of the `backingKeyId` with
     `0x`.



    ```
    **0x**35383930373233363232646331356636393961613961623233383761396637343462326238383463313862323138366565386164613466353536613265623964
    ```
    3. Use the converted `backingKeyId` value to filter by the
     `id` attribute. Specify the `verbose` argument to include all attributes
     and key information for the matched key. If you don't specify the `verbose`
     argument, the **key list** operation only returns the matched key's
     key-reference and label attribute.



    ```
    `aws-cloudhsm >` `key list --filter attr.id="`**0x**35383930373233363232646331356636393961613961623233383761396637343462326238383463313862323138366565386164613466353536613265623964`" --verbose`
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
     "**label": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab**",
     "id": "`**0x**35383930373233363232646331356636393961613961623233383761396637343462326238383463313862323138366565386164613466353536613265623964`",
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

[Show moreShow less](# "#")
