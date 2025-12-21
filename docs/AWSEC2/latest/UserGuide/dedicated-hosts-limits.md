# Amazon EC2 Dedicated Host instance capacity configurations

Dedicated Hosts support different configurations (physical cores, sockets, and VCPUs) that allow
you to run instances of different families and sizes.

When you allocate a Dedicated Host in your account, you can choose a configuration that supports
either a **single instance type**, or **multiple instance types** within the same instance family. The number of
instances that you can run on a host depends on the configuration you choose.

###### Contents

- [Single instance type support](#dh-single "#dh-single")
- [Multiple instance type support](#dh-multiple "#dh-multiple")

## Single instance type support

You can allocate a Dedicated Host that supports only one instance type. With this
configuration, every instance that you launch on the Dedicated Host must be of the same
instance type, which you specify when you allocate the host.

For example, you can allocate a host that supports only the
`m5.4xlarge` instance type. In this case, you can run only
`m5.4xlarge` instances on that host.

The number of instances that you can launch onto the host depends on the number of
physical cores provided by the host, and the number of cores consumed by the
specified instance type. For example, if you allocate a host for
`m5.4xlarge` instances, the host provides 48 physical cores, and each
`m5.4xlarge` instance consumes 8 physical cores. This means that you
can launch up to 6 instances on that host (_48 physical cores / 8 cores per
instance = 6 instances_).

## Multiple instance type support

You can allocate a Dedicated Host that supports multiple instance types within the same
instance family. This allows you to run different instance types on the same host,
as long as they're in the same instance family and the host has sufficient instance
capacity.

For example, you can allocate a host that supports different instance types within
the `R5` instance family. In this case, you can launch certain combinations of
`R5` instance types, such as `r5.large`,
`r5.xlarge`, `r5.2xlarge`, and `r5.4xlarge`, on
that host, within the host's physical core capacity.

The following instance families support Dedicated Hosts with multiple instance type
support:

- **General purpose:** A1 | M5 | M5n | M6i | M7i | T3
- **Compute optimized:** C5 | C5n | C6i | C7i
- **Memory optimized:** R5 | R5n | R6i | R7i

The number of instances you can run on the host depends on the number of physical
cores provided by the host, and the number of cores consumed by each instance type
that you run on the host. For example, if you allocate an `R5` host,
which provides 48 physical cores, and you run two `r5.2xlarge` instances
(_4 cores x 2 instances_) and three `r5.4xlarge`
instances (_8 cores x 3 instances_), those instances consume a
total of 32 cores, and you might be able to run certain combinations of `R5` instances as
long as they are within the remaining 16 cores.

However, for each instance family, there is a limit on the number of instances
that can be run for each instance type. For example, an `R5` Dedicated Host
supports a maximum of 2 `r5.8xlarge` instances, which uses 32 of the
physical cores. In this case, additional `R5` instances of smaller types
can then be used to fill the host to core capacity. For the supported number of
instance types for each instance family, see the [Dedicated Hosts Configuration
Table](https://aws.amazon.com/ec2/dedicated-hosts/pricing/#host-configuration "https://aws.amazon.com/ec2/dedicated-hosts/pricing/#host-configuration").

The following table shows example instance type combinations:

| Instance family | Example instance type combinations                                                                                                                                      |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R5              | • Example 1: 4 x `r5.4xlarge` + 4 x<br>`r5.2xlarge`<br>• Example 2: 1 x `r5.12xlarge` + 1 x<br>`r5.4xlarge` + 1 x<br>`r5.2xlarge` + 5 x `r5.xlarge`<br>+ 2 x `r5.large` |
| C5              | • Example 1: 1 x `c5.9xlarge` + 2 x<br>`c5.4xlarge` + 1 x<br>`c5.xlarge`<br>• Example 2: 4 x `c5.4xlarge` + 1 x<br>`c5.xlarge` + 2 x<br>`c5.large`                      |
| M5              | • Example 1: 4 x `m5.4xlarge` + 4 x<br>`m5.2xlarge`<br>• Example 2: 1 x `m5.12xlarge` + 1 x<br>`m5.4xlarge` + 1 x<br>`m5.2xlarge` + 5 x `m5.xlarge`<br>+ 2 x `m5.large` |

###### Considerations

Keep the following in mind when working with Dedicated Hosts that support multiple
instance types:

- Using multiple instance types on the same host is possible only within
  the same instance family.
- When mixing instance types, to maximize host utilization, we recommend
  launching larger instance types first followed by smaller instance types.
  - Depending on the combination and launch order of the instance
    types on a Dedicated Host, it may not be physically possible to
    maximize the utilization of the host. When mixing instance types
    on a host, some capacity might be available on the host but not
    usable. For example, you might see 16 vCPUs available on an r5n
    host but may not be able to launch a 4xlarge instance on the host
    even though r5n.4xlarge runs on 16 vCPUs.

###### Note

If you enable an A1 Dedicated Host for multiple instance types, you can
launch only a mix of `a1.xlarge` and `a1.2xlarge`
instances on that host. If you launch an `a1.medium` or
`a1.large` instance on that host, you will be restricted to
launching only more of that same instance type on the host. A single
`a1.4xlarge` instance consumes all capacity on the host. If you
require a host for either `a1.medium` or `a1.large`
instances, we recommend that you allocate separate hosts for those instance
types.
