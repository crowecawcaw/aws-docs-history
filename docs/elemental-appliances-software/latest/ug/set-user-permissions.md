# Grant permissions to users for Quote Confirmation

Access to the Quote Confirmation service is granted through AWS Identity and Access Management (IAM) policies that are
assigned to each user provisioned within an account. The AWS account root user (the login for the
person who created the AWS account; sometimes referred to as the “account admin”) has
access to all services by default and doesn't need to add any IAM policies to their user
profile to use the Quote Confirmation service.

The root user can create additional users under the same AWS account. For example, you can
create users with the permission to place new orders and other users with permission to
download software and open technical support cases. For information about creating
additional users under the same AWS account, see [Creating IAM users (Console)](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in
the _IAM User Guide_.

To view and place orders, any additional users on the account must have the **ElementalAppliancesSoftwareFullAccess** IAM policy.

###### To add the policy to users

1. Log in to your AWS account.
2. From the account drop-down list, choose \***\*My Security
   Credentials\*\***.
3. If you see a message that indicates that you are accessing the security
   credentials page for your AWS account, choose **Continue to Security
   Credentials**.
4. From the menu on the left, choose **Users**, and then choose the
   user to whom you wish to grant viewing or ordering permissions.
5. On the **Summary** page, choose **Add
   permissions**, and then choose **Attach policies
   directly**.
6. In the search field, enter `ElementalAppliances`.
7. Choose **ElementalAppliancesSoftwareFullAccess**, and then choose
   **Next**.
8. On the **Review** page, choose **Add
   permissions** to add the policy.
9. Repeat the steps for each user on the account that needs permissions.

## Additional resources

For information about IAM policies,
see [Understanding How IAM Works](../../../IAM/latest/UserGuide/intro-structure.md "../../../IAM/latest/UserGuide/intro-structure.md") in the
_IAM User Guide_.
