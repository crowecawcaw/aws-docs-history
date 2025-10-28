# Save and Access Metadata Information About Your

Processing Job

To save metadata from the processing container after exiting it, containers can
write UTF-8 encoded text to the `/opt/ml/output/message` file.
After the processing job enters any terminal status ("`Completed`",
"`Stopped`", or "`Failed`"), the
"`ExitMessage`" field in [`DescribeProcessingJob`](../APIReference/API_DescribeProcessingJob.md "../APIReference/API_DescribeProcessingJob.md") contains the first 1 KB of this
file. Access that initial part of file with a call to [`DescribeProcessingJob`](../APIReference/API_DescribeProcessingJob.md "../APIReference/API_DescribeProcessingJob.md"), which returns it through the
`ExitMessage` parameter. For failed processing jobs, you can use this
field to communicate information about why the processing container failed.

###### Important

Don't write sensitive data to the `/opt/ml/output/message`
file.

If the data in this file isn't UTF-8 encoded, the job fails and returns a
`ClientError`. If multiple containers exit with an
`ExitMessage,` the content of the `ExitMessage` from each
processing container is concatenated, then truncated to 1 KB.
