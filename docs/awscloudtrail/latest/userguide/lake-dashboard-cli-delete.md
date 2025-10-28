# Delete a dashboard with the AWS CLI

This section describes how to use the AWS CLI `delete-dashboard` command to delete a CloudTrail Lake dashboard.

To delete a dashboard, specify the `--dashboard-id` by providing the dashboard ARN, or the dashboard name.

```
aws cloudtrail delete-dashboard --dashboard-id arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash
```

There is no response if the operation is successful.

###### Note

You can't delete a dashboard if `--termination-protection-enabled` is set.
