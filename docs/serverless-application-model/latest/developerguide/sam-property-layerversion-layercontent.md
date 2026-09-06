

# LayerContent
<a name="sam-property-layerversion-layercontent"></a>

A ZIP archive that contains the contents of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Syntax
<a name="sam-property-layerversion-layercontent-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-layerversion-layercontent-syntax.yaml"></a>

```
  [Bucket](#sam-layerversion-layercontent-bucket): {{String}}
  [Key](#sam-layerversion-layercontent-key): {{String}}
  [StorageMode](#sam-layerversion-layercontent-storagemode): {{String}}
  [Version](#sam-layerversion-layercontent-version): {{String}}
```

## Properties
<a name="sam-property-layerversion-layercontent-properties"></a>

 `Bucket`   <a name="sam-layerversion-layercontent-bucket"></a>
The Amazon S3 bucket of the layer archive.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[S3Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3bucket)` property of the `AWS::Lambda::LayerVersion` `Content` data type.

 `Key`   <a name="sam-layerversion-layercontent-key"></a>
The Amazon S3 key of the layer archive.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[S3Key](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3key)` property of the `AWS::Lambda::LayerVersion` `Content` data type.

 `StorageMode`   <a name="sam-layerversion-layercontent-storagemode"></a>
Controls how Lambda stores the layer archive.  
+ `COPY` – Lambda uploads a copy of your layer archive to Lambda-managed storage. You can delete the Amazon S3 object after Lambda creates the layer version.
+ `REFERENCE` – Lambda references the layer archive from your Amazon S3 bucket and doesn't store a copy. The object must remain in place, and Lambda must keep access to it, for the lifetime of the layer version.
To use `REFERENCE`, enable versioning on your Amazon S3 bucket and grant the Lambda service principal access to the object. For more information, see [Self-managed Amazon S3 code storage](https://docs.aws.amazon.com/lambda/latest/dg/configuration-self-managed-storage.html) in the *AWS Lambda Developer Guide*.  
*Type*: String  
*Valid values*: `COPY` \| `REFERENCE`  
*Required*: No  
*Default*: `COPY`  
*CloudFormation compatibility*: This property is passed directly to the `[S3ObjectStorageMode](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3objectstoragemode)` property of the `AWS::Lambda::LayerVersion` `Content` data type.

 `Version`   <a name="sam-layerversion-layercontent-version"></a>
For versioned objects, the version of the layer archive object to use.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[S3ObjectVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3objectversion)` property of the `AWS::Lambda::LayerVersion` `Content` data type.

## Examples
<a name="sam-property-layerversion-layercontent--examples"></a>

### LayerContent
<a name="sam-property-layerversion-layercontent--examples--layercontent"></a>

Layer Content example

#### YAML
<a name="sam-property-layerversion-layercontent--examples--layercontent--yaml"></a>

```
LayerContent:
  Bucket: amzn-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212
```

### Self-managed Amazon S3 code storage
<a name="sam-property-layerversion-layercontent--examples--storagemode"></a>

The following `LayerContent` references the layer archive from your own Amazon S3 bucket instead of copying it to Lambda-managed storage.

#### YAML
<a name="sam-property-layerversion-layercontent--examples--storagemode--yaml"></a>

```
LayerContent:
  Bucket: amzn-s3-demo-bucket-name
  Key: mykey-name
  Version: 121212
  StorageMode: REFERENCE
```