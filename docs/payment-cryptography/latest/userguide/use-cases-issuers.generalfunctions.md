# Generate or verify a CVV2 for a specific card

[CVV2](terminology.md#terms.cvv2 "terminology.md#terms.cvv2") is a value that is traditionally provided on the back of a card and is used for online purchases. For virtual cards, it might also be displayed on an app or a screen.
Cryptographically, it is the same as CVV1 but with a different service code value.

## Create the key

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CVV2"},{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
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
 "KeyCheckValue": "AEA5CD",
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

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu_. You need that in the next step.

## Generate a CVV2

In this example, we will generate a [CVV2](terminology.md#terms.cvv2 "terminology.md#terms.cvv2") for a given PAN with
inputs of `PAN` and card expiration date.

For all available parameters see [CardVerificationValue2](../DataAPIReference/API_CardVerificationValue2.md "../DataAPIReference/API_CardVerificationValue2.md") in the API reference guide.

```
`$` `aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu --primary-account-number=171234567890123 --generation-attributes CardVerificationValue2='{CardExpiryDate=1127}'`

```

```

                     `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
 "KeyCheckValue": "AEA5CD",
 "ValidationData": "321"
 }`

```

## Validate a CVV2

In this example, we will verify a [CVV2](terminology.md#terms.cvv2 "terminology.md#terms.cvv2") for a given PAN with
inputs of an CVK, `PAN`and card expiration date and the CVV provided during the transaction to validate.

For all available parameters see, [CardVerificationValue2](../DataAPIReference/API_CardVerificationValue2.md "../DataAPIReference/API_CardVerificationValue2.md") in the API reference guide.

###### Note

CVV2 and the other inputs are user entered values. As such, it is not necessarily a sign of an issue that this periodically fails to validate.

```
`$` `aws payment-cryptography-data verify-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu --primary-account-number=171234567890123 --verification-attributes CardVerificationValue2='{CardExpiryDate=1127} --validation-data 321`

```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
 "KeyCheckValue": "AEA5CD",
 "ValidationData": "801"
 }`

```
