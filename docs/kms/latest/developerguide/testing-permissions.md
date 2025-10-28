# Testing your permissions

To use AWS KMS, you must have credentials that AWS can use to authenticate your API
requests. The credentials must include the permission to access KMS keys and aliases. The
permissions are determined by key policies, IAM policies, grants, and cross-account access
controls. In addition to controlling access to KMS keys, you can control access to your
CloudHSM, and to your custom key stores.

You can specify the `DryRun` API parameter to verify that you have the
necessary permissions to use AWS KMS
keys. You can also use `DryRun` to verify that the request parameters
in a AWS KMS API call are correctly specified.

###### Topics

- [What is the DryRun parameter?](#what-is-dryrun "#what-is-dryrun")
- [Specifying DryRun with the API](#dryrun-api "#dryrun-api")

## What is the DryRun parameter?

`DryRun` is an optional API parameter that you specify to verify that AWS KMS
API calls will succeed. Use `DryRun` to test your API call, before actually
making the call to AWS KMS. You can verify the following.

- That you have the necessary permissions to use
  AWS KMS keys.
- That you have specified the parameters in the call correctly.

AWS KMS supports using the `DryRun` parameter in certain API actions:

- [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md")
- [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")
- [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md")
- [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md")
- [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md")
- [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md")
- [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md")
- [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md")
- [GenerateMac](../APIReference/API_GenerateMac.md "../APIReference/API_GenerateMac.md")
- [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md")
- [RetireGrant](../APIReference/API_RetireGrant.md "../APIReference/API_RetireGrant.md")
- [RevokeGrant](../APIReference/API_RevokeGrant.md "../APIReference/API_RevokeGrant.md")
- [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md")
- [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md")
- [VerifyMac](../APIReference/API_VerifyMac.md "../APIReference/API_VerifyMac.md")

Using the `DryRun` parameter will incur charges and will be billed as a
standard API request. For more information about AWS KMS pricing, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

All API requests using the `DryRun` parameter apply to the request quota
of the API and can result in a throttling exception if you exceed an API request quota.
For example, calling [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") with
`DryRun` or without `DryRun` counts against the same
cryptographic operations quota. See [Throttling AWS KMS requests](throttling.md "throttling.md") to learn more.

Every call to an AWS KMS API operation is captured as an event and recorded in an
AWS CloudTrail log. The output of any operations that specify the `DryRun`
parameter appear in your CloudTrail log. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

## Specifying DryRun with the API

To use `DryRun`, specify the `—dry-run` parameter in AWS CLI
commands and AWS KMS API calls that support the parameter. When you do, AWS KMS will verify
whether your call will succeed. AWS KMS calls that use `DryRun` will
always fail and return a message with information about reason why the call failed. The
message can include the following exceptions:

- `DryRunOperationException` ‐ The
  request would succeed if `DryRun` wasn’t specified.
- `ValidationException` ‐ The request
  failed from specifying an incorrect API parameter.
- `AccessDeniedException` ‐ You do not
  have permissions to perform the specified API action on the KMS resource.

For example, the following command uses the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation and creates a
grant that allows users who are authorized to assume the `keyUserRole` role
to call the [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operation on a
specified [symmetric KMS key](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks"). The
`DryRun` parameter is specified.

```
`$`  `aws kms create-grant \
 --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
 --grantee-principal arn:aws:iam::111122223333:role/keyUserRole \
 --operations Decrypt \
 --dry-run`
```
