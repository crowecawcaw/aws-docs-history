# GetBucketLoggingStatus (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 


 The `GetBucketLoggingStatus` retrieves the logging status for
 an existing bucket.
 


 For a general introduction to this feature, see [Server Logs](../userguide/ServerLogs.md "../userguide/ServerLogs.md").

 

###### Example

`Sample Request`


```
<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <soap:Body>
        <GetBucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">
          <Bucket>mybucket</Bucket>
          <AWSAccessKeyId>`YOUR_AWS_ACCESS_KEY_ID`</AWSAccessKeyId>
          <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
          <Signature>`YOUR_SIGNATURE_HERE`</Signature>
        </GetBucketLoggingStatus>
      </soap:Body>
    </soap:Envelope>
            
```
`Sample Response`


```
<?xml version="1.0" encoding="utf-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >
      <soapenv:Header>
      </soapenv:Header>
      <soapenv:Body>
        <GetBucketLoggingStatusResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
          <GetBucketLoggingStatusResponse>
            <LoggingEnabled>
              <TargetBucket>mylogs</TargetBucket>
              <TargetPrefix>mybucket-access_log-</TargetPrefix>
            </LoggingEnabled>
          </GetBucketLoggingStatusResponse>
        </GetBucketLoggingStatusResponse>
      </soapenv:Body>
    </soapenv:Envelope>
            
```
## Access Control


Only the owner of a bucket is permitted to invoke this operation.
