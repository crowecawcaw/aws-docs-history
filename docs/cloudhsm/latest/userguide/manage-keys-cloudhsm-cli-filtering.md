# Filter keys using CloudHSM CLI

Use the following key commands to utilize the standardized key filtration mechanisms for [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md").

- **key list**
- **key delete**
- **key share**
- **key unshare**
- **key set-attribute**
  To select and/or filter keys with CloudHSM CLI, key commands utilize a standardized filtration mechanism based on
  [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").
  A key or set of keys can be specified in key commands by using one or more AWS CloudHSM attributes that can identify a single key or multiple keys.
  The key filtration mechanism operates only on keys that the currently logged in user owns and shares, as well as all public keys
  in the AWS CloudHSM cluster.

###### Topics

- [Requirements](#chsm-cli-filtering-requirements "#chsm-cli-filtering-requirements")
- [Filtering to find a single key](#chsm-cli-filtering-examples "#chsm-cli-filtering-examples")
- [Filtration Errors](#manage-keys-chsm-cli-filter-error "#manage-keys-chsm-cli-filter-error")
- [Related topics](#manage-keys-chsm-cli-filtering-seealso "#manage-keys-chsm-cli-filtering-seealso")

## Requirements

To filter keys, you must be a logged in as a crypto user (CUs).

## Filtering to find a single key

Please note that in the following examples, each attribute that is used as a filter must be written in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE`.
For example, if you want to filter by the label attribute, you will write `attr.label=my_label`.

###### Example Use a single attribute to find a single key

This example demonstrates how to filter to a single unique key using only a single identifying attribute.

```
`aws-cloudhsm >` `key list --filter attr.label="my_unique_key_label" --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000001c0686",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "alice",
 "key-coverage": "full"
 }
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "my_unique_key_label",
 "id": "",
 "check-value": "0xae8ff0",
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
 "key-length-bytes": 1219,
 "public-exponent": "0x010001",
 "modulus": "0xa8855cba933cec0c21a4df0450ec31675c024f3e65b2b215a53d2bda6dcd191f75729150b59b4d86df58254c8f518f7d000cc04d8e958e7502c7c33098e28da4d94378ef34fb57d1cc7e042d9119bd79be0df728421a980a397095157da24cf3cc2b6dab12225d33fdca11f0c6ed1a5127f12488cda9a556814b39b06cd8373ff5d371db2212887853621b8510faa7b0779fbdec447e1f1d19f343acb02b22526487a31f6c704f8f003cb4f7013136f90cc17c2c20e414dc1fc7bcfb392d59c767900319679fc3307388633485657ce2e1a3deab0f985b0747ef4ed339de78147d1985d14fdd8634219321e49e3f5715e79c298f18658504bab04086bfbdcd3b",
 "modulus-size-bits": 2048
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```

###### Example Use a multiple attributes to find a single key

The following example demonstrates how to find a single key using multiple key attributes.

```
`aws-cloudhsm >` `key list --filter attr.key-type=rsa attr.class=private-key attr.check-value=0x29bbd1 --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000540011",
 "key-info": {
 "key-owners": [
 {
 "username": "cu3",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "cu2",
 "key-coverage": "full"
 }
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "my_crypto_user",
 "id": "",
 "check-value": "0x29bbd1",
 "class": "my_test_key",
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
 }
}`
```

###### Example Filtering to find a set of keys

The following example demonstrates how to filter to find a set of private rsa keys.

```
`aws-cloudhsm >` `key list --filter attr.key-type=rsa attr.class=private-key --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000001c0686",
 "key-info": {
 "key-owners": [
 {
 "username": "my_crypto_user",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "cu2",
 "key-coverage": "full"
 },
 {
 "username": "cu1",
 "key-coverage": "full"
 },
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "rsa_key_to_share",
 "id": "",
 "check-value": "0xae8ff0",
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
 "key-length-bytes": 1219,
 "public-exponent": "0x010001",
 "modulus": "0xa8855cba933cec0c21a4df0450ec31675c024f3e65b2b215a53d2bda6dcd191f75729150b59b4d86df58254c8f518f7d000cc04d8e958e7502c7c33098e28da4d94378ef34fb57d1cc7e042d9119bd79be0df728421a980a397095157da24cf3cc2b6dab12225d33fdca11f0c6ed1a5127f12488cda9a556814b39b06cd8373ff5d371db2212887853621b8510faa7b0779fbdec447e1f1d19f343acb02b22526487a31f6c704f8f003cb4f7013136f90cc17c2c20e414dc1fc7bcfb392d59c767900319679fc3307388633485657ce2e1a3deab0f985b0747ef4ed339de78147d1985d14fdd8634219321e49e3f5715e79c298f18658504bab04086bfbdcd3b",
 "modulus-size-bits": 2048
 }
 },
 {
 "key-reference": "0x0000000000540011",
 "key-info": {
 "key-owners": [
 {
 "username": "my_crypto_user",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "cu2",
 "key-coverage": "full"
 }
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "my_test_key",
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
 "total_key_count": 2,
 "returned_key_count": 2
 }
}`
```

## Filtration Errors

Certain key operations can only be performed on a single key at a time. For these operations, the CloudHSM CLI will provide an error
if the filtration criteria is not sufficiently refined and multiple keys match the criteria.
One such example is shown below with the key delete.

###### Example Filtration Error when matching too many keys

```
`aws-cloudhsm >` `key delete --filter attr.key-type=rsa``{
 "error_code": 1,
 "data": "Key selection criteria matched 48 keys. Refine selection criteria to select a single key."
}`
```

## Related topics

- [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
