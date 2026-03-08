# Troubleshooting assessment runs

Following, you can find topics about troubleshooting issues with running assessment reports with AWS Database Migration Service.
These topics can help you to resolve common issues.

###### Topics

- [ResourceNotFoundFault when running StartReplicationTaskAssessment](#CHAP_Tasks.AssessmentReport.Troubleshooting.ResourceNotFoundFault "#CHAP_Tasks.AssessmentReport.Troubleshooting.ResourceNotFoundFault")

## ResourceNotFoundFault when running StartReplicationTaskAssessment

You may encounter the following exception when running the [StartReplicationTaskAssessment](../APIReference/API_StartReplicationTaskAssessment.md "../APIReference/API_StartReplicationTaskAssessment.md") action.

```
An error occurred (ResourceNotFoundFault) when calling the StartReplicationTaskAssessment operation: Task assessment has not been run or dms-access-for-tasks IAM Role not configured correctly
```

If you encounter this exception, create the **dms-access-for-tasks** role by doing the following:

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, for **Trusted entity type**,
   choose **Custom trust policy**.
5. Paste the following JSON in the editor, replacing the existing text.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "1",
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The preceding policy grants the `sts:AssumeRole` permission to AWS DMS. When you add the
**AmazonDMSRedshiftS3Role** policy, DMS can to create the S3 bucket in your account,
and put the data type assessment results into this S3 bucket. 6. Choose **Next**. 7. On the **Add permissions** page, search for and add the
**AmazonDMSRedshiftS3Role** policy. Choose **Next**. 8. On the **Name, review, and create** page, name the role
**dms-access-for-tasks**. Choose **Create role**.
