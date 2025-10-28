# Using aliases in your applications

You can use an alias to represent an AWS Payment Cryptography key in your application code. The
`key-identifier` parameter in AWS Payment Cryptography [data
operations](data-operations.md "data-operations.md") as well as other operations like List Keys accepts an alias name or alias ARN.

```
`$` `aws payment-cryptography-data generate-card-validation-data --key-identifier alias/BIN_123456_CVK --primary-account-number=171234567890123 --generation-attributes CardVerificationValue2={CardExpiryDate=0123}`
```

When using an alias ARN, remember that the alias mapping to an AWS Payment Cryptography key is defined
in the account that owns the AWS Payment Cryptography key and might differ in each Region.

One of the most powerful uses of aliases is in applications that run in multiple
AWS Regions.

You could create a different version of your application in each Region or use a
dictionary, configuration or switch statement to select the right AWS Payment Cryptography key for each Region. But it might be
easier to create an alias with the same alias name in each Region. Remember that the alias
name is case-sensitive.
