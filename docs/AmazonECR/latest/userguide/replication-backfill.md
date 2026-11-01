

# Replication backfill
<a name="replication-backfill"></a>

You can replicate preexisting images in your Amazon ECR private registry to your configured replication destinations. By default, replication only applies to images pushed after the replication configuration is applied. Replication backfill allows you to replicate images that you pushed before you configured replication.

## How replication backfill works
<a name="replication-backfill-how-it-works"></a>

When you start a replication backfill, you specify a single destination consisting of a Region and registry ID. Amazon ECR evaluates your existing replication configuration to determine which images in your registry qualify for backfill to the specified destination. Only images that match your current replication configuration rules are included in the backfill.

Each replication backfill targets a single destination. To backfill images to multiple destinations, start a separate replication backfill for each destination. Each one is identified by a unique `replicationBackfillId` that you use to monitor progress, view results, and stop it if needed.

## Replication backfill lifecycle
<a name="replication-backfill-lifecycle"></a>

A replication backfill transitions through the following statuses:
+ `PREPARING`: Amazon ECR is identifying qualifying images in your registry.
+ `IN_PROGRESS`: Amazon ECR is actively replicating images to the destination.
+ `COMPLETE`: All qualifying images were successfully replicated.
+ `FAILED`: A replication backfill automatically fails if 50% or more of the underlying replications fail. This threshold is only evaluated once at least 100 replications are processed.
+ `STOPPING`: A stop was requested and Amazon ECR is waiting for in-flight replications to complete.
+ `STOPPED`: You stopped the replication backfill and all in-flight replications have ended.

**Note**  
You can stop a replication backfill only when it is in the `PREPARING` or `IN_PROGRESS` status.

## Considerations for replication backfill
<a name="replication-backfill-considerations"></a>

The following should be considered when using replication backfill.
+ Only images that match your current replication configuration for the specified destination are included in the backfill. If you need to backfill images to a destination that is not in your replication configuration, you must first add that destination to your replication rules.
+ You can run up to 10 replication backfills concurrently per registry. If you start more, Amazon ECR returns a `LimitExceededException` error.
+ You can have only one active replication backfill for a given destination Region at a time. A second request for the same destination Region returns a `ReplicationBackfillInProgressException` error.
+ Amazon ECR retains replication backfills in a terminal state (`COMPLETE`, `FAILED`, or `STOPPED`) for 90 days after completion. During that time, they remain visible in `ListReplicationBackfills` responses.
+ Stopping a replication backfill does not roll back images that it already replicated. Those images remain in the destination registry.
+ Replication backfill uses the same service-linked role that Amazon ECR creates when you first configure replication for your private registry.
+ Most registries are expected to complete backfill within an hour. However, a registry that contains a large amount of data can take hours or even days to fully backfill.
+ Replication backfill skips images whose source repository was deleted. Those images appear with a `FAILED` status in the backfill results.
+ Amazon ECR sends an EventBridge event when a replication backfill reaches a terminal status. For more information, see [Sample events from Amazon ECR](ecr-eventbridge.md#ecr-eventbridge-bus).

## Starting a replication backfill
<a name="replication-backfill-start"></a>

### To start a replication backfill (AWS Management Console)
<a name="replication-backfill-start-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region of the source registry to backfill from.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, choose ** Settings** and then choose **Edit** under **Replication configuration**.

1. On the **Replication** page, choose the **Backfill jobs** tab.

1. Choose **Start backfill job**.

1. Choose up to 10 destinations that you want to backfill to.

1. Choose **Start backfill jobs**.

### To start a replication backfill (AWS CLI)
<a name="replication-backfill-start-cli"></a>
+ Start a replication backfill.

  ```
  aws ecr start-replication-backfill \
      --region {{us-west-2}} \
      --registry-id {{aws_account_id}} \
      --destination region={{destination_region}},registryId={{destination_aws_account_id}}
  ```

## Monitoring replication backfill progress and viewing results
<a name="replication-backfill-monitor"></a>

### To monitor replication backfill progress and view replication backfill results (AWS Management Console)
<a name="replication-backfill-monitor-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains your replication backfills.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, choose ** Settings** and then choose **Edit** under **Replication configuration**.

1. On the **Replication** page, choose the **Backfill jobs** tab to monitor the progress and view the results of your replication backfills.

### To monitor replication backfill progress and view replication backfill results (AWS CLI)
<a name="replication-backfill-monitor-cli"></a>

1. To monitor the progress or view the results of a replication backfill, run the following command. While the replication backfill is in progress, the response contains only progress counts. Per-image results and pagination are available only after it completes.

   ```
   aws ecr describe-replication-backfill-results \
       --region {{us-west-2}} \
       --registry-id {{aws_account_id}} \
       --replication-backfill-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
       --max-results 1000 \
       --result-status-filter COMPLETE
   ```

1. To view summary information of all replication backfills, run the following command.

   ```
   aws ecr list-replication-backfills \
       --region {{us-west-2}} \
       --registry-id {{aws_account_id}} \
       --max-results 50
   ```

## Stopping a replication backfill
<a name="replication-backfill-stop"></a>

### To stop a replication backfill (AWS Management Console)
<a name="replication-backfill-stop-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains your replication backfills.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, choose ** Settings** and then choose **Edit** under **Replication configuration**.

1. On the **Replication** page, choose the **Backfill jobs** tab.

1. Choose the replication backfill that you want to stop.

1. Choose **Stop backfill job**.

### To stop a replication backfill (AWS CLI)
<a name="replication-backfill-stop-cli"></a>
+ To stop a replication backfill, run the following command.

  ```
  aws ecr stop-replication-backfill \
      --region {{us-west-2}} \
      --registry-id {{aws_account_id}} \
      --replication-backfill-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
  ```