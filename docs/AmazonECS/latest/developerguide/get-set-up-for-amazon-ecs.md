# Set up to use Amazon ECS

If you've already signed up for Amazon Web Services (AWS) and have been using Amazon Elastic Compute Cloud
(Amazon EC2), you are close to being able to use Amazon ECS. The set-up process for the two services
is similar. The following guide prepares you for launching your first Amazon ECS cluster.

Complete the following tasks to get set up for Amazon ECS.

## AWS Management Console

The AWS Management Console is a browser-based interface for managing Amazon ECS resources. The console
provides a visual overview of the service, making it easy to explore Amazon ECS features and
functions without needing to use additional tools. Many related tutorials and
walkthroughs are available that can guide you through use of the console.

For a tutorial that guides you through the console, see [Learn how to create and use Amazon ECS resources](getting-started.md "getting-started.md").

When starting out, many customers prefer using the console because it provides instant
visual feedback on whether the actions they take succeed. AWS customers that are
familiar with the AWS Management Console, can easily manage related resources such as load balancers
and Amazon EC2 instances.

Start with the AWS Management Console.

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Create a virtual private cloud

You can use Amazon Virtual Private Cloud (Amazon VPC) to launch AWS resources into a virtual network that
you've defined. We strongly suggest that you launch your
container instances in a VPC.

