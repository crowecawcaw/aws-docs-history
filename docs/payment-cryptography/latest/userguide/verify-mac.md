# Verify MAC

Verify MAC API is used to verify MAC (Message Authentication Code) for card-related data authentication. It must use the same
encryption key used during generate MAC to re-produce MAC value for authentication.
The MAC encryption key can either be created with AWS Payment Cryptography by calling
[CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") or
imported by calling [ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md").
The API supports DUKPT MAC, HMAC and EMV MAC encryption keys for this operation.

If the value is verified, then response parameter `MacDataVerificationSuccessful` will return `Http/200`, otherwise `Http/400`
with a message indicating that `Mac verification failed`.

###### Examples

- [Verify HMAC](#verify-mac-hmac "#verify-mac-hmac")
- [Verify MAC using DUKPT CMAC](#verify-mac-dukpt-cmac "#verify-mac-dukpt-cmac")

## Verify HMAC

In this example, we will verify a HMAC (Hash-Based Message Authentication Code) for card data authentication using HMAC algorithm
`HMAC_SHA256` and HMAC encryption key. The key must have KeyUsage set to `TR31_M7_HMAC_KEY` and KeyModesOfUse `Verify` set to true.

```
`$` `aws payment-cryptography-data verify-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6 \
 --message-data "3b343038383439303031303733393431353d32343038323236303030373030303f33" \
 --mac ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C \
 --verification-attributes Algorithm=HMAC_SHA256`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6",
 "KeyCheckValue": "2976E7"
}`

```

## Verify MAC using DUKPT CMAC

In this example, we will verify a MAC using DUKPT (Derived Unique Key Per Transaction) with CMAC for card data authentication.
The key must have KeyUsage set to `TR31_B0_BASE_DERIVATION_KEY` and KeyModesOfUse `DeriveKey` set to true.
DUKPT keys derive a unique key for each transaction using a Base Derivation Key (BDK) and a Key Serial Number (KSN). The value of DukptKeyVariant
must match between sender and receiver. REQUEST will typically be used from terminal to backend, VERIFY from backend to terminal and BIDIRECTIONAL when a
single key is used in both directions.

```
`$` `aws payment-cryptography-data verify-mac \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
 --message-data "3b343038383439303031303733393431353d32343038323236303030373030303f33" \
 --mac D8E804EE74BF1D909A2C01C0BDE8EF34 \
 --verification-attributes DukptCmac='{"KeySerialNumber":"932A6E954ABB32DD00000001","DukptKeyVariant":"BIDIRECTIONAL"}'`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "C1EB8F"
}`

```
