# Available managed dashboards

The section provides information about the available managed dashboards and
 provides information about the widgets featured on each dashboard.

###### Available managed dashboards:

* [Security monitoring
 dashboard](#lake-managed-dashboard-security "#lake-managed-dashboard-security")
* [IAM activity dashboard](#lake-managed-dashboard-iam "#lake-managed-dashboard-iam")
* [User activity dashboard](#lake-managed-dashboard-user "#lake-managed-dashboard-user")
* [Enriched events dashboard](#lake-managed-dashboard-enriched-events "#lake-managed-dashboard-enriched-events")
* [Error analysis dashboard](#lake-managed-dashboard-error "#lake-managed-dashboard-error")
* [EC2 activity dashboard](#lake-managed-dashboard-ec2 "#lake-managed-dashboard-ec2")
* [Organizations activity
 dashboard](#lake-managed-dashboard-organizations "#lake-managed-dashboard-organizations")
* [Resource changes
 dashboard](#lake-managed-dashboard-resources "#lake-managed-dashboard-resources")
* [Data events overview
 dashboard](#lake-managed-dashboard-data "#lake-managed-dashboard-data")
* [Lambda data events
 dashboard](#lake-managed-dashboard-lambda "#lake-managed-dashboard-lambda")
* [DynamoDB data events
 dashboard](#lake-managed-dashboard-dynamodb "#lake-managed-dashboard-dynamodb")
* [S3 data events dashboard](#lake-managed-dashboard-s3 "#lake-managed-dashboard-s3")
* [Insights events dashboard](#lake-managed-dashboard-insights "#lake-managed-dashboard-insights")
* [Management events
 dashboard](#lake-managed-dashboard-mgmt "#lake-managed-dashboard-mgmt")
* [Overview dashboard](#lake-managed-dashboard-overview "#lake-managed-dashboard-overview")

## Security monitoring
 dashboard


This dashboard provides a centralized view of critical security focused
 widgets, such as top access denied events, failed console login attempts and
 their associated IP addresses, root user console login attempts, destructive
 actions, cross-account access and other critical security focused widgets. It
 provides quick incident detection and response to enhance your overall security
 posture.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Top access denied events**

Tracks the most frequently occurring access-denied events, grouped
 by API.



**Failed ConsoleLogin attempts**

Tracks the trend of failed console login attempts over time, with
 breakdowns on MFA vs Non-MFA authenticated callers. 



**Failed ConsoleLogin attempts by IP address**

Tracks the IP addresses associated with failed console login
 attempts and displays the top offending IP addresses by failed login
 count.



**Root user ConsoleLogin attempts**

Tracks the frequency of console login attempts made by root users
 over time.



**Destructive actions**

Tracks the frequency of delete operations over time.



**Top cross-account access**

Tracks the top cross-account activity by caller account ID and
 action.



**Users who disabled MFA**

Tracks the most recent users who disabled MFA.



**Recent EC2 SecurityGroup and NetworkAcl changes**

Tracks the most recent EC2 SecurityGroup and NetworkAcl
 changes.



**Recent EC2 SecurityGroup changes that allow public access**

Tracks the most recent EC2 security groups that have rules
 allowing public (0.0.0.0/0) access.



**Potential CloudTrail disabling actions**

Tracks recent actions that risk disrupting CloudTrail
 logging.




## IAM activity dashboard


This dashboard provides visibility into commonly used IAM APIs, API errors,
 changes to IAM entities, and top caller IP addresses, enabling the
 identification of unintended IAM actions and compliance issues.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Top IAM APIs**

Tracks the most frequently used IAM APIs.



**Top IAM callers**

Tracks the most frequent IAM API callers.



**IAM success vs failure trend**

Tracks the trend of success and failed IAM API calls over
 time.



**Top IAM API errors**

Tracks the most frequent errors in calling IAM APIs.



**Top AccessDenied IAM APIs**

Tracks the most frequent IAM API calls that failed with access
 denied errors.



**Top IP addresses of IAM calls**

Tracks the top source IP addresses from which IAM API calls were
 made.



**Recent IAM policy changes**

Tracks the most recent changes to IAM policies, categorized by the
 specific IAM API operation that facilitated the change, the IAM
 resource (user, role, or group) associated with the policy change,
 and the policy name or ARN that was used.



**Recent IAM user changes**

Tracks the most recent changes to IAM users, categorized by the
 specific IAM API that facilitates user management, the IAM user
 affected by the change, and the event time.



**Top assumed IAM roles**

Tracks the most frequently assumed IAM roles.




## User activity dashboard


This dashboard provides visibility into user activity trends, insights into
 key areas such as top active users, user traffic patterns, users with access
 denied errors, recent user operations, users who performed destructive
 activities and IAM policy changes, as well as privileged user actions. It
 helps detect unintended user actions and security risks.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**User activity trends by user ARN**

Tracks the user activity trend over time by user ARN.



**User activity trends by API**

Tracks the user activity trend over time by API.



**Most recent user activity**

Tracks the most recent user actions. 



**Top users with errors**

Tracks the users that have the highest number of errors.



**Top users with AccessDenied errors**

Tracks the users that have the highest number of AccessDenied
 errors. 



**Top users making destructive actions**

Tracks the users that are making the highest number of destructive
 actions. 



**Top users changing IAM policies**

Tracks the IAM users who are frequently performing changes to IAM
 policies.



**Top actions performed by potential IAM privileged users**

Tracks the most frequent actions by highly privileged IAM users,
 such as administrators.




## Enriched events dashboard


This enriched events dashboard provides 
 insights on trends across tagged resources, principal activities, and
 AWS global condition keys. These insights help you analyze the most frequent
 resource and principal tag distributions as well as frequently used global condition
 keys in role sessions, requests, and principals in request context.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Enriched events over time**

Tracks the count of enriched events over time.



**Most frequent resource tag key value pairs**

Displays the most frequently used resource tag key-value pairs across enriched events. 



**Most frequent resource tag key value pairs with associated resources and users**

Displays the most frequently used resource tag key-value pairs, showing which resources use these tags and which users are associated with them.



**Most frequent principal tag key value pairs**

Displays the most frequently used principal tag key-value pairs across enriched events.



**Most frequent access denied actions grouped by principal tag key value pairs**

Displays the most frequent access-denied actions grouped by principal tag key-value pairs across enriched events.



**Most frequent principal properties in IAM global condition keys**

Displays the most frequently used IAM global condition keys for principal properties, showing their key-value pairs and counts across all events.



**Most frequent request properties in IAM global condition keys**

Displays the most frequently used IAM global condition keys for request properties, showing their key-value pairs and counts across all events.



**Most frequent role session properties in IAM global condition keys**

Displays the most frequently used IAM global condition keys for role session properties, showing their key-value pairs and counts across all events.




## Error analysis dashboard


This dashboard provides comprehensive insights into error trends across
 services, APIs, users, error codes, and throttled APIs. The visibility enables
 prompt identification and troubleshooting of potential availability issues for
 optimal system performance.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Error count by service**

Tracks the error count of activities by service.



**Error count by API**

Tracks the error count of activities by API.



**Top errors by error code**

Tracks the most frequent errors by error code.



**Top errors by error message**

Tracks the most frequent errors by error message.



**Top AccessDenied errors by API**

Tracks the APIs with the most frequently reported access denied
 errors.



**Top throttled errors by API**

Tracks the APIs with the most frequently reported throttled
 errors.



**Top users with errors**

Tracks the users with the most frequently reported errors.




## EC2 activity dashboard


This dashboard provides comprehensive visibility into EC2 management
 activities, like API trends, access errors, top instance launchers, security
 changes, and network modifications. The insights help identify security risks
 and operational issues.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**EC2 instance management activity overview**

Monitors an overview of EC2 instance management activities over a
 specified time, highlighting key operations such as launches, stops,
 and terminations.



**EC2 API success vs failure trends**

Tracks the trend of success and failed EC2 API calls over
 time.



**Top EC2 errors**

Tracks the most frequent error codes that occur during EC2 API
 calls.



**Top EC2 AccessDenied events**

Tracks EC2 APIs with the most access denied errors.



**Top users launching EC2 instances**

Tracks the users who are the most active in launching new EC2
 instances.



**Recent EC2 SecurityGroup and NetworkInterface changes**

Tracks the most recent EC2 security group and network interface
 changes. 



**Recent VPC management and route table changes**

Tracks the most recent VPC management activities and route table
 changes. 



**Recent EC2 actions by root user**

Tracks the most recent EC2 actions performed by root users with highly privileged permissions.




## Organizations activity
 dashboard


Designed for organization event data stores, this dashboard offers visibility
 into organizational activities and trends, including insights on active members,
 account management, access patterns, policy changes, and top services and APIs
 utilized.


This dashboard is available for organization event data stores and includes
 the following widgets:




**Activity trend in the organization**

Tracks the overall activity trend across the entire AWS Organizations
 organization over time, providing visibility into periods of high or
 low activity levels.



**Member account management summary**

Tracks the distribution of member account management activities
 within the organization, categorized based on the counts of each
 activity type.



**Most used services across organization**

Tracks the AWS services that have been utilized the most across
 the organization.



**Most active accounts by service**

Tracks the most active accounts utilizing an AWS service across
 the organization.



**Most used APIs across organization**

Highlights the AWS APIs that have been invoked most frequently
 across the entire organization.



**Most active member accounts**

Tracks the member accounts within the organization that have
 exhibited the highest count of activity.



**Access denied errors trend across the organization**

Tracks the pattern of access denied errors occurring within the
 organization over time.



**Accounts with most access denied errors** 

Tracks the accounts within the organization that have experienced
 the highest number of access denied errors.



**Recent service control policy changes**

Tracks the most recent changes made to service control policies
 (SCPs) within the organization.




## Resource changes
 dashboard


This dashboard provides a comprehensive view of resource management
 activities, monitoring trends in provisioning, deletion, and modifications
 across services. It highlights critical changes, including those made through
 AWS CloudFormation, manually, and to policies like S3 bucket and KMS access.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Resource creation and deletion trends**

Tracks the creation and deletion of resources within the account
 over time.



**Top users performing resource creation**

Tracks the users who are most actively creating new
 resources.



**Top APIs used for resource creation**

Tracks the APIs that are most frequently used for creating new
 resources within the account.



**Top APIs used for resource deletion**

Tracks the APIs that are most frequently used for deleting
 resources within the account.



**Most recent resources created outside CloudFormation**

Tracks new resources created outside of CloudFormation governance,
 emphasizing changes not managed through CloudFormation
 templates.



**Most recent resource changes made using console**

 Tracks the most recent changes made to resources via the
 AWS Management Console.



**Most recent S3 bucket access changes**

Tracks the most recent S3 bucket access changes. 



**Most recent KMS key access changes**

Tracks the most recent KMS key policy changes. 




## Data events overview
 dashboard


This dashboard offers a centralized view of data events in the event data
 store, including overall activity trends, top services, APIs, regions, throttled
 data plane APIs, and leading data plane users. This dashboard helps you monitor
 data plane API activity for auditing and troubleshooting.


This dashboard is available for event data stores that collect data events and
 includes the following widgets:




**Overall data events trend**

Tracks the trend in overall data events occurring within the
 account over time.



**Top services generating data events**

Tracks the services generating the highest volume of data activity
 within the account.



**Top APIs generating data events**

Tracks the APIs generating the highest volume of data activity
 within the account.



**Top regions generating data events**

Tracks the regions generating the highest volume of data activity
 within the account.



**Top throttled data plane APIs**

Tracks the data plane APIs that are experiencing frequent
 throttling within the account.



**Top users of data plane APIs**

Tracks the top users who utilize data plane APIs most across the
 account.




## Lambda data events
 dashboard


This dashboard provides visibility into Lambda data plane API activity,
 including top users, frequently invoked functions, common API errors. These
 insights help you audit Lambda usage, detect abnormalities, and mitigate
 operational or security risks.


This dashboard is available for event data stores that collect Lambda data
 events and includes the following widgets:




**Lambda data plane API activity**

Tracks the trend in Lambda data plane API activity within the
 account over time.



**Lambda invocations success vs failure trend**

Tracks the trend of success and failed Lambda invocations over
 time.



**Top users of Lambda invocations**

Tracks the users who make the most invocations of Lambda functions
 across the account.



**Top invoked Lambda functions**

Tracks the Lambda functions that are invoked most frequently
 within the account.



**Top 10 Lambda Invoke API errors**

Tracks the top 10 errors encountered during Lambda Invoke API
 calls.



**Most throttled users of Lambda invocations**

Tracks the users who experience the highest number of throttling
 events for Lambda invocations.




## DynamoDB data events
 dashboard


This dashboard provides visibility into DynamoDB data plane API activity,
 including usage trends, top APIs, and throttling patterns involving users and
 tables. These insights help you audit DynamoDB usage, detect abnormalities, and
 mitigate operational or security risks.


This dashboard is available for event data stores that collect DynamoDB data
 events and includes the following widgets:




**DynamoDB account data activity**

Tracks the trend in DynamoDB data events occurring within the
 account over time.



**DynamoDB data plane APIs success vs failure trend**

Tracks the trend of success and failed DynamoDB data plane API
 calls over time.



**Top 10 DynamoDB data plane APIs**

Lists the top 10 DynamoDB data plane API calls.



**Top users of DynamoDB data plane APIs**

Tracks the users who make the highest number of calls to DynamoDB
 data plane APIs within the account.



**Top 10 DynamoDB data plane API errors**

Tracks the top 10 errors in calling DynamoDB data plane
 APIs.



**Most throttled users of DynamoDB data plane APIs**

Tracks the users with most frequent throttling when calling
 DynamoDB data plane APIs.



**Top throttled DynamoDB data plane APIs**

Tracks the DynamoDB data plane APIs that are experiencing frequent
 throttling within the account.



**Top throttled DynamoDB tables**

Tracks the DynamoDB tables experiencing the highest rates of
 throttling within the account.




## S3 data events dashboard


This dashboard provides visibility into S3 data plane API activity, including
 usage trends, most accessed S3 objects, top S3 users, and top S3 actions. These
 insights help you audit S3 usage, detect abnormalities, and mitigate operational
 or security risks.


This dashboard is available for event data stores that collect Amazon S3 data
 events and includes the following widgets:




**S3 account activity**

Tracks S3 account activity.



**Most accessed objects**

Lists the most accessed S3 objects.



**S3 top users**

Tracks the top S3 users. 



**Top S3 actions**

Tracks the top S3 actions.




## Insights events dashboard


This dashboard provides visibility into the overall breakdown of Insights events by
 type, as well as the top users and services generating these event types.
 Additionally, it shows the daily count of Insights events and a 30-day historical view of
 Insights metrics.


###### Note


* After you enable CloudTrail Insights for the first time on the source event data store, it can take up to 7 days for CloudTrail to deliver the first Insights event, 
 if unusual activity is detected.
* The **Insights Events** dashboard only displays information about the Insights events collected 
 by the selected event data store, which is determined by the configuration of the source event data store. For example, 
 if you configure the source event data store to enable Insights events on `ApiCallRateInsight` but not `ApiErrorRateInsight`, 
 you won't see information about Insights events on `ApiErrorRateInsight`.

This dashboard is available for event data stores that collect Insights events and
 includes the following widgets:




**Insight types**

Tracks events by Insights type.



**Insights by date**

Tracks Insights events by date. 



**API call rate Insights by event source**

Tracks API call rate Insights by event source. To view data for
 this widget, your Insights event data store must be configured to
 collect Insights on API call rate.



**API error rate Insights by event source**

Tracks API error rate Insights by event source. To view this
 widget, your Insights event data store must be configured to collect
 Insights on API error rate.



**Insights by top users**

Lists the top users with requests resulting in Insights
 events.



**Insights events**

Lists recent Insights events.




## Management events
 dashboard


This dashboard highlights insights on access denied events, destructive
 actions, console sign-in events, top errors by user, TLS version usage, and
 outdated TLS calls by user.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Top access denied events**

Tracks the top events that resulted in access denied
 errors.



**Top errors by user**

Tracks the top errors by user.



**Console sign-in events**

Shows console sign-in events.



**Destructive actions**

Tracks actions that resulted in destructive actions.



**TLS version**

Shows the TLS versions.



**Outdated TLS calls by user**

Tracks calls using outdated TLS versions by user.




## Overview dashboard


This dashboard highlights insights on access denied events, destructive
 actions, console sign-in events, top errors by user, TLS version usage, and
 outdated TLS calls by user.


This dashboard is available for event data stores that collect management
 events and includes the following widgets:




**Account activity**

Tracks read and write activity for your account. 



**Top errors**

Lists the most frequent errors.



**Most active regions**

Shows the most active AWS Regions.



**Top services**

Shows the top services.



**Most throttled events**

Lists the most throttled events.



**Top users**

Lists the top users.
