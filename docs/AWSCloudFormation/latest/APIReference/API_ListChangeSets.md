# ListChangeSets

Returns the ID and status of each active change set for a stack. For example, CloudFormation
 lists change sets that are in the `CREATE_IN_PROGRESS` or
 `CREATE_PENDING` state.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**NextToken** 


A string (provided by the [ListChangeSets](API_ListChangeSets.md "API_ListChangeSets.md") response output) that
 identifies the next page of change sets that you want to retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackName** 


The name or the Amazon Resource Name (ARN) of the stack for which you want to list change
 sets.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the output exceeds 1 MB, a string that identifies the next page of change sets. If
 there is no additional page, this value is `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**Summaries.member.N**


A list of `ChangeSetSummary` structures that provides the ID and status of each
 change set for the specified stack.


Type: Array of [ChangeSetSummary](API_ChangeSetSummary.md "API_ChangeSetSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### ListChangeSets


This example illustrates one usage of ListChangeSets.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListChangeSets
 &StackName=arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<ListChangeSetsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListChangeSetsResult>
    <Summaries>
      <member>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <Status>CREATE_COMPLETE</Status>
        <ChangeSetId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ChangeSetId>
        <StackName>SampleStack</StackName>
        <CreationTime>2016-03-16T20:44:05.889Z</CreationTime>
        <ChangeSetName>SampleChangeSet</ChangeSetName>
      </member>
      <member>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <Status>CREATE_COMPLETE</Status>
        <ChangeSetId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet-conditional/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ChangeSetId>
        <StackName>SampleStack</StackName>
        <CreationTime>2016-03-16T21:15:56.398Z</CreationTime>
        <ChangeSetName>SampleChangeSet-conditional</ChangeSetName>
      </member>
      <member>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <Status>CREATE_COMPLETE</Status>
        <ChangeSetId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet-replacement/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ChangeSetId>
        <StackName>SampleStack</StackName>
        <CreationTime>2016-03-16T21:03:37.706Z</CreationTime>
        <ChangeSetName>SampleChangeSet-replacement</ChangeSetName>
      </member>
    </Summaries>
  </ListChangeSetsResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</ListChangeSetsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListChangeSets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListChangeSets "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListChangeSets")
