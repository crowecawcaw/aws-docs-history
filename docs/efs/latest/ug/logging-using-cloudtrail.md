# Logging Amazon EFS API calls with AWS CloudTrail

Amazon EFS is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Amazon EFS. CloudTrail captures all API calls for
Amazon EFS as events, including calls from the Amazon EFS console and from code calls to
Amazon EFS API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for Amazon EFS. If you don't configure a trail, you can still view the most
recent events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Amazon EFS, the IP address
from which the request was made, who made the request, when it was made, and additional details.

For more information, see the [What is AWS CloudTrail?](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") in the _AWS CloudTrail User Guide_.

## Amazon EFS information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Amazon EFS, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Working with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon EFS,
create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you
create a trail in the console, the trail applies to all AWS Regions. The trail logs events from
all AWS Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you
specify. Additionally, you can configure other AWS services to further analyze and act upon the
event data collected in CloudTrail logs. For more information, see the following topics in the
_AWS CloudTrail User Guide:_

- [Creating
  a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS service integrations with CloudTrail logs](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Amazon EFS [Amazon EFS API](api-reference.md "api-reference.md") are logged by CloudTrail. For
example, calls to the `CreateFileSystem`, `CreateMountTarget` and
`CreateTags` operations generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide._

## Understanding Amazon EFS log file

entries

A _trail_ is a configuration that enables delivery of
events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log
entries. An _event_ represents a single request from any source
and includes information about the requested action, the date and time of the action, request
parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls,
so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateTags`
operation when a tag for a file system is created from the console.

```
{
	"eventVersion": "1.06",
	"userIdentity": {
		"type": "Root",
		"principalId": "111122223333",
		"arn": "arn:aws:iam::111122223333:root",
		"accountId": "111122223333",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2017-03-01T18:02:37Z"
			}
		}
	},
	"eventTime": "2017-03-01T19:25:47Z",
	"eventSource": "elasticfilesystem.amazonaws.com",
	"eventName": "CreateTags",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "192.0.2.0",
	"userAgent": "console.amazonaws.com",
	"requestParameters": {
		"fileSystemId": "fs-00112233",
		"tags": [{
				"key": "TagName",
				"value": "AnotherNewTag"
			}
		]
	},
	"responseElements": null,
	"requestID": "dEXAMPLE-feb4-11e6-85f0-736EXAMPLE75",
	"eventID": "eEXAMPLE-2d32-4619-bd00-657EXAMPLEe4",
	"eventType": "AwsApiCall",
	"apiVersion": "2015-02-01",
	"recipientAccountId": "111122223333"
}


```

The following example shows a CloudTrail log entry that demonstrates the `DeleteTags`
action when a tag for a file system is deleted from the console.

```
{
	"eventVersion": "1.06",
	"userIdentity": {
		"type": "Root",
		"principalId": "111122223333",
		"arn": "arn:aws:iam::111122223333:root",
		"accountId": "111122223333",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2017-03-01T18:02:37Z"
			}
		}
	},
	"eventTime": "2017-03-01T19:25:47Z",
	"eventSource": "elasticfilesystem.amazonaws.com",
	"eventName": "DeleteTags",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "192.0.2.0",
	"userAgent": "console.amazonaws.com",
	"requestParameters": {
		"fileSystemId": "fs-00112233",
		"tagKeys": []
	},
	"responseElements": null,
	"requestID": "dEXAMPLE-feb4-11e6-85f0-736EXAMPLE75",
	"eventID": "eEXAMPLE-2d32-4619-bd00-657EXAMPLEe4",
	"eventType": "AwsApiCall",
	"apiVersion": "2015-02-01",
	"recipientAccountId": "111122223333"
}


```

### Log entries for EFS service-linked roles

The Amazon EFS service-linked role makes API calls to AWS resources. You will see CloudTrail log
entries with `username: AWSServiceRoleForAmazonElasticFileSystem` for calls made by
the EFS service-linked role. For more information about EFS and service-linked roles, see [Using service-linked roles for Amazon EFS](using-service-linked-roles.md "using-service-linked-roles.md").

The following example shows a CloudTrail log entry that demonstrates a
`CreateServiceLinkedRole` action when Amazon EFS creates the
AWSServiceRoleForAmazonElasticFileSystem service-linked role.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "111122223333",
        "arn": "arn:aws:iam::111122223333:user/user1",
        "accountId": "111122223333",
        "accessKeyId": "A111122223333",
        "userName": "user1",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-10-23T22:45:41Z"
            }
        },
        "invokedBy": "elasticfilesystem.amazonaws.com”
    },
    "eventTime": "2019-10-23T22:45:41Z",
    "eventSource": "iam.amazonaws.com",
    "eventName": "CreateServiceLinkedRole",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "user_agent",
    "requestParameters": {
        "aWSServiceName": "elasticfilesystem.amazonaws.com”
    },
    "responseElements": {
        "role": {
            "assumeRolePolicyDocument": "111122223333-10-111122223333Statement111122223333Action111122223333AssumeRole111122223333Effect%22%3A%20%22Allow%22%2C%20%22Principal%22%3A%20%7B%22Service%22%3A%20%5B%22 elasticfilesystem.amazonaws.com%22%5D%7D%7D%5D%7D",
            "arn": "arn:aws:iam::111122223333:role/aws-service-role/elasticfilesystem.amazonaws.com/AWSServiceRoleForAmazonElasticFileSystem",
            "roleId": "111122223333",
            "createDate": "Oct 23, 2019 10:45:41 PM",
            "roleName": "AWSServiceRoleForAmazonElasticFileSystem",
            "path": "/aws-service-role/elasticfilesystem.amazonaws.com/“
        }
    },
    "requestID": "11111111-2222-3333-4444-abcdef123456",
    "eventID": "11111111-2222-3333-4444-abcdef123456",
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}

```

