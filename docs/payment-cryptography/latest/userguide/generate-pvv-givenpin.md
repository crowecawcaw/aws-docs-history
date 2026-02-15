# Generate a Visa PVV for a known pin

###### Example

In this example, we will generate a PVV for a given (encrypted) pin. An encrypted pin may be received upstream such
as from a payment terminal or from a cardholder using the
[user selectable pin flow](https://github.com/aws-samples/samples-for-payment-cryptography-service/tree/main/python_sdk_example/ecdh_flows "https://github.com/aws-samples/samples-for-payment-cryptography-service/tree/main/python_sdk_example/ecdh_flows"). The key inputs are
`PAN`,
the `Pin Verification Key`,
the `Pin Encryption Key`,
the `Encrypted Pin Block`
and the `PIN block format`.

```
`$` `aws payment-cryptography-data generate-pin-data --generation-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --generation-attributes VisaPinVerificationValue={PinVerificationKeyIndex=1,EncryptedPinBlock=AA584CED31790F37}`
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
