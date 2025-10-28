# Instances

## What is a Lightsail instance?

A Lightsail instance is a virtual private server (VPS) that lives in the AWS Cloud.
Use your Lightsail instances to store your data, run your code, and build web-based
applications or websites. Your instances can connect to each other and to other AWS
resources through both public (internet) and private (VPC) networking. You can create,
manage, and connect easily to instances right from the Lightsail console.

## What is a Lightsail plan?

Also referred to as a bundle, a Lightsail plan includes a virtual server with a fixed
amount of memory (RAM) and compute (vCPUs), SSD-based storage (disks), and a free data
transfer allowance. Lightsail plans also offer static IPv4 addresses, and DNS management.
Lightsail plans are charged on an hourly, on-demand basis, so you only pay for a plan when
you're using it.

## What software can I run on my instances?

Lightsail offers a range of operating system and application templates that are
automatically installed when you create a new Lightsail instance. Application templates
include WordPress, WordPress Multisite, cPanel & WHM, PrestaShop, Django, Drupal, Ghost,
Joomla!, Magento, Redmine, LAMP, Nginx (LEMP), MEAN, and Node.js.

You can install additional software on your instances by using the in-browser SSH or
your own SSH client.

## What operating systems can I use with

Lightsail?

Lightsail currently supports 7 Linux or Unix-like distributions: AlmaLinux OS 9,
Amazon Linux 2, Amazon Linux 2023, CentOS, Debian, FreeBSD, OpenSUSE, and Ubuntu, as well as three Windows
Server versions: 2016, 2019, and 2022.

## Do I need to bring my own license to use

Lightsail instances?

All instance blueprints available on Lightsail include a license, except for the
cPanel & WHM blueprint. That blueprint includes a 15-day trial license. For more
information, see [Quick start
guide: cPanel & WHM on Amazon Lightsail](amazon-lightsail-quick-start-guide-cpanel.md "amazon-lightsail-quick-start-guide-cpanel.md"). For all other instance blueprints, you
don't need to bring your own license (BYOL).

## How do I create a Lightsail

instance?

After logging in to Lightsail, you can use the Lightsail [console](https://lightsail.aws.amazon.com/ls/webapp "https://lightsail.aws.amazon.com/ls/webapp"), command line interface
(CLI), or API to create and manage instances.

The first time you log in to the console, choose Create Instance. The create instance
page is where you can choose the software, location, and name for your instance. Once you
choose Create, your new instance will spin up automatically within minutes.

## How do Lightsail instances

perform?

Lightsail instances are specifically engineered by AWS for web servers, developer
environments, and small database use cases. Such workloads don't use the full CPU often or
consistently, but occasionally need a performance burst. Lightsail uses burstable
performance instances that provide a baseline level of CPU performance with the additional
ability to burst above the baseline. This design enables you to get the performance you
need, when you need it, while protecting you from the variable performance or other common
side effects that you might typically experience from over-subscription in other
environments.

If you need highly configurable environments and instances with consistently high CPU
performance for applications such as video encoding or HPC applications, we recommend you
use [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/").

## How do I know when my instances are

bursting?

On the CPU utilization metric graphs for your instance, you will see a sustainable zone,
and a burstable zone. Your Lightsail instance can operate in the sustainable zone
indefinitely with no impact to the operation of your system. Your instance may begin
operating in the burstable zone when under heavy load. While operating in the burstable zone
your instance is consuming a higher amount of CPU cycles. Therefore, it can only operate in
this zone for a limited period of time. For more information, see [Viewing instance metrics in
Amazon Lightsail](amazon-lightsail-viewing-instance-health-metrics.md "amazon-lightsail-viewing-instance-health-metrics.md").

Add a metric alarm to be notified when your instance’s CPU utilization crosses from the
sustainable zone to the bursting zone. For more information, see [Creating instance metric
alarms in Amazon Lightsail](amazon-lightsail-adding-instance-health-metric-alarms.md "amazon-lightsail-adding-instance-health-metric-alarms.md").

## How do I connect to a Lightsail instance?

Lightsail offers a 1-click secure connection to your instance's terminal right from
your browser, supporting SSH access for Linux/Unix-based instances and RDP access for
Windows-based instances. To use 1-click connections, launch your instance management
screens, choose **Connect using SSH** or **Connect using
RDP**, and a new browser window opens and automatically connects to your
instance.

If you prefer to connect to your Linux/Unix-based instance using your own client,
Lightsail will do the SSH key storing and management work for you, and provide you with a
secure key to use in your SSH client.

## How can I back up my instances?

If you want to back up your data, you can use the Lightsail console or API to create a
manual snapshot of your instance, or enable automatic snapshots to have Lightsail create
daily snapshots for you. If there is a failure or bad code deployment, you can later use
your instance snapshot to create a brand new instance. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

## Can I upgrade my plan?

Yes. You can use a snapshot of your instance to create a new, larger size instance. For
more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

## How can I connect Lightsail

instances to other resources in my AWS account?

You can connect your Lightsail instances to Amazon VPC resources in your AWS account
privately, by using VPC peering. Just choose **Enable VPC peering** on your
Lightsail account page, and Lightsail does the work for you. Once VPC peering is
enabled, you can address other AWS resources in your default Amazon VPC by using their private
IPs. Find instructions [here](lightsail-how-to-set-up-vpc-peering-with-aws-resources.md "lightsail-how-to-set-up-vpc-peering-with-aws-resources.md").

###### Note

Note that you need to have a default Amazon VPC set up in your AWS account in order for
VPC peering with Lightsail to work. AWS accounts created before December 2013 do not
have a default VPC, and you will need to set one up. Find out more about setting up your
default VPC [here](../../../AmazonVPC/latest/UserGuide/default-vpc.md "../../../AmazonVPC/latest/UserGuide/default-vpc.md").

## What is the difference

between stopping and deleting my instance?

When you stop your instance, it is powered down at its current state and is available
for you to start again at any time. Stopping your instance will release its public IPv4
address, so it is recommended that you use static IPv4 addresses for instances that must
retain the same IP after they are stopped and started. Note that the public IPv6 addresses
attached to instances don't change even when instances are stopped and started.

When you delete your instance, you are performing a destructive action. Unless you have
created an instance snapshot, all of your instance data will be lost and you cannot recover
it again. Automatic snapshots are also deleted with the instance unless you keep them by
copying them as manual snapshots. The instance's public and private IP addresses will also
be released. If you were using a static IPv4 address with that instance, the static IPv4
address is detached, but remains in your account.
