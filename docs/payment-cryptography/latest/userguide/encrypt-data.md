# Encrypt data

The `Encrypt Data` API is used to encrypt data using symmetric and asymmetric data encryption keys as well as [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") and [EMV](terminology.md#terms.emv "terminology.md#terms.emv") derived keys.
Various algorithms and variations are supported including `TDES`, `RSA` and `AES`.

The primary inputs are the encryption key used to encrypt the data, the plaintext data in hexBinary format to be encrypted and encryption attributes such as initialization vector and mode for block ciphers such as TDES. The plaintext data needs to be in multiples of 8 bytes for `TDES`, 16 bytes for `AES` and
the length of the key in the case of `RSA`. Symmetric key inputs (TDES, AES, DUKPT, EMV) should be padded in cases where the input data does not meet these requirements. The following table shows the maximum length of plaintext for each type of key and the padding type that you define in `EncryptionAttributes`
for RSA keys.

| Padding type  | RSA_2048 | RSA_3072 | RSA_4096 |
| ------------- | -------- | -------- | -------- |
| `OAEP SHA1`   | 428      | 684      | 940      |
| `OAEP SHA256` | 380      | 636      | 892      |
| `OAEP SHA512` | 252      | 508      | 764      |
| `PKCS1`       | 488      | 744      | 1000     |
| `None`        | 488      | 744      | 1000     |

The primary outputs include the encrypted data as ciphertext in hexBinary format and the checksum value for the encryption key. For details on all available options, please consult the API Guide for [Encrypt](../DataAPIReference/API_EncryptData.md "../DataAPIReference/API_EncryptData.md").

###### Examples

- [Encrypt data using AES symmetric key](#w4aac15c16c11c13 "#w4aac15c16c11c13")
- [Encrypt data using DUKPT key](#w4aac15c16c11c15 "#w4aac15c16c11c15")
- [Encrypt data using EMV-derived symmetric key](#w4aac15c16c11c17 "#w4aac15c16c11c17")
- [Encrypt data using an RSA key](#crypto-ops.encrypt-rsa "#crypto-ops.encrypt-rsa")

## Encrypt data using AES symmetric key

###### Note

All examples assume the relevant key already exists. Keys can be created using the [CreateKey](create-keys.md "create-keys.md") operation or imported using the [ImportKey](keys-import.md "keys-import.md") operation.

In this example, we will encrypt plaintext data using a symmetric key which has been created using the [CreateKey](create-keys.md "create-keys.md") Operation or imported using the [ImportKey](keys-import.md "keys-import.md") Operation.
For this operation, the key must have KeyModesOfUse set to `Encrypt` and KeyUsage set to `TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more options.

```
`$` `aws payment-cryptography-data encrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --plain-text 31323334313233343132333431323334 --encryption-attributes 'Symmetric={Mode=CBC}'`

```

```

         `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "71D7AE",
 "CipherText": "33612AB9D6929C3A828EB6030082B2BD"
}`

```

## Encrypt data using DUKPT key

In this example, we will encrypt plaintext data using a [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") key. AWS Payment Cryptography supports `TDES` and `AES` DUKPT keys.
For this operation, the key must have KeyModesOfUse set to `DeriveKey` and KeyUsage set to `TR31_B0_BASE_DERIVATION_KEY`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more options.

```
`$` `aws payment-cryptography-data encrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --plain-text 31323334313233343132333431323334 --encryption-attributes 'Dukpt={KeySerialNumber=FFFF9876543210E00001}'`

```

```

         `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "71D7AE",
 "CipherText": "33612AB9D6929C3A828EB6030082B2BD"
}`

```

## Encrypt data using EMV-derived symmetric key

In this example, we will encrypt clear text data using an EMV-derived symmetric key which has already been created. You might use a command such as this to send data to an EMV card.
For this operation, the key must have KeyModesOfUse set to `Derive` and KeyUsage set to `TR31_E1_EMV_MKEY_CONFIDENTIALITY` or `TR31_E6_EMV_MKEY_OTHER`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more details.

```
`$` `aws payment-cryptography-data encrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --plain-text 33612AB9D6929C3A828EB6030082B2BD --encryption-attributes 'Emv={MajorKeyDerivationMode=EMV_OPTION_A,PanSequenceNumber=27,PrimaryAccountNumber=1000000000000432,SessionDerivationData=02BB000000000000, InitializationVector=1500000000000999,Mode=CBC}'`
```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "71D7AE",
 "CipherText": "33612AB9D6929C3A828EB6030082B2BD"
}`
```

## Encrypt data using an RSA key

In this example, we will encrypt plaintext data using an [RSA public key](terminology.md#terms.publickey "terminology.md#terms.publickey") which has been imported using the [ImportKey](keys-import.md "keys-import.md") operation.
For this operation, the key must have KeyModesOfUse set to `Encrypt` and KeyUsage set to `TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more options.

For PKCS #7 or other padding schemes not currently supported, please apply prior to calling the service and select no padding by omitting the padding indicator _'Asymmetric={}'_

```
`$` `aws payment-cryptography-data encrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2::key/thfezpmsalcfwmsg --plain-text 31323334313233343132333431323334 --encryption-attributes 'Asymmetric={PaddingType=OAEP_SHA256}'`

```

```

     `{
 "CipherText": "12DF6A2F64CC566D124900D68E8AFEAA794CA819876E258564D525001D00AC93047A83FB13 \
 E73F06329A100704FA484A15A49F06A7A2E55A241D276491AA91F6D2D8590C60CDE57A642BC64A897F4832A3930 \
 0FAEC7981102CA0F7370BFBF757F271EF0BB2516007AB111060A9633D1736A9158042D30C5AE11F8C5473EC70F067 \
 72590DEA1638E2B41FAE6FB1662258596072B13F8E2F62F5D9FAF92C12BB70F42F2ECDCF56AADF0E311D4118FE3591 \
 FB672998CCE9D00FFFE05D2CD154E3120C5443C8CF9131C7A6A6C05F5723B8F5C07A4003A5A6173E1B425E2B5E42AD \
 7A2966734309387C9938B029AFB20828ACFC6D00CD1539234A4A8D9B94CDD4F23A",
 "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/5dza7xqd6soanjtb",
 "KeyCheckValue": "FF9DE9CE"
}`

```
