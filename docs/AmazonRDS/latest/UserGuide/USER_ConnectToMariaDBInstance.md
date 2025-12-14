# Troubleshooting

connections to your MariaDB DB instance

Two common causes of connection failures to a new DB instance are the following:

- The DB instance was created using a security group that doesn't authorize
  connections from the device or Amazon EC2 instance where the MariaDB application or
  utility is running. The DB instance must have a VPC security group that authorizes
  the connections. For more information, see [Amazon VPC and Amazon RDS](USER_VPC.md "USER_VPC.md").

You can add or edit an inbound rule in the security group. For
**Source**, choose **My IP**. This allows
access to the DB instance from the IP address detected in your browser.

- The DB instance was created using the default port of 3306, and your company has
  firewall rules blocking connections to that port from devices in your company
  network. To fix this failure, recreate the instance with a different port.
  For more information on connection issues, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").
