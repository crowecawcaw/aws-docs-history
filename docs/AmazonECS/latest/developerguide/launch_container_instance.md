# Launching an Amazon ECS Linux container

instance

You can create Amazon ECS container instances using the Amazon EC2 console.

You can launch an instance by various methods including the Amazon EC2 console, AWS CLI, and SDK.
For information about the other methods for launching an instance, see [Launch your instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") in the _Amazon EC2 User Guide_.

For more information about the launch wizard, see [Launch an instance using
the new launch instance wizard](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md") in the _Amazon EC2 User Guide_.

Before you begin, complete the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").

You can use the new Amazon EC2 wizard to launch an instance. The launch instance wizard
specifies the launch parameters that are required for launching an instance.

###### Parameters for instance configuration

- [Procedure](#linux-liw-initiate-instance-launch "#linux-liw-initiate-instance-launch")
- [Name and tags](#linux-liw-name-and-tags "#linux-liw-name-and-tags")
- [Application and OS Images (Amazon Machine Image)](#linux-liw-ami "#linux-liw-ami")
- [Instance type](#linux-liw-instance-type "#linux-liw-instance-type")
- [Key pair (login)](#linux-liw-key-pair "#linux-liw-key-pair")
- [Network settings](#linux-liw-network-settings "#linux-liw-network-settings")
- [Configure storage](#linux-liw-storage "#linux-liw-storage")
- [Advanced details](#linux-liw-advanced-details "#linux-liw-advanced-details")

## Procedure

Before you begin, complete the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, the current AWS Region is
   displayed (for example, US East (Ohio)). Select a Region in which
   to launch the instance.
3. From the Amazon EC2 console dashboard, choose **Launch
   instance**.

## Name and tags

The instance name is a tag, where the key is **Name**, and the value
is the name that you specify. You can tag the instance, the volumes, and elastic
graphics. For Spot Instances, you can tag the Spot Instance request only.

Specifying an instance name and additional tags is optional.

- For **Name**, enter a descriptive name for the instance. If
  you don't specify a name, the instance can be identified by its ID, which is
  automatically generated when you launch the instance.
- To add additional tags, choose **Add additional tags**.
  Choose **Add tag**, and then enter a key and value, and select
  the resource type to tag. Choose **Add tag** again for each
  additional tag to add.

## Application and OS Images (Amazon Machine Image)

An Amazon Machine Image (AMI) contains the information required to create an instance.
For example, an AMI might contain the software that's required to act as a web server,
such as Apache, and your website.

Use the **Search** bar to find a suitable Amazon ECS-optimized AMI
published by AWS.

1. Enter one of the following terms in the **Search**
   bar.
   - `ami-ecs`
   - The **Value** of an Amazon ECS-optimized AMI.

   For the latest Amazon ECS-optimized AMIs and their values, see [Linux Amazon ECS-optimized AMI](ecs-optimized_AMI.md#ecs-optimized-ami-linux "ecs-optimized_AMI.md#ecs-optimized-ami-linux").

2. Press **Enter**.
3. On the **Choose an Amazon Machine Image (AMI)** page, select
   the **AWS Marketplace AMIs** tab.
4. From the left **Refine results** pane, select
   **Amazon Web Services** as the **Publisher**.
5. Choose **Select** on the row of the AMI that you want to
   use.

Alternatively, choose **Cancel** (at top right) to return to
the launch instance wizard without choosing an AMI. A default AMI will be
selected. Ensure that the AMI meets the requirements outlined in [Amazon ECS-optimized
Linux AMIs](ecs-optimized_AMI.md "ecs-optimized_AMI.md").

## Instance type

The instance type defines the hardware configuration and size of the instance. Larger
instance types have more CPU and memory. For more information, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the _Amazon EC2 User Guide_. If you want to
run an IPv6-only workload, certain instance types don't support IPv6 addresses. For more
information, see [IPv6
addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing") in the _Amazon EC2 User Guide_.

- For **Instance type**, select the instance type for the
  instance.

The instance type that you select determines the resources available for your
tasks to run on.

## Key pair (login)

For **Key pair name**, choose an existing key pair, or choose
**Create new key pair** to create a new one.

###### Important

If you choose the **Proceed without key pair (Not recommended)**
option, you won't be able to connect to the instance unless you choose an AMI that
is configured to allow users another way to log in.

## Network settings

Configure the network settings as necessary after choosing the
**Edit** button for the **Network settings**
section of the form.

- For **VPC**, choose the VPC that you want to launch the
  instance into. To run an IPv6-only workload, choose a dual stack VPC that
  includes both an IPv4 and an IPv6 CIDR block.
- For **Subnet**, choose the subnet to launch the instance in.
  You can launch an instance in a subnet associated with an Availability Zone,
  Local Zone, Wavelength Zone, or Outpost.

To launch the instance in an Availability Zone, select the subnet in which to
launch your instance. To create a new subnet, choose **Create new
subnet** to go to the Amazon VPC console. When you are done, return to
the launch instance wizard and choose the Refresh icon to load your subnet in
the list.

To launch the instance in a Local Zone, select a subnet that you created in
the Local Zone.

To launch an instance in an Outpost, select a subnet in a VPC that you
associated with the Outpost.

To run an IPv6-only workload, choose a subnet that includes only an IPv6 CIDR
block.

- **Auto-assign Public IP**: If your instance should be
  accessible from the internet, verify that the **Auto-assign Public
  IP** field is set to **Enable**. If not, set this
  field to **Disable**.

###### Note

Container instances need access to communicate with the Amazon ECS service
endpoint. This can be through an interface VPC endpoint or through your
container instances having public IP
addresses.

For more information about interface VPC endpoints, see [Amazon ECS interface VPC endpoints (AWS PrivateLink)](vpc-endpoints.md "vpc-endpoints.md")

If you do not have an interface VPC endpoint configured and your container
instances do not have public IP addresses, then they must use network
address translation (NAT) to provide this access. For more information, see
[NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in
the _Amazon VPC User Guide_ and [Using an HTTP proxy for Amazon ECS Linux container
instances](http_proxy_config.md "http_proxy_config.md") in this
guide.

- If you choose a dual stack VPC and an IPv6-only subnet, for
  **Auto-assign IPv6 IP**, choose
  **Enable**.
- **Firewall (security groups)**: Use a security group to
  define firewall rules for your container instance. These rules specify which
  incoming network traffic is delivered to your container instance. All other
  traffic is ignored.
  - To select an existing security group, choose **Select existing
    security group**, and select the security group that you
    created in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").

- If you are launching the instance for an IPv6-only workload, choose
  **Advanced network configuration**, and then for
  **Assign Primary IPv6 IP**, choose
  **Yes**.

###### Note

Without a primary IPv6 address, tasks running on the container instance in
the host or bridge network modes will fail to register with load balancers
or with AWS Cloud Map.

## Configure storage

The AMI you selected includes one or more volumes of storage, including the root
volume. You can specify additional volumes to attach to the instance.

You can use the **Simple** view.

- **Storage type**: Configure the storage for your container
  instance.

If you are using the Amazon ECS-optimized Amazon Linux 2 AMI, your instance has a single 30 GiB volume
configured, which is shared between the operating system and Docker.

If you are using the Amazon ECS-optimized AMI, your instance has two volumes
configured. The **Root** volume is for the operating system's
use, and the second Amazon EBS volume (attached to `/dev/xvdcz`)
is for Docker's use.

You can optionally increase or decrease the volume sizes for your instance to
meet your application needs.

## Advanced details

For **Advanced details**, expand the section to view the fields and
specify any additional parameters for the instance.

- **Purchasing option**: Choose **Request Spot
  Instances** to request Spot Instances. You also need to set the other fields
  related to Spot Instances. For more information, see [Spot Instance Requests](../../../AWSEC2/latest/UserGuide/spot-requests.md "../../../AWSEC2/latest/UserGuide/spot-requests.md").

###### Note

If you are using Spot Instances and see a `Not
 available` message, you may need to choose a different instance
type.

- **IAM instance profile**: Select your container instance
  IAM role. This is usually named `ecsInstanceRole`.

###### Important

If you do not launch your container instance with the proper IAM
permissions, your Amazon ECS agent cannot connect to your cluster. For more
information, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").

- **User data**: Configure your Amazon ECS container instance with
  user data, such as the agent environment variables from [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md"). Amazon EC2 user
  data scripts are executed only one time, when the instance is first launched.
  The following are common examples of what user data is used for:

      + By default, your container instance launches into your default
       cluster. To launch into a non-default cluster, choose the
       **Advanced Details** list. Then, paste the
       following script into the **User data** field,
       replacing `your_cluster_name` with the name of
       your cluster.



      ```
      #!/bin/bash
      echo ECS_CLUSTER=`your_cluster_name` >> /etc/ecs/ecs.config
      ```
      + If you have an `ecs.config` file in Amazon S3 and have
       enabled Amazon S3 read-only access to your container instance role, choose
       the **Advanced Details** list. Then, paste the
       following script into the **User data** field,
       replacing `your_bucket_name` with the name of
       your bucket to install the AWS CLI and write your configuration file at
       launch time.


      ###### Note

      For more information about this configuration, see [Storing Amazon ECS container instance configuration in Amazon S3](ecs-config-s3.md "ecs-config-s3.md").



      ```
      #!/bin/bash
      yum install -y aws-cli
      aws s3 cp s3://`your_bucket_name`/ecs.config /etc/ecs/ecs.config
      ```
      + Specify tags for your container instance using the
       `ECS_CONTAINER_INSTANCE_TAGS` configuration parameter.
       This creates tags that are associated with Amazon ECS only, they cannot be
       listed using the Amazon EC2 API.


      ###### Important

      If you launch your container instances using an Amazon EC2 Auto Scaling
       group, then you should use the ECS\_CONTAINER\_INSTANCE\_TAGS agent
       configuration parameter to add tags. This is due to the way in which
       tags are added to Amazon EC2 instances that are launched using Auto
       Scaling groups.



      ```
      #!/bin/bash
      cat <<'EOF' >> /etc/ecs/ecs.config
      ECS_CLUSTER=`your_cluster_name`
      ECS_CONTAINER_INSTANCE_TAGS={"`tag_key`": "`tag_value`"}
      EOF
      ```
      + Specify tags for your container instance and then use the
       `ECS_CONTAINER_INSTANCE_PROPAGATE_TAGS_FROM`
       configuration parameter to propagate them from Amazon EC2 to Amazon ECS


      The following is an example of a user data script that would propagate
       the tags associated with a container instance, as well as register the
       container instance with a cluster named
       `your_cluster_name`:



      ```
      #!/bin/bash
      cat <<'EOF' >> /etc/ecs/ecs.config
      ECS_CLUSTER=`your_cluster_name`
      ECS_CONTAINER_INSTANCE_PROPAGATE_TAGS_FROM=ec2_instance
      EOF
      ```
      + By default, the Amazon ECS container agent will try to detect the container
       instance's compatibility for an IPv6-only configuration by looking at the
       instance's default IPv4 and IPv6 routes. To override this behavior, you can set
       the  `ECS_INSTANCE_IP_COMPATIBILITY` parameter to `ipv4`
       or `ipv6` in the instance's `/etc/ecs/ecs.config` file.



      ```
      #!/bin/bash
      cat <<'EOF' >> /etc/ecs/ecs.config
      ECS_CLUSTER=`your_cluster_name`
      ECS_INSTANCE_IP_COMPATIBILITY=ipv6
      EOF
      ```

  For more information, see [Bootstrapping Amazon ECS Linux container instances to pass data](bootstrap_container_instance.md "bootstrap_container_instance.md").
