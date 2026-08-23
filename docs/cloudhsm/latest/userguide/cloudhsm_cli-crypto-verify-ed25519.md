# Verify a signature signed with the PureEdDSA mechanism in CloudHSM CLI

###### Important

PureEdDSA signature verification operations are only supported on hsm2m.medium instances in non-FIPS mode.

Use the **crypto verify ed25519** command in CloudHSM CLI to complete the
following operations:

- Verify signatures of data or files using a given Ed25519 public key.
- Confirm the signature was generated using the PureEdDSA signing mechanism (Ed25519).

###### Note

The maximum message size for PureEdDSA is 16,000 bytes. For larger messages, use
[Verify a signature signed with the HashEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-ed25519ph.md "cloudhsm_cli-crypto-verify-ed25519ph.md").

To use the **crypto verify ed25519** command, you must first have an Ed25519 public key in your AWS CloudHSM cluster.
You can generate an Ed25519 key pair using the [Generate an asymmetric EC key pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-ec.md "cloudhsm_cli-key-generate-asymmetric-pair-ec.md") command with the `curve` parameter set to `ed25519` and the `verify` attribute set to `true`, or import an Ed25519 public key using the [Import a PEM format key with CloudHSM CLI](cloudhsm_cli-key-import-pem.md "cloudhsm_cli-key-import-pem.md") command with the `verify` attribute set to `true`.

###### Note

You can generate a signature in CloudHSM CLI with [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md") subcommands.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.
- PureEdDSA signature verification operations are only supported on hsm2m.medium instances in non-FIPS mode.
- The message data must be no larger than 16,000 bytes.

## Syntax

```
`aws-cloudhsm >` `help crypto verify ed25519``Verify with the Ed25519 mechanism

Usage: crypto verify ed25519 [OPTIONS] --key-filter [`<KEY_FILTER>`...] <--data-path `<DATA_PATH>`|--data `<DATA>`> <--signature-path `<SIGNATURE_PATH>`|--signature `<SIGNATURE>`>

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
 -h, --help
 Print help`
```

## Example

These examples show how to use **crypto verify ed25519** to verify a signature that was generated using the PureEdDSA signing mechanism. This command uses an Ed25519 public key in the HSM.

###### Example: Verify a Base64 encoded signature with Base64 encoded data

```
`aws-cloudhsm >` `crypto verify ed25519 \
 --key-filter attr.label=ed25519-public \
 --data YWJj \
 --signature NjWz797ntYSLFwg7nKYYdn+On3cCMj4zKz059wadVVlBHxyxe4JrSZxgekwb9AYR5xFxuVE9dTnDSo+gCaW/CQ==``{
 "error_code": 0,
 "data": {
 "message": "Signature verified successfully"
 }
}`
```

###### Example: Verify a signature file with a data file

```
`aws-cloudhsm >` `crypto verify ed25519 \
 --key-filter attr.label=ed25519-public \
 --data-path data.txt \
 --signature-path signature-file``{
 "error_code": 0,
 "data": {
 "message": "Signature verified successfully"
 }
}`
```

###### Example: Prove a false signing relationship

This example shows that verification fails when the data, signature, or key do not match.

```
`aws-cloudhsm >` `crypto verify ed25519 \
 --key-filter attr.label=ed25519-public \
 --data bWVzc2FnZQ== \
 --signature NjWz797ntYSLFwg7nKYYdn+On3cCMj4zKz059wadVVlBHxyxe4JrSZxgekwb9AYR5xFxuVE9dTnDSo+gCaW/CQ==``{
 "error_code": 1,
 "data": "Signature verification failed"
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<DATA>`**

Base64 encoded data to be verified. The decoded data must be no larger than 16,000 bytes.

Required: Yes (unless provided through data path)

**`<DATA_PATH>`**

Specifies the location of the data to be verified. The file contents must be no larger than 16,000 bytes.

Required: Yes (unless provided through data parameter)

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

## Related topics

- [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
- [Generate a signature with the PureEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519.md "cloudhsm_cli-crypto-sign-ed25519.md")
- [Verify a signature signed with the HashEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-ed25519ph.md "cloudhsm_cli-crypto-verify-ed25519ph.md")
