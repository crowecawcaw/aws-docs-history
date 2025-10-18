# GetStackPolicy

Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null
 value is returned.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**StackName** 


The name or unique stack ID that's associated with the stack whose policy you want to
 get.


Type: String


Required: Yes




## Response Elements


The following element is returned by the service.





**StackPolicyBody** 


Structure that contains the stack policy body. (For more information, see [Prevent updates to stack resources](../UserGuide/protect-stack-resources.md "../UserGuide/protect-stack-resources.md") in the
 *AWS CloudFormation User Guide*.)


Type: String


Length Constraints: Minimum length of 1. Maximum length of 16384.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### GetStackPolicy


This example illustrates one usage of GetStackPolicy.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=GetStackPolicy
 &StackName=MyStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<GetStackPolicyResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <GetStackPolicyResult>
      <StackPolicyBody>"{
      "Statement" : [
        {
          "Effect" : "Deny",
          "Action" : "Update:*",
          "Principal" : "*",
          "Resource" : "LogicalResourceId/ProductionDatabase"
        },
        {
          "Effect" : "Allow",
          "Action" : "Update:*",
          "Principal" : "*",
          "Resource" : "*"
        }
      ]
    }</StackPolicyBody>
  </GetStackPolicyResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</GetStackPolicyResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetStackPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetStackPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetStackPolicy")
