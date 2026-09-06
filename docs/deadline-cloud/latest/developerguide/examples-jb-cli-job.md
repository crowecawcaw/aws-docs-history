# Run a bash script on Deadline Cloud

The
[cli\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/cli_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/cli_job")
job bundle on the GitHub website submits a multi-line bash script to Deadline Cloud. The script job
parameter uses a multi-line edit control, and a data directory job
parameter lets you select a directory of data for the script to read from
and write to.

Submit the bundle with a data directory:

```
deadline bundle submit job_bundles/cli_job -p DataDir=`~/data_dir`
```

For a minimal starter that supplements the developer guide farm setup
walkthrough, see the
[simple\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/simple_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/simple_job")
bundle on the GitHub website.
