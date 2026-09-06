

# Associate a queue and fleet
<a name="associate-a-queue-and-fleet"></a>

To process jobs, you must associate a queue with a fleet. You can associate a single fleet with multiple queues and a single queue with multiple fleets. When you associate a fleet with multiple queues, it divides its workers evenly among them. Similarly, when you associate a queue with multiple fleets, it distributes jobs evenly across those fleets.

**Note**  
To use wait and save, we recommend you associate your queue only with a fleet that uses wait and save instance types. If you associate your queue with more than one fleet, and any of those fleets use spot or on-demand instance types, your fleet might not process your jobs with wait and save instances. 

To associate an existing queue with an existing fleet, complete the following steps:

1. From your Deadline Cloud farm, select the **Queue** you want to associate with a fleet. The queue displays.

1. To select a fleet to associate with your queue, choose **Associate fleets**.

1. Choose the **Select fleets** dropdown. A list of available fleets displays.

1. From the list of available fleets, select the **checkbox** next to the fleet or fleets you want to associate with your queue.

1. Choose **Associate**. The fleet association status should now be **Active**.

## Stop a queue fleet association
<a name="stop-queue-fleet-association"></a>

To stop a queue fleet association, complete the following steps:

1. From your queue, select the **Associated fleets** tab.

1. Select the checkbox for the fleet you want to stop associating with the queue.

1. From the Actions dropdown, select **Eventual stop** or **Immediate stop**.

   To finish processing jobs before the association stops, select Eventual stop. To immediately stop processing jobs, select Immediate stop.

1. In the confirmation window, enter **confirm** and then choose **Stop**.

1. (Optional) To disassociate the fleet from the queue, complete the following steps:

   1. Wait for the association status to change to **Stopped**.

   1. After the association has stopped, if you haven't already, select the checkbox for the fleet.

   1. From the Actions dropdown, select **Disassociate fleet**.

   1. In the confirmation window, choose **Disassociate**.

## Reactivate a queue fleet association
<a name="reactivate-queue-and-fleet"></a>

To reactivate a queue fleet association, complete the following steps:

1. From your queue, select the **Associated fleets** tab.

1. Select the checkbox for the fleet you want to reactivate the queue fleet association.

1. From the Actions dropdown, choose **Start**. The association status changes to Active. 