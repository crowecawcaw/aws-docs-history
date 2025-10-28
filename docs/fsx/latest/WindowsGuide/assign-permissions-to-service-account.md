# Delegating permissions to the Amazon FSx service account or group

The Amazon FSx service account or admin group must have the [privileges necessary](self-managed-AD.md#service-account-prereqs "self-managed-AD.md#service-account-prereqs") for it to join FSx for Windows File Server file systems
to your self-managed Active Directory domain. To delegate these permissions, you can use either **Delegate Control**
or **Advanced Features** in the Active Directory User and Computers MMC snap-in, as described in the
following procedures.

###### To assign permissions to a service account or group using **Delegate Control**

1. Log in to your system as a domain administrator for your Active Directory domain.
2. Open the **Active Directory User and Computers** MMC snap-in.
3. In the task pane, expand the domain node.
4. Locate and open the context (right-click) menu for the OU that you want to modify, and
   then choose **Delegate Control**.
5. On the **Delegation of Control Wizard** page,
   choose **Next**.
6. Choose **Add** to add the name of your Amazon FSx service account or group, and then choose **Next**.
7. On the **Tasks to Delegate** page, choose **Create a custom task
   to delegate**, and then choose **Next**.
8. Choose **Only the following objects in the folder**, and then choose
   **Computer objects**.
9. Choose **Create selected objects in this folder** and **Delete
   selected objects in this folder**. Then choose **Next**.
10. For **Permissions**, choose the following:
    - **Reset Password**
    - **Read and write Account Restrictions**
    - **Validated write to DNS host name**
    - **Validated write to service principal name**

11. Choose **Next**, and then choose **Finish**.
12. Close the **Active Directory User and Computers** MMC snap-in.
13. Log in to your system as a domain administrator for your Active Directory domain.
14. Open the **Active Directory User and Computers** MMC snap-in.
15. Select **View** from the menu bar and ensure that **Advanced Features** is enabled
    (a check mark will appear next to it if the feature is enabled).
16. In the task pane, expand the domain node.
17. Locate and open (right-click) the context menu for the OU that you want to modify, and
    then choose **Properties**.
18. In the **OU Properties** pane,
    select the **Security** tab.
19. In the **Security** tab,
    select **Advanced**. Then select **Add**.
20. On the **Permission Entry** page, choose **Select a principal** and enter the name of your Amazon FSx service account or group.
    For **Applies to:**, choose
    **This Object and all Descendant Computer**. Ensure that the following are selected:
    - **Modify permissions**
    - **Create Computer Objects**
    - **Delete Computer Objects**

21. Select **Apply**, and then select **OK**.
22. Close the **Active Directory User and Computers** MMC snap-in.
