

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Create a configuration file
<a name="create-config"></a>

You can create a new configuration file.

**To create a new configuration file:**

1. In the navigation pane, choose **Network Settings**, and then choose **Client Configuration**.

1. Choose **Create New Config**.

1. On the **Create Configuration File** window, perform the following steps.

   1. Choose a security group from the **Security group** drop-down list.

   1. Choose the expiration period from the **Expiration period** drop-down list.

   1. Enter a password into the **Password** and **Repeat password** fields.

   1. Optionally, toggle **Generate auto configuration deeplink** to generate an auto configuration deeplink to take users to their installed Wickr Enterprise app when chosen.

   1. Choose the **Advanced** link to manually enter a certificate.
**Note**  
When you create a configuration file, the Wickr Admin Console disables pinning by not including any certificates in the certificates array of the resulting config file.

   1. Enter the **FQDN** or **IP address** of the server where your Wickr instance is hosted in the **Service host** field.

   1. Select the **Use certificate pinning** option to add a certificate to your Wickr app that will be used with every server request to turn Certificate Pinning on.

   1. Under **SSL certificate**, copy the contents of the SSL certificate.

1. Paste the contents of the SSL certificate in the load config file.

   1. In the navigation pane, choose **Network Settings**, and then choose **Security group**.

   1. Choose **Details**, for the security group you want to disable certificate pinning.

   1. Select the **Push Config** tab, then choose **Edit** under the **SSL Certificates** section.

   1. Paste the contents of the SSL certificate in the **Add New Certificate field**, then click **Save**.

   1. Optionally, choose **Add** to add multiple certificates.

1. On the **Create Configuration File **window, choose **Create**.

1. On the **Create Configuration File **pop-up window, choose **Done**.