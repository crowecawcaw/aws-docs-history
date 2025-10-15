# Submit with Deadline Cloud

To run Deadline Cloud jobs on your worker hosts, you create and use an Open Job Description
 (OpenJD) job bundle to configure a job. The bundle configures the job, for example by
 specifying input files for a job and where to write the output of the job. This topic
 includes examples of ways that you can configure a job bundle.

Before you can follow the procedures in this section, you must complete the
 following:


* [Create a Deadline Cloud farm](create-a-farm.md "create-a-farm.md")
* [Run the Deadline Cloud worker agent](run-worker.md "run-worker.md")
To use AWS Deadline Cloud to run jobs, use the following procedures. Use the first AWS CloudShell tab to
 submit jobs to your developer farm. Use the second CloudShell tab to view the worker
 agent output. 

###### Topics

* [Submit the simple\_job
 sample](#submit-a-simplejob-sample "#submit-a-simplejob-sample")
* [Submit a simple\_job with a
 parameter](#submit-with-parameter "#submit-with-parameter")
* [Create a simple\_file\_job job bundle
 with file I/O](#create-job-bundle-with-file-io "#create-job-bundle-with-file-io")
* [Next steps](#submit-a-job-next "#submit-a-job-next")

## Submit the simple\_job
 sample


After you create a farm and run the worker agent, you can submit the
 simple\_job sample to Deadline Cloud. 


###### To submit the simple\_job sample to Deadline Cloud

1. Choose your first CloudShell tab.
2. Download the sample from GitHub.



```
`cd ~
git clone https://github.com/aws-deadline/deadline-cloud-samples.git`
```
3. Navigate to the job bundle samples directory.



```
`cd ~/deadline-cloud-samples/job_bundles/`

```
4. Submit the simple\_job sample.



```
`deadline bundle submit simple_job`

```
5. Choose your second CloudShell tab to view the logging output about calling
 `BatchGetJobEntities`, getting a session, and running a session
 action.



```
...
[2024-03-27 16:00:21,846][INFO    ] 🔷 Session.Starting 🔷 [session-053d77cef82648fe2] Starting new Session. [queue-3ba4ff683ff54db09b851a2ed8327d7b/job-d34cc98a6e234b6f82577940ab4f76c6]
[2024-03-27 16:00:21,853][INFO    ] 📤 API.Req 📤 [deadline:BatchGetJobEntity] resource={'farm-id': 'farm-3e24cfc9bbcd423e9c1b6754bc1', 'fleet-id': 'fleet-246ee60f46d44559b6cce010d05', 'worker-id': 'worker-75e0fce9c3c344a69bff57fcd83'} params={'identifiers': [{'jobDetails': {'jobId': 'job-d34cc98a6e234b6f82577940ab4'}}]} request_url=https://scheduling.deadline.us-west-2.amazonaws.com/2023-10-12/farms/farm-3e24cfc9bbcd423e /fleets/fleet-246ee60f46d44559b1 /workers/worker- 75e0fce9c3c344a69b /batchGetJobEntity
[2024-03-27 16:00:22,013][INFO    ] 📥 API.Resp 📥 [deadline:BatchGetJobEntity](200) params={'entities': [{'jobDetails': {'jobId': 'job-d34cc98a6e234b6f82577940ab6', 'jobRunAsUser': {'posix': {'user': 'job-user', 'group': 'job-group'}, 'runAs': 'QUEUE_CONFIGURED_USER'}, 'logGroupName': '/aws/deadline/farm-3e24cfc9bbcd423e9c1b6754bc1/queue-3ba4ff683ff54db09b851a2ed83', 'parameters': '*REDACTED*', 'schemaVersion': 'jobtemplate-2023-09'}}], 'errors': []} request_id=a3f55914-6470-439e-89e5-313f0c6
[2024-03-27 16:00:22,013][INFO    ] 🔷 Session.Add 🔷 [session-053d77cef82648fea9c69827182] Appended new SessionActions. (ActionIds: ['sessionaction-053d77cef82648fea9c69827182-0']) [queue-3ba4ff683ff54db09b851a2ed8b/job-d34cc98a6e234b6f82577940ab6]
[2024-03-27 16:00:22,014][WARNING ] 🔷 Session.User 🔷 [session-053d77cef82648fea9c69827182] Running as the Worker Agent's user. (User: cloudshell-user) [queue-3ba4ff683ff54db09b851a2ed8b/job-d34cc98a6e234b6f82577940ac6]
[2024-03-27 16:00:22,015][WARNING ] 🔷 Session.AWSCreds 🔷 [session-053d77cef82648fea9c69827182] AWS Credentials are not available: Queue has no IAM Role. [queue-3ba4ff683ff54db09b851a2ed8b/job-d34cc98a6e234b6f82577940ab6]
[2024-03-27 16:00:22,026][INFO    ] 🔷 Session.Logs 🔷 [session-053d77cef82648fea9c69827182] Logs streamed to: AWS CloudWatch Logs. (LogDestination: /aws/deadline/farm-3e24cfc9bbcd423e9c1b6754bc1/queue-3ba4ff683ff54db09b851a2ed83/session-053d77cef82648fea9c69827181) [queue-3ba4ff683ff54db09b851a2ed83/job-d34cc98a6e234b6f82577940ab4]
[2024-03-27 16:00:22,026][INFO    ] 🔷 Session.Logs 🔷 [session-053d77cef82648fea9c69827182] Logs streamed to: local file. (LogDestination: /home/cloudshell-user/demoenv-logs/queue-3ba4ff683ff54db09b851a2ed8b/session-053d77cef82648fea9c69827182.log) [queue-3ba4ff683ff54db09b851a2ed83/job-d34cc98a6e234b6f82577940ab4]
...
```

###### Note

Only the logging output from the worker agent is shown. There is a
 separate log for the session that runs the job.
6. Choose your first tab, then inspect the log files that the worker agent
 writes.


	1. Navigate to the worker agent logs directory and view its
	 contents.
	
	
	
	```
	`cd ~/demoenv-logs
	ls`
	
	```
	2. Print the first log file that the worker agent creates. 
	
	
	
	```
	`cat worker-agent-bootstrap.log`
	
	```
	
	This file contains worker agent output about how it called the Deadline Cloud
	 API to create a worker resource in your fleet, and then assumed the
	 fleet role.
	3. Print the log file output when the worker agent joins the fleet. 
	
	
	
	```
	`cat worker-agent.log`
	
	```
	
	This log contains outputs about all the actions that the worker agent
	 takes, but doesn't contain output about the queues it runs jobs from,
	 except for the IDs of those resources.
	4. Print the log files for each session in a directory that is named the
	 same as the queue resource id.
	
	
	
	```
	`cat $DEV_QUEUE_ID/session-*.log`
	
	```
	
	If the job is successful, the log file output will be similar to the
	 following:
	
	
	
	```
	`cat $DEV_QUEUE_ID/$(ls -t $DEV_QUEUE_ID | head -1)`
	                            
	2024-03-27 16:00:22,026 WARNING Session running with no AWS Credentials.
	2024-03-27 16:00:22,404 INFO 
	2024-03-27 16:00:22,405 INFO ==============================================
	2024-03-27 16:00:22,405 INFO --------- Running Task
	2024-03-27 16:00:22,405 INFO ==============================================
	2024-03-27 16:00:22,406 INFO ----------------------------------------------
	2024-03-27 16:00:22,406 INFO Phase: Setup
	2024-03-27 16:00:22,406 INFO ----------------------------------------------
	2024-03-27 16:00:22,406 INFO Writing embedded files for Task to disk.
	2024-03-27 16:00:22,406 INFO Mapping: Task.File.runScript -> /sessions/session-053d77cef82648fea9c698271812a/embedded_fileswa_gj55_/tmp2u9yqtsz
	2024-03-27 16:00:22,406 INFO Wrote: runScript -> /sessions/session-053d77cef82648fea9c698271812a/embedded_fileswa_gj55_/tmp2u9yqtsz
	2024-03-27 16:00:22,407 INFO ----------------------------------------------
	2024-03-27 16:00:22,407 INFO Phase: Running action
	2024-03-27 16:00:22,407 INFO ----------------------------------------------
	2024-03-27 16:00:22,407 INFO Running command /sessions/session-053d77cef82648fea9c698271812a/tmpzuzxpslm.sh
	2024-03-27 16:00:22,414 INFO Command started as pid: 471
	2024-03-27 16:00:22,415 INFO Output:
	2024-03-27 16:00:22,420 INFO Welcome to AWS Deadline Cloud!
	2024-03-27 16:00:22,571 INFO 
	2024-03-27 16:00:22,572 INFO ==============================================
	2024-03-27 16:00:22,572 INFO --------- Session Cleanup
	2024-03-27 16:00:22,572 INFO ==============================================
	2024-03-27 16:00:22,572 INFO Deleting working directory: /sessions/session-053d77cef82648fea9c698271812a
	
	```
7. Print information about the job. 



```
`deadline job get`

```

When you submit the job, the system saves it as the default so you don't have
 to enter the job ID.

## Submit a simple\_job with a
 parameter


You can submit jobs with parameters. In the following procedure, you edit the
 simple\_job template to include a custom message, submit the
 simple\_job, then print the session log file to view the message. 


###### To submit the simple\_job sample with a parameter

1. Select your first CloudShell tab, then navigate to the job bundle samples
 directory.



```
`cd ~/deadline-cloud-samples/job_bundles/`

```
2. Print the contents of the simple\_job template.



```
`cat simple_job/template.yaml`

```

The `parameterDefinitions` section with the `Message`
 parameter should look like the following:



```
parameterDefinitions:
- name: Message
  type: STRING
  default: Welcome to AWS Deadline Cloud!

```
3. Submit the simple\_job sample with a parameter value, then wait
 for the job to finish running.



```
`deadline bundle submit simple_job \
 -p "Message=Greetings from the developer getting started guide."`
```
4. To see the custom message, view the most recent session log file.



```
`cd ~/demoenv-logs
cat $DEV_QUEUE_ID/$(ls -t $DEV_QUEUE_ID | head -1)`
```

## Create a simple\_file\_job job bundle
 with file I/O


A render job needs to read the scene definition, render an image from it, and then
 save that image to an output file. You can simulate this action by making the job
 compute the hash of the input instead of rendering an image.


###### To create a simple\_file\_job job bundle with file I/O

1. Select your first CloudShell tab, then navigate to the job bundle samples
 directory.



```
`cd ~/deadline-cloud-samples/job_bundles/`
```
2. Make a copy of `simple_job` with the new name
 `simple_file_job`.



```
`cp -r simple_job simple_file_job`
```
3. Edit the job template as follows:


###### Note

We recommend that you use nano for these steps. If you
 prefer to use Vim, you must set its paste mode using
 `:set paste`.


	1. Open the template in a text editor.
	
	
	
	```
	`nano simple_file_job/template.yaml`
	```
	2. Add the following `type`, `objectType`, and
	 `dataFlow`
	`parameterDefinitions`. 
	
	
	
	```
	`- name: InFile
	 type: PATH
	 objectType: FILE
	 dataFlow: IN
	- name: OutFile
	 type: PATH
	 objectType: FILE
	 dataFlow: OUT`
	```
	3. Add the following `bash` script command to the end of the
	 file that reads from the input file and writes to the output file. 
	
	
	
	```
	  `# hash the input file, and write that to the output`
	        `sha256sum "{{Param.InFile}}" > "{{Param.OutFile}}"`
	```
	
	The updated `template.yaml` should exactly match the
	 following:
	
	
	
	```
	specificationVersion: 'jobtemplate-2023-09'
	name: Simple File Job Bundle Example
	parameterDefinitions:
	- name: Message
	  type: STRING
	  default: Welcome to AWS Deadline Cloud!
	- name: InFile
	  type: PATH
	  objectType: FILE
	  dataFlow: IN
	- name: OutFile
	  type: PATH
	  objectType: FILE
	  dataFlow: OUT
	steps:
	- name: WelcomeToDeadlineCloud
	  script:
	    actions:
	      onRun:
	        command: '{{Task.File.Run}}'
	    embeddedFiles:
	    - name: Run
	      type: TEXT
	      runnable: true
	      data: |
	        #!/usr/bin/env bash
	        echo "{{Param.Message}}"
	
	        # hash the input file, and write that to the output
	        sha256sum "{{Param.InFile}}" > "{{Param.OutFile}}"
	```
	
	###### Note
	
	If you want to adjust the spacing in the
	 `template.yaml`, make sure that you use spaces
	 instead of indentations.
	4. Save the file, and exit the text editor.
4. Provide parameter values for the input and output files to submit the
 simple\_file\_job.



```
`deadline bundle submit simple_file_job \
 -p "InFile=simple_job/template.yaml" \
 -p "OutFile=hash.txt"`
```
5. Print information about the job.



```
`deadline job get`
```



	* You will see output such as the following:
	
	
	
	```
	parameters:
	  Message:
	    string: Welcome to AWS Deadline Cloud!
	  InFile:
	    path: /local/home/cloudshell-user/BundleFiles/JobBundle-Examples/simple_job/template.yaml
	  OutFile:
	    path: /local/home/cloudshell-user/BundleFiles/JobBundle-Examples/hash.txt
	
	```
	* Although you only provided relative paths, the parameters have the
	 full path set. The AWS CLI joins the current working directory to any
	 paths that are provided as parameters when the paths have the type
	 `PATH`.
	* The worker agent running in the other terminal window picks up and
	 runs the job. This action creates the `hash.txt` file, which
	 you can view with the following command. 
	
	
	
	```
	`cat hash.txt`
	
	```
	
	This command will print output similar to the following.
	
	
	
	```
	eaa2df5d34b54be5ac34c56a24a8c237b8487231a607eaf530a04d76b89c9cd3 /local/home/cloudshell-user/BundleFiles/JobBundle-Examples/simple_job/template.yaml
	```

## Next steps


After learning how to submit simple jobs using the Deadline Cloud CLI, you can explore:



* [Submit jobs with job attachments in Deadline Cloud](run-jobs-job-attachments.md "run-jobs-job-attachments.md") to learn how to run jobs on hosts
 running different operating systems.
* [Add a service-managed fleet to your developer farm
 in Deadline Cloud](service-managed-fleet.md "service-managed-fleet.md")
 to run your jobs on hosts managed by Deadline Cloud.
* [Clean up your farm resources in Deadline Cloud](cleaning-up.md "cleaning-up.md") to shut down the
 resources that you used for this tutorial.
