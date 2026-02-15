# Creating a queue in AWS PCS

This topic provides an overview of available options and describes what to consider when you
create a queue in AWS PCS.

###### Note

You can configure custom Slurm settings on queues to implement partition-specific scheduling policies and resource management. For more information, see [Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md "slurm-custom-settings.md").

## Prerequisites

- An AWS PCS cluster - queues can only be created in association with a specific AWS PCS
  cluster.
- One or more AWS PCS compute node groups - a queue must be associated with at least one AWS PCS
  compute node group.

## To create a queue in AWS PCS

You can create a queue using the AWS Management Console or the AWS CLI.

AWS Management Console

###### To create a queue using the console

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Select the cluster for the queue. Navigate to
   **Queues** and choose **Create queue**.
3. In the **Queue configuration** section, provide the following
   values:
   1. **Queue name** – A name for your queue. The name can contain
      only alphanumeric characters (case-sensitive) and hyphens. It must start with an
      alphabetic character and can't be longer than 25 characters. The name must be unique
      within the cluster.
   2. **Compute node groups** – Select 1 or more compute node
      groups to service this queue. A compute node group can be associated with more than 1
      queue.

4. (Optional) In the **Additional scheduler settings** section,
   you can add parameter name and value pairs to configure additional Slurm settings. For a complete list of supported parameters, see [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md "slurm-custom-settings-queue.md").
5. (Optional) Under **Tags**, add any tags to your AWS PCS queue
6. Choose **Create queue**. The **Status** field will show
   **Creating** while AWS PCS creates the queue. Queue creation can take
   several minutes.

###### Recommended next step

- Submit a job to your new queue.

AWS CLI

###### To create a queue using AWS CLI

Use the following command to create your queue. Make the
following replacements:

1. Replace `region-code` with the AWS Region of the cluster.
   For example, `us-east-1`.
2. Replace `my-queue` with the name for your queue. The name can
   contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an
   alphabetic character and can't be longer than 25 characters. The name must be unique within
   the cluster.
3. Replace `my-cluster` with the name or ID of your
   cluster.
4. Replace `compute-node-group-id`
   with the ID of the compute node group to service the queue. For example, `pcs_abcdef12345`.

###### Note

When you create a queue, you must provide the ID of the compute node group and not its name.

```
aws pcs create-queue --region `region-code` \
    --queue-name `my-queue` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-configurations \
    computeNodeGroupId=`compute-node-group-id`
```

###### Example– Creating a queue with custom Slurm settings

```
aws pcs create-queue --region `region-code` \
    --queue-name `my-queue` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-configurations \
    computeNodeGroupId=`compute-node-group-id` \
    --slurm-configuration \
    'slurmCustomSettings=[{parameterName=Default,parameterValue=YES}]'
```

For more information, see [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md "slurm-custom-settings-queue.md").

It can take several minutes to create the queue. You can query the status of your queue
with the following command. You won’t be able to submit jobs to the queue until its status
reaches `ACTIVE`.

```
aws pcs get-queue --region `region-code` \
    --cluster-identifier `my-cluster` \
    --queue-identifier `my-queue`
```

###### Recommended next step

- Submit a job to your new queue
