# Generate Visa PVV for a pin

In this example, we will generate a new (random) pin where the outputs will be an encrypted `PIN block` (PinData.PinBlock) and a `PVV` (pinData.Offset). The key inputs are
`PAN`, the `Pin Verification Key`, the `Pin Encryption Key` and the `PIN block format`.

This command requires that the key is of type `TR31_V2_VISA_PIN_VERIFICATION_KEY`.

```
`$` `aws payment-cryptography-data generate-pin-data --generation-key-identifier arn:aws:payment-cryptography:us-east-2::key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2::key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --generation-attributes VisaPin={PinVerificationKeyIndex=1}`
```

```
`{
 "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2::key/37y2tsl45p5zjbh2",
 "GenerationKeyCheckValue": "7F2363",
 "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2::key/ivi5ksfsuplneuyt",
 "EncryptionKeyCheckValue": "7CC9E2",
 "EncryptedPinBlock": "AC17DC148BDA645E",
 "PinData": {
 "VerificationValue": "5507"
 }
 }`
```
