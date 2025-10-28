# Best practices for Amazon EC2

To ensure the maximum benefit from Amazon EC2, we recommend that you perform the
following best practices.

###### Security

- Manage access to AWS resources and APIs using identity federation
  with an identity provider and IAM roles whenever possible.
  For more information, see [Creating IAM
  policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.
- Implement the least permissive rules for your security group.
- Regularly patch, update, and secure the operating system and applications
  on your instance. For more information, see [Update management](update-management.md "update-management.md"). For guidelines specific to
  Windows operating systems, see [Security best practices for Windows instances](ec2-windows-security-best-practices.md "ec2-windows-security-best-practices.md").
- Use Amazon Inspector to automatically discover and scan Amazon EC2 instances for software
  vulnerabilities and unintended network exposure. For more information, see the
  [Amazon Inspector User Guide](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md").
- Use AWS Security Hub controls to monitor your Amazon EC2 resources against security best
  practices and security standards. For more information about using Security Hub, see [Amazon Elastic Compute Cloud controls](../../../securityhub/latest/userguide/ec2-controls.md "../../../securityhub/latest/userguide/ec2-controls.md") in the _AWS Security Hub User
  Guide_.

###### Storage

- Understand the implications of the root volume type for data persistence, backup,
  and recovery. For more information, see [Root volume type](ComponentsAMIs.md#storage-for-the-root-device "ComponentsAMIs.md#storage-for-the-root-device").
- Use separate Amazon EBS volumes for the operating system versus your data. Ensure that
  the volume with your data persists after instance termination. For more information,
  see [Preserve data when an instance is
  terminated](preserving-volumes-on-termination.md "preserving-volumes-on-termination.md").
- Use the instance store available for your instance to store temporary data.
  Remember that the data stored in instance store is deleted when you stop, hibernate,
  or terminate your instance. If you use instance store for database storage, ensure
  that you have a cluster with a replication factor that ensures fault
  tolerance.
- Encrypt EBS volumes and snapshots. For more information, see [Amazon EBS encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the _Amazon EBS User Guide_.

###### Resource management

- Use instance metadata and custom resource tags to track and identify your AWS
  resources. For more information, see [Use instance metadata to manage your EC2
  instance](ec2-instance-metadata.md "ec2-instance-metadata.md") and [Tag your Amazon EC2 resources](Using_Tags.md "Using_Tags.md").
- View your current limits for Amazon EC2. Plan to request any limit increases in advance
  of the time that you'll need them. For more information, see [Amazon EC2 service quotas](ec2-resource-limits.md "ec2-resource-limits.md").
- Use AWS Trusted Advisor to inspect your AWS environment, and then make
  recommendations when opportunities exist to save money, improve system availability
  and performance, or help close security gaps. For more information, see [AWS Trusted Advisor](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md") in the _AWS Support User Guide_.

###### Backup and recovery

- Regularly back up your EBS volumes using [Amazon EBS snapshots](../../../ebs/latest/userguide/ebs-snapshots.md "../../../ebs/latest/userguide/ebs-snapshots.md"), and
  create an [Amazon Machine Image (AMI)](AMIs.md "AMIs.md") from your
  instance to save the configuration as a template for launching future
  instances. For more information about AWS services that help achieve
  this use case, see [AWS Backup](../../../aws-backup/latest/devguide.md "../../../aws-backup/latest/devguide.md") and [Amazon Data Lifecycle Manager](../../../ebs/latest/userguide/snapshot-lifecycle.md "../../../ebs/latest/userguide/snapshot-lifecycle.md").
- Deploy critical components of your application across multiple Availability Zones,
  and replicate your data appropriately.
- Design your applications to handle dynamic IP addressing when your instance
  restarts. For more information, see [Amazon EC2 instance IP addressing](using-instance-addressing.md "using-instance-addressing.md").
- Monitor and respond to events. For more information, see [Monitor Amazon EC2 resources](monitoring_ec2.md "monitoring_ec2.md").
- Ensure that you are prepared to handle failover. For a basic solution, you can
  manually attach a network interface or Elastic IP address to a replacement instance.
  For more information, see [Elastic network interfaces](using-eni.md "using-eni.md"). For
  an automated solution, you can use Amazon EC2 Auto Scaling. For more information, see the
  [Amazon EC2 Auto Scaling User Guide](../../../autoscaling/ec2/userguide.md "../../../autoscaling/ec2/userguide.md").
- Regularly test the process of recovering your instances and Amazon EBS volumes to
  ensure data and services are restored successfully.

###### Networking

- Set the time-to-live (TTL) value for your applications to 255, for IPv4 and IPv6.
  If you use a smaller value, there is a risk that the TTL will expire while
  application traffic is in transit, causing reachability issues for your
  instances.
