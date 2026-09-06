

# Enforcing Kerberos authentication using Group Policy Objects (GPOs)
<a name="enforce-kerberos"></a>

You can enforce Kerberos authentication when accessing the file system by setting the following Group Policy Objects (GPOs) in your Active Directory:
+ **Restrict NTLM: Outgoing NTLM traffic to remote servers** - Use this policy setting to deny or audit outgoing NTLM traffic from a computer to any remote server running the Windows operating system.
+ **Restrict NTLM: Add remote server exceptions for NTLM authentication** - Use this policy setting to create an exception list of remote servers to which client devices are allowed to use NTLM authentication if the *Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers* policy setting is configured.

1. Log on to a Windows instance joined to the Active Directory to which your Amazon FSx file system is joined as an administrator. If you are configuring a self-managed Active Directory, apply these steps directly to your Active Directory.

1. Choose **Start**, choose **Administrative Tools**, and then choose **Group Policy Management**.

1. Choose **Group Policy Objects**.

1. If your Group Policy Object does not already exist, create it.

1. Locate the existing **Network Security: Restrict NTLM: Outgoing NTLM traffic to remote servers** policy. (If there is no existing policy, create a new policy.) In the **Local security setting** tab, open the context (right-click) menu, and choose **Properties**.

1. Choose **Deny all**.

1. Choose **Apply** to save the security setting.

1. To set exceptions for NTLM connections to specific remote servers for the client, locate the **Network security: Restrict NTLM: Add remote server exceptions**.

   Open the context (right-click) menu, and choose **Properties** in the **Local security setting** tab.

1. Enter the names of any servers to add to the exception list.

1. Choose **Apply** to save the security setting.