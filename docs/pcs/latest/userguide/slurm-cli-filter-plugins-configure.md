# Configure Slurm CLI Filter Plugins on an

AWS PCS cluster

Configure CLI Filter Plugins when you create a new AWS PCS cluster. You can enable or disable CLI Filter Plugins on existing clusters using the Update API or console without recreating the cluster.

## Prerequisites

Before you configure CLI Filter Plugins, complete these tasks:

- Write and test a Lua script that implements CLI Filter Plugin API
- Name your Lua script exactly `cli_filter.lua`
- Choose a method to deploy your script to all cluster instances (AMI, S3, or file
  system)
- Verify you are using Slurm version 24.11 or later

## Enable CLI Filter Plugins on a new cluster

AWS PCS console

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/ "https://console.aws.amazon.com/pcs/").
2. In the navigation pane, choose **Clusters**.
3. Choose **Create cluster**.
4. Select a valid version of Slurm (version 24.11 or later).
5. Under **Scheduler settings**, expand **Additional scheduler settings**.
6. Add a new Slurm custom setting with **Parameter name** set to `CliFilterPlugins` and **Parameter value** set to `cli_filter/lua`.
7. Complete the remaining cluster configuration and choose **Create cluster**.

AWS PCS API
Provide the `slurmCustomSettings` configuration in your call to the
`CreateCluster` API action. Set the `parameterName` to
`CliFilterPlugins` and `parameterValue` to
`cli_filter/lua`. For more information, see [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")
in the _AWS PCS API Reference_.

The following example uses the AWS CLI to call
the `CreateCluster` API action. The custom setting
`CliFilterPlugins=cli_filter/lua` enables CLI Filter Plugins.

```
aws pcs create-cluster --cluster-name `cluster-name` \
--scheduler type=SLURM,version=24.11 \
--size SMALL \
--networking subnetIds=`cluster-subnet-id`,securityGroupIds=`cluster-security-group-id` \
--slurm-configuration \
'slurmCustomSettings=[{parameterName=CliFilterPlugins,parameterValue="cli_filter/lua"}]'
```

## Deploy CLI Filter Plugin scripts

###### To deploy CLI Filter Plugin scripts to your cluster

1. Ensure all AMIs used in compute node groups have Slurm installed via the AWS PCS Slurm
   installer.

###### Note

If you use the AWS PCS Sample AMI for all compute node groups, skip this step. Slurm is
already installed. 2. Deploy your `cli_filter.lua` script to
`/etc/aws/pcs/scheduler/slurm-<version>/cli_filter.lua` on all
instances in the cluster.

For example, for Slurm version 24.11:

```
/etc/aws/pcs/scheduler/slurm-24.11/cli_filter.lua
```

3. Launch all login and compute nodes using your prepared AMIs.
4. Test job submission to verify CLI Filter Plugin executes correctly.

## Enable or disable CLI Filter Plugins on existing clusters

You can enable or disable CLI Filter Plugins on existing clusters without rebuilding your infrastructure. For more information, see [Updating a cluster in AWS PCS](working-with_clusters_update.md "working-with_clusters_update.md").

AWS PCS console

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/ "https://console.aws.amazon.com/pcs/").
2. In the navigation pane, choose **Clusters**.
3. Select the cluster to update.
4. Choose **Edit** action.
5. On the Edit cluster page, under **Additional scheduler settings**:
   - To enable CLI Filter Plugins: Add a new Slurm custom setting with **Parameter name** set to `CliFilterPlugins` and **Parameter value** set to `cli_filter/lua`.
   - To disable CLI Filter Plugins: Remove the existing `CliFilterPlugins` setting.

6. Choose **Update cluster** to submit the changes.
7. Monitor the cluster status, which shows as "Updating" during the process and "Active" when the update is complete.

AWS PCS API
Use the `UpdateCluster` API action to enable or disable CLI Filter Plugins. For more information, see [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") in the _AWS PCS API Reference_.

To enable CLI Filter Plugins on an existing cluster:

```
aws pcs update-cluster --cluster-identifier `my-cluster` \
--slurm-configuration \
'slurmCustomSettings=[{parameterName=CliFilterPlugins,parameterValue="cli_filter/lua"}]'
```

To disable CLI Filter Plugins on an existing cluster:

```
aws pcs update-cluster --cluster-identifier `my-cluster` \
--slurm-configuration \
'slurmCustomSettings=[]'
```

## Expected results

After you complete the configuration:

- Your cluster is created with CLI Filter Plugin turned on
- Job submissions trigger your custom validation logic before reaching the Slurm
  controller
- Non-compliant jobs are rejected with your custom error messages
- Compliant jobs proceed normally through the Slurm scheduler

## Troubleshooting

**CLI Filter Plugin script missing on any node**

**Symptoms:** Job submission fails immediately with plugin
loading error.

**Likely cause:** Script not deployed to all instances or
incorrect file path or name.

**Resolution:** Verify script exists at correct path on all
login and compute nodes with exact filename `cli_filter.lua`.

**Invalid CLI Filter Plugin configuration**

**Symptoms:** Cluster creation fails with validation
error.

**Likely cause:**
`CliFilterPlugins` parameter not set to `cli_filter/lua` format.

**Resolution:** Use exact parameter value
`cli_filter/lua` in `slurmCustomSettings`.
