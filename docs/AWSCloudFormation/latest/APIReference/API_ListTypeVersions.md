# ListTypeVersions

Returns summary information about the versions of an extension.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Arn** 


The Amazon Resource Name (ARN) of the extension for which you want version summary
 information.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**DeprecatedStatus** 


The deprecation status of the extension versions that you want to get summary information
 about.


Valid values include:



* `LIVE`: The extension version is registered and can be used in CloudFormation
 operations, dependent on its provisioning behavior and visibility scope.
* `DEPRECATED`: The extension version has been deregistered and can no longer
 be used in CloudFormation operations.

The default is `LIVE`.


Type: String


Valid Values: `LIVE | DEPRECATED`



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
 results, call this action again and assign that token to the request object's
 `NextToken` parameter. If there are no remaining results, the previous response
 object's `NextToken` parameter is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**PublisherId** 


The publisher ID of the extension publisher.


Extensions published by Amazon aren't assigned a publisher ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`



Required: No




**Type** 


The kind of the extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension for which you want version summary information.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all of the remaining results, `NextToken` is set
 to a token. To retrieve the next set of results, call this action again and assign that token
 to the request object's `NextToken` parameter. If the request returns all results,
 `NextToken` is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**TypeVersionSummaries.member.N**


A list of `TypeVersionSummary` structures that contain information about the
 specified extension's versions.


Type: Array of [TypeVersionSummary](API_TypeVersionSummary.md "API_TypeVersionSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




## Examples


### ListTypeRegistrations


The following example returns summary information about the two extension versions
 with a status of `LIVE` for the private resource type
 `My::Resource::Example`.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListTypeRegistrations
 &Version=2010-05-15
 &TypeName=My::Resource::Example
 &Type=RESOURCE
 &DeprecatedStatus=LIVE
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191204T070338Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<ListTypeVersionsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListTypeVersionsResult>
    <TypeVersionSummaries>
      <member>
        <VersionId>00000001</VersionId>
        <TypeName>My::Resource::Example</TypeName>
        <Description>Resource schema for My::Resource::Example</Description>
        <TimeCreated>2019-12-03T23:29:33.321Z</TimeCreated>
        <Arn>arn:aws:cloudformation:us-east-1:012345678910:type/resource/My-Resource-Example/00000001</Arn>
        <Type>RESOURCE</Type>
      </member>
      <member>
        <VersionId>00000002</VersionId>
        <TypeName>My::Resource::Example</TypeName>
        <Description>Resource schema for My::Resource::Example</Description>
        <TimeCreated>2019-12-04T06:58:14.902Z</TimeCreated>
        <Arn>arn:aws:cloudformation:us-east-1:012345678910:type/resource/My-Resource-Example/00000002</Arn>
        <Type>RESOURCE</Type>
      </member>
    </TypeVersionSummaries>
  </ListTypeVersionsResult>
  <ResponseMetadata>
    <RequestId>caedd974-e865-4518-b7f0-a6972example</RequestId>
  </ResponseMetadata>
</ListTypeVersionsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListTypeVersions")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListTypeVersions "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListTypeVersions")
