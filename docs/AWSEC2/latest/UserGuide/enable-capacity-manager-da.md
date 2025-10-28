# Registering a delegated administrator

You can register a delegated administrator for Capacity Manager. This allows a member account to manage Capacity Manager for your AWS Organization.
Only the management account can register or remove a delegated administrator within your organization.

###### Note

You can’t disable Capacity Manager for your organization while there is a registered delegated administrator.

###### Topics

- [Prerequisites](#da-prerequisites "#da-prerequisites")
- [Register a delegated administrator](#add-capacity-manager-da "#add-capacity-manager-da")
- [Remove a delegated administrator](#remove-capacity-manager-da "#remove-capacity-manager-da")

## Prerequisites

Your management account must have enabled Capacity Manager with AWS Organizations. For more information, see
[Enabling EC2 Capacity Manager with AWS Organizations](enable-capacity-manager-organizations.md "enable-capacity-manager-organizations.md").

## Register a delegated administrator

You can register a delegated administrator using the Amazon EC2 console or the AWS CLI.

Console

###### To register a delegated administrator

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Manager**.
3. Choose the **Settings** tab.
4. In the **Delegated administrator** section, choose **Add**.
5. In the prompt that appears, enter the account ID of the organization member you want to add as a delegated administrator.
6. Choose **Add delegated administrator**.

AWS CLI

###### To register a delegated administrator

Run the following command:

```

aws organizations register-delegated-administrator \
    --account-id `123456789012` \
    --service-principal ec2.capacitymanager.amazonaws.com

```

## Remove a delegated administrator

You can remove a delegated administrator using the Amazon EC2 console or the AWS CLI.

Console

###### To remove a delegated administrator

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Manager**.
3. Choose the **Settings** tab.
4. In the **Delegated administrator** section, choose **Manage**.
5. In the prompt that appears, choose **Remove delegated administrator**.

AWS CLI

###### To remove a delegated administrator

Run the following command:

```

aws organizations deregister-delegated-administrator \
    --account-id `123456789012` \
    --service-principal ec2.capacitymanager.amazonaws.com

```
