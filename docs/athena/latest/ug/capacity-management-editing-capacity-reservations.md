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
   processing units that you want. For more information, see [Understand DPUs](capacity-management.md#capacity-management-understanding-dpus "capacity-management.md#capacity-management-understanding-dpus").

###### Note

    * You can request to add DPUs to an active capacity reservation at any time.
    * You can request to decrease DPUs from an active capacity reservation when
     1 minute has passed since the reservation became active or when DPUs were last added.
    * When you request to decrease DPUs, Athena prioritizes removing idle DPUs over
     active DPUs. If queries are consuming DPUs that are marked for removal, Athena waits
     for queries to complete before removing the DPUs.

6. (Optional) For **Tags**, choose
   **Remove** to remove a tag, or choose **Add new
   tag** to add a new tag.
7. Choose **Submit**. The details page for the reservation
   shows the updated configuration.
