# How Deadline Cloud uploads files to

Amazon S3

This example shows how Deadline Cloud uploads files from your workstation or worker host to Amazon S3
so that they can be shared. It uses a sample job bundle from GitHub and the Deadline Cloud CLI to
submit jobs.

Start by cloning the [Deadline Cloud samples GitHub
repository](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples") into your [AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") environment, then copy the
`job_attachments_devguide` job bundle into your home directory:

```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
cp -r deadline-cloud-samples/job_bundles/job_attachments_devguide ~/
```

Install the [Deadline Cloud CLI](https://pypi.org/project/deadline/ "https://pypi.org/project/deadline/") to submit
job bundles:

```
pip install deadline --upgrade
```

The `job_attachments_devguide` job bundle has a single step with a task that
runs a bash shell script whose file system location is passed as a job parameter. The job
parameter’s definition is:

```
...
- name: ScriptFile
  type: PATH
  default: script.sh
  dataFlow: IN
  objectType: FILE
...
```

The `dataFlow` property’s `IN` value tells job attachments that
the value of the `ScriptFile` parameter is an input to the job. The value of the
`default` property is a relative location to the job bundle’s directory, but it
can also be an absolute path. This parameter definition declares the `script.sh`
file in the job bundle’s directory as an input file required for the job to run.

Next, make sure that the Deadline Cloud CLI does not have a storage profile configured then
submit the job to queue `Q1`:

```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE1_ID to queue Q1's identifier
QUEUE1_ID=queue-`00112233445566778899aabbccddeeff`

deadline config set settings.storage_profile_id ''

deadline bundle submit --farm-id $FARM_ID --queue-id $QUEUE1_ID job_attachments_devguide/
```

The output from the Deadline Cloud CLI after this command is run looks like:

```
Submitting to Queue: Q1
...
Hashing Attachments  [####################################]  100%
Hashing Summary:
    Processed 1 file totaling 39.0 B.
    Skipped re-processing 0 files totaling 0.0 B.
    Total processing time of 0.0327 seconds at 1.19 KB/s.

Uploading Attachments  [####################################]  100%
Upload Summary:
    Processed 1 file totaling 39.0 B.
    Skipped re-processing 0 files totaling 0.0 B.
    Total processing time of 0.25639 seconds at 152.0 B/s.

Waiting for Job to be created...
Submitted job bundle:
   job_attachments_devguide/
Job creation completed successfully
job-74148c13342e4514b63c7a7518657005
```

When you submit the job, Deadline Cloud first hashes the `script.sh` file and then it
uploads it to Amazon S3.

Deadline Cloud treats the S3 bucket as content-addressable storage. Files are uploaded to S3
objects. The object name is derived from a hash of the file’s contents. If two files have
identical contents they have the same hash value regardless of where the files are located
or what they are named. This content-addressable storage enables Deadline Cloud to avoid uploading a file if it is already
available.

You can use the [AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") to see the objects that
were uploaded to Amazon S3:

```
# The name of queue `Q1`'s job attachments S3 bucket
Q1_S3_BUCKET=$(
  aws deadline get-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID \
    --query 'jobAttachmentSettings.s3BucketName' | tr -d '"'
)

aws s3 ls s3://$Q1_S3_BUCKET --recursive
```

Two objects were uploaded to S3:

- `DeadlineCloud/Data/87cb19095dd5d78fcaf56384ef0e6241.xxh128` – The
  contents of `script.sh`. The value
  `87cb19095dd5d78fcaf56384ef0e6241` in the object key is the hash of the
  file’s contents, and the extension `xxh128` indicates that the hash value was
  calculated as a 128 bit [xxhash](https://xxhash.com/ "https://xxhash.com/").
- `DeadlineCloud/Manifests/<farm-id>/<queue-id>/Inputs/<guid>/a1d221c7fd97b08175b3872a37428e8c_input`
  – The manifest object for the job submission. The values
  `<farm-id>`, `<queue-id>`, and
  `<guid>` are your farm identifier, queue identifier, and a random
  hexidecimal value. The value `a1d221c7fd97b08175b3872a37428e8c` in this
  example is a hash value calculated from the string
  `/home/cloudshell-user/job_attachments_devguide`, the directory where
  `script.sh` is located.
  The manifest object contains the information for the input files on a specific root
  path uploaded to S3 as part of the job’s submission. Download this manifest file (`aws
s3 cp s3://$Q1_S3_BUCKET/<objectname>`). Its contents are similar to:

```
{
    "hashAlg": "xxh128",
    "manifestVersion": "2023-03-03",
    "paths": [
        {
            "hash": "87cb19095dd5d78fcaf56384ef0e6241",
            "mtime": 1721147454416085,
            "path": "script.sh",
            "size": 39
        }
    ],
    "totalSize": 39
}
```

This indicates that the file `script.sh` was uploaded, and the hash of that
file’s contents is `87cb19095dd5d78fcaf56384ef0e6241`. This hash value matches
the value in the object name
`DeadlineCloud/Data/87cb19095dd5d78fcaf56384ef0e6241.xxh128`. It is used by
Deadline Cloud to know which object to download for this file’s contents.

The full schema for this file is [available in GitHub](https://github.com/aws-deadline/deadline-cloud/blob/mainline/src/deadline/job_attachments/asset_manifests/v2023_03_03/validate.py "https://github.com/aws-deadline/deadline-cloud/blob/mainline/src/deadline/job_attachments/asset_manifests/v2023_03_03/validate.py").

When you use the [CreateJob operation](../APIReference/API_CreateJob.md "../APIReference/API_CreateJob.md")
you can set the location of the manifest objects. You can use the [GetJob
operation](../APIReference/API_GetJob.md "../APIReference/API_GetJob.md") to see the location:

```
{
    "attachments": {
        "file system": "COPIED",
        "manifests": [
            {
                "inputManifestHash": "5b0db3d311805ea8de7787b64cbbe8b3",
                "inputManifestPath": "<farm-id>/<queue-id>/Inputs/<guid>/a1d221c7fd97b08175b3872a37428e8c_input",
                "rootPath": "/home/cloudshell-user/job_attachments_devguide",
                "rootPathFormat": "posix"
            }
        ]
    },
    ...
}
```
