# Step 2:

Download the wrapping public key and import token

After you [create a AWS KMS key with no key
material](importing-keys-create-cmk.md "importing-keys-create-cmk.md"), download a wrapping public key and an import token for that KMS key by
using the AWS KMS console or the [GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md") API. The wrapping public key and import token are an
indivisible set that must be used together.

You will use the wrapping public key to [encrypt your key material](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md") for transport. Before downloading an RSA wrapping key pair, you select the length
(key spec) of the RSA wrapping key pair and the wrapping algorithm that you will use to encrypt
your imported key material for transport in [step 3](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md"). AWS KMS also supports the SM2 wrapping key spec (China Regions only).

Each wrapping public key and import token set is valid for 24 hours. If you don't use them
to import key material within 24 hours of downloading them, you must download a new set. You can
download new wrapping public key and import token sets at any time. This lets you change your
RSA wrapping key length ("key spec") or replace a lost set.

You can also download a wrapping public key and import token set to [reimport the same key material](importing-keys-import-key-material.md#reimport-key-material "importing-keys-import-key-material.md#reimport-key-material") into a KMS key. You
might do this to set or change the expiration time for the key material, or to restore expired
or deleted key material. You must download and re-encrypt your key material every time you
import it to AWS KMS.

**Use of the wrapping public key**

The download includes a public key that is unique to your AWS account, also called a
_wrapping public key_.

Before you import key material, you encrypt the key material with the public wrapping
key, and then upload the encrypted key material to AWS KMS. When AWS KMS receives your
encrypted key material, it decrypts the key material with the corresponding private key,
then reencrypts the key material under an AES symmetric key, all within an AWS KMS hardware
security module (HSM).

**Use of the import token**

The download includes an import token with metadata that ensures that your key
material is imported correctly. When you upload your encrypted key material to AWS KMS, you
must upload the same import token that you downloaded in this step.

## Select a wrapping public key spec

To protect your key material during import, you encrypt it using wrapping public key that
you download from AWS KMS, and a supported [wrapping
algorithm](#select-wrapping-algorithm "#select-wrapping-algorithm"). You select a key spec before you download your wrapping public key and
import token. All wrapping key pairs are generated in AWS KMS hardware security modules (HSMs).
The private key never leaves the HSM in plain text.

**RSA wrapping key specs**

The _key spec_ of the wrapping public key determines the
length of the keys in the RSA key pair that protects your key material during its transport to
AWS KMS. In general, we recommend using the longest wrapping public key that is practical. We
offer several wrapping public key specs to support a variety of HSMs and key managers.

AWS KMS supports the following key specs for the RSA wrapping keys used to import key
material of all types, except as noted.

- RSA_4096 (preferred)
- RSA_3072
- RSA_2048

###### Note

The following combination is NOT supported: ECC_NIST_P521 key material, the RSA_2048 public wrapping key spec, and an RSAES_OAEP_SHA\_\* wrapping algorithm.

You cannot directly wrap ECC_NIST_P521 key material with a RSA_2048 public wrapping key. Use a larger wrapping key or an RSA_AES_KEY_WRAP_SHA\_\* wrapping algorithm.

**SM2 wrapping key spec (China Regions only)**

AWS KMS supports the following key spec for the SM2 wrapping keys used to import
asymmetric key material.

- SM2

## Select a wrapping algorithm

To protect your key material during import, you encrypt it using the downloaded wrapping
public key and a supported wrapping algorithm.

AWS KMS supports several standard RSA wrapping algorithms and a two-step hybrid wrapping
algorithm. In general, we recommend using the most secure wrapping algorithm that is
compatible with your imported key material and [wrapping key spec](#select-wrapping-key-spec "#select-wrapping-key-spec"). Typically, you choose an algorithm that is supported by the
hardware security module (HSM) or key management system that protects your key
material.

The following table shows the wrapping algorithms that are supported for each type of key
material and KMS key. The algorithms are listed in preference order.

| Key material                                                                                                                                                                            | Supported wrapping algorithm and spec                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Symmetric encryption key 256-bit AES key<br>128-bit SM4 key (China Regions only)                                                                                                        | Wrapping algorithms:<br>RSAES_OAEP_SHA_256<br>RSAES_OAEP_SHA_1<br>Deprecated wrapping algorithms:<br>RSAES_PKCS1_V1<br>NoteAs of October 10, 2023, AWS KMS does not support the RSAES_PKCS1_V1_5 wrapping algorithm.<br>Wrapping key specs:<br>RSA_2048<br>RSA_3072<br>RSA_4096 |
| Asymmetric RSA private key                                                                                                                                                              | Wrapping algorithms:<br>RSA_AES_KEY_WRAP_SHA_256<br>RSA_AES_KEY_WRAP_SHA_1<br>SM2PKE (China Regions only)<br>Wrapping key specs:<br>RSA_2048<br>RSA_3072<br>RSA_4096<br>SM2 (China Regions only)                                                                                |
| Asymmetric elliptic curve (ECC) private key<br>You cannot use the RSAES_OAEP_SHA\_\<br>• wrapping algorithms with the RSA_2048<br>wrapping key spec to wrap ECC_NIST_P521 key material. | Wrapping algorithms:<br>RSA_AES_KEY_WRAP_SHA_256<br>RSA_AES_KEY_WRAP_SHA_1<br>RSAES_OAEP_SHA_256<br>RSAES_OAEP_SHA_1<br>SM2PKE (China Regions only)<br>Wrapping key specs:<br>RSA_2048<br>RSA_3072<br>RSA_4096<br>SM2 (China Regions only)                                      |
| Asymmetric SM2 private key (China Regions only)                                                                                                                                         | Wrapping algorithms:<br>RSAES_OAEP_SHA_256<br>RSAES_OAEP_SHA_1<br>SM2PKE (China Regions only)<br>Wrapping key specs:<br>RSA_2048<br>RSA_3072<br>RSA_4096<br>SM2 (China Regions only)                                                                                            |
| HMAC key                                                                                                                                                                                | Wrapping algorithms:<br>RSAES_OAEP_SHA_256<br>RSAES_OAEP_SHA_1<br>Wrapping key specs:<br>RSA_2048<br>RSA_3072<br>RSA_4096                                                                                                                                                       |

###### Note

The `RSA_AES_KEY_WRAP_SHA_256` and `RSA_AES_KEY_WRAP_SHA_1`
wrapping algorithms are not supported in China Regions.

- `RSA_AES_KEY_WRAP_SHA_256` – A two-step hybrid wrapping algorithm that
  combines encrypting your key material with an AES symmetric key that you generate, and
  then encrypting the AES symmetric key with the downloaded RSA public wrapping key and the
  RSAES_OAEP_SHA_256 wrapping algorithm.

An `RSA_AES_KEY_WRAP_SHA_*` wrapping algorithm is required for wrapping RSA private key
material, except in China Regions, where you must use the `SM2PKE` wrapping algorithm.

- `RSA_AES_KEY_WRAP_SHA_1` – A two-step hybrid wrapping algorithm that
  combines encrypting your key material with an AES symmetric key that you generate, and
  then encrypting the AES symmetric key with the downloaded RSA wrapping public key and the
  RSAES_OAEP_SHA_1 wrapping algorithm.

An `RSA_AES_KEY_WRAP_SHA_*` wrapping algorithm is required for wrapping RSA
private key material, except in China Regions, where you must use the `SM2PKE` wrapping algorithm.

- `RSAES_OAEP_SHA_256` – The RSA encryption algorithm with Optimal
  Asymmetric Encryption Padding (OAEP) with the SHA-256 hash function.
- `RSAES_OAEP_SHA_1` – The RSA encryption algorithm with Optimal
  Asymmetric Encryption Padding (OAEP) with the SHA-1 hash function.
- `RSAES_PKCS1_V1_5` (Deprecated; as of October 10, 2023, AWS KMS does
  not support the RSAES_PKCS1_V1_5 wrapping algorithm) – The RSA encryption algorithm with the
  padding format defined in PKCS #1 Version 1.5.
- `SM2PKE` (China Regions only) – An elliptic curve based encryption
  algorithm defined by OSCCA in GM/T 0003.4-2012.

###### Topics

- [Downloading the wrapping
  public key and import token (console)](#importing-keys-get-public-key-and-token-console "#importing-keys-get-public-key-and-token-console")
- [Downloading the wrapping public
  key and import token (AWS KMS API)](#importing-keys-get-public-key-and-token-api "#importing-keys-get-public-key-and-token-api")

## Downloading the wrapping

public key and import token (console)

You can use the AWS KMS console to download the wrapping public key and import token.

1. If you just completed the steps to [create a KMS key with no key material](importing-keys-create-cmk.md#importing-keys-create-cmk-console "importing-keys-create-cmk.md#importing-keys-create-cmk-console") and you are on the **Download
   wrapping key and import token** page, skip to [Step 9](#id-wrap-step "#id-wrap-step").
2. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
3. To change the AWS Region, use the Region selector in the upper-right corner of the page.
4. In the navigation pane, choose **Customer managed keys**.

###### Tip

You can import key material only into an KMS key with an
**Origin** of **External (Import key material)**.
This indicates that the KMS key was created with no key material. To add the
**Origin** column to your table, in the upper-right corner of the
page, choose the settings icon (
![Gear or cog icon representing settings or configuration options.](images/console-icon-settings-new.png)
). Turn on **Origin**, and then choose
**Confirm**. 5. Choose the alias or key ID of the KMS key that is pending import. 6. Choose the **Cryptographic configuration** tab and view its values.
The tabs are below the **General configuration** section.

You can only import key material into KMS keys an **Origin** of
**External (Import Key material)**. For information about
creating KMS keys with imported key material, see, [Importing key material for AWS KMS keys](importing-keys.md "importing-keys.md"). 7. Choose the **Key material** tab and then choose **Import key
material**.

The **Key material** tab appears only for KMS keys that have an
**Origin** value of **External (Import Key
material)**. 8. For **Select wrapping key spec**, choose the configuration for your
KMS key. After you create this key, you can't change the key spec. 9. For **Select wrapping algorithm**, choose the option that you will
use to encrypt your key material. For more information about the options, see [Select a Wrapping Algorithm](#select-wrapping-algorithm "#select-wrapping-algorithm"). 10. Choose **Download wrapping public key and import token**, and then
save the file.

If you have a **Next** option, to continue the process now, choose
**Next**. To continue later, choose **Cancel**. 11. Decompress the `.zip` file that you saved in the previous step
(`Import_Parameters_`<key*id>`*`<timestamp>``).

The folder contains the following files:

    * A wrapping public key in a file named
     `WrappingPublicKey.bin`.
    * An import token in a file named `ImportToken.bin`.
    * A text file named README.txt. This file contains information about the wrapping
     public key, the wrapping algorithm to use to encrypt your key material, and the date
     and time when the wrapping public key and import token expire.

12. To continue the process, see [encrypt your key material](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md").

## Downloading the wrapping public

key and import token (AWS KMS API)

To download the public key and import token, use the [GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md") API.
Specify the KMS key that will be associated with the imported key material. This KMS key
must have an [Origin](create-keys.md#key-origin "create-keys.md#key-origin") value of `EXTERNAL`.

###### Note

You can't import key material for ML-DSA KMS keys.

This example specifies the `RSA_AES_KEY_WRAP_SHA_256` wrapping algorithm, the
RSA_3072 wrapping public key spec, and an example key ID. Replace these example values with
valid values for your download. For the key ID, you can use a [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"), but you cannot use an [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name") or [alias
ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") in this operation.

```
`$` `aws kms get-parameters-for-import \
 --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --wrapping-algorithm `RSA_AES_KEY_WRAP_SHA_256` \
 --wrapping-key-spec `RSA_3072``
```

When the command is successful, you see output similar to the following:

```
`{
 "ParametersValidTo": 1568290320.0,
 "PublicKey": "`public key (base64 encoded)`",
 "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "ImportToken": "`import token (base64 encoded)`"
}`
```

To prepare the data for the next step, base64 decode the public key and import token and
save the decoded values in files.

To base64 decode the public key and import token:

1. Copy the base64 encoded public key (represented by `public key (base64
encoded)` in the example output), paste it into a new file, and then save
   the file. Give the file a descriptive name, such as `PublicKey.b64`.
2. Use [OpenSSL](https://openssl.org/ "https://openssl.org/") to base64 decode the file's
   contents and save the decoded data to a new file. The following example decodes the data
   in the file that you saved in the previous step (`PublicKey.b64`) and saves the
   output to a new file named `WrappingPublicKey.bin`.

```
`$` `openssl enc -d -base64 -A -in PublicKey.b64 -out WrappingPublicKey.bin`
```

3. Copy the base64 encoded import token (represented by `import token (base64
encoded)` in the example output), paste it into a new file, and then save
   the file. Give the file a descriptive name, for example
   `importtoken.b64`.
4. Use [OpenSSL](https://openssl.org/ "https://openssl.org/") to base64 decode the file's
   contents and save the decoded data to a new file. The following example decodes the data
   in the file that you saved in the previous step (`ImportToken.b64`) and saves
   the output to a new file named `ImportToken.bin`.

```
`$` `openssl enc -d -base64 -A -in importtoken.b64 -out ImportToken.bin`
```

Proceed to [Step 3: Encrypt the
key material](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md").
