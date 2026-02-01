• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Viewing individual node details and taking action

on a node

From a list in the **Explore nodes** page in Systems Manager, you can select an
individual node in order to view comprehensive details about the machine or perform a
variety of actions on the node. The **General** page in the detail page
presents comprehensive information about the node.

###### To view individual node details and take action on a node

1.  Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2.  In the navigation pane, choose **Explore nodes**.
3.  (Optional) Follow the steps in [Choosing a filter view for managed node
    summaries](explore-nodes-filter-view.md "explore-nodes-filter-view.md") to refine the list of managed
    nodes displayed for your organization or account.
4.  In the **Node ID** column, choose the linked ID of a
    node.
5.  To view more details about the node, in the left navigation, in the
    **Properties** list, choose a property to view more
    information about:

        * **Tags** – View a list of tags applied to the
         node. You can also add or remove tags.
        * **Inventory** – Choose an inventory type, such
         as **AWS:Application** or
         **AWS:Network**, to view inventory details for the
         node.
        * **Associations** – View details about all
         State Manager associations applied to the node, including details such as
         status and associated SSM document name.
        * **Patches** – View summary information about
         patches and patch status for the node.
        * **Configuration compliance** – View compliance
         details for the node, such as compliance status and compliance issue
         severity.

    For more information about details on the tabs, see [What is the unified console?](systems-manager-unified-console.md "systems-manager-unified-console.md").

6.  To take actions on the node, use the following options in the **Node
    actions** menu:

###### Note

These actions are available only for managed nodes in the AWS account
and Region you are currently working in. For managed nodes you might have
access to in other accounts or Regions, you can instead access a
**Properties** list.

    * **Connect, Start terminal session** – Connect
     to the node using [AWS Systems Manager Session Manager](session-manager.md "session-manager.md").
    * **Tools**




    	+ **View file system** – Browse the
    	 contents of the node's directory structure. Add, rename, and
    	 remove directories. Cut or copy and paste files.
    	+ **View performance counters** – View
    	 performance information about the node such as CPU utilization,
    	 network traffic, and other utilization types.
    	+ **Managed processes** – View
    	 information about resource usage on the node. Start or stop
    	 processes on the node.
    	+ **Manage users and groups** – View,
    	 add, or delete user accounts and user groups on the node.
    	+ **Execute run command** – Use [AWS Systems Manager Run Command](run-command.md "run-command.md") to
    	 manage the configuration of the node. Run Command uses [Systems Manager documents](documents.md "documents.md") to perform
    	 on-demand changes such as updating applications or running Linux
    	 shell scripts and Windows PowerShell commands.
    	+ **Patch nodes** – Use the
    	 **Patch now** feature in [AWS Systems Manager Patch Manager](patch-manager.md "patch-manager.md") to
    	 run an on-demand patching operation on the node from the
    	 console.
    ###### Note

    The preceding tasks can also be initiated from the
     **Tools** menu in the left navigation.
    * **Node settings**




    	+ **Add tags** – Apply additional tag
    	 key-value pairs to the node.
    	+ **Reset node user password** – Set a
    	 new password for a specified user on the node.
    	+ **Modify IAM role** – Change the
    	 IAM role that's associated with the node. Create a new IAM
    	 role to attach to the node.
