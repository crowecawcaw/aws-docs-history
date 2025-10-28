# Understand traffic mirror session concepts

A _traffic mirror session_ establishes a relationship between a traffic mirror
source and a traffic mirror target. Traffic mirror sessions are evaluated based on the ascending
session number that you define when you create the session.

A traffic mirror session contains the following resources:

- A traffic mirror [source](#traffic-mirroring-sources "#traffic-mirroring-sources")
- A traffic mirror [target](traffic-mirroring-targets.md "traffic-mirroring-targets.md")
- A traffic mirror [filter](traffic-mirroring-filters.md "traffic-mirroring-filters.md")
  Each packet is mirrored once. However, you can use multiple traffic mirror sessions on
  the same mirror source. This is useful if you want to send a subset of the mirrored traffic
  from a traffic mirror source to multiple tools. For example, you can filter HTTP traffic in a
  higher priority traffic mirror session and send it to a specific monitoring appliance. At the
  same time, you can filter all other TCP traffic in a lower priority traffic mirror session and
  send it to another monitoring appliance.

## Traffic mirror sources

A traffic mirror source is the network interface of type `interface`. For example,
a network interface for an EC2 instance or an RDS instance.

A network interface can't be used as a traffic mirror source if the same Elastic network
interface is already in use in an existing traffic mirror target.

###### Note

If the source network interface gets deleted, AWS deletes the traffic mirroring session.

Traffic Mirroring is not available on all instance types.

Virtualized instance types in the following instance families are supported as Traffic Mirroring source:

- **General purpose:** A1 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i | M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-m2pro | T3 | T3a | T4g
- **Compute optimized:** C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7a | C7g | C7gd | C7i | C7i-flex
- **Memory optimized:** R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X1 | X1e | X2gd | X2idn | X2iedn | X2iezn | z1d
- **Storage optimized:** D2 | D3 | D3en | H1 | I3 | I3en | I4g | I4i | I7i | Im4gn | Is4gen
- **Accelerated computing:** DL1 | DL2q | F1 | F2 | G3 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | Gr6f | Inf1 | Inf2 | P3 | P3dn | P4d | P4de | P5 | P5e | Trn1 | Trn1n | VT1
- **High-performance computing:** Hpc6a | Hpc6id | Hpc7a
