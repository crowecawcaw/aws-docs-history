This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::Serverless` transform

This topic describes how to use the `AWS::Serverless` transform to process a
template written in the AWS Serverless Application Model (AWS SAM) syntax and transform it into a compliant CloudFormation
template.

For more information about using the `AWS::Serverless` transform, see [AWS SAM transform](https://github.com/aws/serverless-application-model "https://github.com/aws/serverless-application-model") on
GitHub.

## Usage

To use the `AWS::Serverless` transform, you must declare it at the top level of
your CloudFormation template. You can't use `AWS::Serverless` as a transform embedded
in any other template section.

The declaration must use the literal string `AWS::Serverless-2016-10-31` as its
value. You can't use a parameter or function to specify a transform value.

### Syntax

To declare this transform in your CloudFormation template, use the following syntax:

#### JSON

```
{
  "Transform":"AWS::Serverless-2016-10-31",
  "Resources":{
    `...`
  }
}
```

#### YAML

```
Transform: AWS::Serverless-2016-10-31
Resources:
  `...`
```

The `AWS::Serverless` transform is a standalone declaration with no
additional parameters.

## Examples

The following examples show how to use the `AWS::Serverless` transform and
AWS SAM syntax to simplify the declaration of a Lambda function and its execution role.

### JSON

```
{
  "Transform":"AWS::Serverless-2016-10-31",
  "Resources":{
    "MyFunction":{
      "Type":"AWS::Serverless::Function",
      "Properties":{
        "Handler":"`index.handler`",
        "Runtime":"`nodejs20.x`",
        "CodeUri":"`s3://amzn-s3-demo-bucket/MySourceCode.zip`"
      }
    }
  }
}
```

### YAML

```
Transform: AWS::Serverless-2016-10-31
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: `index.handler`
      Runtime: `nodejs20.x`
      CodeUri: '`s3://amzn-s3-demo-bucket/MySourceCode.zip`'
```

When creating a change set from the template, CloudFormation expands the AWS SAM syntax, as
defined by the transform. The processed template expands the
`AWS::Serverless::Function` resource, declaring a Lambda function and an execution
role.

```
{
  "Resources": {
    "MyFunction": {
      "Type": "AWS::Lambda::Function",
      "Properties": {
        "Handler": "`index.handler`",
        "Code": {
          "S3Bucket": "`amzn-s3-demo-bucket`",
          "S3Key": "`MySourceCode.zip`"
        },
        "Role": {
          "Fn::GetAtt": ["MyFunctionRole", "Arn"]
        },
        "Runtime": "`nodejs20.x`"
      }
    },
    "MyFunctionRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"],
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [{
            "Action": ["sts:AssumeRole"],
            "Effect": "Allow",
            "Principal": {
              "Service": ["lambda.amazonaws.com"]
            }
          }]
        }
      }
    }
  }
}
```

## Using `AWS::Serverless` with

`AWS::LanguageExtensions`

When using both `AWS::Serverless` and `AWS::LanguageExtensions`
transforms, referencing resources like `AWS::ApiGateway::Stage` requires special
syntax when the stage name is passed as a non-`NoEcho` parameter value.

Instead of using the AWS SAM syntax for the reference
(``MyApi`.Stage`), use `Fn::Sub`to
 generate the logical ID reference. For example,`"Ref": {"Fn::Sub":
`"${`MyApi`}`${`StageName`}Stage"}`.
This builds the correct logical ID at runtime.

The reason for this special format is because these two transforms handle values
differently:

- `AWS::LanguageExtensions` resolves intrinsic functions to their actual
  values.
- `AWS::Serverless` creates different logical IDs depending on whether it
  receives a static value or an intrinsic function.

## Related resources

For more information about serverless applications and the AWS Serverless Application Model (AWS SAM), see [AWS Serverless Application Model Developer Guide](../../../serverless-application-model/latest/developerguide/what-is-sam.md "../../../serverless-application-model/latest/developerguide/what-is-sam.md").

For the resource and property types that are specific to AWS SAM, see [AWS SAM resources and properties](../../../serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.md "../../../serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.md") in the _AWS Serverless Application Model Developer Guide_.

For general information about using macros, see [Perform custom processing on CloudFormation templates with
template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md") in the _AWS CloudFormation User Guide_.
