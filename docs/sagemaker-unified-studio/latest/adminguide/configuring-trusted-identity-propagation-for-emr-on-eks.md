# Configuring trusted identity propagation for Amazon EMR on EKS

Amazon EMR on EKS requires additional IAM permissions to enable trusted identity propagation.
You must attach the following inline IAM role policy to the IAM role created as the project user role.

###### Note

The project user role for an Amazon SageMaker Unified Studio project is named `datazone_usr_role_`{project_id}``.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TrustedIdentityPropagation",
            "Effect": "Allow",
            "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
            ],
            "Resource": "*"
        }
    ]
}
```
