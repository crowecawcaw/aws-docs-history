# Reducing the number of connections and channels

Connections to your RabbitMQ on Amazon MQ broker can be closed either by your client applications, or by
manually closing them using the RabbitMQ web console. To close a connection using the RabbitMQ web console, do the following:

1. Sign in to AWS Management Console and open your broker's RabbitMQ web console.
2. On the RabbitMQ console, choose the **Connections** tab.
3. On the **Connections** page, under **All connections**, choose the name of the connection you want to close from the list.
4. On the connection details page, choose **Close this connection** to expand the section, then choose **Force Close**.
   Optionally, you can replace the default text for **Reason** with your own description. RabbitMQ on Amazon MQ will return the
   reason you specify to the client when you close the connection.
5. Choose **OK** on the dialog box to confirm and close the connection.

When you close a connection, any channels associated with closed connection will also be closed.

###### Note

Your client applications may be configured to automatically re-establish connections to the broker
after they are closed. In this case, closing connections from the broker web console will not be sufficient
for reducing connection or channel counts.

For brokers without public access, you can temporarily block connections by denying inbound traffic on the appropriate message protocol
port, for example, port `5671` for AMQP connections. You can block the port in the security group that you provided
to Amazon MQ when creating the broker. For more information on modifying your security
group, see [Adding rules to a security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md#adding-security-group-rules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#adding-security-group-rules") in the
_Amazon VPC User Guide_.
