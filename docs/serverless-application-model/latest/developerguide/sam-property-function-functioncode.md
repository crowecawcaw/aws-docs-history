

# FunctionCode
<a name="sam-property-function-functioncode"></a>

The [deployment package](https://docs.aws.amazon.com/lambda/latest/dg/deployment-package-v2.html) for a Lambda function.

## Syntax
<a name="sam-property-function-functioncode-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-functioncode-syntax.yaml"></a>

```
  [Bucket](#sam-function-functioncode-bucket): {{String}}
  [Key](#sam-function-functioncode-key): {{String}}
  [StorageMode](#sam-function-functioncode-storagemode): {{String}}
  [Version](#sam-function-functioncode-version): {{String}}
```

## Properties
<a name="sam-property-function-functioncode-properties"></a>

 `Bucket`   <a name="sam-function-functioncode-bucket"></a>
An Amazon S3 bucket in the same AWS Region as your function.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[S3Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3bucket)` property of the `AWS::Lambda::Function` `Code` data type.

 `Key`   <a name="sam-function-functioncode-key"></a>
The Amazon S3 key of the deployment package.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[S3Key](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3key)` property of the `AWS::Lambda::Function` `Code` data type.

 `StorageMode`   <a name="sam-function-functioncode-storagemode"></a>
Controls how Lambda stores the deployment package.  
+ `COPY` – Lambda uploads a copy of your deployment package to Lambda-managed storage. You can delete the Amazon S3 object after Lambda creates the function.
+ `REFERENCE` – Lambda references the deployment package from your Amazon S3 bucket and doesn't store a copy. The object must remain in place, and Lambda must keep access to it, for the lifetime of the function.
To use `REFERENCE`, enable versioning on your Amazon S3 bucket and grant the Lambda service principal access to the object. For more information, see [Self-managed Amazon S3 code storage](https://docs.aws.amazon.com/lambda/latest/dg/configuration-self-managed-storage.html) in the *AWS Lambda Developer Guide*.  
*Type*: String  
*Valid values*: `COPY` \| `REFERENCE`  
*Required*: No  
*Default*: `COPY`  
*CloudFormation compatibility*: This property is passed directly to the `[S3ObjectStorageMode](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3objectstoragemode)` property of the `AWS::Lambda::Function` `Code` data type.

 `Version`   <a name="sam-function-functioncode-version"></a>
For versioned objects, the version of the deployment package object to use.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[S3ObjectVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3objectversion)` property of the `AWS::Lambda::Function` `Code` data type.

## Examples
<a name="sam-property-function-functioncode--examples"></a>

### FunctionCode
<a name="sam-property-function-functioncode--examples--functioncode"></a>

`CodeUri`: Function Code example

#### YAML
<a name="sam-property-function-functioncode--examples--functioncode--yaml"></a>

```
CodeUri:
  Bucket: sam-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212
```

### Self-managed Amazon S3 code storage
<a name="sam-property-function-functioncode--examples--storagemode"></a>

The following `CodeUri` references the deployment package from your own Amazon S3 bucket instead of copying it to Lambda-managed storage.

#### YAML
<a name="sam-property-function-functioncode--examples--storagemode--yaml"></a>

```
CodeUri:
  Bucket: amzn-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212
  StorageMode: REFERENCE
```