# Export an asymmetric key with

CloudHSM CLI

Use the **key generate-file** command in CloudHSM CLI to export an asymmetric
key from the hardware security module (HSM). If the target is a private key, then the reference
to the private key will be exported in fake PEM format. If the target is a public key, then the
public key bytes will be exported in PEM format.

The fake PEM file, which does not contain the actual private key material but instead references the private key in the HSM, can be used to establish SSL/TLS offloading from your web server to AWS CloudHSM.
For more information, see [SSL/TLS offloading](ssl-offload.md "ssl-offload.md").

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help key generate-file``Generate a key file from a key in the HSM cluster. This command does not export any private key data from the HSM

Usage: key generate-file --encoding `<ENCODING>` --path `<PATH>` --filter [`<FILTER>`...]

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --encoding `<ENCODING>`
 Encoding format for the key file

 Possible values:
 - reference-pem: PEM formatted key reference (supports private keys)
 - pem: PEM format (supports public keys)

 --path `<PATH>`
 Filepath where the key file will be written

 --filter [`<FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key for file generation

 -h, --help
 Print help (see a summary with '-h')`
```

## Example

This example shows how to use **key generate-file** to generate a key file in your AWS CloudHSM cluster.

###### Example

```
`aws-cloudhsm >` `key generate-file --encoding reference-pem --path /tmp/ec-private-key.pem --filter attr.label="ec-test-private-key"``{
 "error_code": 0,
 "data": {
 "message": "Successfully generated key file"
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key for deletion.

For a listing of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")

Required: No

**`<ENCODING>`**

Specifies the encoding format for the key file

Required: Yes

**`<PATH>`**

Specifies the file path where the key file will be written

Required: Yes

## Generating KSP key references (Windows)

###### Note

This feature is only in SDK version 5.16.0 and later.

### Prerequisites

- You can generate KSP key references only on Windows platforms.
- You must sign in as a crypto user (CU).

### File location

By default, AWS CloudHSM stores generated files in:
`C:\Users\Default\AppData\Roaming\Microsoft\Crypto\CaviumKSP\GlobalPartition`

To specify a different location, use the `--path` parameter.

### Syntax

```
`aws-cloudhsm >` `help key generate-file --encoding ksp-key-reference` `Generate a key file from a key in the HSM cluster. This command does not export any private key data from the HSM

Usage: key generate-file --encoding `<ENCODING>` --path `<PATH>` --filter [`<FILTER>`...]

Options:
 --encoding `<ENCODING>`
 Encoding format for the key file

 Possible values:
 - reference-pem: PEM formatted key reference (supports private keys)
 - pem: PEM format (supports public keys)
 - ksp-key-reference: KSP key reference format

 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided with multiple clusters configured, will error

 --path `<PATH>`
 Directory path where the key file will be written

 --filter [<FILTER>...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key for file generation

 --all
 Generate ksp key reference for all available key pairs in HSM

 -h, --help
 Print help (see a summary with '-h')`
```

### Example – Generate a KSP key reference

using an attribute filter of a private key

The following example generates a KSP key reference for a private key with a specific label.

###### Example

```
`aws-cloudhsm >` `key generate-file --encoding ksp-key-reference --path --filter attr.label="ec-test-private-key"``{
 "error_code": 0,
 "data": {
 "message": "Successfully generated key file"
 }
}`
```

### Example – Generate KSP key references for

all key pairs

The following example generates KSP key references for all key pairs in your cluster.

###### Example

```
`aws-cloudhsm >` `key generate-file --encoding ksp-key-reference --all``{
 "error_code": 0,
 "data": {
 "message": "Successfully generated key file"
 }
}`
```

## Related topics

- [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
- [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
- [The generate-asymmetric-pair
  category in CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair.md "cloudhsm_cli-key-generate-asymmetric-pair.md")
- [The generate-symmetric category in
  CloudHSM CLI](cloudhsm_cli-key-generate-symmetric.md "cloudhsm_cli-key-generate-symmetric.md")
