

# Access report groups shared with you
<a name="report-groups-sharing-access-prereqs"></a>

To access a shared report group, a consumer's IAM role requires the `BatchGetReportGroups` permission. You can attach the following policy to their IAM role: 

```
{
    "Effect": "Allow",
    "Resource": [
        "*"
    ],
    "Action": [
        "codebuild:BatchGetReportGroups"
    ]
}
```

 For more information, see [Using identity-based policies for AWS CodeBuild](auth-and-access-control-iam-identity-based-access-control.md). 