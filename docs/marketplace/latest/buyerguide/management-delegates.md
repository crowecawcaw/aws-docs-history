

# Using delegated administrators
<a name="management-delegates"></a>

The steps in the following sections explain how to register and deregister delegated administrators. Delegated administrators can view all the data in your organization.

**Important**  
You or your AWS administrator must enable all features for your organization, and you must belong to an AWS Organizations management account to complete the following steps. For more information, see [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) and [Managing the management account with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-manage_accounts_management.html), both in the *AWS Organizations User Guide*.

**Topics**
+ [Registering delegated administrators](#management-register-delegate)
+ [Deregistering delegated administrators](#management-deregister-delegate)

## Registering delegated administrators
<a name="management-register-delegate"></a>

To create delegated administrators, you register an account ID, and everyone in that account can get a consolidated view of agreement and cost data.

**To register administrators**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

1. In the navigation pane, choose **Settings**.

1. Under **Delegated administrators**, choose **Register**.

   The **Register delegated administrator** page appears.

1. In the **Account ID** box, enter the desired account ID.

1. Choose **Register**.

## Deregistering delegated administrators
<a name="management-deregister-delegate"></a>

The following steps explain how to deregister an account and prevent everyone in that account from seeing an overall view of your data.

**To deregister administrators**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

1. In the navigation pane, choose **Settings**.

1. Under **Delegated administrators**, select the radio button next to account that you want to deregister. 

1. Choose **Deregister**.

1. In the **Deregister a delegate administrator** dialog box, choose **Deregister**.