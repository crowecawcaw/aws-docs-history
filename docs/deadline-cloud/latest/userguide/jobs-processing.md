# Processing Deadline Cloud jobs

When a job enters a queue, Deadline Cloud schedules it on one or more fleets associated with the
 queues. The fleet is chosen based on the capabilities configured for the fleet and the host
 requirements of a specific step. If a job has a requirement that can't be met by a any of the
 fleets associated with the queue, the job's status is set to "Not compatible" and the rest of
 the steps in the job are canceled.

Next, Deadline Cloud sends instructions to the workers to set up a session for the step. The
 software required for the step must be available on the worker instance for the job to run.
 The service opens sessions on multiple workers if the fleets scaling settings allow.

You can set up the software in an Amazon Machine Image (AMI), or your worker can load the software
 at runtime from a repository or package manager. You can use queue, job, or step environments
 to deploy the software that you prefer.

The Deadline Cloud service uses the OpenJD template to identify the steps required for the job, and
 the tasks required for each step. Some steps have dependencies on other steps, so Deadline Cloud
 determines the order to complete the steps. Then, Deadline Cloud sends the tasks for each step to
 workers to process. When a task is finished, the service sends another task in the same
 session, or the worker can start a new session.

After all tasks in each step are finished, the job is complete and the output is ready to
 download to your workstation. Even if the job didn't finish, the output from each step and
 task that finished is available to download.

###### Note

 Deadline Cloud removes jobs 120 days after they were submitted. When a job is removed, all of
 the steps and tasks associated with the job are also removed. If you need to re-run the job,
 submit the OpenJD template for the job again.
