

# Appendix: Authenticating requests (AWS signature version 2)
<a name="Appendix-Sigv2"></a>

**Important**  
This section describes how to authenticate requests using AWS Signature Version 2. Signature Version 2 is being turned off (deprecated), Amazon S3 will only accept API requests that are signed using Signature Version 4. For more information, see [AWS Signature Version 2 turned off (deprecated) for Amazon S3](specify-signature-version.md#UsingAWSSDK-sig2-deprecation)   
Signature Version 4 is supported in all AWS Regions, and it is the only version that is supported for new Regions. For more information, see [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon Simple Storage Service API Reference*.   
Amazon S3 offers you the ability to identify what API signature version was used to sign a request. It is important to identify if any of your workflows are utilizing Signature Version 2 signing and upgrading them to use Signature Version 4 to prevent impact to your business.   
If you are using CloudTrail event logs(recommended option), please see [Identifying Amazon S3 Signature Version 2 requests by using CloudTrail ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-request-identification.html#cloudtrail-identification-sigv2-requests) on how to query and identify such requests. 
If you are using the Amazon S3 Server Access logs, see [Using Amazon S3 server access logs to identify requests ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-s3-access-logs-to-identify-requests.html) 

**Topics**
+ [Authenticating requests using the REST API (AWS signature version 2)](S3_Authentication2.md)
+ [Signing and authenticating REST requests (AWS signature version 2)](RESTAuthentication.md)
+ [Browser-based uploads using POST (AWS signature version 2)](UsingHTTPPOST.md)