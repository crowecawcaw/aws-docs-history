NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Launch template settings

The **Launch template** allows you to control the way
AWS Application Migration Service launches instances in AWS. The default configuration defined in the template
is automatically applied to every newly added server.

To edit the launch template for your entire account, you need to edit your launch
template. Choose **Launch template** from the left-hand
navigation menu.

This opens the account template view. Click **Edit** to
update your account-level launch template.

###### Note

- Ensure the Account Level EC2 Launch Template is not deleted. If it is, edit and
  save the launch template page to create a new Account Level Template.
- You can change the settings for specific servers without affecting the launch template
  as described in [Edit replication settings for
  a server](replication-settings-template.md#edit-replication-settings "replication-settings-template.md#edit-replication-settings") .
- See [Assign an IPv6 address to an instance](../../../WSEC2/latest/UserGuide/working-with-ipv6-addresses.md#assign-ipv6-address "../../../WSEC2/latest/UserGuide/working-with-ipv6-addresses.md#assign-ipv6-address") in the _Amazon EC2 User Guide_
  for a list of instance types that do not support IPv6 addresses

###### Topics

- [General launch settings reference](#general-launch-settings "#general-launch-settings")
- [Default EC2 launch template
  settings](#default-ec2-launch-template "#default-ec2-launch-template")
- [MAP program tagging setting](#map-program-tagging "#map-program-tagging")

## General launch settings reference

In the **General launch settings** section, you can
define:

- **Instance type right sizing**: If you select this
  option, AWS Application Migration Service launches a test or cutover AWS instance type that best
  matches the OS, CPU, and RAM of your source server. Please note that the AWS
  instance type selected by Application Migration Service when this option is selected overwrites the
  instance type defined in your EC2 launch template.
- **Start instance upon launch**: Choose whether to start your test and cutover instances automatically upon launch
  or launch them in a stopped state.
- **Copy private IP**: Select if you want
  AWS Application Migration Service to ensure that the private IP used by the test or cutover instance matches
  the private IP used by the source server. If selected, AWS Application Migration Service monitors the source server on an
  hourly basis to identify the Private IP and uses the private IP of the primary
  network interface. Make sure that the IP range of the
  subnet you set in the EC2 Launch Template includes the private IP address for this
  feature to work. Copy private IP is not supported for IPv6.
- **Transfer server tags**: Select if you want
  AWS Application Migration Service to transfer user-configured custom tags from your source servers to
  your test or cutover instance. If selected, server tags are transferred. These
  tags are attached to all source servers, all launched test and cutover
  instances, and all of the ephemeral resources that are created on your AWS
  account during the normal operation of AWS Application Migration Service, such as snapshots, Amazon EBS
  volumes, replication and conversion servers, and security groups.
- **Operating system licensing**: Select if
  you want to Bring Your Own Licenses (BYOL) from the source server into the test or
  cutover instance.

Select the “Bring your own license (**BYOL**)” option if you are migrating a Linux server. All Linux
licenses are BYOL by default. Any RHEL, SUSE or Debian licenses are transferred
in their current form to the migrated instance.

For Windows servers choose if you want to **BYOL**)”. This sets
set up a Dedicated Host. All the licenses from the source Windows source server are
automatically transferred to the test or cutover instance. Please note that if
you use BYOL licensing for Windows you have to change the **Placement.tenancy** type in the EC2 launch template to **Host**. Otherwise, instance launch fails.

- **Boot mode**: When a computer boots, the first
  software that it runs is responsible for initializing the platform and providing an
  interface for the operating system to perform platform-specific operations. In
  Amazon EC2, two variants of the boot mode software are supported: Unified Extensible
  Firmware Interface (UEFI) and Legacy BIOS. The boot mode allows Application Migration Service to launch a
  test or cutover instance type that best matches the configuration of the source
  server. You can select between **Keep the source boot mode** or change it to **BIOS/UEFI
  modes** .

###### Note

UEFI is not supported in CentOS 6 and Rhel 6.

## Default EC2 launch template

settings

In the **Default EC2 launch template** section, you
can define the following options:

- **Default target subnet** – Choose the target
  subnet for the test and cutover machines. All the test and cutover machines are
  launched in this target subnet.
- **Target security groups** – Choose a number of
  security groups for the test and cutover machines. Upon the target launch, the
  selected security groups are attached to the Amazon EC2 instances.
- **Default instance type** – Choose a default
  instance type for the test and cutover machines. The instance type chosen in
  this template is propagated to source server’s launch template and is used to
  launch the target instance.
- **EBS volume type** – Choose an Amazon EBS volume type
  for the test and cutover machines. The Amazon EBS volume type options are io1, io2,
  gp3, st1, and sc1.

If this setting is not chosen, the default volume type selected in the
launch template is gp3 with maximum IOPS (16000). If a volume type is selected
in this option, and if the disk size does not match the limits of the volume
type, the default gp3 volume type is used with maximum IOPS.

###### Note

Note: if you manually delete the default launch template, AWS Application Migration Service generates
a new default launch template. Any changes previously made to the default template
are discarded, including subnet and security groups. You can make the same changes
on the new launch template, and they are applied to servers you add to the console
after you make the changes.

## MAP program tagging setting

Use this setting to determine whether to apply Migration Acceleration Program
(MAP) tags to your launched instances. Learn more about MAP tagging in [What is tagging for
MAP](https://aws.amazon.com/migration-acceleration-program "https://aws.amazon.com/migration-acceleration-program") in the AWS Migration Hub Launch Guide.

Select**Add MAP tag to Launched Instances** option,
if you want Application Migration Service to automatically tag your launched instances with the tag key and
value combination required for MAP program. Once selected you must specify the MAP tag
value that is used in your MAP tagging. Application Migration Service automatically tagw your migrated resources
with the key: “map-migrated” and the value of the tag that you provided. For more
details about the tag value that should be used here, please refer to the MAP tagging
guide provided in your MAP term.

[Learn more
about the AWS Migration Acceleration Program (MAP).](https://aws.amazon.com/migration-acceleration-program "https://aws.amazon.com/migration-acceleration-program")
