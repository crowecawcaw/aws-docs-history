# Verify a signature signed with the RSA-PKCS

mechanism in CloudHSM CLI

Use the **crypto verify rsa-pkcs** command in CloudHSM CLI complete the
following operations:

- Confirm a file has been signed in the HSM by a given public key.
- Verify the signature was generated using the `RSA-PKCS` signing mechanism.
- Compare a signed file against a source file and determines whether the two are cryptographically related based on a given rsa public key and signing mechanism.
  To use the **crypto verify rsa-pkcs** command, you must first have an RSA public key in your AWS CloudHSM cluster.

###### Note

You can generate a signature using the CloudHSM CLI with the [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md") subcommands.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help crypto verify rsa-pkcs``Verify with the RSA-PKCS mechanism

Usage: crypto verify rsa-pkcs --key-filter [`<KEY_FILTER>`...] --hash-function `<HASH_FUNCTION>` <--data-path `<DATA_PATH>`|--data `<DATA>`> <--signature-path `<SIGNATURE_PATH>`|--signature `<SIGNATURE>`>

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --key-filter [`<KEY_FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key
 --hash-function `<HASH_FUNCTION>`
 [possible values: sha1, sha224, sha256, sha384, sha512]
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
 -h, --help
 Print help`
```

## Example

These examples show how to use **crypto verify rsa-pkcs** to verify a signature that was generated using the RSA-PKCS signing mechanism and `SHA256` hash function.
This command uses a public key in the HSM.

###### Example: Verify a Base64 encoded signature with Base64 encoded data

```
`aws-cloudhsm >` `crypto verify rsa-pkcs --hash-function sha256 --key-filter attr.label=rsa-public --data YWJjMTIz --signature XJ7mRyHnDRYrDWTQuuNb+5mhoXx7VTsPMjgOQW4iMN7E42eNHj2Q0oovMmBdHUEH0F4HYG8FBJOBhvGuM8J/z6y41GbowVpUT6WzjnIQs79K9i7i6oR1TYjLnIS3r/zkimuXcS8/ZxyDzru+GO9BUT9FFU/of9cvu4Oyn6a5+IXuCbKNQs19uASuFARUTZ0a0Ny1CB1MulxUpqGTmI91J6evlP7k/2khwDmJ5E8FEar5/Cvbn9t21p3Uj561ngTXrYbIZ2KHpef9jQh/cEIvFLG61sexJjQi8EdTxeDA+I3ITO0qrvvESvA9+Sj7kdG2ceIicFS8/8LwyxiIC31UHQ==``{
 "error_code": 0,
 "data": {
 "message": "Signature verified successfully"
 }
}`
```

###### Example: Verify a signature file with a data file

```
`aws-cloudhsm >` `crypto verify rsa-pkcs --hash-function sha256 --key-filter attr.label=rsa-public --data-path data.txt --signature-path signature-file``{
 "error_code": 0,
 "data": {
 "message": "Signature verified successfully"
 }
}`
```

###### Example: Prove false signing relationship

This command verifies whether the invalid data was signed by a public key with the label `rsa-public` using the RSAPKCS signing mechanism to produce the signature located in `/home/signature`.
Because the given arguments do not make up a true signing relationship, the command returns an error message.

```
`aws-cloudhsm >` `crypto verify rsa-pkcs --hash-function sha256 --key-filter attr.label=rsa-public --data aW52YWxpZA== --signature XJ7mRyHnDRYrDWTQuuNb+5mhoXx7VTsPMjgOQW4iMN7E42eNHj2Q0oovMmBdHUEH0F4HYG8FBJOBhvGuM8J/z6y41GbowVpUT6WzjnIQs79K9i7i6oR1TYjLnIS3r/zkimuXcS8/ZxyDzru+GO9BUT9FFU/of9cvu4Oyn6a5+IXuCbKNQs19uASuFARUTZ0a0Ny1CB1MulxUpqGTmI91J6evlP7k/2khwDmJ5E8FEar5/Cvbn9t21p3Uj561ngTXrYbIZ2KHpef9jQh/cEIvFLG61sexJjQi8EdTxeDA+I3ITO0qrvvESvA9+Sj7kdG2ceIicFS8/8LwyxiIC31UHQ==``{
 "error_code": 1,
 "data": "Signature verification failed"
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

Required: Yes (unless provided through data path)

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

**`<SIGNATURE>`**

Base64 encoded signature.

Required: Yes (unless provided through signature path)

**`<SIGNATURE_PATH>`**

Specifies the location of the signature.

Required: Yes (unless provided through signature path)

**`<DATA_TYPE>`**

Specifies whether the value of the data parameter should be hashed as part of the signing algorithm. Use `raw` for unhashed data; use `digest` for digests, which are already hashed.

For RSA-PKCS, the data must be passed in DER encoded format as specified in [RFC 8017, Section 9.2](https://www.rfc-editor.org/rfc/rfc8017#section-9.2 "https://www.rfc-editor.org/rfc/rfc8017#section-9.2")

Valid values:

- raw
- digest

## Related topics

- [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
