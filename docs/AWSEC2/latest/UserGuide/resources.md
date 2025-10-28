# Manage your Amazon EC2 resources

A _resource_ is an entity that you can work with. Amazon EC2 creates
resources as you use the features of the service. For example, Amazon EC2 resources include
images, instances, fleets, key pairs, and security groups. All Amazon EC2 resource types include
attributes that describe the resources. For example, names, descriptions, resource
identifiers, and Amazon Resource Names (ARN).

Amazon EC2 resources are specific to the AWS Region or zone in which they reside. For
example, an Amazon Machine Image (AMI) is specific to an AWS Region, but the instance that you
launch from an AMI is specific to the zone in which you launch it. You can specify an
Amazon EC2 resource in a permissions policy using its ARN.

Your AWS account has default quotas for Amazon EC2. These quotas define the maximum number of
resources that you can create. For example, there are quotas for the maximum number of vCPUs
across your running instances. If launching an instance or starting a stopped instance would
cause you to exceed your quota, the operation fails.

You can search for specific resources in your AWS account by Region, using resource IDs
or tags. To search for specific resources or resource types across multiple Regions, use
Amazon EC2 Global View.

###### Contents

- [Select a Region for your Amazon EC2
  resources](using-regions-availability-zones-setup.md "using-regions-availability-zones-setup.md")
- [Find your Amazon EC2 resources](Using_Filtering.md "Using_Filtering.md")
- [View resources across Regions using AWS Global
  View](global-view.md "global-view.md")
- [Tag your Amazon EC2 resources](Using_Tags.md "Using_Tags.md")
- [Amazon EC2 service quotas](ec2-resource-limits.md "ec2-resource-limits.md")
