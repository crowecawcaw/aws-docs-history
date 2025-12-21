# Translate PIN data

Translate PIN data functions are used for translating encrypted PIN data from one set of keys to another
without the encrypted data leaving the HSM. It is used for P2PE encryption where the
working keys should change but the processing system either doesn't need to, or is not permitted to, decrypt the data.
The primary inputs are the encrypted data, the encryption key used to encrypt the data,
the parameters used to generate the input values. The other set of inputs are the requested output parameters
such as the key to be used to encrypt the output and the parameters used to create that output.
The primary outputs are a newly encrypted dataset as well as the parameters used to generate it.

###### Note

AES key types only support ISO Format 4 [pin blocks](terminology.md#terms.pinblock "terminology.md#terms.pinblock").

###### Topics

- [PIN from PEK to DUKPT](#crypto-ops-pindata.pektodukpt "#crypto-ops-pindata.pektodukpt")
- [PIN from DUKPT to AWK](#w2aac15c22c11c11 "#w2aac15c22c11c11")

## PIN from PEK to DUKPT

In this example, we will translate a PIN from PEK TDES encryption using ISO 0 PIN block to an AES ISO 4 PIN Block using the [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") algorithm.
Typically this might be done in reverse, where a payment terminal encrypts a pin in ISO 4 and then it may be translated back to TDES for downstream processing.

```
`$` `aws payment-cryptography-data translate-pin-data --encrypted-pin-block "AC17DC148BDA645E" --incoming-translation-attributes=IsoFormat0='{PrimaryAccountNumber=171234567890123}' --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --outgoing-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/4pmyquwjs3yj4vwe --outgoing-translation-attributes IsoFormat4="{PrimaryAccountNumber=171234567890123}" --outgoing-dukpt-attributes KeySerialNumber="FFFF9876543210E00008"`

```

```

    `{
 "PinBlock": "1F4209C670E49F83E75CC72E81B787D9",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
 "KeyCheckValue": "7CC9E2"
 }`

```

## PIN from DUKPT to AWK

In this example, we will translate a PIN from an AES [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") encrypted PIN to a pin encrypted
under a [AWK](terminology.md#terms.awk "terminology.md#terms.awk"). It is functionally the inverse of the previous example.

```
`$` `aws payment-cryptography-data translate-pin-data --encrypted-pin-block "1F4209C670E49F83E75CC72E81B787D9" --outgoing-translation-attributes=IsoFormat0='{PrimaryAccountNumber=171234567890123}' --outgoing-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/4pmyquwjs3yj4vwe --incoming-translation-attributes IsoFormat4="{PrimaryAccountNumber=171234567890123}" --incoming-dukpt-attributes KeySerialNumber="FFFF9876543210E00008"`
```

```

    `{
 "PinBlock": "AC17DC148BDA645E",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
 "KeyCheckValue": "FE23D3"
 }`

```
