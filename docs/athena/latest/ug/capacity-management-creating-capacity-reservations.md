# Create capacity

reservations

To get started, you create a capacity reservation that has the number of DPUs that you
require, and then assign one or more workgroups that will use that capacity for their
queries. You can adjust your capacity later as needed to provide more consistent
performance or better manage costs. For information about estimating your capacity
requirements, see [Determine capacity requirements](capacity-management-requirements.md "capacity-management-requirements.md").

###### Important

Requests for capacity are not guaranteed and can take up to 30 minutes to
complete.

###### To create a capacity reservation

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu on
   the left.
3. Choose **Administration**, **Capacity
   reservations**.
4. Choose **Create capacity reservation**.
5. On the **Create capacity reservation** page, for
   **Capacity reservation name**, enter name. The name must be
   unique, from 1 to 128 characters long, and use only the characters a-z, A-Z,
   0-9, \_(underscore), .(period) and -(hyphen).You cannot change the name after you
   create the reservation.
6. For **DPU**, choose or enter the number of data processing
   units (DPUs) that you want in increments of 4. For more information, see [Understand DPUs](capacity-management.md#capacity-management-understanding-dpus "capacity-management.md#capacity-management-understanding-dpus").
7. (Optional) Expand the **Tags** option, and then choose
   **Add new tag** to add one or more custom key/value pairs
   to associate with the capacity reservation resource. For more information, see
   [Tag Athena resources](tags.md "tags.md").
8. Choose **Review**.
9. At the **Confirm create capacity reservation** prompt,
   confirm the number of DPUs, AWS Region, and other information. If you accept,
   choose **Submit**.

On the details page, your capacity reservation's **Status**
shows as **Pending**. When your reservation capacity is
available to run queries, its status shows as
**Active**.
At this point, you are ready to add one or more workgroups to your reservation. For
steps, see [Add
workgroups to a reservation](capacity-management-adding-workgroups-to-a-reservation.md "capacity-management-adding-workgroups-to-a-reservation.md").
