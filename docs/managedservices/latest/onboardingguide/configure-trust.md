# Configure the trust

To configure the trust for your AWS Managed Services (AMS) account, follow this MicroSoft AD article
[Create a one-way, incoming, forest trust for one side of the trust](https://technet.microsoft.com/en-us/library/cc756735%28v=ws.10%29.aspx "https://technet.microsoft.com/en-us/library/cc756735%28v=ws.10%29.aspx"), using the settings and choices described in this section.

1. Open the **Start -> Administrative Tools -> Active Directory Domains and Trusts** dialog. Right-click the domain node
   for the domain that you want to establish a trust with, and then click **Properties -> Trusts -> New Trust** to open the
   New Trust Wizard. Enter the domain name provided to you by AMS for the **Trust Name** and press **Next**.
2. Under **Trust Type**, select **Forest Trust**. Press **Next**.
3. Under **Direction of Trust**, select **One-way: incoming**. Press **Next**.
4. Under **Sides of Trust**, select **This domain only**. Press **Next**.
5. Under **Trust Password**, type a password of your choosing. Press **Next**.
6. For **Trust Selections Completed** and **Trust Creation Complete**, just press **Next**.
7. Under **Confirm Incoming Trust**, select **No**, do not confirm the incoming trust. Press **Next**.
8. Under **Completed the New Trust Wizard**, select **Finish**, and then **OK** to close.
9. Provide the trust password (contact us via your CSDM's phone number for security reasons). AMS will complete the trust configuration.
