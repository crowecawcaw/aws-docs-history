# Export Lightsail resources to Amazon Elastic Compute Cloud

(Amazon EC2)

## What is export to Amazon EC2?

Export to Amazon EC2 is a feature that allows you to create a copy of your Lightsail
instance in Amazon EC2. When you export to Amazon EC2, you can pick among the wide set of instance
types, configurations, and pricing models that Amazon EC2 offers, and have even more fine-tuned
control over your networking, storage, and compute environment.

## Why would I want to export to

Amazon EC2?

Lightsail offers you an easy way to run and scale a wide set of cloud-based
applications, at a bundled, predictable, and low price. Lightsail also automatically sets
up your cloud environment configurations such as networking and access management.

Exporting to Amazon EC2 allows you to run your application on a wider set of instance types,
ranging from virtual machines with more CPU power, memory, and networking capabilities, to
specialized or accelerated instances with FPGAs and GPUs. In addition, Amazon EC2 performs less
automatic management and set-up, allowing you more control over how you configure your cloud
environment, such as your VPC.

## How does exporting to Amazon EC2 work?

To get started, you need to export your manual snapshot of a Lightsail instance or
block storage disk. Customers who are comfortable with Amazon EC2 can then use the Amazon EC2 creation
wizard or API to create a new Amazon EC2 instances or Amazon EBS volumes, as they would from an
existing EC2 AMI or EBS volume. Alternatively, Lightsail also provides a guided
Lightsail console experience to help you easily create a new EC2 instance.

###### Note

Snapshots of cPanel & WHM (CentOS 7) instances cannot be exported to Amazon EC2.

## How am I billed?

Using the export to Amazon EC2 feature is free. Once you have exported your manual snapshots
to Amazon EC2, you will be charged for the Amazon EC2 image separately and in addition to your
Lightsail manual snapshot. Any new Amazon EC2 instances you launch will also be billed by
Amazon EC2, including their Amazon EBS storage volume(s) and data transfer. Refer to the [Amazon EC2 pricing page](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") for details on the
pricing for your new instance and resources. Lightsail resources that continue to run in
your Lightsail account will continue to be billed at their regular rates until they are
deleted.

## Can I export managed databases or disk

snapshots?

The export feature allows you to export manual Lightsail disk snapshots but doesn't
currently support manual snapshots of managed databases. Disk snapshots can be rehydrated as
Amazon EBS volumes from the Amazon EC2 console or API.

## What Lightsail resources can I

export?

The Lightsail export to Amazon EC2 feature is designed to support the export of Linux and
Windows instance snapshots to Amazon EC2. It also supports the export of block storage disk
snapshots to Amazon EBS. It does not currently support the export of databases, container
services, content delivery network (CDN) distributions, load balancers, static IPs, and DNS
records. Additionally, snapshots of Django, Ghost, and cPanel & WHM instances cannot be
exported to Amazon EC2 at this time.
