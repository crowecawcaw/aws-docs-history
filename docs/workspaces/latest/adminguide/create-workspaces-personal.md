

# Create a WorkSpace in WorkSpaces Personal
<a name="create-workspaces-personal"></a>

WorkSpaces enables you to provision virtual, cloud-based Windows and Linux desktops for your users, known as *WorkSpaces*.

You can create a WorkSpace by:
+ **Getting a Recommendation** – Provide details of how you will use your WorkSpace, and WorkSpaces Advisor will give you tailored guidance of how you should configure your WorkSpace, including which bundle to use and how to set up a recommended directory.
+ **Copy from an existing WorkSpace** – If you already have an existing WorkSpace that is configured to your needs, you can select the WorkSpace and create another WorkSpace that will be configured exactly the same.
+ **Configure manually** – Choose your own bundle, directory, and other settings without guidance.

## Get a Recommendation
<a name="create-workspaces-get-recommendation"></a>

WorkSpaces Advisor can guide you through the steps to create a WorkSpace, based on the input you provide. To get started:

**Note**  
The recommendation flow requires additional permissions beyond the standard create flow, including `workspaces:Personalization`, which stores your use-case answers and recommendations. For the complete list, see [Amazon WorkSpaces Console operations permissions reference](wsp-console-permissions-ref.md).
**Get a Recommendation** is not available in the Africa (Cape Town) Region or the AWS GovCloud (US) Regions, and does not support Bring Your Own License (BYOL) bundles. In those cases, create your WorkSpace manually. For instructions, see [Configure manually](#create-workspaces-manual).

**To create a WorkSpace with a recommendation**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**, **Personal**.

1. Choose **Create WorkSpaces**.

1. For **Creation method**, keep **Get a Recommendation**, which is selected by default.

1. Choose the category that best represents your end user, and describe the tasks or applications that the WorkSpace will be used for. Then choose **Get recommendations** to see which WorkSpaces Personal bundles are best suited for your use case.

1. Choose a recommended bundle, or expand **Or choose your own** to select a different WorkSpaces bundle. Then choose **Choose bundle**.

1. Choose a running mode. WorkSpaces Advisor recommends a running mode based on your previous answers.

1. Proceed to the **Directory and users** section to create or choose a directory for your WorkSpace. If you already have a directory, WorkSpaces Advisor may suggest reusing it. If not, WorkSpaces Advisor guides you through the steps to create a new directory. Creating a new directory can take up to 40 minutes. You can leave the page and return later; provisioning continues in the background.
**Note**  
If a provisioning step fails, you can edit your input and retry, or discard the retry and start over. Resources created during a failed attempt—such as the VPC, subnets, or directory—are not deleted automatically, and may continue to incur charges until you delete them.

1. Select or create the user to provision the WorkSpace for.

1. Under **Customization** (optional), you can customize volume sizes, root and user volume encryption, and nested virtualization.
   + To enable encryption for the root volume, user volume, or both, select the volumes under **Encryption**, and then select a KMS key. For more information, see [Encrypted WorkSpaces in WorkSpaces Personal](encrypt-workspaces.md).
   + To enable nested virtualization, expand **Nested virtualization** and select **Enable Nested Virtualization**. With nested virtualization, you can run hypervisors such as Hyper-V and KVM inside your WorkSpace. This enables tools like Docker Desktop and WSL2. For more information, see [Nested virtualization for WorkSpaces Personal](nested-virtualization.md).
**Note**  
Nested virtualization is available only on non-GPU bundles that use the DCV (WSP) protocol with a supported operating system. For the full list of supported configurations, see [Nested virtualization for WorkSpaces Personal](nested-virtualization.md).

1. Under **Tags** (optional), specify the key-value pairs that you want to use.

1. Choose **Create WorkSpaces**. A status page tracks the WorkSpace creation (typically 10–20 minutes); you can leave the page and check back later. The initial status of the WorkSpace is `PENDING`. When the creation is complete, the status is `AVAILABLE`, the status page shows the registration code and the steps to connect, and an invitation is sent to the email address that you specified for the user.

1. Send invitations to the email address for each user. For more information, see [Send an invitation email](manage-workspaces-users.md#send-invitation).
**Note**  
These invitations aren't sent automatically if you're using AD Connector or a trust relationship.
Invitation emails aren't sent if the user already exists in Active Directory. Instead, make sure you manually send the user an invitation email. For more information, see [Send an invitation email](manage-workspaces-users.md#send-invitation).
In all Regions, the text of the invitation email is in English (US). In the following Regions, the English text is preceded by a second language:  
Asia Pacific (Seoul): Korean
Asia Pacific (Tokyo): Japanese
Canada (Central): French (Canadian)
China (Ningxia): Simplified Chinese

1. Proceed to [Connect to the WorkSpace](#connect-workspace-ad-connector).

## Copy from an existing WorkSpace
<a name="create-workspaces-copy"></a>

If you have configured an existing WorkSpace and would like to create new WorkSpaces that are identically configured, you can copy an existing WorkSpace to up to 25 new WorkSpaces.

**To copy an existing WorkSpace**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**, **Personal**.

1. Choose **Create WorkSpaces**.

1. For **Creation method**, choose **Copy from an existing WorkSpace**.

1. Under **Select WorkSpace**, choose the existing WorkSpace that you want to copy.

1. Proceed to the **Users** section to choose the users that will use the new WorkSpaces. A WorkSpace is created for each user that you select. You can only choose users that are in the same directory as the one used with the existing WorkSpace.

1. Under **Customization** (optional), review the storage and encryption settings copied from the source WorkSpace, and adjust them if needed.

1. Under **Tags** (optional), specify the key-value pairs that you want to use.

1. Choose **Create WorkSpaces**. The initial status of the WorkSpace is `PENDING`. When the creation is complete, the status is `AVAILABLE` and an invitation is sent to the email address that you specified for the user.

1. Send invitations to the email address for each user. For more information, see [Send an invitation email](manage-workspaces-users.md#send-invitation).
**Note**  
These invitations aren't sent automatically if you're using AD Connector or a trust relationship.
Invitation emails aren't sent if the user already exists in Active Directory. Instead, make sure you manually send the user an invitation email. For more information, see [Send an invitation email](manage-workspaces-users.md#send-invitation).
In all Regions, the text of the invitation email is in English (US). In the following Regions, the English text is preceded by a second language:  
Asia Pacific (Seoul): Korean
Asia Pacific (Tokyo): Japanese
Canada (Central): French (Canadian)
China (Ningxia): Simplified Chinese

1. Proceed to [Connect to the WorkSpace](#connect-workspace-ad-connector).

## Configure manually
<a name="create-workspaces-manual"></a>

Before creating a personal WorkSpace, create a directory by doing one of the following:
+ Create a Simple AD directory.
+ Create an AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD.
+ Connect to an existing Microsoft Active Directory by using Active Directory Connector.
+ Create a trust relationship between your AWS Managed Microsoft AD directory and your on-premises domain.
+ Create a dedicated directory that uses Microsoft Entra ID as the identity source (through IAM Identity Center). WorkSpaces in the directory are native Entra ID-joined and enrolled into Microsoft Intune through Microsoft Windows Autopilot user-driven mode.
**Note**  
Such directories currently only support Windows 10 and 11 Bring Your Own Licenses personal WorkSpaces.
+ Create a dedicated directory that uses an identity provider of your choice as the identity source (through IAM Identity Center). WorkSpaces in the directory are native Entra ID-joined and enrolled into Microsoft Intune through Microsoft Windows Autopilot user-driven mode.
**Note**  
Such directories currently only support Windows 10 and 11 Bring Your Own Licenses personal WorkSpaces.

Now that you have created a directory, you are ready to create a personal WorkSpace.

**To create a personal WorkSpace**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**, **Personal**.

1. Choose **Create WorkSpaces**.

1. For **Creation method**, choose **Configure manually**.

1. Under **Configure personal WorkSpace**, enter the following details:
   + For **Bundle type**, choose from the following the bundle type that you want to use for your WorkSpaces.
     + **Use a WorkSpaces bundle** – Choose one of the bundles from the drop down. For more information about the bundle type you selected, choose **Bundle details**. To compare available bundles, choose **Compare all bundles**.
     + **Use your own custom or BYOL bundle** – Choose a bundle that you previously created. To create a custom bundle, see [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md).
**Note**  
Review the recommended uses and specifications of each bundle to help ensure you select the bundle that works best for your users. For more information about each use case, see [Amazon WorkSpaces Bundles](https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). For more information about bundle specifications, recommended uses, and pricing, see [Amazon WorkSpaces pricing](https://aws.amazon.com/workspaces/pricing/).
   + For **Running mode**, choose from the following to configure your personal WorkSpace's availability and how you pay for it (monthly or hourly):
     + **AlwaysOn** – Your WorkSpace is always available and you pay a fixed monthly fee. This mode is best for users who use their WorkSpace full time as their primary desktop.
     + **AutoStop** – Your WorkSpace stops after a period of inactivity and you pay by the hour. You can configure how long the WorkSpace waits before it stops.

1. Under **User assignment**, enter the following details:
   + Choose the directory that you created. To create a directory, choose **Create directory**. For more information about creating personal directories, see [Register an existing Directory Service directory with WorkSpaces Personal](register-deregister-directory.md).
   + Choose the users from that directory you want to provision personal WorkSpaces for. To create users, do the following.

     1. Choose **Create user**.

     1. Enter the user's **Username**, **First name**, **Last name**, and **Email**. To add additional users, choose **Add another user** and enter their information. You can add up to 5 users at a time.

1. Under **Customization** (optional), you can customize volume sizes, root and user volume encryption, and nested virtualization.
   + To enable encryption for the root volume, user volume, or both, select the volumes under **Encryption**, and then select a KMS key. For more information, see [Encrypted WorkSpaces in WorkSpaces Personal](encrypt-workspaces.md).
   + To enable nested virtualization, expand **Nested virtualization** and select **Enable Nested Virtualization**. With nested virtualization, you can run hypervisors such as Hyper-V and KVM inside your WorkSpace. This enables tools like Docker Desktop and WSL2. For more information, see [Nested virtualization for WorkSpaces Personal](nested-virtualization.md).
**Note**  
Nested virtualization is available only on non-GPU bundles that use the DCV (WSP) protocol with a supported operating system. For the full list of supported configurations, see [Nested virtualization for WorkSpaces Personal](nested-virtualization.md).

1. Under **Tags** (optional), specify the key-value pairs that you want to use. A key can be a general category, such as "project," "owner," or "environment," with specific associated values.

1. Choose **Create WorkSpaces**. The initial status of the WorkSpace is `PENDING`. When the creation is complete, the status is `AVAILABLE` and an invitation is sent to the email address that you specified for the users.

1. Send invitations to the email address for each user. For more information, see [Send an invitation email](manage-workspaces-users.md#send-invitation).
**Note**  
These invitations aren't sent automatically if you're using AD Connector or a trust relationship.
Invitation emails aren't sent if the user already exists in Active Directory. Instead, make sure you manually send the user an invitation email. For more information, see [Send an invitation email](manage-workspaces-users.md#send-invitation).
In all Regions, the text of the invitation email is in English (US). In the following Regions, the English text is preceded by a second language:  
Asia Pacific (Seoul): Korean
Asia Pacific (Tokyo): Japanese
Canada (Central): French (Canadian)
China (Ningxia): Simplified Chinese

1. Proceed to [Connect to the WorkSpace](#connect-workspace-ad-connector).

## Connect to the WorkSpace
<a name="connect-workspace-ad-connector"></a>

You can connect to your WorkSpace using the client of your choice. After you sign in, the client displays the WorkSpace desktop.

**To connect to the WorkSpace**

1. Open the link in the invitation email.

1. Review [WorkSpaces Clients](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-clients.html) in the *Amazon WorkSpaces User Guide* for more information about the requirements for each client, and then do one of the following: 
   + When prompted, download one of the client applications or launch Web Access.
   + If you aren't prompted and you haven't installed a client application already, open [https://clients.amazonworkspaces.com/](https://clients.amazonworkspaces.com/) and download one of the client applications or launch Web Access.

1. Start the client, enter the registration code from the invitation email, and choose **Register**.

1. When prompted to sign in, enter the user's sign-in credentials, and then choose **Sign In**.

1. (Optional) When prompted to save your credentials, choose **Yes**.

**Note**  
Because you're using AD Connector, your users won't be able to reset their own passwords. (The **Forgot password?** option on the WorkSpaces client application login screen won't be available.) For information about how to reset user passwords, see [Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md).

## Next steps
<a name="next-steps-ad-connector"></a>

You can continue to customize the WorkSpace that you just created. For example, you can install software and then create a custom bundle from your WorkSpace. You can also perform various administrative tasks for your WorkSpaces and your WorkSpaces directory. If you are finished with your WorkSpace, you can delete it. For more information, see the following documentation.
+ [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md)
+ [Administer WorkSpaces Personal](administer-workspaces.md)
+ [Manage directories for WorkSpaces Personal](manage-workspaces-directory.md)
+ [Delete a WorkSpace in WorkSpaces Personal](delete-workspaces.md)

For more information about using the WorkSpaces client applications, such as setting up multiple monitors or using peripheral devices, see [WorkSpaces Clients](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-clients.html) and [Peripheral Device Support](https://docs.aws.amazon.com/workspaces/latest/userguide/peripheral_devices.html) in the *Amazon WorkSpaces User Guide*.