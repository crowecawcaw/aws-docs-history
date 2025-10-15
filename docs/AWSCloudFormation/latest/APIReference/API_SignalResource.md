# SignalResource

Sends a signal to the specified resource with a success or failure status. You can use the
 `SignalResource` operation in conjunction with a creation policy or update
 policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the
 required number of signals or the timeout period is exceeded. The `SignalResource`
 operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2
 instance.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**LogicalResourceId** 


The logical ID of the resource that you want to signal. The logical ID is the name of the
 resource that given in the template.


Type: String


Required: Yes




**StackName** 


The stack name or unique stack ID that includes the resource that you want to
 signal.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




**Status** 


The status of the signal, which is either success or failure. A failure signal causes
 CloudFormation to immediately fail the stack creation or update.


Type: String


Valid Values: `SUCCESS | FAILURE`



Required: Yes




**UniqueId** 


A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the
 instance ID that you are signaling as the unique ID. If you send multiple signals to a single
 resource (such as signaling a wait condition), each signal requires a different unique
 ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### SignalResource


This example illustrates one usage of SignalResource.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=SignalResource
 &LogicalResourceId=MyWaitCondition
 &StackName=AWaitingTestStack
 &Status=SUCCESS
 &UniqueId=test-signal
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<SignalResourceResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ResponseMetadata>
    <RequestId>e7d8c346-744b-11e5-b40b-example</RequestId>
  </ResponseMetadata>
</SignalResourceResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SignalResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SignalResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SignalResource")
