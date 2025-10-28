# Share an AWS Cloud WAN core network

The following steps guide you through sharing your core network with other AWS accounts or across your organizations.

###### To share a core network

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Core network**.
5. The **Overview** page opens by default.
6. Choose the **Sharing** tab.
7. To create a resource share, choose **Share core network**.
8. In the **Resource sharing** field, choose an existing resource
   share.
9. For the **Available resource share**, choose the resource that
   you want to share, and then choose **Create resource share**.
10. If there are no resources available to share, you'll need to create a new resource
    share:
    1. Choose **Create resource share**. See [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the
       _AWS RAM User Guide_.
    2. After creating the resource share in AWS RAM, return to the
       **Sharing** page of your core network.
    3. Choose the **Refresh** icon. The page updates to show the
       new resource share that you created.
    4. Choose the newly added resource.

11. Choose **Share core network**.
