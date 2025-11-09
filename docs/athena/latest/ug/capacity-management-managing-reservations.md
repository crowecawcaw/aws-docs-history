# Manage reservations

You can view and manage your capacity reservations on the **Capacity
reservations** page. You can perform management tasks like adding or
reducing DPUs, modifying workgroup assignments, and tagging or cancelling
reservations.

###### To view and manage capacity reservations

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu on
   the left.
3. Choose **Administration**, **Capacity
   reservations**.
4. On the capacity reservations page, you can perform the following tasks:
   - To create a capacity reservation, choose **Create
     capacity reservation**.
   - Use the search box to filter reservations by name or number of
     DPUs.
   - Choose the status drop-down menu to filter by capacity reservation
     status (for example, **Active** or
     **Cancelled**). For information about reservation
     status, see [Understand
     reservation status](#capacity-management-understanding-reservation-status "#capacity-management-understanding-reservation-status").
   - To view details for a capacity reservation, choose the link for the
     reservation. The details page for the reservation includes options for
     [editing capacity](capacity-management-editing-capacity-reservations.md "capacity-management-editing-capacity-reservations.md"), [adding workgroups](capacity-management-adding-workgroups-to-a-reservation.md "capacity-management-adding-workgroups-to-a-reservation.md"), [removing workgroups](capacity-management-removing-a-workgroup-from-a-reservation.md "capacity-management-removing-a-workgroup-from-a-reservation.md"), and for [cancelling](capacity-management-cancelling-a-capacity-reservation.md "capacity-management-cancelling-a-capacity-reservation.md") the reservation.
   - To edit a reservation (for example, by adding or removing DPUs),
     select the button for the reservation, and then choose
     **Edit**.
   - To cancel a reservation, select the button for the reservation, and
     then choose **Cancel**.

## Understand

reservation status

The following table describes the possible status values for a capacity
reservation.

| Status             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pending**        | Athena is processing your capacity request. Capacity is not ready<br>to run queries.                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Active**         | Capacity is available to run queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Failed**         | Your request for capacity was not completed successfully. Note<br>that fulfillment of capacity requests is not guaranteed. Failed<br>reservations count towards your account DPU limits. To release the<br>usage, you must cancel the reservation.                                                                                                                                                                                                                                                 |
| **Update pending** | Athena is processing a change to the reservation. For example,<br>this status occurs after you edit the reservation to add or remove<br>DPUs.                                                                                                                                                                                                                                                                                                                                                      |
| **Cancelling**     | Athena is processing a request to cancel the reservation. Queries<br>that are still running in the workgroups that were using the<br>reservation are allowed to finish, but other queries in the<br>workgroup will use on-demand (non-provisioned) capacity.                                                                                                                                                                                                                                       |
| **Cancelled**      | The capacity reservation cancellation is complete. Cancelled<br>reservations remain in the console for 45 days. After 45 days,<br>Athena will delete the reservation. During the 45 days, you<br>cannot re-purpose or reuse the reservation, but you can refer to<br>its tags and view its details for historical reference.<br>Cancelled capacity is not guaranteed to be re-reservable at a<br>future date. Capacity cannot be transferred to another<br>reservation, AWS account or AWS Region. |

## Understand Active

DPUs and Target DPUs

In the list of capacity reservations in the Athena console, your reservation
displays two DPU values: **Active DPU** and **Target
DPU**.

- Active DPU – The number of DPUs that
  are available in your reservation to run queries. For example, if you
  request 100 DPUs, and your request is fulfilled, **Active
  DPU** displays **100**.
- Target DPU – The number of DPUs that
  your reservation is in the process of moving to. **Target
  DPU** displays a value different than **Active
  DPU** when a reservation is being created, or an increase or
  decrease in the number of DPUs is pending.

For example, after you submit a request to create a reservation with 24 DPUs, the
reservation **Status** will be **Pending**,
**Active DPU** will be **0**, and the
**Target DPU** will be **24**.

If you have a reservation with 100 DPUs, and edit your reservation to request an
increase of 20 DPUs, the **Status** will be **Update
pending**, **Active DPU** will be
**100**, and **Target DPU** will be
**120**.

If you have a reservation with 100 DPUs, and edit your reservation to request a
decrease of 20 DPUs, the **Status** will be **Update
pending**, **Active DPU** will be
**100**, and **Target DPU** will be
**80**.

During these transitions, Athena is actively working to acquire or reduce the
number of DPUs based on your request. When **Active DPU** becomes
equal to **Target DPU**, the target number has been reached and no
changes are pending.

To retrieve these values programmatically, you can call the [GetCapacityReservation](../APIReference/API_GetCapacityReservation.md "../APIReference/API_GetCapacityReservation.md") API action. The API refers to **Active
DPU** and **Target DPU** as `AllocatedDpus`
and `TargetDpus`.

###### Topics

- [Edit capacity
  reservations](capacity-management-editing-capacity-reservations.md "capacity-management-editing-capacity-reservations.md")
- [Add
  workgroups to a reservation](capacity-management-adding-workgroups-to-a-reservation.md "capacity-management-adding-workgroups-to-a-reservation.md")
- [Remove
  a workgroup from a reservation](capacity-management-removing-a-workgroup-from-a-reservation.md "capacity-management-removing-a-workgroup-from-a-reservation.md")
- [Cancel a
  capacity reservation](capacity-management-cancelling-a-capacity-reservation.md "capacity-management-cancelling-a-capacity-reservation.md")
- [Delete a
  capacity reservation](capacity-management-deleting-a-capacity-reservation.md "capacity-management-deleting-a-capacity-reservation.md")
