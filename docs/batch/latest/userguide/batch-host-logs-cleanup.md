

# Step 5: Clean up resources
<a name="batch-host-logs-cleanup"></a>

If you no longer need the host-level log collection, remove the following resources to avoid unnecessary charges:

1. Delete or drain the compute environment that uses the launch template.

1. Delete the launch template from the Amazon EC2 console or by running `aws ec2 delete-launch-template`.

1. Detach and delete the `BatchHostLogsS3Access` IAM policy from your instance role.

1. Empty and delete the Amazon S3 bucket, or remove only the `ecs-logs/` and `fluent-bit/` prefixes if the bucket is shared with other workloads.

1. If you set `minvCpus` to a non-zero value for testing, reset it to zero to avoid unnecessary costs.