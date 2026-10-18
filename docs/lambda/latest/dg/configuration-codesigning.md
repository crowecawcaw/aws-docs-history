

# Using code signing to verify code integrity with Lambda
<a name="configuration-codesigning"></a>

Code signing helps ensure that only trusted code is deployed to your Lambda functions. Using AWS Signer, you can create digitally signed code packages for your functions. When you [add a code signing configuration to a function](configuration-codesigning-create.md), Lambda verifies that all new code deployments are signed by a trusted source. Because code signing validation checks run at deployment time, there is no impact on function execution. For information about managing code signing policies, see [Configuring IAM policies for Lambda code signing configurations](config-codesigning-policies.md).

**Note**  
Code signing applies to Lambda Event Functions deployed as .zip or container image packages. It isn't used by Lambda Web Functions or Lambda MicroVMs.

**Important**  
Code signing configurations only prevent new deployments of unsigned code. If you add a code signing configuration to an existing function that has unsigned code, that code keeps running until you deploy a new code package.

When you enable code signing for a function, any [layers](chapter-layers.md) that you add to the function must also be signed by an allowed signing profile.

There is no additional charge for using AWS Signer or code signing for AWS Lambda.

## Signature validation
<a name="config-codesigning-valid"></a>

Lambda performs the following validation checks when you deploy a signed code package to your function:

1. **Integrity**: Validates that the code package has not been modified since it was signed. Lambda compares the hash of the package with the hash from the signature.

1. **Expiry**: Validates that the signature of the code package has not expired.

1. **Mismatch**: Validates that the code package is signed with an allowed signing profile

1. **Revocation**: Validates that the signature of the code package has not been revoked.

When you create a code signing configuration, you can use the [UntrustedArtifactOnDeployment](https://docs.aws.amazon.com/lambda/latest/api/API_CodeSigningPolicies.html#lambda-Type-CodeSigningPolicies-UntrustedArtifactOnDeployment) parameter to specify how Lambda should respond if the expiry, mismatch, or revocation checks fail. You can choose one of these actions:
+ `Warn`: This is the default setting. Lambda allows the deployment of the code package, but issues a warning. Lambda issues a new Amazon CloudWatch metric (`SignatureValidationErrors`) and also stores the warning in the CloudTrail log.
+ `Enforce` Lambda issues a warning (the same as for the `Warn` action) and blocks the deployment of the code package.

**Topics**
+ [Signature validation](#config-codesigning-valid)
+ [Creating code signing configurations for Lambda](configuration-codesigning-create.md)
+ [Configuring IAM policies for Lambda code signing configurations](config-codesigning-policies.md)
+ [Using tags on code signing configurations](tags-csc.md)