# Find the jobs that require a

specific consumable resource

Batch lets you retrieve a list of jobs that require a specific consumable resource.

**Console:**

1. In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch "https://console.aws.amazon.com/batch"),
   choose **Consumable resources**.
2. In the list, select the name of the consumable resource. The details page for that resource
   opens.
3. Under **Search jobs**, enter any filters you want to apply to the list of
   jobs. You can filter by the **Job name** ('equals', 'starts with'), the
   **Date range** (when the job was created), and by **Additional
   criteria** ('job queue', 'job definition', 'shared job identifier'). For each
   type of filter you want to apply, select from the available options in the drop-down list
   and enter any additional information requested.

Choose **Search**. 4. A (filtered) list of jobs that require the consumable resource is displayed, including
the job's name, status, number of requested units of the consumable resource, other needed
consumable resources, and so on. Using this list, you can select one or more jobs to
**Cancel** or **Terminate**. You can also select a job's
name to open that job's detail page. 5. Under **Search jobs** you can now **Refresh results** or
**Clear search** and start over.
**API:**

You can get a list of jobs that use a specific consumable resource with the [`ListJobsByConsumableResource`
API](../APIReference/API_ListJobsByConsumableResource.md "../APIReference/API_ListJobsByConsumableResource.md"). This API also lets you filter the job list query using the job status or the job name.
