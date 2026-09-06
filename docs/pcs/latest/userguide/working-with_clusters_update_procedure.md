

# Update an AWS PCS cluster
<a name="working-with_clusters_update_procedure"></a>

Use these steps to modify scheduler settings, accounting configuration, and Slurm custom settings on your cluster. For more information, see [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md).

## Prerequisites
<a name="update-cluster-procedure-prerequisites"></a>
+ Cluster must be in `ACTIVE`, `UPDATE_FAILED`, or `SUSPENDED` state
+ All associated resources (Queues, Compute Node Groups) must be in `ACTIVE` state
+ No other update operations can be in progress

## Procedure
<a name="update-cluster-procedure-steps"></a>

------
#### [ AWS Management Console ]

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

1. In the navigation pane, choose **Clusters**.

1. Select the cluster to update.

1. Choose **Edit**.

1. On the Edit cluster page, modify the desired settings:
   + Under **Cluster details**, select a new scheduler version from the **Scheduler** dropdown. For more information, see [Updating the scheduler version of a cluster in AWS PCS](working-with_clusters_version_update.md).
   + Under **Scheduler configuration**, update **Scale-down idle time** to control how long dynamic instances remain idle before automatic termination.
   + Modify **Prolog**, **Epilog**, and **Select-type parameters** settings as needed.
   + Enable, disable, or configure retention time for **managed accounting**.
   + Under **Additional scheduler settings**, add, edit, or remove **Slurm custom settings**. For more information about supported parameters, see [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md).
**Note**  
Fields that cannot be edited display as read-only and show their current values.

1. Choose **Update** to submit the changes.

1. Monitor the cluster status, which shows as "Updating" during the process. The status changes when the update completes successfully.

------
#### [ AWS CLI ]

1. Open a terminal or command prompt.

1. Verify the cluster status using the following command:

   ```
   aws pcs get-cluster --cluster-identifier {{my-cluster}}
   ```

1. Submit an update request using one of the following examples:
   + To enable managed accounting:

     ```
     aws pcs update-cluster --cluster-identifier {{my-cluster}} \
     --slurm-configuration 'accounting={mode=STANDARD}'
     ```
   + To update a Slurm Prolog setting:

     ```
     aws pcs update-cluster --cluster-identifier {{my-cluster}} \
     --slurm-configuration \
     'SlurmCustomSettings=[{parameterName=Prolog,parameterValue="/path/to/prolog.sh"}]'
     ```
   + To update scale-down idle time:

     ```
     aws pcs update-cluster --cluster-identifier {{my-cluster}} \
     --slurm-configuration 'scaleDownIdleTimeInSeconds={{300}}'
     ```
   + To update the scheduler version:

     ```
     aws pcs update-cluster --cluster-identifier {{my-cluster}} \
     --scheduler version={{25.11}}
     ```

1. Monitor update progress by checking cluster status:

   ```
   aws pcs get-cluster --cluster-identifier {{my-cluster}}
   ```

After a successful update request, the command returns the Cluster object with all changes. The cluster status changes from `UPDATING` to `ACTIVE` when complete.

------