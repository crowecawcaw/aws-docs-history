

# Share job bundles on your queue
<a name="share-job-bundles"></a>

After you build a custom job bundle, you can share it on your queue. Everyone who submits jobs to that queue can then use it. AWS Deadline Cloud stores shared bundles in the queue's job attachments Amazon S3 bucket. Because of that, a teammate who can submit jobs to the queue can also browse, download, and submit the bundles shared on it. You don't need to create any additional infrastructure or permissions.

A shared bundle is a single `.ojd` archive file that packages the job bundle directory. It contains the Open Job Description template, asset references, and any script or data files. Deadline Cloud stores the archives in the `job-bundles/` folder under the queue's job attachments root prefix, for example `s3://{{amzn-s3-demo-bucket}}/DeadlineCloud/job-bundles/`. The upload and download commands create and unpack the archive for you.

Your teammates browse, preview, and submit shared bundles with the job bundle browser. For instructions on browsing and submitting shared bundles, see [Load and submit shared job bundles](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/jobs-shared-bundles.html) in the *Deadline Cloud User Guide*. The rest of this page covers the sharing side: publishing bundles, working with them from the command line, and managing the bundles on a queue.

Before you begin, complete the following prerequisites:
+ Create a job bundle. For more information, see [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md).
+ Install the Deadline Cloud CLI and configure it with a default farm and queue. You can also pass the `--farm-id` and `--queue-id` options to each command.
+ Configure a queue with job attachments. For more information, see [Use job attachments to share files](build-job-attachments.md).

The following topics describe how to publish, use, and manage the bundles shared on your queue.

**Topics**
+ [Upload a job bundle](share-job-bundles-upload.md)
+ [Work with shared bundles from the command line](share-job-bundles-cli.md)
+ [Manage the bundles on your queue](share-job-bundles-manage.md)