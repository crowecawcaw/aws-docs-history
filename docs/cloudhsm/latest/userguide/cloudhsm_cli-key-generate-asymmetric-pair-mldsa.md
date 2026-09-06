# Generate an asymmetric ML-DSA key pair with CloudHSM CLI

Use the **key generate-asymmetric-pair ml-dsa** command in CloudHSM CLI to generate an asymmetric ML-DSA key pair in your AWS CloudHSM cluster. ML-DSA is a post-quantum digital signature algorithm. Generate an ML-DSA key pair when you need to sign or verify data using a quantum-resistant algorithm.

###### Note

Starting September 1, 2026, ML-DSA is available in FIPS mode for hsm2m.medium clusters.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help key generate-asymmetric-pair ml-dsa``Generate an ML-DSA key pair

Usage: key generate-asymmetric-pair ml-dsa [OPTIONS] --public-label `<PUBLIC_LABEL>` --private-label `<PRIVATE_LABEL>` --mldsa-algorithm `<MLDSA_ALGORITHM>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --public-label `<PUBLIC_LABEL>`
 Label for the public key
 --private-label `<PRIVATE_LABEL>`
 Label for the private key
 --session
 Creates a session key pair that exists only in the current session. The key cannot be recovered after the session ends
 --mldsa-algorithm `<MLDSA_ALGORITHM>`
 ML-DSA algorithm [possible values: ML-DSA-44, ML-DSA-65, ML-DSA-87]
 --public-attributes [`<PUBLIC_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated ML-DSA public key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --private-attributes [`<PRIVATE_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated ML-DSA private key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --share-crypto-users [`<SHARE_CRYPTO_USERS>`...]
 Space separated list of Crypto User usernames to share the ML-DSA key with
 --manage-private-key-quorum-value `<MANAGE_PRIVATE_KEY_QUORUM_VALUE>`
 The quorum value for key management operations for the private key
 --use-private-key-quorum-value `<USE_PRIVATE_KEY_QUORUM_VALUE>`
 The quorum value for key usage operations for the private key
 -h, --help
 Print help`
```

## Examples

These examples show how to use `key generate-asymmetric-pair ml-dsa` to create an ML-DSA key pair.

###### Example: Create an ML-DSA-44 key pair

```
`aws-cloudhsm >` `key generate-asymmetric-pair ml-dsa \
 --mldsa-algorithm ML-DSA-44 \
 --public-label ml-dsa-public-key-example \
 --private-label ml-dsa-private-key-example``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x000000000000240b",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
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
 "key-type": "ml-dsa",
 "label": "ml-dsa-public-key-example",
 "id": "0x",
 "check-value": "0x988721",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "mldsa-algorithm": "ML-DSA-44",
 "sensitive": false,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1312
 }
 },
 "private_key": {
 "key-reference": "0x0000000000000f63",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
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
 "key-type": "ml-dsa",
 "label": "ml-dsa-private-key-example",
 "id": "0x",
 "check-value": "0x988721",
 "class": "private-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "mldsa-algorithm": "ML-DSA-44",
 "sensitive": true,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 2560
 }
 }
 }
}`
```

###### Example: Create an ML-DSA key pair with optional attributes

```
`aws-cloudhsm >` `key generate-asymmetric-pair ml-dsa \
 --mldsa-algorithm ML-DSA-65 \
 --public-label ml-dsa-public-key-example \
 --private-label ml-dsa-private-key-example \
 --public-attributes verify=true \
 --private-attributes sign=true``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x00000000002806eb",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
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
 "key-type": "ml-dsa",
 "label": "ml-dsa-public-key-example",
 "mldsa-algorithm": "ML-DSA-65",
 "verify": true,
 "key-length-bytes": 1952
 }
 },
 "private_key": {
 "key-reference": "0x00000000002806ec",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
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
 "key-type": "ml-dsa",
 "label": "ml-dsa-private-key-example",
 "mldsa-algorithm": "ML-DSA-65",
 "sign": true,
 "key-length-bytes": 4032
 }
 }
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<MLDSA_ALGORITHM>`**

Specifies the ML-DSA algorithm.

- ML-DSA-44
- ML-DSA-65
- ML-DSA-87

Required: Yes

**`<PUBLIC_KEY_ATTRIBUTES>`**

Specifies a space-separated list of key attributes to set for the generated ML-DSA public key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `verify=true`).

For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<PUBLIC_LABEL>`**

Specifies a user defined label for the public-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.

Required: Yes

**`<PRIVATE_KEY_ATTRIBUTES>`**

Specifies a space-separated list of key attributes to set for the generated ML-DSA private key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`).

For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<PRIVATE_LABEL>`**

Specifies a user defined label for the private-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.

Required: Yes

**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends.

Use this parameter when you need a key only briefly.

By default, the HSM generates persistent (token) keys. Passing in <SESSION> changes this, ensuring the HSM generates a session (ephemeral) key instead.

Required: No

**`<SHARE_CRYPTO_USERS>`**

Specifies a space-separated list of Crypto User usernames to share the ML-DSA private key with.

Required: No

**`<MANAGE_PRIVATE_KEY_QUORUM_VALUE>`**

The quorum value for the private key's key management operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared and the key owner. The maximum value is 8.

Required: No

**`<USE_PRIVATE_KEY_QUORUM_VALUE>`**

The quorum value for the private key's key usage operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared and the key owner. The maximum value is 8.

Required: No

## Related topics

- [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
- [Generate a signature with the ML-DSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-mldsa.md "cloudhsm_cli-crypto-sign-mldsa.md")
- [Verify a signature signed with the ML-DSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-mldsa.md "cloudhsm_cli-crypto-verify-mldsa.md")
