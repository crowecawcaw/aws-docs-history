# Launching an Amazon ECS Windows container instance

Your Amazon ECS container instances are created using the Amazon EC2 console. Before you begin, be
sure that you've completed the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").

For more information about the launch wizard, see [Launch an instance
using the new launch instance wizard](../../../AWSEC2/latest/WindowsGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/WindowsGuide/ec2-launch-instance-wizard.md") in the _Amazon EC2 User Guide_.

You can use the new Amazon EC2 wizard to launch an instance. You can use the following list
for the parameters and leave the parameters not listed as the default. The following
instructions take you through each parameter group.

## Procedure

Before you begin, complete the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, the current AWS Region
   is displayed (for example, US East (Ohio)). Select a Region
   in which to launch the instance. This choice is important because some Amazon EC2
   resources can be shared between Regions, while others can't.
3. From the Amazon EC2 console dashboard, choose **Launch
   instance**.

## Name and tags

The instance name is a tag, where the key is **Name**, and the
value is the name that you specify. You can tag the instance, the volumes, and
elastic graphics. For Spot Instances, you can tag the Spot Instance request only.

Specifying an instance name and additional tags is optional.

- For **Name**, enter a descriptive name for the instance.
  If you don't specify a name, the instance can be identified by its ID, which
  is automatically generated when you launch the instance.
- To add additional tags, choose **Add additional tags**.
  Choose **Add tag**, and then enter a key and value, and
  select the resource type to tag. Choose **Add tag** again
  for each additional tag to add.

## Application and OS Images (Amazon Machine Image)

An Amazon Machine Image (AMI) contains the information required to create an
instance. For example, an AMI might contain the software that's required to act as a
web server, such as Apache, and your website.

For the latest Amazon ECS-optimized AMIs and their values, see [Windows
Amazon ECS-optimized AMI](ecs-optimized_windows_AMI.md "ecs-optimized_windows_AMI.md").

Use the **Search** bar to find a suitable Amazon ECS-optimized AMI
published by AWS.

1. Based on your requirements, enter one of the following AMIs in the
   **Search** bar and press
   **Enter**.
   - Windows_Server-2022-English-Full-ECS_Optimized
   - Windows_Server-2022-English-Core-ECS_Optimized
   - Windows_Server-2019-English-Full-ECS_Optimized
   - Windows_Server-2019-English-Core-ECS_Optimized
   - Windows_Server-2016-English-Full-ECS_Optimized

2. On the **Choose an Amazon Machine Image (AMI)** page,
   select the **Community AMIs** tab.
3. From the list that appears, choose a Microsoft-verified AMI with the most
   recent publish date and click **Select**.

## Instance type

The instance type defines the hardware configuration and size of the instance.
Larger instance types have more CPU and memory. For more information, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md").

- For **Instance type**, select the instance type for the
  instance.

The instance type that you select determines the resources available for
your tasks to run on.

## Key pair (login)

For **Key pair name**, choose an existing key pair, or choose
**Create new key pair** to create a new one.

###### Important

If you choose the **Proceed without key pair (Not
recommended)** option, you won't be able to connect to the instance
unless you choose an AMI that is configured to allow users another way to log
in.

## Network settings

Configure the network settings, as necessary.

- **Networking platform**: Choose **Virtual Private
  Cloud (VPC)**, and then specify the subnet in the
  **Network interfaces** section.
- **VPC**: Select an existing VPC in which to create the
  security group.
- **Subnet**: You can launch an instance in a subnet
  associated with an Availability Zone, Local Zone, Wavelength Zone, or
  Outpost.

To launch the instance in an Availability Zone, select the subnet in which
to launch your instance. To create a new subnet, choose **Create new
subnet** to go to the Amazon VPC console. When you are done, return
to the launch instance wizard and choose the Refresh icon to load your
subnet in the list.

To launch the instance in a Local Zone, select a subnet that you created
in the Local Zone.

To launch an instance in an Outpost, select a subnet in a VPC that you
associated with the Outpost.

- **Auto-assign Public IP**: If your instance should be
  accessible from the internet, verify that the **Auto-assign Public
  IP** field is set to **Enable**. If not, set
  this field to **Disable**.

###### Note

Container instances need access to communicate with the Amazon ECS service
endpoint. This can be through an interface VPC endpoint or through your
container instances having public IP
addresses.

For more information about interface VPC endpoints, see [Amazon ECS interface VPC endpoints (AWS PrivateLink)](vpc-endpoints.md "vpc-endpoints.md")

If you do not have an interface VPC endpoint configured and your
container instances do not have
public IP addresses, then they must use network address translation
(NAT) to provide this access. For more information, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_ and [Using an HTTP proxy for Amazon ECS Linux container instances](http_proxy_config.md "http_proxy_config.md") in
this guide.

- **Firewall (security groups)**: Use a security group to
  define firewall rules for your container instance. These rules specify which
  incoming network traffic is delivered to your container instance. All other
  traffic is ignored.
  - To select an existing security group, choose **Select
    existing security group**, and select the security
    group that you created in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md")

## Configure storage

The AMI you selected includes one or more volumes of storage, including the root
volume. You can specify additional volumes to attach to the instance.

You can use the **Simple** view.

- **Storage type**: Configure the storage for your
  container instance.

If you are using the Amazon ECS-optimized Amazon Linux AMI, your instance has two volumes configured.
The **Root** volume is for the operating system's use, and the
second Amazon EBS volume (attached to `/dev/xvdcz`) is for
Docker's use.

You can optionally increase or decrease the volume sizes for your instance
to meet your application needs.

## Advanced details

For **Advanced details**, expand the section to view the fields
and specify any additional parameters for the instance.

- **Purchasing option**: Choose **Request Spot
  Instances** to request Spot Instances. You also need to set the other
  fields related to Spot Instances. For more information, see [Spot Instance Requests](../../../AWSEC2/latest/UserGuide/spot-requests.md "../../../AWSEC2/latest/UserGuide/spot-requests.md").

###### Note

If you are using Spot Instances and see a `Not
 available` message, you may need to choose a different
instance type.

.

- **IAM instance profile**: Select your container instance
  IAM role. This is usually named `ecsInstanceRole`.

###### Important

If you do not launch your container instance with the proper IAM
permissions, your Amazon ECS agent cannot connect to your cluster. For more
information, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").

- (Optional) **User data**: Configure your Amazon ECS container
  instance with user data, such as the agent environment variables from [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md"). Amazon EC2
  user data scripts are executed only one time, when the instance is first
  launched. The following are common examples of what user data is used
  for:
  - By default, your container instance launches into your default
    cluster. To launch into a non-default cluster, choose the
    **Advanced Details** list. Then, paste the
    following script into the **User data** field,
    replacing `your_cluster_name` with the name
    of your cluster.

  The `EnableTaskIAMRole` turns on the Task IAM roles
  feature for the tasks.

  In addition, the following options are available when you use the
  `awsvpc` network mode.

      - `EnableTaskENI`: This flag turns on task
       networking and is required when you use the
       `awsvpc` network mode.
      - `AwsvpcBlockIMDS`: This optional flag blocks
       IMDS access for the task containers running in the
       `awsvpc` network mode.
      - `AwsvpcAdditionalLocalRoutes`: This optional
       flag allows you to have additional routes in the task
       namespace.


      Replace `ip-address` with the IP Address for
       the additional routes, for example 172.31.42.23/32.

  ```
  <powershell>
  Import-Module ECSTools
  Initialize-ECSAgent -Cluster `your_cluster_name` -EnableTaskIAMRole -EnableTaskENI -AwsvpcBlockIMDS -AwsvpcAdditionalLocalRoutes
  '["`ip-address`"]'
  </powershell>
  ```
