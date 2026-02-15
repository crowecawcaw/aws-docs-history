# Generate or verify a iCVV for a specific card

[iCVV](terminology.md#terms.icvv "terminology.md#terms.icvv") uses the same algorithm as CVV/CVV2 but iCVV is embedded inside a chip card. Its service code is 999.

## Create the key

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"ICVV"},{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/c7dsi763r6s7lfp3",
 "KeyAttributes": {
 "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY",
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
 "KeyCheckValue": "1201FB",
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

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/c7dsi763r6s7lfp3_. You need that in the next step.

## Generate a iCVV

###### Example

In this example, we will generate a [iCVV](terminology.md#terms.icvv "terminology.md#terms.icvv") for a given PAN with
inputs of `PAN`,a service code(as defined by ISO/IEC 7813) of 999 and card expiration date.

For all available parameters see [CardVerificationValue1](../DataAPIReference/API_CardVerificationValue1.md "../DataAPIReference/API_CardVerificationValue1.md") in the API reference guide.

```
`$` `aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/c7dsi763r6s7lfp3 --primary-account-number=171234567890123 --generation-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=999}'`

```

```

                     `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/c7dsi763r6s7lfp3",
 "KeyCheckValue": "1201FB",
 "ValidationData": "532"
 }`

```

## Validate iCVV

###### Example

For validation, the inputs are CVK, `PAN`,
a service code of 999, card expiration date and the iCVV provided during the transaction to validate.

For all available parameters see, [CardVerificationValue1](../DataAPIReference/API_CardVerificationValue1.md "../DataAPIReference/API_CardVerificationValue1.md") in the API reference guide.

###### Note

iCVV is not a user entered value (like CVV2) but is typically embedded on an EMV/chip card.
Consideration should be given to whether it should always validate when provided.

```
`$` `aws payment-cryptography-data verify-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/c7dsi763r6s7lfp3 --primary-account-number=171234567890123 --verification-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=999} --validation-data 532`

```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/c7dsi763r6s7lfp3",
 "KeyCheckValue": "1201FB",
 "ValidationData": "532"
 }`
```
