# Deploy standalone Remote Desktop Gateway into an existing VPC (Console)

The following steps guide you through a Remote Desktop Gateway deployment with AWS Launch Wizard after
you have launched it from the console.

1. When you select **Choose application** from the AWS Launch Wizard landing page, you
   are directed to the Choose application wizard where you are prompted to select the type of
   application that you want to deploy.
2. Select **Microsoft Remote Desktop Gateway**, select **Deploy into
   an existing VPC**, then select **Create deployment.**
3. You are prompted to enter the specifications for the new deployment. The following tabs
   provide information about the specification fields of the deployment model.

General

    * **Deployment name**. Enter a unique application name for
     your deployment.
    * **Amazon Simple Notification Service (SNS) topic ARN — optional**. Specify an
     Amazon SNS topic where AWS Launch Wizard can send notifications and alerts. For more information, see the
     [Amazon Simple Notification Service Developer
     Guide](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
    * **Deactivate rollback on failed deployment**. By default,
     if a deployment fails, your provisioned resources will be deleted. You can enable this
     setting during deployment to prevent this behavior.
    * **Tags - optional**. Enter a key and value to assign
     metadata to your deployment. For help with tagging, see [Tagging Your Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

Network configuration
**Key pair name**. Select an existing key pair from the
dropdown list or create a new one. If you select **Create new key pair
name**, you are directed to the Amazon EC2 console. From there, under **Network
and Security**, choose **Key Pairs**. Choose **Create a
new key pair**, enter a name for the key pair, and then choose **Download
Key Pair**.

###### Important

This is the only opportunity for you to save the private key file. Download it and save
it in a safe place. You must provide the name of your key pair when you launch an instance
and provide the corresponding private key each time that you connect to the instance. Return
to the Launch Wizard console and choose the refresh button next to the **Key Pairs**
dropdown list. The newly created key pair appears in the dropdown list. For more information
about key pairs, see [Amazon EC2 Key Pairs and Windows
Instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

**VPC Settings:**

    * **Select Virtual Private Cloud (VPC)** option. Choose the VPC that you
     want to use from the dropdown list. Your VPC must be associated at least two public subnets
     for HA deployments.



    ###### To add a new public subnet


    If a subnet's traffic is routed to an internet gateway, the subnet is known as a
     public subnet. If, however, a subnet doesn't have a route to the internet gateway, the
     subnet is known as a private subnet. To use an existing VPC that does not have a public
     subnet, you can add a new public subnet using the following steps.



    	+ Follow the steps in [Creating a Subnet in the Amazon VPC User Guide](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet") using the existing VPC you
    	 intend to use AWS Launch Wizard.
    	+ To add an internet gateway to your VPC, follow the steps in [Attaching an Internet Gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway") in the Amazon VPC User Guide.
    	+ To configure your subnets to route internet traffic through the internet gateway,
    	 follow the steps in [Creating a Custom Route Table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing") in the Amazon VPC User Guide. Use IPv4 format
    	 (0.0.0.0/0) for Destination.
    	+ The public subnet should have the “auto-assign public IPv4 address” setting enabled.
    	 To enable this setting, follow the steps in [Modifying the Public IPv4 Addressing Attribute for Your Subnet](../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip "../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip") in the
    	 Amazon VPC User Guide.
    * **Availability Zone (AZ) configuration:** You must choose
     at least two Availability Zones. The deployment will create a highly available architecture
     that spans these Availability Zones.
    * **Allowed Remote Desktop Gateway external access CIDR:**
     You must specify a CIDR block for allowing external RDP access to the Remote Desktop
     Gateways on TCP port 3389.

Microsoft Remote Desktop Gateway configuration

| Parameter label (name) | Default value        | Description                                                                                                      |
| ---------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of RDGW hosts   | 1                    | Enter the number of Remote Desktop Gateway hosts to create.                                                      |
| Admin user name        | StackAdmin           | User name for the new local administrator account.                                                               |
| Admin password         | **_Requires input_** | Password for the administrative account. Must be at least 8 characters containing letters, numbers, and symbols. | 4. When you are satisfied with your infrastructure selections, select **Next**. If you don't want to complete the configuration, select **Cancel**. When you select **Cancel**, all of the selections on the specification page are lost and you are returned to the landing page. To go to the previous screen, select **Previous**. 5. After configuring your application, you are prompted to define the infrastructure requirements for the new deployment on the **Define infrastructure requirements** page. The following tabs provide information about the input fields. Compute <br>• **Infrastructure requirements based on instance type**. You can choose to select your instances, or to use AWS recommended resources. If you choose to use AWS recommended resources, you have the option of defining your performance needs. If no selections are made, default values are assigned. <br>• **Number of instance cores**. Choose the number of CPU cores for your infrastructure. The default value assigned is 4. <br>• **Network performance**. Choose your preferred network performance in Gbps. <br>• **Memory (GB)**. Choose the amount of RAM that you want to attach to your EC2 instances. The default value assigned is 4 GB. <br>• **Recommended resources**. Launch Wizard displays the system-recommended resources based on your infrastructure selections. If you want to change the recommended resources, select different infrastructure requirements. <br>• **Infrastructure requirements based on instance type**. You can choose to select your instance or use AWS recommended resources. If no selections are made, default values are assigned. <br>• **Instance type**. Select your preferred instance type from the dropdown list. 6. When you are satisfied with your infrastructure selections, select **Next**. If you don't want to complete the configuration, select **Cancel**. When you select **Cancel**, all of the selections on the specification page are lost and you are returned to the landing page. To go to the previous screen, select **Previous**. 7. On the **Review and deploy** page, review your configuration details. If you want to make changes, select **Previous**. To stop, select **Cancel**. When you select **Cancel**, all of the selections on the specification page are lost and you are returned to the landing page. When you choose **Deploy**, you agree to the terms of the **Acknowledgment**. Launch Wizard validates the inputs and notifies you of any issues you must address. 8. When validation is complete, Launch Wizard deploys your AWS resources and configures your **Microsoft Remote Desktop Gateway** application. Launch Wizard provides you with status updates about the progress of the deployment on the **Deployments** page. From the **Deployments** page, you can view the list of current and previous deployments 9. When your deployment is ready, a notification informs you that your **Remote Desktop Gateway** application is successfully deployed. If you have set up an Amazon SNS notification, you are also alerted through Amazon SNS. You can manage and access all of the resources related to your application by selecting the deployment, and then selecting **Manage** from the **Actions** dropdown list. 10. When the application is deployed, you can access your EC2 instances through the Amazon EC2 console. |
