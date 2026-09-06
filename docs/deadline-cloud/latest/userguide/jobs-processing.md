

# Processing Deadline Cloud jobs
<a name="jobs-processing"></a>

When a job enters a queue, Deadline Cloud schedules it on one or more fleets associated with the queue. Deadline Cloud chooses the fleet based on the capabilities configured for the fleet and the host requirements of the step. If a job has a requirement that no associated fleet can meet, Deadline Cloud sets the job's status to `NOT_COMPATIBLE` and cancels the remaining steps.

Workers process a job's tasks in sessions. A session sets up the environment for a step, runs one or more tasks, and then tears the environment down. The software required for the step must be available on the worker for the job to run. If the fleet's scaling settings allow, Deadline Cloud opens sessions on multiple workers at the same time.

After all tasks in each step are finished, the job is complete and the output is ready to download to your workstation. Even if the job didn't finish, the output from each step and task that finished is available to download.

**Note**  
 Deadline Cloud removes jobs 120 days after they were submitted. When a job is removed, all of the steps and tasks associated with the job are also removed. If you need to re-run the job, submit the OpenJD template for the job again.

For the details of scheduling – scheduling configurations for a queue, how fleet compatibility is determined, sessions, and step dependencies – see [Schedule jobs in Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-scheduling.html) in the *Deadline Cloud Developer Guide*.