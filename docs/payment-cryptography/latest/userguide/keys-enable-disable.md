# Enabling and disabling keys

You can disable and re-enable AWS Payment Cryptography keys. When you create key, it is enabled by
default. If you disable a key, it cannot be used in any [cryptographic operation](data-operations.md "data-operations.md") until you re-enable
it. Start/stop usage commands take immediate effect, so it's recommended that
you review usage before making such a change. You can also set a change (start or stop usage) to take effect in the future using the optional
`timestamp` parameter.

Because it's temporary and easily undone, disabling an AWS Payment Cryptography key is a safer alternative to
deleting an AWS Payment Cryptography key, an action that is destructive and irreversible. If you are considering
deleting an AWS Payment Cryptography key, disable it first and ensure that you will not need to use
the key to encrypt or decrypt data in the future.

###### Topics

- [Start key usage](#keys-startusage "#keys-startusage")
- [Stop key usage](#keys-stopusage "#keys-stopusage")

## Start key usage

Key usage must be enabled in order to use a key for cryptographic operations. If a key is not enabled, you can use this
operation to make it usable. The field `UsageStartTimestamp` will represent when the key became/will become
active. This will be in the past for an enabled token, and in the future if pending activation.

In this example, a key is requested to be enabled for key usage. The response includes the key information
and the enable flag has been transitioned to true. This will also be reflected in list-keys response object.

```
`$` `aws payment-cryptography start-key-usage --key-identifier "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh"`
```

```
`{
 "Key": {
 "CreateTimestamp": "2022-10-12T10:58:28.920000-07:00",
 "Enabled": true,
 "Exportable": true,
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh",
 "KeyAttributes": {
 "KeyAlgorithm": "TDES_3KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyModesOfUse": {
 "Decrypt": true,
 "DeriveKey": false,
 "Encrypt": true,
 "Generate": false,
 "NoRestrictions": false,
 "Sign": false,
 "Unwrap": true,
 "Verify": false,
 "Wrap": true
 },
 "KeyUsage": "TR31_P1_PIN_GENERATION_KEY"
 },
 "KeyCheckValue": "369D",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "KeyState": "CREATE_COMPLETE",
 "UsageStartTimestamp": "2022-10-27T14:09:59.468000-07:00"
 }
}`
```

## Stop key usage

If you no longer plan to use a key, you can stop the key usage to prevent further cryptographic operations.
This operation is not permanent, so you are able to reverse it using [starting key usage](#keys-startusage "#keys-startusage"). You can also set a key to be disabled in the future. The field `UsageStopTimestamp`
will represent when the key became/will become disabled.

In this example, it's requested to stop key usage in the future. After execution, this key cannot be used
for cryptographic operations unless re-enabled via [start key usage](#keys-startusage "#keys-startusage") The response includes the key information
and the enable flag has been transitioned to false. This will also be reflected in list-keys response object.

```
`$` `aws payment-cryptography stop-key-usage --key-identifier "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh"`
```

```
`{
 "Key": {
 "CreateTimestamp": "2022-10-12T10:58:28.920000-07:00",
 "Enabled": false,
 "Exportable": true,
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh",
 "KeyAttributes": {
 "KeyAlgorithm": "TDES_3KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyModesOfUse": {
 "Decrypt": true,
 "DeriveKey": false,
 "Encrypt": true,
 "Generate": false,
 "NoRestrictions": false,
 "Sign": false,
 "Unwrap": true,
 "Verify": false,
 "Wrap": true
 },
 "KeyUsage": "TR31_P1_PIN_GENERATION_KEY"
 },
 "KeyCheckValue": "369D",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "KeyState": "CREATE_COMPLETE",
 "UsageStopTimestamp": "2022-10-27T14:09:59.468000-07:00"
 }
}`
```
