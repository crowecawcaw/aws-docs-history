

# Configure a Slurm Job Submit Plugin on an AWS PCS cluster

Configure a Job Submit Plugin when you create a new AWS PCS cluster. You can enable, update, or disable a Job Submit Plugin on an existing cluster using the Update API or console without recreating the cluster.

## Prerequisites
<a name="slurm-job-submit-plugins-configure-prerequisites"></a>

Before you configure a Job Submit Plugin, complete these tasks:
+ Verify you are using Slurm version 25.11 or later.
+ Write and test a Starlark script. For more information, see [Write a Starlark Job Submit Plugin script for AWS PCS](slurm-job-submit-plugins-scripts.md).
+ Upload your script to an Amazon S3 bucket.
+ Verify that the IAM identity that creates or updates the cluster can read the script. For more information, see [Minimum permissions to use Job Submit Plugins](security-min-permissions.md#security-min-permissions_job-submit-plugins).

## Enable a Job Submit Plugin on a new cluster
<a name="slurm-job-submit-plugins-configure-create"></a>

You can enable a Job Submit Plugin when you create a cluster. For more information, see [Creating a cluster in AWS PCS](working-with_clusters_create.md).

------
#### [ AWS PCS console ]

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/).

1. In the navigation pane, choose **Clusters**.

1. Choose **Create cluster**.

1. For **Scheduler version**, choose Slurm 25.11 or later.

1. Under **Scheduler configuration**, turn on **Enable job submit plugin**, and then do the following:
   + For **Name**, enter a name for the plugin.
   + For **Job submit Starlark script location**, enter the Amazon S3 URI of your script.
   + (Optional) For **S3 version ID**, enter the version of the script to use.
   + (Optional) For **Checksum**, enter the SHA-256 checksum of the script.

1. Complete the remaining cluster configuration and choose **Create cluster**.

------
#### [ AWS PCS API ]

Provide the `jobSubmitPlugins` configuration in your call to the `CreateCluster` API action. For more information, see [CreateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html) in the *AWS PCS API Reference*.

The following example uses the AWS CLI to call the `CreateCluster` API action with a Job Submit Plugin.

```bash
aws pcs create-cluster --cluster-name {{cluster-name}} \
--scheduler type=SLURM,version=25.11 \
--size SMALL \
--networking subnetIds={{subnet-id}},securityGroupIds={{security-group-id}} \
--slurm-configuration '{
  "jobSubmitPlugins": [
    {
      "name": "{{site-policy}}",
      "type": "STARLARK",
      "scriptSource": {
        "scriptLocation": "s3://{{amzn-s3-demo-bucket}}/{{policy.star}}"
      }
    }
  ]
}'
```

------

## Enable, update, or disable a Job Submit Plugin on an existing cluster
<a name="slurm-job-submit-plugins-configure-update"></a>

You can enable, update, or disable a Job Submit Plugin on an existing cluster without recreating the cluster. For more information, see [Updating a cluster in AWS PCS](working-with_clusters_update.md).

------
#### [ AWS PCS console ]

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/).

1. In the navigation pane, choose **Clusters**.

1. Select the cluster to update.

1. Choose **Edit**.

1. On the **Edit cluster** page, under **Scheduler configuration**:
   + To enable a Job Submit Plugin: Turn on **Enable job submit plugin**, and enter the **Name** and **Job submit Starlark script location**. Optionally, enter the **S3 version ID** and **Checksum**.
   + To update the script: Change the **Job submit Starlark script location**, **S3 version ID**, or **Checksum**.
   + To disable the Job Submit Plugin: Turn off **Enable job submit plugin**.

1. Choose **Update cluster** to submit the changes.

------
#### [ AWS PCS API ]

Use the `UpdateCluster` API action to enable, update, or disable a Job Submit Plugin. For more information, see [UpdateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateCluster.html) in the *AWS PCS API Reference*.

To enable a Job Submit Plugin or update its script on an existing cluster:

```bash
aws pcs update-cluster --cluster-identifier {{my-cluster}} \
--slurm-configuration '{
  "jobSubmitPlugins": [
    {
      "name": "{{site-policy}}",
      "type": "STARLARK",
      "scriptSource": {
        "scriptLocation": "s3://{{amzn-s3-demo-bucket}}/{{policy-v2.star}}"
      }
    }
  ]
}'
```

To disable a Job Submit Plugin on an existing cluster:

```bash
aws pcs update-cluster --cluster-identifier {{my-cluster}} \
--slurm-configuration '{"jobSubmitPlugins": []}'
```

------

**Important**  
AWS PCS downloads the script again only when a value in `jobSubmitPlugins` changes. If you overwrite the script at the same Amazon S3 location, also change the `s3VersionId` or `checksum`, or upload the script to a new key.

## Expected results
<a name="slurm-job-submit-plugins-configure-results"></a>

After you complete the configuration:
+ Your cluster runs with the Job Submit Plugin turned on
+ Job submissions and modifications trigger your custom logic on the Slurm controller
+ Non-compliant jobs are rejected with your custom error messages
+ Compliant jobs proceed normally through the Slurm scheduler

## Troubleshooting
<a name="slurm-job-submit-plugins-configure-troubleshooting"></a>

**Job Submit Plugin script can't be read**  
**Symptoms:** Cluster creation or update fails with an error about the script.  
**Likely cause:** Incorrect Amazon S3 URI, or the IAM identity can't read the script.  
**Resolution:** Verify the script exists at the Amazon S3 URI and the identity has the required permissions.

**Jobs are rejected unexpectedly**  
**Symptoms:** Job submissions fail with `Unspecified error`.  
**Likely cause:** The script has an error or exceeded a limit.  
**Resolution:** Check the `job_submit/json` entries in the Slurm controller log. For more information, see [Troubleshooting Slurm Job Submit Plugin issues in AWS PCS](slurm-job-submit-plugins-troubleshooting.md).