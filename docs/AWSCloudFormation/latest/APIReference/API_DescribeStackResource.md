# DescribeStackResource

Returns a description of the specified resource in the specified stack.

For deleted stacks, DescribeStackResource returns resource information for up to 90 days
 after the stack has been deleted.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**LogicalResourceId** 


The logical name of the resource as specified in the template.


Type: String


Required: Yes




**StackName** 


The name or the unique stack ID that's associated with the stack, which aren't always
 interchangeable:



* Running stacks: You can specify either the stack's name or its unique stack ID.
* Deleted stacks: You must specify the unique stack ID.

Type: String


Required: Yes




## Response Elements


The following element is returned by the service.





**StackResourceDetail** 


A `StackResourceDetail` structure that contains the description of the
 specified resource in the specified stack.


Type: [StackResourceDetail](API_StackResourceDetail.md "API_StackResourceDetail.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeStackResource


This example illustrates one usage of DescribeStackResource.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackResource
 &StackName=MyStack
 &LogicalResourceId=MyDBInstance
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2011-07-08T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<DescribeStackResourceResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeStackResourceResult>
    <StackResourceDetail>
      <StackId>arn:aws:cloudformation:us-east-1:123456789:stack/MyStack/aaf549a0-a413-11df-adb3-5081b3858e83</StackId>
      <StackName>MyStack</StackName>
      <LogicalResourceId>MyDBInstance</LogicalResourceId>
      <PhysicalResourceId>MyStack_DB1</PhysicalResourceId>
      <ResourceType>AWS::RDS::DBInstance</ResourceType>
      <LastUpdatedTimestamp>2011-07-07T22:27:28Z</LastUpdatedTimestamp>
      <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
    </StackResourceDetail>
  </DescribeStackResourceResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</DescribeStackResourceResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackResource")
