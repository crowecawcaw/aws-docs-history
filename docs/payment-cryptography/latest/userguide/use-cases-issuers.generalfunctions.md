# Generate or verify a CVV for a given card

[CVV](terminology.md#terms.cvv "terminology.md#terms.cvv") or CVV1 is a value that is traditionally embedded in a cards magnetic stripe. It is not the same as CVV2 (visible to the cardholder and for use for online purchases).

The first step is to create a key. For this tutorial,
you create a [CVK](terminology.md#terms.cvk "terminology.md#terms.cvk") double-length 3DES (2KEY TDES) key.

###### Note

CVV, CVV2 and iCVV all use similar if not identical algorithms but vary the input data. All use the same key type TR31_C0_CARD_VERIFICATION_KEY
but it is recommended to use separate keys for each purpose. These can be distinguished using aliases and/or tags as in the example below.

## Create the key

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CVV"},{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/r52o3wbqxyf6qlqr",
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
 "KeyCheckValue": "DE89F9",
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

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/r52o3wbqxyf6qlqr_. You need that in the next step.

## Generate a CVV

In this example, we will generate a [CVV](terminology.md#terms.cvv "terminology.md#terms.cvv") for a given PAN with
inputs of `PAN`,a service code(as defined by ISO/IEC 7813) of 121 and card expiration date.

For all available parameters see [CardVerificationValue1](../DataAPIReference/API_CardVerificationValue1.md "../DataAPIReference/API_CardVerificationValue1.md") in the API reference guide.

```
`$` `aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/r52o3wbqxyf6qlqr --primary-account-number=171234567890123 --generation-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=121}'`

```

```

                  `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/r52o3wbqxyf6qlqr",
 "KeyCheckValue": "DE89F9",
 "ValidationData": "801"
 }`

```

## Validate CVV

In this example, we will verify a [CVV](terminology.md#terms.cvv "terminology.md#terms.cvv") for a given PAN with
inputs of an CVK, `PAN`,
a service code of 121, card expiration date and the CVV provided during the transaction to validate.

For all available parameters see, [CardVerificationValue1](../DataAPIReference/API_CardVerificationValue1.md "../DataAPIReference/API_CardVerificationValue1.md") in the API reference guide.

###### Note

CVV is not a user entered value (like CVV2) but is typically embedded on a magstripe.
Consideration should be given to whether it should always validate when provided.

```
`$` `aws payment-cryptography-data verify-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/r52o3wbqxyf6qlqr --primary-account-number=171234567890123 --verification-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=121} --validation-data 801`

```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/r52o3wbqxyf6qlqr",
 "KeyCheckValue": "DE89F9",
 "ValidationData": "801"
}`

```
