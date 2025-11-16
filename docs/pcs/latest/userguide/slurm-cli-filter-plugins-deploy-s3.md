# Use Amazon S3 to deploy a CLI Filter Plugin script

in AWS PCS

Use S3 to deploy your CLI Filter Plugin script when you want to update job submission logic
on a live cluster without rebuilding AMIs. This approach downloads the script from S3 during
instance launch using user data.

## Prerequisites

Before you deploy your script using S3, complete these tasks:

- Create an S3 bucket with your CLI Filter Plugin Lua script
- Configure IAM instance profile with read access to the S3 bucket
- Set up S3 VPC Gateway endpoint for direct access without internet
- Prepare user-data script to download from S3

###### To deploy CLI Filter Plugin script using S3

1. Upload your `cli_filter.lua` script to your S3 bucket.
2. Configure your IAM instance profile with S3 read permissions for the bucket.
3. Add shell code to your launch template user-data to download the script:

```
aws s3 cp s3://my-bucket/cli_filter.lua /etc/aws/pcs/scheduler/slurm-24.11/cli_filter.lua
chmod 644 /etc/aws/pcs/scheduler/slurm-24.11/cli_filter.lua
```

4. Deploy compute node groups with your updated launch templates.
5. Test job submission to verify script functionality.

## Expected results

After you complete the S3 deployment:

- CLI Filter Plugin script is automatically downloaded to all instances during launch
- Script updates in S3 are reflected on newly launched instances
- Job submission policies are enforced consistently across the cluster

## Troubleshooting

**S3 access denied**

**Symptoms:** Instance launch fails or script not
downloaded.

**Likely cause:** Missing IAM permissions or S3 VPC
endpoint.

**Resolution:** Verify IAM instance profile has
`s3:GetObject` permission and S3 VPC endpoint is configured.
