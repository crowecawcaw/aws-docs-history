

# CodeUri
<a name="sam-property-webfunction-codeuri"></a>

Specifies the Amazon S3 location of a Web Function's deployment package. You can specify the location as an object, or as a string of the form `s3://{{bucket}}/{{key}}` with an optional `?versionId={{version}}` query parameter.

The bucket must have versioning enabled and a bucket policy that grants `lambda.amazonaws.com` the `s3:GetObject` and `s3:GetObjectVersion` permissions. We recommend that you scope the policy with an `aws:SourceArn` condition that matches the function's revisions. If the object is encrypted with SSE-KMS, use a customer managed key whose key policy allows `lambda.amazonaws.com` to call `kms:Decrypt`. The AWS managed key for Amazon S3 (`aws/s3`) isn't supported. For details, see [Deploying Web Function code from Amazon S3](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-code-s3.html) in the *AWS Lambda Developer Guide*.

## Syntax
<a name="sam-property-webfunction-codeuri-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-webfunction-codeuri-syntax.yaml"></a>

```
[Bucket](#sam-webfunction-codeuri-bucket): {{String}}
[Key](#sam-webfunction-codeuri-key): {{String}}
[Version](#sam-webfunction-codeuri-version): {{String}}
```

## Properties
<a name="sam-property-webfunction-codeuri-properties"></a>

 `Bucket`   <a name="sam-webfunction-codeuri-bucket"></a>
The name of the Amazon S3 bucket that contains the deployment package.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `Bucket` property of `[BuildConfig.CodeConfig.S3Object](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-s3object.html#cfn-lambda-webfunctionrevision-s3object-bucket)` of an `AWS::Lambda::WebFunctionRevision` resource. 

 `Key`   <a name="sam-webfunction-codeuri-key"></a>
The Amazon S3 key of the deployment package.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `Key` property of `[BuildConfig.CodeConfig.S3Object](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-s3object.html#cfn-lambda-webfunctionrevision-s3object-key)` of an `AWS::Lambda::WebFunctionRevision` resource. 

 `Version`   <a name="sam-webfunction-codeuri-version"></a>
The version ID of the deployment package object. Specify a version to pin the revision to a specific upload.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `VersionId` property of `[BuildConfig.CodeConfig.S3Object](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-s3object.html#cfn-lambda-webfunctionrevision-s3object-versionid)` of an `AWS::Lambda::WebFunctionRevision` resource. AWS SAM passes the value as `VersionId`. 

## Examples
<a name="sam-property-webfunction-codeuri-examples"></a>

### Object form
<a name="sam-property-webfunction-codeuri-example-object"></a>

```
CodeUri:
  Bucket: amzn-s3-demo-bucket
  Key: webfn.zip
  Version: {{object-version-id}}
```

### URI form
<a name="sam-property-webfunction-codeuri-example-uri"></a>

```
CodeUri: s3://amzn-s3-demo-bucket/webfn.zip?versionId={{object-version-id}}
```