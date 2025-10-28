# Logging AWS Lake Formation API calls using

AWS CloudTrail

AWS Lake Formation is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Lake Formation. CloudTrail captures all Lake Formation API calls as events.
The calls captured include calls from the Lake Formation console, the AWS Command Line Interface, and code calls to
the Lake Formation API actions. If you create a trail, you can enable continuous delivery of CloudTrail
events to an Amazon S3 bucket, including events for Lake Formation. If you don't configure a trail, you
can still view the most recent events in the CloudTrail console in **Event history**.
Using the information collected by CloudTrail, you can determine the request that was made to
Lake Formation, the IP address from which the request was made, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, see the [_AWS CloudTrail User Guide_](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Lake Formation information in CloudTrail

CloudTrail is enabled by default when you create a new AWS account. When activity occurs in
Lake Formation, that activity is recorded as a CloudTrail event along with other AWS service events in
**Event history**. An event represents a single request from any source and
includes information about the requested action, the date and time of the action, and request
parameters. In addition, every event or log entry contains information about who generated the
request. The identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

You can view, search, and download recent events for your AWS account. For more
information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Lake Formation,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail on the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services, such as Amazon Athena, to further analyze and act upon the event data
collected in CloudTrail logs. CloudTrail can also deliver log files to Amazon CloudWatch Logs and CloudWatch Events.

For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## Understanding Lake Formation events

All Lake Formation API actions are logged by CloudTrail and are documented in the AWS Lake Formation Developer Guide. For
example, calls to the
`PutDataLakeSettings`,
`GrantPermissions`, and `RevokePermissions` actions generate entries
in the CloudTrail log files.

The following example shows a CloudTrail event for the `GrantPermissions` action. The
entry includes the user who granted the permission (`datalake_admin`), the
principal that the permission was granted to (`datalake_user1`), and the permission
that was granted (`CREATE_TABLE`). The entry also shows that the grant failed
because the target database was not specified in the `resource` argument.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAZKE67KM3P775X74U2",
        "arn": "arn:aws:iam::111122223333:user/datalake_admin",
        "accountId": "111122223333",
        "accessKeyId": "...",
        "userName": "datalake_admin"
    },
    "eventTime": "2021-02-06T00:43:21Z",
    "eventSource": "lakeformation.amazonaws.com",
    "eventName": "GrantPermissions",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "72.21.198.65",
    "userAgent": "aws-cli/1.19.0 Python/3.6.12 Linux/4.9.230-0.1.ac.223.84.332.metal1.x86_64 botocore/1.20.0",
    "errorCode": "InvalidInputException",
    "errorMessage": "Resource must have one of the have either the catalog, table or database field populated.",
    "requestParameters": {
        "principal": {
            "dataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_user1"
        },
        "resource": {},
        "permissions": [
            "CREATE_TABLE"
        ]
    },
    "responseElements": null,
    "requestID": "b85e863f-e75d-4fc0-9ff0-97f943f706e7",
    "eventID": "8d2ccef0-55f3-42d3-9ede-3a6faedaa5c1",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333"
}
```

The next example shows a CloudTrail log entry for the `GetDataAccess` action.
Principals do not directly call this API. Rather, `GetDataAccess` is logged
whenever a principal or integrated AWS service requests temporary credentials to access data
in a data lake location that is registered with Lake Formation.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AWSAccount",
        "principalId": "AROAQGFTBBBGOBWV2EMZA:GlueJobRunnerSession",
        "accountId": "111122223333"
    },
    "eventSource": "lakeformation.amazonaws.com",
    "eventName": "GetDataAccess",
...
...
    "additionalEventData": {
        "requesterService": "GLUE_JOB",
        "lakeFormationPrincipal": "arn:aws:iam::111122223333:role/ETL-Glue-Role",
        "lakeFormationRoleSessionName": "AWSLF-00-GL-111122223333-G13T0Rmng2"
    },
...
}

```

###### Amazon Redshift federated catalog access monitoring

Amazon Redshift federated catalogs in the AWS Glue Data Catalog do not generate `GetDataAccess`
events in Lake Formation CloudTrail logs. To track data access for Amazon Redshift tables in the Data Catalog, monitor
`GetTable` and `BatchGetTable` events, which capture metadata access
patterns for Redshift federated tables, including table name, database name, and catalog ID
information.

###### See Also

- [Cross-account CloudTrail logging](cross-account-logging.md "cross-account-logging.md")
