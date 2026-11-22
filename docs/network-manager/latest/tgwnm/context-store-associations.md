

# Manage context store associations

A context store association links a transit gateway to a context store. While associated, the context store collects context for resources connected to the transit gateway. When you disassociate the transit gateway, context collection stops and its resource context is removed from the store.

Note the following about context store associations:
+ Registering a transit gateway with a global network and associating it with a context store are separate steps. Register the transit gateway with the same global network as the context store before you associate it. For more information, see [Transit gateway registrations in AWS Global Networks for Transit Gateways](tgw-registrations.md).
+ You can associate a transit gateway with only one context store.
+ You can associate transit gateways from more than one Region with a single context store. Each resource context identifies the Region of the resource.

## Associate a transit gateway with a context store using AWS Network Manager
<a name="associate-context-store"></a>

Associate a transit gateway with a context store to collect context for resources connected to it. The association moves from `ASSOCIATING` to `ASSOCIATED`. If the association moves to `FAILED`, disassociate the transit gateway and then associate it again.

**To associate a transit gateway with a context store**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. Choose the **Associations** tab, and then choose **Create association**.

1. Choose the transit gateway to associate, and then choose **Add**.

1. Wait until the association state is `ASSOCIATED`.

**To associate a transit gateway using the AWS CLI**  
Use the [associate-context-store](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/associate-context-store.html) command. Specify the ID of the context store and the Amazon Resource Name (ARN) of the transit gateway.

## View context store associations using AWS Network Manager
<a name="view-context-store-associations"></a>

View all transit gateways associated with a context store or the details and state of a specific association.

**To view context store associations**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. Choose the **Associations** tab, which lists the transit gateways that are associated with the context store, including the state of each association.

**To list context store associations using the AWS CLI**  
Use the [list-context-store-associations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/list-context-store-associations.html) command. Specify the ID of the context store.

**To view a single context store association using the AWS CLI**  
Use the [get-context-store-association](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-context-store-association.html) command. Specify the ID of the context store and the Amazon Resource Name (ARN) of the transit gateway. The command returns the details of the association, including its state and creation time.

## Disassociate a transit gateway from a context store using AWS Network Manager
<a name="disassociate-context-store"></a>

Disassociate a transit gateway to stop collecting its resource context. The association enters the `DISASSOCIATING` state and is removed when the process completes.

Disassociate every transit gateway from a context store before you delete the context store. For more information, see [Delete a context store](manage-context-store.md#delete-context-store).

**To disassociate a transit gateway from a context store**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. Choose the **Associations** tab.

1. Select the transit gateway, and then choose **Delete association**.

1. In the confirmation dialog box, choose **Delete association**.

**To disassociate a transit gateway using the AWS CLI**  
Use the [disassociate-context-store](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/disassociate-context-store.html) command. Specify the ID of the context store and the Amazon Resource Name (ARN) of the transit gateway.