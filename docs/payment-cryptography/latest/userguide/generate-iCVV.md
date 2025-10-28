# Generate iCVV

In this example, we will generate a [iCVV](terminology.md#terms.icvv "terminology.md#terms.icvv") for a given PAN with
inputs of `PAN`,a service code of 999 and card expiration date. This assumes that you have a
card verification key [generated](create-keys.md#cvvkey-example "create-keys.md#cvvkey-example").

For all available parameters see [CardVerificationValue1](../DataAPIReference/API_CardVerificationValue1.md "../DataAPIReference/API_CardVerificationValue1.md") in the API reference guide.

```
`$` `aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2::key/tqv5yij6wtxx64pi --primary-account-number=171234567890123 --generation-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=999}'`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2::key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "CADDA1",
 "ValidationData": "801"
}`

```
