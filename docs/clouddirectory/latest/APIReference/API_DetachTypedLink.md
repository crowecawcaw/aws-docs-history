Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# DetachTypedLink

Detaches a typed link from a specified source and target object. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/typedlink/detach HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "TypedLinkSpecifier": { 
      "IdentityAttributeValues": [ 
         { 
            "AttributeName": "`string`",
            "Value": { 
               "BinaryValue": `blob`,
               "BooleanValue": `boolean`,
               "DatetimeValue": `number`,
               "NumberValue": "`string`",
               "StringValue": "`string`"
            }
         }
      ],
      "SourceObjectReference": { 
         "Selector": "`string`"
      },
      "TargetObjectReference": { 
         "Selector": "`string`"
      },
      "TypedLinkFacet": { 
         "SchemaArn": "`string`",
         "TypedLinkName": "`string`"
      }
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_DetachTypedLink_RequestSyntax "#API_DetachTypedLink_RequestSyntax")**


The Amazon Resource Name (ARN) of the directory where you want to detach the typed
 link.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[TypedLinkSpecifier](#API_DetachTypedLink_RequestSyntax "#API_DetachTypedLink_RequestSyntax")**


Used to accept a typed link specifier as input.


Type: [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md") object


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




**FacetValidationException** 


The [Facet](API_Facet.md "API_Facet.md") that you provided was not well formed or could not be
 validated with the schema.


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


This example illustrates one usage of DetachTypedLink.



```
PUT /amazonclouddirectory/2017-01-11/typedlink/detach HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 459
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170927/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=f2b55a0895ed644a5acfa07e793f5b2d25166c91c5f3be765004cd0b1c1613c1
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20170927T191638Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"TypedLinkSpecifier": {
		"SourceObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA"
		},
		"IdentityAttributeValues": [{
			"AttributeName": "22",
			"Value": {
				"BinaryValue": "c3Ry"
			}
		}],
		"TargetObjectReference": {
			"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
		},
		"TypedLinkFacet": {
			"TypedLinkName": "exampletypedlink8",
			"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1"
		}
	}
}
```

### Example Response


This example illustrates one usage of DetachTypedLink.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 6340a418-a3b8-11e7-8502-0566a31305cf
Date: Wed, 27 Sep 2017 19:16:38 GMT
x-amzn-RequestId: 6340a418-a3b8-11e7-8502-0566a31305cf
Content-Type: application/json
Content-Length: 0

```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/DetachTypedLink")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/DetachTypedLink "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/DetachTypedLink")
