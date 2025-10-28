# Permissions required to view

compute logs in the CodePipeline console

To view the logs in the Commands action on the CodePipeline console, the console role
must have permissions. To view logs in the console, add the
`logs:GetLogEvents` permissions to the console role.

In the console role policy statement, scope down the permissions to the pipeline
level as shown in the following example.

```
{
    "Effect": "Allow",
    "Action": [
        "Action": "logs:GetLogEvents"
    ],
    "Resource": "arn:aws:logs:*:`YOUR_AWS_ACCOUNT_ID`:log-group:/aws/codepipeline/`YOUR_PIPELINE_NAME`:*"
}
```
