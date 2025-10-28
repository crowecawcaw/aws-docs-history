This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Metadata` attribute

The `Metadata` attribute enables you to associate structured data with a
resource. By adding a `Metadata` attribute to a resource, you can add data in JSON
or YAML to the resource declaration. In addition, you can use intrinsic functions (such as
[Fn::GetAtt](intrinsic-function-reference-getatt.md "intrinsic-function-reference-getatt.md") and [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md")), parameters, and pseudo parameters within the `Metadata` attribute to add those
interpreted values.

###### Note

AWS CloudFormation doesn't validate the syntax within the metadata attribute.

###### Important

CloudFormation doesn't redact or obfuscate any information you include in the metadata
attribute. We strongly recommend you don't use this section to store sensitive information,
such as passwords or secrets.

You can retrieve this data using the [describe-stack-resource](../../../cli/latest/reference/cloudformation/describe-stack-resource.md "../../../cli/latest/reference/cloudformation/describe-stack-resource.md") CLI command or the [DescribeStackResource](../APIReference/API_DescribeStackResource.md "../APIReference/API_DescribeStackResource.md") API
operation.

## Example

The following template contains an Amazon S3 bucket resource with a `Metadata`
attribute.

### JSON

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "MyBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Metadata" : {
            "Object1" : "Location1",
            "Object2" : "Location2"
         }
      }
   }
}
```

### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Metadata:
      Object1: Location1
      Object2: Location2
```
