# Build jobs to submit to Deadline Cloud

You submit jobs to Deadline Cloud using job bundles. A job bundle is a collection of files, including
an [Open Job Description
(OpenJD)](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications") job template and any asset files needed to render the job.

The job template describes how workers process and access the assets, and provides the
script that the worker runs. Job bundles enable artists, technical directors, and pipeline
developers to easily submit complex jobs to Deadline Cloud from their local workstations or on-premises
render farm. This is particularly useful for teams working on large-scale visual effects,
animation, or other media rendering projects that require scalable, on-demand computing
resources.

You can create the job bundle using the local file system to store files and a text editor
to create the job template. After creating the bundle, submit the job to Deadline Cloud using either the
Deadline Cloud CLI or a tool like a Deadline Cloud submitter

You can store your assets in a file system shared between your workers, or you can use Deadline Cloud
job attachments to automate moving assets to S3 buckets where your workers can access them. Job
attachments also help move the output from your jobs back to your workstations.

The following sections provide detailed instructions on creating and submitting job bundles
to Deadline Cloud.

###### Topics

- [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md")
- [Using files in your jobs](using-files-in-your-jobs.md "using-files-in-your-jobs.md")
- [Use job attachments to share files](build-job-attachments.md "build-job-attachments.md")
- [Create resource limits for jobs](build-job-limits.md "build-job-limits.md")
- [How to submit a job to Deadline Cloud](submit-jobs-how.md "submit-jobs-how.md")
- [Schedule jobs in Deadline Cloud](build-jobs-scheduling.md "build-jobs-scheduling.md")
- [Modify a job in Deadline Cloud](build-jobs-modifying.md "build-jobs-modifying.md")
