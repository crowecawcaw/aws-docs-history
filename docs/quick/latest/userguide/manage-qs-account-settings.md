

# Account details in AWS Quick

Use this section to change the account-wide settings in AWS Quick. To open your account settings, choose the profile icon, and then select **Manage Quick**. Then, click on **Account settings**.

## Deleting your AWS Quick subscription and closing your account
<a name="closing-account"></a>

**Warning**  
**Deleting your AWS Quick subscription permanently destroys all organizational data across all AWS regions and cannot be reversed.**  
This action will immediately and permanently delete:  
Every dashboard, analysis, and dataset across your entire organization in all regions
All user accounts and their associated work
Custom data sources and connections
All sharing permissions and folder structures
Historical usage data and audit logs
All customizations, themes, and organizational settings
**Account deletion from any region affects your entire global Quick deployment.** Even if you have Quick resources in multiple AWS regions, this single action deletes everything worldwide.  
**There is no recovery option.** Once deleted, this data cannot be restored by AWS or recovered through any means.  
**Before proceeding:** Export critical dashboards, back up datasets, and ensure all stakeholders are informed of this permanent action.

The act of deleting your AWS Quick subscription is immediate and final. Deletion removes every AWS Quick asset on the AWS account you are using. It doesn't delete namespaces that you added. (The **Default** namespace is deleted automatically.) You can locate and delete namespaces by using the API operations [ListNamespaces](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListNamespaces.html) and [DeleteNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteNamespace.html).

You can terminate your AWS Quick account from the **Manage Quick** menu or by using the API. To prevent someone from deleting a AWS Quick user account accidentally or maliciously, AWS Quick uses permissions, a switch for the **Account termination protection** setting, and a required confirmation word. 

After your account is deleted, you can create a new AWS Quick account. The process doesn't take more than 15 minutes. The settings for edition and user authorization method on the new account can be the same or different.

Before you can delete your AWS Quick account, make sure of the following: 
+ You're signed in using an IAM user or role with administrator permissions in AWS Quick. We strongly recommend using an IAM identity instead of the AWS root account. For more information about root user security best practices, see [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) in the *IAM User Guide*.
+ You understand that your AWS account is not deleted when you terminate your AWS Quick account. To instead close your AWS account, see [Closing an AWS account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/close-account.html).
+ Terminating your account deletes all users, all uploaded data, and assets (for example, datasets, data sources, queries, dashboards, analyses, settings, and so on). 

**Topics**
+ [Permissions and access to account termination](#delete-account-permissions)
+ [Deleting your account](#delete-account)

### Permissions and access to account termination
<a name="delete-account-permissions"></a>

You need the following special permissions to terminate a AWS Quick account. Without these permissions, you won't be able to terminate a AWS Quick user account. Contact your account administrator for help. 
+ You're a AWS Quick administrator and have an `Admin` role in AWS Quick.
+ You need permissions to run the following (except if you're the root admin user (IAM ) who added AWS Quick)
  + `quicksight:Unsubscribe` 
  + `quicksight:DeleteAccountSubscription` 
  + `ds:UnauthorizeApplication`
  + `ds:DeleteDirectory`
  + `ds:DescribeDirectories`
  + `quicksight:UpdateAccountSettings`
**Note**  
The `DeleteAccountSubscription` AWS Quick API requires both `quicksight:Unsubscribe` and `quicksight:DeleteAccountSubscription` IAM permissions. An explicit deny on either permission results in an `AccessDeniedException`.
+ To remove custom namespaces, you need permission to run the following API operations:
  + `quicksight:ListNamespaces` 
  + `quicksight:DeleteNamespace` 

  You don't need extra permissions to delete the default namespace.

**Warning**  
Terminating your account is an instant action that cannot be undone by you or by AWS.

### Deleting your account
<a name="delete-account"></a>

The following sections outlines the different ways you can terminate your AWS Quick instance.

**To terminate your AWS Quick account without the AWS Quick UI**
+ Sign in to AWS where you want to remove AWS Quick.

**To terminate your account by using the AWS Quick UI**

1. Choose your profile on the application bar, and then choose **Manage Quick**.

1. Use one of the following methods to open the **Account termination** screen.
   + Use this [direct link](https://us-east-1.quicksight.aws.amazon.com/sn/console/unsubscribe) to the screen.
   + Choose **Account settings**, **Manage**.

1. On the **Account termination** page, confirm that you are viewing the correct AWS Quick account by checking the name listed for account name.

1. Toggle off **Account termination protection is on**. Doing this enables the **Delete account** section.

1. For **Type "confirm" to delete this account**, enter the word confirmation word shown on your screen.