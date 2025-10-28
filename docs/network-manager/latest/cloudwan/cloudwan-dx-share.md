# Create a shared AWS Direct Connect gateway attachment in an AWS Cloud WAN core network

The following steps guide you through creating a shared Direct Connect gateway attachment.

###### To create a shared Direct Connect gateway attachment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, under **Shared by me**, choose
   **Attachments**.
5. Choose **Create attachment**.
6. Enter a **Name** identifying the attachment.
7. From the **Core network** drop-down list, choose the core network
   that you want to associate the Direct Connect gateway with.
8. From the **Attachment type** drop-down list choose
   **Direct Connect gateway attachment**.
9. For the **Edge locations**, choose one of the following:
   - **All** — Choose this option if you want to associate all
     edge locations in your core network with the Direct Connect gateway. When
     choosing this option, any new edge locations deployed in a core network
     policy version are automatically added to the Direct Connect gateway
     attachment and updated with the Direct Connect gateway. This does not
     automatically update any edge locations you might remove from the core
     network policy.
   - **Specific** — Choose this option if you want to
     associate only a subset of edge locations from your core network policy with
     the Direct Connect gateway. When choosing this option, you must manually add
     new or remove edge locations to the Direct Connect gateway attachment after
     deploying a core network policy version. A Direct Connect attachment will be
     attached to the core network edge according to the core network policy edge
     locations but will associated to the segment based on the segment edge
     locations.

10. In the **Direct Connect gateway attachment** section, choose the
    Direct Connect gateway to use for connecting Direct Connect to the Cloud WAN core network.

###### Note

A Direct Connect gateway can be used for only one core network, and can't be
used for any other Direct Connect gateway type. If the attachment between the
Direct Connect gateway and the core network is removed, the gateway becomes
available for other Direct Connect association types. 11. Choose **Create attachment**.
