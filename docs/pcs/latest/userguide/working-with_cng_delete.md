# Deleting a compute node group in AWS PCS

This topic provides an overview of available options and describes what to consider when you delete an compute node group in AWS PCS.

## Considerations when deleting a

compute node group

Compute node groups define EC2 instances that are used to process jobs, provide interactive shell access, and other tasks. They are often associated with one or more AWS PCS queues. Before you delete a compute node group, consider the following:

- Any EC2 instances launched by the compute node group will be terminated. This will cancel jobs that are running on these instances, and terminate running interactive processes.
- You must disassociate the compute node group from all queues before you can delete it. For more information, see [Updating an AWS PCS queue](working-with_queues_update.md "working-with_queues_update.md").

## Delete the compute node group

You can use the AWS Management Console or AWS CLI to delete a compute node group.

AWS Management Console

###### To delete a compute node group

1. Open the [AWS PCS
   console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Select the cluster of the compute node group.
3. Navigate to **Compute node groups** and select the compute node group to delete.
4. Choose **Delete**.
5. The **Status** field shows `Deleting`. It can take several
   minutes to complete.

###### Note

You can use commands native to your scheduler to confirm that the compute node group is deleted. For
example, use `sinfo` or `squeue` for Slurm.

AWS CLI

###### To delete a compute node group

- Use the following command to delete a compute node group, with these replacements:
  - Replace `region-code` with the AWS Region your cluster is
    in.
  - Replace `my-node-group` with the name or ID of your compute node group.
  - Replace `my-cluster` with the name or ID of your cluster.

```
aws pcs delete-compute-node-group --region `region-code` \
       --compute-node-group-identifier `my-node-group` \
       --cluster-identifier `my-cluster`
```

It can take several minutes to delete the compute node group.

###### Note

You can use commands native to your scheduler to confirm that the compute node group is deleted. For
example, use `sinfo` or `squeue` for Slurm.
