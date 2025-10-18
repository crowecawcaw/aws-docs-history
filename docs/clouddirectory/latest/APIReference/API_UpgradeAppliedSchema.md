Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# UpgradeAppliedSchema

Upgrades a single directory in-place using the `PublishedSchemaArn` with schema updates found in `MinorVersion`. Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory. Note: This is a synchronous API call and upgrades only one schema on a given directory per call. To upgrade multiple directories from one schema, you would need to call this API on each directory.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/schema/upgradeapplied HTTP/1.1
Content-type: application/json

{
   "DirectoryArn": "`string`",
   "DryRun": `boolean`,
   "PublishedSchemaArn": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[DirectoryArn](#API_UpgradeAppliedSchema_RequestSyntax "#API_UpgradeAppliedSchema_RequestSyntax")**


The ARN for the directory to which the upgraded schema will be applied.


Type: String


Required: Yes




**[DryRun](#API_UpgradeAppliedSchema_RequestSyntax "#API_UpgradeAppliedSchema_RequestSyntax")**


Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional.


Type: Boolean


Required: No




**[PublishedSchemaArn](#API_UpgradeAppliedSchema_RequestSyntax "#API_UpgradeAppliedSchema_RequestSyntax")**


The revision of the published schema to upgrade the directory to.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "DirectoryArn": "***string***",
   "UpgradedSchemaArn": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[DirectoryArn](#API_UpgradeAppliedSchema_ResponseSyntax "#API_UpgradeAppliedSchema_ResponseSyntax")**


The ARN of the directory that is returned as part of the response.


Type: String




**[UpgradedSchemaArn](#API_UpgradeAppliedSchema_ResponseSyntax "#API_UpgradeAppliedSchema_ResponseSyntax")**


The ARN of the upgraded schema that is returned as part of the response.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**IncompatibleSchemaException** 


Indicates a failure occurred while performing a check for backward compatibility between the specified schema and the schema that is currently applied to the directory.


HTTP Status Code: 400




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**InvalidAttachmentException** 


Indicates that an attempt to make an attachment was invalid. For example, attaching two nodes 
 with a link type that is not applicable to the nodes or attempting to apply a schema to a directory a second time.


HTTP Status Code: 400




**ResourceNotFoundException** 


The specified resource could not be found.


HTTP Status Code: 404




**RetryableConflictException** 


Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.


HTTP Status Code: 409




**SchemaAlreadyExistsException** 


Indicates that a schema could not be created due to a naming conflict. Please select a
 different name and then try again.


HTTP Status Code: 400




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/UpgradeAppliedSchema")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/UpgradeAppliedSchema "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/UpgradeAppliedSchema")
