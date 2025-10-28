# Tutorial: Complete the configuration

required to connect to your instance using EC2 Instance Connect

To connect to your instance using EC2 Instance Connect in the Amazon EC2 console, you first need
to complete the prerequisite configuration that will allow you to successfully connect
to your instance. The purpose of this tutorial is to guide you through the tasks to
complete the prerequisite configuration.

**Tutorial overview**

In this tutorial, you'll complete the following four tasks:

- [Task 1: Grant permissions required to use
  EC2 Instance Connect](#eic-tut1-task1 "#eic-tut1-task1")

First you'll create an IAM policy that contains the IAM permissions that allow
you to push a public key to the instance metadata. You'll attach this policy to
your IAM identity (user, user group, or role) so that your IAM identity gets
these permissions.

- [Task 2: Allow inbound traffic from the
  EC2 Instance Connect service to your instance](#eic-tut1-task2 "#eic-tut1-task2")

Then you'll create a security group that allows traffic from the EC2 Instance Connect
service to your instance. This is required when you use EC2 Instance Connect in the
Amazon EC2 console to connect to your instance.

- [Task 3: Launch your instance](#eic-tut1-task3 "#eic-tut1-task3")

You'll then launch an EC2 instance using an AMI that is pre-installed with
EC2 Instance Connect and you'll add the security group that you created in the previous
step.

- [Task 4: Connect to your instance](#eic-tut1-task4 "#eic-tut1-task4")

Finally, you'll use EC2 Instance Connect in the Amazon EC2 console to connect to your
instance. If you can connect, then you can be sure that the prerequisite
configuration you completed in Tasks 1, 2, and 3 were successful.

## Task 1: Grant permissions required to use

EC2 Instance Connect

When you connect to an instance using EC2 Instance Connect, the EC2 Instance Connect API pushes
an SSH public key to the [instance
metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") where it remains for 60 seconds. You need an IAM policy
attached to your IAM identity (user, user group, or role) to grant you the required
permission to push the public key to the instance metadata.

**Task objective**

You'll create the IAM policy that grants the permission to push the public key to
the instance. The specific action to allow is
`ec2-instance-connect:SendSSHPublicKey`. You must also allow the
`ec2:DescribeInstances` action so that you can view and select your
instance in the Amazon EC2 console.

After you've created the policy, you'll attach the policy to your IAM identity
(user, user group, or role) so that your IAM identity gets the permissions.

You'll create a policy that is configured as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "ec2-instance-connect:SendSSHPublicKey",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeInstances",
 "Resource": "*"
 }
 ]
}`

```

###### Important

The IAM policy created in this tutorial is a highly permissive policy; it
allows you to connect to any instance using any AMI username. We're using this
highly permissive policy to keep the tutorial simple and focused on the specific
configurations that this tutorial is teaching. However, in a production
environment, we recommend that your IAM policy is configured to provide [least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"). For example IAM policies, see [Grant IAM permissions for
EC2 Instance Connect](ec2-instance-connect-configure-IAM-role.md "ec2-instance-connect-configure-IAM-role.md").

###### To create and attach an IAM policy that allows you to use EC2 Instance Connect to

connect to your instances

1. **First create the IAM policy**
   1. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. In the navigation pane, choose
      **Policies**.
   3. Choose **Create policy**.
   4. On the **Specify permission** page, do the
      following:
      1. For **Service**, choose **EC2
         Instance Connect**.
      2. Under **Actions allowed**, in the search
         field start typing `send` to show the
         relevant actions, and then select
         **SendSSHPublicKey**.
      3. Under **Resources**, choose
         **All**. For a production environment,
         we recommend specifying the instance by its ARN, but for
         this tutorial, you're allowing all instances.
      4. Choose **Add more permissions**.
      5. For **Service**, choose
         **EC2**.
      6. Under **Actions allowed**, in the search
         field start typing `describein` to show
         the relevant actions, and then select
         **DescribeInstances**.
      7. Choose **Next**.

   5. On the **Review and create** page, do the
      following:
      1. For **Policy name**, enter a name for the
         policy.
      2. Choose **Create policy**.

2. **Then attach the policy to your
   identity**
   1. In the IAM console, in the navigation pane, choose
      **Policies**.
   2. In the list of policies, select the option button next to the name
      of the policy you created. You can use the search box to filter the
      list of policies.
   3. Choose **Actions**,
      **Attach**.
   4. Under **IAM entities**, select the checkbox next to your identity
      (user, user group, or role). You can use the search box to filter
      the list of entities.
   5. Choose **Attach policy**.

![This animation shows how to create an IAM policy. For the text version of this animation, see the steps in the preceding procedure.](images/eic-tut1-task1-create-iam-policy.gif)

![This animation shows how to attach an IAM policy to an IAM identity. For the text version of this animation, see the steps in the preceding procedure.](images/eic-tut1-task1-attach-iam-policy.gif)

## Task 2: Allow inbound traffic from the

EC2 Instance Connect service to your instance

When you use EC2 Instance Connect in the Amazon EC2 console to connect to an instance, the
traffic that must be allowed to reach the instance is traffic from the EC2 Instance Connect
service. This is different to connecting from your local computer to an instance; in
that case, you must allow traffic from your local computer to your instance. To
allow traffic from the EC2 Instance Connect service, you must create a security group that
allows inbound SSH traffic from the IP address range for the EC2 Instance Connect
service.

AWS uses prefix lists to manage IP address ranges. The names of the EC2 Instance Connect prefix
lists are as follows, with `region` replaced by the Region
code:

- IPv4 prefix list name:
  `com.amazonaws.`region`.ec2-instance-connect`
- IPv6 prefix list name:
  `com.amazonaws.`region`.ipv6.ec2-instance-connect`

**Task objective**

You'll create a security group that allows inbound SSH traffic on port 22 from the IPv4
prefix list in the Region in which your instance is located.

###### To create a security group that allows inbound traffic from the EC2 Instance Connect

service to your instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security
   Groups**.
3. Choose **Create security group**.
4. Under **Basic details**, do the following:
   1. For **Security group name**, enter a meaningful
      name for your security group.
   2. For **Description**, enter a meaningful
      description for your security group.

5. Under **Inbound rules**, do the following:
   1. Choose **Add rule**.
   2. For **Type**, choose
      **SSH**.
   3. For **Source**, leave
      **Custom**.
   4. In the field next to **Source**, select the
      prefix list for EC2 Instance Connect.

   For example, if your instance is located in the US East (N. Virginia)
   (`us-east-1`) Region and your users will connect to
   its public IPv4 address, choose the following prefix list:
   **com.amazonaws.us-east-1.ec2-instance-connect**

6. Choose **Create security group**.

![This animation shows how to configure a security group. For the text version of this animation, see the steps in the preceding procedure.](images/tut1-task2-eic-security-group.gif)

## Task 3: Launch your instance

When you launch an instance, you must specify an AMI that contains the information
required to launch the instance. You can choose to launch an instance with or
without EC2 Instance Connect pre-installed. In this task, we specify an AMI that comes
pre-installed with EC2 Instance Connect.

If you launch your instance without EC2 Instance Connect pre-installed, and you want to
use EC2 Instance Connect to connect to your instance, you'll need to perform additional
configuration steps. These steps are outside the scope of this tutorial.

**Task objective**

You'll launch an instance with the Amazon Linux 2023 AMI, which comes pre-installed
with EC2 Instance Connect. You'll also specify the security group that you created earlier
so that you can use EC2 Instance Connect in the Amazon EC2 console to connect to your instance.
Because you'll use EC2 Instance Connect to connect to your instance, which pushes a public
key to your instance's metadata, you won't need to specify an SSH key when you
launch your instance.

###### To launch an instance that can use EC2 Instance Connect in the Amazon EC2 console for

connection

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, the current AWS Region
   is displayed (for example, **Ireland**). Select a Region in
   which to launch your instance. This choice is important because you created
   a security group that allows traffic for a specific Region, so you must
   select the same Region in which to launch your instance.
3. From the Amazon EC2 console dashboard, choose **Launch
   instance**.
4. (Optional) Under **Name and tags**, for
   **Name**, enter a descriptive name for your
   instance.
5. Under **Application and OS Images (Amazon Machine
   Image)**, choose **Quick Start**.
   **Amazon Linux** is selected by default. Under
   **Amazon Machine Image (AMI)**, **Amazon Linux
   2023 AMI** is selected by default. Keep the default selection
   for this task.
6. Under **Instance type**, for **Instance
   type**, keep the default selection, or choose a different
   instance type.
7. Under **Key pair (login)**, for **Key pair
   name**, choose **Proceed without a key pair (Not
   recommended)**. When you use EC2 Instance Connect to connect to an
   instance, EC2 Instance Connect pushes a key pair to the instance's metadata, and it
   is this key pair that is used for the connection.
8. Under **Network settings**, do the following:
   1. For **Auto-assign public IP**, leave
      **Enable**.

   ###### Note

   To use EC2 Instance Connect in the Amazon EC2 console to connect to an instance, the instance must
   have a public IPv4 or IPv6 address. 2. For **Firewall (security groups)**, choose
   **Select existing security group**. 3. Under **Common security groups**, choose the
   security group that you created earlier.

9. In the **Summary** panel, choose **Launch
   instance**.

![This animation shows how to launch an instance. For the text version of this animation, see the steps in the preceding procedure.](images/tut1-task3-launch-an-instance.gif)

## Task 4: Connect to your instance

When you connect to an instance using EC2 Instance Connect, the EC2 Instance Connect API pushes
an SSH public key to the [instance
metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") where it remains for 60 seconds. The SSH daemon uses
`AuthorizedKeysCommand` and `AuthorizedKeysCommandUser` to
look up the public key from the instance metadata for authentication, and connects
you to the instance.

**Task objective**

In this task, you'll connect to your instance using EC2 Instance Connect in the Amazon EC2
console. If you completed the prerequisite Tasks 1, 2, and 3, the connection should
be successful.

**Steps to connect to your instance**

Use the following steps to connect to your instance. To view an animation of the
steps, see [View an animation: Connect to
your instance](#eic-tut1-task4-animation "#eic-tut1-task4-animation").

###### To connect an instance using EC2 Instance Connect in the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, the current AWS Region
   is displayed (for example, **Ireland**). Select the Region
   in which your instance is located.
3. In the navigation pane, choose **Instances**.
4. Select your instance and choose **Connect**.
5. Choose the **EC2 Instance Connect** tab.
6. Choose **Connect using a Public IP**.
7. Choose **Connect**.

A terminal window opens in the browser, and you are connected to your
instance.

![This animation shows how to connect an instance using EC2 Instance Connect. For the text version of this animation, see the steps in the preceding procedure.](images/eic-tut1-task4-connect.gif)
