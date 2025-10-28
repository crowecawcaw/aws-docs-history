# Create a queue to manage jobs in AWS PCS

You submit a job to a queue to run it. The job remains in the queue until AWS PCS schedules
it to run on a compute node group. Each queue is associated with one or more compute node groups,
which provide the necessary EC2 instances to do the processing.

In this step, you will create a queue that uses the compute node group to process jobs.

###### To create a queue

- Open the [AWS PCS console](https://console.aws.amazon.com/pcs "https://console.aws.amazon.com/pcs").
- Select the cluster named `get-started`.
- Navigate to **Compute node groups** and make sure the status of the
  `compute-1` group is **Active**.

###### Important

The status of the `compute-1` group must be **Active** before
you proceed to the next step.

- Navigate to **Queues** and choose **Create
  queue**.
  - In the **Queue configuration** section, provide the following
    values:
    - **Queue name** – Enter the following: `demo`
    - **Compute node groups** – Select the compute node group named
      `compute-1`.

- Choose **Create queue**.
  The **Status** field shows **Creating** while the queue is
  being created.

###### Important

Wait for the **Status** field to show **Active** before
proceeding to the next step in this tutorial.
