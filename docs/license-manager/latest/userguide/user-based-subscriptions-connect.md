

# Connect to a user-based subscription instance with RDP
<a name="user-based-subscriptions-connect"></a>

Once you have associated users with the instance providing the product, they can connect to the instance if the **Health status** of the instance is **Active**. The users will need to connect with their user credentials for the domain to use the product with their associated identity.

**Important**  
The process of creating the EC2 instance and preparing it for users can take around 20 minutes. The **Association status** of the instance must be **Active** in order to access it and use the product.

**To connect to instances with a user-based subscription**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, under **User-based subscriptions**, choose **User association**.

1. On the **User association** page, confirm the instance’s **Health status** is **Active**.

1. Make note of the instance ID as you will need it to gather connection details.

1. Follow the steps listed in [Connect to your Windows instance using RDP](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html#connect-rdp) while ensuring to specify the fully qualified user name of the associated user.