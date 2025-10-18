# Manage dashboards with the AWS CLI

This section describes several other commands that you can run to manage your dashboards, including 
 getting a dashboard, listing your dashboards, refreshing a dashboard, and updating a dashboard.

When using the AWS CLI,
 remember that your commands run in the AWS Region configured for your profile. If
 you want to run the commands in a different Region, either change the default Region for
 your profile, or use the `--region` parameter with the command.

###### Examples:

* [Get a dashboard with the AWS CLI](#lake-dashboard-cli-get "#lake-dashboard-cli-get")
* [List dashboards with the AWS CLI](#lake-dashboard-cli-list "#lake-dashboard-cli-list")
* [Attach a resource-based policy to an event data store or dashboard with the AWS CLI](#lake-dashboard-cli-add-rbp "#lake-dashboard-cli-add-rbp")
* [Manually refresh a dashboard with the AWS CLI](#lake-dashboard-cli-refresh "#lake-dashboard-cli-refresh")
* [Update a dashboard with the AWS CLI](#lake-dashboard-cli-update "#lake-dashboard-cli-update")

## Get a dashboard with the AWS CLI


Run the `get-dashboard` command to return a dashboard. Specify the `--dashboard-id` by providing the dashboard ARN, or the dashboard name.



```
aws cloudtrail get-dashboard --dashboard-id arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash
```

## List dashboards with the AWS CLI


Run the `list-dashboards` command to list the dashboards for your account.



* Include the `--type` parameter, to view only the `CUSTOM` 
 or `MANAGED` dashboards.
* Include the `--max-results` parameter to limit the number of results. Valid values are 1-100.
* Include the `--name-prefix` to return dashboards matching the specified prefix.

The following example lists all dashboards.



```
aws cloudtrail list-dashboards
```

This example lists only the `CUSTOM` dashboards.



```
aws cloudtrail list-dashboards --type CUSTOM
```

The next example lists only the `MANAGED` dashboards.



```
aws cloudtrail list-dashboards --type MANAGED
```

The final example lists the dashboards matching the specified prefix.



```
aws cloudtrail list-dashboards --name-prefix `ExamplePrefix`
```

## Attach a resource-based policy to an event data store or dashboard with the AWS CLI


Run the `put-resource-policy` command to apply a resource-based policy to an event data store or dashboard.


### Attach a resource-based policy to an event data store


To run queries on a dashboard during a manual or scheduled refresh, you need to attach a resource-based policy to 
 every event data store that is associated with a widget on the dashboard. 
 This allows CloudTrail Lake to run the queries on your behalf. For more information about the resource-based policy, see 
 [Example:
 Allow CloudTrail to run queries to refresh a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard").


The following example attaches a resource-based policy to an event data store.
 Replace `account-id` with your account ID, `eds-arn` with the ARN of the event data store for which CloudTrail will run queries, and
 `dashboard-arn` with the ARN of the
 dashboard.



```
aws cloudtrail put-resource-policy \
--resource-arn `eds-arn` \
--resource-policy '{"Version": "2012-10-17",		 	 	  "Statement": [{"Sid": "EDSPolicy", "Effect": "Allow", "Principal": { "Service": "cloudtrail.amazonaws.com" }, "Action": "cloudtrail:StartQuery", "Condition": { "StringEquals": { "AWS:SourceArn": "`dashboard-arn`", "AWS:SourceAccount": "`account-id`"}}} ]}'
```

### Attach a resource-based policy to a dashboard


To set a refresh schedule for a dashboard, you need to attach a resource-based policy to the dashboard to allow CloudTrail Lake to refresh the dashboard on your behalf. For more information about the resource-based policy, see 
 [Resource-based policy example for a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-dashboards").


The following example attaches a resource-based policy to a dashboard.
 Replace `account-id` with your account ID and `dashboard-arn` with the ARN of the dashboard.



```
aws cloudtrail put-resource-policy \
--resource-arn `dashboard-arn` \
--resource-policy '{"Version": "2012-10-17",		 	 	  "Statement": [{"Sid": "DashboardPolicy", "Effect": "Allow", "Principal": { "Service": "cloudtrail.amazonaws.com" }, "Action": "cloudtrail:StartDashboardRefresh", "Condition": { "StringEquals": { "AWS:SourceArn": "`dashboard-arn`", "AWS:SourceAccount": "`account-id`"}}}]}'
```

## Manually refresh a dashboard with the AWS CLI


Run the `start-dashboard-refresh` command to manually refresh the dashboard. Before you can run this command, 
 you must [attach a resource-based policy](#lake-dashboard-cli-add-rbp-eds "#lake-dashboard-cli-add-rbp-eds") to every event data store associated with a dashboard widget.


The following example shows how to manually refresh a custom dashboard.



```
aws cloudtrail start-dashboard-refresh \ 
--dashboard-id  `dashboard-id` \ 
--query-parameter-values '{"$StartTime$": "2024-11-05T10:45:24.00Z"}'
```

The next example shows how to manually refresh a managed dashboard. Because managed dashboards are configured by CloudTrail, 
 the refresh request needs to include the ID of the event data store that the queries will run on.



```
aws cloudtrail start-dashboard-refresh \
--dashboard-id `dashboard-id`  \
--query-parameter-values '{"$StartTime$": "2024-11-05T10:45:24.00Z", "$EventDataStoreId$": "`eds-id`"}'
```

## Update a dashboard with the AWS CLI


Run the `update-dashboard` command to update 
 a dashboard. You can update the dashboard to set a refresh schedule, enable or disable a refresh schedule, modify the widgets, and enable or disable termination protection.


### Update the refresh schedule with the AWS CLI


The following example updates the refresh schedule for a custom dashboard named `AccountActivityDashboard`.



```
aws cloudtrail update-dashboard --dashboard-id AccountActivityDashboard \
--refresh-schedule '{"Frequency": {"Unit": "HOURS", "Value": 6}, "Status": "ENABLED"}'
```

### Disable termination protection and the refresh schedule on a custom dashboard with the AWS CLI


The following example disables termination protection for a custom dashboard named `AccountActivityDashboard` to allow the dashboard to be deleted. 
 It also turns off the refresh schedule.



```
aws cloudtrail update-dashboard --dashboard-id AccountActivityDashboard \
--refresh-schedule '{ "Status": "DISABLED"}' \
--no-termination-protection-enabled
```

### Add a widget to a custom dashboard


The following example adds a new widget named `TopServices` to the 
 custom dashboard named `AccountActivityDashboard`. The widgets array includes the 
 two widgets that were already created for the dashboard and the new widget.


###### Note

In the this example, `?` is surrounded with
 single quotes because it is used with `eventTime`.
 Depending on the operating system you are running on, you may
 need to surround single quotes with escape quotes. For more
 information, see [Using quotation marks and literals with strings in the
 AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-usage-parameters-quoting-strings.html "https://docs.aws.amazon.com/cli/v1/userguide/cli-usage-parameters-quoting-strings.html").



```
aws cloudtrail update-dashboard --dashboard-id AccountActivityDashboard \
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
        "Title": "TopServices",
        "View": "BarChart",
        "LabelColumn": "service",
        "ValueColumn": "eventCount",
        "FilterColumn": "service",
        "Orientation": "Vertical"
      },
      "QueryStatement": "SELECT replace(eventSource, '.amazonaws.com') AS service, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    }
  ]'
```
