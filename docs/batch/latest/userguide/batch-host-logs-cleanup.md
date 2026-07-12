# Step 5: Clean up resources

If you no longer need the host-level log collection, remove the following resources
to avoid unnecessary charges:

1. Delete or drain the compute environment that uses the launch
   template.
2. Delete the launch template from the Amazon EC2 console or by running
   `aws ec2 delete-launch-template`.
3. Detach and delete the `BatchHostLogsS3Access` IAM policy
   from your instance role.
4. Empty and delete the Amazon S3 bucket, or remove only the
   `ecs-logs/` and `fluent-bit/` prefixes if the bucket
   is shared with other workloads.
5. If you set `minvCpus` to a non-zero value for testing,
   reset it to zero to avoid unnecessary costs.
