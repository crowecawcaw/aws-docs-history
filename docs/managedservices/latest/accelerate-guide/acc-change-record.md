# Tracking changes in your AMS Accelerate accounts

###### Important

The Change Record service is deprecated as of July 1, 2025.

New accounts can’t be onboarded to the Change Record service.

To query CloudTrail data in your AMS Accelerate accounts, you can use these services:

- In AWS CloudTrail, choose **Event history** and filter events using Lookup attributes. You can use the
  time range filter and choose to filter event history by Event source with `s3.amazon.aws.com` specified, or choose to filter event history by Username. For more
  information, see [Working with CloudTrail event
  history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").
- Use AWS CloudTrail Lake to gather data through queries. In AWS CloudTrail choose
  **Lake**, and then choose **Query**. You can create your
  own queries, use the query generator, or use sample queries to gather event-based data.
  For example, you can ask who deleted an Amazon EC2 instance this past week. For more
  information, see [Creating a data
  lake from an AWS CloudTrail source](../../../lake-formation/latest/dg/getting-started-cloudtrail-tutorial.md "../../../lake-formation/latest/dg/getting-started-cloudtrail-tutorial.md") and [CloudTrailLake queries](../../../awscloudtrail/latest/userguide/cloudtrail-lake-queries.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake-queries.md") .
- Create an Amazon Athena table in AWS CloudTrail and set the storage location as the Amazon S3 bucket
  associated with your trail. Verify that the Home region for your trail and Amazon S3 bucket are
  the same. In Amazon Athena, use the Query editor to run the [default queries](#acc-cr-canned-queries "#acc-cr-canned-queries") that
  Accelerate provides to use with the Athena console. For more information on how to
  create an Athena table to to query CloudTrail logs, see [Query AWS CloudTrail logs](../../../athena/latest/ug/cloudtrail-logs.md "../../../athena/latest/ug/cloudtrail-logs.md").

###### Topics

- [Viewing your change records](#acc-cr-using "#acc-cr-using")
- [Default queries](#acc-cr-canned-queries "#acc-cr-canned-queries")
- [Change record permissions](#acc-cr-permissions "#acc-cr-permissions")
  AWS Managed Services helps you track changes made by the AMS Accelerate Operations team and AMS Accelerate automation by providing a
  queryable interface using the [Amazon Athena](../../../athena.md "../../../athena.md") (Athena) console and AMS Accelerate
  log management.

Athena is an interactive query service you can use to analyze data in Amazon S3 by using standard
Structured Query Language (SQL) (see
[SQL Reference for Amazon Athena](../../../athena/latest/ug/ddl-sql-reference.md "../../../athena/latest/ug/ddl-sql-reference.md")).
Athena is serverless, so there is no infrastructure to manage,
and you pay only for the queries that you run. AMS Accelerate creates Athena tables with daily
partitions over CloudTrail logs, and provides queries on your primary AWS Region and within the
**ams-change-record** workgroup. You can choose any of the default queries
and run them as needed. To learn more about Athena workgroups, see [How Workgroups Work](../../../athena/latest/ug/user-created-workgroups.md "../../../athena/latest/ug/user-created-workgroups.md").

###### Note

Only Accelerate can query CloudTrail events for your
Accelerate account using Athena when Accelerate [is integrated with your
CloudTrail Organization trail](acc-onb-trail-choices.md "acc-onb-trail-choices.md"), unless your Organization administrator deployed
an IAM Role for using Athena to query and analyze CloudTrail events in your account, during onboarding.

Using change record, you can easily answer questions like:

- Who (AMS Accelerate Systems or AMS Accelerate Operators) has accessed your account
- What changes have been made by AMS Accelerate in your account
- When did AMS Accelerate perform changes in your account
- Where to go to view changes made in your account
- Why AMS Accelerate needed to make the changes in your account
- How to modify queries to get answers to all those questions for any non-AMS changes too

## Viewing your change records

To use Athena queries, sign in to the AWS Management console and navigate to the Athena
console in your primary AWS Region.

###### Note

If you see the **Amazon Athena Get Started** page while performing any of the steps, click
**Get Started**. This might appear for you even if your Change Record infrastructure is already
in place.

1. Choose **Workgroup** from the upper navigation panel in the Athena
   console.
2. Choose the **ams-change-record** workgroup, and then click
   **Switch Workgroup**.
3. Choose **ams-change-record-database** from the **Database Combo** box.
   The **ams-change-record-database** includes the **ams-change-record-table**
   table.
4. Choose **Saved Queries** from the upper navigation panel.
5. The **Saved Queries** window shows a list of queries that AMS Accelerate provides,
   which you can run. Choose the query you want to run from the **Saved
   Queries** list. For example, **ams_session_accesses_v1
   query**.

For the full list of preset AMS Accelerate queries, see [Default queries](#acc-cr-canned-queries "#acc-cr-canned-queries"). 6. Adjust the **datetime** filter in the query editor box as needed; by default,
the query only checks changes from the last day. 7. Choose **Run query**.

## Default queries

AMS Accelerate provides several default queries you can use within the Athena console. The
default queries are listed in the following tables.

###### Note

- All queries accept **datetime range** as an optional filter; all the queries run over the last 24
  hours, by default. For expected input, see
  the following subsection,
  [Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp").
- Parameter inputs that you can or need to change are shown in the query as
  `<PARAMETER_NAME>` with angular braces. Replace the placeholder **and**
  the angular braces with your parameter value.
- All filters are optional. In the queries, some optional filters are commented out with a double dash (--)
  at the start of the line. All queries will run without them, with default parameters. If you want to specify parameter
  values for these optional filters, remove the double dash (--) at the start of the line and replace the parameter
  as you want.
- All queries return `IAM PincipalId` and `IAM SessionId` in the outputs
- The calculated cost for running a query depends on how many CloudTrail logs are generated for the
  account. To calculate the cost, use the
  [AWS Athena Pricing Calculator](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").

| Canned queries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Purpose/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Inputs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Outputs |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Query name**:<br>`ams_access_session_query_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Tracking AMS Accelerate access sessions<br>Provides information about a specific AMS Accelerate access session. The query<br>accepts the IAM Principal ID as an optional filter and returns event time,<br>business need for accessing the account, requester, and so on.<br>You can filter on a specific IAM Principal ID by uncommenting the line and replacing the placeholder<br>`IAM PrincipalId` with a specific ID in the query editor.<br>You can also list non-AMS access sessions by removing the \*_useragent_<br>• filter line in<br>the WHERE clause of the query.                                                                                                                                                                                                                                                                                                                                                                      | (Optional) `IAM PrincipalId`: The IAM Principal identifier of the resource that is trying to access.<br>The format is `UNIQUE_IDENTIFIER`:`RESOURCE_NAME`. For details see<br>[unique identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids"). You can run the query without this filter to determine the exact IAM PrincipalId the you<br>want to filter with.                                                                                                                                                                                                                                   | • EventTime: Time of gaining the access<br>• EventName: AWS Event name (AssumeRole)<br>• EventRegion: AWS Region that gets the request<br>• EventId: CloudTrail Event ID<br>• BusinessNeed Type: Business reason type to access the account. Allowed values are:<br>SupportCase, OpsItem, Issue, Text.<br>• BusinessNeed: Business need to access the account. For example, Support Case ID, Ops Item ID,<br>and so forth.<br>• Requester: Operator ID that accesses the account, or Automation system that access the<br>account.<br>• RequestAccessType: Requester type (System, OpsConsole, OpsAPI, Unset) |
| **Query name**:<br>`ams_events_query_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Track all mutating actions done by AMS Accelerate<br>Returns all write actions done on the account using that AMS Accelerate role filter.<br>You can also track mutating actions done by non-AMS roles by removing the<br>\*_useridentity.arn_<br>• filter lines from the WHERE clause of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | (Optional) Only **datetime range**. See<br>[Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | • AccountId: AWS Account ID<br>• RoleArn: RoleArn for the requester<br>• EventTime: Time of gaining the access<br>• EventName: AWS Event name (AssumeRole)<br>• EventRegion: AWS Region that gets the request<br>• EventId: CloudTrail Event ID<br>• RequestParameters : Request parameters for the request<br>• ResponseElements: Response elements for the response.<br>• UserAgent: AWS CloudTrail User Agent                                                                                                                                                                                              |
| **Query name**:<br>`ams_instance_access_sessions_query_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Track instance accesses by AMS Accelerate<br>Returns a list of AMS Accelerate instance accesses; every record includes event<br>time, event Region, instance ID, IAM Principal ID, IAM Session ID, SSM Session<br>ID. You can use the IAM Principal ID to get more details on the business need for<br>accessing the instance by using the `ams_access_sessions_query_v1` Athena<br>query. You can use the SSM Session ID to get more details on the instance access<br>session, including the start and end time of the session, log details, and using the<br>AWS Session Manager console in the instance's AWS Region.<br>Users can also list non-AMS instance accesses by removing the \*_useridentity_<br>• filter line in<br>the WHERE clause of the query.                                                                                                                                                                                    | Only `datetime range`. See<br>[Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | • InstanceId: Instance ID<br>• SSMSession Id: SSM Session ID<br>• RoleArn: RoleArn for the requester<br>• EventTime: Time of gaining the access<br>• EventName: AWS Event name (AssumeRole)<br>• EventRegion: AWS Region that gets the request<br>• EventId: CloudTrail Event ID                                                                                                                                                                                                                                                                                                                              |
| **Query name**:<br>`ams_privilege_escalation_events_query_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Track permission (escalation) events for AMS and non-AMS users<br>Provides a list of events that can directly or potentially lead to a privilege escalation.<br>The query accepts ActionedBy as an optional filter and returns EventName, EventId, EventTime, and so forth.<br>All fields associated with the event are also returned. Fields are blank if not applicable for that event.<br>The ActionedBy filter is disabled, by default; to enable it, remove "-<br>• " from that line.<br>By default, the ActionedBy filter is disabled (it will show privilege escalation events from all users). To show<br>events for a particular user or role, remove the double dash (--) from the \*_useridentity_<br>• filter<br>line in the WHERE clause and replace the placeholder `ACTIONEDBY_PUT_USER_NAME_HERE` with an<br>IAM user or role name. You can run the query without the filter to determine the exact user you want to filter<br>with. | (Optional) `ACTIONEDBY_PUT_USER_NAME`: Username for the actionedBy user.<br>This can be an IAM user or role. For example, ams-access-admin.<br>(Optional) `datetime range`. See<br>[Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp").                                                                                                                                                                                                                                                                                                                                                                                                           | • AccountId: Account Id<br>• ActionedBy: ActionedBy Username<br>• EventTime: Time of gaining the access<br>• EventName: AWS Event name (AssumeRole).<br>• EventRegion: AWS Region that gets the request<br>• EventId: CloudTrail Event ID                                                                                                                                                                                                                                                                                                                                                                     |
| **Query name**:<br>`ams_resource_events_query_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Track write events for specific resources AMS or non-AMS<br>Provides a list of events done on a specific resource. The query accepts resource ID as part of<br>the filters (replace placeholder `RESOURCE_INFO` in the WHERE clause of the query), and<br>returns all write actions done on that resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | (Required) `RESOURCE_INFO`: The resource identifier, can be an ID for any AWS resource in the<br>account. Do not confuse this with resource ARNs. For example, an instance ID for an EC2 instance, table name for<br>a DynamoDB table, logGroupName for a CloudWatch Log, etc.<br>(Optional) `datetime range`. See<br>[Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp").                                                                                                                                                                                                                                                                        | • AccountId: Account Id<br>• ActionedBy: ActionedBy Username<br>• EventTime: Time of gaining the access<br>• EventName: AWS Event name (AssumeRole).<br>• EventRegion: AWS Region that gets the request<br>• EventId: CloudTrail Event ID                                                                                                                                                                                                                                                                                                                                                                     |
| **Query name**:<br>`ams_session_events_query_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Track write actions performed by AMS Accelerate during specific session<br>Provides a list of events done on a specific session. The query accepts IAM Principal ID as part<br>of the filters (replace the placeholder `PRINCIPAL_ID` in the WHERE clause of the query),<br>and returns all write actions done on that resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | (Required) `PRINCIPAL_ID`: Principal ID for the session. The format is<br>`UNIQUE_IDENTIFIER`:`RESOURCE_NAME`. For details see<br>[unique identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids"). You can run the query "ams_session_ids_by_requester_v1" to get list of IAM Principal IDs<br>for a requester. You can also run the query without this filter to determine the exact IAM PrincipalId you want to<br>filter with.<br>(Optional) `datetime range`. See<br>[Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp"). | • AccountId: Account Id<br>• ActionedBy: ActionedBy Username<br>• EventTime: Time of gaining the access<br>• EventName: AWS Event name (AssumeRole)<br>• EventRegion: AWS Region that gets the request<br>• EventId: CloudTrail Event ID                                                                                                                                                                                                                                                                                                                                                                      |
| **Query name**:<br>`ams_session_ids_by_requester_v1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Track IAM Principal/Session IDs for a specific requester.<br>The query accepts "requester" (replace the placeholder `Requester` in the WHERE clause of<br>the query), and returns all IAM Principal Ids by that requester during the specified time range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | (Required) `Requester`: Operator ID that accesses the account (for example: alias of an operator),<br>or Automation system that access the account (for example: OsConfiguration, AlarmManager, etc.).<br>(Optional) `datetime range`. See<br>[Modifying the datetime filter in queries](#acc-cr-canned-queries-mod-timestamp "#acc-cr-canned-queries-mod-timestamp").                                                                                                                                                                                                                                                                                                                                                | • IAM PrincipalId - IAM Principal Id of the session. The format is<br>`UNIQUE_IDENTIFIER`:`RESOURCE_NAME`. For details see<br>[unique identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids"). You can run the query without this filter to determine the exact IAM PrincipalId you<br>want to filter with.<br>• IAM SessionId - IAM Session Id for the access session<br>• EventTime: Time of gaining the access                                                                         |

### Modifying the datetime filter in queries

All queries accept **datetime** range as an optional filter. All the queries run over the last one day
by default.

The format used for the **datetime** field is yyyy/MM/dd (for example: 2021/01/01). Remember that it only
stores the date and not the entire timestamp. For the entire timestamp, use the field **eventime**, which stores the timestamp in the ISO 8601 format
yyyy-MM-dd**T**HH:mm:ss**Z** (for example: 2021-01-01T23:59:59Z). However, since the table is
[partitioned](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md") on the datetime field, you’ll need to
pass in both the datetime and eventtime filter to the query. See the following examples.

###### Note

To see all the accepted ways you can modify the range, see the latest
[Presto function documentation](../../../athena/latest/ug/presto-functions.md "../../../athena/latest/ug/presto-functions.md")
based on the Athena engine version currently used for the **Date and Time Functions and Operators**
to see all the accepted ways you can modify the range.

**Date Level: Last 1 day or last 24 hours (Default)** example:
If the CURRENT_DATE='2021/01/01' , the filter will subtract one day from the current date and format it as
datetime > '2020/12/31'

```
datetime > date_format(date_add('day', - 1, CURRENT_DATE), '%Y/%m/%d')
```

**Date Level: Last 2 months** example:

```
datetime > date_format(date_add('month', - 2, CURRENT_DATE), '%Y/%m/%d')
```

**Date Level: Between 2 dates** example:

```
datetime > '2021/01/01'
      AND
      datetime < '2021/01/10'
```

**Timestamp Level: Last 12 hours** example:

Partition data scanned to last 1 day and then filter all events within the last 12 hours

```
datetime > date_format(date_add('day', - 1, CURRENT_DATE), '%Y/%m/%d')
      AND
      eventtime > date_format(date_add('hour', - 12, CURRENT_TIMESTAMP), '%Y-%m-%dT%H:%i:%sZ')
```

**Timestamp Level: Between 2 timestamps** example:

Get events between Jan 1, 2021 12:00PM and Jan 10, 2021 3:00PM.

```
datetime > '2021/01/01' AND datetime < '2021/01/10'
      AND
      eventtime > '2021-01-01T12:00:00Z' AND eventtime < '2021-01-10T15:00:00Z'
```

### Default query examples

```
Name: ams_access_session_query_v1

Description: >-
   The query provides more information on specific AMS access session.
   The query accepts IAM Principal Id as an optional filter and returns event time, business need for accessing the account, requester, ... etc.
   By default; the query filter last day events only, the user can change the datetime filter to search for more wide time range.
   By default; the IAM PrincipalId filter is disabled. To enable it, remove "-- " from that line.

AthenaQueryString: |-
   /*
     The query provides list of AMS access sessions during specific time range.
     The query accepts IAM Principal Id as an optional filter and returns event time, business need for accessing the account, requester, ... etc.

     By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

     By default; the IAM Principal ID filter is disabled (it shows access sessions for all IAM principals).
     If you want to only show access sessions for a particular IAM principal ID, remove the double-dash (--) from
     the "IAM Principal ID" filter line in the WHERE clause of the query, and replace the placeholder "<IAM PrincipalId>" with the specific ID that you want.
     You can run the query without the filter to determine the exact IAM PrincipalId you want to filter with.

     By default; the query only shows AMS access sessions. If you also want to show non-AMS access sessions,
     remove the "useragent" filter in the WHERE clause of the query.

     For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
   */

   SELECT
      json_extract_scalar(responseelements, '$.assumedRoleUser.assumedRoleId') AS "IAM PrincipalId",
      json_extract_scalar(responseelements, '$.credentials.accessKeyId') AS "IAM SessionId",
      eventtime AS "EventTime",
      eventname AS "EventName",
      awsregion AS "EventRegion",
      eventid AS "EventId",
      json_extract_scalar(requestparameters, '$.tags[0].value') AS "BusinessNeed",
      json_extract_scalar(requestparameters, '$.tags[1].value') AS "BusinessNeedType",
      json_extract_scalar(requestparameters, '$.tags[2].value') AS "Requester",
      json_extract_scalar(requestparameters, '$.tags[3].value') AS "AccessRequestType"
   FROM
       "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate
   WHERE
      datetime > date_format(date_add('day', - 1, CURRENT_DATE), '%Y/%m/%d')
      AND eventname = 'AssumeRole'
      AND useragent = 'access.managedservices.amazonaws.com'
      -- AND  json_extract_scalar(responseelements, '$.assumedRoleUser.assumedRoleId') = '<IAM PrincipalId>'
   ORDER BY eventtime

InsightsQueryString: |-
   # The query provides list of AMS access sessions during specific time range.
   # The query accepts IAM Principal Id as an optional filter and returns event time, business need for accessing the account, requester, ... etc.
   #
   # By default; the IAM Principal ID filter is disabled (it shows access sessions for all IAM principals).
   # If you want to only show access sessions for a particular IAM principal ID, remove the # (#) from
   # the "IAM Principal ID" filter of the query, and replace the placeholder "<IAM PrincipalId>" with the specific ID that you want.
   # You can run the query without the filter to determine the exact IAM PrincipalId you want to filter with.
   #
   # By default; the query only shows AMS access sessions. If you also want to show non-AMS access sessions,
   # remove the "useragent" filter from the query.
   #
   # For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries

   filter eventName="AssumeRole" AND userAgent="access.managedservices.amazonaws.com"
   # | filter responseElements.assumedRoleUser.assumedRoleId= "<IAM PrincipalId>"
   | sort eventTime desc
   | fields
      responseElements.assumedRoleUser.assumedRoleId as IAMPrincipalId,
      responseElements.credentials.accessKeyId as IAMSessionId,
      eventTime as EventTime,
      eventName as EventName,
      awsRegion as EventRegion,
      eventID as EventId,
      requestParameters.tags.0.value as BusinessNeed,
      requestParameters.tags.1.value as BusinessNeedType,
      requestParameters.tags.2.value as Requester,
      requestParameters.tags.3.value as AccessRequestType


```

```
ams_events_query_v1.yaml
/*
  The query provides list of events to track write actions for all AMS changes.
  The query returns all write actions done on the account using that AMS role filter.

  By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

  You can also track mutating actions done by non-AMS roles by removing the "useridentity.arn" filter lines from the WHERE clause of the query.

  For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
*/

SELECT
   useridentity.principalId AS "IAM PrincipalId",
   useridentity.accesskeyid AS "IAM SessionId",
   useridentity.accountid AS "AccountId",
   useridentity.arn AS "RoleArn",
   eventid AS "EventId",
   eventname AS "EventName",
   awsregion AS "EventRegion",
   eventsource AS "EventService",
   eventtime AS "EventTime",
   requestparameters As "RequestParameters",
   responseelements AS "ResponseElements",
   useragent AS "UserAgent"
FROM
   "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate
WHERE
   readonly <> 'true'
   AND
   (
      LOWER(useridentity.arn) LIKE '%/ams%'
      OR LOWER(useridentity.arn) LIKE '%/customer_ssm_automation_role%'
   )
ORDER BY eventtime
```

```
ams_instance_access_sessions_query_v1
/*
  The query provides list of AMS Instance accesses during specific time range.

  The query returns the list of AMS instance accesses; every record includes the event time, the event AWS Region, the instance ID, the IAM session ID, and the SSM session ID.
  You can use the IAM Principal ID to get more details on the business need for accessing the instance by using ams_access_session_query_v1 athena query.
  You can use the SSM session ID to get more details on the instance access session, including the start and end time of the session and log details, using the AWS Session Manager Console in the instance's AWS Region.

  You can also list non-AMS instance accesses by removing the "useridentity" filter line in the WHERE clause of the query.

  By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

  For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
*/

SELECT
   useridentity.principalId AS "IAM PrincipalId",
   useridentity.accesskeyid AS "IAM SessionId",
   json_extract_scalar(requestparameters, '$.target') AS "InstanceId",
   json_extract_scalar(responseelements, '$.sessionId') AS "SSM SessionId",
   eventname AS "EventName",
   awsregion AS "EventRegion",
   eventid AS "EventId",
   eventsource AS "EventService",
   eventtime AS "EventTime"
FROM
   "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate
WHERE
   useridentity.sessionContext.sessionIssuer.arn like '%/ams_%'
   AND eventname = 'StartSession'
ORDER BY eventtime
```

```
ams_privilege_escalation_events_query_v1.yaml
/*
  The query provides list of events that can directly or potentially lead to a privilege escalation.

  The query accepts ActionedBy as an optional filter and returns EventName, EventId, EventTime, ... etc.
  All fields associated with the event are also returned. Some fields are blank if not applicable for that event.
  You can use the IAM Session ID to get more details about events happened in that session by using ams_session_events_query_v1 query.

  By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

  By default, the ActionedBy filter is disabled (it shows privilege escalation events from all users).
  To show events for a particular user or role, remove the double-dash (--) from the useridentity filter line in the WHERE clause of the query
  and replace the placeholder "<ACTIONEDBY_PUT_USER_NAME_HERE>" with an IAM user or role name.
  You can run the query without the filter to determine the exact user you want to filter with.

  For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
*/

SELECT
   useridentity.principalId AS "IAM PrincipalId",
   useridentity.accesskeyid AS "IAM SessionId",
   useridentity.accountid AS "AccountId",
   reverse(split_part(reverse(useridentity.arn), ':', 1)) AS "ActionedBy",
   eventname AS "EventName",
   awsregion AS "EventRegion",
   eventid AS "EventId",
   eventtime AS "EventTime",
   json_extract_scalar(requestparameters, '$.userName') AS "UserName",
   json_extract_scalar(requestparameters, '$.roleName') AS "RoleName",
   json_extract_scalar(requestparameters, '$.groupName') AS "GroupName",
   json_extract_scalar(requestparameters, '$.policyArn') AS "PolicyArn",
   json_extract_scalar(requestparameters, '$.policyName') AS "PolicyName",
   json_extract_scalar(requestparameters, '$.permissionsBoundary') AS "PermissionsBoundary",
   json_extract_scalar(requestparameters, '$.instanceProfileName') AS "InstanceProfileName",
   json_extract_scalar(requestparameters, '$.openIDConnectProviderArn') AS "OpenIDConnectProviderArn",
   json_extract_scalar(requestparameters, '$.serialNumber') AS "SerialNumber",
   json_extract_scalar(requestparameters, '$.serverCertificateName') AS "ServerCertificateName",
   json_extract_scalar(requestparameters, '$.accessKeyId') AS "AccessKeyId",
   json_extract_scalar(requestparameters, '$.certificateId') AS "CertificateId",
   json_extract_scalar(requestparameters, '$.newUserName') AS "NewUserName",
   json_extract_scalar(requestparameters, '$.newGroupName') AS "NewGroupName",
   json_extract_scalar(requestparameters, '$.newServerCertificateName') AS "NewServerCertificateName",
   json_extract_scalar(requestparameters, '$.name') AS "SAMLProviderName",
   json_extract_scalar(requestparameters, '$.sAMLProviderArn') AS "SAMLProviderArn",
   json_extract_scalar(requestparameters, '$.sSHPublicKeyId') AS "SSHPublicKeyId",
   json_extract_scalar(requestparameters, '$.virtualMFADeviceName') AS "VirtualMFADeviceName"
FROM
   "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate
WHERE
   (
     -- More event names can be found at https://docs.aws.amazon.com/IAM/latest/UserGuide/list_identityandaccessmanagement.html
     eventname LIKE 'Add%' OR
     eventname LIKE 'Attach%' OR
     eventname LIKE 'Delete%' AND eventname != 'DeleteAccountAlias' OR
     eventname LIKE 'Detach%' OR
     eventname LIKE 'Create%' AND eventname != 'CreateAccountAlias' OR
     eventname LIKE 'Put%' OR
     eventname LIKE 'Remove%' OR
     eventname LIKE 'Update%' OR
     eventname LIKE 'Upload%' OR
     eventname = 'DeactivateMFADevice' OR
     eventname = 'EnableMFADevice' OR
     eventname = 'ResetServiceSpecificCredential' OR
     eventname = 'SetDefaultPolicyVersion'
   )
   AND eventsource = 'iam.amazonaws.com'
ORDER BY eventtime
```

```
Name: ams_resource_events_query_v1

Description: >-
   The query provides list of events done on specific resource.
   The query accepts resource id as part of the filters, and return all write actions done on that resource.
   By default; the query list the accesses for last day, the user can change the time range by changing the datetime filter.

AthenaQueryString: |-
   /*
     The query provides list of events done on specific resource.

     The query accepts the resource ID as part of the filters (replace the placeholder "<RESOURCE_INFO>" in the WHERE clause of the query),
     and returns all write actions done on that resource. The resource ID can be an ID for any AWS resource in the account.
     Example: An instance ID for an EC2 instance, table name for a DynamoDB table, logGroupName for a CloudWatch Log, etc.

     By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

     For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
   */

   SELECT
      useridentity.principalId AS "IAM PrincipalId",
      useridentity.accesskeyid AS "IAM SessionId",
      useridentity.accountid AS "AccountId",
      reverse(split_part(reverse(useridentity.arn), ':', 1)) AS "ActionedBy",
      eventname AS "EventName",
      awsregion AS "EventRegion",
      eventid AS "EventId",
      eventsource AS "EventService",
      eventtime AS "EventTime"
   FROM
       "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate
   WHERE
      datetime > date_format(date_add('day', - 1, CURRENT_DATE), '%Y/%m/%d')
      AND readonly <> 'true'
      AND
      (
         requestparameters LIKE '%<RESOURCE_INFO>%'
         OR responseelements LIKE '%<RESOURCE_INFO>%'
      )
   ORDER BY eventtime

InsightsQueryString: |-
   # The query provides list of events done on specific resource.
   #
   # The query accepts the resource ID as part of the filters (replace the placeholder "<RESOURCE_INFO>" in the filter of the query),
   # and returns all write actions done on that resource. The resource ID can be an ID for any AWS resource in the account.
   # Example: An instance ID for an EC2 instance, table name for a DynamoDB table, logGroupName for a CloudWatch Log, etc.
   #
   # For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries

   filter readOnly=0
   | parse @message '"requestParameters":{*}' as RequestParameters
   | parse @message '"responseElements":{*}' as ResponseElements
   # | filter RequestParameters like "RESOURCE_INFO" or ResponseElements like "<RESOURCE_INFO>"
   | fields
      userIdentity.principalId as IAMPrincipalId,
      userIdentity.accessKeyId as IAMSessionId,
      userIdentity.accountId as AccountId,
      userIdentity.arn as ActionedBy,
      eventName as EventName,
      awsRegion as EventRegion,
      eventID as EventId,
      eventSource as EventService,
      eventTime as EventTime
   | display IAMPrincipalId, IAMSessionId, AccountId, ActionedBy, EventName, EventRegion, EventId, EventService, EventTime
   | sort eventTime desc
```

```
Name: ams_session_events_query_v1

Description: >-
   The query provides list of events done on specific session.
   The query accepts IAM Principal Id as part of the filters, and return all write actions done on that resource.
   By default; the query list the accesses for last day, the user can change the time range by changing the datetime filter.

AthenaQueryString: |-
   /*
     The query provides a list of events executed on a specific session.

     The query accepts the IAM principal ID as part of the filters (replace the placeholder "<PRINCIPAL_ID>" in the WHERE clause of the query),
     and returns all write actions done on that resource.

     By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

     For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
   */

   SELECT
      useridentity.principalId AS "IAM PrincipalId",
      useridentity.accesskeyid AS "IAM SessionId",
      useridentity.accountid AS "AccountId",
      reverse(split_part(reverse(useridentity.arn), ':', 1)) AS "ActionedBy",
      eventname AS "EventName",
      awsregion AS "EventRegion",
      eventsource AS "EventService",
      eventtime AS "EventTime",
      requestparameters As "RequestParameters",
      responseelements AS "ResponseElements",
      useragent AS "UserAgent"
   FROM
       "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate   WHERE
      useridentity.principalid = '<PRINCIPAL_ID>'
      AND datetime > date_format(date_add('day', - 1, CURRENT_DATE), '%Y/%m/%d')
      AND readonly <> 'true'
   ORDER BY eventtime

InsightsQueryString: |-
   # The query provides a list of events executed on a specific session.
   #
   # The query accepts the IAM principal ID as part of the filters (replace the placeholder "<PRINCIPAL_ID>" in the filter of the query),
   # and returns all write actions done on that resource.
   #
   # For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries

   filter readOnly=0 AND userIdentity.principalId = "<IAM Principal>"
   | sort eventTime desc
   | fields
      userIdentity.accessKeyId as IAMSessionId,
      userIdentity.principalId as IAMPrincipalId,
      userIdentity.accountId as AccountId,
      userIdentity.arn as ActionedBy,
      eventName as EventName,
      awsRegion as EventRegion,
      eventSource as EventService,
      eventTime as EventTime,
      userAgent as UserAgent
   | parse @message '"requestParameters":{*}' as RequestParameters
   | parse @message '"responseElements":{*}' as ResponseElements
```

```
Name: ams_session_ids_by_requester_v1

Description: >-
   The query provides list of IAM Principal/Session Ids for specific requester.
   The query accepts requester and return all IAM Principal/Session Ids by that requester during specific time range.
   By default; the query list the accesses for last day, the user can change the time range by changing the datetime filter.

AthenaQueryString: |-
   /*
     The query provides list of IAM Principal IDs for a specific requester.

     The query accepts the requester (replace placeholder "<Requester>" in the WHERE clause of the query),
     and returns all IAM Principal IDs by that requester during a specific time range.

     By default, the query filters the last day's events only; you can change the "datetime" filter to search for a wider time range.

     For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
   */

   SELECT
      json_extract_scalar(responseelements, '$.assumedRoleUser.assumedRoleId') AS "IAM PrincipalId",
      json_extract_scalar(responseelements, '$.credentials.accessKeyId') AS "IAM SessionIId",
      eventtime AS "EventTime"
   FROM
       "{DATABASE NAME HERE}".{TABLENAME HERE} <- This should auto-populate
   WHERE
      datetime > date_format(date_add('day', - 1, CURRENT_DATE), '%Y/%m/%d')
      AND json_extract_scalar(requestparameters, '$.tags[2].value') = '<Requester>'
   ORDER BY eventtime

InsightsQueryString: |-
   # The query provides list of IAM Principal IDs for a specific requester.
   #
   # The query accepts the requester (replace placeholder "<Requester>" in the filter of the query),
   # and returns all IAM Principal IDs by that requester during a specific time range.
   #
   # For expected inputs and scenarios, refer to AMS Documentation -> Tracking changes in your AMS Accelerate accounts -> Default Queries
   filter eventName="AssumeRole" AND requestParameters.tags.2.value="<Requester>"
   | sort eventTime desc
   | fields
      responseElements.assumedRoleUser.assumedRoleId as IAMPrincipalId,
      responseElements.credentials.accessKeyId as IAMSessionId,
      eventTime as EventTime
```

## Change record permissions

The following permissions are needed to run change record queries:

- **Athena**
  - athena:GetWorkGroup
  - athena:StartQueryExecution
  - athena:ListDataCatalogs
  - athena:GetQueryExecution
  - athena:GetQueryResults
  - athena:BatchGetNamedQuery
  - athena:ListWorkGroups
  - athena:UpdateWorkGroup
  - athena:GetNamedQuery
  - athena:ListQueryExecutions
  - athena:ListNamedQueries

- **AWS KMS**
  - kms:Decrypt
  - AWS KMS key ID of AMSCloudTrailLogManagement, or your AWS KMS key ID(s), if Accelerate is using your CloudTrail trail events Amazon S3 bucket data store using [SSE-KMS](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") encryption.

- **AWS Glue**
  - glue:GetDatabase
  - glue:GetTables
  - glue:GetDatabases
  - glue:GetTable

- **Amazon S3 read access**
  - Amazon S3 bucket CloudTrail datastore: ams-a`AccountId`-cloudtrail-`primary region`, or your Amazon S3 bucket name, CloudTrail trail events Amazon S3 bucket data store.

- **Amazon S3 write access**
  - Athena events query results Amazon S3 bucket: ams-a`AccountId`athena-results-`primary region`
