# Use job attachments to share files

Use *job attachments* to make files not in shared directories available
 for your jobs, and to capture the output files if they are not written to shared directories.
 Job attachments uses Amazon S3 to shuttle files between hosts. Files are stored in S3 buckets, and
 you don't need to upload a file if its content hasn't changed.

You must use job attachments when running jobs on [service-managed fleets](../userguide/smf-manage.md "../userguide/smf-manage.md") because
 hosts don't share file system locations. Job attachments are also useful with [customer-managed
 fleets](../userguide/manage-cmf.md "../userguide/manage-cmf.md") when a job’s input or output files stored on a shared network file system, such
 as when your [job bundle](../userguide/submit-job-bundle.md "../userguide/submit-job-bundle.md") contains shell
 or Python scripts. 

 When you submit a job bundle with either the [Deadline Cloud CLI](https://pypi.org/project/deadline/ "https://pypi.org/project/deadline/") or a Deadline Cloud submitter, job
 attachments use the job’s storage profile and the queue’s required file system locations to
 identify the input files that are not on a worker host and should be uploaded to Amazon S3 as part of
 job submission. These storage profiles also help Deadline Cloud identify the output files in worker host
 locations that must be uploaded to Amazon S3 so that they are available to your workstation. 

 The job attachments examples use the farm, fleet, queues, and storage profiles
 configurations from [Sample project infrastructure](sample-project-infrastructure.md "sample-project-infrastructure.md") and [Storage profiles and path mapping](storage-profiles-and-path-mapping.md "storage-profiles-and-path-mapping.md"). You should go through those sections before this one. 

In the following examples, you use a sample job bundle as a starting point, then modify it
 to explore job attachment’s functionality. Job bundles are the best way for your jobs to use job
 attachments. They combine an [Open Job
 Description](https://github.com/OpenJobDescription/openjd-specifications/wiki "https://github.com/OpenJobDescription/openjd-specifications/wiki") job template in a directory with additional files that list the files and
 directories required by jobs using the job bundle. For more information about job bundles, see
 [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md").
