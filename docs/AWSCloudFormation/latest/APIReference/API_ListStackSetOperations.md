# ListStackSetOperations

Returns summary information about operations performed on a StackSet.

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




**MaxResults** 


The maximum number of results to be returned with a single call. If the number of
 available results exceeds this maximum, the response includes a `NextToken` value
 that you can assign to the `NextToken` request parameter to get the next set of
 results.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


If the previous paginated request didn't return all of the remaining results, the response
 object's `NextToken` parameter value is set to a token. To retrieve the next set of
 results, call `ListStackSetOperations` again and assign that token to the request
 object's `NextToken` parameter. If there are no remaining results, the previous
 response object's `NextToken` parameter is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackSetName** 


The name or unique ID of the StackSet that you want to get operation summaries for.


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


A list of `StackSetOperationSummary` structures that contain summary
 information about operations for the specified StackSet.


Type: Array of [StackSetOperationSummary](API_StackSetOperationSummary.md "API_StackSetOperationSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




## Examples


### ListStackSetOperations


This example illustrates one usage of ListStackSetOperations.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListStackSetOperations
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

<ListStackSetOperationsResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <ListStackSetOperationsResult>
    <Summaries>
       <member>
        <CreationTimestamp>2019-12-03T19:57:57.573Z</CreationTimestamp>
        <OperationId>9cc082fa-df4c-45cd-b9a8-7e563e88418e</OperationId>
        <Action>DETECT_DRIFT</Action>
        <EndTimestamp>2019-12-03T20:01:04.630Z</EndTimestamp>
        <Status>SUCCEEDED</Status>
      </member>
      <member>
        <CreationTimestamp>2017-08-04T18:01:29.508Z</CreationTimestamp>
        <OperationId>ddf16f54-ad62-4d9b-b0ab-3ed8example</OperationId>
        <Action>UPDATE</Action>
        <EndTimestamp>2017-08-04T18:03:43.672Z</EndTimestamp>
        <Status>SUCCEEDED</Status>
      </member>
      <member>
        <CreationTimestamp>2017-08-04T17:40:05.828Z</CreationTimestamp>
        <OperationId>fadffcdd-4ae1-4a26-aa02-cb81example</OperationId>
        <Action>CREATE</Action>
        <EndTimestamp>2017-08-04T17:40:24.107Z</EndTimestamp>
        <Status>FAILED</Status>
      </member>
    </Summaries>
  </ListStackSetOperationsResult>
  <ResponseMetadata>
    <RequestId>39602b0c-7e1b-11e7-a79f-5d957example</RequestId>
  </ResponseMetadata>
</ListStackSetOperationsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackSetOperations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackSetOperations "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackSetOperations")
