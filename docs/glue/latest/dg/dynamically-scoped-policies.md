# Granting dynamically scoped policies for job execution

AWS Glue offers a powerful new capability: dynamic session policies for job executions. This feature allows you to specify custom,
fine-grained permissions for each job run without creating multiple IAM roles.

When you start a Glue job using the `StartJobRun` API, you can include an inline session policy. This policy temporarily
modifies the permissions of the job's execution role for the duration of that specific job run. It's similar to using
temporary credentials with the `AssumeRole` API in other AWS services.

- **Enhanced security**: You can limit job permissions to the minimum necessary for each run.
- **Simplified management**: Eliminates the need to create and maintain numerous IAM roles for different scenarios.
- **Flexibility**: You can be adjust permissions dynamically based on runtime parameters or tenant-specific needs.
- **Scalability**: This method excels in multi-tenant environments where you need to isolate resources between tenants.
  **Examples for granting dynamically scoped policies usage:**

The following examples demonstrate granting jobs _read_ and _write_ access only to a
specific Amazon S3 bucket path, where the path is dynamically determined by the job run ID. This illustrates how to implement granular,
execution-specific permissions for each job run.

**From CLI**

```
aws glue start-job-run \
    --job-name "your-job-name" \
    --execution-role-session-policy '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject"
                ],
                "Resource": [
                    "arn:aws:s3:::specific-bucket/${JobRunId}/*"
                ]
            }
        ]
    }'
```
