# JCB specific functions

###### Topics

- [ARQC - CVN04](#use-cases-issuers.networkfunctions.jcb.cvn04 "#use-cases-issuers.networkfunctions.jcb.cvn04")
- [ARQC - CVN01](#use-cases-issuers.networkfunctions.visa.cvn01 "#use-cases-issuers.networkfunctions.visa.cvn01")

## ARQC - CVN04

JCB CVN04 utilizes the [CSK method](use-cases-issuers.generalfunctions.md "use-cases-issuers.generalfunctions.md") of key derivation. Please see the scheme documentation for details on
constructing the transaction data field.

## ARQC - CVN01

CVN01 is an older JCB method for EMV transactions that uses per card key derivation rather than session (per transaction) derivation and also uses a different payload. This
message is also used by Visa hence the element name has that name even though it's also used for JCB. For information on the payload contents, please contact the scheme documentation.

### Create key

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{DeriveKey=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CVN10"},{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
 "KeyAttributes": {
 "KeyUsage": "TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS",
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

### Validate the ARQC

In this example, we will validate an ARQC generated using JCB CVN01. This uses the same options as the Visa method, hence the name of the parameter.

If AWS Payment Cryptography is able to validate the ARQC, an http/200 is returned. If the arqc is not validated, it will return a http/400 response.

```
`$` `aws payment-cryptography-data verify-auth-request-cryptogram --auth-request-cryptogram D791093C8A921769 \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk \
 --major-key-derivation-mode EMV_OPTION_A \
 --transaction-data 00000000170000000000000008400080008000084016051700000000093800000B03011203000000 \
 --session-key-derivation-attributes='{"Visa":{"PanSequenceNumber":"01" \
 ,"PrimaryAccountNumber":"9137631040001422"}}'`
```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
 "KeyCheckValue": "08D7B4"
 }`
```
