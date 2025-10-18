# Wrap a key with AES-PKCS5-PAD using
 CloudHSM CLI

Use the **key wrap aes-pkcs5-pad** command in CloudHSM CLI to wrap a payload
 key using an AES key on the hardware security module (HSM) and the `AES-PKCS5-PAD`
 wrapping mechanism. The payload key's `extractable` attribute must be set to
 `true`.

Only the owner of a key, that is the crypto user (CU) who created the key, can wrap the key. Users who share the key can use the key in cryptographic operations.

To use the **key wrap aes-pkcs5-pad** command, you must first have an AES key in your AWS CloudHSM cluster. You can generate an AES key for wrapping using the 
 [Generate a symmetric AES key with
 CloudHSM CLI](cloudhsm_cli-key-generate-symmetric-aes.md "cloudhsm_cli-key-generate-symmetric-aes.md") command and the `wrap` attribute set to `true`.


## User type


The following types of users can run this command.



* Crypto users (CUs)

## Requirements



* To run this command, you must be logged in as a CU.

## Syntax



```
`aws-cloudhsm >` `help key wrap aes-pkcs5-pad``Usage: key wrap aes-pkcs5-pad [OPTIONS] --payload-filter [`<PAYLOAD_FILTER>`...] --wrapping-filter [`<WRAPPING_FILTER>`...]

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
 -h, --help
 Print help`
```

## Example


This example shows how to use the **key wrap aes-pkcs5-pad** command using an AES key with the `wrap` attribute value set to `true`.



```
`aws-cloudhsm >` `key wrap aes-pkcs5-pad --payload-filter attr.label=payload-key --wrapping-filter attr.label=aes-example``{
 "error_code": 0,
 "data": {
 "payload_key_reference": "0x00000000001c08f1",
 "wrapping_key_reference": "0x00000000001c08ea",
 "wrapped_key_data": "MbuYNresfOKyGNnxKWen88nSfX+uUE/0qmGofSisicY="
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



**`<WRAPPING_APPROVALR>`**

Specifies the file path to a signed quorum token file to approve operation for wrapping key. Only required if wrapping key's key management service quorum value is greater than 1.



**`<PAYLOAD_APPROVALR>`**

Specifies the file path to a signed quorum token file to approve operation for payload key. Only required if payload key's key management service quorum value is greater than 1.




## Related topics



* [The key wrap command in CloudHSM CLI](cloudhsm_cli-key-wrap.md "cloudhsm_cli-key-wrap.md")
* [The key unwrap command in CloudHSM CLI](cloudhsm_cli-key-unwrap.md "cloudhsm_cli-key-unwrap.md")
