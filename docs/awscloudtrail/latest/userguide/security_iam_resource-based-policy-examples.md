# AWS CloudTrail resource-based policy examples

This section provides example resource-based polices for CloudTrail Lake dashboards, event data stores, and channels.

CloudTrail supports the following types of resource-based policies:


* Resource-based policies on channels used for CloudTrail Lake integrations with event sources outside of AWS. The
 resource-based policy for the channel defines which principal entities (accounts, users,
 roles, and federated users) can call `PutAuditEvents` on the channel to deliver events to the destination event data store. For more information about 
 creating integrations with CloudTrail Lake, see [Create an integration with an event
 source outside of AWS](query-event-data-store-integration.md "query-event-data-store-integration.md").
* Resource-based polices to control which principals can perform actions on your event data store. 
 You can use resource-based policies to provide cross-account access to your event data stores.
* Resource-based policies on dashboards to allow CloudTrail to refresh a CloudTrail Lake dashboard at the interval you define when you set a refresh schedule for a dashboard. For more information, see [Set a refresh schedule for a custom dashboard
 with the CloudTrail console](lake-dashboard-refresh.md "lake-dashboard-refresh.md").
###### Examples:

* [Resource-based policy examples for channels](#security_iam_resource-based-policy-examples-channels "#security_iam_resource-based-policy-examples-channels")
* [Resource-based policy examples for event data stores](#security_iam_resource-based-policy-examples-eds "#security_iam_resource-based-policy-examples-eds")
* [Resource-based policy example for a dashboard](#security_iam_resource-based-policy-examples-dashboards "#security_iam_resource-based-policy-examples-dashboards")

## Resource-based policy examples for channels


The resource-based policy for the channel defines which principal entities (accounts, users,
 roles, and federated users) can call `PutAuditEvents` on the channel to deliver events to the destination event data store.


The information required for the policy is determined by the integration
 type.



* For a direction integration, CloudTrail requires the policy to contain the partner's
 AWS account IDs, and requires you to enter the unique external ID provided by the
 partner. CloudTrail automatically adds the partner's AWS account IDs to the resource
 policy when you create an integration using the CloudTrail console. Refer to the [partner's documentation](query-event-data-store-integration.md#cloudtrail-lake-partner-information#lake-integration-partner-documentation "query-event-data-store-integration.md#cloudtrail-lake-partner-information#lake-integration-partner-documentation") to learn how to get the AWS account numbers
 required for the policy.
* For a solution integration, you must specify at least one AWS account ID as
 principal, and can optionally enter an external ID to prevent against confused
 deputy.

The following are requirements for the resource-based policy:



* The policy contains at least one statement. The policy can have a maximum of 20
 statements.
* Each statement contains at least one principal. A principal is an account, user, role, or federated user. A statement can have a maximum of 50 principals.
* The resource ARN defined in the policy must match the channel ARN the policy is attached to.
* The policy contains only one action: `cloudtrail-data:PutAuditEvents`

The channel owner can call the `PutAuditEvents` API on the channel unless the policy denies the owner access to the resource.


###### Topics

* [Example: Providing
 channel access to principals](#security_iam_resource-based-policy-examples-principals "#security_iam_resource-based-policy-examples-principals")
* [Example: Using an external ID to prevent against confused deputy](#security_iam_resource-based-policy-examples-externalID "#security_iam_resource-based-policy-examples-externalID")

### Example: Providing
 channel access to principals


The following example grants permissions to the principals with the ARNs
 `arn:aws:iam::111122223333:root`, `arn:aws:iam::444455556666:root`, and 
 `arn:aws:iam::123456789012:root` to call the [PutAuditEvents](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html "https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html") API on the CloudTrail channel with the ARN `arn:aws:cloudtrail:us-east-1:777788889999:channel/EXAMPLE-80b5-40a7-ae65-6e099392355b`. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":
 [
 {
 "Sid": "ChannelPolicy",
 "Effect": "Allow",
 "Principal":
 {
 "AWS":
 [
 "arn:aws:iam::`111122223333`:root",
 "arn:aws:iam::444455556666:root",
 "arn:aws:iam::123456789012:root"
 ]
 },
 "Action": "cloudtrail-data:PutAuditEvents",
 "Resource": "arn:aws:cloudtrail:us-east-1:777788889999:channel/EXAMPLE-80b5-40a7-ae65-6e099392355b"
 }
 ]
}`

```





### Example: Using an external ID to prevent against confused deputy


The following example uses an external ID to address and prevent against [confused deputy](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"). 
 The confused deputy problem is a security issue where an entity that doesn't have 
 permission to perform an action can coerce a more-privileged entity to perform the action. 
 


The integration partner creates the external ID to use in the policy. Then, it
 provides the external ID to you as part of creating the integration. The value can be
 any unique string, such as a passphrase or account number. 


The example grants permissions to the principals with the ARNs
 `arn:aws:iam::111122223333:root`, `arn:aws:iam::444455556666:root`, and 
 `arn:aws:iam::123456789012:root` to call the [PutAuditEvents](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html "https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html") API on the CloudTrail channel resource if the call to the `PutAuditEvents` API includes the 
 external ID value defined in the policy. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":
 [
 {
 "Sid": "ChannelPolicy",
 "Effect": "Allow",
 "Principal":
 {
 "AWS":
 [
 "arn:aws:iam::`111122223333`:root",
 "arn:aws:iam::444455556666:root",
 "arn:aws:iam::123456789012:root"
 ]
 },
 "Action": "cloudtrail-data:PutAuditEvents",
 "Resource": "arn:aws:cloudtrail:us-east-1:777788889999:channel/EXAMPLE-80b5-40a7-ae65-6e099392355b"
 }
 ]
}`

```





## Resource-based policy examples for event data stores


Resource-based policies allow you to control which principals can perform actions on your event data store.


You can use resource-based policies to provide cross-account access to allow selected principals 
 to query your event data store, list and cancel queries, and view query results. 


For CloudTrail Lake dashboard, resource-based policies are used to allow CloudTrail to run
 queries on your event data stores to populate the data for the dashboard's widgets when the dashboard is
 refreshed. CloudTrail Lake gives you the option to attach a default resource-based policy to
 your event data stores when you [create a custom dashboard](lake-dashboard-custom.md "lake-dashboard-custom.md") or [enable the Highlights
 dashboard](lake-dashboard-highlights.md "lake-dashboard-highlights.md") on the CloudTrail console.


The following actions are supported in resource-based policies for event data stores:



* `cloudtrail:StartQuery`
* `cloudtrail:CancelQuery`
* `cloudtrail:ListQueries`
* `cloudtrail:DescribeQuery`
* `cloudtrail:GetQueryResults`
* `cloudtrail:GenerateQuery`
* `cloudtrail:GenerateQueryResultsSummary`
* `cloudtrail:GetEventDataStore`

When you [create](query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure "query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure") or [update](query-event-data-store-update.md "query-event-data-store-update.md") an event data store, or manage dashboards on the CloudTrail console, you’re given the option to add a resource-based policy to your event data store.
 You can also run the [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-resource-policy.html "https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-resource-policy.html") command to attach a resource-based policy to an event data store.


A resource-based policy consists of one or more statements. For example, it can
 include one statement that allows CloudTrail to query the event data store for a
 dashboard and another statement that allows cross-account access to query the event data
 store. You can [update](query-event-data-store-update.md "query-event-data-store-update.md") an existing
 event data store's resource-based policy from the event data store's details
 page on the CloudTrail console.


For [organization event data stores](cloudtrail-lake-organizations.md "cloudtrail-lake-organizations.md"), CloudTrail creates a [default resource-based policy](cloudtrail-lake-organizations.md#cloudtrail-lake-organizations-eds-rbp "cloudtrail-lake-organizations.md#cloudtrail-lake-organizations-eds-rbp") that
 lists the actions that the delegated administrator accounts are allowed to perform on organization event data stores. The permissions in this policy are derived from the delegated
 administrator permissions in AWS Organizations. This policy is updated automatically following changes to the organization event data store or to the organization 
 (for example, a CloudTrail delegated administrator account is registered or removed).


###### Examples:

* [Example:
 Allow CloudTrail to run queries to refresh a dashboard](#security_iam_resource-based-policy-examples-eds-dashboard "#security_iam_resource-based-policy-examples-eds-dashboard")
* [Example: Allow other accounts to query an event data store and view query results](#security_iam_resource-based-policy-examples-eds-query "#security_iam_resource-based-policy-examples-eds-query")

### Example:
 Allow CloudTrail to run queries to refresh a dashboard


To populate the data on a CloudTrail Lake dashboard during a refresh, you need to allow CloudTrail to run queries on your behalf. 
 To do this, attach a resource-based policy to each event data store associated with a dashboard widget that includes a statement that allows CloudTrail 
 to perform the `StartQuery` operation to populate the data for the widget.


The following are the requirements for the statement:



* The only `Principal` is `cloudtrail.amazonaws.com`.
* The only `Action` allowed is `cloudtrail:StartQuery`.
* The `Condition` only includes the dashboard ARN(s) and AWS account ID. For `AWS:SourceArn`, you can provide an array of dashboard ARNs.

The following example policy includes a statement that allows CloudTrail to run queries
 on an event data store for two custom dashboards named
 `example-dashboard1` and `example-dashboard2` and the
 Highlights dashboard named `AWSCloudTrail-Highlights` for account
 `123456789012`.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":
 [
 {
 "Effect": "Allow",
 "Principal":
 {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action":
 [
 "cloudtrail:StartQuery"
 ],
 "Resource": "arn:aws:cloudtrail:`us-east-1`:`123456789012`:dashboard/*",
 "Condition": {
 "StringLike": {
 "AWS:SourceArn": [
 "arn:aws:cloudtrail:us-east-1:123456789012:dashboard/example-dashboard1",
 "arn:aws:cloudtrail:us-east-1:123456789012:dashboard/example-dashboard2",
 "arn:aws:cloudtrail:us-east-1:123456789012:dashboard/AWSCloudTrail-Highlights"
 ],
 "AWS:SourceAccount": "123456789012"
 }
 }
 }
 ]
}`

```





### Example: Allow other accounts to query an event data store and view query results


You can use resource-based policies to provide cross-account access to 
 your event data stores to allow other accounts to run queries on your event data stores.


The following example policy includes a statement that allows root users in accounts `111122223333`, `777777777777`, 
 `999999999999`, and `111111111111` to run queries and get query results on the event data store owned by account ID `555555555555`. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "policy1",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root",
 "arn:aws:iam::777777777777:root",
 "arn:aws:iam::999999999999:root",
 "arn:aws:iam::111111111111:root"
 ]
 },
 "Action": [
 "cloudtrail:StartQuery",
 "cloudtrail:GetEventDataStore",
 "cloudtrail:GetQueryResults"
 ],
 "Resource": "arn:aws:cloudtrail:us-east-1:555555555555:eventdatastore/example80-699f-4045-a7d2-730dbf313ccf"
 }
 ]
}`

```





## Resource-based policy example for a dashboard


You can set a refresh schedule for a CloudTrail Lake dashboard, which allows CloudTrail to refresh the dashboard on your behalf at the interval you define when you set the refresh schedule. To do this, 
 you need to attach a resource-based policy to the dashboard to allow CloudTrail to perform the `StartDashboardRefresh` operation on your dashboard.


The following are requirements for the resource-based policy:



* The only `Principal` is `cloudtrail.amazonaws.com`.
* The only `Action` allowed in the policy is `cloudtrail:StartDashboardRefresh`.
* The `Condition` only includes the dashboard ARN and AWS account ID.

The following example policy allows CloudTrail to refresh a dashboard named `exampleDash` for account `123456789012`.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":
 [
 {
 "Effect": "Allow",
 "Principal":
 {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action":
 [
 "cloudtrail:StartDashboardRefresh"
 ],
 "Resource": "arn:aws:cloudtrail:`us-east-1`:`123456789012`:dashboard/*",
 "Condition": {
 "StringEquals": {
 "AWS:SourceArn": "arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash",
 "AWS:SourceAccount":"123456789012"
 }
 }
 }
 ]
}`

```
