# Share and unshare keys using CloudHSM CLI

Use the commands in this topic to share and unshare keys in [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md"). In AWS CloudHSM, the crypto user (CU) who creates the key owns it. 
 The owner can use the **key share** and **key unshare** commands to share and unshare the key with other CUs. 
 Users with whom the key is shared can use the key in cryptographic operations, but they cannot export the key, delete the key, or share it with other users.

Before you can share a key, you must log in to the HSM as the crypto user (CU) who owns the key.

###### Topics

* [Example: Sharing and unsharing a key](#w20aac15c21c11b9 "#w20aac15c21c11b9")
* [Related topics](#cloudhsm-cli-share-keys-seealso "#cloudhsm-cli-share-keys-seealso")

## Example: Sharing and unsharing a key


The following example shows how to share and unshare a key with crypto user (CU) `alice`. Along with the **key share** and **key unshare** commands, sharing and unsharing commands 
 also requires a specific key using [CloudHSM CLI key filters](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md") and the specific username of the user whom the key will be shared or unshared with.

1. Start by running the **key list** command with a filter to return a specific key and see whom the key is already shared with.



```
`aws-cloudhsm >` `key list --filter attr.label="rsa_key_to_share" --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000001c0686",
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
 },
 {
 "username": "cu1",
 "key-coverage": "full"
 },
 {
 "username": "cu4",
 "key-coverage": "full"
 },
 {
 "username": "cu5",
 "key-coverage": "full"
 },
 {
 "username": "cu6",
 "key-coverage": "full"
 },
 {
 "username": "cu7",
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
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```
2. View the `shared-users` output to identify whom the key is currently shared with.
3. To share this key with crypto user (CU) `alice`, enter the following command:



```
`aws-cloudhsm >` `key share --filter attr.label="rsa_key_to_share" attr.class=private-key --username alice --role crypto-user``{
 "error_code": 0,
 "data": {
 "message": "Key shared successfully"
 }
}`
```

Note that, along with the **key share** command, this command uses the unique label of the key and the name of the user whom the key will be shared with.
4. Run the **key list** command to confirm that the key has been shared with `alice`:



```
`aws-cloudhsm >` `key list --filter attr.label="rsa_key_to_share" --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000001c0686",
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
 },
 {
 "username": "cu1",
 "key-coverage": "full"
 },
 {
 "username": "cu4",
 "key-coverage": "full"
 },
 {
 "username": "cu5",
 "key-coverage": "full"
 },
 {
 "username": "cu6",
 "key-coverage": "full"
 },
 {
 "username": "cu7",
 "key-coverage": "full"
 },
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
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```
5. To unshare the same key with `alice`, run the following **unshare** command:



```
`aws-cloudhsm >` `key unshare --filter attr.label="rsa_key_to_share" attr.class=private-key --username alice --role crypto-user``{
 "error_code": 0,
 "data": {
 "message": "Key unshared successfully"
 }
}`
```

Note that, along with the **key unshare** command, this command uses the unique label of the key and the name of the user whom the key will be shared with.
6. Run the **key list** command again and confirm the key was unshared with crypto user `alice`:



```
`aws-cloudhsm >` `key list --filter attr.label="rsa_key_to_share" --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000001c0686",
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
 },
 {
 "username": "cu1",
 "key-coverage": "full"
 },
 {
 "username": "cu4",
 "key-coverage": "full"
 },
 {
 "username": "cu5",
 "key-coverage": "full"
 },
 {
 "username": "cu6",
 "key-coverage": "full"
 },
 {
 "username": "cu7",
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
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```

## Related topics



* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
* [Share a key using CloudHSM CLI](cloudhsm_cli-key-share.md "cloudhsm_cli-key-share.md")
* [Unshare a key using CloudHSM CLI](cloudhsm_cli-key-unshare.md "cloudhsm_cli-key-unshare.md")
* [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
