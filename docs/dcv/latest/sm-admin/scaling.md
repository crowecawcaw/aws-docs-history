# Scaling Session Manager

To enable high availability and improve performance, you can configure Session Manager to use multiple
Agents and Brokers. If you do intend to use multiple Agents and Brokers, we recommend that
you install and configure only one Agent and Broker host, create Amazon Machines Images
(AMI) from those hosts, and then launch the remaining hosts from the AMIs.

By default, Session Manager supports the use of multiple Agents without any additional configuration.
However, if you intend to use multiple Brokers, you must use a load balancer to balance the
traffic between the frontend client and the Brokers, and between the Brokers and the Agents.
Load balancer setup and configuration is entirely owned and managed by you.

The following section explains how to configure Session Manager to use multiple hosts with an
Application Load Balancer.

###### Steps

- [Step 1: Create an instance profile](#create-profile "#create-profile")
- [Step 2: Prepare the SSL certificate for the load balancer](#create-cert "#create-cert")
- [Step 3: Create the Broker application load balancer](#create-broker-alb "#create-broker-alb")
- [Step 4: Launch the Brokers](#launch-brokers "#launch-brokers")
- [Step 5: Create the Agent application load balancer](#create-agent-alb "#create-agent-alb")
- [Step 6: Launch the Agents](#launch-agents "#launch-agents")

## Step 1: Create an instance profile

You must attach an instance profile to the Broker and Agent hosts that give them permission to use the
Elastic Load Balancing APIs. For more information, see [IAM roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md")
in the _Amazon EC2 User Guide_.

###### To create an instance profile

1. Create an AWS Identity and Access Management (IAM) role that defines the permissions to use in the instance
   profile. Use the following trust policy:

JSON

```
`{
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
}`

```

Then attach the following policy:

JSON

```
`{
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
}`

```

For more information, see [Creating an IAM role](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-cli "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-cli") in the _IAM User Guide_. 2. Create a new instance profile. For more information, see [create-instance-profile](../../../cli/latest/reference/iam/create-instance-profile.md "../../../cli/latest/reference/iam/create-instance-profile.md")
in the _AWS CLI Command Reference_. 3. Add the IAM role to the instance profile. For more information, see [add-role-to-instance-profile](../../../cli/latest/reference/iam/add-role-to-instance-profile.md "../../../cli/latest/reference/iam/add-role-to-instance-profile.md")
in the _AWS CLI Command Reference_. 4. Attach the instance profile to the Broker hosts. For more information, see [Attaching an IAM role to an
instance](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role") in the _Amazon EC2 User Guide_.

## Step 2: Prepare the SSL certificate for the load balancer

When you use HTTPS for your load balancer listener, you must deploy an SSL certificate on your load
balancer. The load balancer uses this certificate to terminate the connection and decrypt requests from
clients before sending them to the targets.

###### To prepare the SSL certificate

1. Create a private certificate authority (CA) AWS Certificate Manager Private Certificate
   Authority (ACM PCA). For more information, see [Procedures
   for Creating a CA](../../../acm-pca/latest/userguide/PcaCreateCa.md#CA-procedures "../../../acm-pca/latest/userguide/PcaCreateCa.md#CA-procedures") in the AWS _Certificate Manager Private
   Certificate Authority User Guide_.
2. Install the CA. For more information, see [Installing a Root CA
   Certificate](../../../acm-pca/latest/userguide/PCACertInstall.md#InstallRoot "../../../acm-pca/latest/userguide/PCACertInstall.md#InstallRoot") in the AWS _Certificate Manager Private Certificate
   Authority User Guide_.
3. Request a new private certificate signed by the CA. For the domain name, use
   `*.`region`.elb.amazonaws.com` and specify the
   Region in which you intend to create the load balancer. For more information, see
   [Requesting a Private Certificate](../../../acm/latest/userguide/gs-acm-request-private.md#request-private-console "../../../acm/latest/userguide/gs-acm-request-private.md#request-private-console") in the AWS _Certificate
   Manager Private Certificate Authority User Guide_.

## Step 3: Create the Broker application load balancer

Create an application load balancer to balance the traffic between your front-end clients and the Brokers.

###### To create the load balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").

In the navigation pane, choose **Load Balancers** and then choose **Create Load Balancer**. For load balancer type, choose **Application Load Balancer**. 2. For **Step 1: Configure Load Balancer**, do the following:

    1. For **Name**, enter a descriptive name for the load balancer.
    2. For **Scheme**, select **internet-facing**.
    3. For **Load Balancer Protocol**, select **HTTPS**, and for **Load Balancer Port**, enter `8443`.
    4. For **VPC**, select the VPC to use and then select all of the subnets in that VPC.
    5. Choose **Next**.

3. For **Step 2: Configure Security Settings**, do the following:
   1. For **Certificate type**, choose **Choose a certificate from ACM**.
   2. For **Certificate name**, select the private certificate that you requested earlier.
   3. Choose **Next**.

4. For **Step 3: Configure Security Groups**, create a new security group, or select an existing security group that allows inbound and outbound traffic between your frontend client and the Brokers over HTTPS and port 8443.

Choose **Next**. 5. For **Step 4: Configure Routing**, do the following:

    1. For **Target group**, select **New target group**.
    2. For **Name**, enter a name for the target group.
    3. For **Target type**, choose **Instance**.
    4. For **Protocol**, select **HTTPS**. For **Port**, enter `8443`. For **Protocol version**, choose **HTTP1**.
    5. For the health check **Protocol**, choose HTTPS, and for
     **Path**, enter `/health`.
    6. Choose **Next**.

6. For **Step 5: Register Targets**, choose **Next**.
7. Choose **Create**.

## Step 4: Launch the Brokers

Create an initial Broker and configure it to use the load balancer, create an AMI from the Broker, and then use the AMI to launch the remaining Brokers.
This ensures that all of the Brokers are configure to use the same CA and the same load balancer configuration.

###### To launch the Brokers

1. Launch and configure the initial Broker host. For more information about installing and configuring
   the Broker, see [Step 2: Set up the Amazon DCV Session Manager broker](broker.md "broker.md").

###### Note

Broker's self signed certificate is not needed since we are using an application load balancer. 2. Connect to the Broker, open `/etc/dcv-session-manager-broker/session-manager-broker.properties`
using your preferred text editor, and do the following:

    1. Comment out the `broker-to-broker-discovery-addresses` parameter by placing a hash (#) at the start of the line.
    2. For `broker-to-broker-discovery-aws-region`, enter the Region in which you created the application load balancer.
    3. For `broker-to-broker-discovery-aws-alb-target-group-arn`, enter the ARN of the target group associated with the Broker load balancer.
    4. Save and close the file.

3. Stop the Broker instance.
4. Create an AMI from the stopped Broker instance. For more information, see [Creating a Linux AMI from an
   instance](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#how-to-create-ebs-ami "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#how-to-create-ebs-ami") in the _Amazon EC2 User Guide for Linux Instances_.
5. Use the AMI to launch the remaining Brokers.
6. Assign the instance profile that you created to all of the Broker instances.
7. Assign a security group which allows Broker to Broker and Broker to load balancer network traffic to all of the Broker instances.
   For more information about network ports, see [Broker Configuration File](broker-file.md "broker-file.md").
8. Register all of the Broker instances as targets for the Broker load balancer. For more information,
   see [Register targets with your target group](../../../elasticloadbalancing/latest/application/target-group-register-targets.md "../../../elasticloadbalancing/latest/application/target-group-register-targets.md") in the _User Guide for Application Load Balancers_.

## Step 5: Create the Agent application load balancer

Create an application load balancer to balance the Agents and the Brokers.

###### To create the load balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").

In the navigation pane, choose **Load Balancers** and then choose **Create Load Balancer**. For load balancer type, choose **Application Load Balancer**. 2. For **Step 1: Configure Load Balancer**, do the following:

    1. For **Name**, enter a descriptive name for the load balancer.
    2. For **Scheme**, select **internet-facing**.
    3. For **Load Balancer Protocol**, select **HTTPS**, and for **Load Balancer Port**, enter `8445`.
    4. For **VPC**, select the VPC to use and then select all of the subnets in that VPC.
    5. Choose **Next**.

3. For **Step 2: Configure Security Settings**, do the following:
   1. For **Certificate type**, choose **Choose a certificate from ACM**.
   2. For **Certificate name**, select the private certificate that you requested earlier.
   3. Choose **Next**.

4. For **Step 3: Configure Security Groups**, create a new security group, or select an existing security group that allows inbound and outbound traffic the Agents and the Brokers over HTTPS and port 8445.

Choose **Next**. 5. For **Step 4: Configure Routing**, do the following:

    1. For **Target group**, select **New target group**.
    2. For **Name**, enter a name for the target group.
    3. For **Target type**, choose **Instance**.
    4. For **Protocol**, select **HTTPS**. For **Port**, enter `8445`. For **Protocol version**, choose **HTTP1**.
    5. For the health check **Protocol**, choose **HTTPS**, and for
     **Path**, enter `/health`.
    6. Choose **Next**.

6. For **Step 5: Register Targets**, select all of the Broker instances and choose **Add to registered**. Choose **Next: Review**.
7. Choose **Create**.

## Step 6: Launch the Agents

Create an initial Agent and configure it to use the load balancer, create an AMI from the Agent, and then use the AMI to launch the remaining Agents.
This ensures that all of the Agents are configured to use the same load balancer configuration.

###### To launch the Agents

1. Prepare the Amazon DCV server. For more information, see [Step 1: Prepare the Amazon DCV servers](servers.md "servers.md").
2. Place a copy of the CA public key created in [Step 2: Prepare the SSL certificate for the load balancer](#create-cert "#create-cert").
   Choose or create a directory readable by any user. The CA public key file must be readable by any user as well.
3. Install and configure the Agent. For more information about installing and configuring the Agent, see [Step 3: Set up the Amazon DCV Session Manager agent](agent.md "agent.md").

###### Important

When modifying the Agent configuration file:

    * for the `broker_host` parameter, enter the Agent load balancer's DNS
    * for the `ca_file` parameter, enter the path to the CA public key file created in the previous step

4. Configure the Amazon DCV server to use the Broker as the authentication server. For more information, see [Step 4: Configure the Amazon DCV server to use the broker as the authentication server](configure-dcv-server.md "configure-dcv-server.md").

###### Important

When modifying the Amazon DCV server configuration file:

    * for the `ca-file` parameter, enter the same path to the CA public key file used in the previous step
    * for the `auth-token-verifier` parameter, use the Agent load balancer's DNS for `broker_ip_or_dns`

5. Stop the Agent instance.
6. Create an AMI from the stopped Agent instance. For more information, see [Creating a Linux AMI from an
   instance](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#how-to-create-ebs-ami "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#how-to-create-ebs-ami") in the _Amazon EC2 User Guide for Linux Instances_.
7. Use the AMI to launch the remaining Agents and assign the instance profile that you created to all of them.
8. Assign a security group which allows Agent to load balancer network traffic to all of the Agent instances.
   For more information about network ports, see [Agent Configuration File](agent-file.md "agent-file.md").
