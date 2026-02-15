# View a job queue in AWS Batch

After you create a job queue and submit the jobs, it is important to be able to monitor its
progress. You can use the **Job details** page to review, manage, and monitor
your job queue.

## View job queue information

From the AWS Batch console, select **Job queues** in navigation pane and
choose your desired job queue to view its details. On this page, you can review and manage your
job queue and see additional information about the queue’s operations, such as the job queue
snapshot, job state limits, environment order, tags, and the job queue’s JSON code.

### Job queue details

This section provides an overview and maintenance options for the job queue. It is
important to note that you can find the Amazon Resource Name (ARN) in this section.

To find this information through the AWS Command Line Interface, use the [`DescribeJobQueues`](../APIReference/API_DescribeJobQueues.md "../APIReference/API_DescribeJobQueues.md") operation along with the job queue name, or the
corresponding ARN.

### Active shares

For job queues using fair-share scheduling, AWS Batch provides visibility
into how different share identifiers consume capacity. This information helps you
understand resource distribution and identify shares that may need
adjustment.

###### Note

The **Active shares** tab is only present when the job queue's **Scheduling algorithm** is Fair-share.

The top 20 active shares section shows share identifiers whose scheduled,
starting, and running jobs. This view includes:

- **Share identifier name** - The unique
  identifier for the share.

Share identifiers are labels that group jobs for fair-share scheduling. When you
submit jobs with the same share identifier, AWS Batch treats them as part of the same
workload for resource allocation purposes. Share identifiers help ensure equitable
distribution of compute capacity across different teams, projects, or workload
types. For more information, see [Use share identifiers to identify workloads](share-identifiers.md "share-identifiers.md").

- **Capacity utilization** - The amount of resources the job
  is configured to use. This is measured in `instances`, `cpu`, or
  `vCPU` depending on the environment.
- **View jobs action** - A link to see
  all jobs for that share.

You can view this information in both list and chart formats:

- **List view** - Tabular display with
  exact capacity numbers
- **Chart view** - Visual bar chart showing
  relative utilization

### Job queue snapshot

This section provides a static list of the first 100 `RUNNABLE` jobs that are in
queue. You can use the search field to narrow the list by searching for information from any
column in the results section. The jobs in the snapshot results area are sorted according to the
job queue’s run strategy. For first-in-first-out (FIFO) job queues, the ordering of the jobs is
based on the submission time. For [fair-share
scheduling](fair-share-scheduling.md "fair-share-scheduling.md") job queues, the ordering of the jobs is based on the job priority and share
usage. The **Capacity required** field show the amount of resources the job is configured to use.

Because the results are a snapshot of the job queue, the results list doesn’t automatically
update. To update the list, choose the refresh at the top of the section. Choose the job’s name
hyperlink to navigate to **Job details** and view the job’s status and other
related information.

To find this information through the AWS CLI, use the [`GetJobQueueSnapshot`](../APIReference/API_GetJobQueueSnapshot.md "../APIReference/API_GetJobQueueSnapshot.md") operation along with the job queue name or the
corresponding ARN.

```
aws batch get-job-queue-snapshot --job-queue my-sm-training-fifo-jq
```

### Job state limits

Use this tab to review configuration information about the amount of time that a job can
remain in a `RUNNABLE` state before it’s canceled.

To find this information through the AWS CLI, use the [`DescribeJobQueues`](../APIReference/API_DescribeJobQueues.md "../APIReference/API_DescribeJobQueues.md") operation along with the job queue name or the
corresponding ARN.

### Environment order

If your job queue runs in multiple environments, this tab provides their order and an
overview.

To find this information through the AWS CLI, use the [`DescribeJobQueues`](../APIReference/API_DescribeJobQueues.md "../APIReference/API_DescribeJobQueues.md") operation along with the job queue name or the
corresponding ARN.

### Tags

Use this tab to review and manage tags that are associated to this job queue.

### JSON

Use this tab to copy the JSON code that’s associated with this job queue. You can then
reuse the JSON for AWS CloudFormation templates and AWS CLI scripts.
