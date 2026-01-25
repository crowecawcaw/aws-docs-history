# Example of how custom

routing works in Global Accelerator

As an example, let's say that you want to support 10,000 sessions where groups of users interact,
such as gaming sessions or VoIP call sessions, across 1,000
Amazon EC2 instances behind Global Accelerator. In this example, we'll specify a listener port range of
10001–20040 and a destination port range of 81–90. We'll say that we have
the four VPC subnets in us-east-1: subnet-1, subnet-2, subnet-3, and subnet-4.

In our example configuration, each VPC subnet has a block size of /24 so it can
support 251 Amazon EC2 instances. (Five addresses are reserved and unavailable from each
subnet, and these addresses are not mapped.) Each server running on each EC2
instance serves the following 10 ports, that we specified for the destination ports in
our endpoint group: 81-90. This means that we have 2510 ports (10 x 251) associated with
each subnet. Each port can be associated with a session.

Because we've specified 10 destination ports on each EC2 instance in our subnet,
Global Accelerator internally associates them with 10 listener ports that you can use to access EC2
instances. To illustrate this simply, we'll say that there's a block of listener ports
that starts with the first IP address of the endpoint subnet for the first set of 10,
and then moves to the next IP address for the next set of 10 listener ports.

###### Note

The mapping is actually not predictable like this, but we're using a sequential mapping
here to help to show how the port mapping works. To determine the actual mapping for
your listener port ranges, use the following API operations: [ListCustomRoutingPortMappings](../api/API_ListCustomRoutingPortMappings.md "../api/API_ListCustomRoutingPortMappings.md") and [ListCustomRoutingPortMappingsByDestination](../api/API_ListCustomRoutingPortMappingsByDestination.md "../api/API_ListCustomRoutingPortMappingsByDestination.md").

In our example, the first listener port is 10001. That port is associated with the
first subnet IP address, 192.0.2.4, and the first EC2 port, 81. The next listener port,
10002, is associated with the first subnet IP address, 192.0.2.4, and the second EC2
port, 82. The following table illustrates how this example mapping continues through the
last IP address of the first VPC subnet, and then on to the first IP address of the
second VPC subnet.

| Global Accelerator listener port | VPC subnet    | EC2 instance port |
| -------------------------------- | ------------- | ----------------- |
| `10001`                          | `192.0.2.4`   | `81`              |
| `10002`                          | `192.0.2.4`   | `82`              |
| `10003`                          | `192.0.2.4`   | `83`              |
| `10004`                          | `192.0.2.4`   | `84`              |
| `10005`                          | `192.0.2.4`   | `85`              |
| `10006`                          | `192.0.2.4`   | `86`              |
| `10007`                          | `192.0.2.4`   | `87`              |
| `10008`                          | `192.0.2.4`   | `88`              |
| `10009`                          | `192.0.2.4`   | `89`              |
| `10010`                          | `192.0.2.4`   | `90`              |
| `10011`                          | `192.0.2.5`   | `81`              |
| `10012`                          | `192.0.2.5`   | `82`              |
| `10013`                          | `192.0.2.5`   | `83`              |
| `10014`                          | `192.0.2.5`   | `84`              |
| `10015`                          | `192.0.2.5`   | `85`              |
| `10016`                          | `192.0.2.5`   | `86`              |
| `10017`                          | `192.0.2.5`   | `87`              |
| `10018`                          | `192.0.2.5`   | `88`              |
| `10019`                          | `192.0.2.5`   | `89`              |
| `10020`                          | `192.0.2.5`   | `90`              |
| `...`                            | `...`         | `...`             |
| `12501`                          | `192.0.2.244` | `81`              |
| `12502`                          | `192.0.2.244` | `82`              |
| `12503`                          | `192.0.2.244` | `83`              |
| `12504`                          | `192.0.2.244` | `84`              |
| `12505`                          | `192.0.2.244` | `85`              |
| `12506`                          | `192.0.2.244` | `86`              |
| `12507`                          | `192.0.2.244` | `87`              |
| `12508`                          | `192.0.2.244` | `88`              |
| `12509`                          | `192.0.2.244` | `89`              |
| `12510`                          | `192.0.2.244` | `90`              |
| `12511`                          | `192.0.3.4`   | `81`              |
| `12512`                          | `192.0.3.4`   | `82`              |
| `12513`                          | `192.0.3.4`   | `83`              |
| `12514`                          | `192.0.3.4`   | `84`              |
| `12515`                          | `192.0.3.4`   | `85`              |
| `12516`                          | `192.0.3.4`   | `86`              |
| `12517`                          | `192.0.3.4`   | `87`              |
| `12518`                          | `192.0.3.4`   | `88`              |
| `12519`                          | `192.0.3.4`   | `89`              |
| `12520`                          | `192.0.3.4`   | `90`              |
