# File storage for Deadline Cloud

Workers must have access to the storage locations that contain the input files necessary to
 process a job, and to the locations that store the output. AWS Deadline Cloud provides two options for
 storage locations:


* With *job attachments*, Deadline Cloud transfers the input and output files for
 your jobs back and forth between a workstation and Deadline Cloud workers. To enable the file transfers,
 Deadline Cloud uses an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account.


When you use job attachments with a Linux based service-managed fleet, you can enable a virtual file
 system (VFS) to mount job attachments files and access them as needed instead of syncing them to
 the worker at the start of the job.
* With *shared storage*, you use file sharing with your operating system
 to provide access to files.


When you use cross-platform shared storage, you can create a *storage
 profile* so that workers can map the path to files between two different operating
 systems.
###### Topics

* [Storage profiles in Deadline Cloud](storage-profile.md "storage-profile.md")
* [Job attachments in Deadline Cloud](storage-job-attachments.md "storage-job-attachments.md")
