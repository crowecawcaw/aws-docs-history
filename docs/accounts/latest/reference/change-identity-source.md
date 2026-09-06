

# Change identity source from AWS Builder ID
<a name="change-identity-source"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

After you've activated advanced features, you can change your identity source from AWS Builder ID. If you change your identity source from AWS Builder ID, you can never reuse AWS Builder ID as the identity source for your AWS organization.

**To change your identity source from AWS Builder ID**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Projects**.

1. In **Manage this organization**, choose **Change identity source**.

   This will open the IAM Identity Center. This is a task that requires root-level permission.

1. On the **Settings** page of the IAM Identity Center console, choose **Actions**, and then **Change identity source**.

1. For **Choose identity source**, AWS Builder ID will be selected. Choose a new source and then choose **Next**.

1. If you are changing to Active Directory, choose the available directory from the menu on the next page. If you are switching to an external identity provider, we recommend that you follow the steps in [How to connect to an external identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-connect-to-an-external-identity-provider.html).

1. Review and confirm your changes. You will need to select all checkboxes to confirm you understand the changes to your organization.

1. Confirm your choice and choose **Change identity source**.

These steps show you how to change your identity source by first accessing AWS Settings. However, you can sign into the AWS Management Console with your delegate admin account and access the IAM Identity Center to change your identity source.