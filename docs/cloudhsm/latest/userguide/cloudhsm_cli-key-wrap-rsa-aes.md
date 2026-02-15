# Wrap a key with RSA-AES using CloudHSM CLI

Use the **key wrap rsa-aes** command in CloudHSM CLI to wrap a payload key
using an RSA public key on the hardware security module (HSM) and the RSA-AES wrapping
mechanism. The payload key’s `extractable` attribute must be set to
`true`.

Only the owner of a key, that is the crypto user (CU) who created the key, can wrap the key. Users who share the key can use the key in cryptographic operations.

To use the **key wrap rsa-aes** command, you must first have an RSA key in your AWS CloudHSM cluster. You can generate an RSA key pair using the
[The generate-asymmetric-pair
category in CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair.md "cloudhsm_cli-key-generate-asymmetric-pair.md") command and the `wrap` attribute set to `true`.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help key wrap rsa-aes``Usage: key wrap rsa-aes [OPTIONS] --payload-filter [`<PAYLOAD_FILTER>`...] --wrapping-filter [`<WRAPPING_FILTER>`...] --hash-function `<HASH_FUNCTION>` --mgf `<MGF>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --payload-filter [`<PAYLOAD_FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a payload key
 --wrapping-filter [`<WRAPPING_FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a wrapping key
 --path `<PATH>`
 Path to the binary file where the wrapped key data will be saved
 --wrapping-approval `<WRAPPING_APPROVALR>`
 File path of signed quorum token file to approve operation for wrapping key
 --payload-approval `<PAYLOAD_APPROVALR>`
 File path of signed quorum token file to approve operation for payload key
 --hash-function `<HASH_FUNCTION>`
 Hash algorithm [possible values: sha1, sha224, sha256, sha384, sha512]
 --mgf `<MGF>`
 Mask Generation Function algorithm [possible values: mgf1-sha1, mgf1-sha224, mgf1-sha256, mgf1-sha384, mgf1-sha512]
 -h, --help
 Print help`
```

## Example

This example shows how to use the **key wrap rsa-ae** command using an RSA public key with the `wrap` attribute value set to `true`.

###### Example

```
`aws-cloudhsm >` `key wrap rsa-aes --payload-filter attr.label=payload-key --wrapping-filter attr.label=rsa-public-key-example --hash-function sha256 --mgf mgf1-sha256``{
 "error_code": 0,
 "data": {
 "payload-key-reference": "0x00000000001c08f1",
 "wrapping-key-reference": "0x00000000007008da",
 "wrapped-key-data": "HrSE1DEyLjIeyGdPa9R+ebiqB5TIJGyamPker31ZebPwRA+NcerbAJO8DJ1lXPygZcI21vIFSZJuWMEiWpe1R9D/5WSYgxLVKex30xCFqebtEzxbKuv4DOmU4meSofqREYvtb3EoIKwjyxCMRQFgoyUCuP4y0f0eSv0k6rSJh4NuCsHptXZbtgNeRcR4botN7LlzkEIUcq4fVHaatCwd0J1QGKHKyRhkol+RL5WGXKe4nAboAkC5GO7veI5yHL1SaKlssSJtTL/CFpbSLsAFuYbv/NUCWwMY5mwyVTCSlw+HlgKK+5TH1MzBaSi8fpfyepLT8sHy2Q/VRl6ifb49p6m0KQFbRVvz/OWUd6l4d97BdgtaEz6ueg=="
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<PAYLOAD_FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a payload key.

Required: Yes

**`<PATH>`**

Path to the binary file where the wrapped key data will be saved.

Required: No

**`<WRAPPING_FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a wrapping key.

Required: Yes

**`<MGF>`**

Specifies the mask generation function.

###### Note

The mask generation function hash function must match the signing mechanism hash function.

Valid values

- mgf1-sha1
- mgf1-sha224
- mgf1-sha256
- mgf1-sha384
- mgf1-sha512

Required: Yes

**`<WRAPPING_APPROVALR>`**

Specifies the file path to a signed quorum token file to approve operation for wrapping key. Only required if wrapping key's key management service quorum value is greater than 1.

**`<PAYLOAD_APPROVALR>`**

Specifies the file path to a signed quorum token file to approve operation for payload key. Only required if payload key's key management service quorum value is greater than 1.

## Related topics

- [The key wrap command in CloudHSM CLI](cloudhsm_cli-key-wrap.md "cloudhsm_cli-key-wrap.md")
- [The key unwrap command in CloudHSM CLI](cloudhsm_cli-key-unwrap.md "cloudhsm_cli-key-unwrap.md")
