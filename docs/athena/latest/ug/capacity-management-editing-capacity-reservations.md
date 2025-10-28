# Edit capacity

reservations

After you create a capacity reservation, you can adjust its number of DPUs and add
or remove its custom tags.

###### To edit a capacity reservation

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.
3. Choose **Administration**, **Capacity
   reservations**.
4. In the list of capacity reservations, do one of the following:
   - Select the button next to the reservation, and then choose
     **Edit**.
   - Choose the reservation link, and then choose
     **Edit**.

5. For **DPU**, choose or enter the number of data
   processing units that you want in increments of 4. The minimum number of
   DPUs that you can have is 24. For more information, see [Understand DPUs](capacity-management.md#capacity-management-understanding-dpus "capacity-management.md#capacity-management-understanding-dpus").

###### Note

    * You can add DPUs to an existing capacity reservation at any time.
     However, you cannot decrease the number of DPUs until 1 hour after you
     create the reservation or add DPUs to it.
    * When you request to decrease DPUs while queries are running,
     the system waits for the queries to complete before updating the
     capacity reservation with the new target DPUs.

6. (Optional) For **Tags**, choose
   **Remove** to remove a tag, or choose **Add new
   tag** to add a new tag.
7. Choose **Submit**. The details page for the reservation
   shows the updated configuration.
