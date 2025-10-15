# GetAccessPointPolicyForObjectLambda

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

###### Note

This operation is not supported by directory buckets.

Returns the resource policy for an Object Lambda Access Point.

The following actions are related to
 `GetAccessPointPolicyForObjectLambda`:


* [DeleteAccessPointPolicyForObjectLambda](API_control_DeleteAccessPointPolicyForObjectLambda.md "API_control_DeleteAccessPointPolicyForObjectLambda.md")
* [PutAccessPointPolicyForObjectLambda](API_control_PutAccessPointPolicyForObjectLambda.md "API_control_PutAccessPointPolicyForObjectLambda.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspointforobjectlambda/`name`/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax "#API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax")**


The name of the Object Lambda Access Point.


Length Constraints: Minimum length of 3. Maximum length of 45.


Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`



Required: Yes




**[x-amz-account-id](#API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax "#API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax")**


The account ID for the account that owns the specified Object Lambda Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessPointPolicyForObjectLambdaResult](#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-GetAccessPointPolicyForObjectLambdaResult "#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-GetAccessPointPolicyForObjectLambdaResult")>
   <[Policy](#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-Policy "#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-Policy")>***string***</[Policy](#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-Policy "#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-Policy")>
</[GetAccessPointPolicyForObjectLambdaResult](#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-GetAccessPointPolicyForObjectLambdaResult "#AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-GetAccessPointPolicyForObjectLambdaResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessPointPolicyForObjectLambdaResult](#API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax "#API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax")**


Root level tag for the GetAccessPointPolicyForObjectLambdaResult parameters.


Required: Yes




**[Policy](#API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax "#API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax")**


Object Lambda Access Point resource policy document.


Type: String




## Examples


### Sample resource policy


The following illustrates a sample resource policy.



```
{
    "Version" : "2008-10-17",		 	 	 
    "Statement":[{
        "Sid": "Grant account 123456789012 GetObject access",
        "Effect":"Allow",
        "Principal" : {
            "AWS": "arn:aws:iam::123456789012:root"
        },
        "Action":["s3-object-lambda:GetObject"],
        "Resource":["arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/my-object-lambda-ap"]
        },
        {
        "Sid": "Grant account 444455556666 GetObject access",
        "Effect":"Allow",
        "Principal" : {
            "AWS": "arn:aws:iam::444455556666:root"
        },
        "Action":["s3-object-lambda:GetObject"],
        "Resource":["arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/my-object-lambda-ap"]
        }
    ]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda")
