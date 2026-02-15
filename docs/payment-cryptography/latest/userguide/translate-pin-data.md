# Translate PIN data

Translate PIN data functions are used for translating encrypted PIN data from one set of keys to another
without the encrypted data leaving the HSM. It is used for P2PE encryption where the
working keys should change but the processing system either doesn't need to, or is not permitted to, decrypt the data.
The primary inputs are the encrypted data, the encryption key used to encrypt the data,
the parameters used to generate the input values. The other set of inputs are the requested output parameters
such as the key to be used to encrypt the output and the parameters used to create that output.
The primary outputs are a newly encrypted dataset as well as the parameters used to generate it.

###### Note

For PCI compliance, the incoming and outgoing PrimaryAccountNumber values must match. Translating a PIN from one PAN to another is not permitted.

###### Topics

- [PIN from PEK to DUKPT](#crypto-ops-pindata.pektodukpt "#crypto-ops-pindata.pektodukpt")
- [PIN from PEK to PEK](#crypto-ops-pindata.pektopek "#crypto-ops-pindata.pektopek")

## PIN from PEK to DUKPT

###### Example

In this example, we will translate a PIN from an AES ISO 4 PIN Block using the [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") to PEK TDES encryption using ISO 0 PIN block.
This is common where a payment terminal encrypts a pin in ISO 4 and then it may be translated back to TDES for downstream processing if the next connection
doesn't yet support AES.

```
`$` `aws payment-cryptography-data translate-pin-data --encrypted-pin-block "AC17DC148BDA645E" --outgoing-translation-attributes=IsoFormat0='{PrimaryAccountNumber=171234567890123}' --outgoing-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/4pmyquwjs3yj4vwe --incoming-translation-attributes IsoFormat4="{PrimaryAccountNumber=171234567890123}" --incoming-dukpt-attributes KeySerialNumber="FFFF9876543210E00008"`

```

```

    `{
 "PinBlock": "1F4209C670E49F83E75CC72E81B787D9",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
 "KeyCheckValue": "7CC9E2"
 }`

```

## PIN from PEK to PEK

###### Example

In this example, we translate a PIN encrypted under one PEK (PIN Encryption Key) to another PEK.
This is commonly used when routing transactions between different systems or partners that
use different encryption keys, while maintaining PCI PIN compliance by keeping the
PIN encrypted throughout the process. Both keys use TDES 3KEY encryption in this example,
but a variety of options are available including AES ISO-4 to TDES ISO-0, DUKPT to PEK, or AS2805 to PEK.

```
`$` `aws payment-cryptography-data translate-pin-data --encrypted-pin-block "AC17DC148BDA645E" \
 --incoming-translation-attributes IsoFormat0='{PrimaryAccountNumber=171234567890123}' \
 --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
 --outgoing-translation-attributes IsoFormat0='{PrimaryAccountNumber=171234567890123}' \
 --outgoing-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh`
```

```
`{
 "PinBlock": "E8F2A6C4D1B93E7F",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh",
 "KeyCheckValue": "9A325B"
}`
```

The output PIN block is now encrypted under the second PEK and can be safely transmitted to the downstream system that holds the corresponding key.
