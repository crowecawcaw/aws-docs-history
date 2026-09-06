

# Appendix: SOAP API
<a name="APISoap"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

This section describes the SOAP API with respect to service, bucket, and object operations. Note that SOAP requests, both authenticated and anonymous, must be sent to Amazon S3 using SSL. Amazon S3 returns an error when you send a SOAP request over HTTP.

The latest Amazon S3 WSDL is available at [docs.aws.amazon.com/2006-03-01/AmazonS3.wsdl](https://doc.s3.amazonaws.com/2006-03-01/AmazonS3.wsdl).

**Topics**
+ [Operations on the Service (SOAP API)](SOAPServiceOps.md)
+ [Operations on Buckets (SOAP API)](SOAPBucketsOps.md)
+ [Operations on Objects (SOAP API)](SOAPObjectsOps.md)
+ [Authenticating SOAP requests](SOAPAuthentication.md)
+ [Setting access policy with SOAP](SOAPAccessPolicy.md)
+ [Common elements](#SOAPCommon)
+ [SOAP Error Responses](SOAPErrorResponses.md)

## Common elements
<a name="SOAPCommon"></a>

You can include the following authorization-related elements with any SOAP request:
+ `AWSAccessKeyId:` The AWS Access Key ID of the requester
+ `Timestamp:` The current time on your system
+ `Signature:` The signature for the request