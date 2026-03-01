# Examples of using the CLI with Network Flow Monitor

This section includes examples for using the AWS Command Line Interface with Network Flow Monitor operations.

Before you begin, make sure that you log in to use the AWS CLI with the AWS account that provides
the scope that you want to use to monitor network flows. For more information about using API actions with
Network Flow Monitor, see the [Network Flow Monitor API Reference Guide](../../../networkflowmonitor/2.0/APIReference/Welcome.md "../../../networkflowmonitor/2.0/APIReference/Welcome.md").

###### Topics

- [Create a monitor](#CloudWatch-NFM-get-started-CLI-create-monitor "#CloudWatch-NFM-get-started-CLI-create-monitor")
- [View monitor details](#CloudWatch-NFM-get-started-CLI-mon-details "#CloudWatch-NFM-get-started-CLI-mon-details")
- [Create a scope](#CloudWatch-NFM-get-started-CLI-create-scope "#CloudWatch-NFM-get-started-CLI-create-scope")
- [Delete a monitor](#CloudWatch-NFM-get-started-CLI-delete-monitor "#CloudWatch-NFM-get-started-CLI-delete-monitor")
- [Delete a scope](#CloudWatch-NFM-get-started-CLI-delete-scope "#CloudWatch-NFM-get-started-CLI-delete-scope")
- [Get information about a monitor](#CloudWatch-NFM-get-started-CLI-get-monitor "#CloudWatch-NFM-get-started-CLI-get-monitor")
- [Retrieve data on a specific queries](#CloudWatch-NFM-get-started-CLI-get-query-results "#CloudWatch-NFM-get-started-CLI-get-query-results")
- [See scope information](#CloudWatch-NFM-get-scope "#CloudWatch-NFM-get-scope")
- [See a list of monitors for an account](#CloudWatch-NFM-list-monitors "#CloudWatch-NFM-list-monitors")
- [See a list of scopes for an account](#CloudWatch-NFM-list-scopes "#CloudWatch-NFM-list-scopes")
- [See the list of tags for a monitor](#CloudWatch-NFM-list-tags-for-resource "#CloudWatch-NFM-list-tags-for-resource")
- [Starting and stopping queries](#CloudWatch-NFM-query-monitors "#CloudWatch-NFM-query-monitors")
- [Tag a monitor](#CloudWatch-NFM-tag-resource "#CloudWatch-NFM-tag-resource")
- [Remove a tag from a monitor](#CloudWatch-NFM-untag-resource "#CloudWatch-NFM-untag-resource")
- [Update an existing monitor](#CloudWatch-NFM-update-monitor "#CloudWatch-NFM-update-monitor")

## Create a monitor

To create a monitor with the AWS CLI, use the `create-monitor` command. The following example creates a
monitor named `demo` in the specified account.

```
aws networkflowmonitor create-monitor \
        --monitor-name demo \
        --local-resources type="AWS::EC2::VPC",identifier="arn:aws:ec2:us-east-1:111122223333:vpc/vpc-11223344556677889"  \
        --scope-arn arn:aws:networkflowmonitor:us-east-1:111122223333:scope/sample-aaaa-bbbb-cccc-44556677889

```

Output:

```
{
        "monitorArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/demo",
        "monitorName": "demo",
        "monitorStatus": "ACTIVE",
        "tags": {}
    }
```

For more information, see [Create a monitor in Network Flow Monitor](CloudWatch-NetworkFlowMonitor-configure-monitors-create.md "CloudWatch-NetworkFlowMonitor-configure-monitors-create.md").

## View monitor details

To view information about a monitor with the AWS CLI, use the `get-monitor` command.

```
aws networkflowmonitor get-monitor --monitor-name "TestMonitor"
```

Output:

```
{
    "ClientLocationType": "city",
    "CreatedAt": "2022-09-22T19:27:47Z",
    "ModifiedAt": "2022-09-22T19:28:30Z",
    "MonitorArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/TestMonitor",
    "MonitorName": "TestMonitor",
    "ProcessingStatus": "OK",
    "ProcessingStatusInfo": "The monitor is actively processing data",
    "Resources": [
        "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-11223344556677889"
    ],
    "MaxCityNetworksToMonitor": 10000,
    "Status": "ACTIVE"
}
```

## Create a scope

The following `create-scope` example creates a scope that is the set of resources
for which Network Flow Monitor will generate network traffic metrics.

```
aws networkflowmonitor create-scope \
        --targets '[{"targetIdentifier":{"targetId":{"accountId":"111122223333"},"targetType":"ACCOUNT"},"region":"us-east-1"}]'
```

Output:

```

    {
        "scopeId": "sample-aaaa-bbbb-cccc-11112222333",
        "status": "IN_PROGRESS",
        "tags": {}
    }

```

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").

## Delete a monitor

The following `delete-monitor` example deletes a monitor named `Demo` in your account.

```
aws networkflowmonitor delete-monitor \
        --monitor-name Demo
```

This command produces no output.

For more information, see [Delete a monitor in Network Flow Monitor](CloudWatch-NetworkFlowMonitor-configure-monitors-delete.md "CloudWatch-NetworkFlowMonitor-configure-monitors-delete.md").

## Delete a scope

The following `delete-scope` example deletes the specified scope.

```
aws networkflowmonitor delete-scope \
        --scope-id sample-aaaa-bbbb-cccc-44556677889
```

This command produces no output.

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").

## Get information about a monitor

The following `get-monitor` example displays information about the monitor named `demo` in the specified account.

```
aws networkflowmonitor get-monitor \
        --monitor-name Demo
```

Output:

```
{
        "monitorArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/Demo",
        "monitorName": "Demo",
        "monitorStatus": "ACTIVE",
        "localResources": [
            {
                "type": "AWS::EC2::VPC",
                "identifier": "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-11223344556677889"
            }
        ],
        "remoteResources": [],
        "createdAt": "2024-12-09T12:21:51.616000-06:00",
        "modifiedAt": "2024-12-09T12:21:55.412000-06:00",
        "tags": {}
    }
```

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").

## Retrieve data on a specific queries

The following sections provide example CLI commands to retrieve query statuses.

### get-query-results-workload-insights-top-contributors-data

The `get-query-results-workload-insights-top-contributors-data` example returns the data for the specified query.

```
aws networkflowmonitor get-query-results-workload-insights-top-contributors-data \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --query-id sample-dddd-eeee-ffff-44556677889
```

Output:

```
{
        "datapoints": [
            {
                "timestamps": [
                    "2024-12-09T19:00:00+00:00",
                    "2024-12-09T19:05:00+00:00",
                    "2024-12-09T19:10:00+00:00"
                ],
                "values": [
                    259943.0,
                    194856.0,
                    216432.0
                ],
                "label": "use1-az6"
            }
        ],
        "unit": "Bytes"
    }

```

### get-query-results-workload-insights-top-contributors

The following `get-query-results-workload-insights-top-contributors` example returns the data for the specified query.

```
aws networkflowmonitor get-query-results-workload-insights-top-contributors \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --query-id sample-dddd-eeee-ffff-44556677889
```

Output:

```
{
        "topContributors": [
            {
                "accountId": "111122223333",
                "localSubnetId": "subnet-SAMPLE1111",
                "localAz": "use1-az6",
                "localVpcId": "vpc-SAMPLE2222",
                "localRegion": "us-east-1",
                "remoteIdentifier": "",
                "value": 333333,
                "localSubnetArn": "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-2222444455556666",
                "localVpcArn": "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-11223344556677889"
            }
        ]
    }

```

### get-query-status-monitor-top-contributors

The following `get-query-status-monitor-top-contributors` example displays the current status of the query in the specified account.

```
aws networkflowmonitor get-query-status-monitor-top-contributors \
        --monitor-name Demo \
        --query-id sample-dddd-eeee-ffff-44556677889
```

Output:

```
{
        "status": "SUCCEEDED"
    }

```

### get-query-status-workload-insights-top-contributors-data

The following `get-query-status-workload-insights-top-contributors-data` example displays the current status of the query in the specified account.

```
aws networkflowmonitor get-query-status-workload-insights-top-contributors-data \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --query-id sample-dddd-eeee-ffff-44556677889
```

Output:

```
{
        "status": "SUCCEEDED"
    }

```

### get-query-results-workload-insights-top-contributors

The following `get-query-results-workload-insights-top-contributors` example displays the current status of the query in the specified account.

```
aws networkflowmonitor get-query-status-workload-insights-top-contributors \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --query-id sample-dddd-eeee-ffff-44556677889
```

Output:

```
{
        "status": "SUCCEEDED"
    }

```

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

## See scope information

The following `get-scope` example displays information about a scope, such as status, tags, name, and target details.

```
aws networkflowmonitor get-scope \
        --scope-id sample-aaaa-bbbb-cccc-11112222333
```

Output:

```
{
        "scopeId": "sample-aaaa-bbbb-cccc-11112222333",
        "status": "SUCCEEDED",
        "scopeArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:scope/sample-aaaa-bbbb-cccc-11112222333",
        "targets": [
            {
                "targetIdentifier": {
                    "targetId": {
                        "accountId": "111122223333"
                    },
                    "targetType": "ACCOUNT"
                },
                "region": "us-east-1"
            }
        ],
        "tags": {}
    }
```

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").

## See a list of monitors for an account

The following `list-monitors` example returns all the monitors in the specified account.

```
aws networkflowmonitor list-monitors
```

Output:

```
{
        "monitors": [
            {
                "monitorArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/Demo",
                "monitorName": "Demo",
                "monitorStatus": "ACTIVE"
            }
        ]
    }
```

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").

## See a list of scopes for an account

The following `list-scopes` example lists all the scopes in the specified account.

```
aws networkflowmonitor list-scopes
```

Output:

```
{
        "scopes": [
            {
                "scopeId": "sample-aaaa-bbbb-cccc-11112222333",
                "status": "SUCCEEDED",
                "scopeArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:scope/sample-aaaa-bbbb-cccc-11112222333"
            }
        ]
    }
```

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").

## See the list of tags for a monitor

The following `list-tags-for-resource` example returns all the tags associated with the specified resource.

```
aws networkflowmonitor list-tags-for-resource \
        --resource-arn arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/Demo
```

Output:

```
{
        "tags": {
            "Value": "Production",
            "Key": "stack"
        }
    }
```

For more information, see [Tagging your Amazon CloudWatch resources](CloudWatch-Tagging.md "CloudWatch-Tagging.md").

## Starting and stopping queries

The following sections provide example CLI commands for starting and stopping queries in Network Flow Monitor.

### start-query-monitor-top-contributors

The following `start-query-monitor-top-contributors` example starts the query which returns a queryId to retrieve the top contributors.

```
aws networkflowmonitor start-query-monitor-top-contributors \
        --monitor-name Demo \
        --start-time 2024-12-09T19:00:00Z \
        --end-time 2024-12-09T19:15:00Z \
        --metric-name DATA_TRANSFERRED \
        --destination-category UNCLASSIFIED
```

Output:

```
{
        "queryId": "sample-dddd-eeee-ffff-44556677889"
    }
```

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

### start-query-workload-insights-top-contributors-data

The following `start-query-workload-insights-top-contributors-data` example starts the query which returns a queryId to retrieve the top contributors.

```
aws networkflowmonitor start-query-workload-insights-top-contributors-data \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --start-time 2024-12-09T19:00:00Z \
        --end-time 2024-12-09T19:15:00Z \
        --metric-name DATA_TRANSFERRED \
        --destination-category UNCLASSIFIED
```

Output:

```
{
        "queryId": "sample-dddd-eeee-ffff-44556677889"
    }
```

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

### start-query-workload-insights-top-contributors

The following `start-query-workload-insights-top-contributors` example starts the query which returns a queryId to retrieve the top contributors.

```
aws networkflowmonitor start-query-workload-insights-top-contributors \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --start-time 2024-12-09T19:00:00Z \
        --end-time 2024-12-09T19:15:00Z \
        --metric-name DATA_TRANSFERRED \
        --destination-category UNCLASSIFIED
```

Output:

```
{
        "queryId": "sample-dddd-eeee-ffff-44556677889"
    }
```

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

### stop-query-monitor-top-contributors

The following `stop-query-monitor-top-contributors` example stops the query in the specified account.

```
aws networkflowmonitor stop-query-monitor-top-contributors \
        --monitor-name Demo \
        --query-id sample-dddd-eeee-ffff-44556677889
```

This command produces no output.

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

### stop-query-workload-insights-top-contributors-data

The following `stop-query-workload-insights-top-contributors-data` stops the query in the specified account.

```
aws networkflowmonitor stop-query-workload-insights-top-contributors-data \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --query-id sample-dddd-eeee-ffff-44556677889
```

This command produces no output.

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

### stop-query-workload-insights-top-contributors

The following `stop-query-workload-insights-top-contributors` example stops the query in the specified account.

```
aws networkflowmonitor stop-query-workload-insights-top-contributors \
        --scope-id sample-aaaa-bbbb-cccc-11112222333 \
        --query-id sample-dddd-eeee-ffff-44556677889
```

This command produces no output.

For more information, see [Evaluate network flows with workload insights](CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md "CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.md").

## Tag a monitor

The following `tag-resource` adds a tag to the monitor in the specified account.

```
aws networkflowmonitor tag-resource \
        --resource-arn arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/Demo \
        --tags Key=stack,Value=Production
```

This command produces no output.

For more information, see [Tagging your Amazon CloudWatch resources](CloudWatch-Tagging.md "CloudWatch-Tagging.md").

## Remove a tag from a monitor

The following `untag-resource` example removes a tag to the monitor in the specified account.

```
aws networkflowmonitor untag-resource \
        --resource-arn arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/Demo \
        --tag-keys stack
```

This command produces no output.

For more information, see [Tagging your Amazon CloudWatch resources](CloudWatch-Tagging.md "CloudWatch-Tagging.md").

## Update an existing monitor

The following `update-monitor` example updates the monitor named `Demo` in the specified account.

```
aws networkflowmonitor update-monitor \
        --monitor-name Demo \
        --local-resources-to-add type="AWS::EC2::VPC",identifier="arn:aws:ec2:us-east-1:111122223333:vpc/vpc-11223344556677889"
```

Output:

```
{
        "monitorArn": "arn:aws:networkflowmonitor:us-east-1:111122223333:monitor/Demo",
        "monitorName": "Demo",
        "monitorStatus": "ACTIVE",
        "tags": {
            "Value": "Production",
            "Key": "stack"
        }
    }
```

For more information, see [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").
