# Logging calls to the AWS Network Firewall API with

AWS CloudTrail

AWS Network Firewall is integrated with AWS CloudTrail, a service that provides a record of API
calls to Network Firewall by a user, role, or an AWS service. CloudTrail captures all API calls
for Network Firewall as events. The calls captured include calls from the Network Firewall
console and code calls to the Network Firewall API operations. If you create a trail, you
can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for
Network Firewall. If you don't configure a trail, you can still view the most recent events
in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine information including the request that was made to
Network Firewall, the IP address from which the request was made, who made the request, and
when the request was made.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS Network Firewall information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in Network Firewall, it's recorded in a CloudTrail event along with other AWS
service events in **Event history**. You can view, search, and
download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Network Firewall, create a trail. A _trail_ enables CloudTrail to deliver
log files to an Amazon S3 bucket. By default, when you create a trail in the console, the
trail applies to all AWS Regions. The trail logs events from all Regions in the
AWS partition and delivers the log files to the Amazon S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon
the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Network Firewall actions are logged by CloudTrail. These actions are documented in the
[Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") section of the [AWS Network Firewall API Reference](../APIReference.md "../APIReference.md"). For example, calls to the
actions `CreateFirewall`, `ListFirewalls`, and
`DeleteFirewall` generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user
  credentials.
- Whether the request was made with temporary security credentials for a
  role or federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail
userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## CloudTrail log file examples

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the
requested action, the date and time of the action, request parameters, and so on.
CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't
appear in any specific order.

The following are examples of CloudTrail log entries for Network Firewall operations.

Example: CloudTrail log entry for `CreateFirewall`

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "EXAMPLEPrincipalId",
    "arn": "arn:aws:sts::444455556666:assumed-role/Admin/EXAMPLE",
    "accountId": "444455556666",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "EXAMPLEPrincipalId",
        "arn": "arn:aws:iam::444455556666:role/Admin",
        "accountId": "444455556666",
        "userName": "Admin"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-08-13T03:07:52Z"
      }
    }
  },
  "eventTime": "2020-08-13T03:07:53Z",
  "eventSource": "network-firewall.amazonaws.com",
  "eventName": "CreateFirewall",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "203.0.113.4",
  "userAgent": "aws-cli/1.18.117 Python/3.6.10 Linux/4.9.217-0.1.ac.205.84.332.metal1.x86_64 botocore/1.17.40",
  "requestParameters": {
    "firewallName": "firewall01",
    "firewallPolicyArn": "arn:aws:network-firewall:us-west-2:444455556666:firewall-policy/policy01",
    "vpcId": "vpc-11112222",
    "subnetMappings": [
      {
        "subnetId": "subnet-44443333",
        "requestedCapacity": "10"
      }
    ],
    "deleteProtection": false
  },
  "responseElements": {
    "firewall": {
      "firewallName": "firewall01",
      "firewallArn": "arn:aws:network-firewall:us-west-2:444455556666:firewall/firewall01",
      "firewallPolicyArn": "arn:aws:network-firewall:us-west-2:444455556666:firewall-policy/policy01",
      "vpcId": "vpc-11112222",
      "subnetMappings": [
        {
          "subnetId": "subnet-44443333",
          "requestedCapacity": "10"
        }
      ],
      "deleteProtection": false
    },
    "firewallStatus": {
      "status": "PROVISIONING",
      "configurationSyncStateSummary": "PENDING"
    }
  },
  "requestID": "43a8cad0-68b6-45d2-b6f3-28cf0e195d47",
  "eventID": "7d575a14-ec3f-43c8-8735-eaadd21fd9d1",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "recipientAccountId": "444455556666"
}

```

Example: CloudTrail log entry for `ListFirewalls`

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "EXAMPLEPrincipalId",
    "arn": "arn:aws:sts::444455556666:assumed-role/Admin/EXAMPLE",
    "accountId": "444455556666",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "EXAMPLEPrincipalId",
        "arn": "arn:aws:iam::444455556666:role/Admin",
        "accountId": "444455556666",
        "userName": "Admin"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-08-13T03:07:55Z"
      }
    }
  },
  "eventTime": "2020-08-13T03:07:55Z",
  "eventSource": "network-firewall.amazonaws.com",
  "eventName": "ListFirewalls",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "203.0.113.4",
  "userAgent": "aws-cli/1.18.117 Python/3.6.10 Linux/4.9.217-0.1.ac.205.84.332.metal1.x86_64 botocore/1.17.40",
  "requestParameters": {
    "maxResults": 10
  },
  "responseElements": null,
  "requestID": "1ac1567a-fa84-49ac-b5aa-6016052ad646",
  "eventID": "79b95fd6-a288-49b1-a907-b61ed99b94c0",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "recipientAccountId": "444455556666"
}
```

Example: CloudTrail log entry for `DeleteFirewall`

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEPrincipalId",
        "arn": "arn:aws:sts::444455556666:assumed-role/Admin/EXAMPLE",
        "accountId": "444455556666",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEPrincipalId",
                "arn": "arn:aws:iam::444455556666:role/Admin",
                "accountId": "444455556666",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-08-19T16:09:29Z"
            }
        }
    },
    "eventTime": "2020-08-19T16:18:43Z",
    "eventSource": "network-firewall.amazonaws.com",
    "eventName": "DeleteFirewall",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "198.51.100.190",
    "userAgent": "Apache-HttpClient/UNAVAILABLE (Java/1.8.0_232)",
    "requestParameters": {
        "firewallArn": "arn:aws:network-firewall:us-west-2:444455556666:firewall/DeleteMeFast"
    },
    "responseElements": {
        "firewall": {
            "firewallName": "DeleteMeFast",
            "firewallArn": "arn:aws:network-firewall:us-west-2:444455556666:firewall/DeleteMeFast",
            "firewallPolicyArn": "arn:aws:network-firewall:us-west-2:444455556666:firewall-policy/123",
            "vpcId": "vpc-11112222",
            "subnetMappings": [
                {
                    "subnetId": "subnet-99990000",
                    "requestedCapacity": "14"
                },
                {
                    "subnetId": "subnet-77776666",
                    "requestedCapacity": "12"
                }
            ],
            "deleteProtection": true,
            "description": "HIDDEN_DUE_TO_SECURITY_REASONS"
        },
        "firewallStatus": {
            "status": "DELETING",
            "configurationSyncStateSummary": "PENDING",
            "syncStates": {
                "us-west-2c": {
                    "attachment": {
                        "subnetId": "subnet-99990000",
                        "networkInterfaceId": "eni-01e59ab6f6064c453",
                        "status": "SCALING"
                    },
                    "config": {}
                },
                "us-west-2d": {
                    "attachment": {
                        "subnetId": "subnet-77776666",
                        "networkInterfaceId": "eni-04c3ac8c04076ed36",
                        "status": "SCALING"
                    },
                    "config": {}
                }
            }
        }
    },
    "requestID": "299b886e-23da-4c77-8beb-0853a0a08bcf",
    "eventID": "142b089a-8aca-4183-8326-5ff32a38876e",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "444455556666"
}
```
