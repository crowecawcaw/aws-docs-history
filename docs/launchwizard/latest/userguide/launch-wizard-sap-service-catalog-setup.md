# Set up to launch

AWS Service Catalog products created with AWS Launch Wizard

This section provides the required steps to grant permissions to the user group. This
requirement must be met to access AWS Service Catalog products created with
Launch Wizard to launch those products.

**Grant AWS Service Catalog permissions to the user
group**

1. Navigate to the [AWS Identity and Access Management
   console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. Choose **User groups** from the left navigation pane.
3. Choose **Create group.**
4. For **User group name**, enter `Endusers`.
5. Enter `AWSServiceCatalog` in the search box to filter the policy
   list.
6. Select the check box next to the
   **AWSServiceCatalogEndUserFullAccess** policy. You can
   optionally choose **AWSServiceCatalogEndUserReadOnlyAccess** if
   you prefer to grant the user only read-only access. Choose **Create
   group**
7. To add a new user to the group, in the left navigation pane, choose
   **Users**.
8. Choose **Add user**.
9. Enter a **User name**.
10. Select **AWS Management Console access**.
11. Choose **Next: Permissions**.
12. Choose **Add user to group**.
13. Select the check box next to the **Endusers** group, then
    choose **Next:Tags**.
14. Choose **Next: Review**. On the **Review**
    page, choose **Create user**. Download or copy the credentials,
    then choose **Close**.
