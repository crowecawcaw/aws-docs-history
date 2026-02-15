# Verify iCVV

###### Example

In this example, we will verify a [iCVV](terminology.md#terms.icvv "terminology.md#terms.icvv") for a given PAN with
inputs of [Key to Use for validation (CVK)](create-keys.md#cvvkey-example "create-keys.md#cvvkey-example"), `PAN`,
a service code of 999, card expiration date and the iCVV provided by the transaction to validate.

iCVV is not a user entered value (like CVV2) but embedded on an EMV card.
Consideration should be given to whether it should always validate when provided.

For all available parameters see, [CardVerificationValue1](../DataAPIReference/API_CardVerificationValue1.md "../DataAPIReference/API_CardVerificationValue1.md") in the API reference guide.

```
`$` `aws payment-cryptography-data verify-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --primary-account-number=171234567890123 --verification-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=999} --validation-data 801`

```

```

`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "CADDA1",
 "ValidationData": "801"
}`

```
