This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::SecretsManager`

transform

This topic describes how to use the `AWS::SecretsManager` transform and the
[AWS::SecretsManager::RotationSchedule](aws-resource-secretsmanager-rotationschedule.md "aws-resource-secretsmanager-rotationschedule.md") resource type to specify a Lambda function
to perform secrets rotation.

The `AWS::SecretsManager` transform is a CloudFormation macro that, when referenced
in your stack template, automatically generates a Lambda function for secrets rotation when
you create or update a stack using a change set. The Lambda function is placed in a nested
stack in the processed template. It uses a function template from the [AWS Secrets Manager
Rotation Lambda Functions](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas "https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas") repository, based on the value of the [RotationType](aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md#cfn-secretsmanager-rotationschedule-hostedrotationlambda-rotationtype "aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md#cfn-secretsmanager-rotationschedule-hostedrotationlambda-rotationtype") property of the [AWS::SecretsManager::RotationSchedule](aws-resource-secretsmanager-rotationschedule.md "aws-resource-secretsmanager-rotationschedule.md") resource.

## Usage

To use the `AWS::SecretsManager` transform, you must declare it at the top
level of your CloudFormation template. You can't use `AWS::SecretsManager` as a
transform embedded in any other template section.

The declaration must use the literal string
`AWS::SecretsManager-2020-07-23` or
`AWS::SecretsManager-2024-09-16` as its value. You can't use a parameter
or function to specify a transform value.

### Syntax

To declare this transform in your CloudFormation template, use the following
syntax:

#### JSON

```
{
  "Transform":"AWS::SecretsManager-`2020-07-23`",
  "Resources":{
    `...`
  }
}
```

#### YAML

```
Transform: AWS::SecretsManager-`2020-07-23`
Resources:
  `...`
```

The `AWS::SecretsManager` transform is a standalone declaration with no
additional parameters. Instead, you configure the [HostedRotationLambda](aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md "aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md") property of the [AWS::SecretsManager::RotationSchedule](aws-resource-secretsmanager-rotationschedule.md "aws-resource-secretsmanager-rotationschedule.md") resource in your stack template.
The [HostedRotationLambda](aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md "aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md") property specifies the Lambda function to perform
secrets rotation.

## New features in

`AWS::SecretsManager-2024-09-16`

The latest version of the `AWS::SecretsManager` transform
(`AWS::SecretsManager-2024-09-16`) introduces the following
enhancements:

- Automatic Lambda upgrades – When you
  update your CloudFormation stacks, your Lambda functions now automatically update
  their runtime configuration and internal dependencies. This ensures you're using
  the most secure and reliable versions of the code that manages secret rotation
  in Secrets Manager.
- Support for additional attributes – The
  new transform supports additional resource attributes for the
  `AWS::SecretsManager::RotationSchedule` resource type when used
  with the `HostedRotationLambda` property, including the
  `DependsOn` attribute.

###### Note

Both versions support the `DeletionPolicy` and
`UpdateReplacePolicy` attributes.

To learn more about this new version of the `AWS::SecretsManager`
transform, see [Introducing an enhanced version of the AWS Secrets Manager transform:
AWS::SecretsManager-2024-09-16](https://aws.amazon.com/blogs/security/introducing-an-enhanced-version-of-the-aws-secrets-manager-transform-awssecretsmanager-2024-09-16/ "https://aws.amazon.com/blogs/security/introducing-an-enhanced-version-of-the-aws-secrets-manager-transform-awssecretsmanager-2024-09-16/") on the AWS Security
Blog.

## Examples

The following examples show how to use the `AWS::SecretsManager` transform
(`AWS::SecretsManager-2024-09-16`) and the [AWS::SecretsManager::RotationSchedule](aws-resource-secretsmanager-rotationschedule.md "aws-resource-secretsmanager-rotationschedule.md") resource in your template. In this
example, CloudFormation will automatically generate a Lambda function for MySQL single user
secret rotation.

The secret is set to rotate automatically every day at midnight (UTC). The rotation
process may take up to 2 hours to complete. Updating the rotation schedule won't start
an immediate rotation.

### JSON

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Transform":"AWS::SecretsManager-2024-09-16",
  "Resources":{

  `...`

    "`MySecretRotationSchedule`":{
      "Type":"AWS::SecretsManager::RotationSchedule",
      "DependsOn":"`logical name of AWS::SecretsManager::SecretTargetAttachment resource`",
      "Properties":{
        "SecretId":{
          "Ref":"`logical name of AWS::SecretsManager::Secret resource`"
        },
        "HostedRotationLambda":{
          "RotationType":"MySQLSingleUser",
          "RotationLambdaName":"`name of Lambda function to be created`",
          "VpcSecurityGroupIds":{
            "Fn::GetAtt":[
              "`logical name of AWS::EC2::SecurityGroup resource`",
              "GroupId"
            ]
          },
          "VpcSubnetIds":{
            "Fn::Join":[
              ",",
              [
                {
                  "Ref":"`logical name of primary subnet`"
                },
                {
                  "Ref":"`logical name of secondary subnet`"
                }
              ]
            ]
          }
        },
        "RotationRules":{
          "ScheduleExpression":"cron(0 0 * * ? *)",
          "Duration":"2h"
        },
        "RotateImmediatelyOnUpdate":false
      }
    }
  }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::SecretsManager-2024-09-16
Resources:

  `...`

  `MySecretRotationSchedule`:
    Type: AWS::SecretsManager::RotationSchedule
    DependsOn: `logical name of AWS::SecretsManager::SecretTargetAttachment resource`
    Properties:
      SecretId: !Ref `logical name of AWS::SecretsManager::Secret resource`
      HostedRotationLambda:
        RotationType: MySQLSingleUser
        RotationLambdaName: `name of Lambda function to be created`
        VpcSecurityGroupIds: !GetAtt `logical name of AWS::EC2::SecurityGroup resource`.GroupId
        VpcSubnetIds:
          Fn::Join:
          - ","
          - - Ref: `logical name of primary subnet`
            - Ref: `logical name of secondary subnet`
      RotationRules:
        ScheduleExpression: cron(0 0 * * ? *)
        Duration: 2h
      RotateImmediatelyOnUpdate: false
```

## Related resources

For complete CloudFormation template examples that you can use to set up secret rotations,
see the [Examples](aws-resource-secretsmanager-rotationschedule.md#aws-resource-secretsmanager-rotationschedule--examples "aws-resource-secretsmanager-rotationschedule.md#aws-resource-secretsmanager-rotationschedule--examples") section of `AWS::SecretsManager::RotationSchedule`
resource.

For general information about using macros, see [Perform custom processing on CloudFormation
templates with template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md") in the
_AWS CloudFormation User Guide_.
