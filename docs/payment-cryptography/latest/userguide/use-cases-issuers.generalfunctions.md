# Generate a random pin and the associated PVV and then verify the value

###### Topics

- [Create the key(s)](#use-cases-issuers.generalfunctions.pvv.setup "#use-cases-issuers.generalfunctions.pvv.setup")
- [Generate a random pin, generate PVV and return the encrypted PIN and PVV](#use-cases-issuers.generalfunctions.pvv.generate "#use-cases-issuers.generalfunctions.pvv.generate")
- [Validate encrypted PIN using PVV method](#use-cases-issuers.generalfunctions.pvv.verify "#use-cases-issuers.generalfunctions.pvv.verify")

## Create the key(s)

In order to generate a random pin and the [PVV](terminology.md#terms.pvv "terminology.md#terms.pvv"), you'll need two keys, a [Pin Verification Key(PVK)](terminology.md#terms.pvk "terminology.md#terms.pvk")
for generating the PVV and a [Pin Encryption Key](terminology.md#terms.pek "terminology.md#terms.pek") for encrypting the pin. The pin itself is randomly generated securely inside the service
and is not related to either key cryptographically.

The PGK must be a key of algorithm TDES_2KEY based on the PVV algorithm itself. A PEK can be TDES_2KEY, TDES_3KEY or AES_128. In this case, since the PEK is
intended for internal use within your system, AES_128 would be a good choice. If a PEK is used for interchange with other systems (e.g. card networks, acquirers, ATMs) or
are being moved as part of a migration, TDES_2KEY may be the more appropriate choice for compatibility reasons.

### Create the PEK

```
`$` `aws payment-cryptography create-key \
 --exportable
 --key-attributes KeyAlgorithm=AES_128,KeyUsage=TR31_P0_PIN_ENCRYPTION_KEY,\
 KeyClass=SYMMETRIC_KEY,\
 KeyModesOfUse='{Encrypt=true,Decrypt=true,Wrap=true,Unwrap=true}' --tags='[{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
 "KeyAttributes": {
 "KeyUsage": "TR31_P0_PIN_ENCRYPTION_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "AES_128",
 "KeyModesOfUse": {
 "Encrypt": false,
 "Decrypt": false,
 "Wrap": false,
 "Unwrap": false,
 "Generate": true,
 "Sign": false,
 "Verify": true,
 "DeriveKey": false,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "7CC9E2",
 "KeyCheckValueAlgorithm": "CMAC",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
 "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
 }
 }`
```

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt_. You need that in the next step.

### Create the PVK

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_V2_VISA_PIN_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza",
 "KeyAttributes": {
 "KeyUsage": "TR31_V2_VISA_PIN_VERIFICATION_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "TDES_2KEY",
 "KeyModesOfUse": {
 "Encrypt": false,
 "Decrypt": false,
 "Wrap": false,
 "Unwrap": false,
 "Generate": true,
 "Sign": false,
 "Verify": true,
 "DeriveKey": false,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "51A200",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
 "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
 }
 }`
```

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza_. You need that in the next step.

## Generate a random pin, generate PVV and return the encrypted PIN and PVV

In this example, we will generate a new (random) 4 digit pin where the outputs will be an encrypted `PIN block` (PinData.PinBlock) and a `PVV` (pinData.VerificationValue). The key inputs are
`PAN`, the `Pin Verification Key`(also known as the pin generation key),
the `Pin Encryption Key` and the [PIN Block](terminology.md#terms.pinblock "terminology.md#terms.pinblock") format.

This command requires that the key is of type `TR31_V2_VISA_PIN_VERIFICATION_KEY`.

```
`$` `aws payment-cryptography-data generate-pin-data --generation-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --generation-attributes VisaPin={PinVerificationKeyIndex=1}`
```

```
`{
 "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2",
 "GenerationKeyCheckValue": "7F2363",
 "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
 "EncryptionKeyCheckValue": "7CC9E2",
 "EncryptedPinBlock": "AC17DC148BDA645E",
 "PinData": {
 "VerificationValue": "5507"
 }
 }`
```

## Validate encrypted PIN using PVV method

In this example, we will validate a PIN for a given PAN. The PIN is
typically provided by the
cardholder or user during transaction time for validation and is
compared against the value on file (the input from the cardholder is provided as an encrypted value from the terminal or other upstream provider).
In order to validate this input, the
following values will also be provided at runtime -
The encrypted pin, the key used to encrypt the input pin (often referred to as an [IWK](terminology.md#terms.iwk "terminology.md#terms.iwk")),
`PAN` and the value
to verify against (either a `PVV` or `PIN offset`).

If AWS Payment Cryptography is able to validate the pin, an http/200 is returned. If the pin is not validated, it will return an http/400.

```
`$` `aws payment-cryptography-data verify-pin-data --verification-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --verification-attributes VisaPin="{PinVerificationKeyIndex=1,VerificationValue=5507}" --encrypted-pin-block AC17DC148BDA645E`

```

```
`{
 "VerificationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2",
 "VerificationKeyCheckValue": "7F2363",
 "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
 "EncryptionKeyCheckValue": "7CC9E2",
}`
```
