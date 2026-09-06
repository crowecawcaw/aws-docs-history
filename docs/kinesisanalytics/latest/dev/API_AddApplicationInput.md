

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# AddApplicationInput
<a name="API_AddApplicationInput"></a>

**Note**  
This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see [Amazon Kinesis Data Analytics API V2 Documentation](/kinesisanalytics/latest/apiv2/Welcome.html).

 Adds a streaming source to your Amazon Kinesis application. For conceptual information, see [Configuring Application Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html). 

You can add a streaming source either when you create an application or you can use this operation to add a streaming source after you create an application. For more information, see [CreateApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CreateApplication.html).

Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to find the current application version. 

This operation requires permissions to perform the `kinesisanalytics:AddApplicationInput` action.

## Request Syntax
<a name="API_AddApplicationInput_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "Input": { 
      "InputParallelism": { 
         "Count": {{number}}
      },
      "InputProcessingConfiguration": { 
         "InputLambdaProcessor": { 
            "ResourceARN": "{{string}}",
            "RoleARN": "{{string}}"
         }
      },
      "InputSchema": { 
         "RecordColumns": [ 
            { 
               "Mapping": "{{string}}",
               "Name": "{{string}}",
               "SqlType": "{{string}}"
            }
         ],
         "RecordEncoding": "{{string}}",
         "RecordFormat": { 
            "MappingParameters": { 
               "CSVMappingParameters": { 
                  "RecordColumnDelimiter": "{{string}}",
                  "RecordRowDelimiter": "{{string}}"
               },
               "JSONMappingParameters": { 
                  "RecordRowPath": "{{string}}"
               }
            },
            "RecordFormatType": "{{string}}"
         }
      },
      "KinesisFirehoseInput": { 
         "ResourceARN": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "KinesisStreamsInput": { 
         "ResourceARN": "{{string}}",
         "RoleARN": "{{string}}"
      },
      "NamePrefix": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AddApplicationInput_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationInput_RequestSyntax) **   <a name="analytics-AddApplicationInput-request-ApplicationName"></a>
Name of your existing Amazon Kinesis Analytics application to which you want to add the streaming source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: Yes

 ** [CurrentApplicationVersionId](#API_AddApplicationInput_RequestSyntax) **   <a name="analytics-AddApplicationInput-request-CurrentApplicationVersionId"></a>
Current version of your Amazon Kinesis Analytics application. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to find the current application version.  
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 999999999.  
Required: Yes

 ** [Input](#API_AddApplicationInput_RequestSyntax) **   <a name="analytics-AddApplicationInput-request-Input"></a>
The [Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Input.html) to add.  
Type: [Input](API_Input.md) object  
Required: Yes

## Response Elements
<a name="API_AddApplicationInput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddApplicationInput_Errors"></a>

 ** CodeValidationException **   
User-provided application code (query) is invalid. This can be a simple syntax error.    
 ** message **   
Test
HTTP Status Code: 400

 ** ConcurrentModificationException **   
Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.    
 ** message **   

HTTP Status Code: 400

 ** InvalidArgumentException **   
Specified input parameter value is invalid.    
 ** message **   

HTTP Status Code: 400

 ** ResourceInUseException **   
Application is not available for this operation.    
 ** message **   

HTTP Status Code: 400

 ** ResourceNotFoundException **   
Specified application can't be found.    
 ** message **   

HTTP Status Code: 400

 ** UnsupportedOperationException **   
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.   
HTTP Status Code: 400

## See Also
<a name="API_AddApplicationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalytics-2015-08-14/AddApplicationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationInput) 