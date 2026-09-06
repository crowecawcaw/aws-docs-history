

# Scaling Session Manager
<a name="scaling"></a>

To enable high availability and improve performance, you can configure Session Manager to use multiple Agents and Brokers. If you do intend to use multiple Agents and Brokers, we recommend that you install and configure only one Agent and Broker host, create Amazon Machines Images (AMI) from those hosts, and then launch the remaining hosts from the AMIs.

By default, Session Manager supports the use of multiple Agents without any additional configuration. However, if you intend to use multiple Brokers, you must use a load balancer to balance the traffic between the frontend client and the Brokers, and between the Brokers and the Agents. Load balancer setup and configuration is entirely owned and managed by you.

The following section explains how to configure Session Manager to use multiple hosts with an Application Load Balancer.

**Topics**
+ [Step 1: Create an instance profile](#create-profile)
+ [Step 2: Prepare the SSL certificate for the load balancer](#create-cert)
+ [Step 3: Create the Broker application load balancer](#create-broker-alb)
+ [Step 4: Launch the Brokers](#launch-brokers)
+ [Step 5: Create the Agent application load balancer](#create-agent-alb)
+ [Step 6: Launch the Agents](#launch-agents)

## Step 1: Create an instance profile
<a name="create-profile"></a>

You must attach an instance profile to the Broker and Agent hosts that give them permission to use the Elastic Load Balancing APIs. For more information, see [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the *Amazon EC2 User Guide*.

**To create an instance profile**

1. Create an AWS Identity and Access Management (IAM) role that defines the permissions to use in the instance profile. Use the following trust policy:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "ec2.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

   Then attach the following policy:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Action": [
           "ec2:DescribeInstances"
         ],
         "Effect": "Allow",
         "Resource": "*"
       },
       {
         "Action": [
           "elasticloadbalancing:DescribeTargetHealth"
         ],
         "Effect": "Allow",
         "Resource": "*"
       }
     ]
   }
   ```

------

   For more information, see [ Creating an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html#roles-creatingrole-user-cli) in the *IAM User Guide*.

1. Create a new instance profile. For more information, see [create-instance-profile](https://docs.aws.amazon.com/cli/latest/reference/iam/create-instance-profile.html) in the *AWS CLI Command Reference*.

1. Add the IAM role to the instance profile. For more information, see [add-role-to-instance-profile](https://docs.aws.amazon.com/cli/latest/reference/iam/add-role-to-instance-profile.html) in the *AWS CLI Command Reference*.

1. Attach the instance profile to the Broker hosts. For more information, see [Attaching an IAM role to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role) in the *Amazon EC2 User Guide*.

## Step 2: Prepare the SSL certificate for the load balancer
<a name="create-cert"></a>

When you use HTTPS for your load balancer listener, you must deploy an SSL certificate on your load balancer. The load balancer uses this certificate to terminate the connection and decrypt requests from clients before sending them to the targets.

**To prepare the SSL certificate**

1. Create a private certificate authority (CA) AWS Certificate Manager Private Certificate Authority (ACM PCA). For more information, see [Procedures for Creating a CA](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaCreateCa.html#CA-procedures) in the AWS *Certificate Manager Private Certificate Authority User Guide*.

1. Install the CA. For more information, see [Installing a Root CA Certificate](https://docs.aws.amazon.com/acm-pca/latest/userguide/PCACertInstall.html#InstallRoot) in the AWS *Certificate Manager Private Certificate Authority User Guide*. 

1. Request a new private certificate signed by the CA. For the domain name, use `*.{{region}}.elb.amazonaws.com` and specify the Region in which you intend to create the load balancer. For more information, see [ Requesting a Private Certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html#request-private-console) in the AWS *Certificate Manager Private Certificate Authority User Guide*.

## Step 3: Create the Broker application load balancer
<a name="create-broker-alb"></a>

Create an application load balancer to balance the traffic between your front-end clients and the Brokers.

**To create the load balancer**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   In the navigation pane, choose **Load Balancers** and then choose **Create Load Balancer**. For load balancer type, choose **Application Load Balancer**.

1. For **Step 1: Configure Load Balancer**, do the following:

   1. For **Name**, enter a descriptive name for the load balancer.

   1. For **Scheme**, select **internet-facing**.

   1. For **Load Balancer Protocol**, select **HTTPS**, and for **Load Balancer Port**, enter `8443`.

   1. For **VPC**, select the VPC to use and then select all of the subnets in that VPC.

   1. Choose **Next**.

1. For **Step 2: Configure Security Settings**, do the following:

   1. For **Certificate type**, choose **Choose a certificate from ACM**.

   1. For **Certificate name**, select the private certificate that you requested earlier.

   1. Choose **Next**.

1. For **Step 3: Configure Security Groups**, create a new security group, or select an existing security group that allows inbound and outbound traffic between your frontend client and the Brokers over HTTPS and port 8443.

   Choose **Next**.

1. For **Step 4: Configure Routing**, do the following:

   1. For **Target group**, select **New target group**.

   1. For **Name**, enter a name for the target group.

   1. For **Target type**, choose **Instance**.

   1. For **Protocol**, select **HTTPS**. For **Port**, enter `8443`. For **Protocol version**, choose **HTTP1**.

   1. For the health check **Protocol**, choose HTTPS, and for **Path**, enter `/health`.

   1. Choose **Next**.

1. For **Step 5: Register Targets**, choose **Next**.

1. Choose **Create**.

## Step 4: Launch the Brokers
<a name="launch-brokers"></a>

Create an initial Broker and configure it to use the load balancer, create an AMI from the Broker, and then use the AMI to launch the remaining Brokers. This ensures that all of the Brokers are configure to use the same CA and the same load balancer configuration.

**To launch the Brokers**

1. Launch and configure the initial Broker host. For more information about installing and configuring the Broker, see [Step 2: Set up the Amazon DCV Session Manager broker](broker.md).
**Note**  
Broker's self signed certificate is not needed since we are using an application load balancer.

1. Connect to the Broker, open `/etc/dcv-session-manager-broker/session-manager-broker.properties` using your preferred text editor, and do the following:

   1. Comment out the `broker-to-broker-discovery-addresses` parameter by placing a hash (\#) at the start of the line.

   1. For `broker-to-broker-discovery-aws-region`, enter the Region in which you created the application load balancer.

   1. For `broker-to-broker-discovery-aws-alb-target-group-arn`, enter the ARN of the target group associated with the Broker load balancer.

   1. Save and close the file.

1. Stop the Broker instance.

1. Create an AMI from the stopped Broker instance. For more information, see [ Creating a Linux AMI from an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html#how-to-create-ebs-ami) in the *Amazon EC2 User Guide for Linux Instances*.

1. Use the AMI to launch the remaining Brokers.

1. Assign the instance profile that you created to all of the Broker instances.

1. Assign a security group which allows Broker to Broker and Broker to load balancer network traffic to all of the Broker instances. For more information about network ports, see [Broker Configuration File](https://docs.aws.amazon.com/dcv/latest/sm-admin/broker-file.html).

1. Register all of the Broker instances as targets for the Broker load balancer. For more information, see [ Register targets with your target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html) in the *User Guide for Application Load Balancers*.

## Step 5: Create the Agent application load balancer
<a name="create-agent-alb"></a>

Create an application load balancer to balance the Agents and the Brokers.

**To create the load balancer**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   In the navigation pane, choose **Load Balancers** and then choose **Create Load Balancer**. For load balancer type, choose **Application Load Balancer**.

1. For **Step 1: Configure Load Balancer**, do the following:

   1. For **Name**, enter a descriptive name for the load balancer.

   1. For **Scheme**, select **internet-facing**.

   1. For **Load Balancer Protocol**, select **HTTPS**, and for **Load Balancer Port**, enter `8445`.

   1. For **VPC**, select the VPC to use and then select all of the subnets in that VPC.

   1. Choose **Next**.

1. For **Step 2: Configure Security Settings**, do the following:

   1. For **Certificate type**, choose **Choose a certificate from ACM**.

   1. For **Certificate name**, select the private certificate that you requested earlier.

   1. Choose **Next**.

1. For **Step 3: Configure Security Groups**, create a new security group, or select an existing security group that allows inbound and outbound traffic the Agents and the Brokers over HTTPS and port 8445.

   Choose **Next**.

1. For **Step 4: Configure Routing**, do the following:

   1. For **Target group**, select **New target group**.

   1. For **Name**, enter a name for the target group.

   1. For **Target type**, choose **Instance**.

   1. For **Protocol**, select **HTTPS**. For **Port**, enter `8445`. For **Protocol version**, choose **HTTP1**.

   1. For the health check **Protocol**, choose **HTTPS**, and for **Path**, enter `/health`.

   1. Choose **Next**.

1. For **Step 5: Register Targets**, select all of the Broker instances and choose **Add to registered**. Choose **Next: Review**.

1. Choose **Create**.

## Step 6: Launch the Agents
<a name="launch-agents"></a>

Create an initial Agent and configure it to use the load balancer, create an AMI from the Agent, and then use the AMI to launch the remaining Agents. This ensures that all of the Agents are configured to use the same load balancer configuration.

**To launch the Agents**

1. Prepare the Amazon DCV server. For more information, see [Step 1: Prepare the Amazon DCV servers](servers.md).

1. Place a copy of the CA public key created in [Step 2: Prepare the SSL certificate for the load balancer](#create-cert). Choose or create a directory readable by any user. The CA public key file must be readable by any user as well.

1. Install and configure the Agent. For more information about installing and configuring the Agent, see [Step 3: Set up the Amazon DCV Session Manager agent](agent.md).
**Important**  
When modifying the Agent configuration file:  
for the `broker_host` parameter, enter the Agent load balancer's DNS
for the `ca_file` parameter, enter the path to the CA public key file created in the previous step

1. Configure the Amazon DCV server to use the Broker as the authentication server. For more information, see [Step 4: Configure the Amazon DCV server to use the broker as the authentication server](configure-dcv-server.md).
**Important**  
When modifying the Amazon DCV server configuration file:  
for the `ca-file` parameter, enter the same path to the CA public key file used in the previous step
for the `auth-token-verifier` parameter, use the Agent load balancer's DNS for {{broker\_ip\_or\_dns}}

1. Stop the Agent instance.

1. Create an AMI from the stopped Agent instance. For more information, see [ Creating a Linux AMI from an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html#how-to-create-ebs-ami) in the *Amazon EC2 User Guide for Linux Instances*.

1. Use the AMI to launch the remaining Agents and assign the instance profile that you created to all of them.

1. Assign a security group which allows Agent to load balancer network traffic to all of the Agent instances. For more information about network ports, see [Agent Configuration File](https://docs.aws.amazon.com/dcv/latest/sm-admin/agent-file.html).