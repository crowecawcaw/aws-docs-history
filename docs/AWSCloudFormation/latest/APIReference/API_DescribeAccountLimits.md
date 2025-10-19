# DescribeAccountLimits

Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you
 can create in your account. For more information about account limits, see [Understand CloudFormation quotas](../UserGuide/cloudformation-limits.md "../UserGuide/cloudformation-limits.md") in the *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**NextToken** 


A string that identifies the next page of limits that you want to retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




## Response Elements


The following elements are returned by the service.





**AccountLimits.member.N**


An account limit structure that contain a list of CloudFormation account limits and their
 values.


Type: Array of [AccountLimit](API_AccountLimit.md "API_AccountLimit.md") objects




**NextToken** 


If the output exceeds 1 MB in size, a string that identifies the next page of limits. If
 no additional page exists, this value is null.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeAccountLimits


This example illustrates one usage of DescribeAccountLimits.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeAccountLimits
 &NextToken=[NextToken]
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<DescribeAccountLimitsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeAccountLimitsResult>
    <AccountLimits>
      <member>
        <Name>StackLimit</Name>
        <Value>20</Value>
      </member>
    </AccountLimits>
  </DescribeAccountLimitsResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</DescribeAccountLimitsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeAccountLimits")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeAccountLimits "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeAccountLimits")
