# Using Dynamic Keys

Dynamic Keys allows one-time or limited use keys to be used for cryptographic operations like `EncryptData`.
This flow can be utilized when the key material frequently rotates (such as on every card transaction) and there is a desire to avoid importing the key material into the service.
Short-lived keys may be utilized as part of [softPOS/Mpoc](terminology.md#terms.mpoc "terminology.md#terms.mpoc") or other solutions.

###### Note

This can be used in lieu of the typical flow using AWS Payment Cryptography, where cryptographic keys are either created or imported into the service and keys are specified using a key alias
or key arn.

The following operations support Dynamic Keys:

- EncryptData
- DecryptData
- ReEncryptData
- TranslatePin

## Decrypting Data

The following example shows using Dynamic Keys along with the decrypt command. The key identifier in this case is the wrapping key (KEK) that secures the decryption key
(that is provided in the wrapped-key parameter in TR-31 format). The wrapped key shall be key purpose of D0 to be used with decrypt command along with a mode of use of B or D.

```
`$` `aws payment-cryptography-data decrypt-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza --cipher-text 1234123412341234123412341234123A --decryption-attributes 'Symmetric={Mode=CBC,InitializationVector=1234123412341234}' --wrapped-key WrappedKeyMaterial={"Tr31KeyBlock"="D0112D0TN00E0000B05A6E82D7FC68B95C84306634B0000DA4701BE9BCA318B3A30A400B059FD4A8DE19924A9D3EE459F24FDE680F8E4A40"}`

```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza",
 "KeyCheckValue": "0A3674",
 "PlainText": "2E138A746A0032023BEF5B85BA5060BA"
}`

```

## Translating a pin

The following example shows using Dynamic Keys along with the translate pin command to translate from a dynamic key to a semi-static acquirer working key (AWK).
The incoming key identifier in this case is the wrapping key (KEK) that is protecting the dynamic pin encryption key (PEK) that is provided in the TR-31 format.
The wrapped key shall be key purpose of `P0` along with a mode of use of B or D. The outgoing key identifier is a key of type
`TR31_P0_PIN_ENCRYPTION_KEY` and a mode of use of Encrypt=true,Wrap=true

```
`$` `aws payment-cryptography-data translate-pin-data --encrypted-pin-block "C7005A4C0FA23E02" --incoming-translation-attributes=IsoFormat0='{PrimaryAccountNumber=171234567890123}' --incoming-key-identifier alias/PARTNER1_KEK --outgoing-key-identifier alias/ACQUIRER_AWK_PEK --outgoing-translation-attributes IsoFormat0="{PrimaryAccountNumber=171234567890123}" --incoming-wrapped-key WrappedKeyMaterial={"Tr31KeyBlock"="D0112P0TB00S0000EB5D8E63076313162B04245C8CE351C956EA4A16CC32EB3FB61DE3FC75C751734B773F5B645943A854C65740738B8304"}`
```

```
`{
 "PinBlock": "2E66192BDA390C6F",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza",
 "KeyCheckValue": "0A3674"
}`
```
