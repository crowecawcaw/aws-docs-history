

# Create a network function group in an AWS Cloud WAN policy version
<a name="cloudwan-policy-network-function-groups"></a>

The following steps guide you through configuring a core network for a policy version using the **Policy versions** link on the AWS Network Manager console. There are no prerequisites for creating a network functions group. For more information, about network function groups, see [Network function groups](cloudwan-create-policy-version.md#cloudwan-core-network-function). 

**To route traffic using a network function group**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity** choose **Cloud WAN**.

1. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.

1. In the navigation pane, choose **Policy versions**.

1. Choose **Create policy version**.

1. In **Choose policy view mode**, choose **Visual editor**.

1. Choose **Network function groups**.

1. Choose **Create**. 

1. Enter a **Name** identifying this function, and then provide an optional **Description**.

1. If the attachment association requires acceptance, choose **Require acceptance**.
**Note**  
An attachment can be associated only with a segment or a network functions group, but not both. You can't associate an attachment to a network functions group if that attachment is already associated with a segment. 

1. Once you've created the network function group, you can create a service insertion segment action that routes your network functions from source segments to destination segments using this network function group. For more information on creating a segment action, see "Service insertion" in [Add segment actions in an AWS Cloud WAN core network policy version](cloudwan-policy-network-actions-routes.md).