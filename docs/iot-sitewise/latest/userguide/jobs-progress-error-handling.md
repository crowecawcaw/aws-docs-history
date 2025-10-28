# Jobs progress tracking and error handling

A bulk process job takes time to process. Each job is processed in the order of AWS IoT SiteWise receiving the request.
It is processed one-at-a-time for each account. When a job completes, the next in queue automatically starts
processing. AWS IoT SiteWise resolves the jobs asynchronously and updates the status of each as it progresses. Each job has
a status field that contains the state of the resource and an error message, if applicable.

The state can be one of the following values:

- `VALIDATING` – Validating the job including the submitted file format, and its
  contents.
- `PENDING` – The job is in a queue. You can cancel jobs in this state from the AWS IoT SiteWise
  console, but all other states will continue until the end.
- `RUNNING` – Processing the job. It is creating and updating resources as defined by the
  import file, or exporting resources based on the chosen export job filters. If canceled, any resource imported
  by this job is not deleted. See [Review job progress and details (console)](review-job-progress.md#review-job-progress-console "review-job-progress.md#review-job-progress-console") for more information.
- `CANCELLING` – The job is actively being cancelled.
- `ERROR` – One or more resources failed to process. Check the detailed job report for
  more information. See [Inspect error details (console)](inspect-errors.md#inspect-errors-console "inspect-errors.md#inspect-errors-console") for more
  information.
- `COMPLETED` – Job completed without errors.
- `CANCELLED` – The job is cancelled and not queued. If you cancelled a `RUNNING` job,
  resources already imported by this job at the time of cancellation is not deleted from AWS IoT SiteWise.

###### Topics

- [Jobs progress tracking](review-job-progress.md "review-job-progress.md")
- [Inspect errors for AWS IoT SiteWise](inspect-errors.md "inspect-errors.md")
