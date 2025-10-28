# Get keys

An AWS Payment Cryptography key represents a single unit of cryptographic material and can only be used for cryptographic operations for this service.
The GetKeys API takes a KeyIdentifier as input and returns key metadata including attributes, state, and timestamps, but does not return actual cryptographic key material.

```
`$` `aws payment-cryptography get-key --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`

```

```

`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h",
 "KeyAttributes": {
 "KeyUsage": "TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "AES_128",
 "KeyModesOfUse": {
 "Encrypt": true,
 "Decrypt": true,
 "Wrap": true,
 "Unwrap": true,
 "Generate": false,
 "Sign": false,
 "Verify": false,
 "DeriveKey": false,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "0A3674",
 "KeyCheckValueAlgorithm": "CMAC",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2023-06-02T07:38:14.913000-07:00",
 "UsageStartTimestamp": "2023-06-02T07:38:14.857000-07:00"
 }
}`


```