The following example shows a CloudTrail log entry that demonstrates a
`CreateNetworkInterface` action made by the
`AWSServiceRoleForAmazonElasticFileSystem` service-linked role, noted in the
`sessionContext`.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts::0123456789ab:assumed-role/AWSServiceRoleForAmazonElasticFileSystem/0123456789ab",
        "accountId": "0123456789ab",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::0123456789ab:role/aws-service-role/elasticfilesystem.amazonaws.com/AWSServiceRoleForAmazonElasticFileSystem",
                "accountId": "0123456789ab",
                "userName": "AWSServiceRoleForAmazonElasticFileSystem"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-10-23T22:50:05Z"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "20You 19-10-23T22:50:05Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "CreateNetworkInterface",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "elasticfilesystem.amazonaws.com”,
    "userAgent": "elasticfilesystem.amazonaws.com",
    "requestParameters": {
        "subnetId": "subnet-71e2f83a",
        "description": "EFS mount target for fs-1234567 (fsmt-1234567)",
        "groupSet": {},
        "privateIpAddressesSet": {}
    },
    "responseElements": {
        "requestId": "0708e4ad-03f6-4802-b4ce-4ba987d94b8d",
        "networkInterface": {
            "networkInterfaceId": "eni-0123456789abcdef0",
            "subnetId": "subnet-12345678",
            "vpcId": "vpc-01234567",
            "availabilityZone": "us-east-1b",
            "description": "EFS mount target for fs-1234567 (fsmt-1234567)",
            "ownerId": "666051418590",
            "requesterId": "0123456789ab",
            "requesterManaged": true,
            "status": "pending",
            "macAddress": "00:bb:ee:ff:aa:cc",
            "privateIpAddress": "192.0.2.0",
            "privateDnsName": "ip-192-0-2-0.ec2.internal",
            "sourceDestCheck": true,
            "groupSet": {
                "items": [
                    {
                        "groupId": "sg-c16d65b6",
                        "groupName": "default"
                    }
                ]
            },
            "privateIpAddressesSet": {
                "item": [
                    {
                        "privateIpAddress": "192.0.2.0",
                        "primary": true
                    }
                ]
            },
            "tagSet": {}
        }
    },
    "requestID": "11112222-3333-4444-5555-666666777777",
    "eventID": "aaaabbbb-1111-2222-3333-444444555555",
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

### Log entries for EFS authentication

Amazon EFS authorization for NFS clients emits `NewClientConnection` and
`UpdateClientConnection` CloudTrail events. A `NewClientConnection` event
is emitted when a connection is authorized immediately after an initial connection, and
immediately after a re-connection. An `UpdateClientConnection` is emitted when a
connection is reauthorized and the list of permitted actions has changed. The event is also
emitted when the new list of permitted actions doesn't include `ClientMount`. For
more information about EFS authorization, see [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").

The following example shows a CloudTrail log entry that demonstrates a
`NewClientConnection` event.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts::0123456789ab:assumed-role/abcdef0123456789",
        "accountId": "0123456789ab",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE ",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::0123456789ab:role/us-east-2",
                "accountId": "0123456789ab",
                "userName": "username"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-12-23T17:50:16Z"
            },
            "ec2RoleDelivery": "1.0"
        }
    },
    "eventTime": "2019-12-23T18:02:12Z",
    "eventSource": "elasticfilesystem.amazonaws.com",
    "eventName": "NewClientConnection",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "elasticfilesystem",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "27859ac9-053c-4112-aee3-f3429719d460",
    "readOnly": true,
    "resources": [
        {
            "accountId": "0123456789ab",
            "type": "AWS::EFS::FileSystem",
            "ARN": "arn:aws:elasticfilesystem:us-east-2:0123456789ab:file-system/fs-01234567"
        },
        {
            "accountId": "0123456789ab",
            "type": "AWS::EFS::AccessPoint",
            "ARN": "arn:aws:elasticfilesystem:us-east-2:0123456789ab:access-point/fsap-0123456789abcdef0"
        }
    ],
    "eventType": "AwsServiceEvent",
    "recipientAccountId": "0123456789ab",
    "serviceEventDetails": {
        "permissions": {
            "ClientRootAccess": true,
            "ClientMount": true,
            "ClientWrite": true
        },
        "sourceIpAddress": "10.7.3.72"
    }
}
```

## Amazon EFS log file entries for encrypted-at-rest

file systems

Amazon EFS gives you the option of using encryption at rest, encryption in transit, or both, for
your file systems. For more information, see [Data encryption in Amazon EFS](encryption.md "encryption.md").

Amazon EFS sends [Encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
when making AWS KMS API requests to generate data keys and decrypt Amazon EFS data. The file system ID
is the encryption context for all file systems that are encrypted at rest. In the `requestParameters` field of a CloudTrail log entry, the encryption context looks
similar to the following.

```
"EncryptionContextEquals": {}
"aws:elasticfilesystem:filesystem:id" : "`fs-4EXAMPLE`"
```
