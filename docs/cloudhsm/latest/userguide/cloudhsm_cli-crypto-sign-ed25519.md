

# Generate a signature with the PureEdDSA mechanism in CloudHSM CLI
<a name="cloudhsm_cli-crypto-sign-ed25519"></a>

**Important**  
PureEdDSA signing operations are only supported on hsm2m.medium instances in non-FIPS mode.

Use the **crypto sign ed25519** command in CloudHSM CLI to generate a signature using an Ed25519 private key and the PureEdDSA signing mechanism. PureEdDSA (also called Ed25519) signs the raw message directly without prehashing, as defined in [RFC 8032, Section 5.1.6](https://www.rfc-editor.org/rfc/rfc8032#section-5.1.6) on the IETF website.

**Note**  
The maximum message size for PureEdDSA is 16,000 bytes. For larger messages, use [Generate a signature with the HashEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519ph.md).

To use the **crypto sign ed25519** command, you must first have an Ed25519 private key in your AWS CloudHSM cluster. You can generate an Ed25519 private key using the [Generate an asymmetric EC key pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-ec.md) command with the `curve` parameter set to `ed25519` and the `sign` attribute set to `true`.

**Note**  
Signatures can be verified in AWS CloudHSM with [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md) subcommands.

## User type
<a name="cloudhsm_cli-crypto-sign-ed25519-userType"></a>

The following types of users can run this command.
+ Crypto users (CUs)

## Requirements
<a name="cloudhsm_cli-crypto-sign-ed25519-requirements"></a>
+ To run this command, you must be logged in as a CU.
+ PureEdDSA signing operations are only supported on hsm2m.medium instances in non-FIPS mode.
+ The message data must be no larger than 16,000 bytes. For larger messages, use [Generate a signature with the HashEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519ph.md).

## Syntax
<a name="cloudhsm_cli-crypto-sign-ed25519-syntax"></a>

```
aws-cloudhsm > help crypto sign ed25519
Sign with the Ed25519 mechanism

Usage: crypto sign ed25519 [OPTIONS] --key-filter [{{<KEY_FILTER>}}...] <--data-path {{<DATA_PATH>}}|--data {{<DATA>}}>

Options:
      --cluster-id {{<CLUSTER_ID>}}
          Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
      --key-filter [{{<KEY_FILTER>}}...]
          Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key
      --data-path {{<DATA_PATH>}}
          The path to the file containing the data to be signed
      --data {{<DATA>}}
          Base64 Encoded data to be signed
      --approval {{<APPROVAL>}}
          Filepath of signed quorum token file to approve operation
  -h, --help
          Print help
```

## Example
<a name="cloudhsm_cli-crypto-sign-ed25519-examples"></a>

These examples show how to use **crypto sign ed25519** to generate a signature using the PureEdDSA signing mechanism. This command signs the raw message directly without prehashing. This command uses an Ed25519 private key in the HSM.

**Example: Generate a signature for base 64 encoded data**  

```
aws-cloudhsm > crypto sign ed25519 \
    --key-filter attr.label=ed25519-private \
    --data YWJj
{
  "error_code": 0,
  "data": {
    "key-reference": "0x00000000006c1507",
    "signature": "NjWz797ntYSLFwg7nKYYdn+On3cCMj4zKz059wadVVlBHxyxe4JrSZxgekwb9AYR5xFxuVE9dTnDSo+gCaW/CQ=="
  }
}
```

**Example: Generate a signature for a data file**  

```
aws-cloudhsm > crypto sign ed25519 \
    --key-filter attr.label=ed25519-private \
    --data-path data.txt
{
  "error_code": 0,
  "data": {
    "key-reference": "0x00000000006c1507",
    "signature": "NjWz797ntYSLFwg7nKYYdn+On3cCMj4zKz059wadVVlBHxyxe4JrSZxgekwb9AYR5xFxuVE9dTnDSo+gCaW/CQ=="
  }
}
```

## Arguments
<a name="cloudhsm_cli-crypto-sign-ed25519-arguments"></a>

**{{<CLUSTER\_ID>}}**  
The ID of the cluster to run this operation on.  
Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md)

**{{<DATA>}}**  
Base64 encoded data to be signed. The decoded data must be no larger than 16,000 bytes.  
Required: Yes (unless provided through data path)

**{{<DATA\_PATH>}}**  
Specifies the location of the data to be signed. The file contents must be no larger than 16,000 bytes.  
Required: Yes (unless provided through data parameter)

**{{<KEY\_FILTER>}}**  
Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key.  
For a list of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md).  
Required: Yes

**{{<APPROVAL>}}**  
Specifies the file path to a signed quorum token file to approve operation. Only required if the key usage service quorum value of the private key is greater than 1.  
Required: No

## Related topics
<a name="cloudhsm_cli-crypto-sign-ed25519-seealso"></a>
+ [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md)
+ [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md)
+ [Verify a signature signed with the PureEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-ed25519.md)
+ [Generate a signature with the HashEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519ph.md)