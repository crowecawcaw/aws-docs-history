# Validate a PIN against previously stored IBM3624 pin offset

In this example, we will validate a cardholder provided PIN against the pin offset stored on file with the card issuer/processor. The inputs are similar to [Generate IBM3624 pin offset for a pin](generate-ibm3624.md "generate-ibm3624.md")
with the additional of the encrypted pin provided by the payment terminal (or other upstream provider such as card network). If the pin matches, the api will return http 200.
where the outputs will be an encrypted `PIN block` (PinData.PinBlock) and an `IBM3624` offset value (pinData.Offset).

This command requires that the pin generation key is of type `TR31_V1_IBM3624_PIN_VERIFICATION_KEY` and the encryption key is of type `TR31_P0_PIN_ENCRYPTION_KEY`

###### Example

```
`$` `aws payment-cryptography-data generate-pin-data --generation-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --generation-attributes Ibm3624RandomPin="{DecimalizationTable=9876543210654321,PinValidationDataPadCharacter=D,PinValidationData=171234567890123}"`
```

```
`{
"GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2",
"GenerationKeyCheckValue": "7F2363",
"EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
"EncryptionKeyCheckValue": "7CC9E2",
"EncryptedPinBlock": "AC17DC148BDA645E",
"PinData": {
 "PinOffset": "5507"
}
}`
```
