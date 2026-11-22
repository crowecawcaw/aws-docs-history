

# Managing high-availability (HA) pairs

Each FSx for ONTAP file system is powered by one or more high-availability (HA) pairs of file servers in an active-standby configuration. In this configuration, there is a preferred file server that actively serves traffic and a secondary file server that takes over if the active server is unavailable. FSx for ONTAP first-generation file systems are powered by one HA pair, which delivers up to 4 GBps of throughput capacity and 160,000 SSD IOPs. FSx for ONTAP second-generation and third-generation Multi-AZ file systems are powered by one HA pair as well, and they deliver up to 6 GBps of throughput capacity and 200,000 SSD IOPS, and up to 18 GBps of throughput capacity, and 720,000 SSD IOPS respectively. FSx for ONTAP second-generation and third-generation Single-AZ file systems are powered by up to 12 HA pairs. Second-generation Single-AZ file systems can deliver up to 72 GBps of throughput capacity and 2,400,000 SSD IOPS (6 GBps of throughput capacity and 200,000 SSD IOPS per HA pair), and third-generation Single-AZ file systems can deliver up to 216 GBps of throughput capacity and 8,640,000 SSD IOPS (18 GBps of throughput capacity and 720,000 SSD IOPS per HA pair). 

When you create your file system from the Amazon FSx console, Amazon FSx recommends the number of HA pairs that you should use based on your desired SSD storage. You can also manually choose the number of HA pairs based on your workload and performance requirements. We recommend that you use a single HA pair if your file system requirements are satisfied by up to 18 GBps of throughput capacity and 720,000 SSD IOPS, and multiple HA pairs if your workloads need higher levels of performance scalability. 

Each HA pair has one aggregate, which is a logical set of physical disks. 

**Note**  
You can add HA pairs to second-generation and third-generation Single-AZ file systems. For more information, see [Adding high-availability (HA) pairs](adding-HA-pairs.md). Otherwise, you can migrate data between file systems (with different HA pairs) using SnapMirror, AWS DataSync, or by restoring your data from a backup to a new file system. 