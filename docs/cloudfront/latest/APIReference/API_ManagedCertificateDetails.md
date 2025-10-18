# ManagedCertificateDetails

Contains details about the CloudFront managed ACM certificate.


## Contents





**CertificateArn** 


The ARN of the CloudFront managed ACM certificate.


Type: String


Required: No




**CertificateStatus** 


The status of the CloudFront managed ACM certificate.


###### Note

Your distribution tenant will be updated with the latest certificate status. When calling the [UpdateDistributionTenant](API_UpdateDistributionTenant.md "API_UpdateDistributionTenant.md") operation, use the latest value for the `ETag`.


Type: String


Valid Values: `pending-validation | issued | inactive | expired | validation-timed-out | revoked | failed`



Required: No




**ValidationTokenDetails** 


Contains details about the validation token of the specified CloudFront managed ACM certificate.


Type: Array of [ValidationTokenDetail](API_ValidationTokenDetail.md "API_ValidationTokenDetail.md") objects


Required: No




**ValidationTokenHost** 


Contains details about the validation token host of the specified CloudFront managed ACM certificate.



* For `cloudfront`, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.
* For `self-hosted`, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.

###### Note

This setting only affects the initial certificate request. Once the DNS points to CloudFront, all future certificate renewals are automatically handled through CloudFront.


Type: String


Valid Values: `cloudfront | self-hosted`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ManagedCertificateDetails")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ManagedCertificateDetails")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ManagedCertificateDetails "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ManagedCertificateDetails")
