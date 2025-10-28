# Deregister an Active Directory from License Manager settings

You can deregister your Active Directory from License Manager settings if you no longer want to
use it for user-based subscriptions. Deregistering the directory configuration from License Manager settings
doesn't delete the directory. When you deregister the directory from the settings, you can
no longer associate users from that directory for user-based subscriptions in License Manager.

###### Prerequisites

Before you deregister the directory from License Manager settings, you must perform the
following tasks:

1. [Disassociate
   users from an instance](usubs-disassociate-users.md "usubs-disassociate-users.md") from each
   instance that references the directory that you want to deregister.
2. After all of the subscription users are disassociated from the instance, terminate
   the instance. Repeat until all instances that refer to the Active Directory
   are terminated.
3. You also need to [Unsubscribe users](usubs-unsubscribe-users.md "usubs-unsubscribe-users.md") that belong to the
   Active Directory you will deregister to stop incurring changes for them.
   **Deregister**

###### Important

If your Active Directory is used for Microsoft RDS SAL users, you must delete
the associated license server endpoint before you deregister and delete the AD.

###### Deregister the Active Directory from License Manager settings

After you've completed all of the prerequisite tasks, open the License Manager console
at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").

1. In the left navigation pane, choose **Settings**.
2. On the **Settings** page, under the AWS Managed Microsoft AD section, choose
   **Remove**.
3. Enter the required text to confirm that you want to remove the directory and choose
   **Remove**.
   After you choose **Remove**, the **AWS Managed Microsoft AD**
   section on the **Settings** page displays your **Directory
   ID** with the **Status** of **Configuring**.
   Once the configuration process is complete, the directory is removed from the
   **AWS Managed Microsoft AD** section.
