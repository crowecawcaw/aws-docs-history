# What is Amazon Lightsail?

Amazon Lightsail is the easiest way to get started with Amazon Web Services (AWS) for anyone who
needs to build websites or web applications. It includes everything you need to launch your
project quickly—instances (virtual private servers), container services, managed
databases, content delivery network (CDN) distributions, load balancers, SSD-based block
storage, static IP addresses, DNS management of registered domains, and resource snapshots
(backups)—for a low, predictable monthly price.

Lightsail also offers Amazon Lightsail for Research. With Lightsail for Research, academics and researchers can create powerful
virtual computers in the AWS Cloud. These virtual computers come with pre-installed research
applications, such as RStudio and Scilab. For more information see the [Amazon Lightsail for Research
User Guide](../../../lightsail-for-research/latest/ug/what-is-lfr.md "../../../lightsail-for-research/latest/ug/what-is-lfr.md").

###### Topics

- [Features](#lightsail-features "#lightsail-features")
- [Who is Lightsail for?](#who-is-lightsail-for "#who-is-lightsail-for")
- [Get started](#how-to-get-started-lightsail "#how-to-get-started-lightsail")
- [Related services](#related-services "#related-services")
- [Estimates, billing, and cost
  optimization](#lightsail-pricing-additional "#lightsail-pricing-additional")

## Features of Lightsail

Lightsail provides the following high-level features:

**Instances**

Lightsail offers virtual private servers (instances) that are easy to set up and
backed by the power and reliability of AWS. You can launch your website, web
application, or project in minutes, and manage your instance from the intuitive
Lightsail console or API.

As you’re creating your instance, you will click-to-launch a simple operating system
(OS), a pre-configured application, or development stack—such as WordPress, Windows,
Plesk, LAMP, Nginx, and more. Every Lightsail instance comes with a built-in firewall
that you can use to allow or restrict traffic to your instances based on source IP,
port, and protocol. [Learn
more](understanding-instances-virtual-private-servers-in-amazon-lightsail.md "understanding-instances-virtual-private-servers-in-amazon-lightsail.md")

**Containers**

Run and securely access containerized applications in the cloud. A container is a
standard unit of software that packages code and its dependencies together so the
application runs quickly and reliably from one computing environment to another. [Learn more](amazon-lightsail-container-services.md "amazon-lightsail-container-services.md")

**Load balancers**

Route web traffic across your instances so your websites and applications can
accommodate variations in traffic, protected against outages, and deliver a seamless
visitor experience. [Learn
more](understanding-lightsail-load-balancers.md "understanding-lightsail-load-balancers.md")

**Managed databases**

Lightsail offers a fully configured MySQL or PostgreSQL databases plan that
includes memory, processing, storage, and transfer allowance. With Lightsail managed
databases, you can easily scale your databases independently of your virtual servers,
improve application availability, or run standalone databases in the cloud. [Learn more](amazon-lightsail-databases.md "amazon-lightsail-databases.md")

**Block and object storage**

Lightsail offers both block and object storage. You can scale your storage quickly
and easily with highly available SSD-backed storage for your Linux or Windows virtual
server. [Learn
more](elastic-block-storage-and-ssd-disks-in-amazon-lightsail.md "elastic-block-storage-and-ssd-disks-in-amazon-lightsail.md")

With Lightsail Object storage buckets, you can store and retrieve objects, at any
time, from anywhere on the internet. You can also host static content on the cloud.
[Learn more](buckets-in-amazon-lightsail.md "buckets-in-amazon-lightsail.md")

**CDN distributions**

Lightsail enables content delivery network (CDN) distributions, which are built on
the same infrastructure as Amazon CloudFront. You can easily distribute your content to a global
audience by setting up proxy servers across the world, so that your users can access
your website geographically closer to them, thus reducing latency. [Learn more](amazon-lightsail-databases.md "amazon-lightsail-databases.md")

**Access to AWS services**

Lightsail uses a focused set of features like instances, managed databases and
load balancers to make it easier to get started. But that doesn't mean you're limited to
those options –you can integrate your Lightsail project with some of the 90+ other
services in AWS through Amazon VPC peering. [Learn more](using-lightsail-with-other-aws-services.md "using-lightsail-with-other-aws-services.md")

For more details about Lightsail, see [Amazon Lightsail](https://aws.amazon.com/lightsail/ "https://aws.amazon.com/lightsail/").

## Who is Lightsail for?

Lightsail is for everyone. You can choose an image for your Lightsail instance that
jump starts your project so you don't have to spend as much time installing software or
frameworks.

If you're an individual developer or hobbyist working on a personal project, Lightsail
can help you deploy and manage basic cloud resources. You might also be interested in learning
or experimenting with cloud services, such as virtual machines, domains or networking.
Lightsail provides a quick way to get started.

Lightsail has images with base operating systems, development stacks like LAMP, LEMP
(Nginx), and SQL Server Express, and applications like WordPress, Drupal, and Magento. For
more detailed information about the software installed on each image, see [Choose a
Lightsail instance image](compare-options-choose-lightsail-instance-image.md "compare-options-choose-lightsail-instance-image.md").

As your project grows, you can add block storage disks and attach them to your Lightsail
instance. You can take snapshots of these instances and disks and easily create new instances
from those snapshots. You can also peer your VPC so that your Lightsail instances can use
other AWS resources outside of Lightsail.

You can also create a Lightsail load balancer and attach target instances to create a
highly available application. You can also configure your load balancer to handle encrypted
(HTTPS) traffic, session persistence, health checking, and more.

## Get started with Lightsail

After you set up to use Lightsail, you can walk through [Getting started with virtual private servers on
Lightsail](getting-started.md "getting-started.md")
to launch, connect to, and clean up an instance. For more information on how to access Lightsail, see [Access Lightsail](access-lightsail.md "access-lightsail.md")
.

## Related services

You can provision Lightsail resources, such as instances and disks, directly using
Lightsail. In addition, you can provision resources using other AWS services, such as the
following:

- [Amazon EC2](../../../ec2.md "../../../ec2.md")

Provides resizeable computing capacity—literally, servers in Amazon's data
centers—that you use to build and host your software systems. To compare Lightsail and
Amazon EC2, see [Amazon Lightsail or
Amazon EC2](../../../decision-guides/latest/lightsail-or-ec2/lightsail-or-ec2.md "../../../decision-guides/latest/lightsail-or-ec2/lightsail-or-ec2.md").

- [Amazon EC2 Auto Scaling](../../../autoscaling.md "../../../autoscaling.md")

Helps ensure you have the correct number of Amazon EC2 instances available to handle the
load for your application.

- [Elastic Load Balancing](../../../elasticloadbalancing.md "../../../elasticloadbalancing.md")

Automatically distribute incoming application traffic across multiple
instances.

- [Amazon Relational Database Service (Amazon RDS)](../../../rds.md "../../../rds.md")

Set up, operate, and scale a managed relational database in the cloud.

- [Amazon Elastic Container Service (Amazon ECS)](../../../ecs.md "../../../ecs.md")

Deploy, manage, and scale containerized applications on a cluster of Amazon EC2
instances.

## Estimates, billing, and cost

optimization

To create estimates for your AWS use cases, use the [AWS Pricing Calculator](https://calculator.aws/#/ "https://calculator.aws/#/").

To see your bill, go to the **Billing and Cost Management
Dashboard** in the [AWS Billing and Cost Management
console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/"). Your bill contains links to usage reports that provide details about your
bill. To learn more about AWS account billing, see [AWS Billing
and Cost Management User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").

If you have questions concerning AWS billing, accounts, and events, [contact AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

You can optimize the cost, security, and performance of your AWS environment using
[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/").
