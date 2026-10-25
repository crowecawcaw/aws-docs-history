

# Managing AWS account groups
<a name="manage-audiences"></a>

Each hierarchical unit in Organizations — organization, organizational units (OUs), or accounts — can be an AWS account group for an experience. When you associate an AWS account group with a **Live** experience, all users in the AWS account group will be governed by the experience and only allowed to procure products approved in the experience.

You can view all the AWS account groups in your organization from the **AWS account groups** page. This page opens with a **Hierarchy** view displaying the name and ID of the AWS account group, its current governing experience, and association relationship. You can switch to **Organizational unit** to view the list of organizational units (OUs). You can also switch to **Account** to view the list of accounts.

The **Governing experience** column shows the experience governing the AWS account group, and the **Relationship** column shows whether the AWS account group is directly associated with the experience (**Associated**) or if it inherits the experience from a higher level (**Inherited**). AWS account groups showing **Inherited** status are grayed out because inherited relationships can't be disassociated.

**To create a new AWS account group association**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **AWS account groups** under **Private Marketplace**.

1. Choose **Create association**.

1. Navigate the tree structure to choose your target AWS account groups. The hierarchy shown reflects your organization structure, displaying the organizational units (OUs) and accounts that you manage in Organizations.

1. You can choose the entire organization, organizational units (OUs), or accounts. If you choose an AWS account group that is directly associated with another experience, it will be disassociated from that experience and associated with the experience you select.

1. After making your selections, choose **Next**.

1. Choose an active experience. If the experience you choose is **Not live**, it will not take effect and govern the AWS account group you associate. You can update the experience status to **Live** in this wizard.

1. After making your selections, choose **Next**.

1. Review the selected AWS account groups to associate with experience, and edit as needed.

1. When you are satisfied with your selections, choose **Associate**.

**To disassociate an AWS account group from an experience**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **AWS account groups** under **Private Marketplace**.

1. Navigate the tree structure to choose the AWS account groups you want to disassociate.

1. Choose **Disassociate from experience**.

1. Note that OUs and accounts at a lower level which inherit the experience will also be affected when you disassociate. To avoid accidentally disassociating AWS account groups from their currently associated experiences, provide additional consent by entering **confirm** in the text box.

1. Choose **Disassociate**.

**To edit an AWS account group association**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **AWS account groups** under **Private Marketplace**.

1. Navigate the tree structure to choose the AWS account groups you want to edit associations.

1. Choose **Edit association**.

1. Choose an active experience. All AWS account groups will be disassociated from any previous experiences they were associated with and associated with the selected experience.

1. If the experience you choose is **Not live**, it will not take effect and govern the AWS account group you associate. You can update the experience status to **Live** in this wizard.

1. After making your selections, choose **Save changes**.