• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Viewing aggregated

counts of change requests (command line)

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

You can view aggregated counts of change requests in Change Manager, a tool in
AWS Systems Manager, by using the [GetOpsSummary](../APIReference/API_GetOpsSummary.md "../APIReference/API_GetOpsSummary.md") API operation. This API operation can return counts for a
single AWS account in a single AWS Region or for multiple accounts and multiple
Regions.

###### Note

If you want to view aggregated counts of change requests for multiple
AWS accounts and multiple AWS Regions, you must set up and configure a
resource data sync. For more information, see [Creating a resource data sync
for Inventory](inventory-create-resource-data-sync.md "inventory-create-resource-data-sync.md").

The following procedure describes how to use the AWS Command Line Interface (AWS CLI) (on Linux,
macOS, or Windows Server) to view aggregated counts of change requests.

###### To view aggregated counts of change requests

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run one of the following commands.

**Single account and Region**

This command returns a count of all change requests for the AWS account
and AWS Region for which your AWS CLI session is configured.

Linux & macOS

```
aws ssm get-ops-summary \
--filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal \
--aggregators AggregatorType=count,AttributeName=Status,TypeName=AWS:OpsItem
```

Windows

```
aws ssm get-ops-summary ^
--filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal ^
--aggregators AggregatorType=count,AttributeName=Status,TypeName=AWS:OpsItem
```

The call returns information like the following.

```
{
    "Entities": [
        {
            "Data": {
                "AWS:OpsItem": {
                    "Content": [
                        {
                            "Count": "38",
                            "Status": "Open"
                        }
                    ]
                }
            }
        }
    ]
}
```

**Multiple accounts and/or Regions**

This command returns a count of all change requests for the
AWS accounts and AWS Regions specified in the resource data sync.

Linux & macOS

```
aws ssm get-ops-summary \
    --sync-name `resource_data_sync_name` \
    --filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal \
    --aggregators AggregatorType=count,AttributeName=Status,TypeName=AWS:OpsItem
```

Windows

```
aws ssm get-ops-summary ^
    --sync-name `resource_data_sync_name` ^
    --filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal ^
    --aggregators AggregatorType=count,AttributeName=Status,TypeName=AWS:OpsItem
```

The call returns information like the following.

```
{
    "Entities": [
        {
            "Data": {
                "AWS:OpsItem": {
                    "Content": [
                        {
                            "Count": "43",
                            "Status": "Open"
                        },
                        {
                            "Count": "2",
                            "Status": "Resolved"
                        }
                    ]
                }
            }
        }
    ]
}
```

**Multiple accounts and a specific
Region**

This command returns a count of all change requests for the
AWS accounts specified in the resource data sync. However, it only returns
data from the Region specified in the command.

Linux & macOS

```
aws ssm get-ops-summary \
    --sync-name `resource_data_sync_name` \
    --filters Key=AWS:OpsItem.SourceRegion,Values='`Region`',Type=Equal Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal \
    --aggregators AggregatorType=count,AttributeName=Status,TypeName=AWS:OpsItem
```

Windows

```
aws ssm get-ops-summary ^
    --sync-name `resource_data_sync_name` ^
    --filters Key=AWS:OpsItem.SourceRegion,Values='`Region`',Type=Equal Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal ^
    --aggregators AggregatorType=count,AttributeName=Status,TypeName=AWS:OpsItem
```

**Multiple accounts and Regions with output grouped by
Region**

This command returns a count of all change requests for the
AWS accounts and AWS Regions specified in the resource data sync. The
output displays count information per Region.

Linux & macOS

```
aws ssm get-ops-summary \
    --sync-name `resource_data_sync_name` \
    --filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal \
    --aggregators '[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"Status","Aggregators":[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"SourceRegion"}]}]'
```

Windows

```
aws ssm get-ops-summary ^
    --sync-name `resource_data_sync_name` ^
    --filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal ^
    --aggregators '[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"Status","Aggregators":[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"SourceRegion"}]}]'
```

The call returns information like the following.

```
{
        "Entities": [
            {
                "Data": {
                    "AWS:OpsItem": {
                        "Content": [
                            {
                                "Count": "38",
                                "SourceRegion": "us-east-1",
                                "Status": "Open"
                            },
                            {
                                "Count": "4",
                                "SourceRegion": "us-east-2",
                                "Status": "Open"
                            },
                            {
                                "Count": "1",
                                "SourceRegion": "us-west-1",
                                "Status": "Open"
                            },
                            {
                                "Count": "2",
                                "SourceRegion": "us-east-2",
                                "Status": "Resolved"
                            }
                        ]
                    }
                }
            }
        ]
    }
```

**Multiple accounts and Regions with output grouped by
accounts and Regions**

This command returns a count of all change requests for the
AWS accounts and AWS Regions specified in the resource data sync. The
output groups the count information by accounts and Regions.

Linux & macOS

```
aws ssm get-ops-summary \
    --sync-name `resource_data_sync_name` \
    --filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal \
    --aggregators '[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"Status","Aggregators":[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"SourceAccountId","Aggregators":[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"SourceRegion"}]}]}]'
```

Windows

```
aws ssm get-ops-summary ^
    --sync-name `resource_data_sync_name` ^
    --filters Key=AWS:OpsItem.OpsItemType,Values="/aws/changerequests",Type=Equal ^
    --aggregators '[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"Status","Aggregators":[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"SourceAccountId","Aggregators":[{"AggregatorType":"count","TypeName":"AWS:OpsItem","AttributeName":"SourceRegion"}]}]}]'
```

The call returns information like the following.

```
{
    "Entities": [
        {
            "Data": {
                "AWS:OpsItem": {
                    "Content": [
                        {
                            "Count": "38",
                            "SourceAccountId": "123456789012",
                            "SourceRegion": "us-east-1",
                            "Status": "Open"
                        },
                        {
                            "Count": "4",
                            "SourceAccountId": "111122223333",
                            "SourceRegion": "us-east-2",
                            "Status": "Open"
                        },
                        {
                            "Count": "1",
                            "SourceAccountId": "111122223333",
                            "SourceRegion": "us-west-1",
                            "Status": "Open"
                        },
                        {
                            "Count": "2",
                            "SourceAccountId": "444455556666",
                            "SourceRegion": "us-east-2",
                            "Status": "Resolved"
                        },
                        {
                            "Count": "1",
                            "SourceAccountId": "222222222222",
                            "SourceRegion": "us-east-1",
                            "Status": "Open"
                        }
                    ]
                }
            }
        }
    ]
}
```
