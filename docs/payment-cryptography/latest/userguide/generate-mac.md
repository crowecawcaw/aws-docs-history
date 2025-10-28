# Generate MAC

Generate MAC API is used to authenticate card-related data, such as track data from a card magnetic stripe,
by using known data values to generate a MAC (Message Authentication Code) for data validation between sending and receiving parties.
The data used to generate MAC includes message data, secret MAC encryption key and MAC algorithm
to generate a unique MAC value for transmission. The receiving party of the MAC will use the same MAC message data,
MAC encryption key, and algorithm to reproduce another MAC value for comparison and data authentication.
Even if one character of the message changes or the MAC key used for verification is not identical,
the resulting MAC value is different. The API supports DUPKT MAC, HMAC and EMV MAC encryption keys for this operation.

The input value for `message-data` must be hexBinary data.

In this example, we will generate a HMAC (Hash-Based Message Authentication Code) for card data authentication using HMAC algorithm
`HMAC_SHA256` and HMAC encryption key. The key must have KeyUsage set to `TR31_M7_HMAC_KEY`
and KeyModesOfUse to `Generate`. The MAC key can either be created with AWS Payment Cryptography
by calling [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
or imported by calling [ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md").

```
`$` `aws payment-cryptography-data generate-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2::key/qnobl5lghrzunce6 \
 --message-data "3b313038383439303031303733393431353d32343038323236303030373030303f33" \
 --generation-attributes Algorithm=HMAC_SHA256`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2::key/qnobl5lghrzunce6,
 "KeyCheckValue": "2976E7",
 "Mac": "ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C"
}`

```
