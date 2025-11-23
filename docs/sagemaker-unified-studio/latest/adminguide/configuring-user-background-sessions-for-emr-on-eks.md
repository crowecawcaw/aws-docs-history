# Configuring user background sessions for Amazon EMR on EKS

###### Warning

When user background sessions is enabled for Amazon EMR on EKS, Amazon SageMaker Unified Studio will not terminate interactive sessions.
All interactive sessions will be only terminated once all queries are completed and the compute session has timed out.

Amazon EMR on EKS requires additional IAM permissions to enable user background sessions.
You must attach the following inline IAM role policy to the IAM role created as the project user role.

###### Note

The project user role for an Amazon SageMaker Unified Studio project is named `datazone_usr_role_`{project_id}``.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "UserBackgroundSessions",
            "Effect": "Allow",
            "Action": [
                "sso:GetApplicationSessionConfiguration"
            ],
            "Resource": "*"
        }
    ]
}
```
