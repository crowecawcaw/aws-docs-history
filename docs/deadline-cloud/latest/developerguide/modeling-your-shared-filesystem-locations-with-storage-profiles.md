# Model shared
 file system locations with storage profiles

 A storage profile models the file system configuration of one of your host
 configurations. There are four different host configurations in the sample project infrastructure. In this
 example you create a separate storage profile for each. You can create a storage profile
 using any of the following:


* [CreateStorageProfile API](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateStorageProfile.html "https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateStorageProfile.html")
* [AWS::Deadline::StorageProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html") AWS CloudFormation resource
* [AWS
 console](../userguide/storage-shared.md#storage-profile "../userguide/storage-shared.md#storage-profile")
 A storage profile is made up of a list of file system locations that each tell Deadline Cloud
 the location and type of a file system location that is relevant for jobs submitted from or
 run on a host. A storage profile should only model the locations that are relevant for jobs.
 For example, the shared `FSCommon` location is located on workstation
 `WS1` at `S:\`, so the corresponding file system location is: 


```
{
    "name": "FSCommon",
    "path": "S:\\",
    "type": "SHARED"
}
```
 Use the following commands to create the storage profile for workstation configurations
 `WS1`, `WS2`, and `WS3` and the worker configuration
 `WorkerConfig` using the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html") in [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html"): 


```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`

aws deadline create-storage-profile --farm-id $FARM_ID \
  --display-name WSAll \
  --os-family LINUX \
  --file-system-locations \
  '[
      {"name": "FSCommon", "type":"SHARED", "path":"/shared/common"},
      {"name": "FS1", "type":"SHARED", "path":"/shared/projects/project1"},
      {"name": "FS2", "type":"SHARED", "path":"/shared/projects/project2"}
  ]'

aws deadline create-storage-profile --farm-id $FARM_ID \
  --display-name WS1 \
  --os-family WINDOWS \
  --file-system-locations \
  '[
      {"name": "FSCommon", "type":"SHARED", "path":"S:\\"},
      {"name": "FS1", "type":"SHARED", "path":"Z:\\"}
   ]'

aws deadline create-storage-profile --farm-id $FARM_ID \
  --display-name WS2 \
  --os-family MACOS \
  --file-system-locations \
  '[
      {"name": "FSCommon", "type":"SHARED", "path":"/Volumes/common"},
      {"name": "FS2", "type":"SHARED", "path":"/Volumes/projects/project2"}
  ]'

aws deadline create-storage-profile --farm-id $FARM_ID \
  --display-name WorkerCfg \
  --os-family LINUX \
  --file-system-locations \
  '[
      {"name": "FSCommon", "type":"SHARED", "path":"/mnt/common"},
      {"name": "FS1", "type":"SHARED", "path":"/mnt/projects/project1"},
      {"name": "FS2", "type":"SHARED", "path":"/mnt/projects/project2"}
  ]'
```
###### Note

You must refer to the file system locations in your storage profiles using the same
 values for the `name` property across all storage profiles in your farm. Deadline Cloud
 compares the names to determine that file system locations from different storage profiles
 are referring to the same location when generating path mapping rules.
