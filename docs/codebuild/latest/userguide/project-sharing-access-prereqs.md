# Access CodeBuild projects shared with

you

To access a shared project, a consumer's IAM role requires the
`BatchGetProjects` permission. You can attach the following policy to
their IAM role:

```
{
    "Effect": "Allow",
    "Resource": [
        "*"
    ],
    "Action": [
        "codebuild:BatchGetProjects"
    ]
}
```

For more information, see [Using
identity-based policies for AWS CodeBuild](auth-and-access-control-iam-identity-based-access-control.md "auth-and-access-control-iam-identity-based-access-control.md").
