# Setting up ElastiCache

To use the ElastiCache web service, follow these steps.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Set up permissions](#elasticache-set-up-permissions "#elasticache-set-up-permissions")
- [Set up EC2](#elasticache-install-configure-ec2 "#elasticache-install-configure-ec2")
- [Grant network access](#elasticache-install-grant-access-VPN "#elasticache-install-grant-access-VPN")
- [Set up command line access](#Download-and-install-cli "#Download-and-install-cli")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Set up your permissions (new ElastiCache users only)

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

Amazon ElastiCache creates and uses service-linked roles to provision resources and access other
AWS resources and services on your behalf. For ElastiCache to create a service-linked role
for you, use the AWS-managed policy named `AmazonElastiCacheFullAccess`. This
role comes preprovisioned with permission that the service requires to create a
service-linked role on your behalf.

You might decide not to use the default policy and instead to use a custom-managed policy.
In this case, make sure that you have either permissions to call
`iam:createServiceLinkedRole` or that you have created the ElastiCache
service-linked role.

For more information, see the following:

- [Creating a New Policy](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") (IAM)
- [AWS managed policies for Amazon ElastiCache](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Using Service-Linked Roles for Amazon ElastiCache](using-service-linked-roles.md "using-service-linked-roles.md")

## Set up EC2

You will need to setup an EC2 instance from which you will connect to your cache.

- If you don’t already have an EC2 instance, learn how to setup an EC2 instance here: [Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").
- Your EC2 instance must be in the same VPC and have the same security group settings as your cache.
  By default, Amazon ElastiCache creates a cache in your default VPC and uses the default security group.
  To follow this tutorial, ensure that your EC2 instance is in the default VPC and has the default security group.

## Grant network access from an Amazon VPC security group to your cache

ElastiCache node-based clusters use port 6379 for Valkey and Redis OSS commands, and ElastiCache serverless uses both port 6379 and port 6380.
In order to successfully connect and execute Valkey or Redis OSS commands from your EC2 instance, your security group must allow access to these ports as needed.

For ElastiCache serverless specifically:

- **Port 6379 (Primary endpoint):** Required for write operations and reads requiring strong consistency
- **Port 6380 (Read-optimized endpoint):** Used for Read From Replica functionality, providing lower latency reads with eventual consistency

Many clients establish connections to both ports even if not actively using Read From Replica, requiring that you make port 6380 accessible even if you don't intend to use Read From Replica.

ElastiCache for Memcached uses the 11211 and 11212 ports to accept Memcached commands. In order to successfully connect and
execute Memcached commands from your EC2 instance, your security group must allow access to these ports.

1. Sign in to the AWS Command Line Interface and open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**, choose **Security Groups**.
3. From the list of security groups, choose the security group for your Amazon VPC. Unless you created a security group for ElastiCache use,
   this security group will be named _default_.
4. Choose the Inbound tab, and then:
   1. Choose **Edit**.
   2. Choose **Add rule**.
   3. In the Type column, choose **Custom TCP rule**.
   4. If using Valkey or Redis OSS, then in the **Port range** box, type `6379`.

   If using Memcached, then in the **Port range** box, type `11211`. 5. In the **Source** box, choose **Anywhere** which has the port range (0.0.0.0/0)
   so that any Amazon EC2
   instance that you launch within your Amazon VPC can connect to your cache. 6. If you are using ElastiCache serverless, add another rule by choosing **Add rule**. 7. In the **Type** column, choose **Custom TCP** rule. 8. If using ElastiCache for Redis OSS, then in the **Port range**box, type `6380`.

   If using ElastiCache for Memcached, then in the **Port range**box, type `11212`. 9. In the **Source** box, choose **Anywhere** which has the port range (0.0.0.0/0)
   so that any Amazon EC2 instance that you launch within your Amazon VPC can connect to your cache. 10. Choose **Save**

## Download and set up command line access

**Download and install the _valkey-cli_
utility.**

If you use ElastiCache for Valkey, then you might find the valkey-cli utility useful.
If you're using ElastiCache for Redis OSS with redis-cli, consider switching to valkey-cli as it works for Redis OSS as well.

1. Connect to your Amazon EC2 instance using the connection utility of your choice. For instructions on how to connect to an Amazon EC2 instance,
   see the [Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").
2. Download and install valkey-cli utility by running the appropriate command for your setup.

**Amazon Linux 2023**

```
sudo dnf install gcc jemalloc-devel openssl-devel tcl tcl-devel -y
wget -O valkey-8.0.0.tar.gz https://github.com/valkey-io/valkey/archive/refs/tags/8.0.0.tar.gz
tar xvzf valkey-8.0.0.tar.gz
cd valkey-8.0.0
make valkey-cli BUILD_TLS=yes
sudo install -m 755 src/valkey-cli /usr/local/bin/

```

**Amazon Linux 2**

```
sudo amazon-linux-extras install epel -y
sudo yum install gcc jemalloc-devel openssl-devel tcl tcl-devel -y
wget -O valkey-8.0.0.tar.gz https://github.com/valkey-io/valkey/archive/refs/tags/8.0.0.tar.gz
tar xvzf valkey-8.0.0.tar.gz
cd valkey-8.0.0
make valkey-cli BUILD_TLS=yes
sudo install -m 755 src/valkey-cli /usr/local/bin/

```

###### Note

- When you install the redis6 package, it installs redis6-cli with default encryption support.
- It is important to have build support for TLS when installing valkey-cli or redis-cli. ElastiCache Serverless is only accessible when TLS is enabled.
- If you are connecting to a cluster that isn't encrypted, you don't need the `Build_TLS=yes` option.
