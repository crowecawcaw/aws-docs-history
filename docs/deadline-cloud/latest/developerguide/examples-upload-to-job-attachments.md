

# Upload files to Deadline Cloud job attachments
<a name="examples-upload-to-job-attachments"></a>

The [upload\_to\_job\_attachments](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/utility_scripts/upload_to_job_attachments) Python script on the GitHub website uploads files and directories from your workstation to a Deadline Cloud job attachments Amazon S3 bucket in content-addressable storage format. After files are uploaded, jobs that reference them don't need to upload them again. The script is useful for pre-populating job attachments with large datasets.

The script provides the following:
+ Recursive uploads of files or whole directories.
+ Multi-threaded transfers.
+ Automatic deduplication that skips files already in Amazon S3.
+ Retry logic with exponential backoff.
+ Two configuration modes: direct Amazon S3 specification or queue lookup.

Upload by specifying a queue:

```
python upload_to_job_attachments.py \
    --farm-id {{farm-1234567890abcdef}} \
    --queue-id {{queue-1234567890abcdef}} \
    --paths {{/path/to/files}} {{/path/to/directory}}
```

Or upload directly to an Amazon S3 bucket and prefix:

```
python upload_to_job_attachments.py \
    --s3-bucket {{my-bucket}} \
    --s3-prefix {{job-attachments}} \
    --paths {{/path/to/files}}
```

For high-bandwidth networks, increase `--threads` and `--max-concurrency`. For bandwidth-constrained environments, set `--max-bandwidth` to throttle uploads. For large files, increase `--multipart-chunksize`.

For a job-based alternative that copies files between Amazon S3 buckets, see [Copy an S3 prefix to job attachments on Deadline Cloud](examples-jb-copy-s3-to-attachments.md).