# CloudTrail Lake dashboards

You can use CloudTrail Lake dashboards to see event trends for the event data stores in your account. CloudTrail Lake
 offers the following types of dashboards:


* **Managed dashboards** – You can view a
 managed dashboard to see event trends for an event data store that collects
 management events, data events, or Insights events. These dashboards are
 automatically available to you and are managed by CloudTrail Lake. 
 CloudTrail offers 14 managed dashboards to choose from. You can manually refresh managed dashboards. You cannot modify, add, or remove the widgets for these dashboards, 
 however, you can save a managed dashboard as a custom dashboard 
 if you want to modify the widgets or set a refresh schedule.
* **Custom dashboards** – Custom dashboards allow you to query 
 events in any event data store type. You can add up to 10 widgets to a custom dashboard. You can manually refresh a custom dashboard, or you can set a refresh schedule.
* **Highlights dashboards** – Enable the Highlights dashboard to view an at-a-glance overview of the 
AWS activity collected by the event data stores in your account. The Highlights dashboard is managed by CloudTrail 
and includes widgets that are relevant to your account. The widgets shown on the Highlights 
dashboard are unique to each account. These widgets could surface detected abnormal activity or anomalies. 
For example, your Highlights dashboard could include the **Total cross-account access widget**, 
which shows if there is an increase in abnormal cross-account activity. CloudTrail updates the Highlights dashboard every 6 hours. 
The dashboard shows the last 24 hours of data from the last update.
Each dashboard consists of one or more widgets and each widget provides a graphical
 representation of the results of a SQL query. To view the query for a widget, choose
 **View and edit query** to open up the query editor.

When a dashboard is refreshed, CloudTrail Lake runs queries to populate the dashboard's widgets.
 Because running queries incurs costs, CloudTrail asks you to acknowledge the costs associated with
 running queries. For more information about CloudTrail pricing, see [CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Topics

* [Prerequisites](#lake-dashboard-prerequisites "#lake-dashboard-prerequisites")
* [Limitations](#lake-dashboard-limitations "#lake-dashboard-limitations")
* [Region support](#lake-dashboard-regions "#lake-dashboard-regions")
* [Required permissions](#lake-dashboard-permissions "#lake-dashboard-permissions")
* [View a managed dashboard with the CloudTrail
 console](lake-dashboard-managed.md "lake-dashboard-managed.md")
* [Enable the Highlights dashboard with the
 CloudTrail console](lake-dashboard-highlights.md "lake-dashboard-highlights.md")
* [Disable the Highlights dashboard
 with the CloudTrail console](lake-dashboard-highlights-disable.md "lake-dashboard-highlights-disable.md")
* [Create a custom dashboard with the CloudTrail
 console](lake-dashboard-custom.md "lake-dashboard-custom.md")
* [Set a refresh schedule for a custom dashboard
 with the CloudTrail console](lake-dashboard-refresh.md "lake-dashboard-refresh.md")
* [Disable the refresh schedule for a
 custom dashboard with the CloudTrail console](lake-dashboard-refresh-disable.md "lake-dashboard-refresh-disable.md")
* [Change termination protection with
 the CloudTrail console](lake-dashboard-termination-protection.md "lake-dashboard-termination-protection.md")
* [Delete a custom dashboard with the CloudTrail
 console](lake-dashboard-delete.md "lake-dashboard-delete.md")
* [Create, update, and manage dashboards with the AWS CLI](lake-dashboard-cli.md "lake-dashboard-cli.md")

## Prerequisites


The following prerequisites apply to CloudTrail Lake dashboards:



* To view and use Lake dashboards, you must create at least one CloudTrail Lake event
 data store. You can create event data stores using the console, AWS CLI, or SDKs.
 For information about creating an event data store using the console, see [Create an event data store for CloudTrail
 events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md"). For information about
 creating an event data store using the AWS CLI, see [Create an event data store with the AWS CLI](lake-cli-create-eds.md "lake-cli-create-eds.md").
* You must have adequate permissions to view, create, update, and refresh
 dashboards. For more information, see [Required permissions](#lake-dashboard-permissions "#lake-dashboard-permissions").

## Limitations


The following limitations apply to CloudTrail Lake dashboards:



* You can only enable the Highlights dashboard for event data stores that exist in your account.
* You can only view managed dashboards for event data stores that exist in your account.
* For custom dashboards, you can only add sample widgets or create new widgets that query event data stores that exist in your account.
* Delegated administrators for a AWS Organizations organization cannot view or manage dashboards that are owned by the management account.

## Region support


The CloudTrail Lake dashboards are supported in all AWS Regions where CloudTrail Lake is
 supported.


The **Activity summary** widget on the
 **Highlights** dashboard is supported in the following
 Regions:



* Asia Pacific (Tokyo) Region (ap-northeast-1)
* US East (N. Virginia) (us-east-1)
* US West (Oregon) Region (us-west-1)

All other widgets are supported in all AWS Regions where CloudTrail Lake is
 supported.


For information about CloudTrail Lake supported Regions, see [CloudTrail Lake supported Regions](cloudtrail-lake-supported-regions.md "cloudtrail-lake-supported-regions.md").


## Required permissions


This section describes the required permissions for CloudTrail Lake dashboards and discusses
 two types of IAM policies:



* Identity-based policies which allow you to perform actions to create, manage,
 and delete dashboards.
* Resource-based policies that allow CloudTrail to run queries on your event data
 store when the dashboard is refreshed and perform scheduled refreshes of custom
 dashboards and the Highlights dashboard on your behalf. When you create
 dashboards using the CloudTrail console, you are given the option to attach
 resource-based policies. You can also run the AWS CLI [put-resource-policy](lake-dashboard-cli-manage.md#lake-dashboard-cli-add-rbp "lake-dashboard-cli-manage.md#lake-dashboard-cli-add-rbp")
 command to add a resource-based policy to your event data stores or dashboards.

### Identity-based policy
 requirements


Identity-based policies are JSON permissions policy documents that you can attach
 to an identity, such as an IAM user, group of users, or role. These policies
 control what actions users and roles can perform, on which resources, and under what
 conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html") in the
 *IAM User Guide*.


To view and manage CloudTrail Lake dashboards, you need one of the following
 policies:



* The [`CloudTrailFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html") managed policy.
* The [`AdministratorAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html") managed policy.
* A custom policy that includes one or more of the specific permissions
 described in the sections which follow.

###### Topics

* [Required
 permissions for creating dashboards](#lake-dashboard-permissions-identity-create "#lake-dashboard-permissions-identity-create")
* [Required
 permissions for updating dashboards](#lake-dashboard-permissions-identity-update "#lake-dashboard-permissions-identity-update")
* [Required
 permissions for refreshing dashboards](#lake-dashboard-permissions-identity-create "#lake-dashboard-permissions-identity-create")

#### Required
 permissions for creating dashboards


The following sample policy provides the required minimum permissions for
 creating dashboards. Replace `partition`,
 `region`, `account-id`,
 and `eds-id` with the values for your
 configuration.



* `StartQuery` permission is required only if the request
 contains widgets. Provide `StartQuery` permissions for all
 event data stores included in a widget query.
* `StartDashboardRefresh` permission is required only if the
 dashboard has a refresh schedule.
* For the Highlights dashboard, the caller must have
 `StartQuery` permission on all the event data stores in
 the account.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:CreateDashboard",
 "cloudtrail:StartDashboardRefresh",
 "cloudtrail:StartQuery"
 ],
 "Resource": [
 "arn:aws:cloudtrail:`us-east-1`:`111111111111`:dashboard/*",
 "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/`eds-id`"
 ]
 }
 ]
}`

```





#### Required
 permissions for updating dashboards


The following sample policy provides the required minimum permissions for
 updating dashboards. Replace `partition`,
 `region`, `account-id`,
 and `eds-id` with the values for your
 configuration.



* `StartQuery` permission is required only if the request
 contains widgets. Provide `StartQuery` permissions for all
 event data stores included in a widget query.
* `StartDashboardRefresh` permission is required only if the
 dashboard has a refresh schedule.
* For the Highlights dashboard, the caller must have
 `StartQuery` permission on all the event data stores in
 the account.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:UpdateDashboard",
 "cloudtrail:StartDashboardRefresh",
 "cloudtrail:StartQuery"
 ],
 "Resource": [
 "arn:aws:cloudtrail:`us-east-1`:`111111111111`:dashboard/*",
 "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/`eds-id`"
 ]
 }
 ]
}`

```





#### Required
 permissions for refreshing dashboards


The following sample policy provides the required minimum permissions for
 refreshing dashboards. Replace `partition`,
 `region`, `account-id`,
 `dashboard-name`, and
 `eds-id` with the values for your
 configuration.



* For custom dashboards and the Highlights dashboards, the caller must
 have `cloudtrail:StartDashboardRefresh permissions`.
* For managed dashboards, the caller must have
 `cloudtrail:StartDashboardRefresh` permission and
 `cloudtrail:StartQuery` permissions for the event data
 store involved in the refresh.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:StartDashboardRefresh",
 "cloudtrail:StartQuery"
 ],
 "Resource": [
 "arn:aws:cloudtrail:`us-east-1`:`111111111111`:dashboard/`dashboard-name`",
 "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/`eds-id`"
 ]
 }
 ]
}`

```





