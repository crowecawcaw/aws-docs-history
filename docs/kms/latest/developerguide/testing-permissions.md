

# Testing your permissions
<a name="testing-permissions"></a>

To use AWS KMS, you must have credentials that AWS can use to authenticate your API requests. The credentials must include the permission to access KMS keys and aliases. The permissions are determined by key policies, IAM policies, grants, and cross-account access controls. In addition to controlling access to KMS keys, you can control access to your CloudHSM, and to your custom key stores.

You can specify the `DryRun` API parameter to verify that you have the necessary permissions to use AWS KMS keys. You can also use `DryRun` to verify that the request parameters in a AWS KMS API call are correctly specified. 

**Topics**
+ [What is the DryRun parameter?](#what-is-dryrun)
+ [Specifying DryRun with the API](#dryrun-api)

## What is the DryRun parameter?
<a name="what-is-dryrun"></a>

 `DryRun` is an optional API parameter that you specify to verify that AWS KMS API calls will succeed. Use `DryRun` to test your API call, before actually making the call to AWS KMS. You can verify the following. 
+ That you have the necessary permissions to use AWS KMS keys.
+ That you have specified the parameters in the call correctly.

AWS KMS supports using the `DryRun` parameter in certain API actions: 
+ [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)
+ [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)
+ [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html)
+ [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html)
+ [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html)
+ [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html)
+ [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html)
+ [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html)
+ [GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)
+ [ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
+ [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html)
+ [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html)
+ [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html)
+ [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html)
+ [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html)

Using the `DryRun` parameter will incur charges and will be billed as a standard API request. For more information about AWS KMS pricing, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/).

 All API requests using the `DryRun` parameter apply to the request quota of the API and can result in a throttling exception if you exceed an API request quota. For example, calling [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) with `DryRun` or without `DryRun` counts against the same cryptographic operations quota. See [Throttling AWS KMS requests](throttling.md) to learn more.

Every call to an AWS KMS API operation is captured as an event and recorded in an AWS CloudTrail log. The output of any operations that specify the `DryRun` parameter appear in your CloudTrail log. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](logging-using-cloudtrail.md).

## Specifying DryRun with the API
<a name="dryrun-api"></a>

To use `DryRun`, specify the `—dry-run` parameter in AWS CLI commands and AWS KMS API calls that support the parameter. When you do, AWS KMS will verify whether your call will succeed. AWS KMS calls that use `DryRun` will always fail and return a message with information about reason why the call failed. The message can include the following exceptions:
+ `DryRunOperationException` ‐ The request would succeed if `DryRun` wasn’t specified. 
+ `ValidationException` ‐ The request failed from specifying an incorrect API parameter.
+ `AccessDeniedException` ‐ You do not have permissions to perform the specified API action on the KMS resource.

For example, the following command uses the [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) operation and creates a grant that allows users who are authorized to assume the `keyUserRole` role to call the [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation on a specified [symmetric KMS key](symm-asymm-choose-key-spec.md#symmetric-cmks). The `DryRun` parameter is specified.

```
$  aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-principal arn:aws:iam::111122223333:role/keyUserRole \
    --operations Decrypt \
    --dry-run
```