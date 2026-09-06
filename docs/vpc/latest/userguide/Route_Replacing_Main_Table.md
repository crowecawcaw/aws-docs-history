

# Replace the main route table
<a name="Route_Replacing_Main_Table"></a>

This section describes how to change which route table is the main route table in your VPC. 

**To replace the main route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and then select the new main route table.

1. Choose **Actions**, **Set main route table**.

1. When prompted for confirmation, enter **set**, and then choose **OK**.

**To replace the main route table using AWS CLI**
+ Use the [replace-route-table-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-route-table-association.html) command.

The following procedure describes how to remove an explicit association between a subnet and the main route table. The result is an implicit association between the subnet and the main route table. The process is the same as disassociating any subnet from any route table.

**To remove an explicit association with the main route table**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and then select the route table.

1. From the **Subnet associations** tab, choose **Edit subnet associations**.

1. Clear the checkbox for the subnet.

1. Choose **Save associations**.