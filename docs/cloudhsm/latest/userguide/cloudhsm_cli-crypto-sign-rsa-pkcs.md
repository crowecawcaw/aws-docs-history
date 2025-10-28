# Generate a signature with the RSA-PKCS

mechanism in CloudHSM CLI

Use the **crypto sign rsa-pkcs** command in CloudHSM CLI to generate a
signature using an RSA private key and the RSA-PKCS signing mechanism.

To use the **crypto sign rsa-pkcs** command, you must first have a RSA private key in your AWS CloudHSM cluster.
You can generate an RSA private key using the [Generate an asymmetric RSA key
pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-rsa.md "cloudhsm_cli-key-generate-asymmetric-pair-rsa.md") command with the `sign` attribute set to `true`.

###### Note

Signatures can be verified in AWS CloudHSM with [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md") subcommands.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help crypto sign rsa-pkcs``Sign with the RSA-PKCS mechanism

Usage: crypto sign rsa-pkcs --key-filter [`<KEY_FILTER>>`...] --hash-function `<HASH_FUNCTION>` <--data-path `<DATA_PATH>`|--data `<DATA>`>

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --key-filter [`<KEY_FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key
 --hash-function `<HASH_FUNCTION>`
 [possible values: sha1, sha224, sha256, sha384, sha512]
 --data-path `<DATA_PATH>`
 The path to the file containing the data to be signed
 --data `<DATA>`
 Base64 Encoded data to be signed
 --approval `<APPROVAL>`
 Filepath of signed quorum token file to approve operation
 --data-type `<DATA_TYPE>`
 The type of data passed in, either raw or digest [possible values: raw, digest]
 -h, --help
 Print help`
```

## Example

These examples show how to use **crypto sign rsa-pkcs** to generate a signature using the RSA-PKCS signing mechanism and `SHA256` hash function. This command uses a private key in the HSM.

###### Example: Generate a signature for base 64 encoded data

```
`aws-cloudhsm >` `crypto sign rsa-pkcs --key-filter attr.label=rsa-private --hash-function sha256 --data YWJjMTIz``{
 "error_code": 0,
 "data": {
 "key-reference": "0x00000000007008db",
 "signature": "XJ7mRyHnDRYrDWTQuuNb+5mhoXx7VTsPMjgOQW4iMN7E42eNHj2Q0oovMmBdHUEH0F4HYG8FBJOBhvGuM8J/z6y41GbowVpUT6WzjnIQs79K9i7i6oR1TYjLnIS3r/zkimuXcS8/ZxyDzru+GO9BUT9FFU/of9cvu4Oyn6a5+IXuCbKNQs19uASuFARUTZ0a0Ny1CB1MulxUpqGTmI91J6evlP7k/2khwDmJ5E8FEar5/Cvbn9t21p3Uj561ngTXrYbIZ2KHpef9jQh/cEIvFLG61sexJjQi8EdTxeDA+I3ITO0qrvvESvA9+Sj7kdG2ceIicFS8/8LwyxiIC31UHQ=="
 }
}`
```

###### Example: Generate a signature for a data file

```
`aws-cloudhsm >` `crypto sign rsa-pkcs --key-filter attr.label=rsa-private --hash-function sha256 --data-path data.txt``{
 "error_code": 0,
 "data": {
 "key-reference": "0x00000000007008db",
 "signature": "XJ7mRyHnDRYrDWTQuuNb+5mhoXx7VTsPMjgOQW4iMN7E42eNHj2Q0oovMmBdHUEH0F4HYG8FBJOBhvGuM8J/z6y41GbowVpUT6WzjnIQs79K9i7i6oR1TYjLnIS3r/zkimuXcS8/ZxyDzru+GO9BUT9FFU/of9cvu4Oyn6a5+IXuCbKNQs19uASuFARUTZ0a0Ny1CB1MulxUpqGTmI91J6evlP7k/2khwDmJ5E8FEar5/Cvbn9t21p3Uj561ngTXrYbIZ2KHpef9jQh/cEIvFLG61sexJjQi8EdTxeDA+I3ITO0qrvvESvA9+Sj7kdG2ceIicFS8/8LwyxiIC31UHQ=="
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

Required: Yes (unless provided through data)

**`<HASH_FUNCTION>`**

Specifies the hash function.

Valid values:

- sha1
- sha224
- sha256
- sha384
- sha512

Required: Yes

**`<KEY_FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key.

For a listing of supported CloudHSM CLI key attributes, see Key attributes for CloudHSM CLI.

Required: Yes

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if the key usage service quorum value of the private key is greater than 1.

**`<DATA_TYPE>`**

Specifies whether the value of the data parameter should be hashed as part of the signing algorithm. Use `raw` for unhashed data; use `digest` for digests, which are already hashed.

For RSA-PKCS, the data must be passed in DER encoded format as specified in [RFC 8017, Section 9.2](https://www.rfc-editor.org/rfc/rfc8017#section-9.2 "https://www.rfc-editor.org/rfc/rfc8017#section-9.2")

Valid values:

- raw
- digest

## Related topics

- [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
