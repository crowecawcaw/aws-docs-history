# Cross-account CloudTrail logging

Lake Formation provides a centralized audit trail of all cross-account access to data in your
data lake. When a recipient AWS account accesses data in a shared table, Lake Formation copies the
CloudTrail event to the owning account's CloudTrail logs. Copied events include queries against the
data by integrated services such as Amazon Athena and Amazon Redshift Spectrum, and data accesses
by AWS Glue jobs.

CloudTrail events for cross-account operations on Data Catalog resources are similarly
copied.

As a resource owner, if you enable object-level logging in Amazon S3, you can run queries
that join S3 CloudTrail events with Lake Formation CloudTrail events to determine the accounts that have
accessed your S3 buckets.

###### Topics

- [Including principal identities in
  cross-account CloudTrail logs](#cross-account-logging-optin "#cross-account-logging-optin")
- [Querying CloudTrail logs for Amazon S3 cross-account
  access](#cross-account-logging-s3 "#cross-account-logging-s3")

## Including principal identities in

cross-account CloudTrail logs

By default, cross-account CloudTrail events added to the shared resource recipient's logs
and copied to resource owner's logs contain only the AWS principal ID of the external
account principal—not the human-readable Amazon Resource Name (ARN) of the
principal (principal ARN). When sharing resources within trusted boundaries, such as
within the same organization or team, you can opt in to include the principal ARN in the
CloudTrail events. Resource owner accounts can then track the principals in recipient accounts
that access their owned resources.

###### Important

As a shared resource recipient, to see the principal ARN in events in your own
CloudTrail logs, you must opt in to share the principal ARN with the owner account.

If the data access occurs through a resource link, two events are logged in the
shared resource recipient account: one for the resource link access and one for the
target resource access. The event for the resource link access _does_ include the principal ARN. The event for the target resource access
does not include the principal ARN without the opt-in. The resource link access event
is not copied to the owner account.

The following is an excerpt from a default cross-account CloudTrail event (without
opt-in). The account performing the data access is 1111-2222-3333. This is the
log that is shown in both the calling account and the resource owner account. Lake Formation
populates logs in both accounts in the cross-account case.

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
        "lakeFormationRoleSessionName": "AWSLF-00-GL-111122223333-G13T0Rmng2"
    },
...
}
```

As a shared resource consumer, when you opt in to include the principal ARN, the
excerpt becomes the following. The `lakeFormationPrincipal` field represents
the end role or user performing the query through Amazon Athena, Amazon Redshift Spectrum, or AWS Glue
jobs.

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
        **"lakeFormationPrincipal": "arn:aws:iam::111122223333:role/ETL-Glue-Role",**
        "lakeFormationRoleSessionName": "AWSLF-00-GL-111122223333-G13T0Rmng2"
    },
...
}
```

###### To opt in to include principal ARNs in cross-account CloudTrail logs

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as the `Administrator` user, or a user with the
`Administrator Access` IAM policy. 2. In the navigation pane, choose **Settings**. 3. On the **Data catalog settings** page, in the **Default
permissions for AWS CloudTrail** section, for **Resource
owners**, enter one or more AWS resource owner account IDs.

Press **Enter** after each account ID. 4. Choose **Save**.

Now cross-account CloudTrail events stored in the logs for both the shared resource
recipient and the resource owner contain the principal ARN.

## Querying CloudTrail logs for Amazon S3 cross-account

access

As a shared resource owner, you can query S3 CloudTrail logs to determine the accounts
that have accessed your Amazon S3 buckets (provided that you enabled object-level logging in
Amazon S3). This applies only to S3 locations that you registered with Lake Formation. If shared resource
consumers opt in to include principal ARNs in Lake Formation CloudTrail logs, you can determine the roles or
users that accessed the buckets.

When running queries with Amazon Athena, you can join Lake Formation CloudTrail events and
S3 CloudTrail events on the session name property. Queries can also filter Lake Formation events on
`eventName="GetDataAccess"`, and S3 events on
`eventName="Get Object"` or `eventName="Put Object"`.

The following is an excerpt from a Lake Formation cross-account CloudTrail event where data in a
registered S3 location was accessed.

```
{
  "eventSource": "lakeformation.amazonaws.com",
  "eventName": "GetDataAccess",
  ..............
  ..............
  "additionalEventData": {
    "requesterService": "GLUE_JOB",
    "lakeFormationPrincipal": "arn:aws:iam::111122223333:role/ETL-Glue-Role",
    "lakeFormationRoleSessionName": "**AWSLF-00-GL-111122223333-B8JSAjo5QA**"
   }
}
```

The `lakeFormationRoleSessionName` key value,
`AWSLF-00-GL-111122223333-B8JSAjo5QA`, can be joined with the
session name in the `principalId` key of the S3 CloudTrail event. The following is
an excerpt from the S3 CloudTrail event. It shows the location of the session name.

```

{
   "eventSource": "s3.amazonaws.com",
   "eventName": "Get Object"
   ..............
   ..............
   "principalId": "AROAQSOX5XXUR7D6RMYLR:**AWSLF-00-GL-111122223333-B8JSAjo5QA**",
   "arn": "arn:aws:sets::111122223333:assumed-role/Deformationally/AWSLF-00-GL-111122223333-B8JSAjo5QA",
   "session Context": {
     "session Issuer": {
       "type": "Role",
       "principalId": "AROAQSOX5XXUR7D6RMYLR",
       "arn": "arn:aws:iam::111122223333:role/aws-service-role/lakeformation.amazonaws.com/Deformationally",
       "accountId": "111122223333",
       "user Name": "Deformationally"
     },
   ..............
   ..............
}

```

The session name is formatted as follows:

```
AWSLF-<version-number>-<query-engine-code>-<account-id->-<suffix>
```

**`version-number`**

The version of this format, currently `00`. If the session name
format changes, the next version will be `01`.

**`query-engine-code`**

Indicates the entity that accessed the data. Current values are:

|      |                          |
| ---- | ------------------------ |
| `GL` | AWS Glue ETL job         |
| `AT` | Athena                   |
| `RE` | Amazon Redshift Spectrum |

**`account-id`**

The AWS account ID that requested credentials from Lake Formation.

**`suffix`**

A randomly generated string.
