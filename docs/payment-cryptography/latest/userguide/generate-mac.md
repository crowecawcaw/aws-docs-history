# Generate MAC

Generate MAC API is used to authenticate card-related data, such as track data from a card magnetic stripe,
by using known cryptographic keys to generate a MAC (Message Authentication Code) for data validation between sending and receiving parties.
The data used to generate MAC includes message data, secret MAC encryption key and MAC algorithm
to generate a unique MAC value for transmission. The receiving party of the MAC will use the same MAC message data,
MAC encryption key, and algorithm to reproduce another MAC value for comparison and data authentication.
Even if one character of the message changes or the MAC key used for verification is not identical,
the resulting MAC value is different. The API supports ISO 9797-1 Algorithm 1 and ISO 9797-1 Algorithm 3 MAC
(using a static MAC key and a derived DUKPT key), HMAC and EMV MAC encryption keys for this operation.

The input value for `message-data` must be hexBinary data.

For more information on all options for this API,
see [GenerateMac](../DataAPIReference/API_GenerateMac.md "../DataAPIReference/API_GenerateMac.md") and
[VerifyMac](../DataAPIReference/API_VerifyMac.md "../DataAPIReference/API_VerifyMac.md").

The optional parameter mac-length allows you to truncate the output value (although this can also be done within your code). A length of 8
refers to 8 bytes or 16 hex characters.

MAC keys can either be created with AWS Payment Cryptography
by calling [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
or imported by calling [ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md").

###### Note

CMAC and HMAC algorithms don't require padding. All others require that the data be padded to the block size of the algorithm,
which is multiples of 8 bytes (16 hex characters) for TDES and 16 bytes (32 hex characters) for AES.

###### Examples

- [Generate HMAC](#generate-mac-hmac "#generate-mac-hmac")
- [Generate MAC using ISO 9797-1 Algorithm 3](#generate-mac-iso9797-alg3 "#generate-mac-iso9797-alg3")
- [Generate MAC using CMAC](#generate-mac-cmac "#generate-mac-cmac")
- [Generate MAC using DUKPT CMAC](#generate-mac-dukpt-cmac "#generate-mac-dukpt-cmac")

## Generate HMAC

In this example, we will generate a HMAC (Hash-Based Message Authentication Code) for card data authentication using HMAC algorithm
`HMAC_SHA256` and HMAC encryption key. The key must have KeyUsage set to `TR31_M7_HMAC_KEY`
and KeyModesOfUse to `Generate`. The hash length (e.g. 256) is defined when the key is created and cannot be modified.

The optional mac-length parameter will trim the output MAC, although this can be performed outside the service as well. This value
is in bytes, so a value of 16 will expect a hex string of length 32.

```
`$` `aws payment-cryptography-data generate-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6 \
 --message-data "3b313038383439303031303733393431353d32343038323236303030373030303f33" \
 --generation-attributes Algorithm=HMAC`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6",
 "KeyCheckValue": "2976E7",
 "Mac": "ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C"
}`

```

## Generate MAC using ISO 9797-1 Algorithm 3

In this example, we will generate a MAC using ISO 9797-1 Algorithm 3 (Retail MAC) for card data authentication.
The key must have KeyUsage set to `TR31_M3_ISO_9797_3_MAC_KEY` and KeyModesOfUse to `Generate`.

```
`$` `aws payment-cryptography-data generate-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h \
 --message-data "3b313038383439303031303733393431353d32343038323236303030373030303f33" \
 --generation-attributes="Algorithm=ISO9797_ALGORITHM3"`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h",
 "KeyCheckValue": "2976EA",
 "Mac": "A8F7A73DAF87B6D0"
}`

```

## Generate MAC using CMAC

CMAC is most commonly used when the keys are AES but it also supports TDES.
In this example, we will generate a MAC using CMAC (ISO 9797-1 Algorithm 5) for card data authentication with an AES key.
The key must have KeyUsage set to `TR31_M6_ISO_9797_5_CMAC_KEY` and KeyModesOfUse to `Generate`.

```
`$` `aws payment-cryptography-data generate-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
 --message-data "3b313038383439303031303733393431353d32343038323236303030373030303f33" \
 --generation-attributes Algorithm="CMAC"`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "C1EB8F",
 "Mac": "1F8C36E63F91E4E93DF7842BF5E2E5F7"
}`

```

## Generate MAC using DUKPT CMAC

In this example, we will generate a MAC using DUKPT (Derived Unique Key Per Transaction) with CMAC for card data authentication.
The key must have KeyUsage set to `TR31_B0_BASE_DERIVATION_KEY` and KeyModesOfUse `DeriveKey` set to true.
DUKPT keys derive a unique key for each transaction using a Base Derivation Key (BDK) and a Key Serial Number (KSN).

```
`$` `aws payment-cryptography-data generate-mac --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6 --message-data "3b313038383439303031303733393431353d32343038323236303030373030303f33" --generation-attributes="DukptCmac={KeySerialNumber="932A6E954ABB32DD00000001",Direction=BIDIRECTIONAL}"`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6",
 "KeyCheckValue": "C1EB8F"
}`

```
