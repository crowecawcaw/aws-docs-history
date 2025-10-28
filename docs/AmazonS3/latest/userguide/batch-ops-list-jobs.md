# Listing jobs

You can retrieve a list of your S3 Batch Operations jobs. The list includes jobs that
haven't yet finished and jobs that finished within the last 90 days. The job list
includes information for each job, such as its ID, description, priority, current
status, and the number of tasks that have succeeded and failed. You can filter your job
list by status. When you retrieve a job list through the console, you can also search
your jobs by description or ID and filter them by AWS Region.

## Get a list of

`Active` and `Complete` jobs

The following AWS CLI example gets a list of `Active` and
`Complete` jobs. To use this example, replace the
`user input placeholders` with your
own information.

```
aws s3control list-jobs \
    --region `us-west-2` \
    --account-id `account-id` \
    --job-statuses '["Active","Complete"]' \
    --max-results `20`
```

For more information and examples, see [list-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-jobs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-jobs.html") in the _AWS CLI Command Reference_.
