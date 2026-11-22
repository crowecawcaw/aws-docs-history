

# View, update, and delete a context store

View the details of a context store, update its description, or delete it from a global network.

## View a context store
<a name="view-context-stores"></a>

A global network can have one context store. You can view its Amazon Resource Name (ARN), description, state, and creation time.

**To view your context store**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. The **Context Store** page shows the context store in your global network, including its state.

**To list context stores using the AWS CLI**  
Use the [list-context-stores](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/list-context-stores.html) command. Specify the ID of the global network.

**To view the details of a context store using the AWS CLI**  
Use the [get-context-store](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-context-store.html) command. Specify the ID of the context store. The command returns the details of the context store, including its ARN, description, state, and creation time.

## Update a context store
<a name="update-context-store"></a>

Update the description of a context store while it is in the `AVAILABLE` state. During the update, the context store moves to `UPDATING` and then returns to `AVAILABLE`.

**To update a context store**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. Choose **Edit**.

1. For **Description**, enter a new description for the context store.

1. Choose **Save changes**.

1. Wait until the context store returns to the `AVAILABLE` state.

**To update a context store using the AWS CLI**  
Use the [update-context-store](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/update-context-store.html) command. Specify the ID of the context store and the new description.

## Delete a context store
<a name="delete-context-store"></a>

Delete a context store when you no longer need it. Before deleting the context store, disassociate every transit gateway from it. The context store must be in the `AVAILABLE` state and moves to `DELETING` while Network Manager removes it. After deletion, the context store and its context records are no longer available. For more information, see [Disassociate a transit gateway from a context store using AWS Network Manager](context-store-associations.md#disassociate-context-store).

**To delete a context store**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. Choose **Delete**.

1. In the confirmation dialog box, choose **Delete**.

**To delete a context store using the AWS CLI**  
Use the [delete-context-store](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-context-store.html) command. Specify the ID of the context store.