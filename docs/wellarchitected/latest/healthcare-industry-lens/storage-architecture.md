

# Storage architecture
<a name="storage-architecture"></a>


| HCL\_PERF4. How do you define and test storage performance requirements? | 
| --- | 
|   | 

 Healthcare requirements for compute are generally consistent with other industries. Guidance from the [Well-Architected Framework Storage Architecture Selection](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-storage.html) still applies. 

 AWS offers storage with extreme durability and performance. For example, [Amazon S3](https://aws.amazon.com/s3) provides 99.999999999% (11 nines) of data durability of objects over a given year. [Amazon EBS io2](https://aws.amazon.com/ebs/provisioned-iops/) block storage offers not only 99.999% durability, but up to 500 IOPS per GiB, enabling high performance and durability for healthcare workloads that require higher performance, such as transactional databases. 