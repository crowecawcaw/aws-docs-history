

# Restricting which users can access the monitor
<a name="restrict-user-management-visibility"></a>

To sign in to the Deadline Cloud monitor, a user needs two levels of access:
+ **AWS IAM Identity Center (IAM Identity Center) application access** – Permission to sign in to the Deadline Cloud monitor application.
+ **Deadline Cloud resource access** – Permission to view farms, queues, and other resources after signing in.

By default, IAM Identity Center application access is open to all users in your identity store. Deadline Cloud resource access is the primary access control layer. However, you can add a second layer of control by restricting who can sign in to the monitor application.

To restrict monitor sign-in, enable the **Require assignments** setting on the Deadline Cloud monitor application in IAM Identity Center. After you enable this setting, only users and groups that you explicitly assign to the application can sign in to the monitor.

**To enable Require assignments for the monitor application**

1. Open the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon](https://console.aws.amazon.com/singlesignon/home).

1. In the navigation pane, choose **Applications**.

1. Select the Deadline Cloud monitor application.

1. In the application's assignment configuration, enable **Require assignments**.

1. Assign the specific users and groups who need access to the application.

Users and groups that you don't assign to the application can't sign in to the monitor, even if they exist in your IAM Identity Center identity store.

For more information about application assignments, see [Assign user access to applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/assignuserstoapp.html) in the *IAM Identity Center User Guide*.