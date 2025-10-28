# Object storage, file storage, and file caching on Amazon EC2

Cloud file storage is a method for storing data in the cloud that provides servers and applications
access to data through shared file systems. This compatibility makes cloud file storage ideal for
workloads that rely on shared file systems and provides simple integration without code changes.

There are many file storage solutions that exist, ranging from a single node file server on a compute
instance using block storage as the underpinnings with no scalability or few redundancies to protect
the data, to a do-it-yourself clustered solution, to a fully-managed solution. The following content
introduces some of the storage services provided by AWS for use with Amazon EC2 instances.

###### Contents

- [Use Amazon S3 with Amazon EC2 instances](AmazonS3.md "AmazonS3.md")
- [Use Amazon EFS with Amazon EC2 Linux instances](AmazonEFS.md "AmazonEFS.md")
- [Use Amazon FSx with Amazon EC2 instances](storage_fsx.md "storage_fsx.md")
- [Use Amazon File Cache with Amazon EC2 instances](AmazonEFC.md "AmazonEFC.md")
