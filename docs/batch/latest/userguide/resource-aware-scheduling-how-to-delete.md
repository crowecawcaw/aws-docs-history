# Delete a consumable resource

You can delete a consumable resource at any time, even when the jobs that require
the resource are still running. Once a consumable resource is deleted, there may be
a gap between the time the delete command is received and the job scheduler honors
the delete, so it's possible jobs that consume the resource may be scheduled right
after the delete call. If the deleted consumable resource has resource type
(`resourceType`) `REPLENISHABLE`, this will be ignored when
the jobs complete. If you delete a consumable resource and re-create it with the
same name, it is considered to be the same resource and it can be used by
`RUNNABLE` jobs.

**Console:**

1. In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch "https://console.aws.amazon.com/batch"),
   choose **Consumable resources**.
2. Select either the **Replenishable** or **Non-replenishable**
   tab to view the resources of that type that you have created.
3. Select each resource you want to delete, then choose **Delete**. A
   pop-up window **Delete consumable resource** appears. To confirm the
   deletion, choose **Delete**.
   You can also delete a consumable resource from its detail page in the console.

4. In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch "https://console.aws.amazon.com/batch"),
   choose **Consumable resources**.
5. Select either the **Replenishable** or **Non-replenishable**
   tab to view the resources of that type that you have created.
6. Choose the name of the resource you want to delete. The details page of the consumable
   resource appears. Choose **Delete**. A pop-up window **Delete
   consumable resource** appears. To confirm the deletion, choose
   **Delete**.
   **API:**

Use the [`DeleteConsumableResource` API](../APIReference/API_DeleteConsumableResource.md "../APIReference/API_DeleteConsumableResource.md") to delete a consumable
resource.
