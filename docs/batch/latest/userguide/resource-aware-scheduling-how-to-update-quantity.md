# Update the quantity of a

resource while it is in use by jobs

You can reset the total quantity of a resource to a new value, add to the total
quantity or subtract from it.

If the new total quantity you specify is greater than before, Batch schedules more
jobs accordingly. If the new total quantity is less than before and there are no
units of this resource in use, Batch just reduces the total (or available) quantity.
If there are units in use, Batch reduces the available quantity immediately and, as
jobs finish, Batch reduces the total (available) quantity so that it eventually
arrives at the new number.

**Console:**

1.  In the left navigation panel of the [AWS Batch console](https://console.aws.amazon.com/batch "https://console.aws.amazon.com/batch"),
    choose **Consumable resources**.
2.  Select either the **Replenishable** or **Non-replenishable**
    tab to view the resources of that type that you have created.
3.  For **Replenishable** resources:

        1. Choose the resource you want to update, then select **Actions**
         and choose **Set resources**, **Add resources**,
         or **Remove resources**.
        2. A pop-up window appears in which you can **Set total value**,
         **Add resources**, or **Remove resources** depending
         on which action you chose in the previous step. Enter the quantity you want to set
         as the new total value, you want to add to the total quantity or that you want to
         subtract from the total quantity, then select **Ok**.

    For **Non-replenishable** resources:

        1. Choose the resource you want to update, then select **Actions**
         and choose **Set resources**, **Add resources**,
         or **Remove resources**.
        2. A pop-up window appears in which you can **Set available value**,
         **Add resources**, or **Remove resources**
         depending on which action you chose in the previous step. Enter the quantity you
         want to set as the new available value, you want to add to the available quantity or
         that you want to subtract from the available quantity, then select
         **Ok**.

    **API:**

Use the [`UpdateConsumableResource` API](../APIReference/API_UpdateConsumableResource.md "../APIReference/API_UpdateConsumableResource.md") to set a new total quantity for the resource,
or to increase or reduce the total quantity.
