# Verify a signature signed with the HashEdDSA

mechanism in CloudHSM CLI

###### Important

HashEdDSA signature verification operations are only supported on hsm2m.medium instances in non-FIPS mode.

Use the **crypto verify ed25519ph** command in CloudHSM CLI to complete the
following operations:

- Verify signatures of data or files using a given Ed25519 public key.
- Confirm the signature was generated using the HashEdDSA signing mechanism. For additional information on HashEdDSA,
  see [NIST SP 186-5, Section 7.8](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf").
  To use the **crypto verify ed25519ph** command, you must first have an Ed25519 public key in your AWS CloudHSM cluster.
  You can generate an Ed25519 key pair using the [Generate an asymmetric EC key
  pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-ec.md "cloudhsm_cli-key-generate-asymmetric-pair-ec.md") command with the `curve` parameter set to `ed25519` and the `verify` attribute set to `true`, or import an Ed25519 public key using the [Import a PEM format key with CloudHSM CLI](cloudhsm_cli-key-import-pem.md "cloudhsm_cli-key-import-pem.md") command with the `verify` attribute set to `true`.

###### Note

You can generate a signature in CloudHSM CLI with [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md") subcommands.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.
- HashEdDSA signature verification operations are only supported on hsm2m.medium instances in non-FIPS mode.

## Syntax

```
`aws-cloudhsm >` `help crypto verify ed25519ph``Verify with the Ed25519ph mechanism

Usage: crypto verify ed25519ph [OPTIONS] --key-filter [`<KEY_FILTER>`...] --data-type `<DATA_TYPE>` --hash-function `<HASH_FUNCTION>` <--data-path `<DATA_PATH>`|--data `<DATA>`> <--signature-path `<SIGNATURE_PATH>`|--signature `<SIGNATURE>`>

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --key-filter [`<KEY_FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key
 --data-path `<DATA_PATH>`
 The path to the file containing the data to be verified
 --data `<DATA>`
 Base64 encoded data to be verified
 --signature-path `<SIGNATURE_PATH>`
 The path to where the signature is located
 --signature `<SIGNATURE>`
 Base64 encoded signature to be verified
 --data-type `<DATA_TYPE>`
 The type of data passed in, either raw or digest [possible values: raw, digest]
 --hash-function `<HASH_FUNCTION>`
 Hash function [possible values: sha512]
 -h, --help
 Print help`
```

## Example

These examples show how to use **crypto verify ed25519ph** to verify a signature that was generated using the Ed25519ph signing mechanism and `sha512` hash function. This command uses an Ed25519 public key in the HSM.

###### Example: Verify a Base64 encoded signature with Base64 encoded data

```
`aws-cloudhsm >` `crypto verify ed25519ph \
 --hash-function sha512 \
 --key-filter attr.label=ed25519-public \
 --data-type raw \
 --data YWJj \
 --signature mKcCIvC4Ehqp0w+BPWg/gJ5GK0acf/h2OUmbuU5trkEx+FBCRjwqNVogA9BirfWqoQuMYeY2Biqq0RwqJgg0Bg==``{
 "error_code": 0,
 "data": {
 "message": "Signature verified successfully"
 }
}`
```

###### Example: Verify a signature file with a data file

```
`aws-cloudhsm >` `crypto verify ed25519ph \
 --hash-function sha512 \
 --key-filter attr.label=ed25519-public \
 --data-type raw \
 --data-path data.txt \
 --signature-path signature-file``{
 "error_code": 0,
 "data": {
 "message": "Signature verified successfully"
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<DATA>`**

Base64 encoded data to be verified.

Required: Yes (unless provided through data path)

**`<DATA_PATH>`**

Specifies the location of the data to be verified.

Required: Yes (unless provided through data parameter)

**`<HASH_FUNCTION>`**

Specifies the hash function. Ed25519ph only supports SHA512.

Valid values:

- sha512

Required: Yes

**`<KEY_FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key.

For a listing of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: Yes

**`<SIGNATURE>`**

Base64 encoded signature.

Required: Yes (unless provided through signature path)

**`<SIGNATURE_PATH>`**

Specifies the location of the signature.

Required: Yes (unless provided through signature parameter)

**`<DATA_TYPE>`**

Specifies whether the value of the data parameter should be hashed as part of the verification algorithm. Use `raw` for unhashed data; use `digest` for digests, which are already hashed.

Valid values:

- raw
- digest

Required: Yes

## Related topics

- [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
- [Generate a signature with the HashEdDSA mechanism in
  CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519ph.md "cloudhsm_cli-crypto-sign-ed25519ph.md")
