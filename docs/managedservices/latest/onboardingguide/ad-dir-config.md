

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Active Directory name suffix routing
<a name="ad-dir-config"></a>

After the one-way forest trust has been established, please complete the additional steps.

1. Under **Start > All Programs > Administrative Tools**, click **Active Directory Domains and Trusts**.

   The Active Directory Domains and Trusts console opens.

1. Right-click your corporate domain and click **Properties**

   The Properties dialog for that domain opens.

1. Click the **Trusts** tab.

   The Trusts page opens.

1. Click the Amazon domain name and click **Properties**.

   The Properties page for the Amazon domain trust opens.

1. Click **Name Suffix Routing** and click **Refresh**.

   These steps ensure that the Service Principal Names (SPNs) can resolve over the trust.