### Resource-based policies for
 dashboards and event data stores


Resource-based policies are JSON policy documents that you attach to a resource.
 Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket
 policies. For the resource where the policy is attached, the policy defines what
 actions a specified principal can perform on that resource and under what
 conditions. You must specify a principal in a resource-based policy. 


To run queries on a dashboard during a manual or scheduled refresh, you must
 attach a resource-based policy to every event data store that is associated with a
 widget on the dashboard. This allows CloudTrail Lake to run the queries on your behalf.
 When you create a custom dashboard, or enable the **Highlights**
 dashboard using the CloudTrail console, CloudTrail gives you the option to choose which event
 data stores you want to apply permissions to. For more information about the
 resource-based policy, see [Example:
 Allow CloudTrail to run queries to refresh a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard").


To set a refresh schedule for a dashboard, you must attach a resource-based policy
 to the dashboard to allow CloudTrail Lake to refresh the dashboard on your behalf. When
 you set a refresh schedule for a custom dashboard, or enable the
 **Highlights** dashboard using the CloudTrail console, CloudTrail gives you
 the option to attach a resource-based policy to your dashboard. For an example
 policy, see [Resource-based policy example for a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards").


You can attach a resource-based policy using the CloudTrail console, the [AWS CLI](lake-dashboard-cli-manage.md#lake-dashboard-cli-add-rbp "lake-dashboard-cli-manage.md#lake-dashboard-cli-add-rbp"), or the
 [PutResourcePolicy](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md") API operation.


### KMS key permissions to decrypt
 data in an event data store


If an event data store being queried is encrypted with a KMS key, ensure the
 KMS key policy allows CloudTrail to decrypt the data in the event data store. The
 following example policy statement allows the CloudTrail service principal to decrypt the
 event data store.



```
{
      "Sid": "AllowCloudTrailDecryptAccess",
      "Effect": "Allow",
      "Principal": {
          "Service": "cloudtrail.amazonaws.com"
        },
      "Action": "kms:Decrypt",
      "Resource": "*"
}
```
