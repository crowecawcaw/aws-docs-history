# ListTypeRegistrations

Returns a list of registration tokens for the specified extension(s).


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





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




**RegistrationStatusFilter** 


The current status of the extension registration request.


The default is `IN_PROGRESS`.


Type: String


Valid Values: `COMPLETE | IN_PROGRESS | FAILED`



Required: No




**Type** 


The kind of extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeArn** 


The Amazon Resource Name (ARN) of the extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**TypeName** 


The name of the extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



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




**RegistrationTokenList.member.N**


A list of extension registration tokens.


Use [DescribeTypeRegistration](API_DescribeTypeRegistration.md "API_DescribeTypeRegistration.md") to return detailed information about a type
 registration request.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




## Examples


### ListTypeRegistrations


The example below returns a list of the registration tokens for the three versions of
 `My::Resource::Example`, a private resource type, that have completed
 registration.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListTypeRegistrations
 &Version=2010-05-15
 &TypeName=My::Resource::Example
 &Type=RESOURCE
 &RegistrationStatusFilter=COMPLETE
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191204T071759Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<ListTypeRegistrationsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListTypeRegistrationsResult>
    <RegistrationTokenList>
      <member>b5c40e0e-68da-47d2-8ed2-b8db7example</member>
      <member>03458954-61b1-44e9-90d8-f1b8aexample</member>
      <member>356b9e72-7d1e-43aa-83ba-81c2example</member>
    </RegistrationTokenList>
  </ListTypeRegistrationsResult>
  <ResponseMetadata>
    <RequestId>de6b93f6-c68b-4840-9537-eb2357example</RequestId>
  </ResponseMetadata>
</ListTypeRegistrationsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListTypeRegistrations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListTypeRegistrations "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListTypeRegistrations")
