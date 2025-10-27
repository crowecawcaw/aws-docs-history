# Submitting files with a job

With Deadline Cloud, you can enable job workflows to access input files that are unavailable in
shared file system locations on worker hosts. Job attachments allow rendering jobs to access
files residing only on a local workstation drive or a service-managed fleet environment. When
submitting a job bundle, you can include lists of input files and directories required by the
job. Deadline Cloud identifies these non-shared files, uploads them from the local machine to Amazon S3, and
downloads them to the worker host. It streamlines the process of transferring input assets to
render nodes, ensuring all required files are accessible for distributed job execution.

You can specify the files for jobs directly in the job bundle, use parameters in the job
template that you provide using environment variables or a script, and use the job's
`assets_references` file. You can use one of these methods or a combination of
all three. You can specify a storage profile for the bundle for the job so that it only
uploads files that have changed on the local workstation.

This section uses an example job bundle from GitHub to demonstrate how Deadline Cloud identifies
the files in your job to upload, how those files are organized in Amazon S3, and how they are made
available to the worker hosts processing your jobs.

###### Topics

- [How Deadline Cloud uploads files to
  Amazon S3](what-job-attachments-uploads-to-amazon-s3.md "what-job-attachments-uploads-to-amazon-s3.md")
- [How Deadline Cloud chooses
  the files to upload](how-job-attachments-decides-what-to-upload-to-amazon-s3.md "how-job-attachments-decides-what-to-upload-to-amazon-s3.md")
- [How jobs find job attachment
  input files](how-jobs-find-job-attachments-input-files.md "how-jobs-find-job-attachments-input-files.md")
