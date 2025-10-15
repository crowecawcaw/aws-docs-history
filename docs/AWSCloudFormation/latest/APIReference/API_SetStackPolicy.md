# SetStackPolicy

Sets a stack policy for a specified stack.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**StackName** 


The name or unique stack ID that you want to associate a policy with.


Type: String


Required: Yes




**StackPolicyBody** 


Structure that contains the stack policy body. For more information, see [Prevent updates to stack resources](../UserGuide/protect-stack-resources.md "../UserGuide/protect-stack-resources.md") in the *AWS CloudFormation User Guide*.
 You can specify either the `StackPolicyBody` or the `StackPolicyURL`
 parameter, but not both.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 16384.


Required: No




**StackPolicyURL** 


Location of a file that contains the stack policy. The URL must point to a policy (maximum
 size: 16 KB) located in an Amazon S3 bucket in the same AWS Region as the stack. The location for
 an Amazon S3 bucket must start with `https://`. URLs from S3 static websites are not
 supported.


You can specify either the `StackPolicyBody` or the `StackPolicyURL`
 parameter, but not both.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### SetStackPolicy


This example illustrates one usage of SetStackPolicy.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=SetStackPolicy
 &StackName=MyStack
 &StackPolicyBody=[Stack Policy Document]
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<SetStackPolicyResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ResponseMetadata>
    <RequestId>e7d8c346-744b-11e5-b40b-example</RequestId>
  </ResponseMetadata>
</SetStackPolicyResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetStackPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetStackPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetStackPolicy")
