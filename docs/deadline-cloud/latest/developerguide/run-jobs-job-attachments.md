# Submit jobs with job attachments in Deadline Cloud

Many farms use shared filesystems to share files between the hosts that submit jobs and
 those that run jobs. For example, in the previous `simple_file_job` example, the
 local filesystem is shared between the AWS CloudShell terminal windows, which run in tab one where
 you submit the job, and tab two where you run the worker agent. 

A shared filesystem is advantageous when the submitter workstation and the worker hosts
 are on the same local area network. If you store your data on premises near the workstations
 that access it, then using a cloud-based farm means you have to share your filesystems over
 a high-latency VPN or synchronize your filesystems in the cloud. Neither of these options
 are easy to set up or operate. 

AWS Deadline Cloud offers a simple solution with *job
 attachments*, which are similar to email attachments. With job attachments, you
 attach data to your job. Then, Deadline Cloud handles the details of transferring and storing your
 job data in Amazon Simple Storage Service (Amazon S3) buckets.

Content creation workflows are often iterative, meaning a user submits jobs with a small
 subset of modified files. Because Amazon S3 buckets store job attachments in a
 content-addressable storage, the name of each object is based on the hash of the object's
 data and the contents of a directory tree are stored in a manifest file format attached to a
 job. 

Before you can follow the procedures in this section, you must complete the
 following:


* [Create a Deadline Cloud farm](create-a-farm.md "create-a-farm.md")
* [Run the Deadline Cloud worker agent](run-worker.md "run-worker.md")
To run jobs with job attachments, complete the following steps.

###### Topics

