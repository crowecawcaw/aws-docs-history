# Software and architecture

| HPCSUS02: Have you complemented your architecture with a remote desktop<br>solution? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

By enabling remote visualization of simulation results, rather
than transferring and storing large datasets locally,
organizations can minimize network traffic, optimize resource
usage, and improve overall sustainability of their HPC operations.

## HPCSUS02-BP01 Use a VDI solution to reduce data movement

In
[SUS03-BP05
Use software patterns and architectures that best support data
access and storage patterns](../sustainability-pillar/sus_sus_software_a6.md "../sustainability-pillar/sus_sus_software_a6.md"), you understand how data is
used within your workload, consumed by your users, transferred,
and stored. For HPC workloads, Virtual Desktop Infrastructure
(VDI) technologies help you reduce network traffic between the
end-users' clients rather than transferring the entire data set
and duplicating storage on-premises. In addition, optimizing
data movement across the network reduces the total networking
resources required for the workload and lowers its environmental
impact.

### Implementation guidance

Use a remote visualization technology, such as Amazon DCV or
Amazon AppStream 2.0, to visualize the results of your
simulations without the need of copying back the results.

## Key AWS services

- [Amazon
  DCV](https://aws.amazon.com/hpc/dcv/ "https://aws.amazon.com/hpc/dcv/")
- [Amazon
  AppStream 2.0](https://aws.amazon.com/appstream2/ "https://aws.amazon.com/appstream2/")
- [Research
  and Engineering Studio on AWS](https://aws.amazon.com/hpc/res/ "https://aws.amazon.com/hpc/res/")

## Resources

- [Empowering
  Researchers to Run HPC Workloads on AWS with Research
  Gateway](https://aws.amazon.com/blogs/apn/empowering-researchers-to-run-hpc-workloads-on-aws-with-research-gateway/ "https://aws.amazon.com/blogs/apn/empowering-researchers-to-run-hpc-workloads-on-aws-with-research-gateway/")
