

# Registering a delegated administrator
<a name="enable-capacity-manager-da"></a>

You can register a delegated administrator for Capacity Manager. This allows a member account to manage Capacity Manager for your AWS Organization. Only the management account can register or remove a delegated administrator within your organization.

**Note**  
You can't disable Capacity Manager for your organization while there is a registered delegated administrator. 

**Topics**
+ [Prerequisites](#da-prerequisites)
+ [Register a delegated administrator](#add-capacity-manager-da)
+ [Remove a delegated administrator](#remove-capacity-manager-da)

## Prerequisites
<a name="da-prerequisites"></a>

Your management account must have enabled Capacity Manager with AWS Organizations. For more information, see [Enabling EC2 Capacity Manager with AWS Organizations](enable-capacity-manager-organizations.md).

## Register a delegated administrator
<a name="add-capacity-manager-da"></a>

You can register a delegated administrator using the Amazon EC2 console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To register a delegated administrator**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the **Settings** tab.

1. In the **Delegated administrator** section, choose **Add**.

1. In the prompt that appears, enter the account ID of the organization member you want to add as a delegated administrator.

1. Choose **Add delegated administrator**.

------
#### [ AWS CLI ]

**To register a delegated administrator**  
Run the following command:

```
aws organizations register-delegated-administrator \
    --account-id {{123456789012}} \
    --service-principal ec2.capacitymanager.amazonaws.com
```

------
#### [ PowerShell ]

**To register a delegated administrator**  
Use the [Register-ORGDelegatedAdministrator](https://docs.aws.amazon.com/powershell/latest/reference/items/Register-ORGDelegatedAdministrator.html) cmdlet.

```
Register-ORGDelegatedAdministrator `
    -AccountId "{{123456789012}}" `
    -ServicePrincipal "ec2.capacitymanager.amazonaws.com"
```

------

## Remove a delegated administrator
<a name="remove-capacity-manager-da"></a>

You can remove a delegated administrator using the Amazon EC2 console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To remove a delegated administrator**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the **Settings** tab.

1. In the **Delegated administrator** section, choose **Manage**.

1. In the prompt that appears, choose **Remove delegated administrator**.

------
#### [ AWS CLI ]

**To remove a delegated administrator**  
Run the following command:

```
aws organizations deregister-delegated-administrator \
    --account-id {{123456789012}} \
    --service-principal ec2.capacitymanager.amazonaws.com
```

------
#### [ PowerShell ]

**To remove a delegated administrator**  
Use the [Unregister-ORGDelegatedAdministrator](https://docs.aws.amazon.com/powershell/latest/reference/items/Unregister-ORGDelegatedAdministrator.html) cmdlet.

```
Unregister-ORGDelegatedAdministrator `
    -AccountId "{{123456789012}}" `
    -ServicePrincipal "ec2.capacitymanager.amazonaws.com"
```

------