If you have a default VPC, you can skip this section and move to the
next task, [Create a security group](#create-a-base-security-group "#create-a-base-security-group"). To determine whether you have a
default VPC, see [Work with your default VPC and default subnets](../../../vpc/latest/userguide/work-with-default-vpc.md#view-default-vpc "../../../vpc/latest/userguide/work-with-default-vpc.md#view-default-vpc") in the
_Amazon VPC User Guide_. Otherwise, you can create a nondefault VPC in
your account using the steps below.

For information about how to create a VPC, see [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the
_Amazon VPC User Guide_, and use the following table to
determine what options to select.

| Option              | Value                                                                               |
| ------------------- | ----------------------------------------------------------------------------------- |
| Resources to create | VPC only                                                                            |
| Name                | Optionally provide a name for your VPC.                                             |
| IPv4 CIDR block     | IPv4 CIDR manual input<br>The CIDR block size must have a size between /16 and /28. |
| IPv6 CIDR block     | No IPv6 CIDR block                                                                  |
| Tenancy             | Default                                                                             |

For more information about Amazon VPC, see [What is Amazon
VPC?](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the _Amazon VPC User Guide_.

## Create a security group

Security groups act as a firewall for associated container instances, controlling both
inbound and outbound traffic at the container instance level. You can add rules to a
security group that enable you to connect to your container instance from your IP
address using SSH. You can also add rules that allow inbound and outbound HTTP and HTTPS
access from anywhere. Add any rules to open ports that are required by your tasks.
Container instances require external network access to communicate with the Amazon ECS
service endpoint.

If you plan to launch container instances in multiple Regions, you need to create a
security group in each Region. For more information, see [Regions and Availability
Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

###### Tip

You need the public IP address of your local computer, which you can get using a
service. For example, we provide the following service: [http://checkip.amazonaws.com/](http://checkip.amazonaws.com/ "http://checkip.amazonaws.com/") or
[https://checkip.amazonaws.com/](https://checkip.amazonaws.com/ "https://checkip.amazonaws.com/"). To locate another service that provides
your IP address, use the search phrase "what is my IP address." If you are
connecting through an internet service provider (ISP) or from behind a firewall
without a static IP address, you must find out the range of IP addresses used by
client computers.

For information about how to create a security group, see [Create a security group for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/creating-security-group.md "../../../AWSEC2/latest/UserGuide/creating-security-group.md") in the _Amazon EC2 User Guide_ and use the following table to determine what options
to select.

| Option | Value                                                                                                                                               |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Region | The same Region in which you created your key pair.                                                                                                 |
| Name   | A name that is easy for you to remember, such as<br>_ecs-instances-default-cluster_.                                                                |
| VPC    | The default VPC (marked with "(default)").NoteIf your account supports Amazon EC2 Classic, select the VPC that<br>you created in the previous task. |

For information about the outbound rules to add for your use cases, see [Security group
rules for different use cases](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md") in the _Amazon EC2 User Guide_.

Amazon ECS container instances do not require any inbound ports to be open. However, you
might want to add an SSH rule so you can log into the container instance and examine the
tasks with Docker commands. You can also add rules for HTTP and HTTPS if you want your
container instance to host a task that runs a web server. Container instances do require
external network access to communicate with the Amazon ECS service endpoint. Complete
the following steps to add these optional security group rules.

Add the following three inbound rules to your security group.For information about how
to create a security group, see [Configure security group rules](../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules "../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules") in the _Amazon EC2 User Guide_.

| Option     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTP rule  | Type: HTTP<br>Source: Anywhere (`0.0.0.0/0`)<br>This option automatically adds the 0.0.0.0/0 IPv4 CIDR block as<br>the source. This is acceptable for a short time in a test<br>environment, but it's unsafe in production environments. In<br>production, authorize only a specific IP address or range of<br>addresses to access your instance.                                                                                                                                                                                                                                                       |
| HTTPS rule | Type: HTTPS<br>Source: Anywhere (`0.0.0.0/0`)<br>This is acceptable for a short time in a test environment, but<br>it's unsafe in production environments. In production, authorize<br>only a specific IP address or range of addresses to access your<br>instance.                                                                                                                                                                                                                                                                                                                                     |
| SSH rule   | Type: SSH<br>Source: Custom, specify the public IP address of your computer or<br>network in CIDR notation. To specify an individual IP address in<br>CIDR notation, add the routing prefix `/32`. For example,<br>if your IP address is `203.0.113.25`, specify<br>`203.0.113.25/32`. If your company allocates<br>addresses from a range, specify the entire range, such as<br>`203.0.113.0/24`.<br>ImportantFor security reasons, we don't recommend that you allow SSH<br>access from all IP addresses (`0.0.0.0/0`) to your<br>instance, except for testing purposes and only for a short<br>time. |

## Create the credentials to connect to your EC2 instance

For Amazon ECS, a key pair is only needed if you intend on using EC2.

AWS uses public-key cryptography to secure the login
information for your instance. A Linux instance, such as an Amazon ECS container
instance, has no password to use for SSH access. You use a key pair to log in to your
instance securely. You specify the name of the key pair when you launch your container
instance, then provide the private key when you log in using SSH.

If you haven't created a key pair already, you can create one using the Amazon EC2 console.
If you plan to launch instances in multiple regions, you'll need to create a key pair in
each region. For more information about regions, see [Regions and Availability
Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

###### To create a key pair

- Use the Amazon EC2 console to create a key pair. For more information about creating a key pair,
  see [Create a key
  pair](../../../AWSEC2/latest/UserGuide/create-key-pairs.md "../../../AWSEC2/latest/UserGuide/create-key-pairs.md") in the _Amazon EC2 User Guide_.

For information about how to connect to your instance, see [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md") in the
_Amazon EC2 User Guide_.

## Install the AWS CLI

The AWS Management Console can be used to manage all operations manually with Amazon ECS. However, you
can install the AWS CLI on your local desktop or a developer box so that you can build
scripts that can automate common management tasks in Amazon ECS.

To use the AWS CLI with Amazon ECS, install the latest AWS CLI version. For information about
installing the AWS CLI or upgrading it to the latest version, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The AWS Command Line Interface (AWS CLI) is a unified tool that you can use to manage your AWS
services. With this one tool alone, you can both control multiple AWS services and
automate these services through scripts. The Amazon ECS commands in the AWS CLI are a
reflection of the Amazon ECS API.

The AWS CLI is suitable for customers who prefer and are used to scripting and
interfacing with a command line tool and know exactly which actions they want to perform
on their Amazon ECS resources. The AWS CLI is also helpful to customers who want to familiarize
themselves with the Amazon ECS APIs. Customers can use the AWS CLI to perform a number of
operations on Amazon ECS resources, including Create, Read, Update, and Delete operations,
directly from the command line interface.

Use the AWS CLI if you are or want to become familiar with the Amazon ECS APIs and
corresponding CLI commands and want to write automated scripts and perform specific
actions on Amazon ECS resources.

AWS also provides the command line tools [AWS Tools for Windows PowerShell](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md"). For
more information, see the [AWS Tools for Windows PowerShell User
Guide](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md").

## Next steps for using Amazon ECS

After installing the AWS CLI, there are many different tools you can utilize as you continue to
use Amazon ECS. The following links explain what some of those tools are and give examples of how to
use them with Amazon ECS.

- [Create your
  first container image](create-container-image.md "create-container-image.md") with Docker and push it to Amazon ECR for use in your Amazon ECS
  task definitions.
- [Learn how to create an Amazon ECS Linux task for Fargate](getting-started-fargate.md "getting-started-fargate.md").
- [Learn how to create an Amazon ECS Windows task for Fargate](Windows_fargate-getting_started.md "Windows_fargate-getting_started.md").
- [Learn how to create an Amazon ECS Windows task for EC2](getting-started-ecs-ec2-v2.md "getting-started-ecs-ec2-v2.md").
- Using your preferred programming language, define infrastructure or architecture
  as code with the [Creating Amazon ECS resources using the AWS CDK](tutorial-ecs-web-server-cdk.md "tutorial-ecs-web-server-cdk.md").
- Define and manage all AWS resources in your environment with automated
  deployment using [Using Amazon ECS with AWS CloudFormation](ecs-with-cloudformation.md "ecs-with-cloudformation.md").
- Use the complete [Creating Amazon ECS resources using the AWS Copilot command line interface](AWS_Copilot.md "AWS_Copilot.md") end-to-end developer workflow to
  create, release, and operate container applications that comply with AWS best
  practices for infrastructure.
