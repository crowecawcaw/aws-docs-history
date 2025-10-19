# ListTypes

Returns summary information about all extensions, including your private resource types,
 modules, and Hooks as well as all public extensions from AWS and third-party
 publishers.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**DeprecatedStatus** 


The deprecation status of the extension that you want to get summary information
 about.


Valid values include:



* `LIVE`: The extension is registered for use in CloudFormation
 operations.
* `DEPRECATED`: The extension has been deregistered and can no longer be used
 in CloudFormation operations.

Type: String


Valid Values: `LIVE | DEPRECATED`



Required: No




**Filters** 


Filter criteria to use in determining which extensions to return.


Filters must be compatible with `Visibility` to return valid results. For
 example, specifying `AWS_TYPES` for `Category` and `PRIVATE`
 for `Visibility` returns an empty list of types, but specifying `PUBLIC`
 for `Visibility` returns the desired list.


Type: [TypeFilters](API_TypeFilters.md "API_TypeFilters.md") object


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


If the previous paginated request didn't return all the remaining results, the response
 object's `NextToken` parameter value is set to a token. To retrieve the next set of
 results, call this action again and assign that token to the request object's
 `NextToken` parameter. If there are no remaining results, the previous response
 object's `NextToken` parameter is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ProvisioningType** 


For resource types, the provisioning behavior of the resource type. CloudFormation determines
 the provisioning type during registration, based on the types of handlers in the schema
 handler package submitted.


Valid values include:



* `FULLY_MUTABLE`: The resource type includes an update handler to process
 updates to the type during stack update operations.
* `IMMUTABLE`: The resource type doesn't include an update handler, so the
 type can't be updated and must instead be replaced during stack update operations.
* `NON_PROVISIONABLE`: The resource type doesn't include create, read, and
 delete handlers, and therefore can't actually be provisioned.

The default is `FULLY_MUTABLE`.


Type: String


Valid Values: `NON_PROVISIONABLE | IMMUTABLE | FULLY_MUTABLE`



Required: No




**Type** 


The type of extension.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**Visibility** 


The scope at which the extensions are visible and usable in CloudFormation operations.


Valid values include:



* `PRIVATE`: Extensions that are visible and usable within this account and
 Region. This includes:




	+ Private extensions you have registered in this account and Region.
	+ Public extensions that you have activated in this account and Region.
* `PUBLIC`: Extensions that are publicly visible and available to be
 activated within any AWS account. This includes extensions from AWS and third-party
 publishers.

The default is `PRIVATE`.


Type: String


Valid Values: `PUBLIC | PRIVATE`



Required: No




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all the remaining results, `NextToken` is set to
 a token. To retrieve the next set of results, call this action again and assign that token to
 the request object's `NextToken` parameter. If the request returns all results,
 `NextToken` is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**TypeSummaries.member.N**


A list of `TypeSummary` structures that contain information about the specified
 extensions.


Type: Array of [TypeSummary](API_TypeSummary.md "API_TypeSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




## Examples


### ListTypes


The following example returns summary information for all the private resource types
 registered in this AWS account.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListTypes
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191204T183443Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
  <ListTypesResult>
    <TypeSummaries>
      <member>
        <LastUpdated>2019-12-04T18:28:15.059Z</LastUpdated>
        <DefaultVersionId>00000003</DefaultVersionId>
        <TypeArn>arn:aws:cloudformation:us-east-1:012345678910:type/resource/My-Resource-Example</TypeArn>
        <TypeName>My::Resource::Example</TypeName>
        <Description>Resource schema for My::Resource::Example</Description>
        <Type>RESOURCE</Type>
      </member>
      <member>
        <LastUpdated>2019-12-04T18:28:15.059Z</LastUpdated>
        <DefaultVersionId>00000001</DefaultVersionId>
        <TypeArn>arn:aws:cloudformation:us-east-1:012345678910:type/resource/My-Second-Example</TypeArn>
        <TypeName>My::Second::Example</TypeName>
        <Description>Resource schema for My::Second::Example</Description>
        <Type>RESOURCE</Type>
      </member>
    </TypeSummaries>
  </ListTypesResult>
  <ResponseMetadata>
    <RequestId>69dc5a34-5462-4e1b-81fb-7a310example</RequestId>
  </ResponseMetadata>
</ListTypesResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListTypes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListTypes "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListTypes")
