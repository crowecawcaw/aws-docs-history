# AwsKms resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsKms`
resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsKmsKey

The `AwsKmsKey` object provides details about an AWS KMS key.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsKmsKey` object. To view descriptions of `AwsKmsKey`
attributes, see [AwsKmsKeyDetails](../../1.0/APIReference/API_AwsKmsKeyDetails.md "../../1.0/APIReference/API_AwsKmsKeyDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsKmsKey": {
                        "AWSAccountId": "string",
                        "CreationDate": "string",
                        "Description": "string",
                        "KeyId": "string",
                        "KeyManager": "string",
                        "KeyRotationStatus": boolean,
                        "KeyState": "string",
                        "Origin": "string"
                    }
```
