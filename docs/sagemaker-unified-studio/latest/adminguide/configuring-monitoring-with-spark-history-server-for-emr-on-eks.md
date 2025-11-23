# Configuring monitoring with Spark History Server for Amazon EMR on EKS

Amazon EMR on EKS requires additional IAM permissions to enable monitoring with Spark History Server.
You must attach the following inline IAM role policy to the IAM role created as the project user role.

###### Note

The project user role for an Amazon SageMaker Unified Studio project is named `datazone_usr_role_`{project_id}``.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SparkHistoryServer",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePresignedDomainUrl"
            ],
            "Resource": "arn:aws:sagemaker:*:*:user-profile/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/AmazonDataZoneProject": "${aws:PrincipalTag/AmazonDataZoneProject}"
                }
            }
        }
    ]
}
```
