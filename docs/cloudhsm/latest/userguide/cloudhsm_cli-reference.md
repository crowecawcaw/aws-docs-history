

# Reference for CloudHSM CLI commands
<a name="cloudhsm_cli-reference"></a>

CloudHSM CLI helps admins manage users in their AWS CloudHSM cluster. CloudHSM CLI can be run in two modes: Interactive Mode and Single Command Mode. For a quick start, see [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md). 

To run most CloudHSM CLI commands, you must start the CloudHSM CLI and log in to the HSM. If you add or delete HSMs, update the configuration files for CloudHSM CLI. Otherwise, the changes that you make might not be effective for all HSMs in the cluster.

The following topics describe commands in CloudHSM CLI: 


| Command | Description | User Type | 
| --- | --- | --- | 
| [activate](cloudhsm_cli-cluster-activate.md) | Activates an CloudHSM cluster and provides confirmation the cluster is new. This must be done before any other operations can be performed. | Unactivated admin | 
| [hsm-info](cloudhsm_cli-cluster-hsm-info.md) | List the HSMs in your cluster. | All [1](#cli-ref-1), including unauthenticated users. Login is not required. | 
| [ecdsa](cloudhsm_cli-crypto-sign-ecdsa.md) | Generates a signature using an EC private key and the ECDSA signing mechanism.  | Crypto users (CU) | 
| [ed25519](cloudhsm_cli-crypto-sign-ed25519.md) | Generates a signature using an Ed25519 private key and the PureEdDSA signing mechanism.  | CU | 
| [ed25519ph](cloudhsm_cli-crypto-sign-ed25519ph.md) | Generates a signature using an Ed25519 private key and the HashEdDSA signing mechanism.  | CU | 
| [ml-dsa](cloudhsm_cli-crypto-sign-mldsa.md) | Generates a signature using an ML-DSA[2](#cli-ref-2) private key and the ML-DSA signing mechanism. | CU | 
| [rsa-pkcs](cloudhsm_cli-crypto-sign-rsa-pkcs.md) | Generates a signature using an RSA private key and the RSA-PKCS signing mechanism. | CU | 
| [rsa-pkcs-pss](cloudhsm_cli-crypto-sign-rsa-pkcs-pss.md) | Generates a signature using an RSA private key and the RSA-PKCS-PSS signing mechanism. | CU | 
| [ecdsa](cloudhsm_cli-crypto-verify-ecdsa.md) | Confirms a file has been signed in the HSM by a given public key. Verifies the signature was generated using the ECDSA signing mechanism. Compares a signed file against a source file and determine whether the two are cryptographically related based on a given ecdsa public key and signing mechanism.  | CU | 
| [ed25519](cloudhsm_cli-crypto-verify-ed25519.md) | Verifies PureEdDSA signatures using an Ed25519 public key. | CU | 
| [ed25519ph](cloudhsm_cli-crypto-verify-ed25519ph.md) | Verifies HashEdDSA signatures using an Ed25519 public key. | CU | 
| [ml-dsa](cloudhsm_cli-crypto-verify-mldsa.md) | Verifies a signature using an ML-DSA[2](#cli-ref-2) public key and the ML-DSA verification mechanism. | CU | 
| [rsa-pkcs](cloudhsm_cli-crypto-verify-rsa-pkcs.md) | Confirms a file has been signed in the HSM by a given public key. Verifies the signature was generated using the RSA-PKCS signing mechanism. Compares a signed file against a source file and determines whether the two are cryptographically related based on a given rsa public key and signing mechanism. | CU | 
| [rsa-pkcs-pss](cloudhsm_cli-crypto-verify-rsa-pkcs-pss.md) | Confirms a file has been signed in the HSM by a given public key. Verifies the signature was generated using the RSA-PKCS-PSS signing mechanism. Compares a signed file against a source file and determines whether the two are cryptographically related based on a given rsa public key and signing mechanism. | CU | 
| [key delete](cloudhsm_cli-key-delete.md) | Deletes a key from your AWS CloudHSM cluster. | CU | 
| [key generate-file](cloudhsm_cli-key-generate-file.md) | Generates a key file in your AWS CloudHSM cluster. | CU | 
| [key generate-asymmetric-pair rsa](cloudhsm_cli-key-generate-asymmetric-pair-rsa.md) | Generates an asymmetric RSA key pair in your AWS CloudHSM cluster. | CU | 
| [key generate-asymmetric-pair ec](cloudhsm_cli-key-generate-asymmetric-pair-ec.md) | Generates an asymmetric Elliptic-curve (EC) key pair in your AWS CloudHSM cluster. | CU | 
| [key generate-asymmetric-pair ml-dsa](cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md) | Generates an asymmetric ML-DSA key pair in your AWS CloudHSM cluster. | CU | 
| [key generate-symmetric aes](cloudhsm_cli-key-generate-symmetric-aes.md) | Generates a symmetric AES key in your AWS CloudHSM cluster. | CU | 
| [key generate-symmetric generic-secret](cloudhsm_cli-key-generate-symmetric-generic-secret.md) | Generates a symmetric Generic Secret key in your AWS CloudHSM cluster. | CU | 
| [key import pem](cloudhsm_cli-key-import-pem.md) | Imports a PEM format key into an HSM. You can use it to import public keys that were generated outside of the HSM. | CU | 
| [key list](cloudhsm_cli-key-list.md) | Finds all keys for the current user present in your AWS CloudHSM cluster. | CU | 
| [key replicate](cloudhsm_cli-key-replicate.md) | Replicate a key from a source cluster to a cloned destination cluster. | CU | 
| [key set-attribute](cloudhsm_cli-key-set-attribute.md) | Sets the attributes of keys in your AWS CloudHSM cluster. | CUs can run this command, admins can set the trusted attribute. | 
| [key share](cloudhsm_cli-key-share.md) | Shares a key with other CUs in your AWS CloudHSM cluster. | CU | 
| [key unshare](cloudhsm_cli-key-unshare.md) | Unshares a key with other CUs in your AWS CloudHSM cluster. | CU | 
| [aes-gcm](cloudhsm_cli-key-unwrap-aes-gcm.md) | Unwraps a payload key into the cluster using the AES wrapping key and the AES-GCM unwrapping mechanism. | CU | 
| [aes-no-pad](cloudhsm_cli-key-unwrap-aes-no-pad.md) | Unwraps a payload key into the cluster using the AES wrapping key and the AES-NO-PAD unwrapping mechanism. | CU | 
| [aes-pkcs5-pad](cloudhsm_cli-key-unwrap-aes-pkcs5-pad.md) | Unwraps a payload key using the AES wrapping key and the AES-PKCS5-PAD unwrapping mechanism. | CU | 
| [aes-zero-pad](cloudhsm_cli-key-unwrap-aes-zero-pad.md) | Unwraps a payload key into the cluster using the AES wrapping key and the AES-ZERO-PAD unwrapping mechanism. | CU | 
| [cloudhsm-aes-gcm](cloudhsm_cli-key-unwrap-cloudhsm-aes-gcm.md) | Unwraps a payload key into the cluster using the AES wrapping key and the CLOUDHSM-AES-GCM unwrapping mechanism. | CU | 
| [rsa-aes](cloudhsm_cli-key-unwrap-rsa-aes.md) | Unwraps a payload key using an RSA private key and the RSA-AES unwrapping mechanism. | CU | 
| [rsa-oaep](cloudhsm_cli-key-unwrap-rsa-oaep.md) | Unwraps a payload key using the RSA private key and the RSA-OAEP unwrapping mechanism. | CU | 
| [rsa-pkcs](cloudhsm_cli-key-unwrap-rsa-pkcs.md) | Unwraps a payload key using the RSA private key and the RSA-PKCS unwrapping mechanism. | CU | 
| [aes-gcm](cloudhsm_cli-key-wrap-aes-gcm.md) | Wraps a payload key using an AES key on the HSM and the AES-GCM wrapping mechanism. | CU | 
| [aes-no-pad](cloudhsm_cli-key-wrap-aes-no-pad.md) | Wraps a payload key using an AES key on the HSM and the AES-NO-PAD wrapping mechanism. | CU | 
| [aes-pkcs5-pad](cloudhsm_cli-key-wrap-aes-pkcs5-pad.md) | Wraps a payload key using an AES key on the HSM and the AES-PKCS5-PAD wrapping mechanism. | CU | 
| [aes-zero-pad](cloudhsm_cli-key-wrap-aes-zero-pad.md) | Wraps a payload key using an AES key on the HSM and the AES-ZERO-PAD wrapping mechanism. | CU | 
| [cloudhsm-aes-gcm](cloudhsm_cli-key-wrap-cloudhsm-aes-gcm.md) | Wraps a payload key using an AES key on the HSM and the CLOUDHSM-AES-GCM wrapping mechanism. | CUs | 
| [rsa-aes](cloudhsm_cli-key-wrap-rsa-aes.md) | Wraps a payload key using an RSA public key on the HSM and the RSA-AES wrapping mechanism. | CU | 
| [rsa-oaep](cloudhsm_cli-key-wrap-rsa-oaep.md) | Wraps a payload key using an RSA public key on the HSM and the RSA-OAEP wrapping mechanism. | CU | 
| [ Wrap a key with RSA-PKCS using CloudHSM CLIrsa-pkcs  The **key wrap rsa-pkcs** command wraps a payload key using an RSA public key on the HSM and the `RSA-PKCS` wrapping mechanism.   Use the **key wrap rsa-pkcs** command in CloudHSM CLI to wrap a payload key using an RSA public key on the hardware security module (HSM) and the `RSA-PKCS` wrapping mechanism. The payload key’s `extractable` attribute must be set to `true`. Only the owner of a key, that is the crypto user (CU) who created the key, can wrap the key. Users who share the key can use the key in cryptographic operations. To use the **key wrap rsa-pkcs** command, you must first have an RSA key in your AWS CloudHSM cluster. You can generate an RSA key pair using the [The generate-asymmetric-pair category in CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair.md) command and the `wrap` attribute set to `true`.  User type  The following types of users can run this command.   Crypto users (CUs)     Requirements    To run this command, you must be logged in as a CU.     Syntax  

```
aws-cloudhsm > help key wrap rsa-pkcs
Usage: key wrap rsa-pkcs [OPTIONS] --payload-filter [{{<PAYLOAD_FILTER>}}...] --wrapping-filter [{{<WRAPPING_FILTER>}}...]

Options:
      --cluster-id {{<CLUSTER_ID>}}
          Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
      --payload-filter [{{<PAYLOAD_FILTER>}}...]
          Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a payload key
      --wrapping-filter [{{<WRAPPING_FILTER>}}...]
          Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a wrapping key
      --path {{<PATH>}}
          Path to the binary file where the wrapped key data will be saved
      --wrapping-approval {{<WRAPPING_APPROVALR>}}
          File path of signed quorum token file to approve operation for wrapping key
      --payload-approval {{<PAYLOAD_APPROVALR>}}
          File path of signed quorum token file to approve operation for payload key
  -h, --help
          Print help
```   Example  This example shows how to use the **key wrap rsa-pkcs** command using an RSA public key. 

**Example**  

```
aws-cloudhsm > key wrap rsa-pkcs --payload-filter attr.label=payload-key --wrapping-filter attr.label=rsa-public-key-example
{
  "error_code": 0,
  "data": {
    "payload_key_reference": "0x00000000001c08f1",
    "wrapping_key_reference": "0x00000000007008da",
    "wrapped_key_data": "am0Nc7+YE8FWs+5HvU7sIBcXVb24QA0l65nbNAD+1bK+e18BpSfnaI3P+r8Dp+pLu1ofoUy/vtzRjZoCiDofcz4EqCFnGl4GdcJ1/3W/5WRvMatCa2d7cx02swaeZcjKsermPXYRO1lGlfq6NskwMeeTkV8R7Rx9artFrs1y0DdIgIKVaiFHwnBIUMnlQrR2zRmMkfwU1jxMYmOYyD031F5VbnjSrhfMwkww2la7uf/c3XdFJ2+0Bo94c6og/yfPcpOOobJlITCoXhtMRepSdO4OggYq/6nUDuHCtJ86pPGnNahyr7+sAaSI3a5ECQLUjwaIARUCyoRh7EFK3qPXcg=="
  }
```   Arguments   

**{{<CLUSTER\_ID>}}**  
The ID of the cluster to run this operation on.  
Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md) 

**{{<PAYLOAD\_FILTER>}}**  
Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a payload key.  
Required: Yes 

**{{<PATH>}}**  
Path to the binary file where the wrapped key data will be saved.  
Required: No 

**{{<WRAPPING\_FILTER>}}**  
Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a wrapping key.   
Required: Yes 

**{{<WRAPPING\_APPROVALR>}}**  
Specifies the file path to a signed quorum token file to approve operation for wrapping key. Only required if wrapping key's key management service quorum value is greater than 1. 

**{{<PAYLOAD\_APPROVALR>}}**  
Specifies the file path to a signed quorum token file to approve operation for payload key. Only required if payload key's key management service quorum value is greater than 1.    Related topics    [The key wrap command in CloudHSM CLI](cloudhsm_cli-key-wrap.md)   [The key unwrap command in CloudHSM CLI](cloudhsm_cli-key-unwrap.md)    ](cloudhsm_cli-key-wrap-rsa-pkcs.md) | Wraps a payload key using an RSA public key on the HSM and the RSA-PKCS wrapping mechanism. | CU | 
| [login](cloudhsm_cli-login.md) | Log in to your AWS CloudHSM cluster. | Admin, crypto user (CU), and appliance user (AU) | 
| [logout](cloudhsm_cli-logout.md) | Log out of your AWS CloudHSM cluster. | Admin, CU, and appliance user (AU) | 
| [quorum token-sign delete](cloudhsm_cli-qm-token-del.md) | Deletes one or more tokens for a quorum authorized service. | Admin | 
| [quorum token-sign generate](cloudhsm_cli-qm-token-gen.md) | Generates a token for a quorum authorized service. | Admin | 
| [quorum token-sign list](cloudhsm_cli-qm-token-list.md) | Lists all token-sign quorum tokens present in your CloudHSM cluster. | All [1](#cli-ref-1), including unauthenticated users. Login is not required. | 
| [quorum token-sign list-quorum-values](cloudhsm_cli-qm-token-list-qm.md) | Lists the quorum values set in your CloudHSM cluster. | All [1](#cli-ref-1), including unauthenticated users. Login is not required. | 
| [quorum token-sign set-quorum-value](cloudhsm_cli-qm-token-set-qm.md) | Sets a new quorum value for a quorum authorized service. | Admin | 
| [user change-mfa](cloudhsm_cli-user-change-mfa.md) | Changes a user's multi-factor authentication (MFA) strategy. | Admin, CU | 
| [user change-password](cloudhsm_cli-user-change-password.md) | Changes the passwords of users on the HSMs. Any user can change their own password. Admins can change anyone's password. | Admin, CU | 
| [user create](cloudhsm_cli-user-create.md) | Creates a user in your AWS CloudHSM cluster. | Admin | 
| [user delete](cloudhsm_cli-user-delete.md) | Deletes a user in your AWS CloudHSM cluster. | Admin | 
| [user list](cloudhsm_cli-user-list.md) | Lists the users in your AWS CloudHSM cluster. | All [1](#cli-ref-1), including unauthenticated users. Login is not required. | 
| [user change-quorum token-sign register](cloudhsm_cli-user-chqm-token-reg.md) | Registers the quorum token-sign quorum strategy for a user. | Admin | 

**Annotations**
+ [1] All users includes all listed roles and users not logged in.
+ [2] Starting September 1, 2026, ML-DSA is available in FIPS mode for hsm2m.medium clusters.