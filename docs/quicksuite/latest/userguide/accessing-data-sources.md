# Accessing AWS resources

|                                                                 |
| --------------------------------------------------------------- |
| \*_Applies<br>to:_<br>• Enterprise Edition and Standard Edition |

|                                                                                   |
| --------------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick Suite administrators |

You can control the AWS resources that Amazon Quick Suite can access and scope down access to
these resources at a more granular level. In Enterprise edition, you can also set up general
access defaults for everyone in your account, and you can set up specific access for
individual users and groups.

These access configurations are essential for Amazon Quick Sight data source connectivity, enabling
secure connections to AWS services like Amazon S3, Amazon RDS, Amazon Redshift, and Athena for data analysis
and visualization. Proper resource access setup ensures that Amazon Quick Sight can retrieve and
process data from your AWS data sources while maintaining appropriate security
boundaries.

Use the following sections to help you configure your AWS resources to work with
Quick Suite.

Before you begin, make sure that you have the correct permissions; your system
administrator can give you these. To do so, your system administrator creates a policy that
enables you to use certain IAM actions. Your system administrator then associates that
policy with your user or group in IAM. The required actions are the following:

- `quicksight:AccountConfigurations`
  – To enable setting default access to AWS resources
- `quicksight:ScopeDownPolicy` –
  Scoping policies for permissions to AWS resources
- You can also bring your own IAM roles into Amazon Quick Suite. For more information,
  see [Passing IAM roles to Amazon Quick Suite](../../../quicksight/latest/user/security-create-iam-role.md "../../../quicksight/latest/user/security-create-iam-role.md").

###### To enable or disable the AWS services that Amazon Quick Suite can access

1. Sign in to Amazon Quick Suite at [https://quicksight.aws.amazon.com/](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. At the upper right, choose your user name, and then choose **Manage
   Quick Suite**.
3. Choose **Security & permissions**.
4. Under **QuickSight access to AWS services**, choose
   **Add or remove**.

A screen appears where you can enable all available AWS services.

###### Note

If you see a permissions error, and you're an authorized Amazon Quick Suite
administrator, contact your system administrator for assistance. 5. Select the check boxes for the services that you want to allow. Clear check boxes
for services that you don't want to allow.

If you have already enabled an AWS service, the check box for that service is
already selected. If Amazon Quick Suite can't access a particular AWS service, its check
box is not selected.

In some cases, you might see a message like the following.

`This policy used by Amazon Quick Suite for AWS resource access was modified
 outside of Amazon Quick Suite, so you can no longer edit this policy to provide AWS
 resource permission to Amazon Quick Suite. To edit this policy permissions, go to the
 IAM console and delete this policy permission with policy arn -
 arn:aws:iam::111122223333:policy/service-role/AWSQuickSightS3Policy.`

This type of message means that one of the IAM policies that Amazon Quick Suite uses
was manually altered. To fix this, the system administrator needs to delete the
IAM policy listed in the error message and reload the **Security &
permissions** screen before you try again. 6. Choose **Update** to confirm, or **Cancel** to
return to the previous screen.

###### Topics

- [Setting granular access to AWS
  services through IAM](scoping-policies-iam-interface.md "scoping-policies-iam-interface.md")
- [Using AWS Secrets Manager secrets instead of
  database credentials in Quick Suite](secrets-manager-integration.md "secrets-manager-integration.md")
