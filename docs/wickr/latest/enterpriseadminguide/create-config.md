This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Create a configuration file

You can create a new configuration file.

**To create a new configuration file:**

1. In the navigation pane, choose **Network Settings**, and then choose
   **Client Configuration**.
2. Choose **Create New Config**.
3. On the **Create Configuration File** window, perform the following
   steps.
   1. Choose a security group from the **Security group** drop-down
      list.
   2. Choose the expiration period from the **Expiration period** drop-down
      list.
   3. Enter a password into the **Password** and **Repeat
      password** fields.
   4. Optionally, toggle **Generate auto configuration deeplink** to
      generate an auto configuration deeplink to take users to their installed Wickr Enterprise
      app when chosen.
   5. Choose the **Advanced** link to manually enter a certificate.

   ###### Note

   When you create a configuration file, the Wickr Admin Console disables pinning by
   not including any certificates in the certificates array of the resulting config
   file. 6. Enter the **FQDN** or **IP address** of the server
   where your Wickr instance is hosted in the **Service host** field. 7. Select the **Use certificate pinning** option to add a certificate to
   your Wickr app that will be used with every server request to turn Certificate Pinning
   on. 8. Under **SSL certificate**, copy the contents of the SSL
   certificate.

4. Paste the contents of the SSL certificate in the load config file.
   1. In the navigation pane, choose **Network Settings**, and then choose
      **Security group**.
   2. Choose **Details**, for the security group you want to disable
      certificate pinning.
   3. Select the **Push Config** tab, then choose **Edit**
      under the **SSL Certificates** section.
   4. Paste the contents of the SSL certificate in the **Add New Certificate
      field**, then click **Save**.
   5. Optionally, choose **Add** to add multiple certificates.

5. On the **Create Configuration File** window, choose
   **Create**.
6. On the **Create Configuration File** pop-up window, choose
   **Done**.
