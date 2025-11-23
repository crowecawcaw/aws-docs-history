# Accessing the Spark UI

The Apache Spark UIs present visual interfaces with detailed information about your running and completed Spark jobs. You can monitor and debug interactive sessions in Athena Spark using native Apache Spark UIs, where you can dive into job-specific metrics and information about event timelines, stages, tasks, and executors for each Spark job.

## Accessing the Spark UI

After you start an Athena Spark interactive session, you can view the real-time Spark UI for running sessions from the Amazon SageMaker AI Unified Studio notebooks or request a secure URL using the `GetResourceDashboard` API. For completed sessions, you can view the Spark History Server from the Amazon SageMaker AI Unified Studio notebooks, Amazon Athena Console or using the same API.

```
aws athena get-resource-dashboard \
  --region "REGION" \
  --session-id "SESSION_ID"
```

## Required permissions for accessing the Spark UI

Before you can access the Spark UI, include the following permissions in the permissions policy for the user or role.

```
{
    "Action": "athena:GetResourceDashboard",
    "Resource": "WORKGROUP",
    "Effect": "Allow"
}
```
