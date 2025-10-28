This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Condition` attribute

To create resources in CloudFormation based on conditions, first declare your condition in the
template's `Conditions` section. Then, use the `Condition` key along
with the condition's logical ID as an attribute on the resource. CloudFormation creates the
resource only when the condition evaluates to true. This lets you control resource creation
based on specific criteria or parameters you define in your template.

If you're new to using conditions in your templates, we recommend you first review the
[CloudFormation
template Conditions syntax](../UserGuide/conditions-section-structure.md "../UserGuide/conditions-section-structure.md") topic in the
_AWS CloudFormation User Guide_.

###### Note

If a resource with a condition isn't created, any resources that depend on that resource
aren't created either, regardless of their own conditions.

## Example

The following template contains an Amazon S3 bucket resource with a `Condition`
attribute. The bucket is only created if the `CreateBucket` condition evaluates
to `true`.

### JSON

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Parameters" : {
      "EnvType" : {
         "Type" : "String",
         "AllowedValues" : ["prod", "dev"],
         "Default" : "dev",
         "Description" : "Environment type"
      }
   },
   "Conditions" : {
      "CreateBucket" : {"Fn::Equals" : [{"Ref" : "EnvType"}, "prod"]}
   },
   "Resources" : {
      "MyBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Condition" : "CreateBucket",
         "Properties" : {
            "BucketName" : {"Fn::Join" : ["-", ["mybucket", {"Ref" : "EnvType"}]]}
         }
      }
   }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  EnvType:
    Type: String
    AllowedValues:
      - prod
      - dev
    Default: dev
    Description: Environment type
Conditions:
  CreateBucket: !Equals [!Ref EnvType, prod]
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Condition: CreateBucket
    Properties:
      BucketName: !Sub mybucket-${EnvType}
```

## Using multiple conditions

You can combine multiple conditions using intrinsic functions like [Fn::And](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and"), [Fn::Or](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or"), and [Fn::Not](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not") to create more complex
conditional logic.

### JSON

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Parameters" : {
      "EnvType" : {
         "Type" : "String",
         "AllowedValues" : ["prod", "test", "dev"],
         "Default" : "dev",
         "Description" : "Environment type"
      },
      "CreateResources" : {
         "Type" : "String",
         "AllowedValues" : ["true", "false"],
         "Default" : "true",
         "Description" : "Create resources flag"
      }
   },
   "Conditions" : {
      "IsProd" : {"Fn::Equals" : [{"Ref" : "EnvType"}, "prod"]},
      "IsTest" : {"Fn::Equals" : [{"Ref" : "EnvType"}, "test"]},
      "CreateResourcesFlag" : {"Fn::Equals" : [{"Ref" : "CreateResources"}, "true"]},
      "CreateProdResources" : {"Fn::And" : [{"Condition" : "IsProd"}, {"Condition" : "CreateResourcesFlag"}]},
      "CreateTestOrDevResources" : {"Fn::And" : [{"Fn::Or" : [{"Condition" : "IsTest"}, {"Fn::Not" : [{"Condition" : "IsProd"}]}]}, {"Condition" : "CreateResourcesFlag"}]}
   },
   "Resources" : {
      "ProdBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Condition" : "CreateProdResources",
         "Properties" : {
            "BucketName" : {"Fn::Join" : ["-", ["prod-bucket", {"Ref" : "AWS::StackName"}]]}
         }
      },
      "TestDevBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Condition" : "CreateTestOrDevResources",
         "Properties" : {
            "BucketName" : {"Fn::Join" : ["-", [{"Ref" : "EnvType"}, "bucket", {"Ref" : "AWS::StackName"}]]}
         }
      }
   }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  EnvType:
    Type: String
    AllowedValues:
      - prod
      - test
      - dev
    Default: dev
    Description: Environment type
  CreateResources:
    Type: String
    AllowedValues:
      - 'true'
      - 'false'
    Default: 'true'
    Description: Create resources flag
Conditions:
  IsProd: !Equals [!Ref EnvType, prod]
  IsTest: !Equals [!Ref EnvType, test]
  CreateResourcesFlag: !Equals [!Ref CreateResources, 'true']
  CreateProdResources: !And
    - !Condition IsProd
    - !Condition CreateResourcesFlag
  CreateTestOrDevResources: !And
    - !Or
      - !Condition IsTest
      - !Not [!Condition IsProd]
    - !Condition CreateResourcesFlag
Resources:
  ProdBucket:
    Type: AWS::S3::Bucket
    Condition: CreateProdResources
    Properties:
      BucketName: !Sub prod-bucket-${AWS::StackName}
  TestDevBucket:
    Type: AWS::S3::Bucket
    Condition: CreateTestOrDevResources
    Properties:
      BucketName: !Sub ${EnvType}-bucket-${AWS::StackName}
```

## Using `AWS::AccountId` in

conditions

You can use pseudo parameters like `AWS::AccountId` in your conditions to
create resources based on the AWS account where the stack is being deployed. This is
useful for multi-account deployments or when you need to exclude specific accounts from
receiving certain resources. For more information about pseudo parameters, see [Get AWS values
using pseudo parameters](../UserGuide/pseudo-parameter-reference.md "../UserGuide/pseudo-parameter-reference.md") in the _AWS CloudFormation User Guide_.

### JSON

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Conditions" : {
      "ExcludeAccount1" : {"Fn::Not" : [{"Fn::Equals" : [{"Ref" : "AWS::AccountId"}, "111111111111"]}]},
      "ExcludeAccount2" : {"Fn::Not" : [{"Fn::Equals" : [{"Ref" : "AWS::AccountId"}, "222222222222"]}]},
      "ExcludeBothAccounts" : {"Fn::And" : [{"Condition" : "ExcludeAccount1"}, {"Condition" : "ExcludeAccount2"}]}
   },
   "Resources" : {
      "StandardBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Properties" : {
            "BucketName" : {"Fn::Join" : ["-", ["standard-bucket", {"Ref" : "AWS::StackName"}]]}
         }
      },
      "RestrictedResource" : {
         "Type" : "AWS::SNS::Topic",
         "Condition" : "ExcludeBothAccounts",
         "Properties" : {
            "TopicName" : {"Fn::Join" : ["-", ["restricted-topic", {"Ref" : "AWS::StackName"}]]}
         }
      }
   }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Conditions:
  ExcludeAccount1: !Not [!Equals [!Ref 'AWS::AccountId', '111111111111']]
  ExcludeAccount2: !Not [!Equals [!Ref 'AWS::AccountId', '222222222222']]
  ExcludeBothAccounts: !And
    - !Condition ExcludeAccount1
    - !Condition ExcludeAccount2
Resources:
  StandardBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub standard-bucket-${AWS::StackName}
  RestrictedResource:
    Type: AWS::SNS::Topic
    Condition: ExcludeBothAccounts
    Properties:
      TopicName: !Sub restricted-topic-${AWS::StackName}
```
