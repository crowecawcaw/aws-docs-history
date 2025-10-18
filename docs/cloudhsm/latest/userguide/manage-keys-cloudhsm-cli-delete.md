# Delete keys using CloudHSM CLI

Use the example in this topic to delete a key with [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md"). Only key owners can delete keys.

###### Topics

* [Example: Delete a key](#cloudhsm-cli-delete-keys-example "#cloudhsm-cli-delete-keys-example")
* [Related topics](#cloudhsm-cli-delete-keys-seealso "#cloudhsm-cli-delete-keys-seealso")

## Example: Delete a key


1. Run the **key list** command to identify the key you want to delete:



```
`aws-cloudhsm >` `key list --filter attr.label="my_key_to_delete" --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000540011",
 "key-info": {
 "key-owners": [
 {
 "username": "my_crypto_user",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "my_key_to_delete",
 "id": "",
 "check-value": "0x29bbd1",
 "class": "private-key",
 "encrypt": false,
 "decrypt": true,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": false,
 "unwrap": true,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1217,
 "public-exponent": "0x010001",
 "modulus": "0x8b3a7c20618e8be08220ed8ab2c8550b65fc1aad8d4cf04fbf2be685f97eeb78fcbbad9b02cd91a3b15e990c2a7c7cdeff0b730576c6c5630a8509a778a96acbc7c36931e9a86e8956fbd07f0863404ce06c8bd68256784be9f5b258a35e229ce7f630228b9323b4e1f14a0384ead90bdf07dc762f710fc5663887d0787ad98d64bbe303134f545acb2ab194fee6edaecd4dd5cf31ff7f7491e37d7a850ab23247414b42d9abdd5de89b78fd464560df29a90607e9d462f21b22365da419021fb9f28ea7e6fdb1f40bf83aaf1636fba5e475ad19889cfe3f28186a969b4826c39466c0855c974d1fb723d111e4a32ab6e32b3129bc95c9206fced160015d8b2f",
 "modulus-size-bits": 2048
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }`
```
2. After identifying the key, run the **key delete** with the key's unique `label` attribute to delete the key:



```
`aws-cloudhsm >` `key delete --filter attr.label="my_key_to_delete"``{
 "error_code": 0,
 "data": {
 "message": "Key deleted successfully"
 }
}`
```
3. Run the **key list** command with the key's unique `label` attribute and confirm the key has been deleted. As shown in the following example, no key with the label `my_key_to_delete` is in the HSM cluster:



```
`aws-cloudhsm >` `key list --filter attr.label="my_key_to_delete"``{
 "error_code": 0,
 "data": {
 "matched_keys": [],
 "total_key_count": 0,
 "returned_key_count": 0
 }
}`
```

## Related topics



* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
* [Delete a key with CloudHSM CLI](cloudhsm_cli-key-delete.md "cloudhsm_cli-key-delete.md")
