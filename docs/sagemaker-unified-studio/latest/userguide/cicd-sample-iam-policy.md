# Sample IAM policy

The following policy grants the permissions required to deploy applications that include Glue, Athena, QuickSight, and SageMaker AI resources. Scope permissions to specific resources and accounts for production deployments.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket",
                "glue:*",
                "quicksight:*",
                "athena:*",
                "lakeformation:*",
                "logs:*",
                "iam:GetRole",
                "iam:PassRole",
                "sts:GetCallerIdentity",
                "datazone:GetProject",
                "datazone:GetDomain",
                "datazone:GetEnvironment",
                "datazone:ListConnections",
                "datazone:GetConnection",
                "datazone:SearchListings",
                "datazone:GetListing"
            ],
            "Resource": "*"
        }
    ]
}
```
