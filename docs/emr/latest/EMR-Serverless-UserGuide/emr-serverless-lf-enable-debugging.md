# Debugging jobs

###### Note

With this feature, access **stdout** and **stderr** logs for the system profile workers that may
contain sensitive, unfiltered information. The following permission should be used only for accessing non-production data. For applications
created for use with production jobs, we strongly suggest that you add these permissions only to administrators or users
with elevated data access.

With EMR-7.3.0 and later, EMR Serverless is enabling self-debugging capability for Lake Formation-enabled batch jobs. To do so, use the new parameter **accessSystemProfileLogs** in
the [GetDashboardForJobRun](../../../emr-serverless/latest/APIReference/API_GetDashboardForJobRun.md "../../../emr-serverless/latest/APIReference/API_GetDashboardForJobRun.md") API. If **accessSystemProfileLogs** is set to **true**, you
can access the **stdout** and **stderr** logs
for the system profile workers, which can be used for debugging a Lake Formation-enabled EMR Serverless batch job.

```
aws emr-serverless get-dashboard-for-job-run \
  --application-id `application-id`
  --job-run-id `job-run-id`
  --access-system-profile-logs
```

## Required permissions

The principal who wants to debug Lake Formation-enabled batch jobs using **GetDashboardForJobRun** must have the following additional permissions:

```
{
    "Sid": "AccessSystemProfileLogs",
    "Effect": "Allow",
    "Action": [
        "emr-serverless:GetDashboardForJobRun",
        "emr-serverless:AccessSystemProfileLogs",
        "glue:GetDatabases",
        "glue:SearchTables"
    ],
    "Resource": [
        "arn:aws:emr-serverless:region:account-id:/applications/`applicationId`/jobruns/`jobid`",
        "arn:aws:glue:region:account-id:catalog",
        "arn:aws:glue:region:account-id:database/*",
        "arn:aws:glue:region:account-id:table/*/*"
    ]
}
```

## Considerations

System profile logs for debugging are visible for jobs that access databases or tables in Lake Formation within the same account as the job. They are not visible in the following scenarios:

- If the data catalog managed using Lake Formation permissions has cross-account databases and tables
- If the data catalog managed using Lake Formation permissions has resource links
