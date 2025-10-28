# Managing audiences

Each hierarchical unit in Organizations — organization, organizational units (OUs), or accounts — can be an audience for an experience. When you associate an audience with a **Live** experience, all users in the audience will be governed by the experience and only allowed to procure products approved in the experience.

You can view all the audiences in your organization from the **Audiences** page. This page opens with a **Hierarchy** view displaying the name and ID of the audience, its current governing experience, and association relationship. You can switch to **Organizational unit** to view the list of organizational units (OUs). You can also switch to **Account** to view the list of accounts.

The **Governing experience** column shows the experience governing the audience, and the **Relationship** column shows whether the audience is directly associated with the experience (**Associated**) or if it inherits the experience from a higher level (**Inherited**). Audiences showing **Inherited** status are grayed out because inherited relationships can't be disassociated.

###### To create a new audience association

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Audiences** under **Private Marketplace**.
3. Choose **Create association**.
4. Navigate the tree structure to choose your target audiences. The hierarchy shown reflects your organization structure, displaying the organizational units (OUs) and accounts that you manage in Organizations.
5. You can choose the entire organization, organizational units (OUs), or accounts. If you choose an audience that is directly associated with another experience, it will be disassociated from that experience and associated with the experience you select.
6. After making your selections, choose **Next**.
7. Choose an active experience. If the experience you choose is **Not live**, it will not take effect and govern the audience you associate. You can update the experience status to **Live** in this wizard.
8. After making your selections, choose **Next**.
9. Review the selected audiences to associate with experience, and edit as needed.
10. When you are satisfied with your selections, choose **Associate**.

###### To disassociate an audience from an experience

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Audiences** under **Private Marketplace**.
3. Navigate the tree structure to choose the audiences you want to disassociate.
4. Choose **Disassociate from experience**.
5. Note that OUs and accounts at a lower level which inherit the experience will also be affected when you disassociate. To avoid accidentally disassociating audiences from their currently associated experiences, provide additional consent by entering `confirm` in the text box.
6. Choose **Disassociate**.

###### To edit an audience association

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Audiences** under **Private Marketplace**.
3. Navigate the tree structure to choose the audiences you want to edit associations.
4. Choose **Edit association**.
5. Choose an active experience. All audiences will be disassociated from any previous experiences they were associated with and associated with the selected experience.
6. If the experience you choose is **Not live**, it will not take effect and govern the audience you associate. You can update the experience status to **Live** in this wizard.
7. After making your selections, choose **Save changes**.
