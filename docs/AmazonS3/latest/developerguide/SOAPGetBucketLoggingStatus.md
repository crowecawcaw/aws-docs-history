

# GetBucketLoggingStatus (SOAP API)
<a name="SOAPGetBucketLoggingStatus"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

 The `GetBucketLoggingStatus` retrieves the logging status for an existing bucket. 

 For a general introduction to this feature, see [Server Logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html). 

**Example**  
`Sample Request`  

```
 1. <?xml version="1.0" encoding="utf-8"?>
 2.     <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
 3.       <soap:Body>
 4.         <GetBucketLoggingStatus xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 5.           <Bucket>mybucket</Bucket>
 6.           <AWSAccessKeyId>{{YOUR_AWS_ACCESS_KEY_ID}}</AWSAccessKeyId>
 7.           <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
 8.           <Signature>{{YOUR_SIGNATURE_HERE}}</Signature>
 9.         </GetBucketLoggingStatus>
10.       </soap:Body>
11.     </soap:Envelope>
```
`Sample Response`  

```
 1. <?xml version="1.0" encoding="utf-8"?>
 2.     <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >
 3.       <soapenv:Header>
 4.       </soapenv:Header>
 5.       <soapenv:Body>
 6.         <GetBucketLoggingStatusResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
 7.           <GetBucketLoggingStatusResponse>
 8.             <LoggingEnabled>
 9.               <TargetBucket>mylogs</TargetBucket>
10.               <TargetPrefix>mybucket-access_log-</TargetPrefix>
11.             </LoggingEnabled>
12.           </GetBucketLoggingStatusResponse>
13.         </GetBucketLoggingStatusResponse>
14.       </soapenv:Body>
15.     </soapenv:Envelope>
```

## Access Control
<a name="SOAPGetBucketLoggingStatusAccessControl"></a>

Only the owner of a bucket is permitted to invoke this operation.