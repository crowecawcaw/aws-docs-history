

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Condition` attribute
<a name="aws-attribute-condition"></a>

To create resources in CloudFormation based on conditions, first declare your condition in the template's `Conditions` section. Then, use the `Condition` key along with the condition's logical ID as an attribute on the resource. CloudFormation creates the resource only when the condition evaluates to true. This lets you control resource creation based on specific criteria or parameters you define in your template.

If you're new to using conditions in your templates, we recommend you first review the [CloudFormation template Conditions syntax](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html) topic in the *AWS CloudFormation User Guide*.

**Note**  
If a resource with a condition isn't created, any resources that depend on that resource aren't created either, regardless of their own conditions.

## Example
<a name="aws-attribute-condition-example"></a>

The following template contains an Amazon S3 bucket resource with a `Condition` attribute. The bucket is only created if the `CreateBucket` condition evaluates to `true`.

### JSON
<a name="aws-attribute-condition-example.json"></a>

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
<a name="aws-attribute-condition-example.yaml"></a>

```
 1. AWSTemplateFormatVersion: 2010-09-09
 2. Parameters:
 3.   EnvType:
 4.     Type: String
 5.     AllowedValues:
 6.       - prod
 7.       - dev
 8.     Default: dev
 9.     Description: Environment type
10. Conditions:
11.   CreateBucket: !Equals [!Ref EnvType, prod]
12. Resources:
13.   MyBucket:
14.     Type: AWS::S3::Bucket
15.     Condition: CreateBucket
16.     Properties:
17.       BucketName: !Sub mybucket-${EnvType}
```

## Using multiple conditions
<a name="aws-attribute-condition-multiple"></a>

You can combine multiple conditions using intrinsic functions like [`Fn::And`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and), [`Fn::Or`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or), and [`Fn::Not`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not) to create more complex conditional logic.

### JSON
<a name="aws-attribute-condition-multiple.json"></a>

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
<a name="aws-attribute-condition-multiple.yaml"></a>

```
 1. AWSTemplateFormatVersion: 2010-09-09
 2. Parameters:
 3.   EnvType:
 4.     Type: String
 5.     AllowedValues:
 6.       - prod
 7.       - test
 8.       - dev
 9.     Default: dev
10.     Description: Environment type
11.   CreateResources:
12.     Type: String
13.     AllowedValues:
14.       - 'true'
15.       - 'false'
16.     Default: 'true'
17.     Description: Create resources flag
18. Conditions:
19.   IsProd: !Equals [!Ref EnvType, prod]
20.   IsTest: !Equals [!Ref EnvType, test]
21.   CreateResourcesFlag: !Equals [!Ref CreateResources, 'true']
22.   CreateProdResources: !And
23.     - !Condition IsProd
24.     - !Condition CreateResourcesFlag
25.   CreateTestOrDevResources: !And
26.     - !Or
27.       - !Condition IsTest
28.       - !Not [!Condition IsProd]
29.     - !Condition CreateResourcesFlag
30. Resources:
31.   ProdBucket:
32.     Type: AWS::S3::Bucket
33.     Condition: CreateProdResources
34.     Properties:
35.       BucketName: !Sub prod-bucket-${AWS::StackName}
36.   TestDevBucket:
37.     Type: AWS::S3::Bucket
38.     Condition: CreateTestOrDevResources
39.     Properties:
40.       BucketName: !Sub ${EnvType}-bucket-${AWS::StackName}
```

## Using `AWS::AccountId` in conditions
<a name="aws-attribute-condition-account"></a>

You can use pseudo parameters like `AWS::AccountId` in your conditions to create resources based on the AWS account where the stack is being deployed. This is useful for multi-account deployments or when you need to exclude specific accounts from receiving certain resources. For more information about pseudo parameters, see [Get AWS values using pseudo parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html) in the *AWS CloudFormation User Guide*.

### JSON
<a name="aws-attribute-condition-account.json"></a>

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
<a name="aws-attribute-condition-account.yaml"></a>

```
 1. AWSTemplateFormatVersion: 2010-09-09
 2. Conditions:
 3.   ExcludeAccount1: !Not [!Equals [!Ref 'AWS::AccountId', '111111111111']]
 4.   ExcludeAccount2: !Not [!Equals [!Ref 'AWS::AccountId', '222222222222']]
 5.   ExcludeBothAccounts: !And
 6.     - !Condition ExcludeAccount1
 7.     - !Condition ExcludeAccount2
 8. Resources:
 9.   StandardBucket:
10.     Type: AWS::S3::Bucket
11.     Properties:
12.       BucketName: !Sub standard-bucket-${AWS::StackName}
13.   RestrictedResource:
14.     Type: AWS::SNS::Topic
15.     Condition: ExcludeBothAccounts
16.     Properties:
17.       TopicName: !Sub restricted-topic-${AWS::StackName}
```