* [Add a job attachments configuration to your
 queue](#job-attachments-config "#job-attachments-config")
* [Submit simple\_file\_job with job
 attachments](#submit-job-attachments "#submit-job-attachments")
* [Understanding how job attachments are stored
 in Amazon S3](#job-attachments-in-depth "#job-attachments-in-depth")
* [Next steps](#run-jobs-job-attachments-next "#run-jobs-job-attachments-next")

## Add a job attachments configuration to your
 queue


To enable job attachments in your queue, add a job attachments configuration to the
 queue resource in your account.
 


###### To add a job attachments configuration to your queue

1. Choose your first CloudShell tab, then enter one of the following commands
 to use an Amazon S3 bucket for job attachments.


	* If you don't have an existing private Amazon S3 bucket, you can create and
	 use a new S3 bucket.
	
	
	
	```
	`DEV_FARM_BUCKET=$(echo $DEV_FARM_NAME \
	 | tr '[:upper:]' '[:lower:]')-$(xxd -l 16 -p /dev/urandom)
	if [ "$AWS_REGION" == "us-east-1" ]; then LOCATION_CONSTRAINT=
	else LOCATION_CONSTRAINT="--create-bucket-configuration \
	 LocationConstraint=${AWS_REGION}"
	fi
	aws s3api create-bucket \
	 $LOCATION_CONSTRAINT \
	 --acl private \
	 --bucket ${DEV_FARM_BUCKET}`
	```
	* If you already have a private Amazon S3 bucket, you can use it by replacing
	 ``MY_BUCKET_NAME`` with the
	 name of your bucket.
	
	
	
	```
	`DEV_FARM_BUCKET=`MY_BUCKET_NAME``
	```
2. After you create or choose your Amazon S3 bucket, add the bucket name to
 `~/.bashrc` to make the bucket available for other terminal
 sessions.



```
`echo "DEV_FARM_BUCKET=$DEV_FARM_BUCKET" >> ~/.bashrc
 source ~/.bashrc`
```
3. Create an AWS Identity and Access Management (IAM) role for the queue.



```
`aws iam create-role --role-name "${DEV_FARM_NAME}QueueRole" \
 --assume-role-policy-document \
 '{
 "Version": "2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.deadline.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }'
aws iam put-role-policy \
 --role-name "${DEV_FARM_NAME}QueueRole" \
 --policy-name S3BucketsAccess \
 --policy-document \
 '{
 "Version": "2012-10-17", 
 "Statement": [
 {
 "Action": [
 "s3:GetObject*",
 "s3:GetBucket*",
 "s3:List*",
 "s3:DeleteObject*",
 "s3:PutObject",
 "s3:PutObjectLegalHold",
 "s3:PutObjectRetention",
 "s3:PutObjectTagging",
 "s3:PutObjectVersionTagging",
 "s3:Abort*"
 ],
 "Resource": [
 "arn:aws:s3:::'$DEV_FARM_BUCKET'",
 "arn:aws:s3:::'$DEV_FARM_BUCKET'/*"
 ],
 "Effect": "Allow"
 }
 ]
 }'`
```
4. Update your queue to include the job attachments settings and the IAM
 role.



```
`QUEUE_ROLE_ARN="arn:aws:iam::$(aws sts get-caller-identity \
 --query "Account" --output text):role/${DEV_FARM_NAME}QueueRole"
aws deadline update-queue \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --role-arn $QUEUE_ROLE_ARN \
 --job-attachment-settings \
 '{
 "s3BucketName": "'$DEV_FARM_BUCKET'",
 "rootPrefix": "JobAttachments"
 }'`
```
5. Confirm that you updated your queue.



```
`deadline queue get`

```

Output such as the following is shown:



```
...
jobAttachmentSettings:
  s3BucketName: DEV_FARM_BUCKET
  rootPrefix: JobAttachments
roleArn: arn:aws:iam::ACCOUNT_NUMBER:role/DeveloperFarmQueueRole
...
```

## Submit simple\_file\_job with job
 attachments


When you use job attachments, job bundles must give Deadline Cloud enough information to
 determine the job's data flow, such as using `PATH` parameters. In the case
 of the simple\_file\_job, you edited the `template.yaml` file to
 tell Deadline Cloud that the data flow is in the input file and output file.


After you've added the job attachments configuration to your queue, you can submit the
 simple\_file\_job sample with job attachments. After you do this, you can view the logging
 and job output to confirm that the simple\_file\_job with job attachments
 is working.


###### To submit the simple\_file\_job job bundle with job attachments

1. Choose your first CloudShell tab, then open the
 `JobBundle-Samples` directory.
2. ```
`cd ~/deadline-cloud-samples/job_bundles/`

```
3. Submit simple\_file\_job to the queue. When prompted to confirm the upload,
 enter `y`.



```
`deadline bundle submit simple_file_job \
 -p InFile=simple_job/template.yaml \
 -p OutFile=hash-jobattachments.txt`

```
4. To view the job attachments data transfer session log output, run the
 following command.



```
`JOB_ID=$(deadline config get defaults.job_id)
SESSION_ID=$(aws deadline list-sessions \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --job-id $JOB_ID \
 --query "sessions[0].sessionId" \
 --output text)
cat ~/demoenv-logs/$DEV_QUEUE_ID/$SESSION_ID.log`

```
5. List the session actions that were run within the session.



```
`aws deadline list-session-actions \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --job-id $JOB_ID \
 --session-id $SESSION_ID`

```

Output such as the following is shown:



```
{
    "sessionactions": [
        {
            "sessionActionId": "sessionaction-123-0",
            "status": "SUCCEEDED",
            "startedAt": "<timestamp>",
            "endedAt": "<timestamp>",
            "progressPercent": 100.0,
            "definition": {
                "syncInputJobAttachments": {}
            }
        },
        {
            "sessionActionId": "sessionaction-123-1",
            "status": "SUCCEEDED",
            "startedAt": "<timestamp>",
            "endedAt": "<timestamp>",
            "progressPercent": 100.0,
            "definition": {
                "taskRun": {
                    "taskId": "task-abc-0",
                    "stepId": "step-def"
                }
            }
        }
    ]
}

```

The first session action downloaded the input job attachments, while the
 second action runs the task like in previous steps and then uploaded the output
 job attachments.
6. List the output directory.



```
`ls *.txt`

```

Output such as `hash.txt` exists in the directory,
 but
 `hash-jobattachments.txt` doesn't exist because the output file
 from the job hasn't been downloaded yet.
7. Download the output from the most recent job.



```
`deadline job download-output`

```
8. View the output of the downloaded file.



```
`cat hash-jobattachments.txt`

```

Output such as the following is shown:



```
eaa2df5d34b54be5ac34c56a24a8c237b8487231a607eaf530a04d76b89c9cd3  /tmp/openjd/session-123/assetroot-abc/simple_job/template.yaml

```

## Understanding how job attachments are stored
 in Amazon S3


You can use the AWS Command Line Interface (AWS CLI) to upload or download data for job attachments,
 which are stored in Amazon S3 buckets. Understanding how Deadline Cloud stores job attachments on Amazon S3
 will help when you develop workloads and pipeline integrations.
 


###### To inspect how Deadline Cloud job attachments are stored in Amazon S3

1. Choose your first CloudShell tab, then open the job bundle samples
 directory.



```
`cd ~/deadline-cloud-samples/job_bundles/`

```
2. Inspect the job properties.



```
`deadline job get`

```

Output such as the following is shown:



```
parameters:
  Message:
    string: Welcome to AWS Deadline Cloud!
  InFile:
    path: /home/cloudshell-user/deadline-cloud-samples/job_bundles/simple_job/template.yaml
  OutFile:
    path: /home/cloudshell-user/deadline-cloud-samples/job_bundles/hash-jobattachments.txt
attachments:
  manifests:
  - rootPath: /home/cloudshell-user/deadline-cloud-samples/job_bundles/
    rootPathFormat: posix
    outputRelativeDirectories:
    - .
    inputManifestPath: farm-3040c59a5b9943d58052c29d907a645d/queue-cde9977c9f4d4018a1d85f3e6c1a4e6e/Inputs/f46af01ca8904cd8b514586671c79303/0d69cd94523ba617c731f29c019d16e8_input.xxh128
    inputManifestHash: f95ef91b5dab1fc1341b75637fe987ee
  fileSystem: COPIED
```

The attachments field contains a list of manifest structures that describe
 input and output data paths that the job uses when it runs. Look at
 `rootPath` to see the local directory path on the machine that
 submitted the job. To view the Amazon S3 object suffix that contains a manifest file,
 review the `inputManifestFile`. The manifest file contains metadata
 for a directory tree snapshot of the job's input data.
3. Pretty-print the Amazon S3 manifest object to see the input directory structure for
 the job.



```
`MANIFEST_SUFFIX=$(aws deadline get-job \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --job-id $JOB_ID \
 --query "attachments.manifests[0].inputManifestPath" \
 --output text)
 aws s3 cp s3://$DEV_FARM_BUCKET/JobAttachments/Manifests/$MANIFEST_SUFFIX - | jq .`

```

Output such as the following is shown:



```
{
     "hashAlg": "xxh128",
     "manifestVersion": "2023-03-03",
     "paths": [
     {
         "hash": "2ec297b04c59c4741ed97ac8fb83080c",
         "mtime": 1698186190000000,
         "path": "simple_job/template.yaml",
         "size": 445
     }
     ],
     "totalSize": 445
 }
```
4. Construct the Amazon S3 prefix that holds manifests for the output job attachments
 and list the object under it.



```
`SESSION_ACTION=$(aws deadline list-session-actions \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --job-id $JOB_ID \
 --session-id $SESSION_ID \
 --query "sessionActions[?definition.taskRun != null] | [0]")
STEP_ID=$(echo $SESSION_ACTION | jq -r .definition.taskRun.stepId)
TASK_ID=$(echo $SESSION_ACTION | jq -r .definition.taskRun.taskId)
TASK_OUTPUT_PREFIX=JobAttachments/Manifests/$DEV_FARM_ID/$DEV_QUEUE_ID/$JOB_ID/$STEP_ID/$TASK_ID/
aws s3api list-objects-v2 --bucket $DEV_FARM_BUCKET --prefix $TASK_OUTPUT_PREFIX`

```

The output job attachments are not directly referenced from the job resource
 but are instead placed in an Amazon S3 bucket based on farm resource IDs.
5. Get the newest manifest object key for the specific session action id, then
 pretty-print the manifest objects.



```
`SESSION_ACTION_ID=$(echo $SESSION_ACTION | jq -r .sessionActionId)
 MANIFEST_KEY=$(aws s3api list-objects-v2 \
 --bucket $DEV_FARM_BUCKET \
 --prefix $TASK_OUTPUT_PREFIX \
 --query "Contents[*].Key" --output text \
 | grep $SESSION_ACTION_ID \
 | sort | tail -1)
 MANIFEST_OBJECT=$(aws s3 cp s3://$DEV_FARM_BUCKET/$MANIFEST_KEY -)
 echo $MANIFEST_OBJECT | jq .`

```

You'll see properties of the file `hash-jobattachments.txt` in the
 output such as the following:



```
{
     "hashAlg": "xxh128",
     "manifestVersion": "2023-03-03",
     "paths": [
     {
         "hash": "f60b8e7d0fabf7214ba0b6822e82e08b",
         "mtime": 1698785252554950,
         "path": "hash-jobattachments.txt",
         "size": 182
     }
     ],
     "totalSize": 182
 }
 
```

Your job will only have a single manifest object per task run, but in general
 it is possible to have more of objects per task run.
6. View content-addressible Amazon S3 storage output under the `Data`
 prefix.



```
 `FILE_HASH=$(echo $MANIFEST_OBJECT | jq -r .paths[0].hash)
 FILE_PATH=$(echo $MANIFEST_OBJECT | jq -r .paths[0].path)
 aws s3 cp s3://$DEV_FARM_BUCKET/JobAttachments/Data/$FILE_HASH -`
 
```

Output such as the following is shown:



```
eaa2df5d34b54be5ac34c56a24a8c237b8487231a607eaf530a04d76b89c9cd3  /tmp/openjd/session-123/assetroot-abc/simple_job/template.yaml
```

## Next steps


After learning how to submit jobs with attachments using the Deadline Cloud CLI, you can
 explore:



* [Submit with Deadline Cloud](submit-a-job.md "submit-a-job.md") to learn how to
 run jobs using an OpenJD bundle on your worker hosts.
* [Add a service-managed fleet to your developer farm
 in Deadline Cloud](service-managed-fleet.md "service-managed-fleet.md")
 to run your jobs on hosts managed by Deadline Cloud.
* [Clean up your farm resources in Deadline Cloud](cleaning-up.md "cleaning-up.md") to shut down the
 resources that you used for this tutorial.
