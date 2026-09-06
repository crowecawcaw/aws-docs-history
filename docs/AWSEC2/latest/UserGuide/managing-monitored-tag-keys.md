

# Managing monitored tag keys
<a name="managing-monitored-tag-keys"></a>

Amazon EC2 Capacity Manager lets you select tag keys from your Amazon EC2 resources (for example, `environment` or `team`) to use as dimensions when analyzing your capacity data. After a tag key is activated, you can group and filter your metrics by that tag's values — just like you can with Region, Instance Type, or Availability Zone.

Each account can monitor up to five tag keys. Capacity Manager-provided tags do not count toward this limit.

**Topics**
+ [Capacity Manager-provided tags](#cm-provided-tags)
+ [Tag lifecycle](#tag-lifecycle)
+ [Activate and deactivate monitored tag keys](#activate-deactivate-tag-keys)
+ [View monitored tag keys](#view-monitored-tag-keys)
+ [Query metrics using tag dimensions](#query-metrics-tag-dimensions)
+ [Tags in data exports](#tags-in-data-exports)
+ [Organizations and delegated administrator](#tag-keys-organizations)
+ [Considerations](#tag-keys-considerations)

## Capacity Manager-provided tags
<a name="cm-provided-tags"></a>

Capacity Manager includes a set of default tags for every account. These do not count toward your tag key limit. Capacity Manager-provided tags represent commonly used grouping dimensions and include:
+ `aws:autoscaling:groupName` — EC2 Auto Scaling Group
+ `aws:eks:cluster-name` — EKS cluster name
+ `eks:kubernetes-node-pool-name` — EKS Kubernetes node pool
+ `karpenter.sh/nodepool` — Karpenter node pool

Capacity Manager-provided tags appear in `GetCapacityManagerMonitoredTagKeys` with `CapacityManagerProvided` set to `true` and cannot be activated or deactivated by the customer. When Capacity Manager is first enabled, Capacity Manager-provided tags start in `activating` status and transition to `activated` after Capacity Manager receives the first data point that includes a Capacity Manager-provided tag, typically within one to two hours.

## Tag lifecycle
<a name="tag-lifecycle"></a>

Monitored tag keys progress through the following statuses:


| Status | Description | 
| --- | --- | 
| activating | The tag key is registered. Capacity Manager is preparing to collect data for this tag. You cannot query metrics using a tag in this status. | 
| activated | Tag data is being ingested and is queryable through the metric APIs and in data exports. | 
| suspended | The tag key has exceeded the threshold of 100,000 unique tag values. The tag still counts toward your limit, but Capacity Manager no longer ingests data for it. If your tag value usage decreases below the threshold for a sustained period, the tag is reactivated automatically. | 
| deactivating | The tag key is being removed. It will no longer appear in GetCapacityManagerMonitoredTagKeys after deactivation completes. | 

When a tag is in `suspended` status, `GetCapacityManagerMonitoredTagKeys` returns the following status message: "Tag suspended due to too many tag values. Reduce the usage of the tag or deactivate it."

**Note**  
If you deactivate a tag key and later re-activate the same key, only data ingested after re-activation is queryable. Historical data from the previous activation is not accessible. The `EarliestDatapointTimestamp` resets with each new activation.

## Activate and deactivate monitored tag keys
<a name="activate-deactivate-tag-keys"></a>

You can activate tag keys to begin monitoring them as dimensions, or deactivate tag keys you no longer need. Activation is asynchronous — the tag enters an `activating` state and transitions to `activated` after Capacity Manager begins receiving data for that tag. Deactivation removes the tag key from your monitored set.

**Note**  
When activating a tag key, enter only the key name (for example, `environment`). Capacity Manager automatically makes it available as a dimension for grouping and filtering your metrics.

------
#### [ Console ]

**To activate or deactivate monitored tag keys**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the **Settings** tab.

1. In the **Monitored tag keys** section, choose **Manage tag keys**.

1. To activate a tag key, enter the tag key name and choose **Add**. To deactivate a tag key, select the tag key and choose **Remove**.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To activate tag keys**  
Use the following command to activate one or more tag keys:

```
aws ec2 update-capacity-manager-monitored-tag-keys \
    --activate-tag-keys "environment" "teamId"
```

The output shows the tag keys and their initial statuses:

```
{
    "CapacityManagerTagKeys": [
        {
            "TagKey": "environment",
            "Status": "activating"
        },
        {
            "TagKey": "teamId",
            "Status": "activating"
        }
    ]
}
```

**To deactivate tag keys**  
Use the following command to deactivate one or more tag keys:

```
aws ec2 update-capacity-manager-monitored-tag-keys \
    --deactivate-tag-keys "project"
```

The output shows the updated statuses:

```
{
    "CapacityManagerTagKeys": [
        {
            "TagKey": "project",
            "Status": "deactivating"
        }
    ]
}
```

You can activate and deactivate tag keys in the same request:

```
aws ec2 update-capacity-manager-monitored-tag-keys \
    --activate-tag-keys "environment" "teamId" \
    --deactivate-tag-keys "project"
```

------

## View monitored tag keys
<a name="view-monitored-tag-keys"></a>

You can view all monitored tag keys for your account, including their current status and the earliest timestamp from which data is available.

------
#### [ Console ]

**To view monitored tag keys**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the **Settings** tab.

1. In the **Monitored tag keys** section, view your tag keys, their statuses, and whether they are Capacity Manager-provided tags.

------
#### [ AWS CLI ]

**To view monitored tag keys**  
Run the following command:

```
aws ec2 get-capacity-manager-monitored-tag-keys
```

The output lists all tag keys, including Capacity Manager-provided tags and customer-managed tags:

```
{
    "CapacityManagerTagKeys": [
        {
            "TagKey": "aws:autoscaling:groupName",
            "Status": "activated",
            "CapacityManagerProvided": true,
            "earliestDatapointTimestamp": "2026-04-08T00:00:00"
        },
        {
            "TagKey": "environment",
            "Status": "activated",
            "CapacityManagerProvided": false,
            "earliestDatapointTimestamp": "2025-08-11T22:00:00"
        }
    ]
}
```

The `CapacityManagerProvided` field indicates whether a tag is a Capacity Manager-provided tag (`true`) or a customer-managed tag (`false`). Capacity Manager-provided tags do not count toward your tag key limit. The `EarliestDatapointTimestamp` indicates the earliest point in time from which data is available for that tag key.

------

## Query metrics using tag dimensions
<a name="query-metrics-tag-dimensions"></a>

After a tag key reaches `activated` status, you can use it as a dimension in `GetCapacityManagerMetricDimensions` and `GetCapacityManagerMetricData`.

**To query metrics grouped by a tag dimension**  
Use the following command:

```
aws ec2 get-capacity-manager-metric-dimensions \
    --group-by tag:environment account-id \
    --filter-by 'DimensionCondition={Dimension=tag:environment,Comparison=equals,Values=[prod]}'
```

When you group by a tag dimension, the results include all resources in your account — not only those that have the tag. Resources that do not have a value for the tag are grouped into a separate bucket with an empty string value. For example, if your account used 800 vCPU hours in a given period and only some of those resources have an `environment` tag, grouping by the `environment` tag key might return:
+ `prod` — 300 vCPU hours
+ `staging` — 200 vCPU hours
+ `""` (empty string) — 300 vCPU hours from resources without an `environment` tag

This ensures that the totals across all buckets account for your full usage. You can explicitly filter for untagged resources by passing an empty string as the filter value:

```
--filter-by 'DimensionCondition={Dimension=tag:environment,Comparison=equals,Values=[""]}'
```

**Note**  
If you query with a tag key that is still in `activating` status, the query is rejected with a 400 error. Wait for the tag's status to change to `activated` before querying. You can check the status using `GetCapacityManagerMonitoredTagKeys`.

**Note**  
Queries with a start time before the `EarliestDatapointTimestamp` of any supplied tag dimension are rejected. Use `GetCapacityManagerMonitoredTagKeys` to check when data became available for each tag.

## Tags in data exports
<a name="tags-in-data-exports"></a>

When you enable tag monitoring, your data exports include activated tag keys and Capacity Manager-provided tags as additional columns. Tag columns appear after all standard columns with headers such as `tag:environment` and `tag:team`. Tag columns are sorted alphabetically.

Exports include only tags in `activated` status. Capacity Manager excludes tags in `activating`, `deactivating`, or `suspended` status.

**Note**  
If you activate a new tag key, existing data exports do not automatically include the new tag. You must create a new data export to include the newly activated tag key as a column.

## Organizations and delegated administrator
<a name="tag-keys-organizations"></a>

When your account is part of an AWS Organization with an organization-level Capacity Manager enabled, each account (the organization administrator and the delegated administrator) can independently activate, deactivate, and query tag keys. Each account maintains its own tag status, `EarliestDatapointTimestamp`, and tag key limit.

An account can only query metric data for tag keys that the account itself has activated. If both the organization administrator and a delegated administrator activate the same tag key (for example, `environment`), each account tracks its own activation status and data availability independently.

When the delegated administrator deactivates a tag key, the delegated administrator can no longer query data for that tag, even if the organization administrator still has the same tag key activated.

## Considerations
<a name="tag-keys-considerations"></a>
+ **Tag value updates:** Tag values for new resources and tags newly applied to existing resources are available within a few hours. If you change the value of an existing tag on a resource, the updated value can take up to 24 hours to reflect in Capacity Manager.
+ **Activation time:** After you activate a tag key, it can take up to 24 hours before the tag transitions to `activated` status and data becomes queryable. The `EarliestDatapointTimestamp` represents when data is available, not when the tag was activated.
+ **Tag key limit:** Each account can monitor up to five tag keys. Capacity Manager-provided tags do not count toward this limit.
+ **Tag key character requirements:** Tag keys can contain Unicode letters, digits, white space, and the following characters: `_ . : / = + @ -`. Tag keys must not exceed 128 characters.
+ **Re-activation:** If you deactivate and re-activate the same tag key, only new data is available. The `EarliestDatapointTimestamp` resets with each activation.
+ **Suspended tags:** Each tag key supports up to 100,000 unique tag values. If a tag key exceeds this threshold, it is moved to `suspended` status. The tag still counts toward your limit but data is no longer ingested. Reduce the number of unique values for the tag or deactivate it to free up space for another tag key.