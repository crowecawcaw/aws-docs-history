# How Deadline Cloud chooses
 the files to upload

 The files and directories that job attachments considers for upload to Amazon S3 as inputs
 to your job are: 


* The values of all `PATH`-type job parameters defined in the job bundle’s
 job template with a `dataFlow` value of `IN` or
 `INOUT`.
* The files and directories listed as inputs in the job bundle’s asset references
 file.
 If you submit a job with no storage profile, all of the files considered for uploading
 are uploaded. If you submit a job with a storage profile, files are not uploaded to Amazon S3 if
 they are located in the storage profile’s `SHARED`-type file system locations
 that are also required file system locations for the queue. These locations are expected to
 be available on the worker hosts that run the job, so there is no need to upload them to S3. 

 In this example, you create `SHARED` file system locations in
 `WSAll` in your AWS CloudShell environment and then add files to those file
 system locations. Use the following command: 


```
# Change the value of WSALL_ID to the identifier of the WSAll storage profile
WSALL_ID=sp-`00112233445566778899aabbccddeeff`

sudo mkdir -p /shared/common /shared/projects/project1 /shared/projects/project2
sudo chown -R cloudshell-user:cloudshell-user /shared

for d in /shared/common /shared/projects/project1 /shared/projects/project2; do
  echo "File contents for $d" > ${d}/file.txt
done
```
 Next, add an asset references file to the job bundle that includes all the files that
 you created as inputs for the job. Use the following command: 


```
cat > ${HOME}/job_attachments_devguide/asset_references.yaml << EOF
assetReferences:
  inputs:
    filenames:
    - /shared/common/file.txt
    directories:
    - /shared/projects/project1
    - /shared/projects/project2
EOF
```
 Next, configure the Deadline Cloud CLI to submit jobs with the `WSAll` storage
 profile, and then submit the job bundle: 


```

# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE1_ID to queue Q1's identifier
QUEUE1_ID=queue-`00112233445566778899aabbccddeeff`
# Change the value of WSALL_ID to the identifier of the WSAll storage profile
WSALL_ID=sp-`00112233445566778899aabbccddeeff`

deadline config set settings.storage_profile_id $WSALL_ID

deadline bundle submit --farm-id $FARM_ID --queue-id $QUEUE1_ID job_attachments_devguide/
```
Deadline Cloud uploads two files to Amazon S3 when you submit the job. You can download the manifest
 objects for the job from S3 to see the uploaded files: 


```
for manifest in $( \
  aws deadline get-job --farm-id $FARM_ID --queue-id $QUEUE1_ID --job-id $JOB_ID \
    --query 'attachments.manifests[].inputManifestPath' \
    | jq -r '.[]'
); do
  echo "Manifest object: $manifest"
  aws s3 cp --quiet s3://$Q1_S3_BUCKET/DeadlineCloud/Manifests/$manifest /dev/stdout | jq .
done
```
 In this example, there is a single manifest file with the following contents: 


```
{
    "hashAlg": "xxh128",
    "manifestVersion": "2023-03-03",
    "paths": [
        {
            "hash": "87cb19095dd5d78fcaf56384ef0e6241",
            "mtime": 1721147454416085,
            "path": "home/cloudshell-user/job_attachments_devguide/script.sh",
            "size": 39
        },
        {
            "hash": "af5a605a3a4e86ce7be7ac5237b51b79",
            "mtime": 1721163773582362,
            "path": "shared/projects/project2/file.txt",
            "size": 44
        }
    ],
    "totalSize": 83
}
```
 Use the [GetJob operation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetJob.html "https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetJob.html") for the
 manifest to see that the `rootPath` is "/". 


```
aws deadline get-job --farm-id $FARM_ID --queue-id $QUEUE1_ID --job-id $JOB_ID --query 'attachments.manifests[*]'
```
 The root path for set of input files is always the longest common subpath of those
 files. If your job was submitted from Windows instead and there are input files with no
 common subpath because they were on different drives, you see a separate root path on each
 drive. The paths in a manifest are always relative to the root path of the manifest, so the
 input files that were uploaded are: 


* `/home/cloudshell-user/job_attachments_devguide/script.sh` – The script
 file in the job bundle.
* `/shared/projects/project2/file.txt` – The file in a
 `SHARED` file system location in the `WSAll` storage profile
 that is **not** in the list of required file system
 locations for queue `Q1`.
The files in file system locations `FSCommon`
 (`/shared/common/file.txt`) and `FS1`
 (`/shared/projects/project1/file.txt`) are not in the list. This is because
 those file system locations are `SHARED` in the `WSAll` storage
 profile and they both are in the list of required file system locations in queue
 `Q1`. 

You can see the file system locations considered `SHARED` for a job that is
 submitted with a particular storage profile with the [GetStorageProfileForQueue operation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStorageProfileForQueue.html "https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStorageProfileForQueue.html"). To query for storage profile
 `WSAll` for queue `Q1` use the following command: 


```
aws deadline get-storage-profile --farm-id $FARM_ID --storage-profile-id $WSALL_ID

aws deadline get-storage-profile-for-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID --storage-profile-id $WSALL_ID
```
