# How jobs find job attachment

input files

For a job to use the files that Deadline Cloud uploads to Amazon S3 using job attachments, your job
needs those files available through the file system on the worker hosts. When a [session](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run#sessions "https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run#sessions") for your job runs on a worker host, Deadline Cloud downloads the input files for
the job into a temporary directory on the worker host’s local drive and adds path mapping
rules for each of the job’s root paths to its file system location on the local drive.

For this example, start the Deadline Cloud worker agent in an AWS CloudShell tab. Let any
previously submitted jobs finish running, and then delete the job logs from the logs
directory:

```
rm -rf ~/devdemo-logs/queue-*
```

The following script modifies the job bundle to show all files in the session’s
temporary working directory and the contents of the path mapping rules file, and then
submits a job with the modified bundle:

```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE1_ID to queue Q1's identifier
QUEUE1_ID=queue-`00112233445566778899aabbccddeeff`
# Change the value of WSALL_ID to the identifier of the WSAll storage profile
WSALL_ID=sp-`00112233445566778899aabbccddeeff`

deadline config set settings.storage_profile_id $WSALL_ID

cat > ~/job_attachments_devguide/script.sh << EOF
#!/bin/bash

echo "Session working directory is: \$(pwd)"
echo
echo "Contents:"
find . -type f
echo
echo "Path mapping rules file: \$1"
jq . \$1
EOF

cat > ~/job_attachments_devguide/template.yaml << EOF
specificationVersion: jobtemplate-2023-09
name: "Job Attachments Explorer"
parameterDefinitions:
- name: ScriptFile
  type: PATH
  default: script.sh
  dataFlow: IN
  objectType: FILE
steps:
- name: Step
  script:
    actions:
      onRun:
        command: /bin/bash
        args:
        - "{{Param.ScriptFile}}"
        - "{{Session.PathMappingRulesFile}}"
EOF

deadline bundle submit --farm-id $FARM_ID --queue-id $QUEUE1_ID job_attachments_devguide/
```

You can look at the log of the job’s run after it has been run by the worker in your
AWS CloudShell environment:

```
cat demoenv-logs/queue-*/session*.log
```

The log shows that the first thing that occurs in the session is the two input files for
the job are downloaded to the worker:

```
2024-07-17 01:26:37,824 INFO ==============================================
2024-07-17 01:26:37,825 INFO --------- Job Attachments Download for Job
2024-07-17 01:26:37,825 INFO ==============================================
2024-07-17 01:26:37,825 INFO Syncing inputs using Job Attachments
2024-07-17 01:26:38,116 INFO Downloaded 142.0 B / 186.0 B of 2 files (Transfer rate: 0.0 B/s)
2024-07-17 01:26:38,174 INFO Downloaded 186.0 B / 186.0 B of 2 files (Transfer rate: 733.0 B/s)
2024-07-17 01:26:38,176 INFO Summary Statistics for file downloads:
Processed 2 files totaling 186.0 B.
Skipped re-processing 0 files totaling 0.0 B.
Total processing time of 0.09752 seconds at 1.91 KB/s.
```

Next is the output from `script.sh` run by the job:

- The input files uploaded when the job was submitted are located under a directory
  whose name begins with "assetroot" in the session’s temporary directory.
- The input files’ paths have been relocated relative to the "assetroot" directory
  instead of relative to the root path for the job’s input manifest
  (`"/"`).
- The path mapping rules file contains an additional rule that remaps
  `"/"` to the absolute path of the "assetroot" directory.
  For example:

```
2024-07-17 01:26:38,264 INFO Output:
2024-07-17 01:26:38,267 INFO Session working directory is: /sessions/session-`5b33f`
2024-07-17 01:26:38,267 INFO
2024-07-17 01:26:38,267 INFO Contents:
2024-07-17 01:26:38,269 INFO ./tmp_xdhbsdo.sh
2024-07-17 01:26:38,269 INFO ./tmpdi00052b.json
2024-07-17 01:26:38,269 INFO ./assetroot-`assetroot-3751a`/shared/projects/project2/file.txt
2024-07-17 01:26:38,269 INFO ./assetroot-`assetroot-3751a`/home/cloudshell-user/job_attachments_devguide/script.sh
2024-07-17 01:26:38,269 INFO
2024-07-17 01:26:38,270 INFO Path mapping rules file: /sessions/session-`5b33f`/tmpdi00052b.json
2024-07-17 01:26:38,282 INFO {
2024-07-17 01:26:38,282 INFO   "version": "pathmapping-1.0",
2024-07-17 01:26:38,282 INFO   "path_mapping_rules": [
2024-07-17 01:26:38,282 INFO     {
2024-07-17 01:26:38,282 INFO       "source_path_format": "POSIX",
2024-07-17 01:26:38,282 INFO       "source_path": "/shared/projects/project1",
2024-07-17 01:26:38,283 INFO       "destination_path": "/mnt/projects/project1"
2024-07-17 01:26:38,283 INFO     },
2024-07-17 01:26:38,283 INFO     {
2024-07-17 01:26:38,283 INFO       "source_path_format": "POSIX",
2024-07-17 01:26:38,283 INFO       "source_path": "/shared/common",
2024-07-17 01:26:38,283 INFO       "destination_path": "/mnt/common"
2024-07-17 01:26:38,283 INFO     },
2024-07-17 01:26:38,283 INFO     {
2024-07-17 01:26:38,283 INFO       "source_path_format": "POSIX",
2024-07-17 01:26:38,283 INFO       "source_path": "/",
2024-07-17 01:26:38,283 INFO       "destination_path": "/sessions/session-`5b33f`/assetroot-`assetroot-3751a`"
2024-07-17 01:26:38,283 INFO     }
2024-07-17 01:26:38,283 INFO   ]
2024-07-17 01:26:38,283 INFO }
```

###### Note

If the job you submit has multiple manifests with different root paths, there is a
different "assetroot"-named directory for each of the root paths.

If you need to reference the relocated file system location of one of your input files,
directories, or file system locations you can either process the path mapping rules file in
your job and perform the remapping yourself, or add a `PATH` type job parameter
to the job template in your job bundle and pass the value that you need to remap as the
value of that parameter. For example, the following example modifies the job bundle to have
one of these job parameters and then submits a job with the file system location
`/shared/projects/project2` as its value:

```
cat > ~/job_attachments_devguide/template.yaml << EOF
specificationVersion: jobtemplate-2023-09
name: "Job Attachments Explorer"
parameterDefinitions:
- name: LocationToRemap
  type: PATH
steps:
- name: Step
  script:
    actions:
      onRun:
        command: /bin/echo
        args:
        - "The location of {{RawParam.LocationToRemap}} in the session is {{Param.LocationToRemap}}"
EOF

deadline bundle submit --farm-id $FARM_ID --queue-id $QUEUE1_ID job_attachments_devguide/ \
  -p LocationToRemap=/shared/projects/project2
```

The log file for this job’s run contains its output:

```
2024-07-17 01:40:35,283 INFO Output:
2024-07-17 01:40:35,284 INFO The location of /shared/projects/project2 in the session is /sessions/session-`5b33f`/assetroot-`assetroot-3751a`
```
