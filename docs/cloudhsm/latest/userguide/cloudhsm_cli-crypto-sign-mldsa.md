

# Generate a signature with the ML-DSA mechanism in CloudHSM CLI
<a name="cloudhsm_cli-crypto-sign-mldsa"></a>

Use the **crypto sign ml-dsa** command in CloudHSM CLI to generate a signature using an ML-DSA private key and the ML-DSA signing mechanism.

To use the **crypto sign ml-dsa** command, you must first have an ML-DSA private key in your AWS CloudHSM cluster. You can generate an ML-DSA private key using the [Generate an asymmetric ML-DSA key pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md) command with the `sign` attribute set to `true`.

**Note**  
Starting September 1, 2026, ML-DSA is available in FIPS mode for hsm2m.medium clusters.

**Note**  
You can verify signatures in AWS CloudHSM using [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md) subcommands.

You can generate a signature using two data types: raw data or computed external mu data.

## Steps to generate external mu
<a name="cloudhsm_cli-crypto-sign-mldsa-external-mu"></a>

To use the `external-mu` data type, you must first generate a 64-byte mu digest from your message using the ML-DSA public key:

1. **Generate the public key PEM file using the CloudHSM CLI:**

   ```
   aws-cloudhsm > key generate-file --encoding pem --path /tmp/public_key.pem --filter attr.label="mldsa-public-key-example"
   ```

   For more information, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md).

1. **Construct the message prefix:**

   The prefix contains a domain separator, the length of any context, and the context. The default for the domain separator and context length is zero.

1. **Prepend the message prefix to the message.**

1. **Use SHAKE256 to hash the public key and prepend it to the result of step 3.**

1. **Hash the result to produce a 64-byte external mu:**

### OpenSSL example
<a name="cloudhsm_cli-crypto-sign-mldsa-external-mu-openssl"></a>

The following example uses OpenSSL 3.5 to construct the external mu:

```
{
    openssl asn1parse -inform PEM -in public_key.pem -strparse 17 -noout -out - 2>/dev/null |
    openssl dgst -provider default -shake256 -xoflen 64 -binary;
    
    printf '\x00\x00';
    
    echo -n "your message"
} | openssl dgst -provider default -shake256 -xoflen 64 -binary | base64
```

Use the resulting base64-encoded 64-byte digest as the `--data` parameter with `--data-type external-mu`.

## User type
<a name="cloudhsm_cli-crypto-sign-mldsa-userType"></a>

The following types of users can run this command.
+ Crypto users (CUs)

## Requirements
<a name="cloudhsm_cli-crypto-sign-mldsa-requirements"></a>
+ To run this command, you must be logged in as a CU.

## Syntax
<a name="cloudhsm_cli-crypto-sign-mldsa-syntax"></a>

```
aws-cloudhsm > help crypto sign ml-dsa
Signs data with a ML-DSA private key

Usage: crypto sign ml-dsa [OPTIONS] --key-filter {{<KEY_FILTER>}} --data-type {{<DATA_TYPE>}} --hash-function {{<HASH_FUNCTION>}}

Options:
      --key-filter {{<KEY_FILTER>}}
          The key reference or a list of key attributes to filter for a key to sign with

      --hash-function {{<HASH_FUNCTION>}}
          The hash function to use with ML-DSA. [possible values: shake256]

      --data {{<DATA>}}
          Data to be signed

      --data-path {{<DATA_PATH>}}
          Path to file containing data to be signed

      --data-type {{<DATA_TYPE>}}
          Specifies if the data is raw or has been processed using external mu. [possible values: raw, external-mu]

      --approval {{<APPROVAL>}}
          File path of signed quorum token file to approve operation. Necessary for keys with quorum enabled

  -h, --help
          Print help
```

## Examples
<a name="crypto-sign-mldsa-examples"></a>

**Example: Sign raw data with ML-DSA private key**

Use this command to sign raw data with an ML-DSA private key.

```
aws-cloudhsm > crypto sign ml-dsa \
    --key-filter attr.label=ml-dsa-private-key-example \
    --data-type raw \
    --hash-function shake256 \
    --data YWJjMTIz
{
  "error_code": 0,
  "data": {
    "key-reference": "0x0000000000000f63",
    "signature": "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"
  }
}
```

**Example: Sign external mu data with ML-DSA private key**

Use this command to sign external mu data with an ML-DSA private key.

```
aws-cloudhsm > crypto sign ml-dsa \
    --key-filter attr.label="MLDSA_private_key" \
    --data-type external-mu \
    --hash-function shake256 \
    --data DgFbkWgb9fbejQUSbJ09/Nmp7phb714RTkWdNAwQqd9u7M7XCWbI8EoaIeGcZCUwIzaG6kDavZDYxCcaEicbTw==
{
  "error_code": 0,
  "data": {
    "key-reference": "0x0000000000000be2",
    "signature": "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"
  }
}
```

**Example: Sign data from a file path**

Use this command to sign data from a file with an ML-DSA private key.

```
aws-cloudhsm > crypto sign ml-dsa \
    --key-filter attr.label=ml-dsa-private-key-example \
    --data-type raw \
    --hash-function shake256 \
    --data-path /tmp/data.bin
{
  "error_code": 0,
  "data": {
    "key-reference": "0x0000000000000f63",
    "signature": "..."
  }
}
```

## Arguments
<a name="cloudhsm_cli-crypto-sign-mldsa-arguments"></a>

**{{<CLUSTER\_ID>}}**  
The ID of the cluster to run this operation on.  
Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md)

**{{<DATA>}}**  
Base64 encoded data to be signed.  
Required: Yes (unless provided through data path)

**{{<DATA\_PATH>}}**  
Specifies the location of the data to be signed.  
Required: Yes (unless provided through data)

**{{<HASH\_FUNCTION>}}**  
Specifies the hash function to use with ML-DSA.  
Valid values:  
+ shake256
Required: Yes

**{{<KEY\_FILTER>}}**  
Key reference (for example, `key-reference=0xabc`) or space-separated list of key attributes in the form of attr.KEY\_ATTRIBUTE\_NAME=KEY\_ATTRIBUTE\_VALUE to select a matching key.  
For a listing of supported CloudHSM CLI key attributes, see Key attributes for CloudHSM CLI.  
Required: Yes

**{{<APPROVAL>}}**  
Specifies the file path to a signed quorum token file to approve an operation. Only required if the key usage service quorum value of the private key is greater than 1.  
Required: No

**{{<DATA\_TYPE>}}**  
Specifies the data type of the provided data. Use `raw` for unhashed data; use `external-mu` for computed external mu data.  
Valid values:  
+ raw
+ external-mu
Required: Yes

## Related topics
<a name="cloudhsm_cli-crypto-sign-mldsa-seealso"></a>
+ [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md)
+ [Verify a signature signed with the ML-DSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-mldsa.md)
+ [Generate an asymmetric ML-DSA key pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md)