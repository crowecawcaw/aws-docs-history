

# Updating an AWS PCS queue
<a name="working-with_queues_update"></a>

This topic provides an overview of available options and describes what to consider when you update an AWS PCS queue. For information about Slurm custom settings, see [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md).

## Considerations when updating an AWS PCS queue
<a name="working-with_queues_update_considerations"></a>

Queue updates will not impact running jobs but the cluster may not be able to accept new jobs while the queue is being updated.

## To update an AWS PCS queue
<a name="working-with_queues_update_update"></a>

You can use the AWS Management Console or AWS CLI to update a queue.

------
#### [ AWS Management Console ]

**To update a queue**

1. Open the AWS PCS console at `https://console.aws.amazon.com/pcs/home#/clusters`

1. Select the cluster where you wish to update a queue.

1. Navigate to **Queues**, go to the queue wish to update, then select **Edit**.

1. In the queue configuration section, update any of the following values:
   +  **Node groups** – Add or remove compute node groups from association with the queue. 
   +  **Additional scheduler settings** – Add, modify, or remove custom Slurm settings for the queue. For more information, see [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md). 
   +  **Tags** – Add or remove tags for the queue. 

1. Choose **Update**. The **Status** field will show *Updating* while changes are being applied.
**Important**  
Queue updates can take several minutes.

------
#### [ AWS CLI ]

**To update a queue**

1. Update your queue with the command that follows. Before running the command, make the following replacements:

   1. Replace {{region-code}} with the AWS Region that you want to create your cluster in.

   1. Replace {{my-queue}} with the name or `computeNodeGroupId` for your queue.

   1. Replace {{my-cluster}} with the name or `clusterId` of your cluster.

   1.  To change compute node group associations, provide an updated list for `--compute-node-group-configurations`. 

      1.  For example, to add a second compute node group `computeNodeGroupExampleID2`: 

        ```
        --compute-node-group-configurations computeNodeGroupId=computeNodeGroupExampleID1,computeNodeGroupId=computeNodeGroupExampleID2
        ```

   ```
   aws pcs update-queue --region {{region-code}} \
       --queue-identifier {{my-queue}} \
       --cluster-identifier {{my-cluster}} \
       --compute-node-group-configurations \
       computeNodeGroupId={{computeNodeGroupExampleID1}}
   ```  
**Example – Updating a queue with custom Slurm settings**  

   ```
   aws pcs update-queue --region {{region-code}} \
       --queue-identifier {{my-queue}} \
       --cluster-identifier {{my-cluster}} \
       --slurm-configuration \
       'slurmCustomSettings=[{parameterName=Default,parameterValue=YES}]'
   ```

   For more information, see [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md).

1. It can take several minutes to update the queue. You can query the status of your queue with the following command. You won't be able to submit jobs to the queue until its status reaches `ACTIVE`.

   ```
   aws pcs get-queue --region {{region-code}} \
       --cluster-identifier {{my-cluster}} \ 
       --queue-identifier {{my-queue}}
   ```

------

**Recommended next steps**
+ Submit a job to your updated queue.