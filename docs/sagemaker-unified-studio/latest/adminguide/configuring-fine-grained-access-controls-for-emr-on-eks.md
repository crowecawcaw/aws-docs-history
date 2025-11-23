# Configuring fine-grained access controls for Amazon EMR on EKS

Amazon EMR on EKS requires additional IAM permissions to enable fine-grained access controls.
You must attach the following inline IAM role policy to the IAM role created as the project user role.

###### Note

The project user role for an Amazon SageMaker Unified Studio project is named `datazone_usr_role_`{project_id}``.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "FineGrainedAccessControls",
            "Effect": "Allow",
            "Action": [
                "emr-containers:CreateCertificate"
            ],
            "Resource": "*"
        }
    ]
}
```
