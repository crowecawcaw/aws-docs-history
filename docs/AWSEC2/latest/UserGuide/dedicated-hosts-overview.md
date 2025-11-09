# Amazon EC2 Dedicated Hosts

An Amazon EC2 Dedicated Host is a physical server that is fully dedicated for your use. You can optionally choose to share the instance capacity with other
AWS accounts. For more information, see [Cross-account Amazon EC2 Dedicated Host sharing](dh-sharing.md "dh-sharing.md").

Dedicated Hosts provide visibility and control over instance placement and they support host
affinity. This means that you can launch and run instances on specific hosts, and you can
ensure that instances run only on specific hosts. For more information, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").

Dedicated Hosts provide comprehensive Bring Your Own License (BYOL) support. They allow you to use
your existing per-socket, per-core, or per-VM software licenses, including Windows Server,
SQL Server, SUSE Linux Enterprise Server, Red Hat Enterprise Linux, or other software
licenses that are bound to VMs, sockets, or physical cores, subject to your license
terms.

If you require your instances to run on dedicated hardware, but you do not need visibility
or control over instance placement, and you do not need to use per-socket or per-core
software licenses, you can consider using Dedicated Instances instead. Dedicated Instances and Dedicated Hosts can both be used to
launch Amazon EC2 instances onto dedicated physical servers. There are no performance, security,
or physical differences between Dedicated Instances and instances on Dedicated Hosts. However, there are some key
differences between them. The following table highlights some of the key differences between
Dedicated Instances and Dedicated Hosts:

