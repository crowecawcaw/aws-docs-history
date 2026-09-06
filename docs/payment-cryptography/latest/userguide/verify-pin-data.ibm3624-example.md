

# Validate a PIN against previously stored IBM3624 pin offset
<a name="verify-pin-data.ibm3624-example"></a>

In this example, you validate a cardholder-provided PIN against the pin offset stored on file with the card issuer or processor. The inputs include the verification key (PVK), the encryption key (PEK), the primary account number, the encrypted PIN block from the payment terminal (or other upstream provider such as a card network), and the previously stored pin offset. If the PIN matches, the API returns an HTTP/200 response. 

 This command requires that the pin verification key is of type `TR31_V1_IBM3624_PIN_VERIFICATION_KEY` and the encryption key is of type `TR31_P0_PIN_ENCRYPTION_KEY`. 

**PIN length validation**  
The optional `--pin-data-length` parameter specifies the length of the PIN being verified (4 to 12 digits). If you do not specify this parameter, the service validates the entire PIN length that the offset value protects. If you want to validate only a part of the PIN, use the `--pin-data-length` parameter. For example, if `--pin-data-length` is set to 4 but the actual PIN is 6 digits, the service validates only the rightmost 4 digits. The remaining 2 digits are not checked. You might do this intentionally if the cardholder PIN is 6 digits but the incoming PIN is only 4 digits, such as when the incoming network or merchant only supports a 4-digit PIN.

**Example**  

```
$ aws payment-cryptography-data verify-pin-data \
    --verification-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 \
    --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --primary-account-number 171234567890123 \
    --pin-block-format ISO_FORMAT_0 \
    --encrypted-pin-block AC17DC148BDA645E \
    --pin-data-length 4 \
    --verification-attributes Ibm3624PinOffset="{DecimalizationTable=9876543210654321,PinValidationDataPadCharacter=D,PinValidationData=171234567890123,PinOffset=5507}"
```

```
{
    "VerificationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2",
    "VerificationKeyCheckValue": "7F2363",
    "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
    "EncryptionKeyCheckValue": "7CC9E2"
}
```