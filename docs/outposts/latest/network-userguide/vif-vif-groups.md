# VIF and VIF groups

Local gateway virtual interfaces (VIFs) is a logical interface component of Outposts racks
that sets up VLAN, IP, and BGP connectivity between your Outposts networking devices and an
on-premise networking device for local gateway connectivity. VIFs are created within VIF
groups. VIF groups are logical groupings of VIFs and VIFs are created within VIF groups. You
must create four local gateway VIFs within each VIF group.

###### Contents

###### To create a local gateway VIF group and VIFs

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. From the navigation pane, choose **LGW virtual interface (VIF)
   groups**.
4. Choose **Create VIF group**.
5. In the **LGW VIF group settings** section:
   - Enter a name for the VIF group.
   - Choose the local gateway.
   - Add your BGP ASN.

6. In the **LGW virtual interface** section:
   - Enter a name for the VIF.
   - Choose the link aggregation group (LAG).
   - Add a virtual local area network (VLAN).
   - Add local IP address.
   - Add a peer IP address.
   - Add the peer BGP ASN.

###### Note

    * You must create four local gateway virtual interfaces (LGW VIFs). Each VIF must
     be associated to a link aggregation group (LAG) within the VIF group. This ensures
     complete connectivity between your Outpost and on-premise network devices.
     Incomplete VIF groups can not be associated with local gateway route tables to
     create a routing domain.
    * To ensure proper point-to-point connectivity between your Outpost and
     on-premises router, it's essential to match each LAG with its corresponding local
     gateway VIF. You can review these configurations in the **Link Aggregation
     Groups (LAGs)** section of the AWS Outposts console, where you'll find details
     about your LAGs and their associated service link VIFs networking configurations.
     This information helps you verify the correct mapping of your network connections
     between your Outpost and on-premises infrastructure.
    * The local gateway IP addresses can’t overlap with the service link IP addresses
     that are associated with the same LAG. You can review your service link IP
     information in the **Link Aggregation Groups (LAGs)** section of
     the AWS Outposts console.
    * A local gateway VIF is ready to transfer local gateway traffic when its state is
     available.

7. Choose **Create a LGW VIF Group**.

###### To delete a local gateway VIF

Before deleting a virtual interfaces (VIF) from a VIF group, ensure that the local
gateway VIF group is not associated with a local gateway routing domain and is disconnected
from local gateway route tables. Deleting a local gateway routing domain can impact your local gateway local
network connectivity.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. From the navigation pane, choose **LGW virtual interface (VIF)
   groups**.
4. Choose the VIF group that contains the VIF you want to delete.
5. Choose **Manage LGW VIFs**.
6. Select the VIF to be deleted.
7. Choose **Delete**.

###### To add a local gateway VIF

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. From the navigation pane, choose **LGW virtual interface (VIF)
   groups**.
4. Choose the VIF group that you want to add the VIF to.
5. Choose **Manage LGW VIFs**.
6. Choose **Add VIF**.
7. Provide the following information:
   - Enter a name for the VIF.
   - Choose the link aggregation group (LAG).
   - Add a virtual local area network (VLAN).
   - Add local IP address.
   - Add a peer IP address.
   - Add the peer BGP ASN.

###### Note

    * You must create four local gateway virtual interfaces (LGW VIFs). Each VIF must
     be associated to a link aggregation group (LAG) within the VIF group. This ensures
     complete connectivity between your Outpost and on-premise network devices.
     Incomplete VIF groups can not be associated with local gateway route tables to
     create a routing domain.
    * To ensure proper point-to-point connectivity between your Outpost and
     on-premises router, it's essential to match each LAG with its corresponding local
     gateway VIF. You can review these configurations in the **Link Aggregation
     Groups (LAGs)** section of the AWS Outposts console, where you'll find details
     about your LAGs and their associated service link VIFs networking configurations.
     This information helps you verify the correct mapping of your network connections
     between your Outpost and on-premises infrastructure.
    * The local gateway IP addresses can’t overlap with the service link IP addresses
     that are associated with the same LAG. You can review your service link IP
     information in the **Link Aggregation Groups (LAGs)** section of
     the AWS Outposts console.
    * A local gateway VIF is ready to transfer local gateway traffic when its state is
     available.

8. Choose **Save changes**.

###### To delete a VIF group

You can delete a VIF group if it is not associated with a local gateway routing table.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. From the navigation pane, choose **Networking** and **LGW virtual interface (VIF)
   groups**.
4. Choose the VIF group that you want to delete.
5. On the VIF group page, choose **Disassociate LGW routing domain**.

###### Note

Deleting a local gateway routing domain can impact your local gateway local network connectivity. 6. On the **Delete LGW routing domain** window that appears, choose **Delete LGW routing domain**. 7. On the VIF group page, choose **Delete**. 8. On the **Delete LGW VIF group** window that appears, choose **Delete LGW VIF group**.

###### Note

Deleting a VIF group will delete all the VIFs in the group. You cannot undo this action.
