# Grant permissions to AWS Service Catalog end users

Before the end user can use AWS Service Catalog, you must grant access to the AWS Service Catalog end user console view. To
grant access, you attach policies to the IAM user, group, or role that is used by the end user.
In the following procedure, we attach the \***\*`AWSServiceCatalogEndUserFullAccess`\*\*** policy
to an IAM group.

###### To grant permissions to an end user group

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups**.
3. Choose **Create group** and do the following:
   1. For **User group name**, type `Endusers`.
   2. In the search field, type `AWSServiceCatalog` to filter the policy list.
   3. Select the checkbox for the \***\*`AWSServiceCatalogEndUserFullAccess`\*\*** policy.
      You also have the option to choose \***\*`AWSServiceCatalogEndUserReadOnlyAccess`\*\*** instead.
   4. Choose **Create Group**.

4. In the navigation pane, choose **Users**.
5. Choose **Add users** and do the following:
   1. For **User name**, type a name for the user.
   2. Select **Password - AWS Management Console access**.
   3. Choose **Next: Permissions**.
   4. Choose **Add user to group**.
   5. Select the checkbox for the **Endusers** group and choose **Next: Tags** and then **Next: Review**.
   6. On the **Review** page, choose **Create user**. Download or copy
      the credentials and then choose **Close**.
