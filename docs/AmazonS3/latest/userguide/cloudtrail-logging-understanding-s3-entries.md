# CloudTrail log file entries
 for Amazon S3 and S3 on Outposts

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3)
 as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no
 additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration 
 and for new object uploads is available in AWS CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header 
 in the AWS Command Line Interface and AWS SDKs. For more information, 
 see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

###### Note

To view CloudTrail log file examples for Amazon S3 Express One Zone, see [CloudTrail log file examples for S3 Express One Zone](s3-express-log-files.md "s3-express-log-files.md").

For more information, see the following examples.

###### Topics

* [Example: CloudTrail log file entry for
 Amazon S3](#example-ct-log-s3 "#example-ct-log-s3")

## Example: CloudTrail log file entry for
 Amazon S3


The following example shows a CloudTrail log entry that demonstrates the [GET Service](../API/RESTServiceGET.md "../API/RESTServiceGET.md"),
 [PutBucketAcl](../API/RESTBucketPUTacl.md "../API/RESTBucketPUTacl.md"), and [GetBucketVersioning](../API/RESTBucketGETversioningStatus.md "../API/RESTBucketGETversioningStatus.md") actions.



```
{
    "Records": [
    {
        "eventVersion": "1.03",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "`111122223333`",
            "arn": "arn:aws:iam::111122223333:user/`myUserName`",
            "accountId": "`111122223333`",
            "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
            "userName": "`myUserName`"
        },
        "eventTime": "2019-02-01T03:18:19Z",
        "eventSource": "s3.amazonaws.com",
        "eventName": "ListBuckets",
        "awsRegion": "`us-west-2`",
        "sourceIPAddress": "`127.0.0.1`",
        "userAgent": "[]",
        "requestParameters": {
            "host": [
                "s3.`us-west-2`.amazonaws.com"
            ]
        },
        "responseElements": null,
        "additionalEventData": {
            "SignatureVersion": "SigV2",
            "AuthenticationMethod": "QueryString",
            "aclRequired": "Yes"
    },
        "requestID": "47B8E8D397DCE7A6",
        "eventID": "cdc4b7ed-e171-4cef-975a-ad829d4123e8",
        "eventType": "AwsApiCall",
        "recipientAccountId": "`444455556666`",
        "tlsDetails": {
            "tlsVersion": "TLSv1.2",
            "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
            "clientProvidedHostHeader": "s3.amazonaws.com"
    }      
    },
    {
       "eventVersion": "1.03",
       "userIdentity": {
            "type": "IAMUser",
            "principalId": "`111122223333`",
            "arn": "arn:aws:iam::`111122223333`:user/`myUserName`",
            "accountId": "`111122223333`",
            "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
            "userName": "`myUserName`"
        },
      "eventTime": "2019-02-01T03:22:33Z",
      "eventSource": "s3.amazonaws.com",
      "eventName": "PutBucketAcl",
      "awsRegion": "`us-west-2`",
      "sourceIPAddress": "",
      "userAgent": "[]",
      "requestParameters": {
          "bucketName": "",
          "AccessControlPolicy": {
              "AccessControlList": {
                  "Grant": {
                      "Grantee": {
                          "xsi:type": "CanonicalUser",
                          "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                          "ID": "d25639fbe9c19cd30a4c0f43fbf00e2d3f96400a9aa8dabfbbebe1906Example"
                       },
                      "Permission": "FULL_CONTROL"
                   }
              },
              "xmlns": "http://s3.amazonaws.com/doc/2006-03-01/",
              "Owner": {
                  "ID": "d25639fbe9c19cd30a4c0f43fbf00e2d3f96400a9aa8dabfbbebe1906Example"
              }
          },
          "host": [
              "s3.`us-west-2`.amazonaws.com"
          ],
          "acl": [
              ""
          ]
      },
      "responseElements": null,
      "additionalEventData": {
          "SignatureVersion": "SigV4",
          "CipherSuite": "ECDHE-RSA-AES128-SHA",
          "AuthenticationMethod": "AuthHeader"
      },
      "requestID": "BD8798EACDD16751",
      "eventID": "607b9532-1423-41c7-b048-ec2641693c47",
      "eventType": "AwsApiCall",
      "recipientAccountId": "`111122223333`",
      "tlsDetails": {
            "tlsVersion": "TLSv1.2",
            "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
            "clientProvidedHostHeader": "s3.amazonaws.com"
    }              
    },
    {
      "eventVersion": "1.03",
      "userIdentity": {
          "type": "IAMUser",
          "principalId": "`111122223333`",
          "arn": "arn:aws:iam::`111122223333`:user/`myUserName`",
          "accountId": "`111122223333`",
          "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
          "userName": "`myUserName`"
        },
      "eventTime": "2019-02-01T03:26:37Z",
      "eventSource": "s3.amazonaws.com",
      "eventName": "GetBucketVersioning",
      "awsRegion": "`us-west-2`",
      "sourceIPAddress": "",
      "userAgent": "[]",
      "requestParameters": {
          "host": [
              "s3.u`s-west-2`.amazonaws.com"
          ],
          "bucketName": "`amzn-s3-demo-bucket1`",
          "versioning": [
              ""
          ]
      },
      "responseElements": null,
      "additionalEventData": {
          "SignatureVersion": "SigV4",
          "CipherSuite": "ECDHE-RSA-AES128-SHA",
          "AuthenticationMethod": "AuthHeader"
    },
      "requestID": "07D681279BD94AED",
      "eventID": "f2b287f3-0df1-4961-a2f4-c4bdfed47657",
      "eventType": "AwsApiCall",
      "recipientAccountId": "`111122223333`",
      "tlsDetails": {
            "tlsVersion": "TLSv1.2",
            "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
            "clientProvidedHostHeader": "s3.amazonaws.com"
    }                 
    }
  ]
}
```
