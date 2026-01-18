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

## Validate encrypted PIN using PVV method - error bad pin

In this example, we will attempt to validate a PIN for a given PAN but it will fail due to the pin being incorrect.

When using SDKs, this appears as {"Message":"Pin block verification failed.","Reason":"INVALID_PIN"}

```
`$` `aws payment-cryptography-data verify-pin-data --verification-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --verification-attributes VisaPin="{PinVerificationKeyIndex=1,VerificationValue=9999}" --encrypted-pin-block AC17DC148BDA645E`

```

```

        `An error occurred (VerificationFailedException) when calling the VerifyPinData operation: Pin block verification failed.`

```

## Validate encrypted PIN using PVV method - error bad inputs

In this example, we will attempt to validate a PIN for a given PAN but it will fail due to bad inputs and the incoming
data was not a valid pin. Common causes are: 1/wrong key being used
2/input parameters such as pan or pin block format are incorrect 3/pin block is corrupted.

```
`$` `aws payment-cryptography-data verify-pin-data --verification-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 --encryption-key-identifier --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --verification-attributes VisaPin="{PinVerificationKeyIndex=1,VerificationValue=9999}" --encrypted-pin-block AC17DC148BDA645E`

```

```

        `An error occurred (ValidationException) when calling the VerifyPinData operation: Pin block provided is invalid. Please check your input to ensure all field values are correct.`

```
