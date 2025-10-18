Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# ListFacetNames

Retrieves the names of facets that exist in a schema.


## Request Syntax



```
POST /amazonclouddirectory/2017-01-11/facet/list HTTP/1.1
x-amz-data-partition: `SchemaArn`
Content-type: application/json

{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[SchemaArn](#API_ListFacetNames_RequestSyntax "#API_ListFacetNames_RequestSyntax")**


The Amazon Resource Name (ARN) to retrieve facet names from.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[MaxResults](#API_ListFacetNames_RequestSyntax "#API_ListFacetNames_RequestSyntax")**


The maximum number of results to retrieve.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**[NextToken](#API_ListFacetNames_RequestSyntax "#API_ListFacetNames_RequestSyntax")**


The pagination token.


Type: String


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "FacetNames": [ "***string***" ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[FacetNames](#API_ListFacetNames_ResponseSyntax "#API_ListFacetNames_ResponseSyntax")**


The names of facets that exist within the schema.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `^[a-zA-Z0-9._-]*$`





**[NextToken](#API_ListFacetNames_ResponseSyntax "#API_ListFacetNames_ResponseSyntax")**


The pagination token.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**InvalidNextTokenException** 


Indicates that the `NextToken` value is not valid.


HTTP Status Code: 400




**LimitExceededException** 


Indicates that limits are exceeded. See [Limits](../developerguide/limits.md "../developerguide/limits.md") for more information.


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


This example illustrates one usage of ListFacetNames.



```
POST /amazonclouddirectory/2017-01-11/facet/list HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171017/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=e29fa5e564697e1912f34bd1d1437f78be8e8ebbd4f31fce6d300f5be5c814bd
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1
X-Amz-Date: 20171017T202730Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8


```

### Example Response


This example illustrates one usage of ListFacetNames.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 9a69f750-b379-11e7-bd9d-f9e3493b0666
Date: Tue, 17 Oct 2017 20:27:32 GMT
x-amzn-RequestId: 9a69f750-b379-11e7-bd9d-f9e3493b0666
Content-Type: application/json
Content-Length: 101

{
	"FacetNames": ["Legal_Entity", "Organization", "node1", "node2", "nodex", "policyfacet"],
	"NextToken": null
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListFacetNames")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListFacetNames "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListFacetNames")
