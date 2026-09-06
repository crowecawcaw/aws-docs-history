

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Logging in to your Amazon EC2 gateway local console
<a name="EC2_MaintenanceConsoleWindow-fgw"></a>

You log in to the gateway local console on an Amazon EC2 instance by using a Secure Shell (SSH) client. For detailed information, see [Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide*. To connect this way, you need the SSH key pair that you specified when you launched your instance. For information about Amazon EC2 key pairs, see [Amazon EC2 key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide.*<a name="EC2_MaintenanceConsoleWindowMenu-fgw"></a>

**To log in to the gateway local console**

1. Connect to the Amazon EC2 instance using SSH and log in as the *admin* user.

1. After you log in, you see the **AWS Appliance Activation - Configuration** main menu, from which you can perform various tasks.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceConsoleWindow-fgw.html)

To shut down the gateway, enter **0**.

To exit the configuration session, enter **X**.