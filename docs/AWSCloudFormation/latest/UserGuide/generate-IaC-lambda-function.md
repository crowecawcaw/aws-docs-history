# How to resolve issues with write-only properties
 in AWS::Lambda::Function resources

This topic explains how to resolve issues with write-only properties in [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html") resources when using the IaC generator.


## Issue


The `AWS::Lambda::Function` resource has three mutually exclusive sets of
 properties for specifying the Lambda code:



* `Code/S3Bucket` and `Code/S3Key` properties, and optionally the
 `Code/S3ObjectVersion` property
* `Code/ImageUri` property
* `Code/ZipFile` property

Only one of these sets can be used for a given `AWS::Lambda::Function`
 resource.


The IaC generator can't determine which set of exclusive write-only properties was used to
 create or update the resource. As a result, it includes only the first set of properties in
 the generated template. The `Code/ImageUri` and `Code/ZipFile`
 properties are omitted. 


Additionally, the IaC generator issues the following warnings:



* `MUTUALLY_EXCLUSIVE_PROPERTIES` –
 Warns that `Code/S3Bucket` and `Code/S3Key` are identified as
 mutually exclusive properties.
* `UNSUPPORTED_PROPERTIES` – Warns that
 the `Code/S3ObjectVersion` property is unsupported.

To include `AWS::Lambda::Function` resources in a generated template, you must
 download and update the template with the correct code properties.


## Resolution


If you store your Lambda code in an Amazon S3 bucket and do not use the
 `S3ObjectVersion` property, you can import the generated template
 without any modifications. The IaC generator will ask you for the Amazon S3 bucket and key as
 template parameters during the import operation.


###### If you store your Lambda code as an Amazon ECR repository, you
 can update your template using the following instructions:

1. Download the generated template.
2. Remove the properties and corresponding parameters for the `Code/S3Bucket`
 and `Code/S3Key` properties from the generated template.
3. Replace the removed properties in the generated template with the
 `Code/ImageUri` property, specifying the URL for the Amazon ECR repository.
4. Open the generated template in the IaC generator console and choose the
 **Import edited template** button.

###### If you store your Lambda code as in a zip file, you can
 update your template using the following instructions:

1. Download the generated template.
2. Remove the properties and corresponding parameters for the `Code/S3Bucket`
 and `Code/S3Key` properties from the generated template.
3. Replace the removed properties in the generated template with the
 `Code/ZipFile` property.
4. Open the generated template in the IaC generator console and choose the
 **Import edited template** button.

###### If you don’t have a copy of your Lambda code, you can
 update your template using the following instructions:

1. Use the AWS Lambda [`GetFunction`](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html "https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html") API action
 (for example, by using the [`aws lambda
 get-function`](https://docs.aws.amazon.com/cli/latest/reference/lambda/get-function.html "https://docs.aws.amazon.com/cli/latest/reference/lambda/get-function.html") AWS CLI command.
2. In the response, the `RepositoryType` parameter is `S3` if the
 code is in a Amazon S3 bucket, or `ECR` if the code is in an Amazon ECR
 repository.
3. In the response, the `Location` parameter contains a pre-signed URL that
 you can use to download the deployment package for 10 minutes. Download the code.
4. Upload the code to a Amazon S3 bucket.
5. Run an import operation with t he generated template and provide the bucket name and
 key as parameter values.
