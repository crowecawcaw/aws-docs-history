# SetTypeDefaultVersion

Specify the default version of an extension. The default version of an extension will be
 used in CloudFormation operations.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Arn** 


The Amazon Resource Name (ARN) of the extension for which you want version summary
 information.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+`



Required: No




**Type** 


The kind of extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




**VersionId** 


The ID of a specific version of the extension. The version ID is the value at the end of
 the Amazon Resource Name (ARN) assigned to the extension version when it is registered.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




**TypeNotFound** 


The specified extension doesn't exist in the CloudFormation registry.


HTTP Status Code: 404




## Examples


### SetTypeDefaultVersion


This example illustrates one usage of SetTypeDefaultVersion.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=SetTypeDefaultVersion
 &Version=2010-05-15
 &TypeName=My::Resource::Example
 &VersionId=00000003
 &Type=RESOURCE
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191204T182814Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<SetTypeDefaultVersionResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <SetTypeDefaultVersionResult/>
  <ResponseMetadata>
    <RequestId>dc46ff50-4ab3-485a-a104-bbbd3example</RequestId>
  </ResponseMetadata>
</SetTypeDefaultVersionResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetTypeDefaultVersion")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetTypeDefaultVersion "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetTypeDefaultVersion")
