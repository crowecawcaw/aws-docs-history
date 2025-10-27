# Associate a queue and fleet

To process jobs, you must associate a queue with a fleet. You can associate a single
fleet with multiple queues and a single queue with multiple fleets. When you associate a
fleet with multiple queues, it divides its workers evenly among them. Similarly, when
you associate a queue with multiple fleets, it distributes jobs evenly across those
fleets.

###### Note

To use wait and save, we recommend you associate your queue only with a fleet that
uses wait and save instance types. If you associate your queue with more than one fleet,
and any of those fleets use spot or on-demand instance types, your fleet might not process
your jobs with wait and save instances.

To associate an existing queue with an existing fleet, complete the following steps:

1. From your Deadline Cloud farm, select the **Queue** you want to
   associate with a fleet. The queue displays.
2. To select a fleet to associate with your queue, choose **Associate
   fleets**.
3. Choose the **Select fleets** dropdown. A list of available
   fleets displays.
4. From the list of available fleets, select the **checkbox**
   next to the fleet or fleets you want to associate with your queue.
5. Choose **Associate**. The fleet association status should now
   be **Active**.

## Stop a queue fleet association

To stop a queue fleet association, complete the following steps:

1. From your queue, select the **Associated fleets** tab.
2. Select the checkbox for the fleet you want to stop associating with the queue.
3. From the Actions dropdown, select **Eventual stop** or **Immediate stop**.

To finish processing jobs before the association stops, select Eventual stop. To immediately stop processing jobs, select Immediate stop. 4. In the confirmation window, enter `confirm` and then choose **Stop**. 5. (Optional) To disassociate the fleet from the queue, complete the following steps:

    1. Wait for the association status to change to **Stopped**.
    2. After the association has stopped, if you haven't already, select the checkbox for the fleet.
    3. From the Actions dropdown, select **Disassociate fleet**.
    4. In the confirmation window, choose **Disassociate**.

## Reactivate a queue fleet association

To reactivate a queue fleet association, complete the following steps:

1. From your queue, select the **Associated fleets** tab.
2. Select the checkbox for the fleet you want to reactivate the queue fleet association.
3. From the Actions dropdown, choose **Start**. The association status changes to Active.
