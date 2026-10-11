

# Debugging fine-grained access control (FGAC) jobs and sessions
<a name="debugging-fgac-jobs-sessions"></a>

**Note**  
With this feature, you access the logs for the system profile workers, which may contain sensitive, unfiltered information. The following permissions should be used only for accessing non-production data. For jobs and sessions that access production data, we strongly suggest that you add these permissions only to administrators or users with elevated data access.

AWS Glue runs a Lake Formation-enabled job or session with two Spark resource profiles. The user profile runs the code that you supplied, and the system profile enforces Lake Formation policies. You can access the logs for the tasks that ran as the user profile at any time. For more information, see [Logging](security-lf-troubleshooting.md#security-lf-troubleshooting-logging).

To troubleshoot a failure that occurs in the system profile, use the `GetSystemLogsForJobRun` and `GetSystemLogsForSession` API operations. Each operation returns a `SystemLogsUrl` value, which is a presigned Amazon S3 URL that gives you the *system logs* — the logs that the system profile driver produced for that job run or session.

The presigned URL is valid for one hour. You can call these operations while the job run or session is still active.

## Prerequisites
<a name="debugging-fgac-prerequisites"></a>

System logs are available only for job runs and sessions that meet all of the following requirements:
+ You enabled fine-grained access control by setting the `--enable-lakeformation-fine-grained-access` parameter to `true`. For more information, see [Using AWS Glue with AWS Lake Formation for fine-grained access control](security-lf-enable.md).
+ The job or session uses AWS Glue version 5.0 or later.
+ The job or session is a Spark ETL or Spark streaming job or session. Ray jobs and Python shell jobs are not supported.

If the job run or session doesn't have fine-grained access control enabled, the operation returns an `InvalidInputException`.

## Required permissions
<a name="debugging-fgac-permissions"></a>

The principal that debugs a Lake Formation-enabled job run or session must have the following permissions. The `glue:GetDatabases` and `glue:SearchTables` permissions are both required, on all databases and tables in the account.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AccessSystemLogs",
            "Effect": "Allow",
            "Action": [
                "glue:GetJob",
                "glue:GetJobRun",
                "glue:GetSession",
                "glue:GetSystemLogsForJobRun",
                "glue:GetSystemLogsForSession",
                "glue:GetDatabases",
                "glue:SearchTables"
            ],
            "Resource": [
                "arn:aws:glue:{{region}}:{{account-id}}:catalog",
                "arn:aws:glue:{{region}}:{{account-id}}:database/*",
                "arn:aws:glue:{{region}}:{{account-id}}:table/*/*",
                "arn:aws:glue:{{region}}:{{account-id}}:job/*",
                "arn:aws:glue:{{region}}:{{account-id}}:session/*"
            ]
        }
    ]
}
```

If any of these permissions are missing, the operation returns an `AccessDeniedException` that names the missing action.

## Retrieving system logs
<a name="debugging-fgac-retrieving"></a>

To get the system logs for a job run, call `GetSystemLogsForJobRun` with the job name and the job run ID.

```
aws glue get-system-logs-for-job-run \
    --job-name {{my-fgac-job}} \
    --run-id {{jr_EXAMPLE1234567890}} \
    --region {{region}}
```

To get the system logs for a session, call `GetSystemLogsForSession` with the session ID.

```
aws glue get-system-logs-for-session \
    --id {{my-fgac-session}} \
    --region {{region}}
```

Both operations return a presigned Amazon S3 URL.

```
{
    "SystemLogsUrl": "{{presigned-url}}"
}
```

Open the URL to get the logs.

## Encrypting system logs with a customer managed key
<a name="debugging-fgac-encryption"></a>

To encrypt the system logs with a customer managed AWS KMS key, set the `--system-logs-kms-key-arn` parameter to the ARN of the key when you create the job or session.

The job or session runtime role must have an identity-based policy that grants `kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey`, `kms:ReEncryptFrom`, `kms:ReEncryptTo`, and `kms:DescribeKey` on the key. A key policy that grants these permissions is not sufficient on its own. Without the identity-based policy, the job run or session fails to start.

The principal that calls `GetSystemLogsForJobRun` or `GetSystemLogsForSession` must also have `kms:Decrypt`, `kms:DescribeKey`, and `kms:GenerateDataKey` on the key. Otherwise, the operation fails and reports that AWS KMS permissions are missing.

## Considerations
<a name="debugging-fgac-considerations"></a>
+ System logs are visible for jobs and sessions that access databases or tables in Lake Formation within the same account as the job or session. They are not visible if the Data Catalog that is managed with Lake Formation permissions has cross-account databases and tables, or has resource links.
+ After a job run or session ends, the system logs can take a few minutes to become available. If the logs are empty, call the operation again.
+ The presigned URL expires one hour after the operation returns it. Call the operation again to get a new URL.