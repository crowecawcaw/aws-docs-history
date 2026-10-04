

# Job attachments
<a name="build-job-attachments"></a>

Job attachments is a Deadline Cloud feature that uses Amazon S3 to transfer a job's files, making the job's input files available to worker hosts and its output files available for download from the AWS Deadline Cloud monitor (Deadline Cloud monitor). The files are stored in an Amazon S3 bucket that belongs to the job's queue. When you create a queue in the Deadline Cloud console with default settings, the bucket and IAM policies that job attachments needs are configured for you.

Job attachments covers any job files that another shared storage solution doesn't cover. If your workers can reach a shared file system, define its locations as `SHARED` in a storage profile. For more information, see [Storage profiles and path mapping](storage-profiles-and-path-mapping.md). Job attachments transfers every input and output file outside those `SHARED` locations. It works the same way on [service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html) and [customer-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/manage-cmf.html).

Job attachments moves a job's files at four points in the job's lifecycle:

1. **When you submit the job.** The Deadline Cloud CLI or submitter reads the job bundle to find the job's input files. It hashes each file and compares the hash with the files already stored in the queue's bucket. It uploads only new or changed files.

1. **When a worker starts the job.** The worker downloads the job's input files into the session's working directory before the job's tasks run. If [virtual file system (VFS)](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/storage-virtual.html) support is enabled for the job, the worker mounts the input files through the virtual file system instead. The virtual file system loads each file from Amazon S3 when a task reads it.

1. **When each task finishes.** The worker checks the output locations that the job bundle defines. It uploads any new files that it finds there to the queue's bucket.

1. **When the job's output is retrieved.** To download all of a job's output files, open the context menu on the job in the Deadline Cloud monitor and choose **Download output**. To browse and download individual input or output files, choose **Browse attachments**. For more information, see [Download finished output](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/download-finished-output.html) and [Browse job attachments](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/browse-job-attachments.html) in the *Deadline Cloud User Guide*.

The following topics describe these points in more detail.

**Topics**
+ [Submitting files with a job](submitting-files-with-a-job.md)
+ [Getting output files from a job](getting-output-files-from-a-job.md)
+ [Using files from a step in a dependent step](using-files-output-from-a-step-in-a-dependent-step.md)