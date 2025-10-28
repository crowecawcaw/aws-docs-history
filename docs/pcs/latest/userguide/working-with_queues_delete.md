# Deleting a queue in AWS PCS

This topic provides an overview of how to delete an queue in AWS PCS.

## Considerations when deleting a

queue

- If there are jobs running in the queue, they will be terminated by the scheduler when the
  queue is deleted. Pending jobs in the queue will be canceled. Consider waiting for jobs in the
  queue to finish or manually stop/cancel them using the scheduler’s native commands (such as
  `scancel` for Slurm).

## Delete the queue

You can use the AWS Management Console or AWS CLI to delete a queue.

AWS Management Console

###### To delete a queue

1. Open the [AWS PCS
   console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Select the cluster of the queue.
3. Navigate to **Queues** and select the queue to delete.
4. Choose **Delete**.
5. The **Status** field shows `Deleting`. It can take several
   minutes to complete.

###### Note

You can use commands native to your scheduler to confirm that the queue is deleted. For
example, use `sinfo` or `squeue` for Slurm.

AWS CLI

###### To delete a queue

- Use the following command to delete a queue, with these replacements:
  - Replace `region-code` with the AWS Region your cluster is
    in.
  - Replace `my-queue` with the name or ID of your queue.
  - Replace `my-cluster` with the name or ID of your cluster.

```
aws pcs delete-queue --region `region-code` \
       --queue-identifier `my-queue` \
       --cluster-identifier `my-cluster`
```

It can take several minutes to delete the queue.

###### Note

You can use commands native to your scheduler to confirm that the queue is deleted. For
example, use `sinfo` or `squeue` for Slurm.
