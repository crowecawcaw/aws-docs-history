# View and change a permission

set

You can use permission sets to grant users access to AWS accounts. You can
view and change a permission set with the AWS IAM Identity Center console. You can search and
sort permission sets by name in the IAM Identity Center console. For more information about
permission sets and how they are used in IAM Identity Center, see [Manage AWS accounts with permission
sets](permissionsetsconcept.md "permissionsetsconcept.md").

Permission sets are not required to manage user access to applications.

###### Note

To use permission sets, you'll need to use an Organization instance of
IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

## View permission set

assignments

Use this procedure to view applied permission set in the AWS IAM Identity Center
console.

All AWS accounts where a permission set is
provisioned
To view all the assignments for a permission set, use the
following procedure:

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Under **Multi-account
   permissions**, choose **Permission sets**.
3. On the **Permission
   sets** page, select the permission set you
   want to view.
4. Once on the selected permission sets page, under the
   **Accounts** tab, you can see the
   accounts where the permission set is used. You can
   select the account to see how the permission set is
   provisioned within the account. You can [delete](howtoremovepermissionset.md "howtoremovepermissionset.md"), edit, and attach policies to the
   permission set.

All permission sets for an AWS account
To view all the assignments for a permission set, use the
following procedure:

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Under **Multi-account permissions**,
   choose **AWS accounts**. Select the
   account for which you want to view the provisioned
   permission sets.
3. Once on the selected AWS account page, under the
   **Permission sets** tab, you can
   view the different permission set assigned to the
   selected AWS account. You can select the permission
   set hyperlink to learn more about the permission set.

All applied permission sets to users and groups
To view all the permission sets assigned to users or groups,
use the following procedure:

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Select either Users or Groups under
   **Dashboard** to view IAM Identity Center users
   or groups.
   1. Once on the **Users** page,
      select the user for whom you want to see applied
      permission sets. Next, select the
      **AWS accounts** tab and the
      AWS account under the **AWS account
      access** section. You’ll be able to see
      the applied permission sets and AWS account for
      the selected user.
   2. Once on the **Groups** page,
      select the group you want to view applied
      permission sets. Next, select the
      **AWS accounts** tab and the
      AWS account under the **AWS account
      access** section. You’ll be able to see
      the applied permission sets and AWS account for
      the selected group.

## Change a permission set

Use this procedure to change a [permission set](permissionsetsconcept.md "permissionsetsconcept.md") with the IAM Identity Center console. You can add or remove
permission sets from users or groups.

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Under **Multi-account permissions**,
   choose **AWS accounts**.
3. On the **AWS account** page, a tree
   view list of your organization appears. Select the name of the
   AWS account from which you want to change the permission
   set.
4. On the **Overview** page of the
   AWS account, under **Assigned Users and
   Groups**, select the username or group name of the
   permission set you want to change. Then choose **Change permission sets**.
5. Make the desired changes to the permission set and then choose
   **Save changes**.
6. Navigate to the **Permission sets**
   tab and select the recently changed permission set and choose
   **Update**.
7. On the **Update permissions** page,
   choose **Update**.
