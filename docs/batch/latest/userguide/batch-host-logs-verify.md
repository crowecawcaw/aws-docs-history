

# Step 4: Verify and troubleshoot
<a name="batch-host-logs-verify"></a>

After you submit a job that triggers instance scale-up, verify that log files appear in the Amazon S3 bucket.

**Tip**  
To test log collection before a full rollout, set `minvCpus` to a non-zero value in your compute environment. This forces AWS Batch to scale up at least one instance without waiting for a job submission. Set `minvCpus` back to zero after testing to avoid unnecessary costs.

------
#### [ AWS Console ]

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Open your bucket and navigate to the `ecs-logs/` prefix.

1. Confirm that folders named with instance IDs appear. Each folder contains subdirectories for each log source.

------
#### [ AWS CLI ]

Run the following command to list uploaded log objects:

```
aws s3 ls s3://{{host-level-logs-bucket}}/ecs-logs/ --recursive
```

If the command returns objects organized by instance ID, date, and source tag, log collection is working correctly.

------

If logs are not appearing, connect to the instance by using SSH or SSM Session Manager to debug the Fluent Bit agent. Check the service status with `systemctl status fluent-bit`. Review `/var/log/cloud-init-output.log` to confirm the user-data script ran successfully.

When you use Spot instances or short-lived compute environments that scale to zero frequently, consider the following adjustments to avoid log data loss:
+ **Spot reclaim risk** – Lower the `upload_timeout` and `total_file_size` values in `fluent-bit.conf` to flush log data more frequently. This reduces the window of data that might be lost if an instance is reclaimed.
+ **Short-lived instances** – When AWS Batch scales to zero between jobs, lower the `Flush` interval and `upload_timeout` so that collected data is uploaded before the instance terminates.
+ **Amazon S3 lifecycle rules** – We recommend configuring an Amazon S3 lifecycle rule to expire or transition old log objects to a lower-cost storage class. This prevents unbounded storage growth.