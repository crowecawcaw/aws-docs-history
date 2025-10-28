# Usage profiles and jobs

## Authoring jobs with usage profiles

While authoring jobs, the limits and defaults set in your usage profile will apply. Your profile will be assigned to the job upon save.

## Running jobs with usage profiles

When you start a job run, AWS Glue enforces the limits set in your caller's profile. If there is no direct caller, Glue will then apply the limits from the profile assigned to the job by its author.

###### Note

When a job is ran on a schedule (by AWS Glue workflows or AWS Glue triggers), the profile assigned to the job the author will apply.

When a job is ran by an external service (Step Functions, MWAA) or a `StartJobRun` API, the caller's profile limit will be enforced.

For AWS Glue workflows or AWS Glue triggers: pre-existing jobs need to be updated to save the new profile name so that profile's limits (min, max, and allowed workers) will be enforced at runtime for scheduled runs.

## Viewing a usage profile assigned for jobs

To view the profile assigned to your jobs (that will be used at runtime with scheduled AWS Glue workflows or AWS Glue triggers), you may look at the job **Details** tab. You may also look at the profile used in past runs in the job runs details tab.

## Updating or deleting a usage profile attached to a job

The profile assigned to a job is changed upon update. If the author isn't assigned a usage profile, any profile previously attached to the job will be removed from it.
