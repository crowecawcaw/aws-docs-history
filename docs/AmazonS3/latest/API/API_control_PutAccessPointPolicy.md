# PutAccessPointPolicy

Associates an access policy with the specified access point. Each access point can have only one policy,
 so a request made to this API replaces any existing policy associated with the specified
 access point.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_PutAccessPointPolicy.md#API_control_PutAccessPointPolicy_Examples "API_control_PutAccessPointPolicy.md#API_control_PutAccessPointPolicy_Examples") section.

The following actions are related to `PutAccessPointPolicy`:


* [GetAccessPointPolicy](API_control_GetAccessPointPolicy.md "API_control_GetAccessPointPolicy.md")
* [DeleteAccessPointPolicy](API_control_DeleteAccessPointPolicy.md "API_control_DeleteAccessPointPolicy.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/accesspoint/`name`/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[PutAccessPointPolicyRequest](#AmazonS3-control_PutAccessPointPolicy-request-PutAccessPointPolicyRequest "#AmazonS3-control_PutAccessPointPolicy-request-PutAccessPointPolicyRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Policy](#AmazonS3-control_PutAccessPointPolicy-request-Policy "#AmazonS3-control_PutAccessPointPolicy-request-Policy")>`string`</[Policy](#AmazonS3-control_PutAccessPointPolicy-request-Policy "#AmazonS3-control_PutAccessPointPolicy-request-Policy")>
</[PutAccessPointPolicyRequest](#AmazonS3-control_PutAccessPointPolicy-request-PutAccessPointPolicyRequest "#AmazonS3-control_PutAccessPointPolicy-request-PutAccessPointPolicyRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_PutAccessPointPolicy_RequestSyntax "#API_control_PutAccessPointPolicy_RequestSyntax")**


The name of the access point that you want to associate with the specified policy.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the access point accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name>`. For example, to access the access point `reports-ap` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_PutAccessPointPolicy_RequestSyntax "#API_control_PutAccessPointPolicy_RequestSyntax")**


The AWS account ID for owner of the bucket associated with the specified access point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[PutAccessPointPolicyRequest](#API_control_PutAccessPointPolicy_RequestSyntax "#API_control_PutAccessPointPolicy_RequestSyntax")**


Root level tag for the PutAccessPointPolicyRequest parameters.


Required: Yes




**[Policy](#API_control_PutAccessPointPolicy_RequestSyntax "#API_control_PutAccessPointPolicy_RequestSyntax")**


The policy that you want to apply to the specified access point. For more information about access point
 policies, see [Managing data access with Amazon S3
 access points](../userguide/access-points.md "../userguide/access-points.md") or [Managing access to
 shared datasets in directory buckets with access points](../userguide/access-points-directory-buckets.md "../userguide/access-points-directory-buckets.md") in the
 *Amazon S3 User Guide*.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample request syntax for the PutAccessPointPolicy action for Amazon S3 on Outposts
 access point


This example illustrates one usage of PutAccessPointPolicy.



```

           PUT /v20180820/accesspoint/example-access-point/policy HTTP/1.1
           Host: s3-outposts.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2020 22:32:00 GMT
           Authorization: authorization string
           x-amz-account-id: example-account-id
           x-amz-outpost-id: op-01ac5d28a6a232904
           <?xml version="1.0" encoding="UTF-8"?>
               <PutAccessPointPolicyRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
                  <Policy>
{
   "Version":"2012-10-17",		 	 	 
   "Id":"AccessPointPolicy-for-example-access-point",
   "Statement":[
      {
         "Sid":"st1",
         "Effect":"Allow",
         "Principal":{
            "AWS":"example-account-id"
         },
         "Action":"s3-outposts:*",
         "Resource":"arn:aws:s3-outposts:your-Region:example-account-id:outpost/op-01ac5d28a6a232904/accesspoint/example-access-point
      }
   ]
}
                  </Policy>
               </PutAccessPointPolicyRequest>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointPolicy")
