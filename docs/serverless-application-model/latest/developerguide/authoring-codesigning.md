# Set up code signing for your AWS SAM application

To ensure that only trusted code is deployed, you can use AWS SAM to enable code signing with your serverless applications.
Signing your code helps ensure that code has not been altered since signing and that only signed code packages
from trusted publishers run in your Lambda functions. This helps free up organizations from the burden of building
gatekeeper components in their deployment pipelines.

For more information about code signing, see
[Configuring
code signing for Lambda functions](../../../lambda/latest/dg/configuration-codesigning.md "../../../lambda/latest/dg/configuration-codesigning.md") in the _AWS Lambda Developer Guide_.

Before you can configure code signing for your serverless application, you must create a
signing profile using AWS Signer. You use this signing profile for the following tasks:

1. **Creating a code signing configuration** – Declare
   an [`AWS::Lambda::CodeSigningConfig`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md") resource to specify the signing
   profiles of trusted publishers and to set the policy action for validation checks. You can
   declare this object in the same AWS SAM template as your serverless function, in a different
   AWS SAM template, or in an CloudFormation template. You then enable code signing for a serverless
   function by specify the [`CodeSigningConfigArn`](sam-resource-function.md#sam-function-codesigningconfigarn "sam-resource-function.md#sam-function-codesigningconfigarn") property the function with the Amazon
   Resource Name (ARN) of an [`AWS::Lambda::CodeSigningConfig`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md") resource.
2. **Signing your code** – Use the [`sam package`](sam-cli-command-reference-sam-package.md "sam-cli-command-reference-sam-package.md") or [`sam deploy`](sam-cli-command-reference-sam-deploy.md "sam-cli-command-reference-sam-deploy.md") command with the `--signing-profiles`
   option.

###### Note

In order to successfully sign your code with the `sam package` or `sam
 deploy` commands, versioning must be enabled for the Amazon S3 bucket you use with these
commands. If you are using the Amazon S3 Bucket that AWS SAM creates for you, versioning is enabled
automatically. For more information about Amazon S3 bucket versioning and instructions for enabling
versioning on an Amazon S3 bucket that you provide, see [Using versioning in Amazon S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") in
the _Amazon Simple Storage Service User Guide_.

When you deploy a serverless application, Lambda performs validation checks on all functions
that you've enabled code signing for. Lambda also performs validation checks on any layers that
those functions depend on. For more information about Lambda's validation checks, see [Signature
validation](../../../lambda/latest/dg/configuration-codesigning.md#config-codesigning-valid "../../../lambda/latest/dg/configuration-codesigning.md#config-codesigning-valid") in the _AWS Lambda Developer Guide_.

## Example

### Creating a signing

profile

To create a signing profile, run the following command:

```
aws signer put-signing-profile --platform-id "AWSLambda-SHA384-ECDSA" --profile-name `MySigningProfile`
```

If the previous command is successful, you see the signing profile's ARN returned. For
example:

```
{
    "arn": "arn:aws:signer:us-east-1:`111122223333`:/signing-profiles/`MySigningProfile`",
    "profileVersion": "SAMPLEverx",
    "profileVersionArn": "arn:aws:signer:us-east-1:`111122223333`:/signing-profiles/`MySigningProfile`/SAMPLEverx"
}
```

The `profileVersionArn` field contains the ARN to use when you create the
code signing configuration.

### Creating a

code signing configuration and enabling code signing for a function

The following example AWS SAM template declares an [`AWS::Lambda::CodeSigningConfig`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md") resource and enables code signing
for a Lambda function. In this example, there is one trusted profile, and deployments are
rejected if the signature checks fail.

```
Resources:
  HelloWorld:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.7
      CodeSigningConfigArn: !Ref MySignedFunctionCodeSigningConfig

  MySignedFunctionCodeSigningConfig:
    Type: AWS::Lambda::CodeSigningConfig
    Properties:
      Description: "Code Signing for MySignedLambdaFunction"
      AllowedPublishers:
        SigningProfileVersionArns:
          - `MySigningProfile-profileVersionArn`
      CodeSigningPolicies:
        UntrustedArtifactOnDeployment: "Enforce"
```

### Signing your code

You can sign your code when packaging or deploying your application. Specify the
`--signing-profiles` option with either the `sam package` or
`sam deploy` command, as shown in the following example commands.

Signing your function code when packaging your application:

```
sam package --signing-profiles `HelloWorld=MySigningProfile` --s3-bucket `amzn-s3-demo-bucket` --output-template-file packaged.yaml
```

Signing both your function code and a layer that your function depends on, when
packaging your application:

```
sam package --signing-profiles `HelloWorld=MySigningProfile MyLayer=MySigningProfile` --s3-bucket `amzn-s3-demo-bucket` --output-template-file packaged.yaml
```

Signing your function code and a layer, then performing a deployment:

```
sam deploy --signing-profiles `HelloWorld=MySigningProfile MyLayer=MySigningProfile` --s3-bucket `amzn-s3-demo-bucket` --template-file packaged.yaml --stack-name --region us-east-1 --capabilities CAPABILITY_IAM
```

###### Note

In order to successfully sign your code with the `sam package` or `sam
 deploy` commands, versioning must be enabled for the Amazon S3 bucket you use with
these commands. If you are using the Amazon S3 Bucket that AWS SAM creates for you, versioning is
enabled automatically. For more information about Amazon S3 bucket versioning and instructions
for enabling versioning on an Amazon S3 bucket that you provide, see [Using versioning in
Amazon S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") in the _Amazon Simple Storage Service User Guide_.

## Providing signing profiles with

`sam deploy --guided`

When you run the `sam deploy --guided` command with a serverless application
that's configured with code signing, AWS SAM prompts you to provide the signing profile to use
for code signing. For more information about `sam deploy --guided` prompts, see
[sam deploy](sam-cli-command-reference-sam-deploy.md "sam-cli-command-reference-sam-deploy.md") in the AWS SAM CLI command
reference.
