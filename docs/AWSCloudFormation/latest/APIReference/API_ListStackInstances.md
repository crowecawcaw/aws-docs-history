# ListStackInstances

Returns summary information about stack instances that are associated with the specified
 StackSet. You can filter for stack instances that are associated with a specific AWS account
 name or Region, or that have a specific status.


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




**Filters.member.N**


The filter to apply to stack instances


Type: Array of [StackInstanceFilter](API_StackInstanceFilter.md "API_StackInstanceFilter.md") objects


Array Members: Maximum number of 3 items.


Required: No




**MaxResults** 


The maximum number of results to be returned with a single call. If the number of
 available results exceeds this maximum, the response includes a `NextToken` value
 that you can assign to the `NextToken` request parameter to get the next set of
 results.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


If the previous request didn't return all the remaining results, the response's
 `NextToken` parameter value is set to a token. To retrieve the next set of
 results, call `ListStackInstances` again and assign that token to the request
 object's `NextToken` parameter. If there are no remaining results, the previous
 response object's `NextToken` parameter is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackInstanceAccount** 


The name of the AWS account that you want to list stack instances for.


Type: String


Pattern: `^[0-9]{12}$`



Required: No




**StackInstanceRegion** 


The name of the Region where you want to list stack instances.


Type: String


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: No




**StackSetName** 


The name or unique ID of the StackSet that you want to list stack instances for.


Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all the remaining results, `NextToken` is set to
 a token. To retrieve the next set of results, call `ListStackInstances` again and
 assign that token to the request object's `NextToken` parameter. If the request
 returns all results, `NextToken` is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**Summaries.member.N**


A list of `StackInstanceSummary` structures that contain information about the
 specified stack instances.


Type: Array of [StackInstanceSummary](API_StackInstanceSummary.md "API_StackInstanceSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




## Examples


### ListStackInstances


The following example returns summary information about the stack instances associated
 with the specified StackSet in the specified account.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListStackInstances
 &StackInstanceAccount=012345678910
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &MaxResults=10
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<ListStackInstancesResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <ListStackInstancesResult>
    <Summaries>
      <member>
        <DriftStatus>IN_SYNC</DriftStatus>
        <StackSetId>stack-set-example:45331555-4b18-45a1-aa43-ecf5example</StackSetId>
        <StackId>arn:aws:cloudformation:ap-northeast-2:012345678910:stack/StackSet-stack-set-example-0ca3eed7-0b67-4be7-8a71-828641fa5193/ea68eca0-f9c1-11e9-aac0-0example</StackId>
        <Region>ap-northeast-2</Region>
        <Account>012345678910</Account>
        <LastDriftCheckTimestamp>2019-12-03T20:01:04.511Z</LastDriftCheckTimestamp>
        <Status>CURRENT</Status>
      </member>
      <member>
        <DriftStatus>IN_SYNC</DriftStatus>
        <StackSetId>stack-set-example:45331555-4b18-45a1-aa43-ecf5example</StackSetId>
        <StackId>arn:aws:cloudformation:eu-west-2:012345678910:stack/StackSet-stack-set-example-da07ae82-0478-485e-a32f-c1cb8cec57c2/e0df84a0-f9c1-11e9-bb3e-06afexamplec</StackId>
        <Region>eu-west-2</Region>
        <Account>012345678910</Account>
        <LastDriftCheckTimestamp>2019-12-03T19:59:14.488Z</LastDriftCheckTimestamp>
        <Status>CURRENT</Status>
      </member>
      <member>
        <DriftStatus>IN_SYNC</DriftStatus>
        <StackSetId>stack-set-example:45331555-4b18-45a1-aa43-ecf5example</StackSetId>
        <StackId>arn:aws:cloudformation:us-east-1:012345678910:stack/StackSet-stack-set-example-35588cf5-396d-4469-8a9e-912214ce3a7a/c684ff40-f9c1-11e9-b738-1245bexample</StackId>
        <Region>us-east-1</Region>
        <Account>012345678910</Account>
        <LastDriftCheckTimestamp>2019-12-03T19:58:37.477Z</LastDriftCheckTimestamp>
        <Status>CURRENT</Status>
      </member>
      <member>
        <DriftStatus>IN_SYNC</DriftStatus>
        <StackSetId>stack-set-example:45331555-4b18-45a1-aa43-ecf5example</StackSetId>
        <StackId>arn:aws:cloudformation:us-east-2:012345678910:stack/StackSet-stack-set-example-d3db3374-7683-4e82-bdeb-c388d7b16dc9/d8c208b0-f9c1-11e9-81c9-02300example</StackId>
        <Region>us-east-2</Region>
        <Account>012345678910</Account>
        <LastDriftCheckTimestamp>2019-12-03T20:00:27.570Z</LastDriftCheckTimestamp>
        <Status>CURRENT</Status>
      </member>
      <member>
        <DriftStatus>IN_SYNC</DriftStatus>
        <StackSetId>stack-set-example:45331555-4b18-45a1-aa43-ecf5example</StackSetId>
        <StackId>arn:aws:cloudformation:us-west-2:012345678910:stack/StackSet-stack-set-example-05f9348f-3f6e-4051-9083-8663c59f0352/cffefdf0-f9c1-11e9-a552-02ca0example</StackId>
        <Region>us-west-2</Region>
        <Account>012345678910</Account>
        <LastDriftCheckTimestamp>2019-12-03T19:59:51.501Z</LastDriftCheckTimestamp>
        <Status>CURRENT</Status>
      </member>
    </Summaries>
  </ListStackInstancesResult>
  <ResponseMetadata>
    <RequestId>6a94faf0-5632-4618-9c0a-cf273example</RequestId>
  </ResponseMetadata>
</ListStackInstancesResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackInstances")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackInstances "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackInstances")
