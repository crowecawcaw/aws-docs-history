# Getting output files from a job

This example shows how Deadline Cloud identifies the output files that your jobs generate, decides
whether to upload those files to Amazon S3, and how you can get those output files on your
workstation.

Use the `job_attachments_devguide_output` job bundle instead of the
`job_attachments_devguide` job bundle for this example. Start by making a copy of
the bundle in your AWS CloudShell environment from your clone of the Deadline Cloud samples GitHub
repository:

```
cp -r deadline-cloud-samples/job_bundles/job_attachments_devguide_output ~/
```

The important difference between this job bundle and the
`job_attachments_devguide` job bundle is the addition of a new job parameter in
the job template:

```
...
parameterDefinitions:
...
- name: OutputDir
  type: PATH
  objectType: DIRECTORY
  dataFlow: OUT
  default: ./output_dir
  description: This directory contains the output for all steps.
...
```

The `dataFlow` property of the parameter has the value `OUT`. Deadline Cloud
uses the value of `dataFlow` job parameters with a value of `OUT` or
`INOUT` as outputs of your job. If the file system location passed as a value to
these kinds of job parameters is remapped to a local file system location on the worker that
runs the job, then Deadline Cloud will look for new files at the location and upload those to Amazon S3 as
job outputs.

To see how this works, first start the Deadline Cloud worker agent in an AWS CloudShell tab. Let any
previously submitted jobs finish running. Then delete the job logs from the logs directory:

```
rm -rf ~/devdemo-logs/queue-*
```

Next, submit a job with this job bundle. After the worker running in your CloudShell
runs, look at the logs:

```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE1_ID to queue Q1's identifier
QUEUE1_ID=queue-`00112233445566778899aabbccddeeff`
# Change the value of WSALL_ID to the identifier of the WSAll storage profile
WSALL_ID=sp-`00112233445566778899aabbccddeeff`

deadline config set settings.storage_profile_id $WSALL_ID

deadline bundle submit --farm-id $FARM_ID --queue-id $QUEUE1_ID ./job_attachments_devguide_output
```

The log shows that a file was detected as output and uploaded to Amazon S3:

```
2024-07-17 02:13:10,873 INFO ----------------------------------------------
2024-07-17 02:13:10,873 INFO Uploading output files to Job Attachments
2024-07-17 02:13:10,873 INFO ----------------------------------------------
2024-07-17 02:13:10,873 INFO Started syncing outputs using Job Attachments
2024-07-17 02:13:10,955 INFO Found 1 file totaling 117.0 B in output directory: /sessions/session-7efa/assetroot-`assetroot-3751a`/output_dir
2024-07-17 02:13:10,956 INFO Uploading output manifest to DeadlineCloud/Manifests/farm-0011/queue-2233/job-4455/step-6677/task-6677-0/2024-07-17T02:13:10.835545Z_sessionaction-8899-1/c6808439dfc59f86763aff5b07b9a76c_output
2024-07-17 02:13:10,988 INFO Uploading 1 output file to S3: `s3BucketName`/DeadlineCloud/Data
2024-07-17 02:13:11,011 INFO Uploaded 117.0 B / 117.0 B of 1 file (Transfer rate: 0.0 B/s)
2024-07-17 02:13:11,011 INFO Summary Statistics for file uploads:
Processed 1 file totaling 117.0 B.
Skipped re-processing 0 files totaling 0.0 B.
Total processing time of 0.02281 seconds at 5.13 KB/s.
```

The log also shows that Deadline Cloud created a new manifest object in the Amazon S3 bucket configured
for use by job attachments on queue `Q1`. The name of the manifest object is
derived from the farm, queue, job, step, task, timestamp, and `sessionaction`
identifiers of the task that generated the output. Download this manifest file to see where
Deadline Cloud placed the output files for this task:

```
# The name of queue `Q1`'s job attachments S3 bucket
Q1_S3_BUCKET=$(
  aws deadline get-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID \
    --query 'jobAttachmentSettings.s3BucketName' | tr -d '"'
)

# Fill this in with the object name from your log
OBJECT_KEY="`DeadlineCloud/Manifests/...`"

aws s3 cp --quiet s3://$Q1_S3_BUCKET/$OBJECT_KEY /dev/stdout | jq .
```

The manifest looks like:

```
{
  "hashAlg": "xxh128",
  "manifestVersion": "2023-03-03",
  "paths": [
    {
      "hash": "34178940e1ef9956db8ea7f7c97ed842",
      "mtime": 1721182390859777,
      "path": "output_dir/output.txt",
      "size": 117
    }
  ],
  "totalSize": 117
}
```

This shows that the content of the output file is saved to Amazon S3 the same way that job
input files are saved. Similar to input files, the output file is stored in S3 with an object
name containing the hash of the file and the prefix `DeadlineCloud/Data`.

```
$ aws s3 ls --recursive s3://$Q1_S3_BUCKET | grep `34178940e1ef9956db8ea7f7c97ed842
2024-07-17 02:13:11 117 DeadlineCloud/Data/34178940e1ef9956db8ea7f7c97ed842.xxh128`
```

You can download the output of a job to your workstation using the Deadline Cloud monitor or the
Deadline Cloud CLI:

```
deadline job download-output --farm-id $FARM_ID --queue-id $QUEUE1_ID --job-id $JOB_ID
```

The value of the `OutputDir` job parameter in the submitted job is
`./output_dir`, so the output are downloaded to a directory called
`output_dir` within the job bundle directory. If you specified an absolute path
or different relative location as the value for `OutputDir`, then the output files
would be downloaded to that location instead.

```

$ deadline job download-output --farm-id $FARM_ID --queue-id $QUEUE1_ID --job-id $JOB_ID
`Downloading output from Job 'Job Attachments Explorer: Output'

Summary of files to download:
 /home/cloudshell-user/job_attachments_devguide_output/output_dir/output.txt (1 file)

You are about to download files which may come from multiple root directories. Here are a list of the current root directories:
[0] /home/cloudshell-user/job_attachments_devguide_output
> Please enter the index of root directory to edit, y to proceed without changes, or n to cancel the download (0, y, n) [y]:

Downloading Outputs [####################################] 100%
Download Summary:
 Downloaded 1 files totaling 117.0 B.
 Total download time of 0.14189 seconds at 824.0 B/s.
 Download locations (total file counts):
 /home/cloudshell-user/job_attachments_devguide_output (1 file)`
```
