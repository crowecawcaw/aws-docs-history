# AES key wrapping in AWS CloudHSM

This topic describes the options for AES key wrapping in AWS CloudHSM. AES key wrapping uses an AES
key (the wrapping key) to wrap another key of any type (the target key). You use key wrapping to
protect stored keys or transmit keys over insecure networks.

###### Topics

- [Supported algorithms](#supported-types "#supported-types")
- [Using AES key wrap in AWS CloudHSM](#use-aes-key-wrap "#use-aes-key-wrap")

## Supported algorithms

AWS CloudHSM offers three options for AES key wrapping, each based on how the target key is
padded before being wrapped. Padding is done automatically, in accordance with the algorithm
you use, when you call key wrap. The following table lists the supported algorithms and
associated details to help you choose an appropriate wrapping mechanism for your
application.

| AES Key Wrap Algorithm            | Specification                                                                                                                                                                                                                                                    | Supported Target Key Types              | Padding Scheme                                                          | AWS CloudHSM Client Availability |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | -------------------------------- |
| AES Key Wrap with Zero Padding    | [RFC 5649](https://tools.ietf.org/html/rfc5649 "https://tools.ietf.org/html/rfc5649") and [SP<br>800–38F](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38F.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38F.pdf") | All                                     | Adds zeros after key bits, if necessary, to block align                 | SDK 3.1 and later                |
| AES Key Wrap with No Padding      | [RFC 3394](https://tools.ietf.org/html/rfc3394 "https://tools.ietf.org/html/rfc3394") and [SP<br>800–38F](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38F.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38F.pdf") | Block-aligned keys such as AES and 3DES | None                                                                    | SDK 3.1 and later                |
| AES Key Wrap with PKCS #5 Padding | None                                                                                                                                                                                                                                                             | All                                     | At least 8 bytes are added as per PKCS #5 padding scheme to block align | All                              |

To learn how to use the AES key wrap algorithms from the preceding table in your
application, see [Using AES Key Wrap in AWS CloudHSM.](#use-aes-key-wrap "#use-aes-key-wrap")

### Understanding initialization vectors in AES key

wrap

Prior to wrapping, CloudHSM appends an initialization vector (IV) to the target key for
data integrity. Each key wrap algorithm has specific restrictions on what type of IV is
allowed. To set the IV in AWS CloudHSM, you have two options:

- Implicit: set the IV to NULL and CloudHSM uses the default value for that algorithm
  for wrap and unwrap operations (recommended)
- Explicit: set the IV by passing the default IV value to the key wrap function

###### Important

You must understand what IV you are using in your application. To unwrap the key, you
must provide the same IV that you used to wrap the key. If you use an implicit IV to wrap,
then use an implicit IV to unwrap. With an implicit IV, CloudHSM will use the default
value to unwrap.

The following table describes permitted values for IVs, which the wrapping algorithm
specifies.

| AES Key Wrap Algorithm            | Implicit IV                                                                  | Explicit IV                                               |
| --------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------- |
| AES Key Wrap with Zero Padding    | Required Default value: (IV calculated internally based on<br>specification) | Not allowed                                               |
| AES Key Wrap with No Padding      | Allowed (recommended) Default value:<br>`0xA6A6A6A6A6A6A6A6`                 | Allowed Only this value accepted:<br>`0xA6A6A6A6A6A6A6A6` |
| AES Key Wrap with PKCS #5 Padding | Allowed (recommended) Default value:<br>`0xA6A6A6A6A6A6A6A6`                 | Allowed Only this value accepted:<br>`0xA6A6A6A6A6A6A6A6` |

## Using AES key wrap in AWS CloudHSM

You wrap and unwrap keys as follows:

- In the [PKCS #11 library](pkcs11-library.md "pkcs11-library.md"), select the appropriate mechanism
  for the `C_WrapKey` and `C_UnWrapKey` functions as shown in the following table.
- In the [JCE provider](java-library.md "java-library.md"), select the appropriate algorithm,
  mode and padding combination, implementing cipher methods `Cipher.WRAP_MODE`
  and `Cipher.UNWRAP_MODE` as shown in the following table.
- In the [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md"), choose the appropriate algorithm from
  the list of supported [The key wrap command in CloudHSM CLI](cloudhsm_cli-key-wrap.md "cloudhsm_cli-key-wrap.md") and [The key unwrap command in CloudHSM CLI](cloudhsm_cli-key-unwrap.md "cloudhsm_cli-key-unwrap.md") algorithms as
  shown in the following table.
- In [key_mgmt_util (KMU)](key_mgmt_util.md "key_mgmt_util.md"), use commands
  [Export an AWS CloudHSM key using KMU](key_mgmt_util-wrapKey.md "key_mgmt_util-wrapKey.md") and [Unwrap an AWS CloudHSM key using KMU](key_mgmt_util-unwrapKey.md "key_mgmt_util-unwrapKey.md")
  with appropriate m values as shown in
  the following table.

| AES Key Wrap Algorithm            | PKCS #11 Mechanism                                                    | Java Method                | CloudHSM CLI Sub Command | Key Management Utility (KMU) Argument |
| --------------------------------- | --------------------------------------------------------------------- | -------------------------- | ------------------------ | ------------------------------------- |
| AES Key Wrap with Zero Padding    | • `CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD` (Vendor Defined Mechanism)     | `AESWrap/ECB/ZeroPadding`  | aes-zero-pad             | m = 6                                 |
| AES Key Wrap with No Padding      | • `CKM_CLOUDHSM_AES_KEY_WRAP_NO_PAD` (Vendor Defined<br>Mechanism)    | `AESWrap/ECB/NoPadding`    | aes-no-pad               | m = 5                                 |
| AES Key Wrap with PKCS #5 Padding | • `CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD` (Vendor Defined<br>Mechanism) | `AESWrap/ECB/PKCS5Padding` | aes-pkcs5-pad            | m = 4                                 |
