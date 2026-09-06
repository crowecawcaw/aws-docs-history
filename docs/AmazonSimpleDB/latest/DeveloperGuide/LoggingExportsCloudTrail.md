

# Log Amazon SimpleDB export calls with AWS CloudTrail
<a name="LoggingExportsCloudTrail"></a>

 Amazon SimpleDB integrates with AWS CloudTrail to provide comprehensive logging of export-related API calls. This integration helps you track who performed export operations, when they occurred, and what parameters were used. 

 AWS CloudTrail is an AWS service that helps you audit your AWS account. AWS CloudTrail is turned on for your AWS account when you create it. For more information about AWS CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/). All export-related Amazon SimpleDB actions are logged by AWS CloudTrail. AWS CloudTrail provides a record of actions related to an export taken by a user, role, or an AWS service in Amazon SimpleDB. 

 AWS CloudTrail captures export API calls for Amazon SimpleDB as events. An *event* represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. 

 The following example shows a AWS CloudTrail log entry that demonstrates the `StartDomainExport` action: 

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws::sts::111122223333:assumed-role/cloudtrail-test-role-iad/i-1234567890abcdef0",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws::iam::111122223333:role/cloudtrail-test-role-iad",
                "accountId": "111122223333",
                "userName": "cloudtrail-test-role-iad"
            },
            "attributes": {
                "creationDate": "2025-07-10T08:39:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-07-10T09:15:13Z",
    "eventSource": "sdb.amazonaws.com",
    "eventName": "StartDomainExport",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-cli/2.13.5",
    "requestParameters": {
        "clientToken": "59d2024d-5ae0-4fda-baf7-880222f29b7b",
        "domainName": "myProductionDomain",
        "s3Bucket": "my-export-bucket"
    },
    "responseElements": {
        "clientToken": "59d2024d-5ae0-4fda-baf7-880222f29b7b",
        "exportArn": "arn:aws::sdb:us-east-1:111122223333:domain/myProductionDomain/export/45abe2ef-87ca-4a59-9f9a-c176d12c0bf9",
        "requestedAt": "Jul 10, 2025, 9:15:13 AM"
    },
    "requestID": "ca2b69d4-3c2f-e8f8-be99-efe0d1f6675a",
    "eventID": "777f9823-07ba-4b8c-aa87-20985ffce95f",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::SDB::Domain",
            "ARN": "arn:aws::sdb:us-east-1:111122223333:domain/myProductionDomain"
        },
        {
            "accountId": "111122223333",
            "type": "AWS::SDB::Domain::DomainExport",
            "ARN": "arn:aws::sdb:us-east-1:111122223333:domain/myProductionDomain/export/45abe2ef-87ca-4a59-9f9a-c176d12c0bf9"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_256_GCM_SHA384",
        "clientProvidedHostHeader": "sdb.us-east-1.amazonaws.com"
    }
}
```

 Key elements in this AWS CloudTrail log entry include: 
+ *eventName*: The API action that was called (StartDomainExport)
+ *eventTime*: When the API call occurred
+ *userIdentity*: Information about the user or role that made the call
+ *requestParameters*: The parameters passed to the API call
+ *responseElements*: Key information returned by the API call