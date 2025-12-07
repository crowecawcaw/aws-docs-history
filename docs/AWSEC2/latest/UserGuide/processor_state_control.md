# Processor state control for Amazon EC2 Linux instances

**C-states** control the sleep levels that a core can enter when it is idle. C-states are
numbered starting with C0 (the shallowest state where the core is totally awake and
executing instructions) and go to C6 (the deepest idle state where a core is powered
off).

**P-states** control the desired performance (in CPU frequency) from a core. P-states are
numbered starting from P0 (the highest performance setting where the core is allowed to use
Intel Turbo Boost Technology to increase frequency if possible), and they go from P1 (the
P-state that requests the maximum baseline frequency) to P15 (the lowest possible
frequency).

###### Note

AWS Graviton processors have built-in power saving modes and operate at a fixed frequency.
Therefore, they do not provide the ability for the operating system to control C-states and
P-states.

###### C-states and P-states

The following instance types provide the ability for an operating system to control
processor C-states and P-states:

- General purpose: `m4.10xlarge` | `m4.16xlarge`
- Compute optimized: `c4.8xlarge`
- Memory optimized: `r4.8xlarge` | `r4.16xlarge` |
  `x1.16xlarge` | `x1.32xlarge` | `x1e.8xlarge` | `x1e.16xlarge` |
  `x1e.32xlarge`
- Storage optimized: `d2.8xlarge` |
  `i3.8xlarge` | `i3.16xlarge` |
  `h1.8xlarge` | `h1.16xlarge`
- Accelerated computing: `f1.16xlarge` |
  `g3.16xlarge` |
  `p2.16xlarge` | `p3.16xlarge`
- Bare metal: All bare metal instances with Intel and AMD processors

###### C-states only

The following instance types provide the ability for an operating system to control
processor C-states:

- General purpose:
  `m5.12xlarge` | `m5.24xlarge` | `m5d.12xlarge` |
  `m5d.24xlarge` | `m5n.12xlarge` | `m5n.24xlarge` |
  `m5dn.12xlarge` | `m5dn.24xlarge` | `m5zn.6xlarge` |
  `m5zn.12xlarge` | `m6a.24xlarge` | `m6a.48xlarge` |
  `m6i.16xlarge` | `m6i.32xlarge` | `m6id.16xlarge` |
  `m6id.32xlarge` | `m6idn.16xlarge` | `m6in.16xlarge` |
  `m6in.32xlarge` | `m7a.medium` | `m7a.large` |
  `m7a.xlarge` | `m7a.2xlarge` | `m7a.4xlarge` |
  `m7a.8xlarge` | `m7a.12xlarge` | `m7a.16xlarge` |
  `m7a.24xlarge` | `m7a.32xlarge` | `m7a.48xlarge` |
  `m7i.large` | `m7i.xlarge` | `m7i.2xlarge` |
  `m7i.4xlarge` | `m7i.8xlarge` | `m7i.12xlarge` |
  `m7i.16xlarge` | `m7i.24xlarge` | `m7i.48xlarge` |
  `m8a.medium` | `m8a.large` | `m8a.xlarge` |
  `m8a.2xlarge` | `m8a.4xlarge` | `m8a.8xlarge` |
  `m8a.12xlarge` | `m8a.16xlarge` | `m8a.24xlarge` |
  `m8a.48xlarge` | `m8i.large` | `m8i.xlarge` |
  `m8i.2xlarge` | `m8i.4xlarge` | `m8i.8xlarge` |
  `m8i.12xlarge` | `m8i.16xlarge` | `m8i.24xlarge` |
  `m8i.32xlarge` | `m8i.48xlarge` | `m8i.96xlarge`
- Compute optimized:
  `c5.9xlarge` | `c5.12xlarge` | `c5.18xlarge` |
  `c5.24xlarge` | `c5a.24xlarge` | `c5ad.24xlarge` |
  `c5d.9xlarge` | `c5d.12xlarge` | `c5d.18xlarge` |
  `c5d.24xlarge` | `c5n.9xlarge` | `c5n.18xlarge` |
  `c6a.24xlarge` | `c6a.32xlarge` | `c6a.48xlarge` |
  `c6i.16xlarge` | `c6i.32xlarge` | `c6id.24xlarge` |
  `c6id.32xlarge` | `c6in.32xlarge` | `c7a.medium` |
  `c7a.large` | `c7a.xlarge` | `c7a.2xlarge` |
  `c7a.4xlarge` | `c7a.8xlarge` | `c7a.12xlarge` |
  `c7a.16xlarge` | `c7a.24xlarge` | `c7a.32xlarge` |
  `c7a.48xlarge` | `c7i.large` | `c7i.xlarge` |
  `c7i.2xlarge` | `c7i.4xlarge` | `c7i.8xlarge` |
  `c7i.12xlarge` | `c7i.16xlarge` | `c7i.24xlarge` |
  `c7i.48xlarge` | `c8a.medium` | `c8a.large` |
  `c8a.xlarge` | `c8a.2xlarge` | `c8a.4xlarge` |
  `c8a.8xlarge` | `c8a.12xlarge` | `c8a.16xlarge` |
  `c8a.24xlarge` | `c8a.48xlarge` | `c8i.large` |
  `c8i.xlarge` | `c8i.2xlarge` | `c8i.4xlarge` |
  `c8i.8xlarge` | `c8i.12xlarge` | `c8i.16xlarge` |
  `c8i.24xlarge` | `c8i.32xlarge` | `c8i.48xlarge` |
  `c8i.96xlarge`
