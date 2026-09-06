

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# ListSourceResources
<a name="API_ListSourceResources"></a>

Lists all the source resource that are associated with the specified `MigrationTaskName` and `ProgressUpdateStream`.

## Request Syntax
<a name="API_ListSourceResources_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MigrationTaskName": "{{string}}",
   "NextToken": "{{string}}",
   "ProgressUpdateStream": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSourceResources_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSourceResources_RequestSyntax) **   <a name="migrationhub-ListSourceResources-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the value that you specify here for `MaxResults`, the response will include a token that you can use to retrieve the next set of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: No

 ** [MigrationTaskName](#API_ListSourceResources_RequestSyntax) **   <a name="migrationhub-ListSourceResources-request-MigrationTaskName"></a>
A unique identifier that references the migration task. *Do not store confidential data in this field.*   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^:|]+`   
Required: Yes

 ** [NextToken](#API_ListSourceResources_RequestSyntax) **   <a name="migrationhub-ListSourceResources-request-NextToken"></a>
If `NextToken` was returned by a previous call, there are more results available. The value of `NextToken` is a unique pagination token for each page. To retrieve the next page of results, specify the `NextToken` value that the previous call returned. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`   
Required: No

 ** [ProgressUpdateStream](#API_ListSourceResources_RequestSyntax) **   <a name="migrationhub-ListSourceResources-request-ProgressUpdateStream"></a>
The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[^/:|\000-\037]+`   
Required: Yes

## Response Syntax
<a name="API_ListSourceResources_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SourceResourceList": [ 
      { 
         "Description": "string",
         "Name": "string",
         "StatusDetail": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSourceResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSourceResources_ResponseSyntax) **   <a name="migrationhub-ListSourceResources-response-NextToken"></a>
If the response includes a `NextToken` value, that means that there are more results available. The value of `NextToken` is a unique pagination token for each page. To retrieve the next page of results, call this API again and specify this `NextToken` value in the request. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$` 

 ** [SourceResourceList](#API_ListSourceResources_ResponseSyntax) **   <a name="migrationhub-ListSourceResources-response-SourceResourceList"></a>
The list of source resources.  
Type: Array of [SourceResource](API_SourceResource.md) objects

## Errors
<a name="API_ListSourceResources_Errors"></a>

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 400

 ** InternalServerError **   
Exception raised when an internal, configuration, or dependency error is encountered.  
HTTP Status Code: 500

 ** InvalidInputException **   
Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception raised when the request references a resource (Application Discovery Service configuration, update stream, migration task, etc.) that does not exist in Application Discovery Service (Application Discovery Service) or in Migration Hub's repository.  
HTTP Status Code: 400

 ** ServiceUnavailableException **   
Exception raised when there is an internal, configuration, or dependency error encountered.  
HTTP Status Code: 500

 ** ThrottlingException **   
The request was denied due to request throttling.    
 ** Message **   
A message that provides information about the exception.  
 ** RetryAfterSeconds **   
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

## See Also
<a name="API_ListSourceResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWSMigrationHub-2017-05-31/ListSourceResources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListSourceResources) 