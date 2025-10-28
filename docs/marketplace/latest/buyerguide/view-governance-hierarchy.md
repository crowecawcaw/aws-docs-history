# Viewing governance hierarchy

Private Marketplace uses the hierarchy that you configured in Organizations to provide hierarchical governance. An experience associated with an audience governs all audiences at a lower level unless the lower level audience is directly associated with another experience. When you make updates to the hierarchy in Organizations, the changes are automatically synchronized and the governance is updated in Private Marketplace. To visualize the governance, refer to following sections:

- For a hierarchical view of all audiences in your organization, see [Audiences](#audiences-view "#audiences-view").
- For governance details of an organizational unit (OU), see [Organizational unit (OU) details](#organizational-unit-details "#organizational-unit-details").
- For governance details of an account, see [Account details](#account-details "#account-details").

###### Topics

- [Audiences](#audiences-view "#audiences-view")
- [Organizational unit (OU) details](#organizational-unit-details "#organizational-unit-details")
- [Account details](#account-details "#account-details")

## Audiences

The **Audiences** page displays all the audiences in your organization with their governing experiences and association relationship. To view this page:

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Audiences** under **Private Marketplace**.
3. Use the default **Hierarchy** view to navigate down your organization structure viewing nested organizational units (OUs) and accounts.
4. To view the list of OUs, switch to **Organizational unit**.
5. To view the list of accounts, switch to **Account**.
6. Search for an OU or account using its exact ID.

The **Governing experience** column shows the experience governing the audience. The **Relationship** column shows whether the audience is directly associated with the experience (**Associated**) or if it inherits the experience from a higher level (**Inherited**).

An audience is governed by the first **Live** experience on its path to root. For more information, see [Governance hierarchy](private-marketplace-concepts.md#governance-hierarchy "private-marketplace-concepts.md#governance-hierarchy"). If you have nested OUs with accounts at different levels, it may not be straight-forward to deduce the governing experience for an audience. To visualize this, you can use the details pages for OUs and accounts.

## Organizational unit (OU) details

###### To view the governance of an OU

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Audiences** under **Private Marketplace**.
3. Search for an OU using its exact ID. You can also navigate the tree structure to find your OU.
4. Choose the OU name.
5. In the OU details page, you can view the current associated experience and the governing experience for the OU. They will be the same if the current associated experience is **Live**. If the current associated experience is **Not live** or if there isn't one, the governing experience will be inherited from a higher level.
6. View the direct child accounts of the OU in the **Child accounts** table.
7. View the direct child OUs of the OU in the **Child organizational units** table.

## Account details

###### To view the governance of an account

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Audiences** under **Private Marketplace**.
3. Search for an account using its exact ID. You can also navigate the tree structure to find your account.
4. Choose the account name.
5. In the account details page, you can view the current associated experience and the governing experience for the account. They will be the same if the current associated experience is **Live**. If the current associated experience is **Not live** or if there isn't one, the governing experience will be inherited from a higher level.
6. View the hierarchy from the account up to the organization root in the **Hierarchy view** container. View the governing experience at each level. You can visualize how the governing experience for the account is resolved by traversing the tree from leaf to root.
