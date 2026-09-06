

# Cancel a capacity reservation
<a name="capacity-management-cancelling-a-capacity-reservation"></a>

If you no longer want to use a capacity reservation, you can cancel it. Queries that are still running in the workgroups that were using the reservation will be allowed to finish, but other queries in the workgroup will no longer use the reservation.

**Note**  
Cancelled capacity is not guaranteed to be re-reservable at a future date. Capacity cannot be transferred to another reservation, AWS account or AWS Region. 

**To cancel a capacity reservation**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. If the console navigation pane is not visible, choose the expansion menu on the left.

1. Choose **Administration**, **Capacity reservations**.

1. In the list of capacity reservations, do one of the following:
   + Select the button next to the reservation, and then choose **Cancel**.
   + Choose the reservation link, and then choose **Cancel capacity reservation**.

1. At the **Cancel capacity reservation?** prompt, enter **cancel**, and then choose **Cancel capacity reservation**.

   The reservation's status changes to **Cancelling**, and a progress banner informs you that the cancellation is in progress.

   When the cancellation is complete, the capacity reservation remains, but its status shows as **Cancelled**. The reservation will be deleted 45 days after cancellation. During the 45 days, you cannot re-purpose or reuse a reservation that has been cancelled, but you can refer to its tags and view it for historical reference.