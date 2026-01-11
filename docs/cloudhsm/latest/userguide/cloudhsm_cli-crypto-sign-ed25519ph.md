# Generate a signature with the HashEdDSA mechanism in

CloudHSM CLI

###### Important

HashEdDSA signing operations are only supported on hsm2m.medium instances in non-FIPS mode.

Use the **crypto sign ed25519ph** command in CloudHSM CLI to generate a signature
using an Ed25519 private key and the HashEdDSA signing mechanism. For additional information on HashEdDSA,
see [NIST SP 186-5, Section 7.8](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf").

To use the **crypto sign ed25519ph** command, you must first have an Ed25519 private key in your AWS CloudHSM cluster.
You can generate an Ed25519 private key using the [Generate an asymmetric EC key
pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-ec.md "cloudhsm_cli-key-generate-asymmetric-pair-ec.md") command with the `curve` parameter set to `ed25519` and the `sign` attribute set to `true`.

###### Note

Signatures can be verified in AWS CloudHSM with [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md") subcommands.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.
- HashEdDSA signing operations are only supported on hsm2m.medium instances in non-FIPS mode.

## Syntax

```
`aws-cloudhsm >` `help crypto sign ed25519ph``Sign with the Ed25519ph mechanism

Usage: crypto sign ed25519ph [OPTIONS] --key-filter [`<KEY_FILTER>`...] --data-type `<DATA_TYPE>` --hash-function `<HASH_FUNCTION>` <--data-path `<DATA_PATH>`|--data `<DATA>`>

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --key-filter [`<KEY_FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key
 --data-path `<DATA_PATH>`
 The path to the file containing the data to be signed
 --data `<DATA>`
 Base64 Encoded data to be signed
 --approval `<APPROVAL>`
 Filepath of signed quorum token file to approve operation
 --data-type `<DATA_TYPE>`
 The type of data passed in, either raw or digest [possible values: raw, digest]
 --hash-function `<HASH_FUNCTION>`
 Hash function [possible values: sha512]
 -h, --help
 Print help`
```

## Example

These examples show how to use **crypto sign ed25519ph** to generate a signature using the Ed25519ph signing mechanism and `sha512` hash function. This command uses a private key in the HSM.

###### Example: Generate a signature for base 64 encoded data

```
`aws-cloudhsm >` `crypto sign ed25519ph \
 --key-filter attr.label=ed25519-private \
 --data-type raw \
 --hash-function sha512 \
 --data YWJj``{
 "error_code": 0,
 "data": {
 "key-reference": "0x0000000000401cdf",
 "signature": "mKcCIvC4Ehqp0w+BPWg/gJ5GK0acf/h2OUmbuU5trkEx+FBCRjwqNVogA9BirfWqoQuMYeY2Biqq0RwqJgg0Bg=="
 }
}`
```

###### Example: Generate a signature for a data file

```
`aws-cloudhsm >` `crypto sign ed25519ph \
 --key-filter attr.label=ed25519-private \
 --data-type raw \
 --hash-function sha512 \
 --data-path data.txt``{
 "error_code": 0,
 "data": {
 "key-reference": "0x0000000000401cdf",
 "signature": "mKcCIvC4Ehqp0w+BPWg/gJ5GK0acf/h2OUmbuU5trkEx+FBCRjwqNVogA9BirfWqoQuMYeY2Biqq0RwqJgg0Bg=="
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<DATA>`**

Base64 encoded data to be signed.

Required: Yes (unless provided through data path)

**`<DATA_PATH>`**

Specifies the location of the data to be signed.

Required: Yes (unless provided through data parameter)

**`<HASH_FUNCTION>`**

Specifies the hash function. Ed25519ph only supports SHA512.

Valid values:

- sha512

Required: Yes

**`<KEY_FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key.

For a list of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: Yes

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if the key usage service quorum value of the private key is greater than 1.

**`<DATA_TYPE>`**

Specifies whether the value of the data parameter should be hashed as part of the signing algorithm. Use `raw` for unhashed data; use `digest` for digests, which are already hashed.

Valid values:

- raw
- digest

Required: Yes

## Related topics

- [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
