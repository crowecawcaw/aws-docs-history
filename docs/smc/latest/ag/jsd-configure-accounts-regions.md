

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Accounts and Regions
<a name="jsd-configure-accounts-regions"></a>

After you install the AWS Service Management Connector, you need to configure it. To do so, choose the Jira administration icon in the top right, then choose **Add-ons**.

1. From the Service Catalog section on the left navigation menu, choose **AWS Accounts**.

1. Choose **Connect new account**.

1. Enter the account alias (used to identify the AWS account in the Connector).

1. Enter the credentials for SC-sync-user. It is the access key identity and credentials for a sync user saved from the AWS configuration. SC-sync-user credentials can retrieve portfolios and products to make them available through Jira Service Management. You can set the allowed groups that can access them.

1. Enter the credentials for SC-end-user. It is the access key identity and credentials for the end user saved from the AWS configuration. The SC-end-user credentials provision products on behalf of a Jira user.

1. Add **AWS Regions**. It contains Service Catalog products and portfolios you want available in Jira Service Management.

1. Choose **Test Connectivity**.

1. Upon successful connection status, choose **Connect**.

**Note**  
We recommend the Sync user and End user be new users in AWS, used only with AWS Service Management Connector. These users should have minimum required privileges. You can use the available AWS CloudFormation templates for your sandbox and development AWS accounts to configure and enable available integrations. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/smc/latest/ag/jsd-baseline-permissions.html).