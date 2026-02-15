# Generate CVV2

###### Example

In this example, we will generate a CVV2 for a given PAN with
inputs of `PAN` and card expiration date. This assumes that you have a
card verification key [generated](create-keys.md#cvvkey-example "create-keys.md#cvvkey-example").

```
`$` `aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --primary-account-number=171234567890123 --generation-attributes CardVerificationValue2={CardExpiryDate=0123}`

```

```

  `{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "CADDA1",
 "ValidationData": "801"
 }`

```
