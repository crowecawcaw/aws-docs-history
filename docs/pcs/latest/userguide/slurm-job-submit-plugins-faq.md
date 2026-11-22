

# Frequently asked questions about Slurm Job Submit Plugins in AWS PCS

Review these frequently asked questions about Job Submit Plugins.

**What is the difference between Job Submit Plugin and CLI Filter Plugin?**  
Job Submit Plugin runs server-side on the Slurm controller after job submission, while CLI Filter Plugin runs client-side on login and compute nodes before job submission reaches the controller. Job Submit Plugin can't be bypassed by users but can affect cluster performance, while CLI Filter Plugin can be bypassed by users but doesn't run on the controller. For more information about CLI Filter Plugins, see [Use Slurm CLI Filter Plugins to customize job submission in AWS PCS](slurm-cli-filter-plugins.md).

**Can I use Job Submit Plugin for security enforcement?**  
Yes. The script runs on the Slurm controller, so users can't bypass it.

**Can I use a Lua or C Job Submit Plugin?**  
No. Only Starlark scripts are supported in AWS PCS. To use an existing Lua script, translate it to Starlark. For more information, see [Translate a Lua Job Submit Plugin script to Starlark for AWS PCS](slurm-job-submit-plugins-translate.md).

**Do I need to deploy the script to my login and compute nodes?**  
No. AWS PCS downloads the script from Amazon S3 and installs it on the Slurm controller when you create or update the cluster.

**Can I modify the Job Submit Plugin script on a live cluster?**  
Yes. Upload the new script and update the cluster with a new script location, `s3VersionId`, or `checksum`. If you overwrite the script at the same Amazon S3 location without changing these values, the cluster keeps using the previous script.

**Can I use more than one Job Submit Plugin on a cluster?**  
No. You can configure one Job Submit Plugin on a cluster. The plugin applies to all queues in the cluster.

**What happens if my script fails?**  
Slurm rejects the job. A script that fails for every job rejects all jobs on the cluster, so test your script on a non-production cluster before you deploy it.

**Can the Amazon S3 bucket be in a different AWS account?**  
Yes, if the bucket policy grants the IAM identity that creates or updates the cluster permission to read the script.

**Can I turn Job Submit Plugin on or off on an existing cluster?**  
Yes, you can enable or disable Job Submit Plugin on existing clusters using the Update API or console without recreating the cluster.