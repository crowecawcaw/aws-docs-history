# Verify CVV2

###### Example

In this example, we will validate a CVV/CVV2 for a given PAN. The CVV2 is typically provided by the
cardholder or user during transaction time for validation. In order to validate their input, the
following values will be provided at runtime -
[Key to Use for validation (CVK)](create-keys.md#cvvkey-example "create-keys.md#cvvkey-example"),
`PAN`, card expiration date and CVV2 entered.
Card expiration format must match that used in initial value generation.

For all available parameters see [CardVerificationValue2](../DataAPIReference/API_CardVerificationValue2.md "../DataAPIReference/API_CardVerificationValue2.md") in the API reference guide.

```
`$` `aws payment-cryptography-data verify-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --primary-account-number=171234567890123 --verification-attributes CardVerificationValue2={CardExpiryDate=0123} --validation-data 801`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "CADDA1"
 }`

```
