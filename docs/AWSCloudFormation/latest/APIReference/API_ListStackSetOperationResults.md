# ListStackSetOperationResults

Returns summary information about the results of a StackSet operation.

###### Note

This API provides *eventually consistent* reads meaning it may take
 some time but will eventually return the most up-to-date data.


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


The filter to apply to operation results.


Type: Array of [OperationResultFilter](API_OperationResultFilter.md "API_OperationResultFilter.md") objects


Array Members: Maximum number of 1 item.


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


If the previous request didn't return all the remaining results, the response object's
 `NextToken` parameter value is set to a token. To retrieve the next set of
 results, call `ListStackSetOperationResults` again and assign that token to the
 request object's `NextToken` parameter. If there are no remaining results, the
 previous response object's `NextToken` parameter is set to
 `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**OperationId** 


The ID of the StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: Yes




**StackSetName** 


The name or unique ID of the StackSet that you want to get operation results for.


Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all results, `NextToken` is set to a token. To
 retrieve the next set of results, call `ListOperationResults` again and assign that
 token to the request object's `NextToken` parameter. If there are no remaining
 results, `NextToken` is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**Summaries.member.N**


A list of `StackSetOperationResultSummary` structures that contain information
 about the specified operation results, for accounts and AWS Regions that are included in the
 operation.


Type: Array of [StackSetOperationResultSummary](API_StackSetOperationResultSummary.md "API_StackSetOperationResultSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**OperationNotFound** 


The specified ID refers to an operation that doesn't exist.


HTTP Status Code: 404




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




## Examples


### ListStackSetOperationResults


This example illustrates one usage of ListStackSetOperationResults.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListStackSetOperationResults
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &OperationId=61806005-bde9-46f1-949d-6791example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<ListStackSetOperationResultsResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <ListStackSetOperationResultsResult>
    <Summaries>
      <member>
        <StatusReason>Cancelled since failure tolerance has exceeded</StatusReason>
        <Region>us-west-2</Region>
        <Account>[account]</Account>
        <Status>CANCELLED</Status>
      </member>
      <member>
        <AccountGateResult>
          <StatusReason>Account [account] should have 'AWSCloudFormationStackSetAdministrationRole' role with trust relationship to CloudFormation service.</StatusReason>
          <Status>FAILED</Status>
        </AccountGateResult>
        <StatusReason>Account [account] should have 'AWSCloudFormationStackSetAdministrationRole' role with trust relationship to CloudFormation service.</StatusReason>
        <Region>us-east-1</Region>
        <Account>[account]</Account>
        <Status>FAILED</Status>
      </member>
    </Summaries>
  </ListStackSetOperationResultsResult>
  <ResponseMetadata>
    <RequestId>bf662a8d-7e1b-11e7-98fb-db38example</RequestId>
  </ResponseMetadata>
</ListStackSetOperationResultsResponse>
```

### ListStackSetOperationResults


This example illustrates one usage of ListStackSetOperationResults.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListStackSetOperationResults
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &OperationId=61806005-bde9-46f1-949d-6791example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<ListStackSetOperationResultsResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <ListStackSetOperationResultsResult>
    <Summaries>
      <member>
        <AccountGateResult>
          <StatusReason>AWSCloudFormationStackSetAccountGate function not found</StatusReason>
          <Status>SKIPPED</Status>
        </AccountGateResult>
        <Region>us-west-2</Region>
        <Account>[account]</Account>
        <Status>SUCCEEDED</Status>
      </member>
      <member>
        <AccountGateResult>
          <StatusReason>AWSCloudFormationStackSetAccountGate function not found</StatusReason>
          <Status>SKIPPED</Status>
        </AccountGateResult>
        <Region>us-east-1</Region>
        <Account>[account]</Account>
        <Status>SUCCEEDED</Status>
      </member>
    </Summaries>
  </ListStackSetOperationResultsResult>
  <ResponseMetadata>
    <RequestId>ee444e6b-7e1b-11e7-8bb3-1f65example</RequestId>
  </ResponseMetadata>
</ListStackSetOperationResultsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackSetOperationResults")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackSetOperationResults "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackSetOperationResults")
