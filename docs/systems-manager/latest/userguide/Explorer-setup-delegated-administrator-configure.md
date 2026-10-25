

# Configure an Explorer delegated administrator
<a name="Explorer-setup-delegated-administrator-configure"></a>

Use the following procedure to register an Explorer delegated administrator.

**To register an Explorer delegated administrator**

1. Log into your AWS Organizations management account.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Explorer**.

1. Choose **Settings**.

1. In the **Delegated administrator for Explorer** section, verify that you have configured the required service-linked role and service access options. If necessary, choose the **Create role** and **Enable access** buttons to configure these options.

1. For **Account ID**, enter the AWS account ID. This account must be a member account in AWS Organizations.

1. Choose **Register delegated administrator**.

The delegated administrator now has access to the **Include all accounts from my AWS Organizations configuration** and **Select organization units in AWS Organizations** options on the **Create resource data sync** page. 