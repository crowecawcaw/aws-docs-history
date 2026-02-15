# File storage for Deadline Cloud

Workers must have access to the storage locations that contain the input files necessary to
process a job, and to the locations that store the output. AWS Deadline Cloud provides two options for
storage locations:

- With _job attachments_, Deadline Cloud transfers the input and output files for
  your jobs back and forth between a workstation and Deadline Cloud workers. To enable the file transfers,
  Deadline Cloud uses an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account.

When you use job attachments with a Linux based service-managed fleet, you can enable a virtual file
system (VFS) to mount job attachments files and access them as needed instead of syncing them to
the worker at the start of the job.

- With _shared storage_, you use file sharing with your operating system
  to provide access to files.

When you use cross-platform shared storage, you can create a _storage
profile_ so that workers can map the path to files between two different operating
systems.

You can also integrate third-party cloud storage solutions, such as LucidLink, with
service-managed fleets using host configuration scripts. For more information, see [Set up
LucidLink with service managed fleet scripts for Deadline Cloud](https://aws.amazon.com/blogs/media/set-up-lucidlink-with-service-managed-fleet-scripts-for-aws-deadline-cloud/ "https://aws.amazon.com/blogs/media/set-up-lucidlink-with-service-managed-fleet-scripts-for-aws-deadline-cloud/") on the AWS for M&E
Blog.

###### Topics

- [Storage profiles in Deadline Cloud](storage-profile.md "storage-profile.md")
- [Job attachments in Deadline Cloud](storage-job-attachments.md "storage-job-attachments.md")
