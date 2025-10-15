# Using files in your jobs

 Many of the jobs that you submit to AWS Deadline Cloud have input and output files. Your input files
 and output directories may be located on a combination of shared filesystems and local drives.
 Jobs need to locate the content in those locations. Deadline Cloud provides two features, [job attachments](../userguide/storage-job-attachments.md "../userguide/storage-job-attachments.md") and [storage
 profiles](../userguide/storage-shared.md "../userguide/storage-shared.md") that work together to help your jobs locate the files that they need. 

Job attachments offer several benefits


* Move files between hosts using Amazon S3
* Transfer files from your work station to worker hosts and vice versa
* Available for jobs in queues where you enable the feature
* Primarily used with service-managed fleets, but also compatible with customer-managed
 fleets.
 Use storage profiles to map the layout of shared filesystem locations on your workstation
 and worker hosts. This helps your jobs locate shared files and directories when their locations
 differ between your workstation and worker hosts, such as cross-platform setups with
 Windows-based workstations and Linux-based worker hosts. Storage profile's map of your
 filesystem configuration is also used by job attachments to identify the files it needs to
 shuttle between hosts through Amazon S3. 

 If you are not using job attachments, and you don't need to remap file and directory
 locations between workstations and worker hosts then you don't need to model your fileshares
 with storage profiles. 

###### Topics

* [Sample project infrastructure](sample-project-infrastructure.md "sample-project-infrastructure.md")
* [Storage profiles and path mapping](storage-profiles-and-path-mapping.md "storage-profiles-and-path-mapping.md")
