NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review source server information

The **Server info** tab shows a variety of general server
information, hardware, and network information.

This tab shows you general information about the source server:

- **General information**
  - **Last updated**: when was the data in this tab
    updated.
  - **Date added**: when was this server added to the
    service.
  - **AWS ID**: the ID of this source server resource
  - **arn**: the AWS Resource Name for this source
    server.

- **Identification hint**s: under most circumstances, the
  source server name is the best identifier, as it is what is used throughout the console as the
  name of the source server. If you need to validate which external server this is referring to
  in your data center, you can use one of the additional fields: Fully qualified domain name,
  VMware virtual machine identifier (only if source is VMWare), AWS instance ID (only is source
  is running on AWS).
- **Hardware and operating system**: the CPUs, RAM, disks, and
  network interfaces on the external server, as well as the type and full name of the operating
  system running on that server. The disks shown are all the disk on the source server, and may
  include disks not being replicated.
- **Recommended instance type**: this is the EC2 instance type
  the service is auto-recommending to use for the launched recovery instance. This is based only
  on the CPUs and RAM at the source (and not on utilization information). This is the instance
  type that is launched for this server by default.
  Information shown includes:

- **Last updated**
- **Date added**
- **Hostname**
- **Fully qualified domain name**
- **VMware virtual machine identifier (if relevant)**
- **AWS instance ID**
- **AWS ID**
- **ARN**
- **Operating system** information
- **CPUs**
- **RAM**
- **Network interfaces**
- **Recommended instance type**
