# Verify PIN data

Verify PIN data functions are used for verifying whether a pin is correct.
This typically involves comparing the pin value previously stored against what was entered by the cardholder
at a POI. These functions compare two values without exposing the underlying value of either source.

## Validate encrypted PIN using PVV method

In this example, we will validate a PIN for a given PAN. The PIN is
typically provided by the
cardholder or user during transaction time for validation and is
compared against the value on file (the input from the cardholder is provided as an encrypted value from the terminal or other upstream provider).
In order to validate this input, the
following values will also be provided at runtime:
The key used to encrypt the input pin (this is often an `IWK`),
`PAN` and the value
to verify against (either a `PVV` or `PIN offset`).

If AWS Payment Cryptography is able to validate the pin, an http/200 is returned. If the pin is not validated, it will return an http/400.

```
`$` `aws payment-cryptography-data verify-pin-data --verification-key-identifier arn:aws:payment-cryptography:us-east-2::key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2::key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --verification-attributes VisaPin="{PinVerificationKeyIndex=1,VerificationValue=5507}" --encrypted-pin-block AC17DC148BDA645E`

```

```

        `{
 "VerificationKeyArn": "arn:aws:payment-cryptography:us-east-2::key/37y2tsl45p5zjbh2",
 "VerificationKeyCheckValue": "7F2363",
 "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2::key/ivi5ksfsuplneuyt",
 "EncryptionKeyCheckValue": "7CC9E2",

 }`

```
