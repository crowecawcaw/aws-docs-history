Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# AttachPolicy

Attaches a policy object to a regular object. An object can have a limited number of attached
 policies.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/policy/attach HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "ObjectReference": { 
      "Selector": "`string`"
   },
   "PolicyReference": { 
      "Selector": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_AttachPolicy_RequestSyntax "#API_AttachPolicy_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md")
 where both objects reside. For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ObjectReference](#API_AttachPolicy_RequestSyntax "#API_AttachPolicy_RequestSyntax")**


The reference that identifies the object to which the policy will be
 attached.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**[PolicyReference](#API_AttachPolicy_RequestSyntax "#API_AttachPolicy_RequestSyntax")**


The reference that is associated with the policy object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**DirectoryNotEnabledException** 


Operations are only permitted on enabled directories.


HTTP Status Code: 400




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**LimitExceededException** 


Indicates that limits are exceeded. See [Limits](../developerguide/limits.md "../developerguide/limits.md") for more information.


HTTP Status Code: 400




**NotPolicyException** 


Indicates that the requested operation can only operate on policy objects.


HTTP Status Code: 400




**ResourceNotFoundException** 


The specified resource could not be found.


HTTP Status Code: 404




**RetryableConflictException** 


Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.


HTTP Status Code: 409




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## Examples


The following examples are formatted for legibility.


### Example Request


This example illustrates one usage of AttachPolicy.



```
PUT /amazonclouddirectory/2017-01-11/policy/attach HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 168
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171017/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=d6ba55fbae53295150b69a92946e542ad08f7557492c5862d70d6a8c62fa24b0
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171017T185436Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"PolicyReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWgcBsTVmcQEWs6jlygfhuew"
	},
	"ObjectReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWQoovm1s3Ts2v0NKrzdVnPw"
	}
}
```

### Example Response


This example illustrates one usage of AttachPolicy.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 9ff9d709-b36c-11e7-843e-9fad359f817f
Date: Tue, 17 Oct 2017 18:54:37 GMT
x-amzn-RequestId: 9ff9d709-b36c-11e7-843e-9fad359f817f
Content-Type: application/json
Content-Length: 2

{}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/AttachPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/AttachPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/AttachPolicy")
