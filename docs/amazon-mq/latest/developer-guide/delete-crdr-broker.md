# Deleting an Amazon MQ cross-Region data replication broker

To delete a primary or replica cross-Region data replication (CRDR) broker, you must first unpair then reboot the brokers.
The following instructions show how you can unpair and reboot the brokers using the AWS Management Console.

1. On the **Brokers** page, select the CRDR broker you want to unpair, then choose **Edit**.
2. On the broker **Edit** page in the **Data replication** section,
   choose **Unpair brokers**.
3. Enter "confirm" in the pop-up window to confirm your choice. Then choose **Unpair brokers**.
4. Next, reboot the unpaired primary broker. This will also reboot the replica broker.
   For instructions on rebooting your broker, see [Rebooting a Broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").
   After the primary broker is rebooted, both brokers are unpaired and can be individually deleted.
   To delete your broker, see [Deleting a broker](amazon-mq-deleting-broker.md "amazon-mq-deleting-broker.md").
