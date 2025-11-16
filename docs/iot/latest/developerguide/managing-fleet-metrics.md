# Managing fleet metrics

This topic shows how to use the AWS IoT console and AWS CLI to manage your fleet
metrics.

###### Topics

- [Managing fleet metrics (Console)](#managing-fleet-metrics-console "#managing-fleet-metrics-console")
- [Managing fleet metrics (CLI)](#managing-fleet-metrics-cli "#managing-fleet-metrics-cli")
- [Authorize tagging of IoT resources](#managing-fleet-metrics-policy "#managing-fleet-metrics-policy")

## Managing fleet metrics (Console)

The following sections show how to use the AWS IoT console to manage your fleet metrics.
Make sure you've enabled fleet indexing with associated data sources and configurations
before creating fleet metrics.

### Enable fleet indexing

If you've already enabled fleet indexing, skip this section.

If you haven't enabled fleet indexing, follow these instructions.

1. Open your AWS IoT console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. On the AWS IoT menu, choose **Settings**.
3. To view the detailed settings, on the **Settings** page, scroll
   down to the **Fleet indexing** section.
4. To update your fleet indexing settings, to the right of the **Fleet
   indexing** section, select **Manage indexing**.
5. On the **Manage fleet indexing** page, update your fleet indexing
   settings based on your needs.
   - **Configuration**

   To turn on thing indexing, toggle **Thing indexing** on, and
   then select the data sources you want to index from.

   To turn on thing group indexing, toggle **Thing group
   indexing** on.
   - **Custom fields for aggregation - _optional_**

   Custom fields are a list of field name and field type pairs.

   To add a custom field pair, choose **Add new field**. Enter a
   custom field name such as `attributes.temperature`, then select a field
   type from the **Field type** menu. Note that a custom field name
   begins with `attributes.` and will be saved as an attribute to run
   [thing aggregations queries](index-aggregate.md "index-aggregate.md").

   To update and save the setting, choose **Update**.

### Create a fleet metric

1. Open your AWS IoT console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. On the AWS IoT menu, choose **Manage**, and then choose
   **Fleet metrics**.
3. On the **Fleet metrics** page, choose **Create fleet
   metric** and complete the creation steps.
4. In step 1 **Configure fleet metrics**
   - In **Query** section, enter a query string to specify the
     things or thing groups you want to perform the aggregate search. The query string
     consists of an attribute and a value. For **Properties**, choose
     the attribute you want, or, if it doesn't appear in the list, enter the attribute
     in the field. Enter the value after `:`. An example query string can be
     `thingName:TempSensor*`. For each query string you enter, press
     **enter** in your keyboard. If you enter multiple query
     strings, specify their relationship by selecting **and**,
     **or**, **and not**, or **or
     not** between them.
   - In **Report properties**, choose **Index
     name**, **Aggregation type**, and
     **Aggregation field** from their respective lists. Next, select
     the data you want to aggregate in **Select data**, where you can
     select multiple data values.
   - Choose **Next**.

5. In step 2 **Specify fleet metric properties**
   - In **Fleet metric name** field, enter a name for the fleet
     metric you're creating.
   - In **Description - _optional_** field, enter a description for the fleet metric
     you're creating. This field is optional.
   - In **Hours** and **Minutes** fields, enter
     the time (how often) you want the fleet metric to emit data to CloudWatch.
   - Choose **Next**.

6. In step 3 **Review and create**
   - Review the settings of step 1 and step 2. To edit the settings, choose
     **Edit**.
   - Choose **Create fleet metric**.

After successful creation, the fleet metric is listed on the **Fleet
metric** page.

### Update a fleet metric

1. On the **Fleet metric** page, choose the fleet metric that you
   want to update.
2. On the fleet metric **Details** page, choose
   **Edit**. This opens the creation steps where you can update your
   fleet metric in any of the three steps.
3. After you finish updating the fleet metric, choose **Update fleet
   metric**.

### Delete a fleet metric

1. On the **Fleet metric** page, choose the fleet metric that you
   want to delete.
2. On the next page that shows details of your fleet metric, choose
   **Delete**.
3. In the dialog box, enter the name of your fleet metric to confirm deletion.
4. Choose **Delete**. This step deletes your fleet metric
   permanently.

## Managing fleet metrics (CLI)

The following sections show how to use the AWS CLI to manage your fleet metrics. Make sure
you've enabled fleet indexing with associated data sources and configurations before
creating fleet metrics. To enable fleet indexing for your things or thing groups, follow the
instructions in [Managing thing indexing](managing-index.md#enable-index "managing-index.md#enable-index") or [Managing thing group indexing](thinggroup-index.md#enable-group-index "thinggroup-index.md#enable-group-index").

### Create a fleet metric

You can use the create-fleet-metric CLI command to create a fleet metric.

```
`aws iot create-fleet-metric --metric-name "YourFleetMetricName" --query-string "*" --period 60 --aggregation-field "registry.version" --aggregation-type name=Statistics,values=sum`
```

The output of this command contains the name and Amazon Resource Name (ARN) of your
fleet metric. The output looks like the following:

```
{
    "metricArn": "arn:aws:iot:us-east-1:`111122223333:fleetmetric/YourFleetMetricName`",
    "metricName": "YourFleetMetricName"
}
```

### List fleet metrics

You can use the list-fleet-metric CLI command to list all the fleet metrics in your
account.

```
`aws iot list-fleet-metrics`
```

The output of this command contains all your fleet metrics. The output looks like the
following:

```
{
    "fleetMetrics": [
        {
            "metricArn": "arn:aws:iot:us-east-1:`111122223333:fleetmetric/YourFleetMetric1`",
            "metricName": "YourFleetMetric1"
        },
        {
            "metricArn": "arn:aws:iot:us-east-1:`111122223333:fleetmetric/YourFleetMetric2`",
            "metricName": "YourFleetMetric2"
        }
    ]
}
```

### Describe a fleet metric

You can use the describe-fleet-metric CLI command to display more detailed information
about a fleet metric.

```
`aws iot describe-fleet-metric --metric-name "YourFleetMetricName"`
```

The output of command contains the detailed information about the specified fleet
metric. The output looks like the following:

```
{
    "queryVersion": "2017-09-30",
    "lastModifiedDate": 1625790642.355,
    "queryString": "*",
    "period": 60,
    "metricArn": "arn:aws:iot:us-east-1:`111122223333:fleetmetric/YourFleetMetricName`",
    "aggregationField": "registry.version",
    "version": 1,
    "aggregationType": {
        "values": [
            "sum"
        ],
        "name": "Statistics"
    },
    "indexName": "AWS_Things",
    "creationDate": 1625790642.355,
    "metricName": "YourFleetMetricName"
}
```

### Update a fleet metric

You can use the update-fleet-metric CLI command to update a fleet metric.

```
`aws iot update-fleet-metric --metric-name "YourFleetMetricName" --query-string "*" --period 120 --aggregation-field "registry.version" --aggregation-type name=Statistics,values=sum,count --index-name AWS_Things`
```

The update-fleet-metric command doesn't produce any output. You can use the
describe-fleet-metric CLI command to see the result.

```
{
    "queryVersion": "2017-09-30",
    "lastModifiedDate": 1625792300.881,
    "queryString": "*",
    "period": 120,
    "metricArn": "arn:aws:iot:us-east-1:`111122223333:fleetmetric/YourFleetMetricName`",
    "aggregationField": "registry.version",
    "version": 2,
    "aggregationType": {
        "values": [
            "sum",
            "count"
        ],
        "name": "Statistics"
    },
    "indexName": "AWS_Things",
    "creationDate": 1625792300.881,
    "metricName": "YourFleetMetricName"
}
```

### Delete a fleet metric

Use the delete-fleet-metric CLI command to delete a fleet metric.

```
`aws iot delete-fleet-metric --metric-name "YourFleetMetricName"`
```

This command doesn't produce any output if the deletion is successful or if you specify
a fleet metric that doesn't exist.

For more information, see [Troubleshooting fleet metrics](fleet-indexing-troubleshooting.md#fleet-metrics-troubleshooting "fleet-indexing-troubleshooting.md#fleet-metrics-troubleshooting").

## Authorize tagging of IoT resources

For better control over fleet metrics that you can create, modify, or use, you can
attach tags to the fleet metrics.

To tag fleet metrics that you create by using AWS Management Console or AWS CLI, you must include the
`iot:TagResource` action in your IAM policy to grant the user permissions. If
your IAM policy doesn't include `iot:TagResource`, any actions to create a
fleet metric with a tag will return an `AccessDeniedException` error.

For general information about tagging your resources, see [Tagging your AWS IoT
resources](tagging-iot.md "tagging-iot.md").

### IAM policy example

Refer to the following IAM policy example granting tagging permissions when you create
a fleet metric:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iot:TagResource"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:*:*:fleetmetric/*"
 ]
 },
 {
 "Action": [
 "iot:CreateFleetMetric"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:*:*:index/*",
 "arn:aws:iot:*:*:fleetmetric/*"
 ]
 }
 ]
}`

```

For more information, see [Actions, resources, and
condition keys for AWS IoT](../../../service-authorization/latest/reference/list_awsiot.md "../../../service-authorization/latest/reference/list_awsiot.md").
