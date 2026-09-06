

# Delete a capacity reservation
<a name="capacity-management-deleting-a-capacity-reservation"></a>

If you want to remove all references to a cancelled capacity reservation, you can delete the reservation. A reservation must be cancelled before it can be deleted. A deleted reservation is immediately removed from your account and can no longer be referenced, including by its ARN.

**To delete a capacity reservation**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. If the console navigation pane is not visible, choose the expansion menu on the left.

1. Choose **Administration**, **Capacity reservations**.

1. In the list of capacity reservations, do one of the following:
   + Select the button next to the cancelled reservation, and then choose **Actions**, **Delete**.
   + Choose the reservation link, and then choose **Delete**.

1. At the **Delete capacity reservation?** prompt, choose **Delete**.

   A banner informs you that the capacity reservation has been successfully deleted. The deleted reservation no longer appears in the list of capacity reservations.