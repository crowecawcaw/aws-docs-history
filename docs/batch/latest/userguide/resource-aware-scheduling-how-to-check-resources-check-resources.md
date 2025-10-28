# Check how many resources are

in-use and available

Batch lets you query the number of available resources (`availableQuantity`),
the number of resources in use (`inUseQuantity`), and the total resources
(`totalQuantity`) at a given moment.

Once a job goes to the `STARTING` state, the consumed resources will be subtracted
from the available quantity of that resource. If the resource is `REPLENISHABLE`, the
number of consumed resources will be added back to the available quantity as soon as the job has
moved to either the SUCCEEDED or FAILED state, and the total quantity will remain the same. If
the resource is `NON_REPLENISHABLE`, the number of consumed resources is subtracted
from both the total and available quantities and won't be added back whether the job moves to
the `SUCCEEDED` or `FAILED` state.

###### Note

This information may lag by up to 30 seconds.

**Console:**

1. In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch "https://console.aws.amazon.com/batch"),
   choose **Consumable resources**.
2. Select either the **Replenishable** or **Non-replenishable**
   tab to view the resources of that type that you have created.
3. For each **Replenishable** resource, the console displays the
   **Name**, the **Total** quantity of the resource, the
   number currently **In-use** and how many are still **Available**,
   along with a calculation of the **Utilization** (the number of resources
   in-use divided by the total quantity of that resource).

For each **Non-replenishable** resource, the console displays the
**Name**, the number currently **In-use** and how
many are still **Available**.
You can also view current information about consumable resources from a job detail page in
the console.

1. In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch "https://console.aws.amazon.com/batch"),
   choose **Jobs**, then select a job's name to open the details page
   for that job.
2. Information on both **Replenishable resources** and
   **Non-replenishable resources** are available to view if the job requires
   them. For both types, the console displays the resource's **Name**, the
   **Requested** quantity for the job, how many are still
   **Available**, the number currently **In-use**, the
   **Total** quantity of the resource, along with a calculation of the
   **Current utilization** (the number of resources in-use by the job
   divided by the total quantity of that resource).
   **API:**

Use the [`DescribeConsumableResource` API](../APIReference/API_DescribeConsumableResource.md "../APIReference/API_DescribeConsumableResource.md") which returns the following information:

```
{
   "availableQuantity": number,
   "consumableResourceArn": "string",
   "consumableResourceName": "string",
   "createdAt": number,
   "inUseQuantity": number,
   "resourceType": "string",
   "tags": {
      "string" : "string"
   },
   "totalQuantity": number
}
```

The [`ListConsumableResources` API](../APIReference/API_ListConsumableResources.md "../APIReference/API_ListConsumableResources.md") also reports the number of resources in use
(`inUseQuantity`) and the total number of resources currently available (`totalQuantity`)
as part of its listing of all the consumable resources you have created in your account. This
API also allows you filter the consumable resource list query based on the consumable resource name.
