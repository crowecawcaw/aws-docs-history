

# Create consumable resources
<a name="resource-aware-scheduling-how-to-create"></a>

You must first create the consumable resources that represent the non-CE resources that are consumed when a job is running and are only available in limited quantities. Each consumable resource has a: 
+ resource name (`consumableResourceName`) that must be unique at the account level.
+ (optional) resource type (`resourceType`) that indicates whether the resource is available to be re-used after a job completes. This can be one of:
  + `REPLENISHABLE` (default)
  + `NON_REPLENISHABLE`
+ total quantity (`totalQuantity`) that specifies the total amount of the consumable resource available.

The maximum number of consumable resources per account is 50k.

**Console:**

1. In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch), choose **Consumable resources**.

1. Choose **Create consumable resource**.

1. Enter a unique **Resource name**, the **Total resource quantity**, and select whether the **Type of resource** is **Replenishable** or **Non-replenishable**.

1. Choose **Create consumable resource**.

**API:**

Use the [`CreateConsumableResource` API](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateConsumableResource.html) to define the resources you want.