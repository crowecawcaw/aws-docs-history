# TestFunction

Tests a CloudFront function.

To test a function, you provide an *event object* that represents
 an HTTP request or response that your CloudFront distribution could receive in production.
 CloudFront runs the function, passing it the event object that you provided, and returns the
 function's result (the modified event object) in the response. The response also
 contains function logs and error messages, if any exist. For more information about
 testing functions, see [Testing functions](../../../AmazonCloudFront/latest/DeveloperGuide/managing-functions.md#test-function "../../../AmazonCloudFront/latest/DeveloperGuide/managing-functions.md#test-function") in the *Amazon CloudFront Developer Guide*.

To test a function, you provide the function's name and version (`ETag`
 value) along with the event object. To get the function's name and version, you can use
 `ListFunctions` and `DescribeFunction`.


## Request Syntax



```
POST /2020-05-31/function/`Name`/test HTTP/1.1
If-Match: `IfMatch`
<?xml version="1.0" encoding="UTF-8"?>
<TestFunctionRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <EventObject>`blob`</EventObject>
   <Stage>`string`</Stage>
</TestFunctionRequest>
```

## URI Request Parameters


The request uses the following URI parameters.





**[If-Match](#API_TestFunction_RequestSyntax "#API_TestFunction_RequestSyntax")**


The current version (`ETag` value) of the function that you are testing,
 which you can get using `DescribeFunction`.


Required: Yes




**[Name](#API_TestFunction_RequestSyntax "#API_TestFunction_RequestSyntax")**


The name of the function that you are testing.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[TestFunctionRequest](#API_TestFunction_RequestSyntax "#API_TestFunction_RequestSyntax")**


Root level tag for the TestFunctionRequest parameters.


Required: Yes




**[EventObject](#API_TestFunction_RequestSyntax "#API_TestFunction_RequestSyntax")**


The event object to test the function with. For more information about the structure
 of the event object, see [Testing functions](../../../AmazonCloudFront/latest/DeveloperGuide/managing-functions.md#test-function "../../../AmazonCloudFront/latest/DeveloperGuide/managing-functions.md#test-function") in the *Amazon CloudFront Developer Guide*.


Type: Base64-encoded binary data object


Length Constraints: Minimum length of 0. Maximum length of 40960.


Required: Yes




**[Stage](#API_TestFunction_RequestSyntax "#API_TestFunction_RequestSyntax")**


The stage of the function that you are testing, either `DEVELOPMENT` or
 `LIVE`.


Type: String


Valid Values: `DEVELOPMENT | LIVE`



Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<TestResult>
   <ComputeUtilization>***string***</ComputeUtilization>
   <FunctionErrorMessage>***string***</FunctionErrorMessage>
   <FunctionExecutionLogs>
      <member>***string***</member>
   </FunctionExecutionLogs>
   <FunctionOutput>***string***</FunctionOutput>
   <FunctionSummary>
      <FunctionConfig>
         <Comment>***string***</Comment>
         <KeyValueStoreAssociations>
            <Items>
               <KeyValueStoreAssociation>
                  <KeyValueStoreARN>***string***</KeyValueStoreARN>
               </KeyValueStoreAssociation>
            </Items>
            <Quantity>***integer***</Quantity>
         </KeyValueStoreAssociations>
         <Runtime>***string***</Runtime>
      </FunctionConfig>
      <FunctionMetadata>
         <CreatedTime>***timestamp***</CreatedTime>
         <FunctionARN>***string***</FunctionARN>
         <LastModifiedTime>***timestamp***</LastModifiedTime>
         <Stage>***string***</Stage>
      </FunctionMetadata>
      <Name>***string***</Name>
      <Status>***string***</Status>
   </FunctionSummary>
</TestResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[TestResult](#API_TestFunction_ResponseSyntax "#API_TestFunction_ResponseSyntax")**


Root level tag for the TestResult parameters.


Required: Yes




**[ComputeUtilization](#API_TestFunction_ResponseSyntax "#API_TestFunction_ResponseSyntax")**


The amount of time that the function took to run as a percentage of the maximum
 allowed time. For example, a compute utilization of 35 means that the function completed
 in 35% of the maximum allowed time.


Type: String




**[FunctionErrorMessage](#API_TestFunction_ResponseSyntax "#API_TestFunction_ResponseSyntax")**


If the result of testing the function was an error, this field contains the error
 message.


Type: String




**[FunctionExecutionLogs](#API_TestFunction_ResponseSyntax "#API_TestFunction_ResponseSyntax")**


Contains the log lines that the function wrote (if any) when running the test.


Type: Array of strings




**[FunctionOutput](#API_TestFunction_ResponseSyntax "#API_TestFunction_ResponseSyntax")**


The event object returned by the function. For more information about the structure of
 the event object, see [Event
 object structure](../../../AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.md "../../../AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.md") in the *Amazon CloudFront Developer Guide*.


Type: String




**[FunctionSummary](#API_TestFunction_ResponseSyntax "#API_TestFunction_ResponseSyntax")**


Contains configuration information and metadata about the CloudFront function that was
 tested.


Type: [FunctionSummary](API_FunctionSummary.md "API_FunctionSummary.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**NoSuchFunctionExists** 


The function does not exist.


HTTP Status Code: 404




**TestFunctionFailed** 


The CloudFront function failed.


HTTP Status Code: 500




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/TestFunction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TestFunction "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TestFunction")
