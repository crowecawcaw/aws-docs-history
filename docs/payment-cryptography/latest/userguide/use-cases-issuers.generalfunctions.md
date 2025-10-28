# Verify an EMV ARQC and generate an ARPC

[ARQC](terminology.md#terms.arqc "terminology.md#terms.arqc") (Authorization Request Cryptogram) is a cryptogram generated
by an EMV (chip) card and used to validate the transaction details as well as the use of an authorized card. It incorporates data from the card, terminal and the transaction itself.

At validation time on the backend, the same inputs are provided to AWS Payment Cryptography, the cryptogram is internally re-created and this is compared against the value provided with the transaction.
In this sense, it is similar to a MAC. [EMV 4.4 Book 2](https://www.emvco.com/specifications/?post_id=80377 "https://www.emvco.com/specifications/?post_id=80377") defines three aspects of this function -
key derivation methods (known as common session key - CSK) to generate one-time transaction keys, a minimum payload and methods for generating a response (ARPC).

Individual card schemes may specify additional transactional fields to incorporate or the order those fields appear. Other (generally deprecated) scheme specific derivation schemes exist as well
and are covered elsewhere in this documentation.

For more information, see [VerifyCardValidationData](../DataAPIReference/API_VerifyCardValidationData.md "../DataAPIReference/API_VerifyCardValidationData.md") in the API guide.

## Create the key

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{DeriveKey=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CVN18"},{"Key":"CARD_BIN","Value":"12345678"}]'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2::key/pw3s6nl62t5ushfk",
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

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2::key/pw3s6nl62t5ushfk_. You need that in the next step.

## Generate an ARQC

The ARQC is generated exclusively by an EMV card. As such, AWS Payment Cryptography has no facility for generating such a payload. For test purposes, a
number of libraries are available online that can generate an appropriate payload as well as known values that are generally provided by the various schemes.

## Validate an ARQC

If AWS Payment Cryptography is able to validate the ARQC, an http/200 is returned. An ARPC (response) can optionally be provided and in included in the response after the ARQC is validated.

```
`$` `aws payment-cryptography-data verify-auth-request-cryptogram --auth-request-cryptogram 61EDCC708B4C97B4 --key-identifier arn:aws:payment-cryptography:us-east-2::key/pw3s6nl62t5ushfk --major-key-derivation-mode EMV_OPTION_A --transaction-data 00000000170000000000000008400080008000084016051700000000093800000B1F2201030000000000000000000000000000000000000000000000000000008000000000000000 --session-key-derivation-attributes='{"EmvCommon":{"ApplicationTransactionCounter":"000B", "PanSequenceNumber":"01","PrimaryAccountNumber":"9137631040001422"}}' --auth-response-attributes='{"ArpcMethod2":{"CardStatusUpdate":"12345678"}}'`
```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2::key/pw3s6nl62t5ushfk",
 "KeyCheckValue": "08D7B4",
 "AuthResponseValue":"2263AC85"
}`
```
