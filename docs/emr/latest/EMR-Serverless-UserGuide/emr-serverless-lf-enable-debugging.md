

# Debugging jobs and sessions
<a name="emr-serverless-lf-enable-debugging"></a>

**Note**  
With this feature, access **stdout** and **stderr** logs for the system profile workers that may contain sensitive, unfiltered information. The following permission should be used only for accessing non-production data. For applications created for use with production jobs, we strongly suggest that you add these permissions only to administrators or users with elevated data access.

Amazon EMR Serverless provides a self-debugging capability that lets you access the **stdout** and **stderr** logs of the system profile workers for a Lake Formation-enabled workload. To use it, set the **accessSystemProfileLogs** parameter to **true** on the dashboard API for your workload type:
+ For a Lake Formation-enabled batch job (EMR-7.3.0 and later), use the [GetDashboardForJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html) API.
+ For a Lake Formation-enabled Spark Connect session (`emr-7.14.0` and later, or `emr-spark-8.1.0` and later), use the [GetResourceDashboard](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetResourceDashboard.html) API with **resourceType** set to **SESSION**.

```
aws emr-serverless get-dashboard-for-job-run \
  --application-id {{application-id}}
  --job-run-id {{job-run-id}}
  --access-system-profile-logs
```

```
aws emr-serverless get-resource-dashboard \
  --application-id {{application-id}} \
  --resource-id {{session-id}} \
  --resource-type SESSION \
  --access-system-profile-logs
```

## Required permissions
<a name="emr-serverless-lf-enable-debugging-perms"></a>

The principal who wants to self-debug must have the following additional permissions. The `//` comments mark which action and resource ARN apply to a batch job versus a Spark Connect session — keep the entries for your workload type and remove the comments before you use the policy, because JSON does not support comments.

```
{
    "Sid": "AccessSystemProfileLogs",
    "Effect": "Allow",
    "Action": [
        "emr-serverless:GetDashboardForJobRun",    // batch job
        "emr-serverless:GetResourceDashboard",     // Spark Connect session
        "emr-serverless:AccessSystemProfileLogs",
        "glue:GetDatabases",
        "glue:SearchTables"
    ],
    "Resource": [
        "arn:aws:emr-serverless:region:account-id:/applications/{{applicationId}}/jobruns/{{jobid}}",        // batch job
        "arn:aws:emr-serverless:region:account-id:/applications/{{applicationId}}/sessions/{{sessionId}}",  // Spark Connect session
        "arn:aws:glue:region:account-id:catalog",
        "arn:aws:glue:region:account-id:database/*",
        "arn:aws:glue:region:account-id:table/*/*"
    ]
}
```

## Considerations
<a name="emr-serverless-lf-enable-debugging-considerations"></a>

System profile logs for debugging are visible for jobs and sessions that access databases or tables in Lake Formation within the same account as the job or session. They are not visible in the following scenarios:
+ If the data catalog managed using Lake Formation permissions has cross-account databases and tables
+ If the data catalog managed using Lake Formation permissions has resource links