NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Full launch template setting review

This section reviews the entire EC2 launch template and identifies which fields should and
should not be changed in order for the EC2 launch template to work with Application Migration
Service. Editing or changing any fields that are marked as "do not edit" or "do not change" can
cause AWS Application Migration Service to not function.

- **Launch template name** – This name is automatically
  generated when the template is first created upon Agent installation. The name cannot be
  changed.
- **Template version description** – You can give the
  template any description you wish.

- **AMI** – Customers do not typically choose a specific AMI
  to include in the launch template. If you edit the launch template to use an existing AMI,
  the contents of the AMI are not used by AWS Application Migration Service. If the AMI is not configured properly
  (licensing, flags, and more), then this may prevent the test or cutover instance launched
  from booting correctly or from being properly licensed.

- **Instance type** – You can select any instance type you
  want. The launch template shows the instance type suggested by AWS Application Migration Service.

- **Key pair (login)** – **Do
  not** alter this field. Do not include a key pair with the launch template.

- **Networking platform** – Be sure to select **Virtual Private Cloud (VPC)**. **EC2-Classic** is **not** supported.
- **Security groups** – **Do
  not** add Security group here. This field should remain blank. You can add security
  groups later under **Network interface**.

- **Storage (volumes)** – This section shows all of the
  disks that you chose to replicate from your source server upon AWS Replication Agent
  installation.

###### Important

Initial settings for EBS volumes are not derived from activity on the Source Server.
Default values are chosen to give maximum performance on first launch.

Each disk is composed of the following fields:

    + **Storage type** – Shows the default volume type (EBS).
     This cannot be changed.
    + **Device name** – **Do not**
     change or edit this field. The device name shown here corresponds to the disk name on the
     source server. This field allows you to identify which disk is which.
    + **Snapshot** – **Do not**
     change or edit this field. Snapshots should not be included in the launch template.
    + **Size** – **Do not** change
     or edit this field.
    + **Volume type** – You can select any volume type you want
     to use. AWS Application Migration Service automatically sets **General Purpose SSD
     (gp3)** as the default. You may want to change the volume type in order to reduce
     costs. Ensure that you read the caveats in the [EBS
     documentation](../../../AWSEC2/latest/UserGuide/EBSPerformance.md#initialize "../../../AWSEC2/latest/UserGuide/EBSPerformance.md#initialize").
    + **IOPS** – Set the number of I/O operations per second that
     the volume can support. You can select any number as long as it matches the [EBS
     guidelines](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md").




    	- Provisioned IOPS SSD (io1) : 50 IOPS per GiB of storage
    	- Provisioned IOPS SSD (io2) : 500 IOPS per GiB of storage
    	- General Purpose SSD (gp3) : 500 IOPS per GiB of storage
    AWS Application Migration Service automatically provisions the maximum IOPS possible for the volume, based on
     the above ratio. This is to minimize the impact of the [performance penalty](../../../AWSEC2/latest/UserGuide/EBSPerformance.md#initialize "../../../AWSEC2/latest/UserGuide/EBSPerformance.md#initialize")
     when working with EBS volumes created from snapshots.
    + **Delete on termination** – Do **not** change or edit this field. This should not be included in the launch
     template.
    + **Encrypted** – **Do not**
     change or edit this field. This should not be included in the launch template.
    + **Key** – **Do not** change
     or edit this field. This should not be included in the launch template.
    + **Add volume** – **Do not**
     use this functionality. You cannot add volumes to the source server through the launch
     template.
    + **Remove (volume)** – **Do
     not** use this functionality. You cannot remove volumes from the source server
     through the launch template. If you do, AWS MGN automatically creates a volume using
     the default volume settings.

- **Resource tags** – You can add up to 50 tags. These are transferred to your test and cutover instances. Note that these tags may interfere with
  other tags that have already been added to the source server. Launch template tags always
  take precedence over tags set in the AWS MGN console or tags manually assigned to the
  server.

- **Network interfaces** – The network interface is created
  by default based on your replication template. The network interface section is composed of
  the following fields:
  - **Device index** – **Do
    not** change or edit this field. The value should always be "**0**".
  - **Network interface** – Use this option only if you want
    use a pre-existing ENI (Elastic Network Interface). The Launch Template overwrites
    certain ENI settings. Use this if you want to add an Elastic IP. You have to attach
    the Elastic IP to the ENI.

  ###### Note

  When selecting an pre-existing ENI, you must change the **Auto-assign public IP** value to **Don't include in launch
  template** for a successful target launch.
  - **Description** – Add an optional description for the
    network interface (if chosen).
  - **Subnet** – Choose the subnet. This is the subnet within
    which the network interface is located and the test or cutover instance is launched.
    AWS Application Migration Service selects the default VPC subnet by default (if one exists).
  - **Auto-assign public IP** - Choose whether you want the
    public IP to be auto-assigned.
  - **Primary IP** – Use this field if you wish to utilize a
    private IP. The private IP you set in the **Copy private IP**
    field in the AWS MGN launch settings is copied to this field.
  - **Secondary IP** - Define a secondary IP, if
    needed.
  - **IPv6 IPs** – Define IPv6 IPs, if needed.
  - **Security groups** – Choose a security group. If no
    security group is chosen, then the default VPC security group is used by
    default.
  - **Delete on termination** – We suggest choosing
    "**Yes**". Choosing "**No**"
    makes this network interface a permanent ENI.
  - **Elastic Fabric Adapter** – **Do
    not** change or edit this field.
  - **Network card index** – **Do
    not** change or edit this field.
  - **Add network interface** – Note that the EC2 launch
    template only supports two network interfaces. If you require more than two network
    interfaces, you need to define them after the test or cutover instance has been
    launched. This can be done through a post-launch action.

- **Advanced details** – In this section, we focus on
  the fields you should **not** change or edit in order to allow
  AWS Application Migration Service to function properly. **Do not** change or edit any of
  the following fields:
  - RAM disk ID
  - Kernel
  - Nitro Enclave
  - Metadata accessible
