# GetManagedCertificateDetails

Gets details about the CloudFront managed ACM certificate.


## Request Syntax



```
GET /2020-05-31/managed-certificate/`Identifier` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Identifier](#API_GetManagedCertificateDetails_RequestSyntax "#API_GetManagedCertificateDetails_RequestSyntax")**


The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ManagedCertificateDetails>
   <CertificateArn>***string***</CertificateArn>
   <CertificateStatus>***string***</CertificateStatus>
   <ValidationTokenDetails>
      <ValidationTokenDetail>
         <Domain>***string***</Domain>
         <RedirectFrom>***string***</RedirectFrom>
         <RedirectTo>***string***</RedirectTo>
      </ValidationTokenDetail>
   </ValidationTokenDetails>
   <ValidationTokenHost>***string***</ValidationTokenHost>
</ManagedCertificateDetails>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ManagedCertificateDetails](#API_GetManagedCertificateDetails_ResponseSyntax "#API_GetManagedCertificateDetails_ResponseSyntax")**


Root level tag for the ManagedCertificateDetails parameters.


Required: Yes




**[CertificateArn](#API_GetManagedCertificateDetails_ResponseSyntax "#API_GetManagedCertificateDetails_ResponseSyntax")**


The ARN of the CloudFront managed ACM certificate.


Type: String




**[CertificateStatus](#API_GetManagedCertificateDetails_ResponseSyntax "#API_GetManagedCertificateDetails_ResponseSyntax")**


The status of the CloudFront managed ACM certificate.


###### Note

Your distribution tenant will be updated with the latest certificate status. When calling the [UpdateDistributionTenant](API_UpdateDistributionTenant.md "API_UpdateDistributionTenant.md") operation, use the latest value for the `ETag`.


Type: String


Valid Values: `pending-validation | issued | inactive | expired | validation-timed-out | revoked | failed`





**[ValidationTokenDetails](#API_GetManagedCertificateDetails_ResponseSyntax "#API_GetManagedCertificateDetails_ResponseSyntax")**


Contains details about the validation token of the specified CloudFront managed ACM certificate.


Type: Array of [ValidationTokenDetail](API_ValidationTokenDetail.md "API_ValidationTokenDetail.md") objects




**[ValidationTokenHost](#API_GetManagedCertificateDetails_ResponseSyntax "#API_GetManagedCertificateDetails_ResponseSyntax")**


Contains details about the validation token host of the specified CloudFront managed ACM certificate.



* For `cloudfront`, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.
* For `self-hosted`, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.

###### Note

This setting only affects the initial certificate request. Once the DNS points to CloudFront, all future certificate renewals are automatically handled through CloudFront.


Type: String


Valid Values: `cloudfront | self-hosted`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetManagedCertificateDetails")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetManagedCertificateDetails")
