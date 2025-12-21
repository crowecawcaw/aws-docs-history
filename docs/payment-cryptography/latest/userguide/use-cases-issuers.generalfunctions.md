# Generate and Verify an EMV MAC

EMV MAC is MAC using an input of an EMV derived key and then performing a ISO9797-3 (Retail) MAC over the resulting data. EMV MAC is typically used to send commands
to an EMV card such as unblock scripts.

###### Note

AWS Payment Cryptography does not validate the contents of the script. Please consult your scheme or card manual for details on specific commands to include.

For more information, see [MacAlgorithmEmv](../DataAPIReference/API_MacAlgorithmEmv.md "../DataAPIReference/API_MacAlgorithmEmv.md") in the API guide.

###### Topics

- [Create the key](#use-cases-issuers.generalfunctions.emvmac.setup "#use-cases-issuers.generalfunctions.emvmac.setup")
- [Generate an EMV MAC](#use-cases-issuers.generalfunctions.emvmac.generate "#use-cases-issuers.generalfunctions.emvmac.generate")

## Create the key

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_E2_EMV_MKEY_INTEGRITY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{DeriveKey=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CVN18"},{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
 "KeyAttributes": {
 "KeyUsage": "TR31_E2_EMV_MKEY_INTEGRITY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "TDES_2KEY",
 "KeyModesOfUse": {
 "Encrypt": false,
 "Decrypt": false,
 "Wrap": false,
 "Unwrap": false,
 "Generate": false,
 "Sign": false,
 "Verify": false,
 "DeriveKey": true,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "08D7B4",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2024-03-07T06:41:46.648000-07:00",
 "UsageStartTimestamp": "2024-03-07T06:41:46.626000-07:00"
 }
 }`
```

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk_. You need that in the next step.

## Generate an EMV MAC

The typical flow is that a backend process will generate an EMV script (such as card unblock), sign it using this command (which derives a one-time key specific to one particular card)
and then return the MAC. Then the command + MAC are sent to the card to be applied. Sending the command to the card is outside the scope of AWS Payment Cryptography.

###### Note

This command is meant for commands when no encrypted data (such as PIN) is sent. EMV Encrypt can be combined with this command to append encrypted data to the issuer script prior to calling this command

Message Data
Message data includes the APDU header and command. While this can vary by implementation, this example is the APDU header for unblock (84 24 00 00 08), following
by ATC (0007) and then ARQC of the previous transaction (999E57FD0F47CACE). The service does not validate the contents of this field.

Session Key Derivation Mode
This field defines how the session key is generated. EMV_COMMON_SESSION_KEY is generally used for the new implementations,
while EMV2000 | AMEX | MASTERCARD_SESSION_KEY | VISA may be used as well.

MajorKeyDerivationMode
EMV Defines Mode A, B or C. Mode A is the most common and AWS Payment Cryptography currently supports mode A or mode B.

PAN
The account number, typically available in chip field 5A or ISO8583 field 2 but may also be retrieved from the card system.

PSN
The card sequence number. If not used, enter 00.

SessionKeyDerivationValue
This is the per session derivation data. It can either be the last ARQC(ApplicationCryptogram) from field 9F26
or the last ATC from 9F36 depending on the derivation scheme.

Padding
Padding is automatically applied and uses ISO/IEC 9797-1 padding method 2.

```
`$` `aws payment-cryptography-data generate-mac --message-data 84240000080007999E57FD0F47CACE --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk --message-data 8424000008999E57FD0F47CACE0007 --generation-attributes EmvMac="{MajorKeyDerivationMode=EMV_OPTION_A,PanSequenceNumber='00',PrimaryAccountNumber='2235521304123282',SessionKeyDerivationMode=EMV_COMMON_SESSION_KEY,SessionKeyDerivationValue={ApplicationCryptogram='999E57FD0F47CACE'}}"`
```

```
`{
"KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
"KeyCheckValue": "08D7B4",
"Mac":"5652EEDF83EA0D84"
}`
```
