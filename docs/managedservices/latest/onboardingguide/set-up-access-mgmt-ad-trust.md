

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Establish an Active Directory Trust
<a name="set-up-access-mgmt-ad-trust"></a>

To set up a trust, AMS requires your domain controller **Local Policies -> Security Options -> Network Access: Named Pipes that can be accessed anonymously**, have the **Netlogon** and **lsarpc** pipes listed. These pipes are listed by default, but are sometimes removed for security concerns. Once the trust is established, they can be removed from the list again.