- Memory optimized:
  `r5.12xlarge` | `r5.24xlarge` | `r5b.12xlarge` |
  `r5d.12xlarge` | `r5d.24xlarge` | `r5n.12xlarge` |
  `r5n.24xlarge` | `r5dn.12xlarge` | `r5dn.24xlarge` |
  `r6a.24xlarge` | `r6a.48xlarge` | `r6i.16xlarge` |
  `r6i.32xlarge` | `r6id.16xlarge` | `r6id.32xlarge` |
  `r6in.16xlarge` | `r6in.32xlarge` | `r7a.medium` |
  `r7a.large` | `r7a.xlarge` | `r7a.2xlarge` |
  `r7a.4xlarge` | `r7a.8xlarge` | `r7a.12xlarge` |
  `r7a.16xlarge` | `r7a.24xlarge` | `r7a.32xlarge` |
  `r7a.48xlarge` | `r7i.large` | `r7i.xlarge` |
  `r7i.2xlarge` | `r7i.4xlarge` | `r7i.8xlarge` |
  `r7i.12xlarge` | `r7i.16xlarge` | `r7i.24xlarge` |
  `r7i.48xlarge` | `r7iz.large` | `r7iz.xlarge` |
  `r7iz.2xlarge` | `r7iz.4xlarge` | `r7iz.8xlarge` |
  `r7iz.12xlarge` | `r7iz.16xlarge` | `r7iz.32xlarge` |
  `r8a.medium` | `r8a.large` | `r8a.xlarge` |
  `r8a.2xlarge` | `r8a.4xlarge` | `r8a.8xlarge` |
  `r8a.12xlarge` | `r8a.16xlarge` | `r8a.24xlarge` |
  `r8a.48xlarge` | `r8i.large` | `r8i.xlarge` |
  `r8i.2xlarge` | `r8i.4xlarge` | `r8i.8xlarge` |
  `r8i.12xlarge` | `r8i.16xlarge` | `r8i.24xlarge` |
  `r8i.32xlarge` | `r8i.48xlarge` | `r8i.96xlarge` |
  `u-3tb1.56xlarge` | `u-6tb1.56xlarge` | `u-6tb1.112xlarge` |
  `u-9tb1.112xlarge` | `u-12tb1.112xlarge` | `u-18tb1.112xlarge` |
  `u-24tb1.112xlarge` | `u7i-6tb.112xlarge` | `u7i-8tb.112xlarge` |
  `u7i-12tb.224xlarge` | `u7in-16tb.224xlarge` | `u7in-24tb.224xlarge` |
  `u7in-32tb.224xlarge` | `u7inh-32tb.480xlarge` | `x2idn.32xlarge` |
  `x2iedn.16xlarge` | `x2iedn.32xlarge` | `x2iezn.12xlarge` |
  `x8aedz.large` | `x8aedz.xlarge` | `x8aedz.3xlarge` |
  `x8aedz.6xlarge` | `x8aedz.12xlarge` | `x8aedz.24xlarge` |
  `z1d.6xlarge` | `z1d.12xlarge`
- Storage optimized:
  `d3en.12xlarge` | `dl1.24xlarge` | `i3en.12xlarge` |
  `i3en.24xlarge` | `i4i.16xlarge` | `i7i.large` |
  `i7i.xlarge` | `i7i.2xlarge` | `i7i.4xlarge` |
  `i7i.8xlarge` | `i7i.12xlarge` | `i7i.16xlarge` |
  `i7i.24xlarge` | `i7i.48xlarge` | `i7ie.large` |
  `i7ie.xlarge` | `i7ie.2xlarge` | `i7ie.3xlarge` |
  `i7ie.6xlarge` | `i7ie.12xlarge` | `i7ie.18xlarge` |
  `i7ie.24xlarge` | `i7ie.48xlarge` | `r5b.12xlarge` |
  `r5b.24xlarge`
- Accelerated computing:
  `dl1.24xlarge` | `f2.6xlarge` |
  `f2.12xlarge` | `f2.48xlarge` |
  `g5.24xlarge` | `g5.48xlarge` | `g6.24xlarge` |
  `g6.48xlarge` | `g6e.12xlarge` | `g6e.24xlarge` |
  `g6e.48xlarge` |
  `inf1.24xlarge` | `p3dn.24xlarge` |
  `p4d.24xlarge` | `p4de.24xlarge` | `p5.48xlarge` |
  `p5e.48xlarge` | `p5en.48xlarge` |
  `p6-b200.48xlarge` | `p6-b300.48xlarge` |
  `trn1.32xlarge` | `trn2.3xlarge` | `trn2.48xlarge` |
  `trn2a.3xlarge` | `trn2a.48xlarge` |
  `trn2n.3xlarge` | `trn2n.48xlarge` |
  `trn2p.48xlarge` | `trn2u.48xlarge` | `vt1.24xlarge`
  You might want to change the C-state or P-state settings to increase processor performance
  consistency, reduce latency, or tune your instance for a specific workload. The default
  C-state and P-state settings provide maximum performance, which is optimal for most
  workloads. However, if your application would benefit from reduced latency at the cost of
  higher single- or dual-core frequencies, or from consistent performance at lower frequencies
  as opposed to bursty Turbo Boost frequencies, consider experimenting with the C-state or
  P-state settings that are available to these instances.

For information about different processor configurations and how to monitor the effects of
your configuration for Amazon Linux, see [Processor state control for Amazon EC2 Amazon Linux
instance](../../../linux/al2/ug/processor_state_control.md "../../../linux/al2/ug/processor_state_control.md") in the _Amazon Linux 2 User Guide_. These procedures were written for, and apply to Amazon Linux; however, they might also work for other Linux distributions
with a Linux kernel of 3.9 or newer. For more information about other Linux distributions and processor state control, see your system-specific documentation.
