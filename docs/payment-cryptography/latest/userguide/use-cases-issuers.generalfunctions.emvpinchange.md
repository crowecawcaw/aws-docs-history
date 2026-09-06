

# Generate EMV MAC for PIN Change
<a name="use-cases-issuers.generalfunctions.emvpinchange"></a>

EMV PIN change combines two operations: generating a MAC for an issuer script and encrypting a new PIN for offline PIN change on an EMV chip card. This command is only needed in certain countries where the pin is stored on the chip card (this is common for European countries). This is commonly used when a cardholder needs to change their PIN and the new PIN must be securely transmitted to the card along with a MAC to verify the command's authenticity. 

**Note**  
 If you only need to send commands to the card but not change the PIN, consider using [ARPC CSU](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyAuthRequestCryptogram.html) or [Generate EMV MAC](use-cases-issuers.generalfunctions.emvmac.md) commands instead. 

For more information, see [GenerateMacEmvPinChange](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMacEmvPinChange.html) in the API guide.

## Generate EMV MAC and encrypted PIN for PIN change
<a name="use-cases-issuers.generalfunctions.emvpinchange.generate"></a>

This operation requires two keys: an EMV integrity key (KeyUsage: TR31\_E2\_EMV\_MKEY\_INTEGRITY) for MAC generation and an EMV confidentiality key (KeyUsage: TR31\_E4\_EMV\_MKEY\_CONFIDENTIALITY) for PIN encryption. The typical flow is that a backend process will generate an EMV PIN change script, which includes both the MAC for the issuer script and the encrypted new PIN. The command and encrypted PIN are then sent to the card to update the offline PIN. Sending the command to the card is outside the scope of AWS Payment Cryptography. 

Message Data  
Message data includes the APDU command for the issuer script. The service does not validate the contents of this field.

New Encrypted PIN Block  
The new encrypted PIN block that will be sent to the card. This must be provided as an encrypted value using a PIN encryption key.

New PIN PEK Identifier  
The key used to encrypt the new PIN before it's passed to this API.

Secure Messaging Integrity Key  
The EMV integrity key (KeyUsage: TR31\_E2\_EMV\_MKEY\_INTEGRITY) used for MAC generation.

Secure Messaging Confidentiality Key  
The EMV confidentiality key (KeyUsage: TR31\_E4\_EMV\_MKEY\_CONFIDENTIALITY) used for PIN encryption.

MajorKeyDerivationMode  
EMV defines Mode A, B, or C. Mode A is the most common and AWS Payment Cryptography currently supports mode A or mode B.

Mode  
The encryption mode, typically CBC for PIN change operations.

PAN  
The account number, typically available in chip field 5A or ISO8583 field 2 but may also be retrieved from the card system.

PanSequenceNumber  
The card sequence number. If not used, enter 00.

ApplicationCryptogram  
This is the per session derivation data, typically the last ARQC from field 9F26.

PinBlockLengthPosition  
Specifies where the PIN block length is encoded. Typically set to NONE. Check your card scheme specifications if you're not sure.

PinBlockPaddingType  
Specifies the padding type for the PIN block. Typically set to NO\_PADDING. Check your card scheme specifications if you're not sure.

**Example**  

```
$ aws payment-cryptography-data generate-mac-emv-pin-change \
    --message-data 00A4040008A000000004101080D80500000001010A04000000000000 \
    --new-encrypted-pin-block 67FB27C75580EFE7 \
    --new-pin-pek-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --pin-block-format ISO_FORMAT_0 \
    --secure-messaging-confidentiality-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
    --secure-messaging-integrity-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk \
    --derivation-method-attributes 'EmvCommon={ApplicationCryptogram=1234567890123457,MajorKeyDerivationMode=EMV_OPTION_A,Mode=CBC,PanSequenceNumber=00,PinBlockLengthPosition=NONE,PinBlockPaddingType=NO_PADDING,PrimaryAccountNumber=171234567890123}'
```

```
{
    "SecureMessagingIntegrityKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
    "SecureMessagingIntegrityKeyCheckValue": "08D7B4",
    "SecureMessagingConfidentialityKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
    "SecureMessagingConfidentialityKeyCheckValue": "C1EB8F",
    "Mac": "5652EEDF83EA0D84",
    "EncryptedPinBlock": "F1A2B3C4D5E6F7A8"
}
```