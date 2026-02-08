# Storage

Optimizing storage costs is essential for Microsoft workloads on
AWS, as storage represents a significant portion of infrastructure
expenses. AWS offers various cost-effective storage solutions, from
newer generation EBS volumes (gp3) to fully managed services like
Amazon FSx for Windows File Server and FSx for ONTAP. By
implementing proper lifecycle management for volumes and snapshots,
and choosing the right storage solutions for specific workload
requirements, organizations can significantly reduce storage costs
while maintaining or improving performance.

| MSFTCOST05: How do you save on storage for your Microsoft<br>workload? |
| ---------------------------------------------------------------------- |
|                                                                        |

The storage layer is a critical architecture component for most
applications, including Microsoft workloads. Exploring the
compatible Amazon storage offers can help you provide the required
performance to your workloads and save costs. Constantly managing
storage resources avoids unused resources, over-provisioning, and
keeps the workloads performant.

###### Best practices

- [MSFTCOST05-BP01 Migrate Amazon EBS volumes from gp2 to
  gp3](msftcost05-bp01.md "msftcost05-bp01.md")
- [MSFTCOST05-BP02 Control Amazon EBS volumes or snapshots
  lifecycle](msftcost05-bp02.md "msftcost05-bp02.md")
- [MSFTCOST05-BP03 Use Amazon FSx for NetApp ONTAP](msftcost05-bp03.md "msftcost05-bp03.md")
- [MSFTCOST05-BP04 Use
  Amazon FSx for Windows File Server](msftcost05-bp04.md "msftcost05-bp04.md")
