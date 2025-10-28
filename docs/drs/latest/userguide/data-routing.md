# Data routing and throttling

AWS Elastic Disaster Recovery lets you control how data is routed from your source servers to the
replication servers on AWS through the **Data routing and
throttling** settings. By default, data is sent from the source
servers to the replication servers over the public internet, using the public IP
that was automatically assigned to the replication servers. Transferred data is
always encrypted in transit. Choose **Use private IP for
data replication...** if you want to route the replicated data from
your source servers to the staging area subnet through a private network with a
VPN, AWS Direct Connect, VPC peering, or another type of existing private
connection. Data replication does not work unless you have already set up the
VPN, AWS Direct Connect, or VPC peering in the AWS Console. Usee this option
if you want to:

- Allocate a dedicated bandwidth for replication;
- Use another level of encryption;
- Add another layer of security by transferring the replicated data from one private IP
  address (source) to another private IP address (on AWS).

###### Note

- If you selected the Default subnet, it is unlikely that the
  Private IP is used for that Subnet. Ensure that Private IP (VPN, AWS
  Direct Connect, or VPC peering) is used for your chosen subnet if
  you use this option.
- You can safely select and deselect **Use
  private IP for data replication....** even
  after data replication has begun. This switch causes a
  short pause in replication, and does not have long-term effects
  on the replication.
- Choosing the **Use Private IP for data
  replication...** option does not create a new private
  connection.
- When you select the **Use private IP** option, you choose to
  **Create public IP**. Public IPs are used by default.

## Throttle network bandwidth

You can control the amount of network bandwidth used for data replication per server. By
default, AWS Elastic Disaster Recovery uses all available network bandwidth over five
concurrent connections.

Choose **Throttle network
bandwidth...** to control the transfer rate of data sent from your
source servers to the replication servers over TCP Port 1500.
Enter the bandwidth in Mpbs in the bandwidth field
