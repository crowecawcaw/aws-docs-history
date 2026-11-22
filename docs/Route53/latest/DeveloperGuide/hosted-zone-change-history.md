

# Viewing the change history of a hosted zone

Change History shows the changes to the DNS records in a hosted zone. You can use it to answer questions such as the following:
+ Who changed the records in this hosted zone last week?
+ When did the value of `www.example.com` change, and who changed it?
+ Which changes has the hosted zone received since the last change that my system processed?

Change History is available only for hosted zones that use the `ADVANCED` tier, and it's enabled by default for those hosted zones. For more information about tiers, see [Hosted zone tiers](hosted-zone-tiers.md).

**Topics**
+ [How Change History works](#hosted-zone-change-history-how-it-works)
+ [Understanding how the tier affects Change History](#hosted-zone-change-history-on-off)
+ [Viewing changes](#hosted-zone-change-history-view)
+ [Change History compared with CloudTrail](#hosted-zone-change-history-vs-cloudtrail)
+ [Reading new changes into another system](#hosted-zone-change-history-sync)
+ [Permissions for Change History](hosted-zone-change-history-permissions.md)

## How Change History works
<a name="hosted-zone-change-history-how-it-works"></a>

Route 53 records each [change batch](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeBatch.html) that it applies to the hosted zone, which is the set of changes that Route 53 records for one request, such as a `ChangeResourceRecordSets` request, and retains it for 365 days. For each change batch, Change History shows who submitted it, when it was submitted, and which records changed, in the same format that `ListResourceRecordSets` returns. For an `UPSERT`, Change History shows the new values, so to see the earlier values, look at the previous change to the same record.

Each change batch includes the following information:

**`ChangeId`**  
The ID of the change batch. This is the same ID that `ChangeResourceRecordSets` returns in `ChangeInfo/Id` and that you pass to `GetChange`.

**`Operation`**  
The Route 53 API operation that submitted the change batch. Valid values: `ChangeResourceRecordSets` \| `CreateHostedZone`. A hosted zone that you create on the `ADVANCED` tier starts its history with a `CreateHostedZone` entry.

**`SubmittedAt`**  
The date and time, in UTC, when the change batch was submitted. Route 53 lists change batches in the order in which it applied them, so `SubmittedAt` values aren't always in strict order.

**`SubmittedBy`**  
The ARN of the principal that submitted the request, for example `arn:aws:sts::111122223333:assumed-role/Admin/my-session`.

**`RequestId`**  
The request ID of the call that submitted the change batch.

**`Comment`**  
The comment from the `ChangeResourceRecordSets` request, if any.

**`ChangeCount`**  
The number of changes in the change batch. For `CreateHostedZone`, the value is 0, because the entry doesn't list the name server (NS) and start of authority (SOA) records that Route 53 creates with the hosted zone.

Change History shows only changes to records. It doesn't show changes to the hosted zone itself, such as its comment, tier, features, or VPC associations, or changes to other resources, such as health checks, CIDR collections, DNSSEC signing, and query logging configurations. To audit those changes, use CloudTrail. For more information, see [Change History compared with CloudTrail](#hosted-zone-change-history-vs-cloudtrail).

When you delete a hosted zone, you can no longer read its change history. If you need the history, read it and store it before you delete the hosted zone.

## Understanding how the tier affects Change History
<a name="hosted-zone-change-history-on-off"></a>

Route 53 records changes whenever a hosted zone uses the `ADVANCED` tier. `RetentionStartsAt` is the earliest time that you can read changes from:
+ When you create a hosted zone on the `ADVANCED` tier, `RetentionStartsAt` is the time when you created the hosted zone.
+ When you upgrade a hosted zone to `ADVANCED`, `RetentionStartsAt` is the time of the upgrade. Changes from before the upgrade aren't available.

**Warning**  
When you change a hosted zone from `ADVANCED` to `STANDARD`, you permanently lose access to its change history. If you upgrade the hosted zone to `ADVANCED` again, even right away, Route 53 starts a new history from the time of the upgrade and doesn't restore the earlier changes. Before you downgrade, read and store any history that you need.

To change the tier of a hosted zone, see [Changing the tier of a hosted zone](hosted-zone-tiers.md#hosted-zone-tiers-change).

To see `RetentionStartsAt`, call [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html). The following AWS Command Line Interface (AWS CLI) command shows only the Change History element of the response:

```bash
aws route53 get-hosted-zone \
    --id {{Z11111112222222333333}} \
    --query 'HostedZone.Features.ChangeHistory'
```

Example output:

```json
{
    "Status": "ENABLED",
    "RetentionStartsAt": "2026-11-20T16:05:31.214000+00:00"
}
```

For a hosted zone that uses the `STANDARD` tier, `Status` is `DISABLED` and the response doesn't include `RetentionStartsAt`.

## Viewing changes
<a name="hosted-zone-change-history-view"></a>

You can view the change history of a hosted zone in the Route 53 console, with the AWS CLI, or with an AWS SDK.

### Using the Route 53 console
<a name="hosted-zone-change-history-console"></a>

**To view the change history of a hosted zone**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of an advanced hosted zone.

1. Choose the **Change history** tab.

   The tab lists the change batches in the hosted zone, newest first.

1. (Optional) To show only some changes, do one or both of the following:

   1. To show the changes in a time range, select a time range.

   1. To show the changes to one record, enter its record name and select its type. The list then shows one row for each change to records with that name and type.

1. To view the changes in a batch, select it. The details panel shows each change in the batch, its action, and the record values.

### Using the AWS CLI
<a name="hosted-zone-change-history-cli"></a>

Use the AWS CLI commands for the following actions:
+ [ListHostedZoneChangeBatches](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZoneChangeBatches.html) lists the change batches in a hosted zone, with a summary of each batch.
+ [GetHostedZoneChangeBatch](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneChangeBatch.html) returns one change batch, including every change in it.
+ [ListResourceRecordSetChanges](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSetChanges.html) lists the individual changes in a hosted zone, optionally only the changes to the records that have a specific name and type.

For the request parameters, such as the time range, sort order, and paging, see each action's page in the [Amazon Route 53 API Reference](https://docs.aws.amazon.com/Route53/latest/APIReference/). The AWS CLI follows `NextToken` for you and returns every page. To control paging, use `--page-size`, `--max-items`, and `--starting-token`. In the following examples, replace {{Z11111112222222333333}} with the ID of your hosted zone.

**To list the change batches in a hosted zone**
+ The following AWS CLI command lists the change batches that were submitted to the hosted zone on December 1, 2026, newest first.

  ```bash
  aws route53 list-hosted-zone-change-batches \
      --hosted-zone-id {{Z11111112222222333333}} \
      --submitted-after 2026-12-01T00:00:00Z \
      --submitted-before 2026-12-02T00:00:00Z
  ```

  Example output:

  ```json
  {
      "ChangeBatchSummaries": [
          {
              "ChangeId": "C2682N5HXP0BZ4",
              "Operation": "ChangeResourceRecordSets",
              "SubmittedAt": "2026-12-01T17:42:10.123000+00:00",
              "SubmittedBy": "arn:aws:sts::111122223333:assumed-role/Admin/my-session",
              "RequestId": "b25f48e8-84fd-11e6-80d9-574EXAMPLE11",
              "Comment": "Move www to the new load balancer",
              "ChangeCount": 2
          },
          {
              "ChangeId": "C1PA6795UKMFR9",
              "Operation": "ChangeResourceRecordSets",
              "SubmittedAt": "2026-12-01T09:15:47.508000+00:00",
              "SubmittedBy": "arn:aws:sts::111122223333:assumed-role/Deploy/my-pipeline-session",
              "RequestId": "0f9a8c2e-3b1d-4a5e-9c7f-2d6EXAMPLE22",
              "ChangeCount": 1
          }
      ]
  }
  ```

**To get the changes in a change batch**
+ The following AWS CLI command returns the change batch with the ID `C2682N5HXP0BZ4`. You can specify the ID with or without the `/change/` prefix that `ChangeResourceRecordSets` returns.

  ```bash
  aws route53 get-hosted-zone-change-batch \
      --hosted-zone-id {{Z11111112222222333333}} \
      --change-id C2682N5HXP0BZ4
  ```

  Example output:

  ```json
  {
      "ChangeBatchSummary": {
          "ChangeId": "C2682N5HXP0BZ4",
          "Operation": "ChangeResourceRecordSets",
          "SubmittedAt": "2026-12-01T17:42:10.123000+00:00",
          "SubmittedBy": "arn:aws:sts::111122223333:assumed-role/Admin/my-session",
          "RequestId": "b25f48e8-84fd-11e6-80d9-574EXAMPLE11",
          "Comment": "Move www to the new load balancer",
          "ChangeCount": 2
      },
      "ChangeBatch": {
          "Comment": "Move www to the new load balancer",
          "Changes": [
              {
                  "Action": "UPSERT",
                  "ResourceRecordSet": {
                      "Name": "www.example.com.",
                      "Type": "A",
                      "TTL": 60,
                      "ResourceRecords": [
                          {
                              "Value": "10.0.1.44"
                          }
                      ]
                  }
              },
              {
                  "Action": "DELETE",
                  "ResourceRecordSet": {
                      "Name": "old.example.com.",
                      "Type": "A",
                      "TTL": 300,
                      "ResourceRecords": [
                          {
                              "Value": "10.0.2.7"
                          }
                      ]
                  }
              }
          ]
      }
  }
  ```

**To list the changes to one record**
+ The following AWS CLI command lists the changes to the `A` records for `www.example.com`, newest first.

  ```bash
  aws route53 list-resource-record-set-changes \
      --hosted-zone-id {{Z11111112222222333333}} \
      --record-name www.example.com \
      --record-type A
  ```

  Example output:

  ```json
  {
      "ResourceRecordSetChanges": [
          {
              "ChangeId": "C2682N5HXP0BZ4",
              "Operation": "ChangeResourceRecordSets",
              "SubmittedAt": "2026-12-01T17:42:10.123000+00:00",
              "SubmittedBy": "arn:aws:sts::111122223333:assumed-role/Admin/my-session",
              "RequestId": "b25f48e8-84fd-11e6-80d9-574EXAMPLE11",
              "Action": "UPSERT",
              "ResourceRecordSet": {
                  "Name": "www.example.com.",
                  "Type": "A",
                  "TTL": 60,
                  "ResourceRecords": [
                      {
                          "Value": "10.0.1.44"
                      }
                  ]
              }
          },
          {
              "ChangeId": "C0X4HN2R6YPLA7",
              "Operation": "ChangeResourceRecordSets",
              "SubmittedAt": "2026-11-30T21:15:03.402000+00:00",
              "SubmittedBy": "arn:aws:sts::111122223333:assumed-role/Admin/my-session",
              "RequestId": "e4b8d2a6-0f71-4c39-a5e2-6d9EXAMPLE44",
              "Action": "UPSERT",
              "ResourceRecordSet": {
                  "Name": "www.example.com.",
                  "Type": "A",
                  "TTL": 60,
                  "ResourceRecords": [
                      {
                          "Value": "10.0.1.10"
                      }
                  ]
              }
          },
          {
              "ChangeId": "C3QW7VKZ8M1TJ2",
              "Operation": "ChangeResourceRecordSets",
              "SubmittedAt": "2026-11-24T10:02:11.870000+00:00",
              "SubmittedBy": "arn:aws:sts::111122223333:assumed-role/Deploy/my-pipeline-session",
              "RequestId": "7c1e9f04-5a2b-4d8e-b3f6-91aEXAMPLE33",
              "Action": "CREATE",
              "ResourceRecordSet": {
                  "Name": "www.example.com.",
                  "Type": "A",
                  "TTL": 300,
                  "ResourceRecords": [
                      {
                          "Value": "10.0.1.10"
                      }
                  ]
              }
          }
      ]
  }
  ```

  Each entry shows one change, with the full record that the change wrote or deleted. Weighted, latency, and other records that have the same name and type appear as separate entries, each with its `SetIdentifier`.

### Using an AWS SDK
<a name="hosted-zone-change-history-sdk"></a>

Call the [ListHostedZoneChangeBatches](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZoneChangeBatches.html), [GetHostedZoneChangeBatch](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneChangeBatch.html), and [ListResourceRecordSetChanges](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSetChanges.html) APIs. The following AWS SDK for Python (Boto3) example prints each change that was submitted to the hosted zone on December 1, 2026, with who submitted it. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

```python
import boto3

route53 = boto3.client("route53")
zone_id = "{{Z11111112222222333333}}"

paginator = route53.get_paginator("list_hosted_zone_change_batches")
for page in paginator.paginate(
    HostedZoneId=zone_id,
    SubmittedAfter="2026-12-01T00:00:00Z",
    SubmittedBefore="2026-12-02T00:00:00Z",
):
    for summary in page["ChangeBatchSummaries"]:
        batch = route53.get_hosted_zone_change_batch(
            HostedZoneId=zone_id, ChangeId=summary["ChangeId"]
        )
        for change in batch["ChangeBatch"]["Changes"]:
            record = change["ResourceRecordSet"]
            print(summary["SubmittedAt"], summary.get("SubmittedBy"),
                  change["Action"], record["Name"], record["Type"])
```

## Change History compared with CloudTrail
<a name="hosted-zone-change-history-vs-cloudtrail"></a>

Change History and CloudTrail both show who changed a hosted zone, but they answer different questions. Use Change History to see what changed in the records of a hosted zone. Use CloudTrail to see every call to the Route 53 API in your account. The following table compares them.


|  | Change History | CloudTrail | 
| --- | --- | --- | 
| What it records | Each change batch that Route 53 applied to the records in a hosted zone, with the full record that each change wrote or deleted. | Calls to Route 53 API actions, including read calls, calls that fail, and changes to resources other than records, such as health checks and VPC associations. | 
| How to find the changes to one record | Call `ListResourceRecordSetChanges` with the record name and type. The results include only changes that Route 53 applied. | Search the `ChangeResourceRecordSets` events for the hosted zone, and read the changes in `requestParameters.changeBatch`. Each event shows the request as it was sent, including requests that Route 53 rejected. | 
| How long it's available | 365 days after each change batch was submitted. Changes from before `RetentionStartsAt` aren't available. | The last 90 days in **Event history**. To keep events longer, create a trail that delivers them to an Amazon S3 bucket. | 
| Setup | Enabled by default for every advanced hosted zone. | **Event history** is on for every AWS account. A trail must be created. | 
| Reading new changes into another system | Read the change batches in the order that Route 53 applied them, and resume after the last change batch that you processed with `StartAfterChangeId`. For more information, see [Reading new changes into another system](#hosted-zone-change-history-sync). | Process the events that the trail delivers. | 

To find the CloudTrail event for a change batch, match the change batch's `RequestId` to the event's `requestID`, or its `ChangeId` to `responseElements.changeInfo.id`. The event includes details that Change History doesn't, such as the IP address that the request came from.

For more information about CloudTrail, see [Logging Amazon Route 53 API calls with AWS CloudTrail](logging-using-cloudtrail.md).

## Reading new changes into another system
<a name="hosted-zone-change-history-sync"></a>

To keep a copy of a hosted zone in another system, such as an inventory or an audit store, read the records once and then read new change batches as they arrive:

1. Find the starting point. Call `ListHostedZoneChangeBatches` with `MaxResults` set to 1 and the default `SortOrder` (`DESCENDING`), and save the `ChangeId` of the newest change batch. If the response has no change batches, leave out `StartAfterChangeId` when you list new changes.

1. Read the current records with [ListResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSets.html).

1. Call `ListHostedZoneChangeBatches` with `SortOrder` set to `ASCENDING` and `StartAfterChangeId` set to the saved `ChangeId`. Follow `NextToken` until the response doesn't include it.

1. For each change batch, call `GetHostedZoneChangeBatch` to get its changes, apply them, and save its `ChangeId`. Changes made while you read the records can already be in your copy, so apply each change so that applying it again has no effect.

1. To check for new changes later, repeat the previous two steps, starting after the saved `ChangeId`.

Save the last `ChangeId` that you processed rather than a `NextToken`, because a `NextToken` expires after 24 hours. If `StartAfterChangeId` returns an `InvalidInput` error because the change batch expired or the hosted zone was downgraded to `STANDARD` and upgraded again, read the records again with `ListResourceRecordSets` and start over.