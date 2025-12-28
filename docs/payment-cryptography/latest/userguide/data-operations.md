# Verify auth request (ARQC) cryptogram

The verify auth request cryptogram API is used for verifying [ARQC](terminology.md#terms.arqc "terminology.md#terms.arqc"). The
generation of the ARQC is outside of the scope of the AWS Payment Cryptography and is typically performed on an EMV Chip Card (or digital equivalent such as mobile wallet)
during transaction authorization time. An ARQC is unique to each transactions and is intended to cryptographically show both the validity of the card as well as to
ensure that the transaction data exactly matches the current (expected) transaction.

AWS Payment Cryptography provides a variety of options for validating ARQC and generating optional ARPC values including those defined
in [EMV 4.4 Book 2](https://www.emvco.com/specifications/?post_id=80377 "https://www.emvco.com/specifications/?post_id=80377")
and other schemes used by Visa and Mastercard. For a full list of all available options, please see the VerifyCardValidationData section in the
[API Guide](../DataAPIReference/API_VerifyCardValidationData.md "../DataAPIReference/API_VerifyCardValidationData.md").

ARQC cryptograms typically require the following inputs (although this may vary by implementation):

- [PAN](terminology.md#terms.pan "terminology.md#terms.pan") - Specified in the PrimaryAccountNumber field
- [PAN Sequence Number (PSN)](terminology.md#terms.psn "terminology.md#terms.psn") - specified in the PanSequenceNumber field
- Key Derivation Method such as Common Session Key (CSK) - Specified in the SessionKeyDerivationAttributes
- Master Key Derivation Mode (such as EMV Option A) - Specified in the MajorKeyDerivationMode
- Transaction data - a string of various transaction, terminal and card data such as Amount and Date - specified in the TransactionData field
- [Issuer Master Key](terminology.md#terms.imk "terminology.md#terms.imk") - the master key used to derive the cryptogram (AC) key used to protect individual transactions and specified in the KeyIdentifier field

###### Topics

- [Building transaction data](#w2aac15c25c13 "#w2aac15c25c13")
- [Transaction data padding](#w2aac15c25c15 "#w2aac15c25c15")
- [Examples](#w2aac15c25c17 "#w2aac15c25c17")

## Building transaction data

The exact content (and order) of the transaction data field varies by implementation and network scheme but the minimum recommended fields (and concatenation sequence) is defined in
[EMV 4.4 Book 2 Section 8.1.1 - Data Selection](https://www.emvco.com/specifications/?post_id=80377 "https://www.emvco.com/specifications/?post_id=80377"). If the first three fields are amount (17.00), other amount (0.00) and country of purchase,
that would result in the transaction data beginning as follows:

- 000000001700 - amount - 12 positions implied two digit decimal
- 000000000000 - other amount - 12 positions implied two digit decimal
- 0124 - four digit country code
- Output (partial) Transaction Data - 0000000017000000000000000124

## Transaction data padding

Transaction data should be padded prior to sending to the service. Most schemes use ISO 9797 Method 2 padding, where a hex string is
appended by hex 80 followed by 00 until the field is a multiple of the encryption block size; 8 bytes or 16 characters for TDES and 16 bytes or 32 characters for AES. The
alternative (method 1) is not as common but uses only 00 as the padding characters.

### ISO 9797 Method 1 Padding

Unpadded: 00000000170000000000000008400080008000084016051700000000093800000B03011203 (74 characters or 37 bytes)

Padded: 00000000170000000000000008400080008000084016051700000000093800000B03011203**000000** (80 characters or 40 bytes)

### ISO 9797 Method 2 Padding

Unpadded: 00000000170000000000000008400080008000084016051700000000093800000B1F220103000000 (80 characters or 40 bytes)

Padded: 00000000170000000000000008400080008000084016051700000000093800000B1F220103000000**8000000000000000** (88 characters or 44 bytes)

## Examples

### Visa CVN10

In this example, we will validate an ARQC generated using Visa CVN10.

If AWS Payment Cryptography is able to validate the ARQC, an http/200 is returned. If then ARCQ (Authorization Request Cryptogram) is not validated, it will return a http/400 response.

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

### Visa CVN18 and Visa CVN22

In this example, we will validate an ARQC generated using Visa CVN18 or CVN22. The cryptographic operations are the same between CVN18 and CVN22 but the data contained within transaction data varies. Compared to CVN10, a completely different cryptogram is generated even with the same inputs.

If AWS Payment Cryptography is able to validate the ARQC, an http/200 is returned. If the ARCQ is not validated, it will return an http/400.

```
`$` `aws payment-cryptography-data verify-auth-request-cryptogram \
--auth-request-cryptogram 61EDCC708B4C97B4
--key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk \
--major-key-derivation-mode EMV_OPTION_A
--transaction-data 00000000170000000000000008400080008000084016051700000000093800000B1F22010300000000000 \
00000000000000000000000000000000000000000008000000000000000
--session-key-derivation-attributes='{"EmvCommon":{"ApplicationTransactionCounter":"000B", \
"PanSequenceNumber":"01","PrimaryAccountNumber":"9137631040001422"}}'`

```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
 "KeyCheckValue": "08D7B4"
}`
```
