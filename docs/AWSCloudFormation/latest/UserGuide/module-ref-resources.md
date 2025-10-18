# Reference module resources in CloudFormation
 templates

In CloudFormation templates, you often need to set properties on one resource based on the
 name or property of another resource. For more information, see [Referencing resources](resources-section-structure.md#using-cross-resource-references "resources-section-structure.md#using-cross-resource-references").

To reference a resource contained within a module in your CloudFormation template, you must
 combine two logical names:


* The logical name you gave to the module itself when you included it in your
 template.
* The logical name of the specific resource within that module.
You can combine these two logical names with or without using a period (.) between them.
 For example, if the module's logical name is `MyModule` and the resource's logical
 name is `MyBucket`, you can refer to that resource as either
 `MyModule.MyBucket` or `MyModuleMyBucket`.

To find the logical names of resources inside a module, you can consult the module's
 schema, which is available in the CloudFormation registry or by using the [DescribeType](../APIReference/API_DescribeType.md "../APIReference/API_DescribeType.md") operation. The schema lists all the resources and
 their logical names that are part of the module.

Once you have the full logical name, you can use CloudFormation functions like
 `GetAtt` and `Ref` to access property values on module resources. 

For example, you have a `My::S3::SampleBucket::MODULE` module that contains an
 `AWS::S3::Bucket` resource with the logical name `S3Bucket`. To refer
 to the name of this bucket using the `Ref` function, you combine the module's name
 in your template (`MyBucket`) with the logical name of the resource in the module
 (`S3Bucket`). The full logical name is either `MyBucket.S3Bucket` or
 `MyBucketS3Bucket`.


###### Example template


The following example template creates an S3 bucket using the
 `My::S3::SampleBucket::MODULE` module. It also create an Amazon SQS queue and set
 its name to be the same as the bucket name from the module. Additionally, the template
 outputs the Amazon Resource Name (ARN) of the created S3 bucket.



```
# Template that uses My::S3::SampleBucket::MODULE
Parameters:
  BucketName:
    Description: Name for your sample bucket
    Type: String
Resources:
  MyBucket:
    Type: My::S3::SampleBucket::MODULE
    Properties:
      BucketName: !Ref BucketName
  exampleQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Ref **MyBucket.S3Bucket**
Outputs:
  BucketArn:
    Value: !**GetAtt MyBucket.S3Bucket.Arn**
```
