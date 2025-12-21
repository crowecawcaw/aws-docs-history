# Decrypt data

The `Decrypt Data` API is used to decrypt data using symmetric and asymmetric data encryption keys as well as [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") and [EMV](terminology.md#terms.emv "terminology.md#terms.emv") derived keys.
Various algorithms and variations are supported including `TDES`, `RSA` and `AES`.

The primary inputs are the decryption key used to decrypt the data, the ciphertext data in hexBinary format to be decrypted and decryption attributes such as initialization vector, mode as block ciphers etc.
The primary outputs include the decrypted data as plaintext in hexBinary format and the checksum value for the decryption key. For details on all available options, please consult the API Guide for [Decrypt](../DataAPIReference/API_DecryptData.md "../DataAPIReference/API_DecryptData.md").

###### Examples

- [Decrypt data using AES symmetric key](#w2aac15c16c13b9 "#w2aac15c16c13b9")
- [Decrypt data using DUKPT key](#w2aac15c16c13c11 "#w2aac15c16c13c11")
- [Decrypt data using EMV-derived symmetric key](#w2aac15c16c13c13 "#w2aac15c16c13c13")
- [Decrypt data using an RSA key](#crypto-ops.decrypt-rsa "#crypto-ops.decrypt-rsa")

## Decrypt data using AES symmetric key

In this example, we will decrypt ciphertext data using a symmetric key. This example shows an `AES` key but `TDES_2KEY` and `TDES_3KEY` are also supported.
For this operation, the key must have KeyModesOfUse set to `Decrypt` and KeyUsage set to `TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more options.

```
`$` `aws payment-cryptography-data decrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --cipher-text 33612AB9D6929C3A828EB6030082B2BD --decryption-attributes 'Symmetric={Mode=CBC}'`

```

```

         `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "71D7AE",
 "PlainText": "31323334313233343132333431323334"
}`

```

## Decrypt data using DUKPT key

###### Note

Using decrypt-data with DUKPT for P2PE transactions may return credit card PAN and other cardholder data to your application that will need to accounted for when determining its PCI DSS scope.

In this example, we will decrypt ciphertext data using a [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") key which has been created using the [CreateKey](create-keys.md "create-keys.md") Operation or imported using the [ImportKey](keys-import.md "keys-import.md") Operation.
For this operation, the key must have KeyModesOfUse set to `DeriveKey` and KeyUsage set to `TR31_B0_BASE_DERIVATION_KEY`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more options.
When you use `DUKPT`, for `TDES` algorithm, the ciphertext data length must be a multiple of 16 bytes. For `AES` algorithm, the ciphertext data length must be a multiple of 32 bytes.

```
`$` `aws payment-cryptography-data decrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --cipher-text 33612AB9D6929C3A828EB6030082B2BD --decryption-attributes 'Dukpt={KeySerialNumber=FFFF9876543210E00001}'`

```

```

         `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "71D7AE",
 "PlainText": "31323334313233343132333431323334"
}`

```

## Decrypt data using EMV-derived symmetric key

In this example, we will decrypt ciphertext data using an EMV-derived symmetric key which has been created using the [CreateKey](create-keys.md "create-keys.md") operation or imported using the [ImportKey](keys-import.md "keys-import.md") operation.
For this operation, the key must have KeyModesOfUse set to `Derive` and KeyUsage set to `TR31_E1_EMV_MKEY_CONFIDENTIALITY` or `TR31_E6_EMV_MKEY_OTHER`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more details.

```
`$` `aws payment-cryptography-data decrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --cipher-text 33612AB9D6929C3A828EB6030082B2BD --decryption-attributes 'Emv={MajorKeyDerivationMode=EMV_OPTION_A,PanSequenceNumber=27,PrimaryAccountNumber=1000000000000432,SessionDerivationData=02BB000000000000, InitializationVector=1500000000000999,Mode=CBC}'`

```

```
`{
"KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
"KeyCheckValue": "71D7AE",
"PlainText": "31323334313233343132333431323334"
}`
```

## Decrypt data using an RSA key

In this example, we will decrypt ciphertext data using an [RSA key pair](terminology.md#terms.privatekey "terminology.md#terms.privatekey") which has been created using the [CreateKey](create-keys.md "create-keys.md") operation.
For this operation, the key must have KeyModesOfUse set to enable `Decrypt` and KeyUsage set to `TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION`. Please see [Keys for Cryptographic Operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md") for more options.

For PKCS #7 or other padding schemes not currently supported, please select no padding by omitting the padding indicator _'Asymmetric={}'_ and remove padding subsequent to calling the service.

```
`$` `aws payment-cryptography-data decrypt-data \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/5dza7xqd6soanjtb --cipher-text 8F4C1CAFE7A5DEF9A40BEDE7F2A264635C... \
 --decryption-attributes 'Asymmetric={PaddingType=OAEP_SHA256}'`

```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/5dza7xqd6soanjtb",
 "KeyCheckValue": "FF9DE9CE",
 "PlainText": "31323334313233343132333431323334"
}`
```
