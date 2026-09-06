

# Set up to launch AWS Service Catalog products created with AWS Launch Wizard
<a name="launch-wizard-sap-service-catalog-setup"></a>

This section provides the required steps to grant permissions to the user group. This requirement must be met to access AWS Service Catalog products created with Launch Wizard to launch those products.

**Grant AWS Service Catalog permissions to the user group**

1. Navigate to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam).

1. Choose **User groups** from the left navigation pane.

1. Choose **Create group.**

1. For **User group name**, enter `Endusers`. 

1. Enter `AWSServiceCatalog` in the search box to filter the policy list.

1. Select the check box next to the **AWSServiceCatalogEndUserFullAccess** policy. You can optionally choose **AWSServiceCatalogEndUserReadOnlyAccess** if you prefer to grant the user only read-only access. Choose **Create group**

1. To add a new user to the group, in the left navigation pane, choose **Users**.

1. Choose **Add user**.

1. Enter a **User name**.

1. Select **AWS Management Console access**.

1. Choose **Next: Permissions**.

1. Choose **Add user to group**.

1. Select the check box next to the **Endusers** group, then choose **Next:Tags**.

1. Choose **Next: Review**. On the **Review** page, choose **Create user**. Download or copy the credentials, then choose **Close**.