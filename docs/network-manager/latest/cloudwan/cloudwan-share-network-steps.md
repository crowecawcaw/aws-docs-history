

# Share an AWS Cloud WAN core network
<a name="cloudwan-share-network-steps"></a>

The following steps guide you through sharing your core network with other AWS accounts or across your organizations.

**To share a core network**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Core network**.

1. The **Overview** page opens by default. 

1. Choose the **Sharing** tab.

1. To create a resource share, choose **Share core network**. 

1. In the **Resource sharing** field, choose an existing resource share.

1. For the **Available resource share**, choose the resource that you want to share, and then choose **Create resource share**. 

1. If there are no resources available to share, you'll need to create a new resource share: 

   1. Choose **Create resource share**. See [Create a resource share ](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-create) in the *AWS RAM User Guide*.

   1. After creating the resource share in AWS RAM, return to the **Sharing** page of your core network.

   1. Choose the **Refresh** icon. The page updates to show the new resource share that you created.

   1. Choose the newly added resource.

1. Choose **Share core network**.