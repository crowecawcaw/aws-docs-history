# Find all keys for an AWS CloudHSM key store

You can identify the keys in your AWS CloudHSM cluster that serve as key material for your AWS CloudHSM
key store. To do that, use the [key
list](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI.

You can also use the **key list** command to find the AWS KMS for an AWS CloudHSM
key. When AWS KMS creates the key material for a KMS key in your AWS CloudHSM cluster, it writes the
Amazon Resource Name (ARN) of the KMS key in the key label. The **key
list** command returns the `key-reference` and the
`label`.

###### Notes

The following procedures use the AWS CloudHSM Client SDK 5 command line tool, [CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli.md "../../../cloudhsm/latest/userguide/cloudhsm_cli.md"). The CloudHSM CLI replaces
`key-handle` with `key-reference`.

On January 1, 2025, AWS CloudHSM will end support for the Client SDK 3 command line tools, the CloudHSM
Management Utility (CMU) and the Key Management Utility (KMU). For more information on the
differences between the Client SDK 3 command line tools and the Client SDK 5 command line
tool, see [Migrate from Client SDK 3 CMU and KMU to
Client SDK 5 CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md") in the _AWS CloudHSM User Guide_.

To run this procedure you need to disconnect the AWS CloudHSM key store temporarily so you can
log in as the `kmsuser` CU.

1. Disconnect the AWS CloudHSM key store, if it is not already disconnected, then log in as
   `kmsuser`, as explained in [How to disconnect and log in](fix-keystore.md#login-kmsuser-1 "fix-keystore.md#login-kmsuser-1").

###### Note

While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in cryptographic operations will
fail. This action can prevent users from storing and accessing sensitive data. 2. Use the [**key
list**](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md") command in CloudHSM CLI to find all keys for the current user
present in your AWS CloudHSM cluster.

By default, only 10 keys of the currently logged in user are displayed, and only the
`key-reference` and `label` are displayed as output. For more
options, see [key list](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md#chsm-cli-key-list-syntax "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-list.md#chsm-cli-key-list-syntax") in the _AWS CloudHSM User Guide_.

```
`aws-cloudhsm >` `key list`
`{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000000123",
 "attributes": {
 "label": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 }
 },
 {
 "key-reference": "0x0000000000000456",
 "attributes": {
 "label": "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321"
 }
 },.
 ...8 keys later...
 ],
 "total_key_count": 56,
 "returned_key_count": 10,
 "next_token": "10"
 }
}`

```

3. Log out and reconnect the AWS CloudHSM key store as described in [How to log out and reconnect](fix-keystore.md#login-kmsuser-2 "fix-keystore.md#login-kmsuser-2").
