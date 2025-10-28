# VPC peering configuration for

AWS DMS.

VPC peering enables private network connectivity between two VPCs, allowing AWS DMS
replication instances and database endpoints to communicate across different VPCs as
if they were in the same network. This is crucial when your DMS replication instance
resides in one VPC while source or target databases exist in separate VPCs, enabling
direct, secure data migration without traversing the public internet.

When using Amazon RDS, you must configure VPC peering between DMS and RDS if your
instances are located in different VPCs.

You must perform the following steps:

###### Creating a VPC peering connection

1. Navigate to the [Amazon
   VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, select **Peering Connections**
   under **Virtual private cloud**.
3. Click **Create Peering Connection**.
4. Configure the peering connections:
   - Name tag (optional): Enter a name for the peering connection
     (example: `DMS-RDS-Peering`).

   **VPC Requester**: Select the VPC
   that contains your DMS instance.
   - **VPC accepter**: Select the VPC that
     contains your RDS instance.

   ###### Note

   If the accepter VPC is associated with a different AWS
   account, you must have the Account ID and VPC ID for that
   acount.

5. Click **Create the Peering Connection**.

###### Accepting the VPC peering connection

1. In the **Peering Connections** list, find the new peering
   connection with a **Pending Acceptance**
   status.
2. Select the appropriate peering connection, click
   **Actions** and select **Accept
   Request**.

The peering connection status changes to **Active**.

###### Updating route tables

To enable traffic between the VPCs, you must update the route table in both
your VPCs. To update the route tables in the DMS VPC:

1. Identify CIDR block of the RDS VPC:
   1. Navigate to your VPCs and select your RDS VPC.
   2. Copy the IPv4 CIDR value in **CIDRs** tab.

2. Identify relevant DMS route tables using resource map:
   1. Navigate to your VPCs and select your DMS VPC.
   2. Click the **Resource Map** tab and note the route
      tables associated with the subnets where your DMS instance is
      located.

3. Update all route tables in the DMS VPC:
   1. Navigate to the route tables in the [Amazon VPC
      console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
   2. Select the route tables identifies for the DMS VPC. You can open
      them from the VPC's **Resource map** tab.
   3. Click **Edit routes**.
   4. Click Add route and enter the following information:
      - **Destination**: Enter the
        IPv4 CIDR block of the RDS VPC (Example:
        `10.1.0.0/16`).
      - **Target**: Select the
        peering configuration ID (Example:
        `pcx-1234567890abcdef`).

   5. Click **Save routes**.

   Your VPC routes are saved for the DMS VPC. Perform the same steps
   for your RDS VPC.

###### Update Security Groups

1. Verify the DMS instance Security Group:
   1. You must ensure that the outbound rules allow traffic to the RDS
      instance:
      - **Type**: Custom TCP or the
        specific database port (Example: 3306 fir MySQL).
      - **Destination**: The CIDR
        block of the RDS VPC or the security group of the RDS
        instance.

2. Verify the RDS instance Security Group:
   1. You must ensure that the inbound rules allow traffic from the DMS
      instance:
      - **Type**: The specific
        database port.
      - Source: The CIDR block of the DMS VPC or the security
        group of the RDS instabce.

###### Note

You must also ensure the following:

- **Active Peering Connection**: Ensure the
  VPC peering connection is in the **Active**
  state before proceeding.
- **Resource Map**: Use the
  **Resource map** tab in the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/")
  console to identify which route tables need update.
- **No Overlapping CIDR Blocks**: The VPCs
  must have non-overlapping CIDR blocks.
- **Security Best Practices**: Restrcict
  Security Group rules to the necessary ports and sources.

For more information, see [VPC peering connections](../../../vpc/latest/peering/working-with-vpc-peering.md "../../../vpc/latest/peering/working-with-vpc-peering.md") in the
_Amazon Virtual Private Cloud user
guide_.
