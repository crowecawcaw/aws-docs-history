# Granting Access to Users

Give users access to portfolios through groups or roles. The best way to
provide portfolio access for many users is to put the users in an IAM group and grant access
to that group. That way you can simply add and remove users from the group to manage portfolio
access. For more information, see [IAM users and groups](../../../IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.md "../../../IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.md") in the
_IAM User Guide_.

In addition to access to a portfolio, users must also have access to the AWS Service Catalog end user
console. You grant access to the console by applying permissions in IAM. For more information,
see [Identity and Access Management in
AWS Service Catalog](controlling_access.md "controlling_access.md").

If you want to share a portfolio and its Principals with other accounts, you can associate
Principal Names (groups, roles or users) with the Portfolio. Principal Names are shared
with the Portfolio and used in recipient accounts to grant access to end users.

###### To grant portfolio access to users or groups

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. From the navigation pane,
   choose **Administration**,
   and then choose **Portfolios**.
3. Choose a portfolio
   that you want
   to grant groups, roles, or users access
   to. AWS Service Catalog directs
   to the **Portfolio details** page.
4. On the **Portfolio details** page,
   choose the **Access** tab.
5. Under **Portfolio access**,
   choose **Grant access**.
6. For **Type**, choose **Principal Name**, and then select the
   **group/**, **role/**, or **user/**,
   Type. You can add up to 9 principal names.
7. Choose **Grant Access**
   to associate the principal
   to the current portfolio.

###### To remove access to a portfolio

1. On the **Portfolio details** page, choose a group, role, or
   user name.
2. Choose **Remove access**.