|                                           | Dedicated Host                                                                                                                        | Dedicated Instance                                                |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Dedicated physical server                 | Physical server with instance capacity fully dedicated to<br>your use.                                                                | Physical server that's dedicated to a single customer<br>account. |
| Instance capacity sharing                 | Can share instance capacity with other accounts.                                                                                      | Not supported                                                     |
| Billing                                   | Per-host billing                                                                                                                      | Per-instance billing                                              |
| Visibility of sockets, cores, and host ID | Provides visibility of the number of sockets and physical<br>cores                                                                    | No visibility                                                     |
| Host and instance affinity                | Allows you to consistently deploy your instances to the same<br>physical server over time                                             | Not supported                                                     |
| Targeted instance placement               | Provides additional visibility and control over how instances<br>are placed on a physical server                                      | Not supported                                                     |
| Automatic instance recovery               | Supported. For more information, see [Amazon EC2 Dedicated Host recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md"). | Supported                                                         |
| Bring Your Own License (BYOL)             | Supported                                                                                                                             | Partial support \*                                                |
| Capacity Reservations                     | Not supported                                                                                                                         | Supported                                                         |

\* Microsoft SQL Server with License Mobility through Software Assurance, and Windows Virtual Desktop
Access (VDA) licenses can be used with Dedicated Instance.

For more information about Dedicated Instances, see [Amazon EC2 Dedicated Instances](dedicated-instance.md "dedicated-instance.md").

## Dedicated Hosts restrictions

Before you allocate Dedicated Hosts, take note of the following limitations and
restrictions:

- To run RHEL and SUSE Linux on Dedicated Hosts, you must bring your own AMIs.
  You can't use the RHEL and SUSE Linux AMIs that are offered by AWS or that are
  available on AWS Marketplace with Dedicated Hosts. For more information about how to create your own
  AMI, see [Bring your own software licenses to Amazon EC2 Dedicated Hosts](dedicated-hosts-BYOL.md "dedicated-hosts-BYOL.md").

This restriction does not apply to hosts allocated for
high memory instances (`u-6tb1.metal`, `u-9tb1.metal`,
`u-12tb1.metal`, `u-18tb1.metal`, and
`u-24tb1.metal`). RHEL and SUSE Linux AMIs that are offered by
AWS or that are available on AWS Marketplace can be used with these hosts.

- There is a limit on the number of running Dedicated Hosts per instance family per AWS
  account per Region. Quotas apply to running instances only. If your instance is
  pending, stopping, or stopped, it does not count towards your quota. To view the
  quotas for your account, or to request a quota increase, use the [Service Quotas
  console](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas").
- Auto Scaling groups are supported when using a launch template that specifies a host
  resource group. For more information, see [Create a launch template using advanced settings](../../../autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.md "../../../autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.md") in the
  _Amazon EC2 Auto Scaling User Guide_.
- Amazon RDS instances are not supported.
- The AWS Free Usage tier is not available for Dedicated Hosts.
- Instance placement control refers to managing instance launches onto Dedicated Hosts.
  You can't launch Dedicated Hosts into placement groups.
- If you allocate a host for a virtualized instance type, you can't modify the
  instance type to a `.metal` instance type after the host is
  allocated. For example, if you allocate a host for the `m5.large`
  instance type, you can't modify the instance type to
  `m5.metal`.

Similarly, if you allocate a host for a `.metal` instance type, you
can't modify the instance type to a virtualized instance type after the host is
allocated. For example, if you allocate a host for the `m5.metal`
instance type, you can't modify the instance type to
`m5.large`.

###### Contents

- [Pricing and billing](dedicated-hosts-billing.md "dedicated-hosts-billing.md")
- [Instance capacity configurations](dedicated-hosts-limits.md "dedicated-hosts-limits.md")
- [Burstable instances on Dedicated Hosts](burstable-t3.md "burstable-t3.md")
- [Bring your own licenses](dedicated-hosts-BYOL.md "dedicated-hosts-BYOL.md")
- [Auto-placement and affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md")
- [Allocate a Dedicated Host](dedicated-hosts-allocating.md "dedicated-hosts-allocating.md")
- [Launch instances on a Dedicated Host](launching-dedicated-hosts-instances.md "launching-dedicated-hosts-instances.md")
- [Launch instances into a host resource group](launching-hrg-instances.md "launching-hrg-instances.md")
- [Modify Dedicated Host auto-placement](modify-host-auto-placement.md "modify-host-auto-placement.md")
- [Modify supported instance types](modify-host-support.md "modify-host-support.md")
- [Modify tenancy and affinity for an instance](moving-instances-dedicated-hosts.md "moving-instances-dedicated-hosts.md")
- [Release Dedicated Host](dedicated-hosts-releasing.md "dedicated-hosts-releasing.md")
- [Migrate to Nitro-based Amazon EC2 Dedicated Hosts](dh-migrate.md "dh-migrate.md")
- [Purchase a Dedicated Host Reservation](#purchasing-dedicated-host-reservations "#purchasing-dedicated-host-reservations")
- [Cross-account sharing](dh-sharing.md "dh-sharing.md")
- [Dedicated Hosts on Outposts](dh-outposts.md "dh-outposts.md")
- [Host recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md")
- [Host maintenance](dedicated-hosts-maintenance.md "dedicated-hosts-maintenance.md")
- [Monitor Dedicated Hosts](dedicated-hosts-monitoring.md "dedicated-hosts-monitoring.md")
- [Track configuration changes](dedicated-hosts-aws-config.md "dedicated-hosts-aws-config.md")

## Purchase Dedicated Host Reservations for Dedicated Host billing discounts

Dedicated Host Reservations provide you with a discount of up to 70 percent compared to On-Demand
Dedicated Host pricing. You must have active Dedicated Hosts allocated in your account before you can
purchase Dedicated Host Reservations. For more information, see [Dedicated Host Reservations](dedicated-hosts-billing.md#dedicated-host-reservations "dedicated-hosts-billing.md#dedicated-host-reservations").

Console

###### To purchase reservations

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Dedicated Hosts**,
   **Dedicated Host Reservations**, **Purchase
   Dedicated Host Reservation**.
3. On the **Find offerings** screen, do the
   following:
   1. For **Instance family**, select the
      instance family of the Dedicated Host for which to purchase the
      Dedicated Host Reservation.
   2. For **Payment option**, select and
      configure your preferred payment option.

4. Choose **Next**.
5. Select the Dedicated Hosts with which to associate the Dedicated Host Reservation, and then
   choose **Next**.
6. (_Optional_) Assign tags to the
   Dedicated Host Reservation.
7. Review your order and choose
   **Purchase**.

AWS CLI

###### To purchase reservations

1. Use the [describe-host-reservation-offerings](../../../cli/latest/reference/ec2/describe-host-reservation-offerings.md "../../../cli/latest/reference/ec2/describe-host-reservation-offerings.md") command
   to list the available offerings that match your needs. The
   following example lists the offerings that support instances in
   the `m4` instance family and have a one-year
   term.

The term is specified in seconds. A one-year term includes
31,536,000 seconds, and a three-year term includes
94,608,000 seconds.

```
aws ec2 describe-host-reservation-offerings \
    --filter Name=`instance-family`,Values=`m4` \
    --max-duration `31536000`
```

The command returns a list of offerings that match your
criteria. Note the ID of the offering to purchase. 2. Use the [purchase-host-reservation](../../../cli/latest/reference/ec2/purchase-host-reservation.md "../../../cli/latest/reference/ec2/purchase-host-reservation.md") command to purchase
the offering and provide the `offeringId` noted in
the previous step. The following example purchases the specified
reservation and associates it with a specific Dedicated Host that is
already allocated in the AWS account, and it applies a tag
with a key of `purpose` and a value of
`production`.

```
aws ec2 purchase-host-reservation \
    --offering-id `hro-03f707bf363b6b324` \
    --host-id-set `h-013abcd2a00cbd123` \
    --tag-specifications 'ResourceType=host-reservation,Tags={Key=purpose,Value=production}'
```

PowerShell

###### To purchase reservations

1. Use the [Get-EC2HostReservationOffering](../../../powershell/latest/reference/items/Get-EC2HostReservationOffering.md "../../../powershell/latest/reference/items/Get-EC2HostReservationOffering.md") cmdlet to
   list the available offerings that match your needs. The
   following examples list the offerings that support instances in
   the `m5` instance family and have a one-year
   term.

The term is specified in seconds. A one-year term includes
31,536,000 seconds, and a three-year term includes
94,608,000 seconds.

```
$filter = @{Name="instance-family"; Values="m5"}
Get-EC2HostReservationOffering `
    -Filter $filter `
    -MaxDuration `31536000`
```

The command returns a list of offerings that match your
criteria. Note the ID of the offering to purchase. 2. Use the [New-EC2HostReservation](../../../powershell/latest/reference/items/New-EC2HostReservation.md "../../../powershell/latest/reference/items/New-EC2HostReservation.md") cmdlet to
purchase the offering and provide the offering ID
noted in the previous step. The following example purchases the
specified reservation and associates it with a specific Dedicated Host
that is already allocated in the AWS account.

```
New-EC2HostReservation `
    -OfferingId `hro-03f707bf363b6b324` `
    -HostIdSet `h-013abcd2a00cbd123`
```
