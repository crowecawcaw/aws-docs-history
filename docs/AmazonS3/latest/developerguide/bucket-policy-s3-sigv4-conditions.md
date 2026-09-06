

# Amazon S3 Signature Version 4 Authentication Specific Policy Keys
<a name="bucket-policy-s3-sigv4-conditions"></a>

The following table shows the policy keys related Amazon S3 Signature Version 4 authentication that can be in Amazon S3 policies. In a bucket policy, you can add these conditions to enforce specific behavior when requests are authenticated by using Signature Version 4. For example policies, see [Bucket policy examples using Signature Version 4 related condition keys](#bucket-policy-sig-v4-condition-key-example). 


| Applicable Keys | Description | 
| --- | --- | 
| `s3:signatureversion` | Identifies the version of AWS Signature that you want to support for authenticated requests. For authenticated requests, Amazon S3 supports both Signature Version 4 and Signature Version 2. You can add this condition in your bucket policy to require a specific signature version.<br />Valid values: <br />`"AWS"` identifies Signature Version 2 <br /> `"AWS4-HMAC-SHA256"` identifies Signature Version 4 | 
| `s3:authType` | Amazon S3 supports various methods of authentication (see [Authenticating Requests (AWS Signature Version 4)](sig-v4-authenticating-requests.md). You can optionally use this condition key to restrict incoming requests to use a specific authentication method. For example, you can allow only the HTTP `Authorization` header to be used in request authentication. <br />Valid values: <br />`REST-HEADER` <br />`REST-QUERY-STRING` <br />`POST` <br />  | 
| `s3:signatureAge` | The length of time, in milliseconds, that a signature is valid in an authenticated request.<br />This condition works for:+ *Presigned URLs* — where the most restrictive condition wins. For more information, see [Working with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html).<br />+ *Presigned POST* — upload files directly to S3 using pre-signed POST. For more information, see [Amazon S3 POST Policy](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html).<br />In Signature Version 2, this value is always set to 0. <br />In Signature Version 4, the signing key is valid for up to seven days. Therefore, the signatures are also valid for up to seven days. You can use this condition to further limit the signature age. For more information, see [Introduction to Signing Requests](sig-v4-authenticating-requests.md#signing-request-intro).<br />Example value: `100` | 
| `s3:x-amz-content-sha256` | You can use this condition key to disallow unsigned content in your bucket.<br />When you use Signature Version 4, for requests that use the `Authorization` header, you add the `x-amz-content-sha256` header in the signature calculation and then set its value to the hash payload. Note that this condition key doesn't support the `x-amz-content-sha256` header as a query string parameter.<br />You can use this condition key in your bucket policy to deny any uploads where payloads are not signed. For example, you can deny uploads that use the `Authorization` header to authenticate requests but don't sign the payload. For more information, see [Signature Calculations for the Authorization Header: Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md).<br />Valid value: `UNSIGNED-PAYLOAD` | 

## Bucket policy examples using Signature Version 4 related condition keys
<a name="bucket-policy-sig-v4-condition-key-example"></a>

The following bucket policy denies any Amazon S3 presigned URL request on objects in `examplebucket` if the signature is more than ten minutes old. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Sid": "Deny a presigned URL request if the signature is more than 10 min old",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "s3:*",
         "Resource": "arn:aws:s3:::examplebucket3/*",
         "Condition": {
            "NumericGreaterThan": {
               "s3:signatureAge": 600000
            }
         }
      }
   ]
}
```

------

The following bucket policy allows only requests that use the `Authorization` header for request authentication. Any POST or presigned URL requests will be denied.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
         {
               "Sid": "Allow only requests that use Authorization header for request authentication. Deny POST or presigned URL requests.",
               "Effect": "Deny",
               "Principal": "*",
               "Action": "s3:*",
               "Resource": "arn:aws:s3:::examplebucket3/*",
               "Condition": {
                     "StringNotEquals": {
                           "s3:authType": "REST-HEADER"
                     }
               }
         }
   ]
}
```

------

The following bucket policy denies requests that use presigned URLS for request authentication:

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"DenyUploadsUsingPresignedURL",
         "Effect":"Deny",
         "Principal":"*",
         "Action":"s3:*",
         "Resource":"arn:aws:s3:::amzn-s3-demo-bucket1/*",
         "Condition":{
            "StringEquals":{
               "s3:authType":"{{REST-query-string}}"
            }
         }
      }
   ]
}
```

------

The following bucket policy denies any uploads with unsigned payloads:

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
         {
               "Sid": "Deny uploads with unsigned payloads that use the Authorization header.",
               "Effect": "Deny",
               "Principal": "*",
               "Action": "s3:*",
               "Resource": "arn:aws:s3:::examplebucket3/*",
               "Condition": {
                     "StringEquals": {
                           "s3:x-amz-content-sha256": "UNSIGNED-PAYLOAD"
                     }
               }
         }
   ]
}
```

------