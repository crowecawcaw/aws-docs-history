# CloudFormation template Transform section

The optional `Transform` section specifies one or more macros that CloudFormation
 uses to process your template in some way. 

Macros can perform simple tasks like finding and replacing text, or they can make more
 extensive transformations to the entire template. CloudFormation executes macros in the order
 that they're specified. When you create a change set, CloudFormation generates a change set that
 includes the processed template content. You can then review the changes and execute the
 change set. For more information about how macros work, see [Perform custom processing on CloudFormation templates with
 template macros](template-macros.md "template-macros.md").

CloudFormation also supports *transforms*, which are macros hosted by
 CloudFormation. CloudFormation treats these transforms the same as any macros you create in terms of
 execution order and scope. For more information, see [Transform reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-reference.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-reference.html").

To declare multiple macros, use a list format and specify one or more macros.

For example, in the template sample below, CloudFormation evaluates `MyMacro` and
 then `AWS::Serverless`, both of which can process the contents of the entire
 template because of their inclusion in the `Transform` section.


```
# Start of processable content for MyMacro and AWS::Serverless
Transform:
  - MyMacro
  - 'AWS::Serverless'
Resources:
  WaitCondition:
    Type: AWS::CloudFormation::WaitCondition
  MyBucket:
    Type: AWS::S3::Bucket
    Properties: 
      BucketName: `amzn-s3-demo-bucket`
      Tags: `[{"key":"value"}]`
      CorsConfiguration: `[]`
  MyEc2Instance:
    Type: AWS::EC2::Instance 
    Properties:
      ImageId: `ami-1234567890abcdef0`
# End of processable content for MyMacro and AWS::Serverless
```
