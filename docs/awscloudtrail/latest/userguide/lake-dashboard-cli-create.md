# Create a dashboard with the AWS CLI

This section describes how to use the `create-dashboard` command to create 
 a create a custom dashboard or the Highlights dashboard.

When using the AWS CLI,
 remember that your commands run in the AWS Region configured for your profile. If
 you want to run the commands in a different Region, either change the default Region for
 your profile, or use the `--region` parameter with the command.


 CloudTrail runs queries to populate the dashboard's widgets during a manual or
 scheduled refresh. CloudTrail must be granted permissions to run the `StartQuery`
 operation on each event data store associated with a dashboard widget. To provide permissions, run the
 `put-resource-policy` command to attach a resource-based policy to each
 event data store, or edit the event data store's policy on the CloudTrail console. For an example policy, see [Example:
 Allow CloudTrail to run queries to refresh a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard"). 


 To set a refresh schedule, CloudTrail must be granted permissions to run the `StartDashboardRefresh` operation to refresh the dashboard on your behalf. 
 To provide permissions, run the `put-resource-policy` operation to attach a resource-based policy to the dashboard, or edit the dashboard's policy on the CloudTrail console. 
 For an example policy, see [Resource-based policy example for a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards").
 

###### Examples:

* [Create a custom dashboard with the AWS CLI](#lake-dashboard-cli-create-custom "#lake-dashboard-cli-create-custom")
* [Enable the Highlights dashboard with the AWS CLI](#lake-dashboard-cli-create-highlights "#lake-dashboard-cli-create-highlights")
* [View properties for widgets](lake-widget-properties.md "lake-widget-properties.md")

## Create a custom dashboard with the AWS CLI


The following procedure shows how to create a custom dashboard, attach the required resource-based policies to event data stores and the dashboard, 
 and update the dashboard to set and enable a refresh schedule.


1. Run the `create-dashboard` to create a dashboard.


When you create a custom dashboard, you can pass in an array with up to 10
 widgets. A widget provides a graphical representation of the results for a
 query. Each widget consists of `ViewProperties`,
 `QueryStatement`, and `QueryParameters`.




	* `ViewProperties` – Specifies the properties for the view type. For more information, 
	 see [View properties for widgets](lake-widget-properties.md "lake-widget-properties.md").
	* `QueryStatement` – The query CloudTrail runs when the dashboard is refreshed. You can query across multiple event data stores as 
	 long as the event data stores exist in your account.
	* `QueryParameters` – The following `QueryParameters` values are supported for 
	 custom dashboards: `$Period$`, `$StartTime$`, and `$EndTime$`. To use `QueryParameters` place a `?` in the `QueryStatement` where you want to substitute the parameter. CloudTrail will fill 
	 in the parameters when the query is run.
The following
 example creates a dashboard with four widgets, one of each view
 type.


###### Note

In the this example, `?` is surrounded with
 single quotes because it is used with `eventTime`.
 Depending on the operating system you are running on, you may
 need to surround single quotes with escape quotes. For more
 information, see [Using quotation marks and literals with strings in the
 AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-usage-parameters-quoting-strings.html "https://docs.aws.amazon.com/cli/v1/userguide/cli-usage-parameters-quoting-strings.html").



```
aws cloudtrail create-dashboard --name AccountActivityDashboard \
--widgets '[
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "TopErrors",
        "View": "Table"
      },
      "QueryStatement": "SELECT errorCode, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' AND (errorCode is not null) GROUP BY errorCode ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "MostActiveRegions",
        "View": "PieChart",
        "LabelColumn": "awsRegion",
        "ValueColumn": "eventCount",
        "FilterColumn": "awsRegion"
      },
      "QueryStatement": "SELECT awsRegion, COUNT(*) AS eventCount FROM eds where eventTime > '?' and eventTime < '?' GROUP BY awsRegion ORDER BY eventCount LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "AccountActivity",
        "View": "LineChart",
        "YAxisColumn": "eventCount",
        "XAxisColumn": "eventDate",
        "FilterColumn": "readOnly"
      },
      "QueryStatement": "SELECT DATE_TRUNC('?', eventTime) AS eventDate, IF(readOnly, 'read', 'write') AS readOnly, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY DATE_TRUNC('?', eventTime), readOnly ORDER BY DATE_TRUNC('?', eventTime), readOnly",
      "QueryParameters": ["$Period$", "$StartTime$", "$EndTime$", "$Period$", "$Period$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "TopServices",
        "View": "BarChart",
        "LabelColumn": "service",
        "ValueColumn": "eventCount",
        "FilterColumn": "service",
        "Orientation": "Horizontal"
      },
      "QueryStatement": "SELECT REPLACE(eventSource, '.amazonaws.com') AS service, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    }
  ]'
```
2. Create a separate file with the resource policy needed
 for each event data store that is included in a
 widget's `QueryStatement`. Name the file `policy.json`, with
 the following example policy statement:


 Replace `123456789012` with your account ID,
 `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDashboard`
 with the ARN of the dashboard.


For more information about resource-based policies for dashboards,
 see [Example:
 Allow CloudTrail to run queries to refresh a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard").
3. Run the `put-resource-policy` command to attach the policy. You can also update an event data
 store's resource-based policy on the CloudTrail console. 


The following example attaches a resource-based policy to an event data store.
 



```
aws cloudtrail put-resource-policy \
--resource-arn `eds-arn` \
--resource-policy file://`policy.json`
```
4. Run the `put-resource-policy` command to attach a resource-based policy to the dashboard. For an example policy, see [Resource-based policy example for a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards").


The following example attaches a resource-based policy to a dashboard.
 Replace `account-id` with your account ID and `dashboard-arn` with the ARN of the dashboard.



```
aws cloudtrail put-resource-policy \
--resource-arn `dashboard-arn` \
--resource-policy '{"Version": "2012-10-17",		 	 	  "Statement": [{"Sid": "DashboardPolicy", "Effect": "Allow", "Principal": { "Service": "cloudtrail.amazonaws.com" }, "Action": "cloudtrail:StartDashboardRefresh", "Condition": { "StringEquals": { "AWS:SourceArn": "`dashboard-arn`", "AWS:SourceAccount": "`account-id`"}}}]}'
```
5. Run the `update-dashboard` command to set and enable a refresh schedule by configuring the `--refresh-schedule` parameter.


The `--refresh-schedule` consists of the following optional parameters:




	* `Frequency` – The `Unit` and `Value` for the schedule.
	
	
	For custom dashboards, the unit can be `HOURS` or `DAYS`.
	
	
	
	 For custom dashboards, the following values are valid when the unit is `HOURS`: `1`, `6`, `12`, `24`
	
	
	
	For custom dashboards, the only valid value when the unit is `DAYS` is `1`.
	* `Status` – Specifies whether the refresh schedule is enabled. Set the value to `ENABLED` to enable the refresh schedule, or to `DISABLED` to turn off the refresh schedule.
	* `TimeOfDay`  – The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00.
The following example sets a refresh schedule for every six hours and enables the schedule.



```
aws cloudtrail update-dashboard --dashboard-id AccountActivityDashboard \
--refresh-schedule '{"Frequency": {"Unit": "HOURS", "Value": 6}, "Status": "ENABLED"}'
```

## Enable the Highlights dashboard with the AWS CLI


The following procedure shows how to create the Highlights dashboard, attach the required resource-based policies to your event data stores and the dashboard, 
 and update the dashboard to set and enable the refresh schedule.


1. Run the `create-dashboard` command to create the Highlights dashboard. To create this dashboard, the `--name` must be 
 `AWSCloudTrail-Highlights`.



```
aws cloudtrail create-dashboard --name AWSCloudTrail-Highlights
```
2. For each event data store in your account, run the
 `put-resource-policy` command to attach a resource-based
 policy to the event data store. You can also update an event data store's
 resource-based policy on the CloudTrail console. For an example policy, see [Example:
 Allow CloudTrail to run queries to refresh a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard").


The following example attaches a resource-based policy to an event data store.
 Replace `account-id` with your account ID, `eds-arn` with the ARN of the event data store, and
 `dashboard-arn` with the ARN of the
 dashboard.



```
aws cloudtrail put-resource-policy \
--resource-arn `eds-arn` \
--resource-policy '{"Version": "2012-10-17",		 	 	  "Statement": [{"Sid": "EDSPolicy", "Effect": "Allow", "Principal": { "Service": "cloudtrail.amazonaws.com" }, "Action": "cloudtrail:StartQuery", "Condition": { "StringEquals": { "AWS:SourceArn": "`dashboard-arn`", "AWS:SourceAccount": "`account-id`"}}} ]}'
```
3. Run the `put-resource-policy` command to attach a resource-based policy to the dashboard. For an example policy, see [Resource-based policy example for a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards").


The following example attaches a resource-based policy to a dashboard.
 Replace `account-id` with your account ID and `dashboard-arn` with the ARN of the dashboard.



```
aws cloudtrail put-resource-policy \
--resource-arn `dashboard-arn` \
--resource-policy '{"Version": "2012-10-17",		 	 	  "Statement": [{"Sid": "DashboardPolicy", "Effect": "Allow", "Principal": { "Service": "cloudtrail.amazonaws.com" }, "Action": "cloudtrail:StartDashboardRefresh", "Condition": { "StringEquals": { "AWS:SourceArn": "`dashboard-arn`", "AWS:SourceAccount": "`account-id`"}}}]}'
```
4. Run the `update-dashboard` command to set and enable a refresh schedule by configuring the `--refresh-schedule` parameter. For the Highlights dashboard, 
 the only valid `UNIT` is `HOURS` and the only valid `Value` is `6`.



```
aws cloudtrail update-dashboard --dashboard-id AWSCloudTrail-Highlights \
--refresh-schedule '{"Frequency": {"Unit": "HOURS", "Value": 6}, "Status": "ENABLED"}'
```
