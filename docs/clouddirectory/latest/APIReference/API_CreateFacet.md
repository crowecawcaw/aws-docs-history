Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# CreateFacet

Creates a new [Facet](API_Facet.md "API_Facet.md") in a schema. Facet creation is allowed only
 in development or applied schemas.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/facet/create HTTP/1.1
x-amz-data-partition: `SchemaArn`
Content-type: application/json

{
   "Attributes": [ 
      { 
         "AttributeDefinition": { 
            "DefaultValue": { 
               "BinaryValue": `blob`,
               "BooleanValue": `boolean`,
               "DatetimeValue": `number`,
               "NumberValue": "`string`",
               "StringValue": "`string`"
            },
            "IsImmutable": `boolean`,
            "Rules": { 
               "`string`" : { 
                  "Parameters": { 
                     "`string`" : "`string`" 
                  },
                  "Type": "`string`"
               }
            },
            "Type": "`string`"
         },
         "AttributeReference": { 
            "TargetAttributeName": "`string`",
            "TargetFacetName": "`string`"
         },
         "Name": "`string`",
         "RequiredBehavior": "`string`"
      }
   ],
   "FacetStyle": "`string`",
   "Name": "`string`",
   "ObjectType": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[SchemaArn](#API_CreateFacet_RequestSyntax "#API_CreateFacet_RequestSyntax")**


The schema ARN in which the new [Facet](API_Facet.md "API_Facet.md") will be created. For more
 information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Attributes](#API_CreateFacet_RequestSyntax "#API_CreateFacet_RequestSyntax")**


The attributes that are associated with the [Facet](API_Facet.md "API_Facet.md").


Type: Array of [FacetAttribute](API_FacetAttribute.md "API_FacetAttribute.md") objects


Required: No




**[FacetStyle](#API_CreateFacet_RequestSyntax "#API_CreateFacet_RequestSyntax")**


There are two different styles that you can define on any given facet, `Static` and `Dynamic`. For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.


Type: String


Valid Values: `STATIC | DYNAMIC`



Required: No




**[Name](#API_CreateFacet_RequestSyntax "#API_CreateFacet_RequestSyntax")**


The name of the [Facet](API_Facet.md "API_Facet.md"), which is unique for a given schema.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `^[a-zA-Z0-9._-]*$`



Required: Yes




**[ObjectType](#API_CreateFacet_RequestSyntax "#API_CreateFacet_RequestSyntax")**


Specifies whether a given object created from this facet is of type node, leaf node,
 policy or index.



* Node: Can have multiple children but one parent.


* Leaf node: Cannot have children but can have multiple parents.


* Policy: Allows you to store a policy document and policy type. For more
 information, see [Policies](../developerguide/key_concepts_directory.md#key_concepts_policies "../developerguide/key_concepts_directory.md#key_concepts_policies").


* Index: Can be created with the Index API.

Type: String


Valid Values: `NODE | LEAF_NODE | POLICY | INDEX`



Required: No




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




**FacetAlreadyExistsException** 


A facet with the same name already exists.


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




**InvalidRuleException** 


Occurs when any of the rule parameter keys or values are invalid.


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


This example illustrates one usage of CreateFacet.



```
PUT /amazonclouddirectory/2017-01-11/facet/create HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 39
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170922/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=d6b41d921e64be7413abf9bd9036289cb34ace20275ed17dee45e594622ced4b
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1
X-Amz-Date: 20170922T214008Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"Name": "node1",
	"ObjectType": "NODE"
}
```

### Example Response


This example illustrates one usage of CreateFacet.



```
HTTP/1.1 200 OK
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Date: Thu, 22 Sep 2017 00:35:44 GMT
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Content-Type: application/json
Content-Length: 521

{}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateFacet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateFacet "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateFacet")
