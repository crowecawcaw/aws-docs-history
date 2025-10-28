# Amazon EC2 Dedicated Host pricing and billing

The price for a Dedicated Host varies by payment option.

###### Payment Options

- [On-Demand Dedicated Hosts](#on-demand-dedicated-hosts "#on-demand-dedicated-hosts")
- [Dedicated Host Reservations](#dedicated-host-reservations "#dedicated-host-reservations")
- [Savings Plans](#dedicated-hosts-savings-plans "#dedicated-hosts-savings-plans")
- [Pricing for Windows Server on Dedicated Hosts](#dh-win-billing "#dh-win-billing")

## On-Demand Dedicated Hosts

On-Demand billing is automatically activated when you allocate a Dedicated Host to your
account.

The On-Demand price for a Dedicated Host varies by instance family and Region. You pay per
second (with a minimum of 60 seconds) for active Dedicated Host, regardless of the quantity or
the size of instances that you choose to launch on it. For
more information about On-Demand pricing, see [Amazon EC2 Dedicated Hosts On-Demand
Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/#on-demand "https://aws.amazon.com/ec2/dedicated-hosts/pricing/#on-demand").

You can release an On-Demand Dedicated Host at any time to stop accruing charges for it. For
information about releasing a Dedicated Host, see [Release an Amazon EC2 Dedicated Host](dedicated-hosts-releasing.md "dedicated-hosts-releasing.md").

## Dedicated Host Reservations

Dedicated Host Reservations provide a billing discount compared to running On-Demand Dedicated Hosts.
Reservations are available in three payment options:

- **No Upfront**—No Upfront Reservations
  provide you with a discount on your Dedicated Host usage over a term and do not
  require an upfront payment. Available in one-year and three-year terms. Only
  some instance families support the three-year term for No Upfront
  Reservations.
- **Partial Upfront**—A portion of the
  reservation must be paid upfront and the remaining hours in the term are
  billed at a discounted rate. Available in one-year and three-year
  terms.
- **All Upfront**—Provides the lowest
  effective price. Available in one-year and three-year terms and covers the
  entire cost of the term upfront, with no additional future charges.

You must have active Dedicated Hosts in your account before you can purchase reservations.
Each reservation can cover one or more hosts that support the same instance family
in a single Availability Zone. Reservations are applied to the instance family on
the host, not the instance size. If you have three Dedicated Hosts with different instances
sizes (`m4.xlarge`, `m4.medium`, and `m4.large`)
you can associate a single `m4` reservation with all those Dedicated Hosts. The
instance family and Availability Zone of the reservation must match that of the
Dedicated Hosts you want to associate it with.

When a reservation is associated with a Dedicated Host, the Dedicated Host can't be released until the
reservation's term is over.

For more information about reservation pricing, see [Amazon EC2 Dedicated Hosts
Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/#reservations "https://aws.amazon.com/ec2/dedicated-hosts/pricing/#reservations").

## Savings Plans

Savings Plans are a flexible pricing model that offers significant savings over
On-Demand Instances. With Savings Plans, you make a commitment to a consistent amount of usage,
in USD per hour, for a term of one or three years. This provides you with the
flexibility to use the Dedicated Hosts that best meet your needs and continue to save money,
instead of making a commitment to a specific Dedicated Host. For more information, see the
[AWS Savings
Plans User Guide](../../../savingsplans/latest/userguide.md "../../../savingsplans/latest/userguide.md").

###### Note

Savings Plans are not supported with `u-6tb1.metal`,
`u-9tb1.metal`, `u-12tb1.metal`,
`u-18tb1.metal`, and `u-24tb1.metal` Dedicated Hosts.

## Pricing for Windows Server on Dedicated Hosts

Subject to Microsoft licensing terms, you can bring your existing Windows Server
and SQL Server licenses to Dedicated Hosts. There is no additional charge for software usage
if you choose to bring your own licenses.

In addition, you can also use Windows Server AMIs provided by Amazon to run the
latest versions of Windows Server on Dedicated Hosts. This is common for scenarios where you
have existing SQL Server licenses eligible to run on Dedicated Hosts, but need Windows Server
to run the SQL Server workload. Windows Server AMIs provided by Amazon are supported
on current generation instance types only. For more information,
see [Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/#windows-dh "https://aws.amazon.com/ec2/dedicated-hosts/pricing/#windows-dh").
