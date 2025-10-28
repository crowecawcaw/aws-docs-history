# Active Directory name suffix routing

After the one-way forest trust has been established, complete the following steps to validate suffix routing:

1. Under **Start > All Programs > Administrative Tools**,
   click **Active Directory Domains and Trusts**.

The Active Directory Domains and Trusts console opens. 2. Right-click your corporate domain and click **Properties**

The Properties dialog for that domain opens. 3. Click the **Trusts** tab.

The Trusts page opens. 4. Click the Amazon domain name and click **Properties**.

The Properties page for the Amazon domain trust opens. 5. Click **Name Suffix Routing** and click **Refresh**.

Make sure there are no conflicts to ensure that the Service Principal Names (SPNs) can resolve over the trust.
