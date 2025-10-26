# Derive path mapping
 rules from storage profiles

 Path mapping rules describe how paths should be remapped from the job to the path's
 actual location on a worker host. When a task is running on a worker, the storage profile
 from the job is compared to the storage profile of the worker's fleet to derive the path
 mapping rules for the task. 

 Deadline Cloud creates a mapping rule for each of the required file system locations in the
 queue's configuration. For example, a job submitted with the `WSAll` storage
 profile to queue `Q1` has the path mapping rules: 


* `FSComm`: `/shared/common -> /mnt/common`
* `FS1`: `/shared/projects/project1 -> /mnt/projects/project1`
 Deadline Cloud creates rules for the `FSComm` and `FS1` file system
 locations, but not the `FS2` file system location even though both the
 `WSAll` and `WorkerConfig` storage profiles define `FS2`.
 This is because queue `Q1`'s list of required file system locations is
 `["FSComm", "FS1"]`. 

 You can confirm the path mapping rules available to jobs submitted with a particular
 storage profile by submitting a job that prints out [Open Job Description's path mapping rules file](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run#path-mapping "https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run#path-mapping"), and then reading the session log
 after the job has completed: 


```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE1_ID to queue Q1's identifier
QUEUE1_ID=queue-`00112233445566778899aabbccddeeff`
# Change the value of WSALL_ID to the identifier of the WSALL storage profile
WSALL_ID=sp-`00112233445566778899aabbccddeeff`

aws deadline create-job --farm-id $FARM_ID --queue-id $QUEUE1_ID \
  --priority 50 \\
  --storage-profile-id $WSALL_ID \
  --template-type JSON --template \
  '{
    "specificationVersion": "jobtemplate-2023-09",
    "name": "DemoPathMapping",
    "steps": [
      {
        "name": "ShowPathMappingRules",
        "script": {
          "actions": {
            "onRun": {
              "command": "/bin/cat",
              "args": [ "{{Session.PathMappingRulesFile}}" ]
            }
          }
        }
      }
    ]
  }'
```
 If you use the [Deadline Cloud CLI](https://pypi.org/project/deadline/ "https://pypi.org/project/deadline/") to
 submit jobs, its configuration `settings.storage_profile_id` setting sets the
 storage profile that jobs submitted with the CLI will have. To submit jobs with the
 `WSAll` storage profile, set: 


```
deadline config set settings.storage_profile_id $WSALL_ID
```
 To run a customer-managed worker as though it is running in the sample infrastructure,
 follow the procedure in [Run the worker agent](../userguide/run-worker.md "../userguide/run-worker.md") in the
 *Deadline Cloud User Guide* to run a worker with AWS CloudShell. If you
 followed those instructions before, delete the `~/demoenv-logs` and
 `~/demoenv-persist` directories first. Also, set the values of the
 `DEV_FARM_ID` and `DEV_CMF_ID` environment variables that the
 directions reference as follows before doing so: 


```
DEV_FARM_ID=$FARM_ID
DEV_CMF_ID=$FLEET_ID
```
 After the job runs, you can see the path mapping rules in the job's log file: 


```
cat demoenv-logs/${QUEUE1_ID}/*.log
...
JJSON log results (see below)
...

```
The log contains mapping for both the `FS1` and `FSComm` file
 systems. Reformatted for readability, the log entry looks like this:


```
{
    "version": "pathmapping-1.0",
    "path_mapping_rules": [
        {
            "source_path_format": "POSIX",
            "source_path": "/shared/projects/project1",
            "destination_path": "/mnt/projects/project1"
        },
        {
            "source_path_format": "POSIX",
            "source_path": "/shared/common",
            "destination_path": "/mnt/common"
        }
    ]

```
 You can submit jobs with different storage profiles to see how the path mapping rules
 change.
