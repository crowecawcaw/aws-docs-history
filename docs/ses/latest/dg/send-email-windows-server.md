

# Integrating Amazon SES with Microsoft Windows Server IIS SMTP

You can configure Microsoft Windows Server's IIS SMTP server to send email through Amazon SES. These instructions were written using Microsoft Windows Server 2022 on an Amazon EC2 instance. You can use the same configuration on Microsoft Windows Server 2016.

**Note**  
Windows Server is a third-party application, and isn't developed or supported by Amazon Web Services. The procedures in this section are provided for informational purposes only, and are subject to change without notice.

**To integrate the Microsoft Windows Server IIS SMTP server with Amazon SES**

1. First, set up Microsoft Windows Server 2022 using the following instructions.

   1. From the [Amazon EC2 management console](https://console.aws.amazon.com/ec2/home), launch a new Microsoft Windows Server 2022 Base Amazon EC2 instance.

   1. Connect to the instance and log into it using Remote Desktop by following the instructions in [Getting Started with Amazon EC2 Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2Win_GetStarted.html).

   1. Launch the Server Manager Dashboard.

   1. Install the **Web Server** role. Be sure to include the **IIS 10 Management Compatibility tools** (an option under the **Web Server** check box).

   1. Install the **SMTP Server** feature.

1. Next, configure the IIS SMTP service using the following instructions.

   1. Return to the Server Manager Dashboard.

   1. From the **Tools** menu, choose **Internet Information Services (IIS) 10.0 Manager**.

   1. Right-click **SMTP Virtual Server \#1** and then select **Properties**.

   1. On the **Access** tab, under **Relay Restrictions**, choose **Relay**.

   1. In the **Relay Restrictions** dialog box, choose **Add**.

   1. Under **Single Computer**, enter **127.0.0.1** for the IP address. You have now granted access for this server to relay email to Amazon SES through the IIS SMTP service.

      In this procedure, we assume that your emails are generated on this server. If the application that generates the email runs on a separate server, you must grant relaying access for that server in IIS SMTP.
**Note**  
To extend the SMTP relay to private subnets, for **Relay Restriction**, use **Single Computer** 127.0.0.1 and **Group of Computers** 172.1.1.0 - 255.255.255.0 (in the netmask section). For **Connection**, use **Single Computer** 127.0.0.1 and **Group of Computers** 172.1.1.0 - 255.255.255.0 (in the netmask section).

1. Finally, configure the server to send email through Amazon SES using the following instructions.

   1. Return to the **SMTP Virtual Server \#1 Properties** dialog box and then choose the **Delivery** tab.

   1. On the **Delivery** tab, choose **Outbound Security**.

   1. Select **Basic Authentication**. Enter the user name and password from your SMTP credentials.

   1. Ensure that **TLS encryption** is selected.

   1. Return to the **Delivery** tab.

   1. Choose **Outbound Connections**.

   1. In the **Outbound Connections** dialog box, set the port to `25` or `587`.
**Important**  
Amazon Elastic Compute Cloud (Amazon EC2) restricts outbound email traffic over port `25` by default. Request removal of the restriction, or use port `587`. For more information, see [How do I remove the restriction on port 25 from my Amazon EC2 instance or AWS Lambda function?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/) in the AWS Knowledge Center.

   1. Choose **Advanced**.

   1. For the **Smart host** name, enter the endpoint from your SMTP credentials.

   1. Return to the Server Manager Dashboard.

   1. On the Server Manager Dashboard, right-click **SMTP Virtual Server \#1** and then restart the service to pick up the new configuration.

   1. Send an email through this server. You can examine the message headers to confirm that it was delivered through Amazon SES.