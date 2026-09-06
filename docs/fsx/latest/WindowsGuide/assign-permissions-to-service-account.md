

# Delegating permissions to the Amazon FSx service account or group
<a name="assign-permissions-to-service-account"></a>

The Amazon FSx service account or admin group must have the [privileges necessary](self-managed-AD.md#service-account-prereqs) for it to join FSx for Windows File Server file systems to your self-managed Active Directory domain. To delegate these permissions, you can use either **Delegate Control** or **Advanced Features** in the Active Directory User and Computers MMC snap-in, as described in the following procedures.

## To assign permissions using **Delegate Control**
<a name="assign-permissions-delegate-control"></a>

**To assign permissions to a service account or group using **Delegate Control****

1. Log in to your system as a domain administrator for your Active Directory domain.

1. Open the **Active Directory User and Computers** MMC snap-in.

1. In the task pane, expand the domain node.

1. Locate and open the context (right-click) menu for the OU that you want to modify, and then choose **Delegate Control**.

1. On the **Delegation of Control Wizard** page, choose **Next**.

1. Choose **Add** to add the name of your Amazon FSx service account or group, and then choose **Next**.

1. On the **Tasks to Delegate** page, choose **Create a custom task to delegate**, and then choose **Next**.

1. Choose **Only the following objects in the folder**, and then choose **Computer objects**.

1. Choose **Create selected objects in this folder** and **Delete selected objects in this folder**. Then choose **Next**.

1. For **Permissions**, choose the following:
   + **Reset Password**
   + **Read and write Account Restrictions**
   + **Validated write to DNS host name**
   + **Validated write to service principal name**

1. Choose **Next**, and then choose **Finish**.

1. Close the **Active Directory User and Computers** MMC snap-in.

## To assign permissions using **Advanced Features**
<a name="assign-permissions-advanced-features"></a>

1. Log in to your system as a domain administrator for your Active Directory domain.

1. Open the **Active Directory User and Computers** MMC snap-in.

1. Select **View** from the menu bar and ensure that **Advanced Features** is enabled (a check mark will appear next to it if the feature is enabled).

1. In the task pane, expand the domain node.

1. Locate and open (right-click) the context menu for the OU that you want to modify, and then choose **Properties**.

1. In the **OU Properties** pane, select the **Security** tab.

1. In the **Security** tab, select **Advanced**. Then select **Add**.

1. On the **Permission Entry** page, choose **Select a principal** and enter the name of your Amazon FSx service account or group. For **Applies to:**, choose **This Object and all Descendant Computer**. Ensure that the following are selected:
   + **Modify permissions**
   + **Create Computer Objects**
   + **Delete Computer Objects**

1. Select **Apply**, and then select **OK**.

1. Close the **Active Directory User and Computers** MMC snap-in.