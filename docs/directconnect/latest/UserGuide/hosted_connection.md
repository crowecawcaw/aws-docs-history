# Hosted Direct Connect connections

To create an Direct Connect hosted connection, you need the following information:

**Direct Connect location**

Work with an AWS Direct Connect Partner in the AWS Direct Connect Partner Program to help you establish network circuits
between an Direct Connect location and your data center, office, or colocation
environment. They can also help provide colocation space within the same
facility as the location. For more information, see [Direct Connect Delivery
Partners](https://aws.amazon.com/directconnect/partners "https://aws.amazon.com/directconnect/partners").

###### Note

You can't request a hosted connection through the Direct Connect console.
However, an AWS Direct Connect Partner can create and configure a hosted connection for
you. Once configured, the connection appears in the
**Connections** pane in the console.

You must accept the hosted connection before you can use it. For more
information, see [Accept a hosted connection](accept-hosted-connection.md "accept-hosted-connection.md").

**Port speed**

For hosted connections, the possible values are 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps,
400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps. Note that
only those Direct Connect partners who have met specific requirements may create a
1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps hosted connection. 25 Gbps
connections are available only in Direct Connect locations where 100 Gbps
port speeds are available.

Note the following:

- Connection port speeds can only be changed by your AWS Direct Connect Partner.
  Please check with your AWS Direct Connect Partner to see if they support upgrade
  or downgrade of an existing connection. If your Partner supports upgrade/downgrade
  of your connection, you are no longer required to delete and then recreate a
  connection in order to upgrade or downgrade an existing hosted connection's
  bandwidth.
- AWS uses traffic policing on hosted connections, which means that when the
  traffic rate reaches the configured maximum rate, excess traffic is dropped.
  This might result in bursty traffic having a lower throughput than non-bursty
  traffic.
- Jumbo frames can be enabled on connections only if originally enabled on the Direct Connect
  hosted parent connection. If Jumbo frames isn't enabled on that parent
  connection, then it can't be enabled on any connection.
  The following console operations are available after you've requested a hosted connection
  and accepted it:

- [Delete a connection](deleteconnection.md "deleteconnection.md")
- [Update a connection](updateconnection.md "updateconnection.md")
- [View connection details](viewdetails.md "viewdetails.md")
  After you accept a connection, create a virtual interface to connect to public and private
  AWS resources. For more information, see [Virtual interfaces and hosted virtual interfaces](WorkingWithVirtualInterfaces.md "WorkingWithVirtualInterfaces.md").
