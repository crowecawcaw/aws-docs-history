# Use cases for directory buckets

Directory buckets support bucket creation in the following bucket location types: Availability Zone or Local Zone. 

For low latency use cases, you can create a directory bucket in a single Availability Zone to store data. 
 Directory buckets in Availability Zones support the S3 Express One Zone storage class. 
 S3 Express One Zone storage class is recommended if your application is performance sensitive and benefits from
 single-digit millisecond `PUT` and `GET` latencies. To learn more about creating directory buckets in Availability Zones, see [High performance workloads](directory-bucket-high-performance.md "directory-bucket-high-performance.md"). 


 For data residency use cases, you can create a directory bucket in a single AWS Dedicated Local Zone (DLZ) to store data. 
 Directory buckets in Local Zones support the S3 One Zone-Infrequent Access (S3 One Zone-IA; Z-IA) storage class.
 
 To learn more about creating directory buckets in Local Zones, see [Data residency workloads](directory-bucket-data-residency.md "directory-bucket-data-residency.md").

###### Topics

* [High performance workloads](directory-bucket-high-performance.md "directory-bucket-high-performance.md")
* [Data residency workloads](directory-bucket-data-residency.md "directory-bucket-data-residency.md")
