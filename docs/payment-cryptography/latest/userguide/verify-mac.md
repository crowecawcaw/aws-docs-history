# Verify MAC

Verify MAC API is used to verify MAC (Message Authentication Code) for card-related data authentication. It must use the same
encryption key used during generate MAC to re-produce MAC value for authentication.
The MAC encryption key can either be created with AWS Payment Cryptography by calling
[CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") or
imported by calling [ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md").
The API supports DUPKT MAC, HMAC and EMV MAC encryption keys for this operation.

If the value is verified, then response parameter `MacDataVerificationSuccessful` will return `Http/200`, otherwise `Http/400`
with a message indicating that `Mac verification failed`.

In this example, we will verify a HMAC (Hash-Based Message Authentication Code) for card data authentication using HMAC algorithm
`HMAC_SHA256` and HMAC encryption key. The key must have KeyUsage set to `TR31_M7_HMAC_KEY` and KeyModesOfUse to `Verify`.

```
`$` `aws payment-cryptography-data verify-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2::key/qnobl5lghrzunce6 \
 --message-data "3b343038383439303031303733393431353d32343038323236303030373030303f33" \
 --verification-attributes='Algorithm=HMAC_SHA256' \
 --mac ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2::key/qnobl5lghrzunce6,
 "KeyCheckValue": "2976E7",
}`

```
