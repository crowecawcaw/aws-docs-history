# Generate IBM3624 pin offset for a pin

IBM 3624 PIN Offset also sometimes called the IBM method. This method generates a natural/intermediate PIN using the validation data (typically the PAN)
and a PIN Key (PVK). Natural pins are effectively a derived value and being deterministic are very efficient to handle for an issuer because no pin data needs to be stored at a cardholder level.
The most obvious con is that this scheme doesn't account for cardholder selectable or random pins. To allow for those types of pins,
an offset algorithm was added to the scheme. The offset represents the difference between the user selected(or random) pin and the natural key. The offset value is stored
by the card issuer or card processor. At transaction time,
the AWS Payment Cryptography service internally recalculates the natural pin and applies the offset to find the pin. It then compares this against the value provided by the transaction authorization.

Several options exist for IBM3624:

- `Ibm3624NaturalPin` will output the natural pin and an encrypted pin block
- `Ibm3624PinFromOffset` will generate an encrypted pin block given an offset
- `Ibm3624RandomPin` will generate a random pin and then the
  matching offset and encrypted pin block.
- `Ibm3624PinOffset` generates the pin offset given a user selected pin.
  Internal to AWS Payment Cryptography, the following steps are performed:

- Pad the provided pan to 16 characters. If <16 are provided, pad on the
  right hand side using the provided padding character.
- Encrypts the validation data using the PIN generation key.
- Decimalize the encrypted data using the decimalization table. This maps
  hexidecimal digits to decimal digits for instance 'A' may map to 9 and 1 may
  map to 1.
- Get the first 4 digits from a hexidecimal representation of the output.
  This is the natural pin.
- If a user selected or random pin was generated, modulo subtract the
  natural pin with customer pin. The result is the pin offset.

###### Examples

- [Example: Generate IBM3624 pin offset for a pin](#generate-ibm3624-random-example "#generate-ibm3624-random-example")

## Example: Generate IBM3624 pin offset for a pin

In this example, we will generate a new (random) pin
where the outputs will be an encrypted `PIN block` (PinData.PinBlock) and an `IBM3624` offset value (pinData.Offset). The inputs are
`PAN`, validation data (typically the pan), padding character, the `Pin Verification Key`,
the `Pin Encryption Key` and the `PIN block format`.

This command requires that the pin generation key is of type `TR31_V1_IBM3624_PIN_VERIFICATION_KEY` and the encryption key is of type `TR31_P0_PIN_ENCRYPTION_KEY`

The following example shows generating a random pin then outputting the encrypted pin block and IBM3624 offset value using Ibm3624RandomPin

```
`$` `aws payment-cryptography-data generate-pin-data --generation-key-identifier arn:aws:payment-cryptography:us-east-2::key/37y2tsl45p5zjbh2 --encryption-key-identifier arn:aws:payment-cryptography:us-east-2::key/ivi5ksfsuplneuyt --primary-account-number 171234567890123 --pin-block-format ISO_FORMAT_0 --generation-attributes Ibm3624RandomPin="{DecimalizationTable=9876543210654321,PinValidationDataPadCharacter=D,PinValidationData=171234567890123}"`
```

```
`{
 "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2::key/37y2tsl45p5zjbh2",
 "GenerationKeyCheckValue": "7F2363",
 "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2::key/ivi5ksfsuplneuyt",
 "EncryptionKeyCheckValue": "7CC9E2",
 "EncryptedPinBlock": "AC17DC148BDA645E",
 "PinData": {
 "PinOffset": "5507"
 }
 }`
```
