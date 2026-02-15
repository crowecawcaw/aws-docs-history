# Traffic Mirroring quotas

The following are the quotas for Traffic Mirroring for your AWS account.

###### Contents

- [Sessions](#traffic-mirroring-quotas-sessions "#traffic-mirroring-quotas-sessions")
- [Targets](#traffic-mirroring-quotas-targets "#traffic-mirroring-quotas-targets")
- [Filters](#traffic-mirroring-quotas-filters "#traffic-mirroring-quotas-filters")
- [Throughput](#traffic-mirroring-quotas-throughput "#traffic-mirroring-quotas-throughput")
- [Packets](#traffic-mirroring-quotas-packets "#traffic-mirroring-quotas-packets")
- [Sources](#traffic-mirroring-quotas-sources "#traffic-mirroring-quotas-sources")

## Sessions

| Name                                                                   | Default   | Adjustable     |
| ---------------------------------------------------------------------- | --------- | -------------- |
| Maximum number of sessions per account                                 | 10,000    | No             |
| Maximum number of sessions per source network interface                | 3         | No             |
| Maximum number of sessions for a single Gateway Load Balancer endpoint | Unlimited | Not applicable |

## Targets

| Name                                  | Default | Adjustable |
| ------------------------------------- | ------- | ---------- |
| Maximum number of targets per account | 10,000  | No         |

## Filters

| Name                                                    | Default | Adjustable |
| ------------------------------------------------------- | ------- | ---------- |
| Maximum number of filters per account                   | 10,000  | No         |
| Maximum number of sessions per source network interface | 3       | No         |
| Maximum number of filter rules per filter               | 10      | No         |

## Throughput

| Name                                                               | Default  | Adjustable |
| ------------------------------------------------------------------ | -------- | ---------- |
| Maximum throughput through a single Gateway Load Balancer endpoint | 100 Gbps | No         |

## Packets

| Name                                                        | Default | Adjustable |
| ----------------------------------------------------------- | ------- | ---------- |
| Maximum number of MTUs for a Gateway Load Balancer endpoint | 8,500   | No         |

## Sources

| Name                                                         | Default                                                                              | Adjustable |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------- |
| Maximum number of sources per Network Load Balancer          | No limit                                                                             | No         |
| Maximum number of sources per Gateway Load Balancer endpoint | No limit                                                                             | No         |
| Maximum number of sources per target                         | 100 or 10 depending on the instance type. For more information, see the list below 1 | No         |

1 The following instance types support up to 100 sources per target. All other instance types support up to 10 sources per target.

- **General Purpose:** m5.24xlarge | m5d.24xlarge | m5dn.24xlarge | m5n.24xlarge | m5zn.12xlarge | m6a.48xlarge | m6g.16xlarge | m6gd.16xlarge | m6i.32xlarge | m6id.32xlarge | m6idn.32xlarge | m6in.32xlarge | m7a.48xlarge | m7i.48xlarge | m8a.48xlarge | m8azn.24xlarge | m8g.48xlarge | m8gb.24xlarge | m8gb.48xlarge | m8gd.48xlarge | m8gn.24xlarge | m8gn.48xlarge | m8i.96xlarge | m8id.96xlarge
- **Compute Optimized:** c5.18xlarge | c5.24xlarge | c5d.18xlarge | c5d.24xlarge | c5n.18xlarge | c6a.48xlarge | c6g.16xlarge | c6gd.16xlarge | c6gn.16xlarge | c6i.32xlarge | c6id.32xlarge | c6in.32xlarge | c7a.48xlarge | c7gn.16xlarge | c7i.48xlarge | c8a.48xlarge | c8g.48xlarge | c8gb.24xlarge | c8gb.48xlarge | c8gd.48xlarge | c8gn.24xlarge | c8gn.48xlarge | c8i.96xlarge | c8id.96xlarge
- **Memory Optimized:** r5.24xlarge | r5b.24xlarge | r5d.24xlarge | r5dn.24xlarge | r5n.24xlarge | r6a.48xlarge | r6g.16xlarge | r6gd.16xlarge | r6i.32xlarge | r6id.32xlarge | r6idn.32xlarge | r6in.32xlarge | r7a.48xlarge | r7i.48xlarge | r7iz.32xlarge | r8a.48xlarge | r8g.48xlarge | r8gb.24xlarge | r8gb.48xlarge | r8gd.48xlarge | r8gn.24xlarge | r8gn.48xlarge | r8i.96xlarge | r8id.96xlarge | u-6tb1.56xlarge | u-6tb1.112xlarge | u-9tb1.112xlarge | u-12tb1.112xlarge | u-18tb1.112xlarge | u-24tb1.112xlarge | u7i-6tb.112xlarge | u7i-8tb.112xlarge | u7i-12tb.224xlarge | u7in-16tb.224xlarge | u7in-24tb.224xlarge | u7in-32tb.224xlarge | u7inh-32tb.480xlarge | x2gd.16xlarge | x2idn.32xlarge | x2iedn.32xlarge | x2iezn.12xlarge | x8g.48xlarge | x8aedz.24xlarge | x8i.96xlarge | z1d.12xlarge
- **Storage Optimized:** i3en.24xlarge | i4g.16xlarge | i4i.32xlarge | i7i.48xlarge | i7ie.48xlarge | i8g.48xlarge | i8ge.48xlarge | im4gn.16xlarge
- **Accelerated Computing:** dl1.24xlarge | dl2q.24xlarge | f2.48xlarge | g5.48xlarge | g5g.16xlarge | g6.48xlarge | g6e.12xlarge | g6e.24xlarge | g6e.48xlarge | g7e.12xlarge | g7e.24xlarge | g7e.48xlarge | inf1.24xlarge | inf2.48xlarge | p3dn.24xlarge | p4d.24xlarge | p4de.24xlarge | p5.4xlarge | p5.48xlarge | p5e.48xlarge | p5en.48xlarge | p6-b200.48xlarge | p6-b300.48xlarge | p6e-gb200.36xlarge | trn1.32xlarge | trn1n.32xlarge | trn2.48xlarge | trn2u.48xlarge | vt1.24xlarge
- **High Performance Computing:** hpc6a.48xlarge | hpc6id.32xlarge | hpc7a.12xlarge | hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96xlarge | hpc7g.4xlarge | hpc7g.8xlarge | hpc7g.16xlarge
