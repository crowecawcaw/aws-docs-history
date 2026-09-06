

# Specify the resources needed to run a job
<a name="resource-aware-scheduling-how-to-for-jobs"></a>

When you register a job you can specify the name of one or more resources you created (`consumableResource`) and the quantity of that resource each instance of the job requires (`quantity`).

Batch keeps track of the available units of each resource at any given moment. For each job in the job queue, the Batch scheduler ensures that your job runs only when the specified resource dependencies are available.

If a consumable resource for the job is not available when the job reaches the head of the queue, the job will wait in `RUNNABLE` state until all the required resources become available or the job state time limit is reached (see [View a job queue in AWS Batch](job_queue_viewing_status.md)). Once Batch has validated that all the resources are available, the job transitions to the `STARTING` state and then to `RUNNING`. Resources are locked once the job moves to `STARTING` and are then unlocked when the job moves to `SUCCEEDED` or `FAILED`.

You can also update the quantity of a resource needed for a specific job when you submit the job.

**Console:**

**To specify resources and their needed quantities when you define a job:**

1. Define a job using the job definition wizard from the [AWS Batch console](https://console.aws.amazon.com/batch) (**Job definitions** -> **Create**).

1. In the wizard's Step 4: **Configure containers**, under **Consumable resource**, select the **Name** of a required resource from the list. In the **Requested value** field, enter the quantity of this resource needed by an instance of this job, then choose **Add consumable resource**.

1. Repeat the previous step for all the consumable resources required by the job. You can specify up to 5 resources for each job you define.

1. You'll see a list of the consumable resources you have created after you complete the job definition wizard but before you choose **Create job definition**.

**To update needed quantities of resources when you submit a job:**

1. In the left navigation pane of the [AWS Batch console](https://console.aws.amazon.com/batch), choose **Jobs**, then choose **Submit new job**.

1. In the wizard's Step 2: **Configure overrides**, under **Consumable resource overrides**, enter a new **Requested value** for any consumable resource whose needed quantity you want to override for the job.

1. After you have completed all the overrides you want to make for this job, choose **Next** to continue to **Review and submit**.

**API:**

When you register a job with the [`RegisterJobDefinition` API](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html), use the `consumableResourceList` in the `consumableResourceProperties` portion of the request to specify the consumable resources required to run an instance of the job, and the quantity of each.

When you submit a job with the [`SubmitJob` API](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) you can override the list of consumable resources and the quantity of each using the `consumableResourcePropertiesOverride` portion of the request. Note that this only overrides the quantity of the resource needed by each instance of the job, not the total quantity available.