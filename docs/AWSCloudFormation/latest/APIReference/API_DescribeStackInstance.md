# DescribeStackInstance

Returns the stack instance that's associated with the specified StackSet, AWS account,
 and AWS Region.

For a list of stack instances that are associated with a specific StackSet, use [ListStackInstances](API_ListStackInstances.md "API_ListStackInstances.md").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**CallAs** 


[Service-managed permissions] Specifies whether you are acting as an account administrator
 in the organization's management account or as a delegated administrator in a
 member account.


By default, `SELF` is specified. Use `SELF` for StackSets with
 self-managed permissions.



* If you are signed in to the management account, specify
 `SELF`.
* If you are signed in to a delegated administrator account, specify
 `DELEGATED_ADMIN`.


Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a
 delegated administrator](../UserGuide/stacksets-orgs-delegated-admin.md "../UserGuide/stacksets-orgs-delegated-admin.md") in the *AWS CloudFormation User Guide*.

Type: String


Valid Values: `SELF | DELEGATED_ADMIN`



Required: No




**StackInstanceAccount** 


The ID of an AWS account that's associated with this stack instance.


Type: String


Pattern: `^[0-9]{12}$`



Required: Yes




**StackInstanceRegion** 


The name of a Region that's associated with this stack instance.


Type: String


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: Yes




**StackSetName** 


The name or the unique stack ID of the StackSet that you want to get stack instance
 information for.


Type: String


Required: Yes




## Response Elements


The following element is returned by the service.





**StackInstance** 


The stack instance that matches the specified request parameters.


Type: [StackInstance](API_StackInstance.md "API_StackInstance.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**StackInstanceNotFound** 


The specified stack instance doesn't exist.


HTTP Status Code: 404




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




## Examples


### DescribeStackInstance


This example illustrates one usage of DescribeStackInstance.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackInstance
 &StackInstanceRegion=ap-northeast-2
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &StackInstanceAccount=012345678910
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<DescribeStackInstanceResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DescribeStackInstanceResult>
    <StackInstance>
      <DriftStatus>IN_SYNC</DriftStatus>
      <StackSetId>stack-set-example:45331555-4b18-45a1-aa43-ecf5example</StackSetId>
      <StackId>arn:aws:cloudformation:ap-northeast-2:012345678910:stack/StackSet-stack-set-example-0ca3eed7-0b67-4be7-8a71-828641fa5193/ea68eca0-f9c1-11e9-aac0-0aaexample</StackId>
      <ParameterOverrides/>
      <Region>ap-northeast-2</Region>
      <Account>012345678910</Account>
      <LastDriftCheckTimestamp>2019-12-03T20:01:04.511Z</LastDriftCheckTimestamp>
      <Status>CURRENT</Status>
    </StackInstance>
  </DescribeStackInstanceResult>
  <ResponseMetadata>
    <RequestId>afc959f5-a87c-4e16-95a9-ca25example</RequestId>
  </ResponseMetadata>
</DescribeStackInstanceResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackInstance")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackInstance "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackInstance")
