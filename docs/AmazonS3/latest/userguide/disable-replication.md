# Managing or pausing live replication

Live replication is the automatic, asynchronous copying of objects across buckets in the
same or different AWS Regions. After you set up your replication configuration, Amazon S3
replicates newly created objects and object updates from a source bucket to one or more
specified destination buckets.

You use the Amazon S3 console to add replication rules to the source bucket. Replication rules
define the source bucket objects to replicate and the destination bucket or buckets where the
replicated objects are stored. For more information about replication, see [Replicating objects within and across Regions](replication.md "replication.md").

You can manage replication rules on the **Replication** page in the Amazon S3
console. You can add, view, edit, enable, disable, or delete replication rules. You can also
change the priority of your replication rules. For information about adding replication rules to
a bucket, see [Using the S3 console](replication-walkthrough1.md#enable-replication "replication-walkthrough1.md#enable-replication").

###### To manage the replication rules for a bucket by using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. On the **General purpose buckets** tab, choose the name of the bucket
   that you want.
4. Choose the **Management** tab, and then scroll down to
   **Replication rules**.
5. You can change your replication rules in the following ways:
   - To enable or disable a replication rule, choose the option button to the left of the
     rule. On the **Actions** menu, choose **Enable rule**
     or **Disable rule**. You can also disable, enable, or delete all the
     rules in the bucket from the **Actions** menu.

   ###### Note

   If you disable a replication rule and then later re-enable the rule, any new or
   changed objects that weren't replicated while the rule was disabled are _not_ automatically replicated when the rule is re-enabled.
   To replicate those objects, you must use S3 Batch Replication. For more information,
   see [Replicating existing objects with
   Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md").
   - To change the priority of a rule, choose the option button to the left of the rule,
     and then choose **Edit rule**.

   You set rule priorities to avoid conflicts caused by objects that are included in
   the scope of more than one rule. In the case of overlapping rules, Amazon S3 uses the rule
   priority to determine which rule to apply. The higher the number, the higher the
   priority. For more information about rule priority, see [Replication configuration file elements](replication-add-config.md "replication-add-config.md").

## Pausing or stopping replication

To temporarily pause replication and have it automatically resume later, you can use the
`aws:s3:bucket-pause-replication` action in AWS Fault Injection Service. For more information, see
[aws:s3:bucket-pause-replication](../../../fis/latest/userguide/fis-actions-reference.md#bucket-pause-replication "../../../fis/latest/userguide/fis-actions-reference.md#bucket-pause-replication") and [Pause S3 Replication](../../../fis/latest/userguide/cross-region-scenario.md#cross-region-scenario-actions-pause-s3-replication "../../../fis/latest/userguide/cross-region-scenario.md#cross-region-scenario-actions-pause-s3-replication") in the _AWS Fault Injection Service User
Guide_.

To stop replication in Amazon S3, we recommend disabling your replication rules. If you disable
a replication rule and then later re-enable the rule, any new or changed objects that weren't
replicated while the rule was disabled are _not_
automatically replicated when the rule is re-enabled. To replicate those objects, you must use
S3 Batch Replication. For more information, see [Replicating existing objects with
Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

Replication will also stop if you remove the AWS Identity and Access Management (IAM) role, the AWS Key Management Service (AWS KMS)
permissions, or the bucket policy permissions that grant Amazon S3 the required permissions.
However, we don't recommend these approaches because they cause replication to fail. Amazon S3
reports the replication status for affected objects as `FAILED`. If permissions are
later restored, objects marked as `FAILED` are _not_ automatically replicated. To replicate those objects, you must use
S3 Batch Replication.
