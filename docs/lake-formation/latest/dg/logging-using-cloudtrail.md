

# Logging AWS Lake Formation API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Lake Formation is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Lake Formation. CloudTrail captures all Lake Formation API calls as events. The calls captured include calls from the Lake Formation console, the AWS Command Line Interface, and code calls to the Lake Formation API actions. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Lake Formation. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Lake Formation, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [*AWS CloudTrail User Guide*](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Lake Formation information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled by default when you create a new AWS account. When activity occurs in Lake Formation, that activity is recorded as a CloudTrail event along with other AWS service events in **Event history**. An event represents a single request from any source and includes information about the requested action, the date and time of the action, and request parameters. In addition, every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

You can view, search, and download recent events for your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for Lake Formation, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail on the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services, such as Amazon Athena, to further analyze and act upon the event data collected in CloudTrail logs. CloudTrail can also deliver log files to Amazon CloudWatch Logs and CloudWatch Events.

For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

## Understanding Lake Formation events
<a name="understanding-service-name-entries"></a>

All Lake Formation API actions are logged by CloudTrail and are documented in the AWS Lake Formation Developer Guide. For example, calls to the `PutDataLakeSettings`, `GrantPermissions`, and `RevokePermissions` actions generate entries in the CloudTrail log files.

The following example shows a CloudTrail event for the `GrantPermissions` action. The entry includes the user who granted the permission (`datalake_admin`), the principal that the permission was granted to (`datalake_user1`), and the permission that was granted (`CREATE_TABLE`). The entry also shows that the grant failed because the target database was not specified in the `resource` argument.

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

The next example shows a CloudTrail log entry for the `GetDataAccess` action. Principals do not directly call this API. Rather, `GetDataAccess` is logged whenever a principal or integrated AWS service requests temporary credentials to access data in a data lake location that is registered with Lake Formation.

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

### Tracing data access in CloudTrail with Lake Formation
<a name="source-identity-cloudtrail"></a>

Lake Formation issues temporary, scoped-down credentials to query engines—such as , Amazon EMR, and AWS Glue—for accessing table data locations in Amazon S3. Lake Formation uses the IAM role that you specify when you [register a data location](https://docs.aws.amazon.com/lake-formation/latest/dg/register-location.html) with Lake Formation for vending these credentials.

#### Change in CloudTrail logging behavior (February 2026)
<a name="source-identity-cloudtrail-change"></a>

**Before February 2026**, when a query engine made an `s3:GetObject` call to fetch query data, CloudTrail logs displayed the Lake Formation registration IAM role as the principal.

**Starting in February 2026**, CloudTrail logs for `s3:GetObject` calls also include the [IAM unique identifier](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-prefixes) (beginning with `AROA`) of the IAM role that initiated the query. This identifier corresponds to the IAM role that initiated the query, Amazon EMR job, or AWS Glue ETL job.

#### Tracing data access from query initiation to Amazon S3
<a name="source-identity-cloudtrail-tracing"></a>

Each `s3:GetObject` call in CloudTrail corresponds to a `lakeformation:GetDataAccess` call. You can use the IAM role identifier that is present in both log entries to trace the caller's IAM role from query initiation through to data access in Amazon S3.

To enable the information of source identity in the Amazon S3 data events CloudTrail logs, follow the below steps. For enabling Amazon S3 data events in CloudTrail, refer [Enabling CloudTrail event logging for Amazon S3 buckets and objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html).

**Important**  
Enabling Amazon S3 data events in CloudTrail incurs additional charges.

**To enable source identity tracking in CloudTrail logs**

1. Using , run the `get-data-lake-settings` command. In the response, edit the `Parameters` field to add `"SET_SOURCE_IDENTITY": "TRUE"`.

   Run the `put-data-lake-settings` command.

   ```
   "Parameters": {
       "CROSS_ACCOUNT_VERSION": "4",
       "SET_SOURCE_IDENTITY": "TRUE"
   },
   ```

1. In the trust policy of the IAM role used to register your Amazon S3 data location with Lake Formation, add `sts:SetSourceIdentity`:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": [
                       "lakeformation.amazonaws.com"
                   ]
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:SetSourceIdentity"
               ]
           }
       ]
   }
   ```

The following log shows the source identity information in an example `s3:GetObject` CloudTrail log.

```
"sessionContext": {
    "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA2EXAMPLEXYZ3AB6CDKLM",
        "arn": "arn:aws:iam::111122223333:role/LFRegistrationRole",
        "accountId": "111122223333",
        "userName": "LFRegistrationRole"
    },
    "sourceIdentity": "V2.111122223333.AROA3EXAMPLEPQR7ST9UVWXY"
},
"invokedBy": "glue.amazonaws.com"
```

**See Also**  
For information about tracking IAM Identity Center user context in CloudTrail logs, see [Integrating IAM Identity Center](identity-center-integration.md).

**Amazon Redshift federated catalog access monitoring**  
Amazon Redshift federated catalogs in the AWS Glue Data Catalog do not generate `GetDataAccess` events in Lake Formation CloudTrail logs. To track data access for Amazon Redshift tables in the Data Catalog, monitor `GetTable` and `BatchGetTable` events, which capture metadata access patterns for Redshift federated tables, including table name, database name, and catalog ID information.

**See Also**  
[Cross-account CloudTrail logging](cross-account-logging.md)