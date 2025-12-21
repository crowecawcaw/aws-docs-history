# AwsS3 resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsS3` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsS3AccessPoint

`AwsS3AccessPoint` provides information about an Amazon S3 access point. S3 access points are named network
endpoints that are attached to S3 buckets that you can use to perform S3 object operations.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsS3AccessPoint` object. To view descriptions of
`AwsS3AccessPoint` attributes, see [AwsS3AccessPointDetails](../../1.0/APIReference/API_AwsS3AccessPointDetails.md "../../1.0/APIReference/API_AwsS3AccessPointDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsS3AccessPoint": {
        "AccessPointArn": "arn:aws:s3:us-east-1:123456789012:accesspoint/asff-access-point",
        "Alias": "asff-access-point-hrzrlukc5m36ft7okagglf3gmwluquse1b-s3alias",
        "Bucket": "amzn-s3-demo-bucket",
        "BucketAccountId": "123456789012",
        "Name": "asff-access-point",
        "NetworkOrigin": "VPC",
        "PublicAccessBlockConfiguration": {
            "BlockPublicAcls": true,
            "BlockPublicPolicy": true,
            "IgnorePublicAcls": true,
            "RestrictPublicBuckets": true
        },
        "VpcConfiguration": {
            "VpcId": "vpc-1a2b3c4d5e6f1a2b3"
        }
}
```

## AwsS3AccountPublicAccessBlock

`AwsS3AccountPublicAccessBlock` provides information about the Amazon S3 Public
Access Block configuration for accounts.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsS3AccountPublicAccessBlock` object. To view descriptions of
`AwsS3AccountPublicAccessBlock` attributes, see [AwsS3AccountPublicAccessBlockDetails](../../1.0/APIReference/API_AwsS3AccountPublicAccessBlockDetails.md "../../1.0/APIReference/API_AwsS3AccountPublicAccessBlockDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsS3AccountPublicAccessBlock": {
    "BlockPublicAcls": true,
    "BlockPublicPolicy": true,
    "IgnorePublicAcls": false,
    "RestrictPublicBuckets": true
}
```

## AwsS3Bucket

The `AwsS3Bucket` object provides details about an Amazon S3 bucket.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsS3Bucket` object. To view descriptions of `AwsS3Bucket`
attributes, see [AwsS3BucketDetails](../../1.0/APIReference/API_AwsS3BucketDetails.md "../../1.0/APIReference/API_AwsS3BucketDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsS3Bucket": {
    "AccessControlList": "{\"grantSet\":null,\"grantList\":[{\"grantee\":{\"id\":\"4df55416215956920d9d056aa8b99803a294ea221222bb668b55a8c6bca81094\",\"displayName\":null},\"permission\":\"FullControl\"},{\"grantee\":\"AllUsers\",\"permission\":\"ReadAcp\"},{\"grantee\":\"AuthenticatedUsers\",\"permission\":\"ReadAcp\"}",,
    "BucketLifecycleConfiguration": {
       "Rules": [
           {
               "AbortIncompleteMultipartUpload": {
                   "DaysAfterInitiation": 5
               },
               "ExpirationDate": "2021-11-10T00:00:00.000Z",
               "ExpirationInDays": 365,
               "ExpiredObjectDeleteMarker": false,
               "Filter": {
                   "Predicate": {
                       "Operands": [
                           {
                               "Prefix": "tmp/",
                               "Type": "LifecyclePrefixPredicate"
                           },
                           {
                               "Tag": {
                                   "Key": "ArchiveAge",
                                   "Value": "9m"
                               },
                               "Type": "LifecycleTagPredicate"
                           }
                       ],
                       "Type": "LifecycleAndOperator"
                   }
               },
               "ID": "Move rotated logs to Glacier",
               "NoncurrentVersionExpirationInDays": -1,
               "NoncurrentVersionTransitions": [
                   {
                       "Days": 2,
                       "StorageClass": "GLACIER"
                   }
               ],
               "Prefix": "rotated/",
               "Status": "Enabled",
               "Transitions": [
                   {
                       "Date": "2020-11-10T00:00:00.000Z",
                       "Days": 100,
                       "StorageClass": "GLACIER"
                   }
               ]
           }
       ]
    },
    "BucketLoggingConfiguration": {
    	"DestinationBucketName": "s3serversideloggingbucket-123456789012",
    	"LogFilePrefix": "buckettestreadwrite23435/"
    },
    "BucketName": "amzn-s3-demo-bucket",
    "BucketNotificationConfiguration": {
    	"Configurations": [{
    		"Destination": "arn:aws:lambda:us-east-1:123456789012:function:s3_public_write",
    		"Events": [
    			"s3:ObjectCreated:Put"
    		],
    		"Filter": {
    			"S3KeyFilter": {
    				"FilterRules": [
    				{
    					"Name": "AffS3BucketNotificationConfigurationS3KeyFilterRuleName.PREFIX",
    					"Value": "pre"
    				},
    				{
    					"Name": "AffS3BucketNotificationConfigurationS3KeyFilterRuleName.SUFFIX",
    					"Value": "suf"
    				},
    				]
    			}
    		},
    		"Type": "LambdaConfiguration"
    	}]
    },
    "BucketVersioningConfiguration": {
    	"IsMfaDeleteEnabled": true,
    	"Status": "Off"
    },
    "BucketWebsiteConfiguration": {
    	"ErrorDocument": "error.html",
    	"IndexDocumentSuffix": "index.html",
    	"RedirectAllRequestsTo": {
    		"HostName": "example.com",
    		"Protocol": "http"
    	},
    	"RoutingRules": [{
    		"Condition": {
    			"HttpErrorCodeReturnedEquals": "Redirected",
    			"KeyPrefixEquals": "index"
    					},
    		"Redirect": {
    			"HostName": "example.com",
    			"HttpRedirectCode": "401",
    			"Protocol": "HTTP",
    			"ReplaceKeyPrefixWith": "string",
    			"ReplaceKeyWith": "string"
    		}
    	}]
    },
    "CreatedAt": "2007-11-30T01:46:56.000Z",
    "ObjectLockConfiguration": {
    	"ObjectLockEnabled": "Enabled",
    	"Rule": {
    		"DefaultRetention": {
    			"Days": null,
    			"Mode": "GOVERNANCE",
    			"Years": 12
    		},
    	},
    },
    "OwnerId": "AIDACKCEVSQ6C2EXAMPLE",
    "OwnerName": "s3bucketowner",
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "BlockPublicPolicy": true,
        "IgnorePublicAcls": true,
        "RestrictPublicBuckets": true,
    },
    "ServerSideEncryptionConfiguration": {
        "Rules": [
            {
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "AES256",
                    "KMSMasterKeyID": "12345678-abcd-abcd-abcd-123456789012"
                }
            }
        ]
     }
}
```

## AwsS3Object

The `AwsS3Object` object provides information about an Amazon S3 object.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsS3Object` object. To view descriptions of `AwsS3Object`
attributes, see [AwsS3ObjectDetails](../../1.0/APIReference/API_AwsS3ObjectDetails.md "../../1.0/APIReference/API_AwsS3ObjectDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsS3Object": {
    "ContentType": "text/html",
    "ETag": "\"30a6ec7e1a9ad79c203d05a589c8b400\"",
    "LastModified": "2012-04-23T18:25:43.511Z",
    "ServerSideEncryption": "aws:kms",
    "SSEKMSKeyId": "arn:aws:kms:us-west-2:123456789012:key/4dff8393-e225-4793-a9a0-608ec069e5a7",
    "VersionId": "ws31OurgOOjH_HHllIxPE35P.MELYaYh"
}
```
