

# Step 1: Launch an Amazon EC2 instance
<a name="vpc-endpoints-tutorial.launch-ec2-instance"></a>

In this step, you launch an Amazon EC2 instance in your default Amazon VPC. You can then create and use a VPC endpoint for Amazon Keyspaces.

**To launch an Amazon EC2 instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Launch Instance** and do the following:

   From the EC2 console dashboard, in the **Launch instance** box, choose **Launch instance**, and then choose **Launch instance** from the options that appear.

   Under **Name and tags**, for **Name**, enter a descriptive name for your instance.

   Under **Application and OS Images (Amazon Machine Image)**:
   + Choose **Quick Start**, and then choose Ubuntu. This is the operating system (OS) for your instance. 
   + Under **Amazon Machine Image (AMI)**, you can use the default image that is marked as **Free tier eligible**. An *Amazon Machine Image (AMI)* is a basic configuration that serves as a template for your instance.

   Under **Instance Type**:
   + From the **Instance type** list, choose the **t2.micro** instance type, which is selected by default.

   Under **Key pair (login)**, for **Key pair name**, choose one of the following options for this tutorial:
   + If you don't have an Amazon EC2 key pair, choose **Create a new key pair** and follow the instructions. You will be asked to download a private key file (*.pem* file). You will need this file later when you log in to your Amazon EC2 instance, so take note of the file path.
   + If you already have an existing Amazon EC2 key pair, go to **Select a key pair** and choose your key pair from the list. You must already have the private key file ( *.pem* file) available in order to log in to your Amazon EC2 instance.

   Under **Network Settings**:
   + Choose **Edit**. 
   + Choose **Select an existing security group**.
   + In the list of security groups, choose **default**. This is the default security group for your VPC.

   Continue to **Summary**.
   + Review a summary of your instance configuration in the **Summary** panel. When you're ready, choose **Launch instance**.

1. On the completion screen for the new Amazon EC2 instance, choose the **Connect to instance** tile. The next screen shows the necessary information and the required steps to connect to your new instance. Take note of the following information:
   + The sample command to protect the key file
   + The connection string
   + The **Public IPv4 DNS** name

   After taking note of the information on this page, you can continue to the next step in this tutorial ([Step 2: Configure your Amazon EC2 instance](vpc-endpoints-tutorial.configure-ec2-instance.md)).

**Note**  
It takes a few minutes for your Amazon EC2 instance to become available. Before you go on to the next step, ensure that the **Instance State** is `running` and that all of its **Status Checks** have passed.